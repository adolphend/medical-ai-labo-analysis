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
