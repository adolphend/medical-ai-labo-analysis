# Acquisition and modality-specific quality assurance

[Diagnostic research index](README.md) · [Acquisition](../stages/07-diagnostic-acquisition.md) · [Anatomy](03-anatomical-localization.md)

## Responsibility
Check whether images, signals and metadata are technically adequate for their *intended* diagnostic task. Distinguish positioning/plane completeness, physical acquisition properties, study completeness and human diagnostic adequacy.

| Modality | Quality questions | Open tool or weights | Academic evidence | Status and limitations |
|---|---|---|---|---|
| **Ultrasound (obstetric)** | Standard planes, anatomy visibility, coverage, motion / shadow | [SonoNet weights](https://github.com/baumgach/SonoNet-weights), [PyTorch port](https://github.com/rdroste/SonoNet_PyTorch) | Baumgartner et al. *Real-Time Detection and Localisation of Fetal Standard Scan Planes*, IEEE TMI (2017), DOI [10.1109/TMI.2017.2712367](https://doi.org/10.1109/TMI.2017.2712367) | Pretrained plane recognition, **not general ultrasound quality**; old framework in original |
| **Ultrasound (image quality)** | Ultrasound-specific perceptual degradation | [US-Metrics](https://github.com/sextant-fable/US-Metrics) | *Defining Robust Ultrasound Quality Metrics via an Ultrasound Foundation Model* (2026) [preprint](https://arxiv.org/abs/2604.19512) | Early research/preprint; clinical adequacy not established |
| **MRI brain** | Motion, artifacts, signal/contrast metrics, study acceptance | [MRIQC](https://github.com/nipreps/mriqc) | Esteban et al. *MRIQC*, PLOS ONE (2017), DOI [10.1371/journal.pone.0184661](https://doi.org/10.1371/journal.pone.0184661) | Predicted quality on unseen centers only ~76% in original study; mainly neuroimaging |
| **X-ray** | Body part, view, rotation, coverage, exposure, blur, markers | [pydicom](https://github.com/pydicom/pydicom), [OpenCV](https://github.com/opencv/opencv) | **Evidence gap:** no peer-reviewed, externally validated general-purpose open-weight X-ray QC model verified in this review | Implement metadata/view/protocol checks first; image-based diagnostic adequacy requires modality-specific annotated data |
| **CT** | Study completeness, slice spacing, protocol, noise, metal/motion artifacts, coverage | [pydicom](https://github.com/pydicom/pydicom), [SimpleITK](https://github.com/SimpleITK/SimpleITK) | **Evidence gap:** peer-reviewed study required for any claimed clinical thresholds | Basic deterministic QC feasible, clinical accept/reject not established |
| **Digital pathology** | Tissue folds, focus, stain, artifacts and slide usability | [HistoQC](https://github.com/choosehappy/HistoQC), [QuPath](https://github.com/qupath/qupath) | Bankhead et al., *QuPath*, Scientific Reports (2017), DOI [10.1038/s41598-017-17204-5](https://doi.org/10.1038/s41598-017-17204-5) | Tool-level evidence; stain/scanner variation needs evaluation |
| **ECG** | Missing leads, baseline drift, electrode artifact, clipping, mains interference | [WFDB](https://github.com/MIT-LCP/wfdb-python), [NeuroKit2](https://github.com/neuropsychology/NeuroKit) | Makowski et al., *NeuroKit2*, Behavior Research Methods (2021), DOI [10.3758/s13428-020-01516-y](https://doi.org/10.3758/s13428-020-01516-y) | Signal metrics are not sufficient to establish diagnostic reliability |

## 2026 corroboration
A retrospective fetal ultrasound quality-assessment study evaluated SonoNet-based plane/structure detection and a fine-tuned VLM on 22,544 planes: https://pmc.ncbi.nlm.nih.gov/articles/PMC13235211/. It is a specialist, data-intensive system, **not a zero-training, universally deployable ultrasound model**.

## Prototype
Build one study validator producing metadata audit, required series/views count, quantitative technical metrics and manually reviewable flags. Evaluate per-modality with expert labels, site shift, scanner/vendor effects, sensitivity, false alarm rate and latency. Do not automatically reject clinical studies.
