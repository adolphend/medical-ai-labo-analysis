#!/usr/bin/env python3
"""Research-only binary classification evaluation. CSV matched by case_id."""
import argparse
import csv
import json
import math
from pathlib import Path

def load_rows(path, required):
    with Path(path).open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        if not set(required).issubset(reader.fieldnames or []):
            raise ValueError(f"{path}: missing columns {sorted(set(required)-set(reader.fieldnames or []))}")
        rows = list(reader)
    keys = [r["case_id"] for r in rows]
    if not rows or any(not k for k in keys) or len(keys) != len(set(keys)):
        raise ValueError(f"{path}: empty file, blank IDs, or duplicated case_id")
    return {r["case_id"]:r for r in rows}

def evaluate(truth_path, predictions_path, threshold=0.5):
    if not 0 <= threshold <= 1 or not math.isfinite(threshold):
        raise ValueError("threshold must be finite in [0, 1]")
    truth=load_rows(truth_path, ("case_id","label"))
    pred=load_rows(predictions_path, ("case_id","score"))
    if set(truth)!=set(pred):
        raise ValueError(f"Case mismatch: {len(set(truth)-set(pred))} missing predictions; {len(set(pred)-set(truth))} unexpected predictions")
    tp=tn=fp=fn=0
    for key,row in truth.items():
        label=int(row["label"])
        score=float(pred[key]["score"])
        if label not in (0,1) or not math.isfinite(score) or not 0<=score<=1:
            raise ValueError(f"Invalid label or score for {key}")
        positive=score>=threshold
        if label==1 and positive: tp+=1
        elif label==1: fn+=1
        elif positive: fp+=1
        else: tn+=1
    div=lambda a,b: a/b if b else None
    return {
        "purpose":"synthetic evaluator verification only; no clinical claims",
        "n_cases":len(truth),"threshold":threshold,
        "tp":tp,"tn":tn,"fp":fp,"fn":fn,
        "sensitivity":div(tp,tp+fn),"specificity":div(tn,tn+fp),
        "precision_ppv":div(tp,tp+fp),"npv":div(tn,tn+fn),
        "accuracy":div(tp+tn,len(truth)),
        "balanced_accuracy":((tp/(tp+fn))+(tn/(tn+fp)))/2 if tp+fn and tn+fp else None
    }

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("--truth",required=True)
    p.add_argument("--predictions",required=True)
    p.add_argument("--threshold",type=float,default=0.5)
    p.add_argument("--output")
    args=p.parse_args()
    result=evaluate(args.truth,args.predictions,args.threshold)
    rendered=json.dumps(result,indent=2)+"\n"
    if args.output:
        path=Path(args.output)
        path.parent.mkdir(parents=True,exist_ok=True)
        path.write_text(rendered,encoding="utf-8")
    print(rendered,end="")

if __name__=="__main__":
    main()
