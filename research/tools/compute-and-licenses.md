# Compute suitability, license and deployment caveats.

[Research index](../README.md) · [Academic references](../evidence/references.md)

### Training / resource suitability

- **Lightweight research components:** OpenMRS client-facing workflows (system hosting not necessarily lightweight), pydicom, medSpaCy, WFDB, NeuroKit2, FHIR parsing, rule-based completeness and state checks. No new model training needed; full enterprise platforms still demand deployment resources.
- **Intermediate:** QuPath on selected images; 3D Slicer on small images; OHIF + Orthanc; existing pathology preprocessing. Image sizes and servers can dominate memory.
- **Heavy:** Whole-slide analysis and 3D segmentation such as TotalSegmentator, especially on CPU. Downloadable weights remove training cost but do **not** remove inference cost.
- **Legal/clinical suitability unresolved:** review every software, dependency, model-weight, dataset and clinical intended-use license separately. Open source does not establish approval for diagnostic use.
