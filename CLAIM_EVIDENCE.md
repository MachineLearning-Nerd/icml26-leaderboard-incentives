# Claim evidence ledger

Each verdict below comes from a committed claim contract, exact verifier,
independent checker or source reconstruction, and a deliberate control.
VERIFIED_SCOPED supports the stated continuous witness. FALSIFIED_SCOPED
records an assumption-satisfying contradiction to the written universal
claim. BLOCKED means the exact empirical input is unavailable.

| Claim | Verdict | Primary evidence | Production path |
| --- | --- | --- | --- |
| C1 | VERIFIED_SCOPED | outputs/exact_theory.json, evidence/claim_1 | repro/src/exact_theory.py and repro/src/check_exact_theory.py |
| C2 | FALSIFIED_SCOPED | outputs/exact_theory.json, evidence/claim_2 | repro/src/exact_theory.py and repro/src/check_exact_theory.py |
| C3 | FALSIFIED_SCOPED | outputs/exact_theory.json, evidence/claim_3 | repro/src/exact_theory.py and repro/src/check_exact_theory.py |
| C4 | FALSIFIED_SCOPED | outputs/exact_theory.json, evidence/claim_4 | repro/src/exact_theory.py and repro/src/check_exact_theory.py |
| C5 | FALSIFIED_SCOPED | outputs/exact_theory.json, evidence/claim_5 | repro/src/exact_theory.py and repro/src/check_exact_theory.py |
| C6 | BLOCKED | outputs/claim6_reconstruction.json, evidence/claim_6 | repro/src/claim6_figure.py and repro/src/check_claim6.py |

## C1 — General PNE nonexistence

The exact theory checker constructs a paper-admissible continuous follower
game with score 1 - exp(-(theta + e)), linear cost, rewards [1, 0], and
capabilities theta_high=1 and theta_low=0.5. Z3 checks every nonnegative
effort-pair case in the partition: high-capability winner above and at the
boundary, and low-capability winner in the middle and high regions. Every
profitable-deviation obligation is unsatisfiable, so no PNE exists in this
admitted game. A reward gap of 1/4 below catch-up effort 1/2 is retained as a
negative control where (0, 0) is a PNE.

This verifies the existential claim within the exact continuous witness. It
does not generalize the result to every game.

## C2 — Capability order at every PNE

The written universal claim is contradicted by cost max(e-1, 0)^2, equal
rewards, efforts [0, 0.75], the same saturating score, and capabilities
1 and 0.5. The lower-capability model strictly outranks the higher-capability
model at the admitted PNE. Z3 checks no profitable deviation, the inverted
ranking, and the flat-cost region. A strictly increasing linear-cost control
destroys the inverted equilibrium as intended.

## C3 — Just-overtake implication

The checker constructs efforts [1, 1], rewards [0.1, 0], cost
max(e-1, 0)^2, and the same score. The baseline just-overtake cost is zero,
so it is strictly below the positive reward gap 0.1, yet [1, 1] is a PNE.
The exact solver checks both players' deviations and the antecedent. Replacing
the flat segment with c(e)=e is a negative control that makes the profile
non-equilibrium.

## C4 — Tune-before-test aggregate uniqueness

For every nonnegative TbT level, the admitted flat-cost example has two
nonzero PNE profiles, [1, 0] and [1, 1]. The all-zero profile is not a PNE
because the lower-capability model can deviate to [0, 0.75]. The exact solver
checks both equilibrium profiles and the profitable deviation.

The narrower conditional Proposition 5.3 is not contradicted by this example:
its antecedent is never true. The audit therefore labels the aggregate
uniqueness claim falsified while preserving that logical distinction.

## C5 — Generalized scaling threshold

The exact generalized-logit family uses L(theta)=theta/(1+theta), U(theta)=1,
alpha(theta)=-log(1+theta), beta(theta)=1, gamma=1, linear cost, kappa=1,
lambda=2, reward gap 2, and theta in [0, 1]. It satisfies the displayed
scaling and cost conditions, but the catch-up effort infimum is one for every
TbT level and no finite TbT threshold can make cost catch up to the reward
gap. Z3 checks the catch-up identity, reward-versus-cost contradiction, and a
monotone-intercept stabilizing control.

This falsifies the written C1–C3 scope. If alpha is additionally required to
be nondecreasing, the counterexample is excluded; that is a separate
interpretation, not an assumption silently added to this verdict.

## C6 — Figure 1 Winogrande reconstruction

The exact displayed claim concerns Qwen2.5 models from 0.5B to 14B, LoRA
post-training from 0 to 3000 steps, and a minimum additional effort of
384668 steps. Four routes are recorded:

1. Direct vector-coordinate calibration gives 384667.5594951132.
2. Endpoint-blind degree-six extrapolation predicts 384648.7961 with the
   selected degree declared before checking the endpoint.
3. Three independent TeX anchors repeat the 3000 and 384668 quantities.
4. A dedicated falsification route finds no alternate curve or coordinate
   contradiction.

The source hash and Figure 1 geometry are reproducible, but the raw
Winogrande measurements, fit parameters, training code, and checkpoints are
absent. The result is BLOCKED rather than promoted from display reconstruction
to empirical rerun.
