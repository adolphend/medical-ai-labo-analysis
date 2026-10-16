#!/usr/bin/env python3
"""Validate/interpret research disease procedure JSON, without executing clinical models."""
import argparse
import json
from pathlib import Path

KINDS={"conversation","examination_selection","quality_control","anatomy","finding_detection","interpretation","management_evidence","follow_up","lab_analysis","signal_analysis"}
EXECUTORS={"none","rule","model","human"}
EVAL_STATUSES={"pending","passed","failed","not_applicable"}

def interpret(procedure):
    if procedure.get("schema_version")!=1 or procedure.get("research_only") is not True:
        raise ValueError("Expected schema_version=1 and research_only=true")
    steps=procedure.get("steps")
    if not isinstance(steps,list) or not steps:
        raise ValueError("Nonempty steps required")
    ids=[s.get("id") for s in steps]
    if not all(isinstance(x,str) and x for x in ids) or len(ids)!=len(set(ids)):
        raise ValueError("Step ids must be unique nonempty strings")
    by_id={s["id"]:s for s in steps}
    if procedure.get("entrypoint") not in by_id: raise ValueError("Invalid entrypoint")
    order=[];visiting=set();visited=set()
    def visit(i):
        if i in visiting: raise ValueError("Dependency cycle")
        if i in visited:return
        visiting.add(i)
        for dep in by_id[i].get("depends_on",[]):
            if dep not in by_id: raise ValueError(f"Unknown dependency {dep}")
            visit(dep)
        visiting.remove(i);visited.add(i);order.append(i)
    for i in ids: visit(i)
    result=[]
    for i in order:
        s=by_id[i]
        if s.get("kind") not in KINDS or s.get("executor") not in EXECUTORS:
            raise ValueError(f"{i}: unsupported kind/executor")
        if not isinstance(s.get("required"),bool) or not isinstance(s.get("approval_required"),bool):
            raise ValueError(f"{i}: required/approval_required must be booleans")
        if not isinstance(s.get("input_keys"),list) or not isinstance(s.get("output_keys"),list):
            raise ValueError(f"{i}: missing input/output contracts")
        e=s.get("evaluation")
        if not isinstance(e,dict) or not e.get("metric") or e.get("status") not in EVAL_STATUSES:
            raise ValueError(f"{i}: each step needs metric and evaluation status")
        if s["kind"] in {"interpretation","management_evidence"} and not s["approval_required"]:
            raise ValueError(f"{i}: clinical human approval required")
        if s["executor"]=="model":
            m=s.get("model")
            if not isinstance(m,dict) or not m.get("registry_id") or not m.get("version"):
                raise ValueError(f"{i}: model registry ID and version required")
            ready=bool(m.get("adapter") and m.get("weights_sha256") and e["dataset_id"] and e["result_path"] and e["status"]=="passed" and s.get("evidence_status")=="verified")
            state="requires_external_validation" if ready else "blocked"
            reason="Research-only; independent adapter and approval required" if ready else "Missing verified adapter, weights, independent evaluation or evidence"
        else:
            state="human_review" if s["executor"]=="human" else "planned"
            reason="No runtime execution; human decision required" if s["executor"]=="human" else "Implementation not connected"
        result.append({"step":i,"kind":s["kind"],"executor":s["executor"],"state":state,"reason":reason,"evaluation":e["status"],"depends_on":s.get("depends_on",[])})
    return {"disease":procedure.get("disease"),"entrypoint":procedure["entrypoint"],"research_only":True,"steps":result,"models_executed":0}
def main():
    p=argparse.ArgumentParser()
    p.add_argument("path",type=Path)
    p.add_argument("--json",action="store_true")
    a=p.parse_args()
    out=interpret(json.loads(a.path.read_text(encoding="utf-8")))
    print(json.dumps(out,indent=2) if a.json else "\n".join(f"{x['step']}: {x['state']} — {x['reason']}" for x in out["steps"]))
if __name__=="__main__": main()
