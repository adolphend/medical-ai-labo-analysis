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

## Multi-model analysis and new-model development

The project evaluates **multiple specialized models**, not just MedGemma. Each disease may combine clinical text extraction, examination selection, quality control, segmentation, detection, interpretation and clinician-reviewed guideline evidence. Different models can also compete for the **same task**. A model is never assumed valid for a disease simply because its upstream repository is available.

### Available analysis options

| Analysis track | Representative existing models/tools | Evaluation questions |
|---|---|---|
| Clinical context and reporting | MedGemma 1.5, medSpaCy, CheXbert, RadGraph, Whisper (transcription) | Facts, missing context, contradictions, hallucinations, missed red flags, source fidelity |
| Ultrasound | EchoNet-Dynamic, SonoNet, MedSAM (prompted segmentation) | Correct plane, left-ventricular measurement error, anatomy masks, patient/site shift |
| Chest X-ray | TorchXRayVision, CheXzero, MedGemma | Per-finding sensitivity/specificity, label uncertainty, out-of-domain errors |
| CT | TotalSegmentator, task-specific MONAI bundles, LUNA16 benchmark implementations | Segmentation Dice and measurement error, nodule sensitivity/false positives per scan |
| MRI | MRIQC, ANTsPyNet, task-specific MONAI models, MedSAM | QC sensitivity, region masks, lesion reference labels, sequence/site robustness |
| Microscopy/pathology | HoVer-Net, Cellpose, QuPath, HistoQC | Nucleus masks, tissue artifacts, classification error and scanner/stain shift |
| Physiological signals | WFDB, NeuroKit2, task-specific ECG classifiers to verify | Signal quality, patient-level sensitivity, rhythm classification; not image interpretation |
| Clinical information systems | HAPI FHIR, OHIF, Orthanc, Medplum | Data provenance, interface correctness, report delivery, acknowledgement and follow-up |

These are **research candidates and infrastructure**, not an approved set of clinical diagnostic models. Some have pretrained checkpoints and some are frameworks, benchmarks or non-AI tools; weight access, code/data licenses and independent validation must be reviewed for each.

### Model selection and development decision

1. **Define the target and reference standard**: disease, patient group, imaging or non-imaging examination, intended outcome, and human review.
2. **Inventory alternatives**: use the [model integration registry](research/imaging/model-integration-registry.md) and [fork manifest](automation/model-forks.json). Distinguish a reusable pretrained model from a framework needing task-specific weights.
3. **Use the same authorized cases where comparable**: lock dataset and split using [DVC governance](evaluation/README.md), verify train/test contamination and licensing, freeze prompts and preprocessing.
4. **Test each model separately**: record exact version, weights, input/output JSON contract, reference labels, task metrics, confidence intervals where feasible, latency, peak GPU/CPU RAM, abstentions and failures.
5. **Compare only like-for-like outputs**: classification against classification, segmentation against segmentation, measurement against reference measurement, and clinical context against adjudicated context. A Dice score cannot be compared directly with medical-text F1.
6. **Test multi-model integration**: evaluate errors propagated between image quality, anatomy, finding detection and report generation; verify that a failed early stage cannot turn into a confident downstream diagnosis or management suggestion.
7. **Develop a new model only for a verified gap**: start with a deterministic baseline or pretrained model; consider calibration or parameter-efficient adaptation if permitted; train from scratch only when evidence, labeled data, rights and computing resources justify it. The **8 GB RTX 4060** is the initial development constraint, not an assumed guarantee of training feasibility.
8. **Release only research outputs with traceability**: write per-step scores/results into [disease procedure JSON](pipeline/README.md) and a model evaluation card. Human specialist verification remains mandatory before any clinical care decision; no autonomous treatment or prescription.

### Example composition: lightweight, task-specific components

**Default architecture: no large language model required.** Start with small, task-specific pretrained models, deterministic rules, or manual specialist review. MedGemma is an **optional benchmark comparator**, not a mandatory stage. GPU memory (8 GB VRAM) and CPU-only deployment feasibility must be measured rather than assumed.

```text
Patient intake        → structured form + medSpaCy (rule-based extraction)
Examination selection → guideline lookup + deterministic eligibility rules + clinician
Image QC              → metadata/geometry checks; SonoNet for fetal planes only
Anatomy/measurement   → small task-specific segmentation model or manual measurement
Finding detection     → a verified small specialist classifier; otherwise MODEL_GAP
Reporting             → structured templates with linked source observations
Management evidence   → versioned guideline retrieval and clinician review
Follow-up             → deterministic task tracking and result acknowledgement
```

For a concrete **cardiac ultrasound** research task, [EchoNet-Dynamic](https://github.com/echonet/dynamic) is a candidate for ejection-fraction assessment; for chest radiographs, a selected [TorchXRayVision](https://github.com/mlmed/torchxrayvision) checkpoint is an alternative. Both require actual checkpoint, licensing, accuracy and memory audits before use. **Do not combine unrelated modality models into one disease pipeline.** Use classical image analysis or a smaller approved model when a deep network is unnecessary.

Evaluate any candidate against a non-AI baseline and optionally against [MedGemma](evaluation/medgemma-technical-clinical-analysis.md) *only on compatible tasks with identical independent reference cases*. The disease JSON must identify exactly which components were evaluated and where clinician approval is required.

## Dataset control

[Dataset candidates for the 50 conditions](evaluation/disease-dataset-mapping.md) require individual access and label reviews. Data and weights are excluded from Git. [DVC guidance](evaluation/README.md) describes local versioning and protected remotes; never push protected records to public storage. Records of completed tests must include hashes, versioned labels and source documentation.

## OpenCode

Run OpenCode from the repository root. Commands include `/build-disease heart-failure`, `/evaluate-model heart-failure echonet`, and `/run-evaluation heart-failure echonet`. The skills and commands are research aids, not clinicians. See [.opencode/README.md](.opencode/README.md).

## Project status

- **Documented:** 50 starting clinical conditions and disease folders; candidate open-source projects/datasets; modality research; JSON procedure and evaluation specifications.
- **Committed prototype code:** dataset download/governance, synthetic scoring, context metrics, per-disease evaluation planning, controlled local MedGemma installation, optional chest X-ray benchmark.
- **Not established:** end-to-end real-model execution across the 50 diseases, model accuracy on local hardware, dataset suitability across all conditions, clinical/regulatory validation or autonomous treatment safety.

**Evidence standards:** cite actual academic studies and clinical guidelines; separate the paper's result from our locally measured output; expose uncertainty, incomplete coverage and limitations.
