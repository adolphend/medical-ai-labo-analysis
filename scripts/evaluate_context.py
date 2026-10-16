#!/usr/bin/env python3
"""Evaluate structured clinical-context extraction/routing against expert-labeled cases.
Research-only exact-match metrics; no live clinical guidance or NLP inference.
"""
import argparse, json
from pathlib import Path

FIELDS=("facts","missing_information","candidate_examinations","contraindication_flags")
def validate_case(c, prediction=False):
    if not isinstance(c,dict) or not isinstance(c.get("case_id"),str) or not c["case_id"]:
        raise ValueError("Every record requires case_id")
    for field in FIELDS:
        x=c.get(field)
        if not isinstance(x,list) or not all(isinstance(z,str) and z for z in x) or len(x)!=len(set(x)):
            raise ValueError(f"{c['case_id']}: {field} must be unique nonempty strings")
    if not isinstance(c.get("requires_human_review"),bool):
        raise ValueError("requires_human_review must be boolean")
    if prediction and not isinstance(c.get("evidence_ids"),list):
        raise ValueError("Predictions require evidence_ids list")

def measure(gold, pred):
    if not isinstance(gold,list) or not isinstance(pred,list):
        raise ValueError("Expected arrays")
    for c in gold: validate_case(c)
    for c in pred: validate_case(c,True)
    g={x["case_id"]:x for x in gold};p={x["case_id"]:x for x in pred}
    if len(g)!=len(gold) or len(p)!=len(pred) or not g or set(g)!=set(p):
        raise ValueError("Duplicate, empty or mismatched case IDs")
    counts={f:{"tp":0,"fp":0,"fn":0} for f in FIELDS}
    missed_human=0;extra_human=0;unsupported=0;case_results=[]
    for key in sorted(g):
        a,b=g[key],p[key];details={}
        for field in FIELDS:
            expected=set(a[field]);obtained=set(b[field])
            tp=len(expected&obtained);fp=len(obtained-expected);fn=len(expected-obtained)
            counts[field]["tp"]+=tp;counts[field]["fp"]+=fp;counts[field]["fn"]+=fn
            details[field]={"tp":tp,"fp":fp,"fn":fn}
        missed_human+=int(a["requires_human_review"] and not b["requires_human_review"])
        extra_human+=int(not a["requires_human_review"] and b["requires_human_review"])
        # Evidence identifiers only count as traceable if included in gold's permitted IDs.
        valid=a.get("evidence_ids",[])
        if not isinstance(valid,list): raise ValueError("Gold evidence_ids must be a list when present")
        if not all(isinstance(x,str) for x in b["evidence_ids"]): raise ValueError("Bad evidence ID")
        unsupported+=len(set(b["evidence_ids"])-set(valid))
        case_results.append({"case_id":key,"field_errors":details,"missed_human_review":a["requires_human_review"] and not b["requires_human_review"]})
    scores={}
    for field,v in counts.items():
        tp,fp,fn=v["tp"],v["fp"],v["fn"]
        scores[field]={**v,"precision":tp/(tp+fp) if tp+fp else None,
                       "recall":tp/(tp+fn) if tp+fn else None,
                       "f1":2*tp/(2*tp+fp+fn) if 2*tp+fp+fn else None}
    return {"purpose":"context contract testing; not clinical correctness or treatment validation",
            "n_cases":len(g),"field_metrics":scores,"missed_human_review":missed_human,
            "extra_human_review":extra_human,"unsupported_evidence_ids":unsupported,
            "cases":case_results}
def main():
    p=argparse.ArgumentParser();p.add_argument("--truth",required=True);p.add_argument("--predictions",required=True);p.add_argument("--output")
    args=p.parse_args()
    result=measure(json.loads(Path(args.truth).read_text()),json.loads(Path(args.predictions).read_text()))
    data=json.dumps(result,indent=2)+"\n"
    if args.output:
        path=Path(args.output);path.parent.mkdir(parents=True,exist_ok=True);path.write_text(data)
    print(data,end="")
if __name__=="__main__":main()
