# Disease screening and early detection by modality

[Diagnostic research index](README.md) · [Disease-model inventory](04-abnormality-and-disease-detection.md) · [Test selection](01-conversation-and-examination-selection.md)

## Fundamental distinction
**Population screening** targets asymptomatic, appropriately selected groups; **early diagnosis** investigates symptoms earlier; **incidental detection** finds unexpected findings during another examination. Image-detection benchmark success does not show improved mortality or justify population screening.

| Condition / finding | Main examination | Early detection benefit and level of evidence | Open-source research starting point | What cannot be inferred |
|---|---|---|---|---|
| Breast cancer | Screening mammography | USPSTF 2024 recommends biennial mammography at 40–74 for average-risk women: [recommendation](https://www.uspreventiveservicestaskforce.org/uspstf/recommendation/breast-cancer-screening) (evidence-based guideline) | [MONAI](https://github.com/Project-MONAI/MONAI), task-specific mammography checkpoints to be verified | No validated general open-weight clinical screening model confirmed here |
| Lung cancer in eligible high-risk people | **Low-dose CT**, not standard chest X-ray | NLST randomized trial found **20% relative reduction in lung-cancer mortality** vs radiography: DOI [10.1056/NEJMoa1102873](https://doi.org/10.1056/NEJMoa1102873) | [LUNA16](https://luna16.grand-challenge.org/) nodule detection benchmark | Nodule ≠ cancer; screening restricted to guideline-eligible populations |
| Cervical precancer/cancer | **HPV DNA testing primarily**, with cytology/colposcopy as indicated | WHO recommends HPV DNA testing as primary screening: [guideline summary](https://www.who.int/news/item/06-07-2021-new-recommendations-for-screening-and-treatment-to-prevent-cervical-cancer) | [QuPath](https://github.com/qupath/qupath) for cytology/histology research | Do not replace primary HPV screening with image-only AI |
| Colorectal cancer | Stool-based testing and colonoscopy; CT colonography in selected pathways | Screening efficacy depends on the particular test and setting; verify local guidelines | [MONAI](https://github.com/Project-MONAI/MONAI) research frameworks | No general justification for CT screening of everyone |
| Diabetic retinopathy | Retinal fundus photography | Detecting referable disease can support earlier specialist management; comparative outcomes and screening eligibility need specialty-specific review | [MONAI](https://github.com/Project-MONAI/MONAI) + specialist models to be verified | No deployment-ready checkpoint validated by this catalog |
| Osteoporosis / vertebral fracture | DXA and incidental CT/X-ray review | Imaging-based detection may reveal previously unrecognized bone disease; population screening standards differ | [3D Slicer](https://github.com/Slicer/Slicer), measurement/segmentation research | CT findings do not replace standardized bone-density assessment without validation |
| Stroke / intracranial hemorrhage | Noncontrast CT and/or MRI in **symptomatic emergency assessment** | Time-sensitive diagnosis, not routine general-population screening | [MONAI model zoo](https://github.com/Project-MONAI/model-zoo) task-specific | Needs urgent clinical pathways; no universal detector claimed |
| Abdominal aortic aneurysm | Ultrasound in eligible groups | Screening has evidence in selected at-risk groups; population and modality guidance must be checked | [3D Slicer](https://github.com/Slicer/Slicer) measurements / ultrasound methods | Not everyone should receive ultrasound |
| Prostate cancer | PSA-based risk pathway, MRI for selected diagnostic indications | Population screening benefit/harms are contested and guidance varies | [MONAI model zoo](https://github.com/Project-MONAI/model-zoo) selected prostate models | MRI is not an unrestricted population screening test |

## Epidemiological ranking method (not completed)
For each disease document incidence/prevalence **by country**, preventable mortality/disability, stage shift with earlier detection, screening RCT/systematic-review outcomes, benefit–harm tradeoff, availability/cost of indicated examination, reference standards, existing commercial competition, public datasets, model checkpoint availability and validation. **Do not call this a ranked list of most common diseases** until jurisdiction/year-specific epidemiology is verified.

## Proposed product
A guideline-linked screening eligibility and follow-up tracking service requiring clinician-approved policies, not automatic screening orders. Separately evaluate specialized image analysis for a single disease with external validation.

## Needed evidence
Screening trials/recommendations for colorectal cancer, diabetic retinopathy, abdominal aortic aneurysm, and each specialty; disease prevalence and local implementation data; complete commercial/model license and benchmark audits.
