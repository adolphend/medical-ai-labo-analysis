# Reproducible image test: PneumoniaMNIST → MedGemma → accuracy

This is a **technical research benchmark**, not pneumonia diagnosis or evidence of treatment safety.

- Official data: [MedMNIST v2](https://github.com/MedMNIST/MedMNIST) / [Zenodo release](https://zenodo.org/records/10519652). PneumoniaMNIST contains pediatric X-ray images, labels 0=normal / 1=pneumonia; published test split has 624 images. Official source includes the 224px version and its MD5 checksum.
- Paper: [MedMNIST v2, Scientific Data 2022](https://doi.org/10.1038/s41597-022-01721-8).
- Source URL: `https://zenodo.org/records/10519652/files/pneumoniamnist_224.npz?download=1`.
- Source-reported MD5: `d6a3c71de1b945ea11211b03746c1fe1`. MD5 is used to match the publisher's distribution artifact, not to prove authenticity against malicious tampering.
- Published license: CC BY 4.0 for PneumoniaMNIST, subject to checking source/derived data terms; attribution required.
- Ground truth is a benchmark label, not independent clinical diagnosis. Test-set training overlap and pediatric-vs-adult shift require scrutiny.
- **Why 224px?** 28px images are too degraded for meaningful image reasoning; even 224px images are still resized and not clinically equivalent to original radiographs.

## Download — explicit permission

```bash
python3 scripts/medgemma_pneumonia_case.py --download --limit 20
```

`--download` fetches an official research artifact with the publisher's MD5 check; no bypass of gating. It is stored at `data/raw/pneumoniamnist_224.npz`, ignored by Git. `--limit` caps inference images, not the download size. Only run after verifying local data terms. There is no download on import or unit test.

## Generate structured predictions with locally installed MedGemma (RTX 4060)

```bash
.venv-medgemma/bin/python scripts/medgemma_pneumonia_case.py --infer --limit 20
```

Requires Google model terms accepted and local weights downloaded per [MedGemma setup](../../../models/medgemma-local/README.md). The script intentionally **does not show gold labels** to the model. It asks for a structured judgment, logs invalid/unclassifiable outputs, and writes `evaluation/results/pneumonia_medgemma_predictions.csv`, paired truth and a provenance JSON. It loads in 4-bit on CUDA and can fail due to GPU memory/runtime dependencies. Do not use real patient information.

## Score recorded predictions

```bash
python3 scripts/medgemma_pneumonia_case.py --score
```

Uses existing `scripts/evaluate_predictions.py`; abstentions are recorded independently and excluded from the binary classifier's covered-case metric. **Always report abstention coverage and overall counts**, not just accuracy on answered cases. Label interpretations are benchmark-specific and never treatment recommendations.

## Why this is not full end-to-end validation

The case directly tests one image finding task. Patient symptoms, clinician examination selection, guideline retrieval, treatment suitability and follow-up require **separate expert-adjudicated cases** and independent stage metrics defined in [nine-stage plan](../../medgemma-end-to-end-50-diseases.md).
