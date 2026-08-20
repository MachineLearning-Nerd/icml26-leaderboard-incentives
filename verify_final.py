from __future__ import annotations

import json
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parent
CANONICAL_NAME = "MachineLearning-Nerd"
CANONICAL_EMAIL = "MachineLearning-Nerd@users.noreply.github.com"
EXPECTED_BRANCHES = {
    "main",
    "historical/judged-baseline",
    "audit/exact-theorem-contracts",
    "audit/generalized-scaling",
    "audit/figure1-reconstruction",
    "release/evaluator-candidate",
    "release/publication-gate",
    "release/publication-20260728",
}
EXPECTED_COMMITS = 31
EXPECTED_STATUSES = {
    "C1": "VERIFIED_SCOPED",
    "C2": "FALSIFIED_SCOPED",
    "C3": "FALSIFIED_SCOPED",
    "C4": "FALSIFIED_SCOPED",
    "C5": "FALSIFIED_SCOPED",
    "C6": "BLOCKED",
}
EXPECTED_OVERALL = (
    "PARTIAL_C1_VERIFIED_C2_C3_C4_C5_FALSIFIED_C6_BLOCKED_"
    "HISTORICAL_SCORE_5_OF_12_NO_CURRENT_SCORE"
)


def run(*args: str) -> str:
    return subprocess.check_output(
        ["git", *args],
        cwd=ROOT,
        text=True,
    ).strip()


def read_json(relative_path: str) -> dict:
    return json.loads((ROOT / relative_path).read_text())


def published_branches() -> set[str]:
    try:
        output = run("ls-remote", "--heads", "origin")
    except subprocess.CalledProcessError:
        output = run("for-each-ref", "--format=%(refname:short)", "refs/heads/")
        return {line for line in output.splitlines() if line}
    return {
        line.split("refs/heads/", 1)[1]
        for line in output.splitlines()
        if "refs/heads/" in line
    }


def require(condition: bool, message: str) -> None:
    if not condition:
        raise SystemExit(f"VERIFY_FAILED: {message}")


def main() -> None:
    claims = read_json("claims.json")
    verdicts = read_json("reproduction_verdicts.json")
    manifest = read_json("EVIDENCE_MANIFEST.json")
    state = read_json("AUTONOMOUS_STATE.json")
    raw_verdict = read_json("outputs/verdict.json")
    exact_theory = read_json("outputs/exact_theory.json")
    claim6 = read_json("outputs/claim6_reconstruction.json")
    gate = read_json("publication_gate.json")

    branches = published_branches()
    require(branches == EXPECTED_BRANCHES, f"branch set is {sorted(branches)}")
    require("orx" not in " ".join(branches), "legacy orx branch remains")
    require(run("symbolic-ref", "--short", "HEAD") == "main", "main is not checked out")
    require(int(run("rev-list", "--count", "--all")) == EXPECTED_COMMITS, "reachable commit count changed")

    identities = run("log", "--all", "--format=%an%x09%ae%x09%cn%x09%ce").splitlines()
    require(identities, "no commits found")
    require(
        all(
            line == "\t".join(
                [CANONICAL_NAME, CANONICAL_EMAIL, CANONICAL_NAME, CANONICAL_EMAIL]
            )
            for line in identities
        ),
        "a commit does not use the canonical identity",
    )

    require(claims["overall_status"] == EXPECTED_OVERALL, "claims overall status mismatch")
    require(verdicts["overall_status"] == EXPECTED_OVERALL, "verdict overall status mismatch")
    require(state["overall_status"] == EXPECTED_OVERALL, "state overall status mismatch")
    require(claims["current_score_claim"] is False, "claims file makes a current score claim")
    require(verdicts["historical_evaluation"]["current_score_claim"] is False, "verdicts make a current score claim")
    require(state["current_score_claim"] is False, "state makes a current score claim")
    require(verdicts["publication"]["publication_allowed"] is False, "publication gate is overstated")

    claim_statuses = {claim["id"]: claim["status"] for claim in claims["claims"]}
    require(claim_statuses == EXPECTED_STATUSES, f"claim statuses are {claim_statuses}")
    require(
        {claim_id: item["status"] for claim_id, item in verdicts["claims"].items()}
        == EXPECTED_STATUSES,
        "machine-readable verdict statuses mismatch",
    )
    require(
        {claim_id: item["status"] for claim_id, item in raw_verdict["claims"].items()}
        == {key.lower(): value.removesuffix("_SCOPED") for key, value in EXPECTED_STATUSES.items()},
        "raw verifier statuses mismatch",
    )

    require(exact_theory["claims"]["c1"]["status"] == "VERIFIED", "C1 exact status mismatch")
    for claim_id in ("c2", "c3", "c4", "c5"):
        require(exact_theory["claims"][claim_id]["status"] == "FALSIFIED", f"{claim_id} exact status mismatch")
    require(claim6["status"] == "BLOCKED", "C6 reconstruction status mismatch")
    require(claim6["raw_training_data_present_in_source"] is False, "C6 raw-data boundary changed")
    require(abs(claim6["observed_source_reconstruction"] - 384667.5594951132) < 1e-9, "C6 reconstruction changed")
    require(claim6["paper_value"] == 384668, "C6 paper value changed")

    require(gate["tests_passed"] is True, "publication tests are not passed")
    require(gate["publication_gate_passed"] is True, "publication gate artifact is not passed")
    require(gate["claims_verified"] == 5 and gate["claims_total"] == 6, "publication claim counts changed")
    require(gate["points"] == 10, "publication forecast changed")

    required_paths = manifest["required_paths"]
    missing = [path for path in required_paths if not (ROOT / path).exists()]
    require(not missing, f"manifest paths missing: {missing}")
    require(state["canonical_identity"]["email"] == CANONICAL_EMAIL, "state identity mismatch")

    readme = (ROOT / "README.md").read_text()
    for required_text in (
        "arXiv:2603.08371",
        "Thank you",
        "STATUS.md",
        "CLAIM_EVIDENCE.md",
        "not a new live-judge result",
    ):
        require(required_text in readme, f"README is missing {required_text!r}")

    branch_audit = (ROOT / "branch-audit.md").read_text()
    require(f"{CANONICAL_NAME} <{CANONICAL_EMAIL}>" in branch_audit, "branch audit identity is not canonical")

    print(
        "FINAL_AUDIT=VERIFIED "
        "branches=8 commits=31 "
        "claims=C1_verified_scoped,C2:C3:C4:C5_falsified_scoped,C6_blocked "
        "historical_score=5/12 current_score_claim=false publication_allowed=false"
    )


if __name__ == "__main__":
    main()
