# Image interpretation and clinical reporting

[Diagnostic research index](README.md) · [Disease models](04-abnormality-and-disease-detection.md) · [Synthesis](../stages/11-diagnostic-synthesis.md)

## Responsibility
Present traceable image observations, annotated evidence, prior comparison and structured report drafts for authorized specialist verification. Reporting is a distinct task from lesion detection.

| Subtask | Reusable material | Academic evidence | Important limits |
|---|---|---|---|
| Viewing and annotation | [OHIF](https://github.com/OHIF/Viewers), [3D Slicer](https://github.com/Slicer/Slicer) | Fedorov et al. (2012), DOI [10.1016/j.mri.2012.05.001](https://doi.org/10.1016/j.mri.2012.05.001) | Not interpreting images by itself |
| Radiology report entities | [RadGraph](https://github.com/Stanford-AIMI/radgraph) | Jain et al., *RadGraph*, NeurIPS Datasets & Benchmarks (2021): https://arxiv.org/abs/2106.14463 | Extracts observations and relations from text, not independently verifies images |
| Chest radiograph report labels | [CheXbert](https://github.com/stanfordmlgroup/CheXbert) | Smit et al., *Combining Automatic Labelers and Expert Annotations for Accurate Radiology Report Labeling*, EMNLP (2020): https://aclanthology.org/2020.emnlp-main.117/ | Labels in text; not a diagnostic substitute |
| Medical vision-language | [MedGemma](https://github.com/Google-Health/medgemma) | Model card and published developer evaluations; independently peer-reviewed external clinical validation requires separate verification | Model weights use Health AI Developer Foundations license, **not standard OSS** |
| General medical reports | [medSpaCy](https://github.com/medspacy/medspacy), [Whisper](https://github.com/openai/whisper) | Eyre et al. (2021) medSpaCy: https://arxiv.org/abs/2106.07799 | Dictation/NLP can omit, negate or distort medical details |

## Evidence about report generation risks
A 2025 systematic review found hallucinations, misdiagnoses and missing details in LLM-generated radiology reports: https://doi.org/10.1016/j.ibmed.2025.100287. A 2026 review highlights weak external validation and poor readiness for autonomous clinical use: https://doi.org/10.1016/j.ijmedinf.2025.106227.

## Proposed output contract
Reference image/study UID; clinical question; modality; technical limitations; human-authored or validated observations, locations, measurement units, temporal comparisons, diagnostic impression, uncertainty, urgent flags, model provenance, reviewer signature and amendments.

## Feasible MVP
Report *consistency* checking: laterality, units, missing sections, findings/impression contradictions, references to unavailable studies; specialist confirms each proposed fix. Evaluate adjudicated discrepancy detection precision/recall, clinically important omissions, false alarms, and editing burden. Never auto-sign or transmit an unreviewed model report.
