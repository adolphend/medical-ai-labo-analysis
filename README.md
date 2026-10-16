# Medical AI Laboratory — Disease-Centered Diagnostic Research

**Research platform, not a medical device.** Develop, verify and compare modular open-source medical AI components from patient conversation and indicated examinations through abnormality analysis, specialist-reviewed reports, evidence-based management review and closed-loop follow-up. No autonomous clinical diagnosis, prescription or patient care.

## Where to start

| Area | Documentation |
|---|---|
| 50 disease/checkup starting conditions | [Disease registry and folders](diseases/README.md) |
| Modality-specific workflow analyses | [Imaging research](research/imaging/README.md) |
| Diagnostic modules and academic evidence | [Research index](research/README.md) |
| Disease procedure JSON and interpreter | [JSON procedure pipeline](pipeline/README.md) |
| Open-source model inventory/fork methodology | [Model integration registry](research/imaging/model-integration-registry.md) · [Fork agent](automation/README.md) |
| Evaluation metrics, datasets and DVC | [Evaluation framework](evaluation/README.md) |
| **MedGemma independent technical/clinical analysis** | [MedGemma analysis](evaluation/medgemma-technical-clinical-analysis.md) |
| MedGemma 50-disease nine-stage evaluation strategy | [End-to-end evaluation](evaluation/medgemma-end-to-end-50-diseases.md) |
| **Real public image + labels example** | [PneumoniaMNIST case](evaluation/cases/pneumonia-medmnist/README.md) |
| Windows / Ubuntu / Mac model setup | [Cross-platform installation](models/medgemma-local/INSTALL-CROSS-PLATFORM.md) |
| OpenCode agents and skills | [Agent instructions](.opencode/README.md) |

## Workflow

1. Select a disease or checkup from `diseases/registry.csv`.
2. Create or refine `diseases/<slug>/procedure.json`, with patient entrypoint, required/optional tests and dependencies. Tests **need not involve imaging**.
3. Identify source-linked clinical guidelines, suitable datasets and model registries; mark unavailable, restricted, or unsupported cases explicitly.
4. Evaluate each JSON step **separately**: context, red flags, examination selection, quality control, findings, diagnostic synthesis, reporting, management evidence and follow-up.
5. Retain per-step prediction provenance, evaluation dataset version, model weights/commit, reference labels, metrics, error analysis, human review, and auditable results.
6. Only afterward study end-to-end propagation of errors. A single strong AI benchmark does not establish clinical safety.

### Repository setup

```bash
git clone https://github.com/adolphend/medical-ai-labo-analysis.git
cd medical-ai-labo-analysis
python3 scripts/scaffold_diseases.py
python3 scripts/medgemma_disease_pipeline.py --output evaluation/results/medgemma-nine-stage-plan.json
python3 scripts/run_evaluation_pipeline.py
```

The offline pipeline uses **synthetic fixtures** for code testing. It does not load model weights.

### Local MedGemma on an 8 GB NVIDIA GPU

```bash
python3 models/medgemma-local/install.py --backend cuda
python3 models/medgemma-local/install.py --backend cuda --apply
.venv-medgemma/bin/python models/medgemma-local/verify.py
```

Then accept Google's Health AI Developer Foundations terms on [MedGemma Hugging Face](https://huggingface.co/google/medgemma-1.5-4b-it), authenticate with the local Hugging Face CLI, and explicitly run `models/medgemma-local/download.py --apply`. 4-bit weight-loading **may** fit on an RTX 4060 8GB; actual compatibility and peak VRAM have not been measured.

### One real-data image benchmark (opt-in)

```bash
# Download authorized official public image array and test labels:
python3 scripts/medgemma_pneumonia_case.py --download

# Requires local gated MedGemma weights and CUDA runtime:
.venv-medgemma/bin/python scripts/medgemma_pneumonia_case.py --infer --limit 20

# Score only genuine generated predictions, with abstention coverage:
python3 scripts/medgemma_pneumonia_case.py --score
```

Read the [case's methodology and limitations](evaluation/cases/pneumonia-medmnist/README.md). This dataset is a resized pediatric chest-radiograph benchmark; **it cannot validate clinical pneumonia diagnosis**, therapeutic recommendations or applicability to adults. Do not claim the pipeline measured clinical accuracy unless real inference was actually executed.

## Dataset control

[Dataset candidates for the 50 conditions](evaluation/disease-dataset-mapping.md) require individual access and label reviews. Data and weights are excluded from Git. [DVC guidance](evaluation/README.md) describes local versioning and protected remotes; never push protected records to public storage. Records of completed tests must include hashes, versioned labels and source documentation.

## OpenCode

Run OpenCode from the repository root. Commands include `/build-disease heart-failure`, `/evaluate-model heart-failure echonet`, and `/run-evaluation heart-failure echonet`. The skills and commands are research aids, not clinicians. See [.opencode/README.md](.opencode/README.md).

## Project status

- **Documented:** 50 starting clinical conditions and disease folders; candidate open-source projects/datasets; modality research; JSON procedure and evaluation specifications.
- **Committed prototype code:** dataset download/governance, synthetic scoring, context metrics, per-disease evaluation planning, controlled local MedGemma installation, optional chest X-ray benchmark.
- **Not established:** end-to-end real-model execution across the 50 diseases, model accuracy on local hardware, dataset suitability across all conditions, clinical/regulatory validation or autonomous treatment safety.

**Evidence standards:** cite actual academic studies and clinical guidelines; separate the paper's result from our locally measured output; expose uncertainty, incomplete coverage and limitations.
