# Medical AI Laboratory — Research Navigation

**Purpose:** navigate one-topic-per-file research. [Repository root](../README.md). Documents contain links to related analyses and publications. All medical findings require academic verification; technology feasibility is not clinical validation.

## Patient journey

[Complete patient journey](workflow/patient-journey.md) · [Specialty-specific pathways](workflow/diagnostic-specialties.md)

| Step | Stage file |
|---|---|
| 1 | [Care-seeking and referral](stages/01-care-seeking-referral.md) |
| 2 | [Patient registration](stages/02-patient-registration.md) |
| 3 | [Triage](stages/03-triage.md) |
| 4 | [Clinical assessment](stages/04-clinical-assessment.md) |
| 5 | [Diagnostic test ordering](stages/05-diagnostic-test-ordering.md) |
| 6 | [Scheduling and preparation](stages/06-scheduling-preparation.md) |
| 7 | [Diagnostic acquisition](stages/07-diagnostic-acquisition.md) |
| 8 | [Technical quality assurance](stages/08-technical-quality-assurance.md) |
| 9 | [Specialist interpretation](stages/09-specialist-interpretation.md) |
| 10 | [Result communication](stages/10-result-communication.md) |
| 11 | [Diagnostic synthesis](stages/11-diagnostic-synthesis.md) |
| 12 | [Management decision](stages/12-management-decision.md) |
| 13 | [Treatment and handoff](stages/13-treatment-handoff.md) |
| 14 | [Follow-up](stages/14-follow-up.md) |

## Research disciplines (single concern per file)

| Concern | Document |
|---|---|
| Diagnostic failure evidence | [Clinical failure evidence](evidence/diagnostic-failures.md) |
| Academic references | [References](evidence/references.md) |
| Hospital technical data exchange | [Interoperability and handoffs](interoperability/data-handoffs.md) |
| Specialty software stacks | [Open-source tools](tools/specialty-stacks.md) |
| Compute and license constraints | [Compute and licensing](tools/compute-and-licenses.md) |
| Product hypotheses | [Candidate products](opportunities/candidate-products.md) |
| Evidence verification process | [Research methodology](methods/research-method.md) |
| Unverified points | [Evidence gaps](methods/evidence-gaps.md) |

## Editorial rules

1. One Markdown file has one primary responsibility. Link to another concern instead of copying its content.
2. Each stage's software candidates belong in that stage's file; software used across specialties belongs in the specialty stack reference.
3. Clinical claims must link to academic publications; distinguish peer-reviewed studies, technical papers, reviews, guidelines and unvalidated hypotheses.
4. Every model/tool entry should link to source code or a launch/demo where available. Model weight and commercial dataset license require separate checks.
5. Update the relevant topic file and add links in this index as the research grows.

**Scope limit:** These are research workflows, not clinically approved diagnostic systems.

## Expanded diagnostic AI analysis

[Eight-stage diagnostic AI research](diagnostics/README.md) covers clinical conversation, examination choice, quality per modality, anatomy, disease, interpretation, screening, cross-modality synthesis, and clinician-led management. Each module is separately sourced and linked.

## Imaging-specific patient-to-management pathways

[Imaging modality research index](imaging/README.md) links independent ultrasound, radiography/mammography, CT, MRI, pathology/endoscopy, and multimodal workflows. Each examines patient conversation, indication, acquisition QC, anatomy, disease findings, reporting and human-supervised treatment/follow-up.

## Fifty disease and checkup research pathways

[50-condition registry, OpenCode agent and folder generator](../diseases/README.md) · [Disease registry CSV](../diseases/registry.csv) · [OpenCode agent instructions](../.opencode/agents/medical-disease-architect.md). Disease-specific folders are **scaffolded locally** by running `python3 scripts/scaffold_diseases.py`; they are not yet 50 completed evidence reviews.
