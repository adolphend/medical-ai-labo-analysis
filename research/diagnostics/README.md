# End-to-end diagnostic AI research index

[Main research index](../README.md) · [Patient journey](../workflow/patient-journey.md) · [Academic evidence](../evidence/references.md)

**Status:** scoped literature review / engineering assessment (2026-10-16). Not a comprehensive systematic review; not clinical software. Each document has **one responsibility** and links to adjacent responsibilities.

| Step | Dedicated analysis |
|---|---|
| 1 | [Patient conversation and appropriate examinations](01-conversation-and-examination-selection.md) |
| 2 | [Acquisition quality: ultrasound, X-ray, MRI, CT, pathology, ECG](02-acquisition-quality.md) |
| 3 | [Anatomical localization: organs, tissues, vessels, nerves, cellular/protein scope](03-anatomical-localization.md) |
| 4 | [Imaging abnormalities and disease-specific detectors](04-abnormality-and-disease-detection.md) |
| 5 | [Interpretation, report drafts and verification](05-interpretation-and-reporting.md) |
| 6 | [Early detection, screening diseases, benefits and trade-offs](06-screening-and-early-detection.md) |
| 7 | [Cross-modality registration and synthetic imaging](07-cross-modality-translation.md) |
| 8 | [Treatment evidence, decision support and follow-up](08-management-and-follow-up.md) |

## Distinct cross-cutting analyses
- [Existing platform interoperability](../interoperability/data-handoffs.md)
- [Open-source specialty stacks](../tools/specialty-stacks.md)
- [Compute and licensing](../tools/compute-and-licenses.md)
- [Candidate product hypotheses](../opportunities/candidate-products.md)
- [Research method](../methods/research-method.md)
- [Evidence gaps](../methods/evidence-gaps.md)

## Staged integration concept
1. Start with **deidentified/synthetic encounter**, keep source text and patient provenance.
2. Extract clinician-verifiable information and link appropriate guideline evidence; **clinician approves** investigation.
3. Ingest real available examination, validate identifiers and quality with modality-specific checks.
4. Use appropriately licensed pretrained components for *defined anatomical structures*.
5. Run narrowly scoped, externally evaluated finding models where available; otherwise explicitly state **no model available / not evaluated**.
6. Present machine findings alongside actual image and raw evidence; draft only a clinician-reviewed report.
7. Show applicable, sourced guidance but do not prescribe individualized treatment autonomously.
8. Record acknowledgements, actions and follow-up; expose unresolved findings.

**Alternative flows:** no imaging necessary, failed examination quality, pathology/laboratory after imaging, multiple concurrent tests, further testing required, unavailable model, clinician disagreement, emergency escalation, inability to reach patient.

## Engineering contracts
Each module returns: `patient_pseudonym`, `encounter_id`, `study_id` when appropriate, `source_type`, `created_at`, `evidence_links`, `software_version`, `weights_version`, `input_quality`, `output`, `uncertainty`, `human_review_status`, `audit_event_id`. Missing outputs remain missing rather than being fabricated.

For true clinical settings, de-identification, consent/lawful basis, access logging, security, privacy, cybersecurity, regulatory classification and specialist evaluation precede deployment.

## Decision framework
For each component evaluate: (a) peer-reviewed task validation and external cohorts; (b) open source **and** pretrained weights availability; (c) data and commercial licensing; (d) compute resources/latency on CPU; (e) safe failure mode; (f) competing solutions; (g) measurable clinical workflow benefit. Clinical benefit is not established simply because a GitHub project exists.

## Review conclusions
- First prototype candidate: **study metadata + quality checks + source-linked imaging report workflow** using public/synthetic data and deterministic tools.
- Second: specialist pretrained segmentation (one anatomically defined task).
- Third: clinically meaningful finding detection and cross-modal synthesis only after dedicated external validation.
- The goal is a *human-supervised modular diagnostic research platform*, not a universal autonomous doctor.
