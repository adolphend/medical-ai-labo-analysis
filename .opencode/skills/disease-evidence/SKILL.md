---
name: disease-evidence
description: Evaluate disease pathways using primary papers and guidelines
compatibility: opencode
---

# disease-evidence

Read diseases/registry.csv, disease clinical and examination files, evaluation/protocol.md. Define condition, cohort, screening versus symptomatic diagnosis, relevant clinical guideline, date, modality and reference standard. Cite DOI and original guideline URL for each claim. Keep unresolved claims EVIDENCE_PENDING. Never generate autonomous patient treatment decisions.

## Output
Record inputs, citations, artifact SHA, test commands, numerical results only when actually measured, safety limitations and next unresolved checks. Never mark unexecuted tests as passed.
