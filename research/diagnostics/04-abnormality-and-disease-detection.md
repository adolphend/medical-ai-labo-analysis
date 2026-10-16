# Abnormalities, imaging findings and disease-specific detection

[Diagnostic research index](README.md) · [Anatomy](03-anatomical-localization.md) · [Reporting](05-interpretation-and-reporting.md)

## Independent responsibility
Evaluate whether an image contains a *specific, well-defined abnormality*, and whether a validated downstream clinical decision can be supported. Localization of an abnormality ≠ disease diagnosis; radiographic findings ≠ histopathological confirmation.

| Target | Modality | Candidate open approach | Research basis | Research readiness |
|---|---|---|---|---|
| Chest radiograph observations | Chest X-ray | [TorchXRayVision](https://github.com/mlmed/torchxrayvision), [CheXzero](https://github.com/rajpurkarlab/CheXzero) | Tiu et al., *Expert-level detection of pathologies from unannotated chest X-ray images*, Nature Biomedical Engineering (2022), DOI [10.1038/s41551-022-00936-9](https://doi.org/10.1038/s41551-022-00936-9) | Specific labels/benchmark dependence; not all diseases or clinical diagnosis |
| Lung nodules | CT | [LUNA16 benchmark](https://luna16.grand-challenge.org/), candidate [inference research repository](https://github.com/nauyan/Luna16) | Setio et al., *Validation, comparison, and combination of algorithms for automatic detection of pulmonary nodules in computed tomography images: the LUNA16 challenge*, Med Image Anal (2017), DOI [10.1016/j.media.2017.06.015](https://doi.org/10.1016/j.media.2017.06.015) | Availability of compatible working weights must be checked; nodules are not necessarily cancer |
| Intracranial abnormalities | Brain MRI | [MONAI bundles](https://github.com/Project-MONAI/model-zoo) | Task-specific model papers must be checked individually | No generic brain disease detector should be assumed |
| CT anatomical quantitative deviation | CT | [TotalSegmentator](https://github.com/wasserth/TotalSegmentator) + measurement rules | Wasserthal et al. (2023), DOI [10.1148/ryai.230024](https://doi.org/10.1148/ryai.230024) | Segmentation gives measurements, not proof of disease |
| Cell/tissue morphology | Pathology | [HoVer-Net](https://github.com/vqdang/hover_net), [QuPath](https://github.com/qupath/qupath) | Graham et al., *Hover-Net*, Med Image Anal (2019), DOI [10.1016/j.media.2019.101563](https://doi.org/10.1016/j.media.2019.101563) | Segment/classify nuclei; diagnosis needs appropriate reference labels |
| Retinal vessel morphology | Fundus photo | [MONAI](https://github.com/Project-MONAI/MONAI) plus validated specialist checkpoints | Evidence and ready-to-use commercial models must be verified | No specific checkpoint certified in this inventory |

## Failure modes
Domain shift, class prevalence shift, false-positive cascade, missed subtle findings, inappropriate normal/abnormal thresholds, nonrepresentative test populations, calibration and uncertainty failures.

## Research protocol
Define one target condition and imaging indication; identify reference-standard diagnoses, patient-level train/test separation, external datasets, sensitivity at specificities, PPV/NPV at real prevalence, subgroup outcomes and clinical review workflow. Compare against a non-AI baseline. Do not equate benchmark AUC with screening mortality benefit.

## Out of scope
Universal disease detection or automatic final diagnosis. Multi-disease aggregation must only combine individually validated modules under an independently validated integration protocol.
