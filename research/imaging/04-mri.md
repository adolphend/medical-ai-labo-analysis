# Magnetic Resonance Imaging (MRI): complete diagnostic workflow

[Imaging category index](README.md) · [Central diagnostic research](../diagnostics/README.md) · [Evidence approach](../methods/research-method.md)

**Scope:** Brain tumor or lesion, stroke in selected pathways, multiple sclerosis lesion evaluation, musculoskeletal injuries, prostate assessment, spinal cord and nerve-related structures where modality/protocol adequate.

Each pathway is **human-supervised research software**, not an autonomous diagnosis/treatment system. Stages: consultation → appropriate imaging decision → acquisition and quality → anatomy → findings → reporting → clinician-managed care and follow-up. When a tool is a framework rather than a pretrained validated model, this is stated.

## 1. Patient conversation and clinical assessment
Use [Whisper](https://github.com/openai/whisper) for optional draft transcription and [medSpaCy](https://github.com/medspacy/medspacy) for source-linked clinical phrase extraction. A clinician verifies patient history, examination, red flags and differential; neither tool performs accurate autonomous triage.

## 2. Selection of examination
Clinician chooses MRI based on presentation, contraindications, implants, sequences and time sensitivity; CT may be more appropriate in some emergencies.

## 3. Acquisition and quality assessment
[MRIQC](https://github.com/nipreps/mriqc) provides neuro-MRI quality indicators and trained quality classifier (Esteban et al. 2017 [DOI](https://doi.org/10.1371/journal.pone.0184661)); published cross-site generalization was limited (~76% accuracy). Not a universal MRI quality gate.

## 4. Anatomical localization and quantitative measurements
[ANTs](https://github.com/ANTsX/ANTs) and [ANTsPyNet](https://github.com/ANTsX/ANTsPyNet) brain registration/extraction; [MONAI model zoo](https://github.com/Project-MONAI/model-zoo) task-specific pretrained bundles; [MedSAM](https://github.com/bowang-lab/MedSAM) interactive segmentation.

## 5. Findings and disease-specific inference
Select verified task/sequence-specific weights, e.g. brain lesions or prostate subregion segmentation; [nnU-Net](https://github.com/MIC-DKFZ/nnUNet) is a framework and **not** preloaded with universal diagnostic weights (Isensee et al. 2021 [DOI](https://doi.org/10.1038/s41592-020-01008-z)).

## 6. Interpretation and report generation
Record sequences, anatomy, lesion measurements, uncertainties, prior studies and explicit specialist validation.

Reusable software: [OHIF](https://github.com/OHIF/Viewers) and [3D Slicer](https://github.com/Slicer/Slicer) where image type allows, [RadGraph](https://github.com/Stanford-AIMI/radgraph) for NLP of radiology reports, and [CheXbert](https://github.com/stanfordmlgroup/CheXbert) specifically for chest X-ray report labels. A text model must not invent observations or auto-sign.

## 7. Treatment decisions, communication and follow-up
Clinical specialists integrate MRI, clinical features, and sometimes biopsy/pathology before deciding treatment; imaging alone does not necessarily establish histological diagnosis.

[HAPI FHIR](https://github.com/hapifhir/hapi-fhir) can exchange structured encounters/orders/reports; [Medplum](https://github.com/medplum/medplum) can support a tracked event workflow. These are infrastructure, not validated autonomous treatment recommenders.

## Hardware, licensing and first prototype
MRIQC can run CPU but volumes/processing are nontrivial; MONAI/3D deep models may be slow/heavy.

**Research direction:** Begin with neuro-MRI QC and a narrowly defined segmentation model, not pan-MRI diagnosis.

## Academic evidence and validation requirements
Papers are linked at each relevant component above. The overarching diagnostic-process framework is from the [National Academies report](https://www.ncbi.nlm.nih.gov/books/NBK338593/) (consensus, not a clinical trial). Test each module for external validity, subgroup performance, false alarms, human correction, source provenance, measured computational cost and licensing. **No claimed clinical outcome benefit of the integrated stack has been established.**
