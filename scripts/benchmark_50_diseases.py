#!/usr/bin/env python3
"""Build and optionally score MedGemma-vs-specialist evaluation plans for 50 diseases.

Input: disease registry, disease dataset catalog and optional JSON predictions.
No network, model download, inference, or invented accuracy. Standard library only.
"""
import argparse, csv, json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
TASKS=("context_extraction","exam_selection","imaging_findings","report_grounding","management_evidence")
def load_registry(root=ROOT):
    with (root/"diseases/registry.csv").open(encoding="utf-8",newline="") as f: return list(csv.DictReader(f))
def plan(root=ROOT):
    rows=load_registry(root)
    catalog=json.loads((root/"evaluation/disease-dataset-catalog.json").read_text(encoding="utf-8"))
    mapping={d["disease"]:d for d in catalog["diseases"]}
    if len(rows)!=50 or len(mapping)!=50: raise ValueError("Expected 50 registered conditions")
    output=[]
    for row in rows:
        slug=row["slug"]
        if slug not in mapping: raise ValueError(f"No candidate dataset mapping for {slug}")
        steps=[]
        for task in TASKS:
            steps.append({
                "task":task,
                "reference_standard":"expert_adjudicated_context" if task in ("context_extraction","exam_selection","management_evidence") else "expert_adjudicated_modality_labels",
                "candidates":["medgemma-1.5-4b-it","specialist_or_deterministic_baseline"],
                "dataset_candidates":[c["dataset_id"] for c in mapping[slug]["candidates"]],
                "dataset_suitability":"unverified",
                "status":"not_tested",
                "result":None,
                "metrics":(["field_precision","field_recall","field_f1","missed_escalations"] if task=="context_extraction" else
                           ["guideline_agreement","unsafe_routing"] if task=="exam_selection" else
                           ["task_specific_performance","abstention_rate"] if task=="imaging_findings" else
                           ["source_fidelity","critical_omissions"] if task=="report_grounding" else
                           ["citation_support","human_review_compliance"])
            })
        output.append({"disease":slug,"candidate_examinations":row["possible_examinations"].split(";"),
                       "clinical_pathway":row["pathway_type"],"tasks":steps})
    return {"schema_version":1,"comparison":"medgemma_1_5_vs_specialist","model_revision":"UNPINNED",
            "execution":"PLAN_ONLY","number_of_diseases":len(output),"number_of_tasks":len(output)*len(TASKS),
            "conditions":output}
def validate_results(results,root=ROOT):
    current=plan(root)
    slots={(x["disease"],s["task"]) for x in current["conditions"] for s in x["tasks"]}
    items=results.get("results")
    if not isinstance(items,list): raise ValueError("results must be array")
    seen=set();summary={"reported_tasks":0,"passed":0,"failed":0,"not_comparable":0}
    for item in items:
        key=(item.get("disease"),item.get("task"))
        if key not in slots or key in seen: raise ValueError(f"Unknown/duplicate task: {key}")
        seen.add(key)
        state=item.get("status")
        if state not in ("passed","failed","not_comparable"): raise ValueError("Invalid status")
        for field in ("dataset_version","ground_truth_source","model_revision","baseline_revision","metric_name","metric_value","run_artifact"):
            if item.get(field) is None: raise ValueError(f"{key}: missing {field}")
        if not isinstance(item["metric_value"],(int,float)) or isinstance(item["metric_value"],bool):
            raise ValueError("metric_value must be numeric (not a fabricated placeholder)")
        summary["reported_tasks"]+=1;summary[state]+=1
    summary["not_tested"]=current["number_of_tasks"]-summary["reported_tasks"]
    return summary
def main():
    p=argparse.ArgumentParser()
    p.add_argument("--output",type=Path)
    p.add_argument("--results",type=Path,help="Optional independently generated evaluation results JSON")
    args=p.parse_args()
    if args.results:
        result=validate_results(json.loads(args.results.read_text(encoding="utf-8")))
    else: result=plan()
    content=json.dumps(result,indent=2)+"\n"
    if args.output:
        args.output.parent.mkdir(parents=True,exist_ok=True)
        args.output.write_text(content,encoding="utf-8")
    print(content,end="")
if __name__=="__main__":main()
