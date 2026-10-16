# MedGemma 1.5 4B — evidence-based technical and clinical analysis

[Evaluation index](README.md) · [Nine-stage 50-disease pipeline](medgemma-end-to-end-50-diseases.md) · [Local RTX 4060 setup](../models/medgemma-local/README.md) · [Official model card](https://developers.google.com/health-ai-developer-foundations/medgemma/model-card)

**Reviewed:** 2026-10-16. **Status:** literature/model-card analysis only. No local inference, reproducibility run, clinical efficacy study or independent benchmark has been completed in this repository.

## 1. Model identity

- **Model:** [google/medgemma-1.5-4b-it](https://huggingface.co/google/medgemma-1.5-4b-it).
- **Publisher:** Google Health AI Developer Foundations. Released January 13, 2026 (model card/release notes). Instruction-tuned, ~4B multimodal model, accepts medical text and supported medical image inputs, produces generated text.
- **Weights and terms:** access requires acceptance of [Health AI Developer Foundations terms](https://huggingface.co/google/medgemma-1.5-4b-it), not unrestricted Apache/MIT weights. Audit software, weights, training/evaluation data and commercialization rights separately.
- **What it is NOT:** a radiology PACS, a universal trained segmentation network, an ultrasound Doppler analyzer, an automatic prescription service or a clinically validated physician replacement.
- **Official publications:** [Google MedGemma 1.5 model card](https://developers.google.com/health-ai-developer-foundations/medgemma/model-card) (developer document); [MedGemma Technical Report, Sellergren et al. 2025](https://arxiv.org/abs/2507.05201) (preprint). Model-card benchmark statements must not be described as independently replicated clinical trials.

## 2. Measured benchmark results published by Google

| Task/dataset | Metric | MedGemma 1 4B | MedGemma 1.5 4B | What result establishes |
|---|---|---:|---:|---|
| CT Dataset 1: 7 conditions/abnormalities | Macro accuracy | 58.2% | **61.1%** | Internal task-specific performance; not 50-disease accuracy |
| CT-RATE validation: 18 labels | Macro F1 | 23.5% | **27.0%** | Modest F1 despite gains; needs external validation and task details |
| MRI Dataset 1: 10 conditions/abnormalities | Macro accuracy | 51.3% | **64.7%** | Internal benchmark improvement; not general clinical correctness |
| MIMIC-CXR: top 5 labels | Macro F1 | 88.9% | **89.5%** | Select labels; potential training-data overlap must be investigated |
| CheXpert: top 5 labels | Macro F1 | 48.1% | **48.2%** | Significant domain/task sensitivity compared with MIMIC |
| CXR14: 3 labels | Macro F1 | 50.1% | **48.4%** | Model revision does not consistently improve every task |
| PathMCQA histopathology | Accuracy | 69.8% | **70.0%** | Visual MCQ task, not tissue-level cancer diagnosis |

**Source:** [Google's official MedGemma 1.5 model card: performance tables](https://developers.google.com/health-ai-developer-foundations/medgemma/model-card). Results not independently reproduced in our repository. Macro accuracy vs macro F1, top-five vs three-label vs multilabel tasks are not directly comparable.

## 3. Suitability along the patient-to-management pathway

| Stage | Potential MedGemma role | Preferred ground truth | Limitation / recommended companion |
|---|---|---|---|
| Patient interview | Extract documented facts and questions from transcript | Expert-adjudicated note/transcript | Use speech recognition separately; do not assume safe autonomous triage; compare with medSpaCy/rules |
| Clinical risk review | Flag explicit context/contraindications for human review | Qualified clinician adjudication | False negatives on urgent flags, hallucination, uncertainty |
| Examination selection | Explain clinician-approved guideline-linked options | Locally applicable guideline + indication adjudication | Rules/retrieval needed; recommendations cannot be autonomous orders |
| Acquisition QC | Interpret relevant metadata or sampled images where supported | Technical reference QC assessment | SonoNet for fetal scan planes, MRIQC for neuro MRI; MedGemma is not a generic QC model |
| Anatomic structures | Describe visible structures with textual references | Expert masks / imaging annotations | Use TotalSegmentator/MedSAM for actual region masks and geometric measurements |
| Finding detection | Generate candidate image observations | Expert-labeled per-modality held-out cohort | Compare TorchXRayVision/CheXzero/other compatible specialist models; not all ultrasound/ECG tasks supported |
| Diagnostic synthesis | Summarize evidence, contradictions and uncertainty | Expert-adjudicated complete case | No unsupported definitive diagnosis; confidence calibration and abstention essential |
| Reporting | Draft source-linked text for professional verification | Specialist-authored report + provenance | Evaluate hallucinations, laterality, missed urgent observations |
| Management evidence | Retrieve/summarize current clinician guidelines, not prescribe | Dated guideline, specialist judgement | No autonomous treatment plans, doses, procedures, or patient orders |
| Follow-up | Summarize status and unresolved tasks | Workflow case reference | Deterministic acknowledgment/tracking (FHIR) preferable for task closure |

## 4. Imaging and other modalities: applicability is conditional

- **Chest X-rays:** documented evaluation, reasonable first image experiment. Exact finding labels, patient-level splits and preprocessing must align with the benchmark.
- **CT and MRI:** MedGemma 1.5 adds volumetric image support, but native full-volume loading can be memory-expensive and requires Google's specific input preparation; 8GB GPU is not guaranteed suitable for 3D workflows.
- **Histopathology:** model supports whole-slide patch collections conceptually; huge slides need specialized preprocessing and may exceed hardware capacity. HoVer-Net/Cellpose/QuPath are more specific for nuclei/tissue analysis.
- **Dermatology, fundus imaging:** medical-image interpretation research is possible; image-specific data and qualified labels essential. Retina screening claims not proven from generic question-answer results.
- **Ultrasound:** test text and explicitly supported still-image inputs separately; no established general Doppler/cine inference or validation of fetal anomaly, heart function, gallstones, DVT, AAA or kidney diseases from this model card.
- **ECG, biomarkers, lab tests, pathology reports:** textual/structured interpretation can be evaluated, but MedGemma is not a replacement for calibrated instruments, lab reference standards, or condition-specific signal classifiers.
- **No imaging cases:** many checkups start with patient history, guideline/risk eligibility, blood tests or ECG rather than an image. Do not force an image model.

## 5. Hardware: local 8GB NVIDIA RTX 4060

- Start with **4-bit NF4** (not BF16 full-weight loading) for text-only testing. Prior Google approximate weight footprint ~3.4 GB in 4-bit is **not a total peak VRAM measurement**; vision encoder, KV cache, CUDA context and processor add memory. Verify CUDA and available host RAM.
- [Installer](../models/medgemma-local/INSTALL-CROSS-PLATFORM.md) · [Opt-in gated download](../models/medgemma-local/download.py) · [CUDA 4-bit smoke script](../models/medgemma-local/infer.py).
- Measure initial load time, tokens/s, latency, peak VRAM via PyTorch and nvidia-smi, RAM, and out-of-memory conditions. Use fixed prompt length, few generation tokens and single-image/short text first. No performance numbers have been measured.
- Windows and WSL CUDA supported as *candidate* configurations, macOS MPS requires a different inference implementation. No clinical use authorized by technical success.

## 6. Independent test design for each of the 50 disease modules

1. **Eligibility / modality mapping:** decide whether MedGemma accepts the actual necessary evidence. Mark `NOT_COMPARABLE` for unsupported tasks.
2. **Data:** choose a task-specific independent dataset and reference labels; check permissions, contamination, demographic/site representativeness and DVC content hash. Many disease-specific datasets remain unresolved.
3. **Prompt / output:** pin model checkpoint SHA, prompt template, decoding config and image processor; require JSON with input references, observations, uncertainty and abstention.
4. **Stage scoring:** facts/missing information/context F1; safety flag recall; guideline-concordance/unsafe suggestions; image modality task metrics (classification, localization, quantitative MAE); reports for hallucinations and omissions; management citations for correctness; follow-up for task closure.
5. **Comparator:** same exact test cases with either a genuinely task-compatible specialist model (EchoNet, CheXzero, TotalSegmentator, etc.) or transparent deterministic baseline. Don't score unlike quantities against each other.
6. **Confidence:** stratify by site/device, race/sex/age where ethically and legally available, critical vs noncritical errors, abstention and data missingness. Calculate 95% CIs and review clinically meaningful harm, not only F1.
7. **End to end:** test whether one early extraction error contaminates downstream results, whether expert review stops false findings, whether the report faithfully cites original data and whether follow-up closes.
8. **Treatment evidence:** measure guideline retrieval and applicable source fidelity only, with clinician signoff. Even source-correct management advice is not automatically safe for a patient.

**Execution status:** [50-disease × 9-stage planner](../scripts/medgemma_disease_pipeline.py) can generate **450 untested** evaluation slots; [context evaluator](../scripts/evaluate_context.py) can score existing structured labeled predictions; [binary evaluator](../scripts/evaluate_predictions.py) measures classification. Real MedGemma inference adapters producing disease-case JSON, per-modality scorers and legally approved independent cohorts are still missing.

## 7. Primary failure modes and mitigation

- **Hallucinated diagnosis or literature:** independent evidence verification and source-linked reports.
- **Wrong examination:** clinician-approved guideline/risk pathway; human signoff before orders.
- **Missing red flags/contraindications:** high-sensitivity specialist-reviewed context tests and safe abstention.
- **Wrong organ/laterality:** image-grounded evidence keys, source series and specialist review.
- **Benchmark contamination:** holdout from independent time/sites; don't train/tune on test sets.
- **Input mismatch:** use correct modality preprocessing and defer unsupported volumetric/cine tasks.
- **Automation bias:** never present model-generated text as signed diagnosis, authoritative prescription or clinical clearance.
- **License/rights:** gated terms, dataset-specific access rules and use restrictions.
- **Privacy:** deidentified/synthetic inputs only by default; locally secured evaluation data; no public release of patient data.

## 8. Recommendation for first genuine experiment

Run three **separate** low-cost evaluations: (a) text-context field extraction on expert-written synthetic clinical cases vs deterministic rules; (b) CXR label classification on approved independent images vs TorchXRayVision; (c) evidence-grounded report consistency vs specialist-reviewed references. The first can avoid image-model GPU memory; the latter two require matching modality inputs, legally usable data, a working real inference adapter, and specialist label review.

**Conclusion:** MedGemma 1.5 4B is a promising compact **clinical-language and supported-image interpretation research component**, but Google-published benchmarks show nontrivial domain/task variation and do not justify automatic diagnoses, treatment advice, or claims covering all 50 diseases. Use separately validated specialist models and explicit human approval.

## Sources
- [Official MedGemma 1.5 model card](https://developers.google.com/health-ai-developer-foundations/medgemma/model-card) (model details, datasets, benchmark metrics, limitations).
- [Official gated Hugging Face model](https://huggingface.co/google/medgemma-1.5-4b-it) (weights, release, terms).
- [Google MedGemma overview](https://developers.google.com/health-ai-developer-foundations/medgemma) (recommended development use and adaptation).
- [MedGemma technical report, Sellergren et al. 2025](https://arxiv.org/abs/2507.05201) (preprint).
