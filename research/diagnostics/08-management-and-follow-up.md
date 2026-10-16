# Management options, clinical decision support and follow-up

[Diagnostic research index](README.md) · [Reporting](05-interpretation-and-reporting.md) · [Clinical decisions](../stages/12-management-decision.md) · [Follow-up](../stages/14-follow-up.md)

## Responsibility
Surface clinical evidence and follow clinician-approved management actions, with provenance, explicit role boundaries and closed-loop monitoring. This is **not** an autonomous treatment prescription engine.

| Component | Open-source material | Evidence and gap |
|---|---|---|
| Structured clinical decision rules | [OpenCDS](https://www.opencds.org/) | Software/project evidence; requires validated specialty guidelines and clinician governance |
| Evidence resources and interoperability | [HAPI FHIR](https://github.com/hapifhir/hapi-fhir) | FHIR infrastructure; does not independently establish benefit |
| Task lifecycle and patient record | [Medplum](https://github.com/medplum/medplum), [OpenMRS](https://github.com/openmrs/openmrs-core) | Technical platform; outcome trials for proposed implementation not verified |
| Clinical note/context extraction | [medSpaCy](https://github.com/medspacy/medspacy) | Eyre et al. (2021) technical paper: https://arxiv.org/abs/2106.07799 |
| Result follow-up evidence | No model necessary; event-driven state machine | Callen et al., *Failure to Follow-Up Test Results for Ambulatory Patients: A Systematic Review* (2012), DOI [10.1007/s11606-011-1949-5](https://doi.org/10.1007/s11606-011-1949-5) |

## Proposed audited state machine
Diagnostic report received → responsible clinician identified → acknowledged → action decided → patient informed → follow-up booked/performed → closed. Add exception states: pending, urgent escalation, unable to contact, transferred responsibility, documented no-action. The specific deadlines and escalations are hospital-policy dependent.

## Treatment guidance boundaries
A document retrieval system may show original guideline recommendations and their publication/version dates. It must not conflate association with causation, invent a treatment from a radiographic finding, recommend patient-specific medication or substitute clinician consent/assessment. Guideline licensing and national differences must be checked.

## Success measures
Verified follow-up completion, time to action, percentage of orphaned test results, false alerts per clinician, documentation burden, missed escalation rate and clinician/patient usability. Research-stage evidence does not establish deployment fitness.
