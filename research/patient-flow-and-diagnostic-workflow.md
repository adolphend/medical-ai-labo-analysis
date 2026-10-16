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


---

# Open-source evidence map by patient-flow stage (expanded 2026-10-16)

## Interpretation and verification rules

This section maps **each of the 14 stages** to directly accessible, relevant open-source material, papers, and realistic integration opportunities. Two kinds of evidence are deliberately separated:

- **Clinical/workflow evidence (W):** a publication describing a clinical process, safety need or failure mode.
- **Tool/technical evidence (T):** a peer-reviewed publication demonstrating a software platform or computational method. A tool paper is **not** evidence that this tool improves clinical outcomes.
- **Repository (R):** accessible software source; an open repository is **not** necessarily a plug-and-play pretrained model, commercially unrestricted, maintained or approved for patient care.
- **Feasibility** refers only to a synthetic/de-identified research prototype with no new large-model training. Hospital integration requires local validation and safety assessment.

Foundational clinical evidence for the *entire diagnostic process*:
- **W0:** National Academies of Sciences, Engineering, and Medicine, *Improving Diagnosis in Health Care* (2015), ch. 2, https://www.ncbi.nlm.nih.gov/books/NBK338593/ (expert consensus report, **not** a peer-reviewed experimental study).
- **W1:** Callen JL et al., *Failure to Follow-Up Test Results for Ambulatory Patients: A Systematic Review*, J Gen Intern Med (2012). DOI: [10.1007/s11606-011-1949-5](https://doi.org/10.1007/s11606-011-1949-5) (systematic review, especially relevant to stages 10 and 14).
- **W2:** Jodogne S., *The Orthanc Ecosystem for Medical Imaging*, J Digit Imaging (2018). DOI: [10.1007/s10278-018-0082-y](https://doi.org/10.1007/s10278-018-0082-y) (technical peer-reviewed paper, imaging acquisition/storage/interface).
- **W3:** Eyre H et al., *Launching into clinical space with medspaCy: a new clinical text processing toolkit in Python*, AMIA Annu Symp Proc (2021), pp. 438–447; [paper](https://arxiv.org/abs/2106.07799) (peer-reviewed proceedings).

## Stage-by-stage inventory

| Stage | Open-source tools (source/launch) | Paper or research evidence | Realistic contribution without training | Caution |
|---|---|---|---|---|
| **1. Care-seeking / referral** | [OpenMRS](https://github.com/openmrs/openmrs-core), [patient management](https://github.com/openmrs/openmrs-esm-patient-management) | W0 (diagnosis unfolds from initial patient concerns); no stage-specific outcome paper confirmed for this exact module | Simulate referral intake and record provenance | OpenMRS is an EMR platform, not a triage AI model |
| **2. Registration / patient ID** | [OpenMRS patient registration](https://github.com/openmrs/openmrs-esm-patient-management), [HAPI FHIR](https://github.com/hapifhir/hapi-fhir) | W0 supports maintaining reliable patient information; **no patient-ID outcome validation paper verified for these particular modules** | Duplicate-record warning using synthetic identifiers and FHIR Patient resources | Must not infer patient identity using image/LLM resemblance |
| **3. Triage / urgency** | [OpenMRS service queues](https://github.com/openmrs/openmrs-esm-patient-management), [OpenCDS](https://www.opencds.org/) | W0 (diagnostic assessment); no verified trial of these specific triage modules | Record clinician-assigned acuity, wait times and escalation events | Do not invent automatic triage scores; no validated standalone model selected |
| **4. History / clinical examination** | [medSpaCy](https://github.com/medspacy/medspacy), [OpenMRS](https://github.com/openmrs/openmrs-core) | **T:** Eyre et al. 2021 (W3) | Section detection, negation/uncertainty extraction from synthetic clinical notes | Extraction is not correct diagnosis; language and context validation needed |
| **5. Test selection / ordering** | [OpenCDS](https://www.opencds.org/), [HAPI FHIR](https://github.com/hapifhir/hapi-fhir) | W0; clinical appropriateness standards can inform local rules but are **not model-evaluation papers** | Validate completeness of clinician-entered indication, body side, order and question | Do not automatically prescribe tests |
| **6. Scheduling / preparation** | [OpenMRS appointments](https://github.com/openmrs/openmrs-esm-patient-management), [Orthanc](https://github.com/orthanc-server/orthanc) (imaging services) | **T:** Jodogne 2018 (W2) for imaging information-flow architecture | Simulate order-to-worklist states, missing preparatory tasks | Orthanc is an imaging archive, not a hospital appointment system |
| **7. Acquisition (images / specimens / signals)** | [Orthanc](https://github.com/orthanc-server/orthanc), [OpenELIS Global 2](https://github.com/DIGI-UW/OpenELIS-Global-2), [WFDB Python](https://github.com/MIT-LCP/wfdb-python) | **T:** Jodogne 2018 for DICOM; [Makowski et al. 2021](https://doi.org/10.3758/s13428-020-01516-y) for physiological signals | Ingest synthetic DICOM, laboratory observations or ECG samples | Modality/specimen acquisition requires local equipment and controls |
| **8. Technical / analytical QC** | [pydicom](https://github.com/pydicom/pydicom), [HistoQC](https://github.com/choosehappy/HistoQC), [NeuroKit2](https://github.com/neuropsychology/NeuroKit), [QuPath](https://github.com/qupath/qupath) | **T:** [Bankhead et al. 2017, QuPath](https://doi.org/10.1038/s41598-017-17204-5); [Makowski et al. 2021, NeuroKit2](https://doi.org/10.3758/s13428-020-01516-y) | DICOM tag consistency, scan quality flags, ECG filtering and repeatable signal measures | Quality thresholds require modality-specific clinical evidence; these publications do not validate every proposed QC rule |
| **9. Specialist interpretation / report** | [3D Slicer](https://github.com/Slicer/Slicer), [QuPath](https://github.com/qupath/qupath), [medSpaCy](https://github.com/medspacy/medspacy), [TotalSegmentator](https://github.com/wasserth/TotalSegmentator) | **T:** [Fedorov et al. 2012](https://doi.org/10.1016/j.mri.2012.05.001); [Bankhead et al. 2017](https://doi.org/10.1038/s41598-017-17204-5); [Wasserthal et al. 2023](https://doi.org/10.1148/ryai.230024); W3 | Display, measurements, optional pretrained segmentation, structured-report checking | TotalSegmentator is computationally heavier and has task-dependent commercial licensing; none of these replace clinician interpretation |
| **10. Report delivery / acknowledgement** | [HAPI FHIR](https://github.com/hapifhir/hapi-fhir), [Medplum](https://github.com/medplum/medplum), [OpenMRS](https://github.com/openmrs/openmrs-core) | **W:** Callen et al. 2012 (W1) | Build a deterministic report-delivered → acknowledged → acted-on task lifecycle | A received report is not proof of action; local accountability and escalation rules needed |
| **11. Diagnostic synthesis** | [medSpaCy](https://github.com/medspacy/medspacy), [HAPI FHIR](https://github.com/hapifhir/hapi-fhir), [3D Slicer](https://github.com/Slicer/Slicer) for reviewing imaging measurements | W0; **T:** Eyre et al. 2021 (W3), Fedorov et al. 2012 | Aggregate reports, encounter notes and tests into provenance-linked evidence timeline | No autonomous diagnosis or unsupported causal inference |
| **12. Management decision** | [OpenCDS](https://www.opencds.org/), [OpenMRS](https://github.com/openmrs/openmrs-core) | W0; no specific patient-outcome trial verified for the combined proposed workflow | Record clinician decisions and link them to evidence | Treatment recommendations are high-risk and may constitute regulated medical device software |
| **13. Treatment / handoff / discharge** | [OpenMRS patient management](https://github.com/openmrs/openmrs-esm-patient-management), [Medplum](https://github.com/medplum/medplum) | W0; **no tool-specific outcome evidence verified** | Open/closed tasks, referrals, transitions and discharge checklist for simulated care | Integrations, consent, privacy and ownership of tasks require validation |
| **14. Follow-up / reassessment** | [Medplum](https://github.com/medplum/medplum), [HAPI FHIR](https://github.com/hapifhir/hapi-fhir), [OpenMRS](https://github.com/openmrs/openmrs-core) | **W:** Callen et al. 2012 (W1) | Track pending investigations, acknowledgements and repeat measurements with rule-based reminders | Do not assume reminders alone improve clinical outcomes; assess alert burden and missed follow-up |

### Specialty-specific open-source stacks

| Diagnostic branch | Components | Peer-reviewed research | First evaluable prototype |
|---|---|---|---|
| **Radiology** | [Orthanc](https://github.com/orthanc-server/orthanc) + [OHIF](https://github.com/OHIF/Viewers) + [pydicom](https://github.com/pydicom/pydicom) + optionally [TotalSegmentator](https://github.com/wasserth/TotalSegmentator) | Jodogne 2018, DOI [10.1007/s10278-018-0082-y](https://doi.org/10.1007/s10278-018-0082-y); Wasserthal 2023, DOI [10.1148/ryai.230024](https://doi.org/10.1148/ryai.230024) | Deidentified study ingest, metadata QC, visualization and physician annotation; CPU-only segmentation may be slow |
| **Pathology** | [QuPath](https://github.com/qupath/qupath) + [HistoQC](https://github.com/choosehappy/HistoQC) | Bankhead 2017, DOI [10.1038/s41598-017-17204-5](https://doi.org/10.1038/s41598-017-17204-5) | Slide QC and reproducible cell/tissue measurements on small regions |
| **Clinical laboratory** | [OpenELIS Global 2](https://github.com/DIGI-UW/OpenELIS-Global-2) + [HAPI FHIR](https://github.com/hapifhir/hapi-fhir) | Clinical need supported by W0/W1; **no peer-reviewed outcome paper for this pairing verified in this review** | Synthetic laboratory result chain and acknowledgement monitoring |
| **Cardiology / ECG** | [WFDB](https://github.com/MIT-LCP/wfdb-python) + [NeuroKit2](https://github.com/neuropsychology/NeuroKit) | Makowski et al. 2021, DOI [10.3758/s13428-020-01516-y](https://doi.org/10.3758/s13428-020-01516-y) | ECG lead import, signal quality and feature extraction with no deep model training |
| **Clinical text** | [medSpaCy](https://github.com/medspacy/medspacy) + [HAPI FHIR](https://github.com/hapifhir/hapi-fhir) | Eyre et al. 2021, [publication](https://arxiv.org/abs/2106.07799) | Rule-based negation, section and uncertainty extraction, with explicit human confirmation |

### Training / resource suitability

- **Lightweight research components:** OpenMRS client-facing workflows (system hosting not necessarily lightweight), pydicom, medSpaCy, WFDB, NeuroKit2, FHIR parsing, rule-based completeness and state checks. No new model training needed; full enterprise platforms still demand deployment resources.
- **Intermediate:** QuPath on selected images; 3D Slicer on small images; OHIF + Orthanc; existing pathology preprocessing. Image sizes and servers can dominate memory.
- **Heavy:** Whole-slide analysis and 3D segmentation such as TotalSegmentator, especially on CPU. Downloadable weights remove training cost but do **not** remove inference cost.
- **Legal/clinical suitability unresolved:** review every software, dependency, model-weight, dataset and clinical intended-use license separately. Open source does not establish approval for diagnostic use.

### Evidence gaps and next validation work

1. Obtain **stage-specific systematic reviews or intervention trials** on appointment no-shows, triage error, test appropriateness, specimen mislabeling, reporting communication and discharge handoffs.
2. Confirm published clinical evaluations and exact licensing of **OpenMRS, OpenELIS Global 2, Medplum and HAPI FHIR** before claiming clinical benefit. Currently, these are included as implementation resources, **not validated outcome-improving interventions**.
3. Inspect competing commercial products and workflow features before treating any proposed gap as unmet.
4. Benchmark CPU RAM, latency, dataset rights and auditability on a local synthetic testbed.
5. Prioritize a research question with measurable endpoints (false-positive alerts, missed discrepancies, task completion times) and a clinician-reviewed reference standard.

### Source verification record

Checked the listed project's official GitHub repository pages and the following academic publications/records on 2026-10-16:
- Jodogne 2018: https://pmc.ncbi.nlm.nih.gov/articles/PMC5959835/
- Bankhead et al. 2017: https://www.nature.com/articles/s41598-017-17204-5
- Fedorov et al. 2012: https://pmc.ncbi.nlm.nih.gov/articles/PMC3466397/
- Wasserthal et al. 2023: https://doi.org/10.1148/ryai.230024
- Makowski et al. 2021: https://doi.org/10.3758/s13428-020-01516-y
- Callen et al. 2012: https://pubmed.ncbi.nlm.nih.gov/22183961/
- Eyre et al. 2021: https://arxiv.org/abs/2106.07799

This is a **mapped inventory, not an exhaustive systematic review**. No tool was evaluated on local patient data, and links are not a statement of clinical fitness or unrestricted commercial use.
