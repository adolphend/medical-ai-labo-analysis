---
name: medgemma-benchmark
description: Compare MedGemma to task-specific models on identical cases
compatibility: opencode
---

# medgemma-benchmark

Read evaluation/medgemma-comparison.md and evaluation/protocol.md. Use Google model card and exact google/medgemma-1.5-4b-it revision and Health AI Developer Foundations terms. Compare on shared cases and reference labels, frozen prompts, matching input modality, consistent abstention policy, task-specific metrics and CPU/GPU resources. Do not claim Google scores as local tests. Require explicit approval before downloading weights or sending medical data to an API.

## Output
Record inputs, citations, artifact SHA, test commands, numerical results only when actually measured, safety limitations and next unresolved checks. Never mark unexecuted tests as passed.

## Registry-wide pipeline
Use `evaluation/medgemma-50-disease-pipeline.md` and `scripts/benchmark_50_diseases.py` for the full 50-condition registry. Each of the 250 tasks has independently required model/dataset evidence, reference labels, result status and safety review. Never fabricate results or infer universal clinical utility.

## 8GB local MedGemma preparation
Read `models/medgemma-local/README.md`. Confirm CUDA and dependency compatibility. Preview `models/medgemma-local/download.py` first, then require user's approval and accepted Hugging Face gated terms before any actual weight download. Run `models/medgemma-local/infer.py` only after local installation. Treat its generated text, memory and duration as a technical smoke test, never a clinical accuracy measurement. Keep weights and run artifacts out of Git.

## Cross-platform install guidance
Read `models/medgemma-local/INSTALL-CROSS-PLATFORM.md` before preparing the environment. Verify operating system, Python, CUDA/MPS and disk capacity; preview first with `models/medgemma-local/install.py`, then request permission before `--apply`. Do not automatically download gated MedGemma weights. The existing inference runner requires NVIDIA CUDA and has not been verified on macOS.
