#!/usr/bin/env python3
"""Compare TWO prediction JSON files on shared gold clinical-context cases.
Does not run any AI model or establish clinical effectiveness.
"""
import argparse,json
from pathlib import Path
from evaluate_context import measure
def main():
 p=argparse.ArgumentParser()
 p.add_argument("--truth",required=True);p.add_argument("--a",required=True)
 p.add_argument("--b",required=True);p.add_argument("--output")
 args=p.parse_args()
 read=lambda x:json.loads(Path(x).read_text(encoding="utf-8"))
 gold=read(args.truth)
 a=measure(gold,read(args.a));b=measure(gold,read(args.b))
 delta={}
 for key in a["field_metrics"]:
  x=a["field_metrics"][key]["f1"];y=b["field_metrics"][key]["f1"]
  delta[key]=None if x is None or y is None else round(y-x,6)
 out={"purpose":"paired structured-context predictions; no model executed",
      "n_cases":a["n_cases"],"model_a":a,"model_b":b,"f1_delta_b_minus_a":delta}
 result=json.dumps(out,indent=2)+"\n"
 if args.output:
  path=Path(args.output);path.parent.mkdir(parents=True,exist_ok=True);path.write_text(result)
 print(result,end="")
if __name__=="__main__":main()
