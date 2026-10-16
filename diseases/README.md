# Disease-oriented medical AI research

[Research index](../research/README.md) · [Imaging categories](../research/imaging/README.md) · [OpenCode agent](../.opencode/agents/medical-disease-architect.md)

## Scope
We begin with **50 clinical conditions across 14 specialties**, including screening/checkup contexts, urgent symptomatic diagnosis, surveillance and longitudinal management. The canonical list is [registry.csv](registry.csv). No automatic imaging or treatment orders are implied.

**The registry's modalities are hypotheses for verification**, not formal clinical protocols. An evidence-focused OpenCode agent processes **one condition at a time**; unresearched disease folders are deliberately marked `EVIDENCE_PENDING`.

## Workflow for every condition
Patient interview/clinician assessment → whether screening or diagnostic examination is indicated → image/lab/signal acquisition and QC → anatomical or biomarker findings → condition-specific model if proven → specialist report → clinician-controlled management options from guidelines → documented follow-up.

## Scaffold all 50 folders

```bash
python3 scripts/scaffold_diseases.py
```

The generator creates standardized linked files and a machine-readable pipeline in every disease folder. It **never overwrites existing content** unless explicitly passed `--force` (avoid that option).

## Run the OpenCode research agent

Install and launch OpenCode in the cloned repository, select the custom agent named `medical-disease-architect`, then ask:

```
Build diseases/abdominal-aortic-aneurysm end to end.
Verify every claim with academic publications and clinical guidelines.
Update each existing topic-specific Markdown file and pipeline.yaml.
No training, no autonomous diagnosis or treatment, CPU-first research only.
```

After verifying the first disease, ask it to process the **next unresearched condition** in the CSV. Do not treat 50 generated scaffolds as 50 researched clinical pipelines.

## Required fields
Every disease research module must record the intended patient group and clinical question, imaging and nonimaging alternatives, data/QC requirements, model repo/weights/version/license, academic evidence and study limitations, safety exceptions, evaluation plan, clinician review points and follow-up responsibilities.

The repo intentionally does **not** provide individualized treatment recommendations. Management files should surface guidelines for a qualified clinician to interpret.
