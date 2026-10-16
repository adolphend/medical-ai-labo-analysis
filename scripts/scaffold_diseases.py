#!/usr/bin/env python3
"""Generate disease research folders from diseases/registry.csv. Standard library only."""
import argparse
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "diseases"
SECTIONS = [
 ("clinical-presentation.md", "Clinical presentation", "History, symptoms, red flags and clinician assessment."),
 ("examination-selection.md", "Examination selection", "Screening eligibility versus symptomatic diagnosis versus surveillance; indications and alternatives."),
 ("acquisition-quality.md", "Acquisition and quality", "Imaging or non-imaging test protocol, quality criteria, patient safety and inadequate data."),
 ("anatomy-findings.md", "Anatomy and findings", "Observable anatomy, measurements, findings, uncertainty and boundaries of inference."),
 ("open-models.md", "Open-source models and tools", "Verified research paper + code + weights + license + compute assessment per tool."),
 ("interpretation-report.md", "Interpretation and reporting", "Source-linked structured observations and clinician verification."),
 ("management-evidence.md", "Management evidence", "Current evidence/guidelines for clinician consideration; no automatic treatment prescriptions."),
 ("follow-up.md", "Follow-up", "Review, communication, reassessment, outstanding tests and owner."),
 ("validation.md", "Validation and evaluation", "Reference standard, external cohorts, bias, clinical safety and resource benchmarks."),
]
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--disease", help="One slug; omitted means all registered conditions")
    ap.add_argument("--force", action="store_true", help="Explicitly overwrite existing generated files (not advised)")
    args = ap.parse_args()
    with (BASE / "registry.csv").open(newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    if args.disease:
        rows = [r for r in rows if r["slug"] == args.disease]
        if not rows:
            ap.error("Unknown disease slug")
    for r in rows:
        folder = BASE / r["slug"]
        folder.mkdir(parents=True, exist_ok=True)
        nav = "\n".join(f"- [{name}](%s)" % file for file,name,_ in SECTIONS)
        welcome = (f"# {r['condition']} — diagnostic research module\n\n"
                   f"[All conditions](../README.md) · [Shared diagnostic models](../../research/diagnostics/README.md) · "
                   f"[Medical imaging research](../../research/imaging/README.md)\n\n"
                   f"**Specialty:** {r['specialty']}  \n**Candidate examinations (not orders):** {r['possible_examinations']}  \n"
                   f"**Pathway context:** {r['pathway_type']}  \n**Research status:** NOT STARTED.\n\n"
                   f"Listed examinations are hypotheses for literature verification, not patient-specific advice.\n\n"
                   f"## Sections\n{nav}\n\n- [Machine-readable workflow](pipeline.yaml)\n")
        files = {"README.md":welcome}
        for filename,title,purpose in SECTIONS:
            files[filename] = (f"# {title} — {r['condition']}\n\n[Condition index](README.md) · "
                 f"[Research method](../../research/methods/research-method.md)\n\n"
                 f"**Responsibility:** {purpose}\n\n"
                 "## Evidence status\nEVIDENCE_PENDING — No patient-facing claims or disease-specific model validations established in this scaffold.\n\n"
                 "## Evidence table\n| Claim / task | Paper DOI or guideline URL | Population / evaluation | Limitations |\n"
                 "|---|---|---|---|\n| Pending review | Pending | Pending | Pending |\n\n"
                 "## Required analysis\nTo be completed by the OpenCode agent using primary literature.\n")
        files["pipeline.yaml"] = (
            f"disease: {r['slug']}\nstatus: not_started\n"
            "workflow:\n  - clinical_presentation\n  - examination_selection\n"
            "  - acquisition_quality\n  - anatomy_findings\n  - open_models\n"
            "  - interpretation_reporting\n  - clinician_management_review\n  - follow_up\n"
            "human_approval_required: true\nclinical_deployment_approved: false\n"
            "evidence: pending\n")
        # Disease-specific declarative JSON: no models activated until independently evaluated.
        import json
        template = json.loads((ROOT / "pipeline/example-procedure.json").read_text(encoding="utf-8"))
        template["disease"] = r["slug"]
        template["clinical_context"] = r["pathway_type"]
        template["candidate_examinations"] = r["possible_examinations"].split(";")
        files["procedure.json"] = json.dumps(template, indent=2) + "\n"
        for filename, content in files.items():
            target = folder / filename
            if target.exists() and not args.force:
                continue
            target.write_text(content, encoding="utf-8")
        print(f"Scaffold: {r['slug']}")
if __name__ == "__main__":
    main()
