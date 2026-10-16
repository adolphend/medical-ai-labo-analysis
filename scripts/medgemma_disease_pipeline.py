#!/usr/bin/env python3
"""Create and audit per-disease MedGemma end-to-end research evaluation plans.

This planner never executes inference, prescribes treatment, or marks clinical
tasks validated. Each stage requires independently attributable evaluation.
"""
import argparse
import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
STAGES = (
    ("clinical_context", "text", "facts_and_missing_information", "expert_adjudicated_context"),
    ("clinical_risk_review", "text", "red_flags_and_abstention", "expert_adjudicated_safety"),
    ("examination_selection", "text", "test_choice_and_guideline_alignment", "clinician_guideline_review"),
    ("acquisition_qc", "modality_dependent", "quality_and_adequacy", "expert_technical_quality"),
    ("anatomy_and_findings", "modality_dependent", "finding_detection_and_localization", "expert_labeled_findings"),
    ("diagnostic_synthesis", "multimodal", "differential_and_uncertainty", "expert_case_adjudication"),
    ("report_grounding", "text", "evidence_and_critical_omissions", "specialist_report_review"),
    ("management_evidence", "text", "guideline_citation_and_relevance", "qualified_clinician_review"),
    ("follow_up", "text", "result_acknowledgement_and_closure", "expert_workflow_audit"),
)

def build(root=ROOT):
    with (root / "diseases/registry.csv").open(newline="", encoding="utf-8") as stream:
        rows = list(csv.DictReader(stream))
    catalog=json.loads((root / "evaluation/disease-dataset-catalog.json").read_text(encoding="utf-8"))
    references={x["disease"]:x["candidates"] for x in catalog["diseases"]}
    if len(rows)!=50 or len(references)!=50:
        raise ValueError("Expected exactly 50 distinct disease entries and dataset maps")
    conditions=[]
    for row in rows:
        slug=row["slug"]
        if slug not in references: raise ValueError("Missing dataset mapping: "+slug)
        candidates=references[slug]
        stages=[]
        for index,(name,modality,metric,reference) in enumerate(STAGES):
            stages.append({
                "id":name,
                "depends_on":[] if index==0 else [STAGES[index-1][0]],
                "required":name not in ("acquisition_qc","anatomy_and_findings"),
                "input_modality":modality,
                "model":"google/medgemma-1.5-4b-it",
                "baseline":"expert_approved_rules_or_compatible_specialist_model",
                "expected_output":"structured_json_with_source_ids_and_uncertainty",
                "reference_standard":reference,
                "metric":metric,
                "dataset_candidates":[v["dataset_id"] for v in candidates],
                "model_applicability":"to_be_verified",
                "evaluation":{"status":"not_tested","dataset_version":None,"model_revision":None,
                              "reference_labels":None,"result_path":None},
                "human_signoff":name in ("clinical_risk_review","examination_selection",
                                        "diagnostic_synthesis","management_evidence","follow_up"),
            })
        conditions.append({
            "disease":slug,
            "clinical_context":row["pathway_type"],
            "possible_examinations_not_orders":row["possible_examinations"].split(";"),
            "research_only":True,
            "entrypoint":"clinical_context",
            "stages":stages,
        })
    return {"schema_version":1,"purpose":"research comparison and workflow-safety evaluation",
            "clinical_use_authorized":False,
            "model_revision":"UNPINNED",
            "number_of_diseases":len(conditions),
            "stages_per_disease":len(STAGES),
            "planned_stage_evaluations":len(conditions)*len(STAGES),
            "conditions":conditions}

def audit(plan):
    if plan.get("clinical_use_authorized") is not False: raise ValueError("Clinical use must remain disabled")
    total=0
    if len(plan.get("conditions",[]))!=50: raise ValueError("Expected 50 conditions")
    for condition in plan["conditions"]:
        seen=set()
        for step in condition["stages"]:
            if step["id"] in seen: raise ValueError("Duplicate stage")
            if any(dep not in seen for dep in step["depends_on"]): raise ValueError("Invalid stage ordering")
            seen.add(step["id"]);total+=1
            e=step["evaluation"]
            if e["status"]!="not_tested":
                if not all(e.get(x) for x in ("dataset_version","model_revision","reference_labels","result_path")):
                    raise ValueError("Cannot claim a tested step without complete provenance")
            if step["id"] in ("management_evidence","diagnostic_synthesis") and not step["human_signoff"]:
                raise ValueError("Clinical signoff cannot be disabled")
    return {"checked_diseases":50,"checked_stages":total,"unmeasured_stages":sum(
        1 for c in plan["conditions"] for s in c["stages"] if s["evaluation"]["status"]=="not_tested")}
def main():
    p=argparse.ArgumentParser()
    p.add_argument("--output",type=Path)
    p.add_argument("--audit",type=Path,help="Audit an existing pipeline JSON instead of creating one")
    args=p.parse_args()
    payload=json.loads(args.audit.read_text()) if args.audit else build()
    checks=audit(payload)
    if args.output:
        args.output.parent.mkdir(parents=True,exist_ok=True)
        args.output.write_text(json.dumps(payload,indent=2)+"\n",encoding="utf-8")
    print(json.dumps(checks,indent=2))
if __name__=="__main__":main()
