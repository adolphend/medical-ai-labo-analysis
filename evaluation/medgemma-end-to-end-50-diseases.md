# MedGemma 1.5: end-to-end evaluation for all 50 disease pathways

[Model setup (8GB NVIDIA)](../models/medgemma-local/README.md) · [Dataset mappings](disease-dataset-mapping.md) · [Existing five-task comparison](medgemma-50-disease-pipeline.md) · [Google model card](https://developers.google.com/health-ai-developer-foundations/medgemma/model-card)

## Objective

The 50-disease registry defines research targets, **not 50 confirmed MedGemma-supported diagnoses**. [Pipeline generator](../scripts/medgemma_disease_pipeline.py) creates nine independently evaluated stages per disease (450 planned evaluations). Nothing is marked as tested by plan generation. Each stage must be scored against its own expert-defined reference standard and applicable external dataset; unsupported tasks must be **NOT_COMPARABLE** and data gaps **NOT_TESTED** rather than inaccurate zero scores.

## Stages in order

| Stage | Expected structured output | Reference standard & validation |
|---|---|---|
| 1. Clinical context | extracted facts, relevant history, missing questions, temporal context | expert-reviewed encounter transcript; fact precision/recall/F1 |
| 2. Clinical risk review | red flags, critical contraindications, abstention, clinician escalation | expert-vetted safety labels; missed-critical-flag and inappropriate certainty rate |
| 3. Examination selection | screening-vs-diagnostic status, candidate tests, evidence/alternatives | jurisdiction-specific clinician-approved guideline; concordance and unsafe-test proposals |
| 4. Acquisition quality | view/sequence adequacy, image/signal artifact flags | expert QC annotations; failure detection, false rejections |
| 5. Anatomy/findings | abnormalities and structures with original image references | matched disease/modality and expert labels; sensitivity/specificity, lesion-FROC, Dice where appropriate |
| 6. Diagnostic synthesis | differential hypotheses, uncertainty and gaps | adjudicated multimodal case record; critical omissions and calibration |
| 7. Report grounding | source-linked draft report, laterality and negations | specialist-reviewed report; hallucinations and unsupported observations |
| 8. Management evidence | **source-linked guideline options for clinician review** | verified guideline version/region; citation correctness, contraindication awareness, unsafe suggestions; **no automatic treatment prescriptions** |
| 9. Follow-up | ownership, result acknowledgement, referral/completion checks | approved simulated care-process checklist; unresolved critical tasks |

Stages 4-5 are conditional: certain conditions rely on lab tests, ECG, or physical examination instead of imaging. Do not force ultrasound or CT when inappropriate. MedGemma can assist with text and compatible images; specialized detection models and deterministic guidelines may be better than an LLM in certain stages. The 8GB RTX 4060 profile does not guarantee that large 3D images or whole-slide pathology will run locally.

## Run the planning and auditing code

```bash
python3 scripts/medgemma_disease_pipeline.py --output evaluation/results/medgemma-nine-stage-plan.json
python3 scripts/medgemma_disease_pipeline.py --audit evaluation/results/medgemma-nine-stage-plan.json
python3 -m unittest discover -s tests -p 'test_medgemma_disease_pipeline.py' -v
```

**Expected plan size:** 50 conditions, 9 stages each = 450 **not-yet-tested** stage evaluations. The plan is metadata; it performs no model inference, imaging processing, clinical recommendation, or download.

## Genuine benchmarking workflow (additional work required)

1. Confirm exact model release, Google terms, 4-bit loader, measured GPU memory/latency, model prompt and input interface.
2. Identify clinically valid tasks and a matching legally usable independent dataset **for each disease-stage combination**; if no reference labels, record a gap rather than a score.
3. DVC-version permitted data, clinical guidelines, test case IDs and structured expert labels. Ensure protected health data never enters the public repository.
4. Build model adapters to return one fixed output JSON with cited inputs, uncertainty, abstention and response type. Check whether MedGemma actually accepts the modality and representation (some images need specific processing).
5. Establish a specialist or deterministic baseline; ensure both receive comparable inputs and exactly the same cases.
6. Run stage-specific scoring; use binary/context evaluators where suitable; implement separate lesion detection, segmentation, multiclass or regression metrics as required.
7. For management evidence, **evaluate citations and guideline-based options only**, under human review. Do not request or automatically execute treatment orders, drug prescriptions or procedures.
8. Record errors, clinician corrections, patient/site/vendor subgroups, out-of-distribution cases, and resource use; generate run artifact linked from disease's `procedure.json`.
9. Evaluate end-to-end propagation of incorrect assumptions: a false clinical fact or poor image must not silently become a confirmed diagnosis or treatment plan.
10. Label untested tasks, incompatible modalities and missing datasets explicitly. Clinical validation and regulatory assessment remain distinct from technical evaluation.

## Model-specific constraints

The [official MedGemma 1.5 card](https://developers.google.com/health-ai-developer-foundations/medgemma/model-card) identifies image and text capabilities but warns against use of raw outputs for clinical diagnosis or management without validation/adaptation. Its capabilities are not necessarily equivalent to specialist models or certified laboratory testing. Require original image/data provenance and independent expert review at each gate.

## Output contract

The pipeline JSON stores `model_applicability: to_be_verified` and `evaluation.status: not_tested` initially. A recorded result requires dataset version, model revision, reference labels and result artifact. A complete final evaluation also needs measured scores, confidence intervals where appropriate, sensitivity analyses, evidence provenance and human signoff. The interpreter deliberately cannot certify clinical fitness.
