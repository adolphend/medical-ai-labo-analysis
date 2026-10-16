---
description: Run safe dataset governance and offline medical model evaluation smoke pipeline
agent: dataset-pipeline
---
Run the evaluation pipeline for $ARGUMENTS. Start with scripts/run_evaluation_pipeline.py and report actual test results. If an eligible dataset is specified, inspect its original source, rights, direct HTTPS artifact URL and checksum; preview download without transferring bytes. Do not approve or download restricted data automatically. For a real model, verify weights/preprocessing and build a task-specific tested adapter, DVC stage and evaluation card.
