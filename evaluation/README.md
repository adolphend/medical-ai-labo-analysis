# Reproducible medical AI evaluation

[50 diseases](../diseases/README.md) · [Protocol](protocol.md) · [Dataset directory](datasets.md) · [Evaluation card](evaluation-card-template.md) · [OpenCode evaluator](../.opencode/agents/model-evaluator.md)

This directory evaluates **model claims and complete clinical workflow simulations**, not clinical autonomous diagnosis. Each model/disease gets independent dataset, label, license and hardware audit. The project initially includes executable **CSV-based binary prediction evaluation** and tests with artificial fixtures. Real model inference adapters and dataset access must be verified separately.

## Run offline tests

```bash
python3 -m unittest discover -s tests -p 'test_evaluation.py' -v
python3 scripts/evaluate_predictions.py --truth evaluation/fixtures/truth.csv --predictions evaluation/fixtures/predictions.csv --output evaluation/results/metrics.json
```

Results from the synthetic fixtures only verify the metric implementation, not any medical AI accuracy.

## DVC dataset versioning

DVC keeps data outside ordinary Git and versions its content by hashes. [Official DVC pipeline syntax](https://doc.dvc.org/user-guide/project-structure/dvcyaml-files).

```bash
python3 -m pip install 'dvc>=3,<4'
dvc init
mkdir -p data/raw
# Acquire a dataset ONLY after licensing and access audit; manually place it under data/raw/your-dataset
dvc add data/raw/your-dataset
git add .dvc .gitignore data/raw/your-dataset.dvc
git commit -m 'data: pin authorized evaluation dataset version'
# dvc remote add -d secure-store s3://YOUR-BUCKET/medical-eval  # only after configuring secure credentials
# dvc push
```

Do **not** push controlled clinical data to public storage. Commit `.dvc` metadata only after checking they contain no sensitive identifiers. Pipeline stages and simple fixtures are in [dvc.yaml](../dvc.yaml). Run `dvc repro` after installing DVC, then `dvc metrics show`. This starter pipeline uses only synthetic fixtures, not medical images.

See [full methodology](protocol.md) and [dataset options](datasets.md).

## Dataset governance checks

[Dataset registry](dataset-registry.json) tracks dataset sources and intentionally marks every real dataset **unapproved** pending legal review. Run `python3 scripts/check_datasets.py` to validate metadata, or `python3 scripts/check_datasets.py --require-approved chexpert` to test that an unapproved dataset is blocked. After authorization, add the dataset locally using `dvc add`, and record permitted version, checksum manifest and access agreement securely. The registry status alone is not proof of rights. Run all tests with `python3 -m unittest discover -s tests -p 'test_*.py' -v`.

## Disease-specific dataset discovery

[50-disease dataset mapping](disease-dataset-mapping.md) · [Machine-readable candidate list](disease-dataset-catalog.json). The discovery catalog maps all 50 conditions to 24 candidate datasets/portals or explicitly unresolved gaps. A disease-to-dataset link is **not** an authorization, validated label match or evidence of clinical accuracy. Run `python3 scripts/check_disease_dataset_catalog.py` to check completeness; all candidates require a rights and label audit.

## Automated downloads and end-to-end smoke tests

[Downloader](../scripts/download_dataset.py) · [Pipeline runner](../scripts/run_evaluation_pipeline.py) · [Downloader tests](../tests/test_download_dataset.py) · [OpenCode dataset agent](../.opencode/agents/dataset-pipeline.md)

```bash
# No network / no patient data. Validates metadata, runs tests and synthetic fixture metrics:
python3 scripts/run_evaluation_pipeline.py

# Fail-closed preview, requiring approved source, version, exact file SHA256 and direct HTTPS URL:
python3 scripts/download_dataset.py --dataset ptb-xl

# Only AFTER explicit dataset approval and verification of direct link + checksum:
python3 scripts/download_dataset.py --dataset DATASET_ID --apply --dvc-add
```

All real sources are **unapproved initially**. Portal URLs cannot be used as `download_url`; some sites require manual registration and cannot be auto-downloaded. Change registry metadata only after reviewing original provider terms. `--dvc-add` requires `dvc init` in the local clone and does not publish dataset bytes. Never commit dataset archives or sensitive metadata. The smoke script tests artificial binary predictions; it does not invoke a pretrained medical model.

## Clinical context analysis (beyond binary accuracy)

[Context evaluator](../scripts/evaluate_context.py) · [Synthetic gold cases](fixtures/context_truth.json) · [Synthetic predictions](fixtures/context_predictions.json) · [Unit tests](../tests/test_context_evaluation.py)

The context evaluation compares structured *patient-history facts*, *missing-information prompts*, *candidate examination categories*, *contraindication flags*, *human-review escalation* and *evidence IDs*. Each dimension has independent precision, recall and F1 (where defined). Additional safety counts are missed human review and unsupported citations. These are **exact-match, research-oriented contract checks**: they do not establish clinical reasoning correctness or treatment appropriateness.

Run:
```bash
python3 scripts/evaluate_context.py --truth evaluation/fixtures/context_truth.json --predictions evaluation/fixtures/context_predictions.json --output evaluation/results/context_metrics.json
python3 scripts/run_evaluation_pipeline.py
```

All cases are fabricated test fixtures. For actual cases, expert-adjudicated labels, guideline concordance, source validity, context chronology, contraindication handling, clinical harm severity, confidence intervals and external-site validation are needed. Binary image-classification metrics alone cannot certify a disease procedure.

## Google MedGemma comparison

[MedGemma 1.5 benchmark methodology](medgemma-comparison.md) · [Paired structured-context comparator](../scripts/compare_context_models.py). The comparator accepts two existing model-output JSON files and gold labels; it does **not** execute MedGemma or assert real accuracy. Six reusable agent skills live in [OpenCode](../.opencode/README.md).

## 50-disease MedGemma evaluation planning

[50-disease comparison pipeline](medgemma-50-disease-pipeline.md) · [Benchmark generator](../scripts/benchmark_50_diseases.py). Generates 250 planned disease/task comparisons without inventing model scores; each test requires independently approved reference data and task-compatible models.
