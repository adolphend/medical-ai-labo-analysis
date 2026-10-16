# Unvalidated product hypotheses, with measurable outcomes.

[Research index](../README.md) · [Academic references](../evidence/references.md)

## 5. Candidate startup opportunities (hypotheses, not proven demand)

| Idea | User | Model training necessary? | Measurable pilot outcome | Main caution |
|---|---|---|---|---|
| Imaging order completeness checker | Ordering clinician/radiology intake | No | Missing-field rate, rejected orders | Cannot autonomously select examinations |
| DICOM study consistency validator | Imaging IT/technologist | No | Detected mismatches, false alarms | Must avoid exposing patient data |
| Image/report reconciliation | Radiologist | Rules initially; optional existing NLP | Laterality/report contradiction detection | Should not act as autonomous reader |
| Critical-result closed-loop tracker | Department/clinical team | No | Acknowledgement and action time | Must integrate with actual workflow |
| Diagnostic episode timeline | Care coordinator/clinician | No | Missing-record retrieval and time saved | Access and record reconciliation complexity |
| ECG acquisition quality checker | Technician/cardiology service | No for classical DSP | Signal-quality metric agreement | Clinical limits of QC scores |
| Pathology specimen-chain validator | Pathology lab | No | Label or process mismatch rates | Local LIS integration required |

**Provisional research priority:** (1) DICOM integrity and study completeness, (2) report/action closed-loop tracking, (3) structured diagnostic episode timeline. These have a plausible training-free first prototype and measurable outputs. Customer demand and competing solutions are not yet established.
