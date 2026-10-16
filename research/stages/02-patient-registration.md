# Stage 2. Registration / patient ID

[Research index](../README.md) · [Patient journey](../workflow/patient-journey.md) · [References](../evidence/references.md) · [Clinical evidence](../evidence/diagnostic-failures.md)

## Open-source material

[OpenMRS patient registration](https://github.com/openmrs/openmrs-esm-patient-management), [HAPI FHIR](https://github.com/hapifhir/hapi-fhir)

## Academic support

W0 supports maintaining reliable patient information; **no patient-ID outcome validation paper verified for these particular modules**

Evidence shorthand (W0, W1, W2, W3) is defined in [the original evidence map](../patient-flow-and-diagnostic-workflow.md), retained for traceability. An academic paper supporting a technology is not evidence of improved patient outcomes.

## Feasible first prototype (no new model training)

Duplicate-record warning using synthetic identifiers and FHIR Patient resources

## Limitations and verification needs

Must not infer patient identity using image/LLM resemblance

## Related analysis

- [Diagnostic specialty workflows](../workflow/diagnostic-specialties.md)
- [Technical interoperability and handoffs](../interoperability/data-handoffs.md)
- [Research methodology](../methods/research-method.md)
