# Source audit

## Paper

- Title: *Leaderboard Incentives: Model Rankings under Strategic Post-Training*
- Authors: Yatong Chen, Guanhua Zhang, and Moritz Hardt
- Source: [arXiv:2603.08371](https://arxiv.org/abs/2603.08371)
- Audited version: arXiv:2603.08371v1
- HTML: https://ar5iv.labs.arxiv.org/html/2603.08371
- Retrieved UTC: 2026-07-28
- HTML SHA-256:
  3779b433938d92d88d9522ccef506645139eccaf7a2fb5d3f12a5518f8c4cf51
- PDF SHA-256:
  fba1d7c5d9bb365aba7e2f7b044ba62276d30858b24b71e5aeebea284f68ba74
- TeX source SHA-256:
  9f6d8668713011bee867b6c83a8e88a5f6b9cec201cc1806a30c891b11106ae8

This repository is an independent reproduction audit. It does not claim to
be maintained by, endorsed by, or identical to the authors' implementation.

## Paper anchors used

- Assumptions 4.1–4.2: cost, score, and capability monotonicity contracts
- Proposition 4.3: capability-order preservation
- Theorem 4.6: all-zero PNE and just-overtake implication
- Proposition 5.3: conditional tune-before-test monotonicity
- Proposition 5.6: generalized scaling and stabilizing threshold
- Figure 1 and Section 5.1: Winogrande model and 384668-step display

The theorem claims are universally quantified. Finite grid sweeps are retained
as toy regressions, while the exact continuous contracts and controls carry
the current verdicts.

## Historical evaluation provenance

- Historical evaluator Space: DineshAI/r6wfuAKmVb
- Historical live score: **5/12**
- Current score claim: false
- Current evidence forecast: 10/12 best-supported total, not a judge result

The publication gate and historical subset checks remain committed under
reports/reproduction/. They document the evaluator-visible artifact without
changing the historical score claim.
