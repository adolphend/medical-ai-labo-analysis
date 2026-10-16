# Radiography / X-ray and mammography: complete diagnostic workflow

[Imaging category index](README.md) · [Central diagnostic research](../diagnostics/README.md) · [Evidence approach](../methods/research-method.md)

**Scope:** Chest radiograph findings (possible pneumonia, pneumothorax, effusion, edema, cardiomegaly); fractures; breast cancer screening by mammography in appropriate groups. Mammography is a distinct specialized X-ray workflow.

Each pathway is **human-supervised research software**, not an autonomous diagnosis/treatment system. Stages: consultation → appropriate imaging decision → acquisition and quality → anatomy → findings → reporting → clinician-managed care and follow-up. When a tool is a framework rather than a pretrained validated model, this is stated.

## 1. Patient conversation and clinical assessment
Use [Whisper](https://github.com/openai/whisper) for optional draft transcription and [medSpaCy](https://github.com/medspacy/medspacy) for source-linked clinical phrase extraction. A clinician verifies patient history, examination, red flags and differential; neither tool performs accurate autonomous triage.

## 2. Selection of examination
Clinician applies indication-specific guidance (e.g. chest symptoms, suspected fracture, breast screening eligibility) through [ACR](https://www.acr.org/Clinical-Resources/Clinical-Tools-and-Reference/Appropriateness-Criteria). X-ray is **not** a substitute for low-dose CT lung-cancer screening.

## 3. Acquisition and quality assessment
[pydicom](https://github.com/pydicom/pydicom), [OpenCV](https://github.com/opencv/opencv) for view, tag, exposure proxy, completeness and position checks. No clinically validated universal open-weight X-ray quality classifier established in this inventory.

## 4. Anatomical localization and quantitative measurements
[MedSAM](https://github.com/bowang-lab/MedSAM) for user-prompted outlines; anatomical labels require separately validated model. [OHIF](https://github.com/OHIF/Viewers) for image review.

## 5. Findings and disease-specific inference
[TorchXRayVision](https://github.com/mlmed/torchxrayvision) pretrained chest X-ray finding models; [CheXzero](https://github.com/rajpurkarlab/CheXzero) zero-shot chest observations (Tiu et al. 2022, [DOI](https://doi.org/10.1038/s41551-022-00936-9)). These findings are *not* definitive pneumonia/cancer diagnoses. Mammography and fracture tasks need separate weights/evidence.

## 6. Interpretation and report generation
[CheXbert](https://github.com/stanfordmlgroup/CheXbert) and [RadGraph](https://github.com/Stanford-AIMI/radgraph) process reports; do not prove image conclusions. Human verification of laterality, impression, urgency.

Reusable software: [OHIF](https://github.com/OHIF/Viewers) and [3D Slicer](https://github.com/Slicer/Slicer) where image type allows, [RadGraph](https://github.com/Stanford-AIMI/radgraph) for NLP of radiology reports, and [CheXbert](https://github.com/stanfordmlgroup/CheXbert) specifically for chest X-ray report labels. A text model must not invent observations or auto-sign.

## 7. Treatment decisions, communication and follow-up
Clinical examination + report + possible additional tests (e.g. CT or laboratory). Follow established disease-specific guidelines; clinician determines actions. No direct drug selection from a predicted chest finding.

[HAPI FHIR](https://github.com/hapifhir/hapi-fhir) can exchange structured encounters/orders/reports; [Medplum](https://github.com/medplum/medplum) can support a tracked event workflow. These are infrastructure, not validated autonomous treatment recommenders.

## Hardware, licensing and first prototype
2D chest models are relatively accessible for CPU experiments; mammography diagnostic validation and licensed data separate.

**Research direction:** Define individual findings and patient populations; benchmark false alerts, sensitivity, dataset shift and clinician impact.

## Academic evidence and validation requirements
Papers are linked at each relevant component above. The overarching diagnostic-process framework is from the [National Academies report](https://www.ncbi.nlm.nih.gov/books/NBK338593/) (consensus, not a clinical trial). Test each module for external validity, subgroup performance, false alarms, human correction, source provenance, measured computational cost and licensing. **No claimed clinical outcome benefit of the integrated stack has been established.**
