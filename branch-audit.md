# Branch audit

This file records the branch normalization for the repository associated with
arXiv:2603.08371. Branch names describe the experiment or release role; the
former OpenResearch names are retained only as historical provenance.

## Mapping

| Clean branch | Former branch | Source tip before normalization | Scope |
| --- | --- | --- | --- |
| main | master | 447f6fe | Publication surface |
| historical/judged-baseline | orx/frozen-judged-baseline | 2b6e3ed | Frozen judged baseline |
| audit/exact-theorem-contracts | orx/exact-theorem-contracts | 5e2fa5c | Exact Claims 1–4 |
| audit/generalized-scaling | orx/full-generalized-scaling-proof | 846c80e | Claim 5 generalized-scaling counterexample |
| audit/figure1-reconstruction | orx/figure-1-source-reconstruction | 93d5371 | Claim 6 source reconstruction |
| release/evaluator-candidate | orx/evaluator-visible-release-candidate | 8f8494d | Cumulative evaluator-visible release |
| release/publication-gate | orx/publication-gate-and-canonical-release | c6a0bf6 | Canonical publication gate |
| release/publication-20260728 | publication/release-20260728 | 447f6fe | Historical publication snapshot |

The former branch names were deleted after the clean refs were published.

## Claim evidence locations

| Claim | Primary implementation | Raw evidence | Independent check |
| --- | --- | --- | --- |
| 1 | repro/src/exact_theory.py | outputs/exact_theory.json | repro/src/check_exact_theory.py |
| 2 | repro/src/exact_theory.py | outputs/exact_theory.json | repro/src/check_exact_theory.py |
| 3 | repro/src/exact_theory.py | outputs/exact_theory.json | repro/src/check_exact_theory.py |
| 4 | repro/src/exact_theory.py | outputs/exact_theory.json | repro/src/check_exact_theory.py |
| 5 | repro/src/exact_theory.py | outputs/exact_theory.json | repro/src/check_exact_theory.py |
| 6 | repro/src/claim6_figure.py | outputs/claim6_reconstruction.json | repro/src/check_claim6.py |

Every claim directory under evidence contains the claim contract, exact
command, method, raw output, checker output, negative control, and limitations.

## Verification contract

The normalized repository must satisfy all of the following:

1. Every published branch is one of the clean names in the mapping above.
2. The default branch is main.
3. Every commit author and committer is
   MachineLearning-Nerd <MachineLearning-Nerd@users.noreply.github.com>.
4. Active README, report, notebook, and tutorial links point to the renamed
   repository and clean branch names.
5. The fixed command remains
   uv run --frozen python repro/src/verify.py.
6. Claim statuses remain VERIFIED for Claim 1, FALSIFIED for Claims 2–5, and
   BLOCKED for Claim 6.

The historical branch and immutable evidence references are not rewritten as
scientific content; they are described as historical provenance.
