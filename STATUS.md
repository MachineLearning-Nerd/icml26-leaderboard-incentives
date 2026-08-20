# Reproduction status

## Overall verdict

**PARTIAL_C1_VERIFIED_C2_C3_C4_C5_FALSIFIED_C6_BLOCKED_HISTORICAL_SCORE_5_OF_12_NO_CURRENT_SCORE**

This repository is an independent, claim-by-claim audit of
[*Leaderboard Incentives: Model Rankings under Strategic Post-Training*](https://arxiv.org/abs/2603.08371).
It is not the authors' official implementation.

- Historical live judge result: **5/12**.
- The current evidence package does not claim a new judge score.
- Claims 1–5 have exact continuous-domain evidence; Claim 6 is blocked by
  missing empirical training artifacts.
- No author endorsement is claimed.

| Claim | Status | How the result is produced | Boundary |
| --- | --- | --- | --- |
| C1 nonexistence of PNE in general | VERIFIED_SCOPED | Z3 checks an exhaustive continuous effort-pair partition and a PNE negative control | Exact admitted game witness; not a proof for every game |
| C2 capability-order preservation | FALSIFIED_SCOPED | Exact inverted PNE under the written score, reward, cost, and tie assumptions | Contradicts the universal written claim |
| C3 just-overtake no-PNE implication | FALSIFIED_SCOPED | Exact PNE whose reward gap exceeds the baseline just-overtake cost | Isolates the missing strictness step |
| C4 tune-before-test uniqueness | FALSIFIED_SCOPED | Two nonzero PNE persist for every nonnegative TbT level | Aggregate uniqueness is contradicted; Proposition 5.3 is separately preserved |
| C5 generalized scaling threshold | FALSIFIED_SCOPED | Generalized-logit family satisfies the displayed conditions but has no finite stabilizing threshold | An additional monotone-alpha interpretation would be a different contract |
| C6 Figure 1 Winogrande steps | BLOCKED | Four source reconstruction and falsification routes reproduce 384667.5595, rounding to 384668 | Raw measurements, fit parameters, code, and checkpoints are unavailable |

See [CLAIM_EVIDENCE.md](CLAIM_EVIDENCE.md) for the production path of each
claim, [SOURCE_AUDIT.md](SOURCE_AUDIT.md) for paper provenance, and
[ENVIRONMENT.md](ENVIRONMENT.md) for the locked runtime.
