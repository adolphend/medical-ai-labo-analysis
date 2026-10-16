# Microscopy, digital pathology, and endoscopy: complete diagnostic workflow

[Imaging category index](README.md) · [Central diagnostic research](../diagnostics/README.md) · [Evidence approach](../methods/research-method.md)

**Scope:** Histopathological cancer assessment, tissue abnormalities, cellular morphology; endoscopy detects visual mucosal abnormalities and often requires biopsy for confirmation. These are **not interchangeable** with CT/MRI.

Each pathway is **human-supervised research software**, not an autonomous diagnosis/treatment system. Stages: consultation → appropriate imaging decision → acquisition and quality → anatomy → findings → reporting → clinician-managed care and follow-up. When a tool is a framework rather than a pretrained validated model, this is stated.

## 1. Patient conversation and clinical assessment
Use [Whisper](https://github.com/openai/whisper) for optional draft transcription and [medSpaCy](https://github.com/medspacy/medspacy) for source-linked clinical phrase extraction. A clinician verifies patient history, examination, red flags and differential; neither tool performs accurate autonomous triage.

## 2. Selection of examination
Clinician chooses endoscopy or tissue sampling for a clinical indication; specimen provenance and processing are necessary.

## 3. Acquisition and quality assessment
[HistoQC](https://github.com/choosehappy/HistoQC) assesses whole-slide artifacts/focus/staining; [QuPath](https://github.com/qupath/qupath) supports microscopy review (Bankhead et al. 2017 [DOI](https://doi.org/10.1038/s41598-017-17204-5)).

## 4. Anatomical localization and quantitative measurements
[Cellpose](https://github.com/MouseLand/cellpose) cell masks; [HoVer-Net](https://github.com/vqdang/hover_net) nuclei segmentation/classification (Graham et al. 2019 [DOI](https://doi.org/10.1016/j.media.2019.101563)). Histology tissue structure differs from macroscopic organs.

## 5. Findings and disease-specific inference
Morphology features and nuclei class distributions can support research; pathology diagnosis needs qualified pathologist and sufficient tissue context, immunostains/ancillary testing as needed. No universal cancer classifier confirmed.

## 6. Interpretation and report generation
Specimen ID, source, processing, fields examined, measurements, uncertainty and pathologist-signed report.

Reusable software: [OHIF](https://github.com/OHIF/Viewers) and [3D Slicer](https://github.com/Slicer/Slicer) where image type allows, [RadGraph](https://github.com/Stanford-AIMI/radgraph) for NLP of radiology reports, and [CheXbert](https://github.com/stanfordmlgroup/CheXbert) specifically for chest X-ray report labels. A text model must not invent observations or auto-sign.

## 7. Treatment decisions, communication and follow-up
Treating team incorporates pathology type/stage and other clinical findings to select appropriate multidisciplinary care.

[HAPI FHIR](https://github.com/hapifhir/hapi-fhir) can exchange structured encounters/orders/reports; [Medplum](https://github.com/medplum/medplum) can support a tracked event workflow. These are infrastructure, not validated autonomous treatment recommenders.

## Hardware, licensing and first prototype
ROI/patch analysis often modest; full whole-slide tiling and storage can be demanding.

**Research direction:** Focus on QC, segmentation and report integrity before proposing automated tumor grading.

## Academic evidence and validation requirements
Papers are linked at each relevant component above. The overarching diagnostic-process framework is from the [National Academies report](https://www.ncbi.nlm.nih.gov/books/NBK338593/) (consensus, not a clinical trial). Test each module for external validity, subgroup performance, false alarms, human correction, source provenance, measured computational cost and licensing. **No claimed clinical outcome benefit of the integrated stack has been established.**
