# Model and software integration registry

[Imaging index](README.md) · [Disease evidence matrix](disease-modality-evidence-matrix.md) · [Fork workflow](model-fork-and-evaluation-process.md)

**Purpose:** one row per *upstream code repository* with a specific contribution to our platform. An OSS framework is not necessarily a trained diagnostic model. Fork candidates are not yet forked. We should selectively fork only when modifications are needed; otherwise pin an upstream release or commit as a dependency.

| Upstream | Function | Clinical modality | Paper | Checkpoint / license / CPU suitability |
|---|---|---|---|---|
| [EchoNet-Dynamic](https://github.com/echonet/dynamic) | LV segmentation and EF | Echo | [Ouyang 2020](https://doi.org/10.1038/s41586-020-2145-8) | Pretrained model available; audit weight/data rights; video inference benchmark pending |
| [SonoNet-weights](https://github.com/baumgach/SonoNet-weights) | Fetal plane recognition | Ultrasound | [Baumgartner 2017](https://doi.org/10.1109/TMI.2017.2712367) | Weights available; old dependencies/license audit pending |
| [TorchXRayVision](https://github.com/mlmed/torchxrayvision) | CXR findings | X-ray | [Repository publications](https://github.com/mlmed/torchxrayvision#citation) | Pretrained weights available; per-weight restrictions/benchmark pending |
| [CheXzero](https://github.com/rajpurkarlab/CheXzero) | Zero-shot CXR findings | X-ray | [Tiu 2022](https://doi.org/10.1038/s41551-022-00936-9) | Weights and terms to verify; CPU benchmark pending |
| [MRIQC](https://github.com/nipreps/mriqc) | Neuro MRI QC | MRI | [Esteban 2017](https://doi.org/10.1371/journal.pone.0184661) | CPU-compatible processing; may be slow; domain shift |
| [TotalSegmentator](https://github.com/wasserth/TotalSegmentator) | CT organ masks | CT | [Wasserthal 2023](https://doi.org/10.1148/ryai.230024) | Pretrained, compute-heavy; task-specific commercial licensing |
| [MedSAM](https://github.com/bowang-lab/MedSAM) | Prompted region segmentation | Multimodal images | [Ma 2024](https://doi.org/10.1038/s41467-024-44824-z) | Includes lightweight direction; confirm specific checkpoints/terms |
| [MONAI model zoo](https://github.com/Project-MONAI/model-zoo) | Curated pretrained bundles | CT/MRI etc. | Bundle-specific paper required | Check every bundle, not entire zoo |
| [RadGraph](https://github.com/Stanford-AIMI/radgraph) | Radiology NLP | Reports | [Jain 2021](https://arxiv.org/abs/2106.14463) | Pretrained NLP; not image verification |
| [CheXbert](https://github.com/stanfordmlgroup/CheXbert) | CXR report NLP labels | Reports | [Smit 2020](https://aclanthology.org/2020.emnlp-main.117/) | Pretrained NLP, CPU research candidate |
| [medSpaCy](https://github.com/medspacy/medspacy) | Structured clinical text | Consultations | [Eyre 2021](https://arxiv.org/abs/2106.07799) | Rules/pipelines, no large-model training |
| [Whisper](https://github.com/openai/whisper) | Speech transcription | Consultations | [Radford et al. 2022](https://arxiv.org/abs/2212.04356) (preprint) | Small variants for CPU; medical transcript validation |
| [Orthanc](https://github.com/orthanc-server/orthanc) | DICOM archive | Infrastructure | [Jodogne 2018](https://doi.org/10.1007/s10278-018-0082-y) | Not AI; license/components review |
| [OHIF](https://github.com/OHIF/Viewers) | Image viewer | Infrastructure | [Official documentation](https://docs.ohif.org/) | Not AI; no paper-based clinical effectiveness claim |
| [HAPI FHIR](https://github.com/hapifhir/hapi-fhir) | Structured exchange | Infrastructure | [FHIR standard](https://hl7.org/fhir/) | Not AI; validation of local workflow still needed |
| [NeuroKit2](https://github.com/neuropsychology/NeuroKit) | ECG signal preprocessing | ECG | [Makowski 2021](https://doi.org/10.3758/s13428-020-01516-y) | Low-compute DSP; not diagnosis |
| [QuPath](https://github.com/qupath/qupath) | Pathology imaging | Slides | [Bankhead 2017](https://doi.org/10.1038/s41598-017-17204-5) | Desktop and whole-slide workloads vary |

## Field-level acceptance checklist

Before an upstream project is marked ready:
- [ ] Check current official repo ownership, maintenance and release.
- [ ] Check paper DOI and whether paper evaluates **this exact model variant**.
- [ ] Verify pretrained weights download works without fine-tuning.
- [ ] Record code license, weight license, dataset license and commercial terms independently.
- [ ] Estimate CPU RAM/inference time, dependency requirements and supported platforms.
- [ ] Record expected input orientation, calibration, preprocessing, output fields and uncertainty.
- [ ] Check external site/patient-group validation and clinician workflow error modes.
- [ ] Pin exact SHA/version; maintain upstream attribution and local patches.
- [ ] Pass reproducible inference tests on public or synthetic data.

No candidate is certified commercially safe or clinically deployable by this list.
