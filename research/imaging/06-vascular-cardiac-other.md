# Vascular, cardiac signals, and multimodality diagnostics: complete diagnostic workflow

[Imaging category index](README.md) · [Central diagnostic research](../diagnostics/README.md) · [Evidence approach](../methods/research-method.md)

**Scope:** Arrhythmia (ECG, not an imaging modality), structural heart disease (echo/MRI/CT), thrombosis (Doppler ultrasound), arterial stenosis (Doppler/CT angiography), pulmonary processes (ultrasound/X-ray/CT), and combined workups.

Each pathway is **human-supervised research software**, not an autonomous diagnosis/treatment system. Stages: consultation → appropriate imaging decision → acquisition and quality → anatomy → findings → reporting → clinician-managed care and follow-up. When a tool is a framework rather than a pretrained validated model, this is stated.

## 1. Patient conversation and clinical assessment
Use [Whisper](https://github.com/openai/whisper) for optional draft transcription and [medSpaCy](https://github.com/medspacy/medspacy) for source-linked clinical phrase extraction. A clinician verifies patient history, examination, red flags and differential; neither tool performs accurate autonomous triage.

## 2. Selection of examination
Examination selection depends on problem: some conditions require no imaging; use ECG or laboratory tests first where appropriate. No single model determines correct examination universally.

## 3. Acquisition and quality assessment
[WFDB](https://github.com/MIT-LCP/wfdb-python) and [NeuroKit2](https://github.com/neuropsychology/NeuroKit) for ECG signal quality (Makowski et al. 2021 [DOI](https://doi.org/10.3758/s13428-020-01516-y)); modality-specific DICOM QC for actual imaging.

## 4. Anatomical localization and quantitative measurements
EchoNet-Dynamic for echo LV; TotalSegmentator for CT; MRI-specific tools for relevant structures. Cross-modal registration with [SimpleITK](https://github.com/SimpleITK/SimpleITK) only for physically compatible cases.

## 5. Findings and disease-specific inference
Use separate validated ECG, ultrasound, CT or MRI models. Combining outputs does not make the result independently validated as a disease diagnosis.

## 6. Interpretation and report generation
Structured encounter timeline with signal, image, reports and source-linked evidence, using [HAPI FHIR](https://github.com/hapifhir/hapi-fhir).

Reusable software: [OHIF](https://github.com/OHIF/Viewers) and [3D Slicer](https://github.com/Slicer/Slicer) where image type allows, [RadGraph](https://github.com/Stanford-AIMI/radgraph) for NLP of radiology reports, and [CheXbert](https://github.com/stanfordmlgroup/CheXbert) specifically for chest X-ray report labels. A text model must not invent observations or auto-sign.

## 7. Treatment decisions, communication and follow-up
Clinician-based diagnosis and decisions; results acknowledgement, referral and follow-up are tracked using [Medplum](https://github.com/medplum/medplum) or similar.

[HAPI FHIR](https://github.com/hapifhir/hapi-fhir) can exchange structured encounters/orders/reports; [Medplum](https://github.com/medplum/medplum) can support a tracked event workflow. These are infrastructure, not validated autonomous treatment recommenders.

## Hardware, licensing and first prototype
Rule-based coordination and ECG preprocessing low-compute; multi-modal image inference varies.

**Research direction:** Start with safe result reconciliation and clinician-facing task tracking. Evaluate combined-model errors independently.

## Academic evidence and validation requirements
Papers are linked at each relevant component above. The overarching diagnostic-process framework is from the [National Academies report](https://www.ncbi.nlm.nih.gov/books/NBK338593/) (consensus, not a clinical trial). Test each module for external validity, subgroup performance, false alarms, human correction, source provenance, measured computational cost and licensing. **No claimed clinical outcome benefit of the integrated stack has been established.**
