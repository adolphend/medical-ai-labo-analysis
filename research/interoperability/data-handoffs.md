# Data passed across clinical and diagnostic systems.

[Research index](../README.md) · [Academic references](../evidence/references.md)

## 4. Technology and data handoffs

| Link | Typical information | Common systems/standards |
|---|---|---|
| Registration → consultation | Patient and encounter | EHR/HIS, HL7 ADT, FHIR Patient/Encounter |
| Clinician → diagnostic department | Order, indication, laterality, priority | CPOE/EHR, RIS/LIS, HL7 v2, FHIR ServiceRequest |
| RIS → modality | Worklist/procedure metadata | DICOM Modality Worklist |
| Modality → archive | Images, instances, study identifiers | DICOM, PACS/VNA |
| Diagnostic specialist → clinician | Signed report, urgent notification | RIS/LIS/EHR, HL7 ORU, FHIR DiagnosticReport |
| Clinician → patient / next care site | Explained result, plan, outstanding tasks | Patient portal, EHR, referral/discharge documents |

Mappings vary by institution and standards implementation.
