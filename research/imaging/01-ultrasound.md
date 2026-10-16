# Ultrasound and Doppler: complete diagnostic workflow

[Imaging category index](README.md) · [Central diagnostic research](../diagnostics/README.md) · [Evidence approach](../methods/research-method.md)

**Scope:** Heart failure/reduced EF, valvular abnormalities; obstetric structural/growth concerns; hydronephrosis; gallstones/cholecystitis; thyroid nodules; DVT; AAA; pleural effusion. Not all are screening indications.

Each pathway is **human-supervised research software**, not an autonomous diagnosis/treatment system. Stages: consultation → appropriate imaging decision → acquisition and quality → anatomy → findings → reporting → clinician-managed care and follow-up. When a tool is a framework rather than a pretrained validated model, this is stated.

## 1. Patient conversation and clinical assessment
Use [Whisper](https://github.com/openai/whisper) for optional draft transcription and [medSpaCy](https://github.com/medspacy/medspacy) for source-linked clinical phrase extraction. A clinician verifies patient history, examination, red flags and differential; neither tool performs accurate autonomous triage.

## 2. Selection of examination
Use specialty protocols and clinician-selected clinical questions; [ACR Appropriateness Criteria](https://www.acr.org/Clinical-Resources/Clinical-Tools-and-Reference/Appropriateness-Criteria) provide guidance, not executable freely licensed models.

## 3. Acquisition and quality assessment
[SonoNet weights](https://github.com/baumgach/SonoNet-weights) recognizes **fetal ultrasound standard planes only** (Baumgartner et al. 2017, [DOI](https://doi.org/10.1109/TMI.2017.2712367)); not general ultrasound image acceptance. For other targets establish plane/coverage/technical quality with specialist-defined reference standards; no universal open model identified.

## 4. Anatomical localization and quantitative measurements
[EchoNet-Dynamic](https://github.com/echonet/dynamic) segments left ventricle in cardiac echo video; [MedSAM](https://github.com/bowang-lab/MedSAM) interactive prompt-based segmentation for research, not automatic organ identification. For kidney/aorta/thyroid tasks a verified pretrained checkpoint remains to be selected.

## 5. Findings and disease-specific inference
[EchoNet-Dynamic](https://github.com/echonet/dynamic) estimates ejection fraction and supports research into reduced EF/cardiomyopathy. Ouyang et al. Nature 2020 [DOI](https://doi.org/10.1038/s41586-020-2145-8). Gallstones, AAA, hydronephrosis, DVT require separate task-specific models or rule-plus-manual measurement; no universal ready-made detector established.

## 6. Interpretation and report generation
Video/study + time stamps + measurements + view adequacy + clinician-reviewed impression; no automatic final diagnosis.

Reusable software: [OHIF](https://github.com/OHIF/Viewers) and [3D Slicer](https://github.com/Slicer/Slicer) where image type allows, [RadGraph](https://github.com/Stanford-AIMI/radgraph) for NLP of radiology reports, and [CheXbert](https://github.com/stanfordmlgroup/CheXbert) specifically for chest X-ray report labels. A text model must not invent observations or auto-sign.

## 7. Treatment decisions, communication and follow-up
Clinician links verified measurements to cardiology/obstetric/vascular guidelines, may seek repeat studies/referral, documents action and follows up. No autonomous treatment engine.

[HAPI FHIR](https://github.com/hapifhir/hapi-fhir) can exchange structured encounters/orders/reports; [Medplum](https://github.com/medplum/medplum) can support a tracked event workflow. These are infrastructure, not validated autonomous treatment recommenders.

## Hardware, licensing and first prototype
SonoNet and smaller 2D image processing feasible for exploratory CPU trials; EchoNet video inference may be relatively slow. EchoNet data have noncommercial terms even though code is MIT.

**Research direction:** Prioritize ultrasound **exam quality and specific organ measurement**, not a general all-disease predictor.

## Academic evidence and validation requirements
Papers are linked at each relevant component above. The overarching diagnostic-process framework is from the [National Academies report](https://www.ncbi.nlm.nih.gov/books/NBK338593/) (consensus, not a clinical trial). Test each module for external validity, subgroup performance, false alarms, human correction, source provenance, measured computational cost and licensing. **No claimed clinical outcome benefit of the integrated stack has been established.**
