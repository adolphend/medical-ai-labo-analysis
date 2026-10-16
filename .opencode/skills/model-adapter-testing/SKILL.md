---
name: model-adapter-testing
description: Evaluate exact pretrained models with independent clinical task metrics
compatibility: opencode
---

# model-adapter-testing

Read research/imaging/model-integration-registry.md, evaluation/protocol.md and disease/procedure.json. Pin repo version, checkpoint hash, input preprocessing and dataset DVC version. Use scripts/evaluate_predictions.py for binary and scripts/evaluate_context.py for context fixtures; implement separate segmentation, detection or regression metrics only with tests. Measure CPU memory and latency. Do not invent metrics or infer clinical readiness.

## Output
Record inputs, citations, artifact SHA, test commands, numerical results only when actually measured, safety limitations and next unresolved checks. Never mark unexecuted tests as passed.
