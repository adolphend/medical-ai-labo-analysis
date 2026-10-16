# Candidate public or researcher-accessible evaluation datasets

[Evaluation plan](README.md) · [Protocol](protocol.md)

**Dataset access is not necessarily unrestricted.** Verify original source, current license, access agreement, allowable clinical/commercial use, patient split and pretrained-model contamination before downloading. None is included in Git.

| Task | Dataset/source | Labels/reference | Access caveat |
|---|---|---|---|
| Echocardiographic EF/ventricular segmentation | [EchoNet-Dynamic](https://echonet.github.io/dynamic/) ([paper](https://doi.org/10.1038/s41586-020-2145-8)) | Echo videos, EF, LV tracings | Research/data terms, commercial restrictions: audit |
| Chest radiograph finding labels | [CheXpert](https://stanfordmlgroup.github.io/competitions/chexpert/) ([paper](https://arxiv.org/abs/1901.07031)) | Multi-label CXR observations, uncertain labels | Agreement/terms, patient disjointness and weak labels |
| Chest radiographs + reports | [MIMIC-CXR-JPG](https://physionet.org/content/mimic-cxr-jpg/) ([paper](https://doi.org/10.1038/s41597-019-0322-0)) | Images, NLP-derived finding labels, split | Credentialed/controlled access, no redistribution |
| Lung CT nodules | [LIDC-IDRI / TCIA](https://www.cancerimagingarchive.net/collection/lidc-idri/) ([paper](https://doi.org/10.1118/1.3528204)) | CT, multiple radiologist nodule annotations | Reader disagreement, lesion matching |
| CT nodule challenge | [LUNA16](https://luna16.grand-challenge.org/) ([paper](https://doi.org/10.1016/j.media.2017.06.015)) | Lung nodule detection standard/official evaluation | Challenge split/annotation eligibility |
| Multi-organ CT/MRI segmentation | [Medical Segmentation Decathlon](http://medicaldecathlon.com/) ([paper](https://doi.org/10.1038/s41467-022-30695-9)) | Organ/tumor voxel annotations across tasks | Task-specific rights and official splits |
| Multi-organ CT | [BTCV (Beyond the Cranial Vault)](https://www.synapse.org/Synapse:syn3193805/wiki/217789) | Abdominal organ voxel masks | Dataset agreement and format verification |
| Brain tumor MRI segmentation | [BraTS challenge](https://www.synapse.org/brats) | Brain tumor regional masks | Access and year's evaluation rules |
| Retinal diabetic retinopathy grading | [EyePACS / Kaggle diabetic retinopathy](https://www.kaggle.com/c/diabetic-retinopathy-detection) | Retinal photographs, disease-grade labels | Competition access, licensing, grader uncertainty |
| General cardiac ECG | [PTB-XL / PhysioNet](https://physionet.org/content/ptb-xl/) ([paper](https://doi.org/10.1038/s41597-020-0495-6)) | 12-lead ECG, diagnostic superclass labels | Multilabel/multiple records per patient |
| Pathology nuclei segmentation | [MoNuSeg challenge](https://monuseg.grand-challenge.org/) | Microscopy nucleus instance masks | Challenge/data-use terms |
| Renal ultrasound and thyroid ultrasound | **MODEL_DATASET_GAP** | Need credible independent annotated multi-site data | Do not pretend general images provide verified labels |
| Prenatal ultrasound plane assessment | [Fetal Planes DB](https://zenodo.org/records/3904280) | Standard fetal ultrasound plane labels | Confirm annotation/version/license and model overlap |

## Dataset acceptance
Record dataset ID, version/date, source URL, license (and any application/access contract), SHA256 manifest, patient/study IDs in **local** protected store, image/modality protocols, label protocol, prevalence, site/vendor, official splits, train/pretraining overlap, annotation reliability. Never commit source images or identifying metadata.

**Models must not be tested only on the exact datasets used to train them** if generalization is claimed. A single public benchmark is an engineering check, not clinical deployment approval.
