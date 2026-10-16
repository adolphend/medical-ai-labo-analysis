#!/usr/bin/env python3
"""Offline end-to-end smoke evaluation: metadata governance -> fixture predictions -> metrics.
Real dataset/model integration requires authorized sources and separate model adapters.
"""
import json, subprocess, sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def call(*args):
    subprocess.run([sys.executable,*args],cwd=ROOT,check=True)
def main():
    call("scripts/check_datasets.py")
    call("scripts/check_disease_dataset_catalog.py")
    call("-m","unittest","discover","-s","tests","-p","test_*.py","-v")
    call("scripts/evaluate_predictions.py","--truth","evaluation/fixtures/truth.csv",
         "--predictions","evaluation/fixtures/predictions.csv",
         "--output","evaluation/results/metrics.json")
    call("scripts/evaluate_context.py","--truth","evaluation/fixtures/context_truth.json",\n         "--predictions","evaluation/fixtures/context_predictions.json",\n         "--output","evaluation/results/context_metrics.json")\n    context=json.loads((ROOT/"evaluation/results/context_metrics.json").read_text())\n    assert context["n_cases"]==2 and context["missed_human_review"]==1\n    metrics=json.loads((ROOT/"evaluation/results/metrics.json").read_text())
    assert metrics["n_cases"]==6 and metrics["tp"]==2 and metrics["tn"]==2
    print("PASS: binary + context fixture pipeline; NO clinical dataset or real model inference.")
if __name__=="__main__":main()
