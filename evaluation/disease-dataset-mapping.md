# Datasets mapped to all 50 conditions

[Full machine-readable catalog](disease-dataset-catalog.json) · [Data evaluation method](protocol.md) · [Dataset governance](dataset-registry.json) · [50-condition registry](../diseases/registry.csv)

**Status:** discovery only. Every dataset is unapproved until a human audits its current permissions, label provenance, specific model weight/pretraining overlap and the relevant research question. In particular, a cancer organ-segmentation dataset is not automatically suitable for cancer diagnosis; a fetal-plane label cannot validate fetal growth restriction or placenta previa. **For many conditions no task-specific open dataset is established in this first pass.**

## Accessible evaluation starting points

| Dataset | Clinical model task | Official source | Access warning |
|---|---|---|---|
| MedMNIST (18 subsets) | Lightweight biomedical image classification, initial code sanity checks | [Official GitHub](https://github.com/MedMNIST/MedMNIST) · [Paper](https://doi.org/10.1038/s41597-022-01721-8) | Mostly CC BY 4.0; DermaMNIST CC BY-NC 4.0; not a clinical benchmark substitute |
| EchoNet-Dynamic | Echo left-ventricular EF and segmentation | [Official dataset](https://echonet.github.io/dynamic/) · [Paper](https://doi.org/10.1038/s41586-020-2145-8) | Registration, **personal noncommercial research** only |
| CheXpert | CXR observation classification | [Official portal](https://stanfordmlgroup.github.io/competitions/chexpert/) | Terms and uncertainty-label handling |
| MIMIC-CXR-JPG | CXR findings and report-grounded validation | [PhysioNet](https://physionet.org/content/mimic-cxr-jpg/) | Credentialed access; don't redistribute |
| MIMIC-IV | Clinical histories, labs and encounter context | [PhysioNet](https://physionet.org/content/mimiciv/) | Credentialed; no general sharing of derived patient data |
| LIDC-IDRI | CT lung nodules with multiple readers | [TCIA](https://www.cancerimagingarchive.net/collection/lidc-idri/) · [Paper](https://doi.org/10.1118/1.3528204) | Nodule ≠ cancer; radiologist disagreement |
| LUNA16 | Lung nodule detection benchmark | [Challenge](https://luna16.grand-challenge.org/) | Challenge evaluation rules and proper splits |
| BraTS | Brain tumor MRI regions | [Official challenge](https://www.synapse.org/brats) | Challenge-specific access, segmentation ≠ histologic tumor diagnosis |
| Medical Segmentation Decathlon | Abdominal organ/tumor CT and other tasks | [Official portal](http://medicaldecathlon.com/) · [Paper](https://doi.org/10.1038/s41467-022-30695-9) | Task-specific applicability/rights |
| IDRiD | Retinal diabetic retinopathy lesions/severity | [Challenge dataset](https://idrid.grand-challenge.org/Data/) | Verify labels, agreement and held-out sites |
| ISIC | Dermoscopy lesion classification/segmentation | [Official archive](https://www.isic-archive.com/) | License varies by image/collection |
| PTB-XL | Multilabel ECG diagnostic statements | [PhysioNet](https://physionet.org/content/ptb-xl/) · [Paper](https://doi.org/10.1038/s41597-020-0495-6) | Patient-level data partition; not all cardiology tasks |
| Fetal Planes DB | Obstetric ultrasound standard-plane recognition | [Zenodo](https://zenodo.org/records/3904280) | **Not** a fetal anomaly/placenta outcome dataset |
| MoNuSeg | Cell nucleus segmentation in histology | [Challenge](https://monuseg.grand-challenge.org/) | Not direct validation of a cancer diagnosis |
| OASIS / ADNI | Brain imaging, aging/cognitive research | [OASIS](https://sites.wustl.edu/oasisbrains/) · [ADNI](https://adni.loni.usc.edu/) | Registration/terms; clinical disease labels and cohort bias |
| RSNA Cervical Spine Fracture | CT fracture detection | [Competition](https://www.kaggle.com/competitions/rsna-2022-cervical-spine-fracture-detection) | Competition-use terms; cervical fracture only |

Other catalog entries are datasets/portals with **specific label or access reviews pending**, rather than confirmed disease-specific validation datasets.

## Disease-level matching methodology

Open `disease-dataset-catalog.json`: each of the **50 disease slugs** has `candidates`. The flag `task_relevant_check_labels` means potentially suited to one component (e.g., EF, nodule, lesion mask) *after independent scrutiny*. The `related_or_proxy_not_disease_validated` flag means related data or infrastructure, **not a direct disease test**.

For any disease with `ultra`/no independent task-specific reference, first find a dedicated disease cohort, expert labels and access terms. Do not repurpose generic ultrasound image classes as validated disease outcomes.

## Agent and data governance

The OpenCode [model evaluator](../.opencode/agents/model-evaluator.md) must read the catalog before choosing an evaluation dataset, and record suitability/mismatch in that disease's validation file. No download is authorized by appearance in this index. Version approved data with DVC, pin exact model and preprocessing versions, use distinct patient-level splits, and publish metrics only with sample counts and source evidence.

Check consistency without downloading data:

```bash
python3 scripts/check_disease_dataset_catalog.py
```

Do not commit original medical images, restricted labels, embedded patient identifiers or model weights to this public repository.
