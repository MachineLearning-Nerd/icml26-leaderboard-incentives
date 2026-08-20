# Environment and reproduction contract

## Fixed command

~~~bash
uv sync --frozen
uv run --frozen python repro/src/verify.py
~~~

The verifier writes the exact theory, Figure 1 reconstruction, and cumulative
verdict outputs, then runs their independent readers and negative controls.

## Pinned environment

- Python: 3.12
- Z3 Solver: 4.15 or newer under uv.lock
- NumPy: 2.2 or newer under uv.lock
- SciPy: 1.15 or newer under uv.lock
- PyMuPDF: 1.26 or newer under uv.lock
- Backend: local CPU
- GPU: none
- Recorded formal and reconstruction runs: under five minutes, one estimated
  CPU core, no Hugging Face compute

No substitute Winogrande data, checkpoints, logits, or training pipeline is
introduced for Claim 6. The exact source vector and Figure 1 geometry are
hash-pinned and independently checked.

## Evidence locations

- Claim contracts and raw records: evidence/claim_1 through evidence/claim_6
- Exact cumulative outputs: outputs/
- Primary implementations: repro/src/
- Publication gate: publication_gate.json
- Historical release checks: reports/reproduction/
