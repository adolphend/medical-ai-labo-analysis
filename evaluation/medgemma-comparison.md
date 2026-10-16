# MedGemma 1.5 benchmarking against disease-specific models

[Evaluation protocol](protocol.md) · [OpenCode benchmarking skill](../.opencode/skills/medgemma-benchmark/SKILL.md) · [Comparison runner](../scripts/compare_context_models.py)

## Correct comparator

Google's **MedGemma 1.5 4B** (January 2026) is an open-weight multimodal medical text/image model. It is **not** a specialized binary detector or guaranteed clinical decision maker. [Google launch](https://research.google/blog/next-generation-medical-image-interpretation-with-medgemma-15-and-medical-speech-to-text-with-medasr/) · [Official model card](https://huggingface.co/google/medgemma-1.5-4b-it). Its weights have Health AI Developer Foundations terms, not ordinary unrestricted OSS licensing. Verify current terms. MedASR is separate medical speech transcription software.

**Do not conflate:** Google's Med-Gemini/AMIE research systems, the general Gemini commercial API, and downloadable MedGemma weights. They differ in accessibility, modality and validated performance.

## What to compare

| Task | General model candidate | Specialized comparator | Metric |
|---|---|---|---|
| Clinical-context facts/missing items | MedGemma 1.5 4B text | Rule-based extractor or medSpaCy | Field-level precision/recall/F1, false safety omissions |
| Clinical test decision support | MedGemma with verified guideline excerpts | Clinician-authored retrieval/rules | Expert-agreement and guideline source precision, unsafe routing |
| Chest X-ray finding labels | MedGemma 1.5 image/text | TorchXRayVision / CheXzero | Per-label sensitivity, specificity, AUROC where probabilities available |
| Echo LV ejection fraction | MedGemma (only if verified modality support) | EchoNet-Dynamic | MAE, RMSE, bias and clinical interpretation error |
| CT anatomic localization | MedGemma 1.5 | TotalSegmentator | Dice/IoU, lesion- or region-specific findings |
| Medical reporting | MedGemma | Specialist source-linked templates | Hallucination rate, missed positives, negative/uncertain handling |

For modality-incompatible tasks, record **NOT_COMPARABLE** rather than forcing a score. MedGemma may not support raw ultrasound cine data or native DICOM input directly in local inference. No single numerical 'clinical superiority' score.

## Experimental design

1. Freeze actual model revision, checkpoint SHA, prompt, decoding seed/parameters, image sampling/preprocessing, dataset version, patient-level test split and scoring script.
2. Use the same authorized cases and expert gold labels. Separate development prompts/threshold fitting from held-out test.
3. Define the output JSON schema *before* testing both models. Reject invalid schema, absent citations, fabricated findings, misplaced anatomy; report abstention.
4. Calculate task-specific metrics and paired differences with confidence intervals when possible. Blind clinician review for free-form explanations and guideline suggestions; measure false-negative/high-risk errors independently.
5. Report hardware, peak RAM, p50/p95 inference duration, tokens, API cost if applicable and privacy boundary.
6. Do not rely on benchmark leakage; audit known training data overlap, particularly public test sets.
7. Keep model-generated guideline suggestions **read-only** and clinician reviewed; don't measure treatment success by mere textual agreement.
8. Archive evaluation card, exact prompts, dataset DVC hash and model outputs. Record NOT_TESTED where no adapter or permission.

## Published Google baseline (not reproduced)

Google reported internal CT finding accuracy 61% (MedGemma 1.5) vs 58% (original MedGemma 1), and MRI finding accuracy 65% vs 51%. These metrics use Google's own benchmark settings and cannot be compared directly to our models or datasets.

## Execution

```bash
python3 scripts/compare_context_models.py --truth evaluation/fixtures/context_truth.json --a evaluation/fixtures/context_predictions.json --b evaluation/fixtures/context_predictions.json
```

This is a **same-data comparison of synthetic structured predictions** and confirms only benchmark code. To compare MedGemma in reality, replace B with JSON outputs from an independently implemented model adapter, and A with specialist model outputs on the same authorized cases. The repository does not download or execute MedGemma by default.
