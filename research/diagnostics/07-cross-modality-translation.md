# Cross-modality registration and image synthesis

[Diagnostic research index](README.md) · [Anatomy](03-anatomical-localization.md) · [Acquisition QC](02-acquisition-quality.md)

## Responsibility
Investigate whether existing image data can be spatially aligned or used to generate a *synthetic* modality for a tightly specified downstream task. Registration, image translation and imaging substitution are distinct.

| Task | Open material | Academic paper | Readiness |
|---|---|---|---|
| CT ↔ MRI spatial registration | [ANTs](https://github.com/ANTsX/ANTs), [SimpleITK](https://github.com/SimpleITK/SimpleITK) | Avants et al. (2011), [DOI 10.1016/j.neuroimage.2010.09.025](https://doi.org/10.1016/j.neuroimage.2010.09.025) | Established algorithms; requires matching anatomy and validation |
| MRI → synthetic CT for radiotherapy | [SynthRAD2023 resources](https://github.com/SynthRAD2023), [challenge](https://synthrad2023.grand-challenge.org/) | Huijben et al. (2024), *Generating synthetic computed tomography for radiotherapy*, [DOI 10.1016/j.media.2024.103276](https://doi.org/10.1016/j.media.2024.103276) | Research benchmarks, not a universal inference product |
| CBCT → synthetic CT | [SynthRAD2023 metrics](https://github.com/SynthRAD2023/metrics) | Same challenge publication | Image similarity alone poorly predicts dose accuracy |
| Generic paired/unpaired medical image translation | [MONAI generative models](https://github.com/Project-MONAI/GenerativeModels) | Need exact task-specific paper and weights | Framework does **not** mean pretrained clinical translation available |

## Critical evidence
Walston et al. (2024), *Evaluating Biases and Quality Issues in Intermodality Image Translation Studies for Neuroradiology: A Systematic Review*, [DOI 10.3174/ajnr.A8211](https://doi.org/10.3174/ajnr.A8211). The review found critical limitations restricting clinical application across studies.

## Non-negotiable safety invariant
A synthetic image must be **clearly marked SYNTHETIC** with source modality, transformation method, date and uncertainty; it cannot introduce verified anatomical or pathological evidence absent from the actual acquisition. Never claim synthetic CT substitutes for X-ray/CT or MRI in diagnosis, screening or treatment planning without separate task-specific prospective validation and appropriate regulatory authorization.

## Evaluation
Paired ground truth where possible, voxel registration error, external sites, clinically relevant lesion preservation, hallucinated lesions, missing structures, uncertainty, downstream dose/measurement impact, prospective specialist evaluation. PSNR/SSIM alone are insufficient.
