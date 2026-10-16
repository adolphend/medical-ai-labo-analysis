# Diagnostic workflows by imaging modality

[Research root](../README.md) · [Diagnostic components](../diagnostics/README.md) · [Peer-reviewed evidence standards](../methods/research-method.md)

**Purpose:** identify distinct end-to-end clinical investigation pathways by modality, with links to software, relevant academic studies, limitations, compute constraints, and potential no-training prototypes. Each file owns **one modality/workflow**; shared concerns are linked instead of copied. Conditions are indications/research targets rather than guarantees of diagnosis.

| Category | Diseases/conditions/examples | Full workflow |
|---|---|---|
| Ultrasound / Doppler / echo | Cardiac dysfunction, fetal assessment, kidney obstruction, gallstones, thyroid masses, venous clot, aortic aneurysm | [Ultrasound](01-ultrasound.md) |
| X-ray / mammography | Chest findings, fractures, selected breast cancer screening | [Radiography](02-xray.md) |
| CT / low-dose CT | Lung nodules/cancer screening (eligible people), trauma, vascular and abdominal findings | [CT](03-ct.md) |
| MRI | Brain lesions, prostate or musculoskeletal assessments, selected stroke pathways | [MRI](04-mri.md) |
| Digital pathology / endoscopy | Tissue and cellular abnormalities, visual mucosal findings | [Pathology and endoscopy](05-pathology.md) |
| Multi-test / cardiac signal and vascular | ECG arrhythmia, cardiac structure, thrombosis, combined diagnostic pathways | [Multimodality](06-vascular-cardiac-other.md) |

## Shared pipeline and boundaries

Patient conversation → human clinical assessment → clinical examination selection → modality acquisition/QC → anatomy → targeted abnormality analysis → specialist-reviewed report → clinician treatment/monitoring choice → result acknowledgement and follow-up.

Some patients need no imaging, and tests may be parallel, repeated, inconclusive, or switched. Algorithms must not turn a plausible synthetic image or a predicted label into unverified diagnostic evidence.

## Missing dedicated investigations

- **Ultrasound sub-specialties** (renal, thyroid, breast, obstetric, POCUS) need separated evidence maps as the review grows.
- **Nuclear medicine/PET/SPECT**, fluoroscopy/angiography, OCT/retinal imaging, dental imaging, dermatology and microscopic molecular imaging still need modality-specific files.
- **Disease prevalence and priority** need jurisdiction-specific peer-reviewed epidemiology, screening trials and benefit-harm evaluations.
- **Clinical treatment recommendation systems** need their own guideline- and diagnosis-specific evidence review.
- No performance or clinical regulatory clearance of any combined toolchain has been established.

## Starting build proposal

Research prototype: clinician-entered scenario, simulated/deidentified DICOM series, deterministic consistency checks, one narrow pretrained model, image/mask comparison, source-linked draft findings, verified report, traceable follow-up. Benchmarks must cover safety and usefulness, not only Dice/AUC.

**Evidence rule:** Peer-reviewed publications support defined algorithms; standards/guidelines support clinical practice choices; GitHub repositories prove source availability but *not* clinical validity or weight/license suitability.
