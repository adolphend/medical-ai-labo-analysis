# Evaluation methodology: model + complete care pathway

[Dataset candidates](datasets.md) · [Metrics code](../scripts/evaluate_predictions.py) · [Evaluation card](evaluation-card-template.md)

1. **Register clinical claim:** disease/finding, patient group, screening vs symptom-driven diagnosis vs surveillance, expected role, actual examination required and appropriate reference standard. No-imaging pathways are valid.
2. **Audit source:** exact model repository SHA, checkpoint SHA256, framework and preprocess specification; code, weights, dataset and commercial licenses separately.
3. **Lock dataset:** official dataset and split if available, clinical indication, inclusion/exclusion, label creation, patient/study-level duplicates and overlap with model pretraining. Use DVC to track actual permitted data content and Git to track metadata; do not store protected IDs in public Git.
4. **Test technical behavior:** reject incompatible modality/view, incomplete series, invalid units, unreadable scans and acquisition failures. Assert fail-closed or specialist review—not fabricated findings.
5. **Freeze threshold:** decide in advance using disjoint validation data; never tune on test labels. Run simple non-AI baseline and model with identical cases.
6. **Classification:** TP/TN/FP/FN, sensitivity, specificity, PPV, NPV, balanced accuracy; additionally ROC-AUC and PR-AUC from probability scores if available. Evaluate confidence intervals and clinical-prevalence impact before any safety claim.
7. **Segmentation:** Dice, IoU per case and region, Hausdorff95 and physical measurement error if geometry/reference masks are available. An average pixel score alone may hide small-lesion failures.
8. **Detection:** lesion-level sensitivity versus false positives per scan, FROC, patient stratification; independent lesion-matching rules.
9. **Regression:** MAE, RMSE, bias, limits of agreement and threshold error for EF/organ diameters.
10. **Report generation:** specialist fact-check, missed urgent findings, false laterality, negation and hallucinations, report completeness, inter-rater agreement.
11. **Management support:** retrieved guideline version and jurisdiction, evidence quality, correctness of citations, missing contraindications, safe abstention, clinician signoff and outcome follow-up. No autonomous medication recommendations.
12. **End-to-end case simulation:** verify decision to image or not, routing, acquisition QC, model abstention, reading, treatment evidence retrieval, report signoff, acknowledged result, referral and follow-up; count safety failures at every handoff.
13. **Generalizability:** independent sites/devices/time cohorts, subgroup performance, missing-data stress tests and label disagreement. Quantify false negatives and uncertainty.
14. **Resources and reproducibility:** CPU environment, 8GB-RAM target measurements, p50/p95 latency, peak RSS, storage, dependency lock, dataset DVC hash, Git SHA, checkpoint checksum, run time; publish signed evaluation card.

**Predefined release gates:** no leakage; explicit rights; correct modality; reproducible technical function; minimum disease-specific performance thresholds **defined by clinicians before testing**; no unresolved critical workflow failure; independent specialist review; external clinical and regulatory validation before live care. Technical benchmark success is not proof of patient outcome benefit.
