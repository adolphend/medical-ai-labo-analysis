---
name: dataset-governance
description: Select and DVC-version permitted clinical benchmark data
compatibility: opencode
---

# dataset-governance

Read evaluation/datasets.md, evaluation/disease-dataset-catalog.json, evaluation/dataset-registry.json. Confirm clinical label and cohort match, provider terms, access agreement, split and training leakage. Run scripts/check_datasets.py and scripts/check_disease_dataset_catalog.py. Use scripts/download_dataset.py preview; only fetch explicitly approved direct HTTPS artifacts with verified SHA256. Never put patient data into Git.

## Output
Record inputs, citations, artifact SHA, test commands, numerical results only when actually measured, safety limitations and next unresolved checks. Never mark unexecuted tests as passed.
