# Patient conversation and examination selection

[Diagnostic research index](README.md) · [Care assessment](../stages/04-clinical-assessment.md) · [Test ordering](../stages/05-diagnostic-test-ordering.md)

## Independent responsibility
Evaluate how reported symptoms, clinical history and clinician examination lead to a *clinician-approved* diagnostic test. This file does **not** implement autonomous diagnosis or prescribing.

## Required data and decisions
Patient concern; onset and time course; relevant history; medications/allergies; pregnancy status when relevant; physical examination; red flags; urgency; prior studies; patient preferences; potential tests' benefits, harms, availability and contraindications. Avoid a language-model generated examination order without clinician review.

## Open materials
| Component | Project | What it contributes | Readiness |
|---|---|---|---|
| Voice transcription | [Whisper](https://github.com/openai/whisper) | Transcription of consultation audio | Research; medical terminology errors possible |
| Clinical negation / section extraction | [medSpaCy](https://github.com/medspacy/medspacy) | Contextual entity extraction from notes | Open framework; validate local language and terminology |
| Biomedical entity representation | [scispaCy](https://github.com/allenai/scispacy) | Biomedical terminology matching | No independent diagnostic reasoning |
| Structured orders | [HAPI FHIR](https://github.com/hapifhir/hapi-fhir) | Patient, Encounter, ServiceRequest and Observation API | Infrastructure |
| Rules-based decision support | [OpenCDS](https://www.opencds.org/) | Rule/standard-based CDS implementation | Guidelines and local governance required |
| Imaging appropriateness | [ACR Appropriateness Criteria](https://acsearch.acr.org/) | Expert guidance for *indications*, not open-source executable code | Guidance, terms must be reviewed |

## Evidence
- National Academies, *Improving Diagnosis in Health Care* (2015), diagnostic process: https://www.ncbi.nlm.nih.gov/books/NBK338593/ (consensus, not a tool evaluation).
- Eyre et al., *Launching into clinical space with medSpaCy*, AMIA Symposium Proceedings (2021): https://arxiv.org/abs/2106.07799 (software methodology).
- ACR Appropriateness Criteria: https://acsearch.acr.org/ (expert guidance, not proof of algorithm accuracy).
- OpenCDS architecture: https://www.opencds.org/ (project documentation; no specific prospective clinical trial verified here).

## Prototype and evaluation
Simulate clinician-authored cases and guideline-aligned orders. Extract explicit symptom facts, show uncertainty and source text, check fields and suggest *guideline pages for clinician consultation* rather than prescribe tests. Evaluate extraction F1, indication completeness, citation accuracy, unsupported suggestion rate and clinician review time. No evidence here supports deploying an autonomous text-to-examination engine.
