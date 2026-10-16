---
name: medgemma-benchmark
description: Compare MedGemma to task-specific models on identical cases
compatibility: opencode
---

# medgemma-benchmark

Read evaluation/medgemma-comparison.md and evaluation/protocol.md. Use Google model card and exact google/medgemma-1.5-4b-it revision and Health AI Developer Foundations terms. Compare on shared cases and reference labels, frozen prompts, matching input modality, consistent abstention policy, task-specific metrics and CPU/GPU resources. Do not claim Google scores as local tests. Require explicit approval before downloading weights or sending medical data to an API.

## Output
Record inputs, citations, artifact SHA, test commands, numerical results only when actually measured, safety limitations and next unresolved checks. Never mark unexecuted tests as passed.
