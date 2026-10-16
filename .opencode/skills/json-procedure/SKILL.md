---
name: json-procedure
description: Generate independently evaluated disease JSON step contracts
compatibility: opencode
---

# json-procedure

Read pipeline/example-procedure.json and scripts/interpret_procedure.py. For each disease set entrypoint, modality-specific steps, dependency DAG, typed input/output keys, model registry and per-step evaluation dataset/metrics/status. Validate static DAG and block unverified model steps. Do not confuse interpretation with model execution.

## Output
Record inputs, citations, artifact SHA, test commands, numerical results only when actually measured, safety limitations and next unresolved checks. Never mark unexecuted tests as passed.
