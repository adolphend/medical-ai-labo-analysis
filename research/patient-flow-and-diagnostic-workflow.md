# Evidence-based patient flow and diagnostic workflow analysis

**Date:** 2026-10-16  
**Status:** Research synthesis, not clinical guidance  
**Scope:** General patient flow, with a detailed focus on diagnostic services, handoffs, and opportunities for low-compute software.

## Executive summary

Healthcare is not a linear chain of symptoms → test → diagnosis → treatment. The diagnostic process is iterative: information gathering, interpretation, hypothesis revision, communication, treatment, and reassessment can take place in different orders. This framework is based primarily on the National Academies' 2015 consensus report, *Improving Diagnosis in Health Care*.

No uniform hospital workflow applies across primary care, emergency, inpatient, ambulatory specialty, pathology, and radiology. This document describes a reference workflow and identifies which specifics require local validation.

## 1. Reference patient journey

| Stage | Actors | Inputs / events | Output or decision | Common risks |
|---|---|---|---|---|
| 1. Health concern and care seeking | Patient, caregiver | Symptoms, screening, referral | Encounter or self-care | Delayed presentation or barriers to access |
| 2. Registration and identification | Administrative team, nurse | Identity, demographic and prior record | Correct patient encounter | Wrong patient or duplicate records |
| 3. Triage and urgency assessment | Nurse, treating clinician | Complaint, vital signs, red flags | Care priority and location | Failure to recognize deterioration |
| 4. Clinical history and examination | Patient, treating clinician | History, examination, risk factors | Differential/working diagnosis | Missing or misleading information |
| 5. Diagnostic strategy | Treating clinician, specialists | Clinical question, probable alternatives | Test order, referral, observation, or no test | Inappropriate or incomplete order |
| 6. Scheduling and preparation | Diagnostic service | Order, preparation and safety requirements | Examination ready | Delay, mismatch, contraindication missed |
| 7. Diagnostic acquisition | Radiographer, sonographer, lab professional | Patient/sample, protocol, equipment | Images, waveforms, specimen results | Artifact, sample error, wrong label |
| 8. Technical/analytical quality check | Diagnostic service | Raw acquisition and QC indicators | Accepted, repeated, or qualified data | Poor quality undetected |
| 9. Interpretation and reporting | Radiologist, pathologist, lab specialist | Results, prior studies, clinical context | Preliminary/final report and uncertainty | Reporting or interpretation error |
| 10. Results routing and acknowledgement | Diagnostic and clinical teams | Verified report, critical notification | Responsible clinician receives result | Missing follow-up, poor handoff |
| 11. Diagnostic synthesis | Treating clinician, patient | History, exam, results, specialist advice | Refined/verified diagnosis or further testing | Premature closure, conflicting evidence |
| 12. Management decision | Clinician and patient | Diagnosis, preferences, treatment options | Agreed plan | Plan not communicated |
| 13. Treatment and transitions | Care team, patient | Interventions, medication, referral/discharge | Care delivered and handoff | Fragmentation |
| 14. Follow-up and reassessment | Patient, clinician, care coordinator | Response and outstanding results | Updated assessment/plan | Lost to follow-up |

**Important:** The pathway is cyclical. Treatment may start under uncertainty; response to treatment may change the working diagnosis. Testing is not universally required.

## 2. Diagnostic subworkflows

### Radiology
1. Treating clinician documents the clinical question and places an appropriate order.
2. RIS/EHR processes the order, scheduling, patient preparation and protocol selection.
3. Staff verify patient identity, appropriate examination and safety prerequisites.
4. Technologist or qualified clinician acquires images and checks technical quality.
5. DICOM images and metadata transfer to PACS/VNA; image completeness and reconciliation are checked.
6. Radiologist interprets images, considers priors and clinical information, and signs a report.
7. Critical/unexpected findings may require nonroutine direct communication.
8. Referring clinician integrates the report into management, communicates with the patient, and ensures follow-up.

IHE Scheduled Workflow describes orders, scheduling, acquisition, storage and viewing, including DICOM Modality Worklist, MPPS and Storage Commitment. The ACR practice parameter addresses communicating diagnostic imaging findings.

### Laboratory medicine
1. Clinical indication and laboratory order.
2. Patient identification, specimen collection and labeling.
3. Specimen transport and receipt.
4. Preanalytical checks (correct sample, integrity, adequacy).
5. Analytical measurement with quality controls.
6. Verification, reference intervals/flags and report release.
7. Result routing, review and action.
8. Repeat sampling or follow-up where indicated.

### Pathology
1. Procedure/specimen order and clinical history.
2. Specimen collection, labeling and accessioning.
3. Fixation and preparation; slide creation and quality assessment.
4. Microscopic/digital evaluation, ancillary testing as appropriate.
5. Pathologist report, clinically significant communications.
6. Multidisciplinary interpretation and subsequent care.

### Cardiology and physiological testing
1. Indication for ECG, echo or monitoring.
2. Preparation, lead/probe/device placement.
3. Acquisition and signal/image quality assessment.
4. Measurements and specialist interpretation as appropriate.
5. Result communication, clinical synthesis, management and reassessment.

These are generalized operational maps; specialist workflows and national requirements differ.

## 3. Evidence-based failure points

- **Missed follow-up:** AHRQ's diagnostic safety issue brief reports that reviewed studies found 6.8–62% of abnormal laboratory results and 1.0–35.7% of abnormal imaging results were not followed up. These are heterogeneous study ranges, *not* universal hospital rates.
- **Closed-loop communication:** A result must not merely exist in an EHR. Responsibility for receipt, acknowledgement, action and patient communication must be clear.
- **Care transitions:** Fragmented systems and transfers between clinicians/organizations may cause loss of context or responsibility.
- **Diagnostic reasoning:** Initial hypotheses may be revised as evidence arrives; contradictory evidence and diagnostic uncertainty require explicit management.
- **Image-data integrity:** IHE standards describe mechanisms for maintaining consistent identifiers and acquisition/storage status across systems.

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

## 6. Research methodology for the repository

1. Define care setting and specialty; do not generalize results across settings.
2. Draw process maps with responsible actors, data objects, decisions, exceptions and timeouts.
3. Extract evidence for failure modes from guidelines, systematic reviews and local data.
4. Interview clinicians and technical staff; compare the stated pathway with real practice.
5. Measure baseline failure rates, turnaround times, redundant entries and user burden.
6. Review incumbent EHR/PACS/RIS/LIS functionality before proposing a new tool.
7. Test a synthetic/deidentified workflow prototype using deterministic checks before adding pretrained AI.
8. Evaluate clinical safety, intended use, privacy, interoperability and applicable medical-device regulations before any real-world deployment.

## 7. Primary sources and papers

1. National Academies (2015), *Improving Diagnosis in Health Care*, Ch. 2: https://www.ncbi.nlm.nih.gov/books/NBK338593/
2. National Academies (2018), *Crossing the Global Quality Chasm*: https://www.nationalacademies.org/read/25152/chapter/4
3. WHO (2024), *Global Patient Safety Report*: https://www.who.int/publications/i/item/9789240095458/
4. AHRQ, *Diagnostic Safety: Current State of the Field*, Results: https://www.ahrq.gov/diagnostic-safety/resources/issue-briefs/dxsafety-current-state3.html
5. Callen et al., *Failure to Follow-Up Test Results for Ambulatory Patients: A Systematic Review*, J Gen Intern Med, doi:10.1007/s11606-011-1949-5 — https://psnet.ahrq.gov/issue/failure-follow-test-results-ambulatory-patients-systematic-review
6. IHE, *Scheduled Workflow*: https://wiki.ihe.net/index.php/Scheduled_Workflow
7. ACR, *Practice Parameter for Communication of Diagnostic Imaging Findings*: https://gravitas.acr.org/PPTS/GetDocumentView?docId=74
8. The Joint Commission, *National Performance Goal #1, Right Patient, Right Care*: https://www.jointcommission.org/en-us/standards/national-performance-goals/right-patient-right-care
9. Lacson et al., *Impact of an electronic alert notification system ...*, BMJ Quality & Safety, doi:10.1136/bmjqs-2015-004276 — https://qualitysafety.bmj.com/content/25/7/518
10. Moore et al. (2023), *Best Practices in Communication and Management of Actionable Incidental Findings*, JACR, doi:10.1016/j.jacr.2023.01.001 — https://pubmed.ncbi.nlm.nih.gov/36922265/
11. AHRQ, *Safer Dx e-Triggers*: https://www.ahrq.gov/patient-safety/reports/issue-briefs/state-of-science-2b.html

## Limitations

This is a literature-backed generic workflow, not an empirical observation of one hospital. The available evidence is not equivalent to local incidence rates, and no user interviews or site-specific timing measurements have been conducted. No proposed software is clinically validated or authorized for diagnostic care.
