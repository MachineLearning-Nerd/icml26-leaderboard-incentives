# Audit report

## Result boundary

The previous live judged result is **5/12**. This repository records no new
judge score. The current scoped evidence package is:

| Claim | Result | Evidence boundary |
| --- | --- | --- |
| C1 | VERIFIED_SCOPED | Exact continuous no-PNE witness and negative control |
| C2 | FALSIFIED_SCOPED | Inverted PNE satisfying the written assumptions |
| C3 | FALSIFIED_SCOPED | Just-overtake antecedent holds while a PNE exists |
| C4 | FALSIFIED_SCOPED | Two nonzero PNE defeat aggregate uniqueness |
| C5 | FALSIFIED_SCOPED | Generalized scaling and linear-cost counterexample |
| C6 | BLOCKED | Source display reconstruction without raw empirical inputs |

The publication artifact gives a best-supported forecast of 10/12 for the
five answered claims. That number is explicitly a forecast and is not a new
live evaluation.

## Claim production

Claims 1–5 are produced by exact continuous-domain Z3 obligations, controls,
and independent readers. Claim 6 is produced by hash-pinned source download,
vector/PDF geometry reconstruction, endpoint-blind extrapolation, TeX anchor
consistency, and a dedicated falsification route. The raw empirical fit
remains unavailable, so no proxy is promoted to a rerun.

## Release integrity

The existing publication gate reports tests_passed=true and
publication_gate_passed=true. The historical subset has all 18 judged paths,
and the evaluator-blind second pass found complete six-claim visibility.
Those records are preserved as release provenance; this GitHub dossier does
not rewrite the historical Space.

## Limitations

Claims 2–5 contradict their written scopes under the registered assumptions,
but the paper authors may intend narrower conditions; those boundaries are
stated in each claim section. Claim 6 needs author Winogrande measurements and
fit parameters, or published CPU-feasible logits/checkpoints. The exact
theory verifier does not establish claims outside the contracts it encodes.
