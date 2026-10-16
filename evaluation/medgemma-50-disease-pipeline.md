# 50-disease MedGemma comparison pipeline

[Evaluation research](README.md) · [MedGemma evidence](medgemma-comparison.md) · [Disease registry](../diseases/registry.csv) · [OpenCode evaluation agent](../.opencode/agents/model-evaluator.md)

## Purpose

Create a **50-disease × 5-task (250 evaluations)** plan; do not claim these are 250 completed benchmarks. For each disease:
1. Clinical-context extraction from patient history, missing information and safety flags.
2. Clinically appropriate checkup/examination selection versus human-written guidance.
3. Modality-compatible imaging findings against specialist models and independent reference standards.
4. Report factual grounding and critical omission review.
5. Guideline evidence and clinician sign-off for management options.

Every task must record its own dataset version, clinical reference, model/checkpoint revision, comparable baseline, metrics, source artifact and limitations. The outcome `not_comparable` is appropriate for unsupported modalities; missing evaluations are `not_tested`, **not** zero accuracy. Source datasets require legal approval and DVC versioning. Never send patient information to an external service without independent authorization.

**Comparability warning:** Google [MedGemma 1.5 model card](https://developers.google.com/health-ai-developer-foundations/medgemma/model-card) describes CT/MRI and whole-slide use, but modality handling and input preprocessing must be verified for each task. Source weights are governed by Health AI Developer Foundations terms. A specialized model's segmentation Dice is not directly comparable to an LLM's textual accuracy. No model is assumed to prescribe treatment autonomously.

## Generate full plan

```bash
python3 scripts/benchmark_50_diseases.py --output evaluation/results/medgemma-50-plan.json
python3 -m unittest discover -s tests -p 'test_benchmark_50.py' -v
```

This step uses repository metadata only, **not** MedGemma inference or clinical datasets. Current status: no comparative scores.

## Record real evaluations

After an independently reviewed experiment, create a local JSON document with `results` entries:
```json
{
  "results": [
    {
      "disease": "heart-failure",
      "task": "context_extraction",
      "status": "passed",
      "dataset_version": "approved-DVC-sha",
      "ground_truth_source": "expert-reviewed-study-ID",
      "model_revision": "actual-locked-commit",
      "baseline_revision": "actual-locked-commit",
      "metric_name": "field_f1",
      "metric_value": 0.0,
      "run_artifact": "secure-run-manifest"
    }
  ]
}
```
The zero above is an **illustrative schema value, not an observed model score**; enter only measured values. `passed` must be justified by predeclared thresholds and human review. This code checks structure, not the truth of the claimed run.

```bash
python3 scripts/benchmark_50_diseases.py --results /path/to/approved-run-results.json
```

## Operational extension

The OpenCode agent selects a disease, prepares approved cases and exact source models, runs independently implemented inference adapters, validates JSON output, measures clinical and model-specific metrics, and writes an evaluation card. Any diagnosis, examination order or treatment must remain under qualified clinician control. Add each adapter and its tests before attempting production evaluation.
