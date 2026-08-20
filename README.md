# Leaderboard Incentives — reproduction audit

This repository is an independent, claim-by-claim reproduction audit for
[Leaderboard Incentives: Model Rankings under Strategic Post-Training](https://arxiv.org/abs/2603.08371).
It is one entry in MachineLearning-Nerd’s ICML 2026 reproduction collection.

The standardized dossier is available in [STATUS.md](STATUS.md),
[CLAIM_EVIDENCE.md](CLAIM_EVIDENCE.md), [SOURCE_AUDIT.md](SOURCE_AUDIT.md),
[ENVIRONMENT.md](ENVIRONMENT.md), [REPORT.md](REPORT.md),
[CITATION.cff](CITATION.cff), [AUTHOR_THANK_YOU.md](AUTHOR_THANK_YOU.md),
[claims.json](claims.json), [reproduction_verdicts.json](reproduction_verdicts.json),
and [verify_final.py](verify_final.py).

The paper studies benchmark design as a Stackelberg game: model developers
strategically spend post-training effort to improve benchmark scores, while a
benchmark designer chooses the evaluation protocol. The paper proves that
ordinary evaluation can create unstable incentives and studies
tune-before-test (TbT) as a protocol intended to recover model-quality
rankings.

## Paper

- Title: Leaderboard Incentives: Model Rankings under Strategic Post-Training
- Authors: Yatong Chen, Guanhua Zhang, and Moritz Hardt
- Source: [arXiv:2603.08371](https://arxiv.org/abs/2603.08371)
- Submitted: 9 March 2026
- Associated tutorial: [leaderboard_incentives_reproduction.py](leaderboard_incentives_reproduction.py)

The audit separates what the paper states from what the available source,
assumptions, and evidence can establish. A falsified result means that an
assumption-satisfying counterexample was found for the written claim. A
blocked result means that the available paper bundle does not contain enough
data or artifacts for an authorized independent rerun.

## Reproduction status

The exact verifier reports Claim 1 as VERIFIED, Claims 2–5 as FALSIFIED under
their written scope, and Claim 6 as BLOCKED. The publication artifact records
five claims with evidence and a 10-point best-supported total, while the
previous live judge score was 5/12. The 10-point value is an evidence-package
forecast, not a new live-judge result.

## Claim-to-evidence ledger

| Claim | What the paper says | How this audit produces evidence | Result |
| --- | --- | --- | --- |
| 1 | A pure Nash equilibrium (PNE) generally need not exist. | The exact theory checker constructs an admitted continuous game and verifies that every effort profile has a profitable deviation. | VERIFIED |
| 2 | Every PNE preserves capability order. | The checker constructs the admitted PNE [0, 3/4], where the weaker model strictly outranks the stronger one. | FALSIFIED |
| 3 | A just-overtake inequality implies that no PNE exists. | The checker constructs the admitted PNE [1, 1] while the baseline just-overtake cost is 0 < 0.1. | FALSIFIED |
| 4 | TbT produces a unique stable equilibrium. | Two nonzero PNE persist for every nonnegative TbT level in the permitted flat-cost example. The narrower conditional Proposition 5.3 is reported separately. | FALSIFIED for aggregate uniqueness |
| 5 | A stabilizing threshold exists and is polynomially bounded. | An exact generalized-logit family satisfying the displayed conditions keeps the catch-up effort above 1 for every TbT level; a stricter monotone-alpha control stabilizes as expected. | FALSIFIED under the written C1–C3 scope |
| 6 | Figure 1 implies 384,668 additional Winogrande steps at TbT 3,000. | The hashed arXiv source is downloaded and the published vector/PDF geometry reconstructs 384,667.5595, which rounds to 384,668. The raw trajectory and fit parameters are absent. | BLOCKED |

The primary evidence is in
[outputs/exact_theory.json](outputs/exact_theory.json) and
[outputs/claim6_reconstruction.json](outputs/claim6_reconstruction.json).
The per-claim contracts, controls, checkers, and limitations are under
[evidence](evidence).

## How to reproduce

The fixed CPU command used by the experiment branches is:

~~~bash
uv sync --frozen
uv run --frozen python repro/src/verify.py
~~~

The verifier retains the historical finite sweeps as regression checks, then
runs exact continuous-domain obligations, writes JSON evidence, validates that
evidence with independent readers, downloads the hash-pinned arXiv source, and
reconstructs Figure 1. It exits nonzero when a proof obligation, source hash,
checker, or negative control fails.

To open the self-contained marimo tutorial:

~~~bash
uv run marimo edit leaderboard_incentives_reproduction.py
uv run marimo run leaderboard_incentives_reproduction.py
~~~

No GPU or Hugging Face compute was used. The formal and reconstruction routes
were designed to run on local CPU.

## Branch map

The experiment branches now use purpose-driven names:

| Clean branch | Purpose |
| --- | --- |
| main | Publication surface and current documentation |
| historical/judged-baseline | Frozen judged artifact and environment/source provenance |
| audit/exact-theorem-contracts | Exact contracts and counterexamples for Claims 1–4 |
| audit/generalized-scaling | Generalized-scaling analysis for Claim 5 |
| audit/figure1-reconstruction | Hash-pinned Figure 1 reconstruction and Claim 6 routes |
| release/evaluator-candidate | Cumulative evaluator-visible evidence package |
| release/publication-gate | Canonical per-claim pages and publication gate |
| release/publication-20260728 | Historical publication snapshot |

The branch-level mapping and verification record is maintained in
[branch-audit.md](branch-audit.md).

## Repository contents

- [repro/src/exact_theory.py](repro/src/exact_theory.py): exact theory checks
  for Claims 1–5.
- [repro/src/claim6_figure.py](repro/src/claim6_figure.py): source and Figure 1
  reconstruction for Claim 6.
- [repro/src/check_exact_theory.py](repro/src/check_exact_theory.py) and
  [repro/src/check_claim6.py](repro/src/check_claim6.py): independent checkers.
- [evidence/claim_1](evidence/claim_1) through
  [evidence/claim_6](evidence/claim_6): contracts, raw outputs, controls, and
  limitations.
- [reports/reproduction/report.md](reports/reproduction/report.md): illustrated
  claim-by-claim report.
- [reports/reproduction/release-report.md](reports/reproduction/release-report.md):
  evaluator-facing release record.
- [publication_gate.json](publication_gate.json): machine-readable gate result.
- [pyproject.toml](pyproject.toml) and [uv.lock](uv.lock): pinned environment.

## Citation

~~~bibtex
@article{chen2026leaderboard,
  title         = {Leaderboard Incentives: Model Rankings under Strategic Post-Training},
  author        = {Yatong Chen and Guanhua Zhang and Moritz Hardt},
  journal       = {arXiv preprint arXiv:2603.08371},
  year          = {2026},
  doi           = {10.48550/arXiv.2603.08371}
}
~~~

## Thank you

Thank you to Yatong Chen, Guanhua Zhang, and Moritz Hardt for making the paper
and its source available. The paper’s clear game-theoretic framing made it
possible to turn broad claims into explicit contracts, exact counterexamples,
controls, and reproducible evidence. This repository is an independent
reproduction audit and is not an official artifact from the authors.

## Scope and limitations

This audit evaluates the written mathematical and empirical claims against the
available arXiv source and repository artifacts. Claims 2–5 are sensitive to
the exact assumptions; Claim 6 cannot be independently rerun without the
authors’ Winogrande measurements, fit parameters, training code, or equivalent
published checkpoints/logits. Please read the linked raw evidence before
interpreting the status labels as statements about the authors’ intent or
implementation.
