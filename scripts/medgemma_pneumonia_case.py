#!/usr/bin/env python3
"""Optional public MedMNIST data acquisition, MedGemma inference, and scoring.

Only download with --download; only GPU inference with --infer.
No patient care, no autonomous management, no synthetic accuracy claims.
"""
import argparse,csv,hashlib,json,os,re,sys,time,urllib.request
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
SOURCE="https://zenodo.org/records/10519652/files/pneumoniamnist_224.npz?download=1"
EXPECTED_MD5="d6a3c71de1b945ea11211b03746c1fe1"
DATA=ROOT/"data/raw/pneumoniamnist_224.npz"
RESULT=ROOT/"evaluation/results"
def fetch():
    DATA.parent.mkdir(parents=True,exist_ok=True)
    tmp=DATA.with_suffix(".partial")
    h=hashlib.md5()
    try:
        req=urllib.request.Request(SOURCE,headers={"User-Agent":"medical-ai-research/0.1"})
        with urllib.request.urlopen(req,timeout=90) as response,open(tmp,"wb") as out:
            if not response.geturl().startswith("https://"): raise ValueError("Non-HTTPS redirect")
            n=0
            while True:
                chunk=response.read(1024*1024)
                if not chunk:break
                n+=len(chunk)
                if n>600_000_000: raise ValueError("Unexpectedly large artifact")
                h.update(chunk);out.write(chunk)
        if h.hexdigest()!=EXPECTED_MD5: raise ValueError("Dataset MD5 does not match published artifact")
        os.replace(tmp,DATA)
        print(f"Downloaded publisher-matched dataset to {DATA}")
    finally:
        tmp.unlink(missing_ok=True)
def load_test(limit):
    import numpy as np
    if not DATA.exists(): raise FileNotFoundError(f"Download dataset first: {DATA}")
    if hashlib.md5(DATA.read_bytes()).hexdigest()!=EXPECTED_MD5:
        raise ValueError("Dataset failed publisher-MD5 check")
    with np.load(DATA,allow_pickle=False) as dataset:
        images=dataset["test_images"][:limit].copy()
        labels=dataset["test_labels"][:limit].reshape(-1).tolist()
    if len(images)!=len(labels) or any(int(x) not in (0,1) for x in labels):
        raise ValueError("Unexpected dataset structure/labels")
    return images,labels
def parse_class(text):
    # A strict research label parser: missing, contradictory or ambiguous = abstain.
    hits=set(re.findall(r"\\b(?:normal|pneumonia)\\b",text.lower()))
    return ("normal" if hits=={"normal"} else "pneumonia" if hits=={"pneumonia"} else None)
def inference(limit,model_path):
    import torch
    from PIL import Image
    from transformers import AutoProcessor,AutoModelForImageTextToText,BitsAndBytesConfig
    if not torch.cuda.is_available(): raise RuntimeError("CUDA GPU required for this 4-bit runner")
    images,labels=load_test(limit)
    quant=BitsAndBytesConfig(load_in_4bit=True,bnb_4bit_quant_type="nf4",
           bnb_4bit_compute_dtype=torch.float16,bnb_4bit_use_double_quant=True)
    processor=AutoProcessor.from_pretrained(model_path)
    model=AutoModelForImageTextToText.from_pretrained(model_path,device_map={"":0},
            quantization_config=quant,torch_dtype=torch.float16,low_cpu_mem_usage=True)
    RESULT.mkdir(parents=True,exist_ok=True)
    pred_path=RESULT/"pneumonia_medgemma_predictions.csv"
    truth_path=RESULT/"pneumonia_medgemma_truth.csv"
    records=[];elapsed=[]
    for idx,img in enumerate(images):
        image=Image.fromarray(img).convert("RGB")
        prompt="Research image classification only. Pick ONE label for this pediatric chest radiograph: NORMAL or PNEUMONIA. Output only the single label; if uncertain output UNKNOWN. Do not recommend treatment."
        msg=[{"role":"user","content":[{"type":"image","image":image},{"type":"text","text":prompt}]}]
        model_inputs=processor.apply_chat_template(msg,add_generation_prompt=True,tokenize=True,return_dict=True,return_tensors="pt").to("cuda:0")
        start=time.perf_counter()
        with torch.inference_mode(): out=model.generate(**model_inputs,max_new_tokens=12,do_sample=False)
        torch.cuda.synchronize();elapsed.append(time.perf_counter()-start)
        answer=processor.decode(out[0][model_inputs["input_ids"].shape[1]:],skip_special_tokens=True).strip()
        label=parse_class(answer)
        records.append((f"test-{idx:05}",label,answer))
        print(f"{idx+1}/{len(images)}: {label or 'ABSTAIN'}")
    with pred_path.open("w",newline="",encoding="utf-8") as f:
        writer=csv.writer(f);writer.writerow(["case_id","score","raw_response","abstained"])
        for cid,label,raw in records:
            writer.writerow([cid,"1" if label=="pneumonia" else "0" if label=="normal" else "",raw,int(label is None)])
    with truth_path.open("w",newline="",encoding="utf-8") as f:
        writer=csv.writer(f);writer.writerow(["case_id","label"])
        for idx,label in enumerate(labels):writer.writerow([f"test-{idx:05}",int(label)])
    meta={"dataset":"PneumoniaMNIST-224","published_md5":EXPECTED_MD5,
          "split":"official_test","cases":len(labels),"model_path":model_path,
          "prompt_type":"single_choice","covered":sum(r[1] is not None for r in records),
          "abstentions":sum(r[1] is None for r in records),
          "mean_inference_seconds":sum(elapsed)/len(elapsed),"clinical_validation":False}
    (RESULT/"pneumonia_medgemma_provenance.json").write_text(json.dumps(meta,indent=2)+"\\n")
    print(f"Saved {pred_path}")
def score():
    sys.path.insert(0,str(ROOT/"scripts"))
    from evaluate_predictions import evaluate
    t=RESULT/"pneumonia_medgemma_truth.csv"
    p=RESULT/"pneumonia_medgemma_predictions.csv"
    with t.open(newline="") as f: truth=list(csv.DictReader(f))
    with p.open(newline="") as f: preds=list(csv.DictReader(f))
    pred_by_id={r["case_id"]:r for r in preds}
    covered=[r for r in truth if pred_by_id[r["case_id"]]["score"]!=""]
    abstained=len(truth)-len(covered)
    if not covered: raise RuntimeError("No usable predictions; report 0% coverage and inspect generation")
    RESULT.mkdir(parents=True,exist_ok=True)
    ta=RESULT/"pneumonia_covered_truth.csv";pa=RESULT/"pneumonia_covered_predictions.csv"
    with ta.open("w",newline="") as f:
        w=csv.DictWriter(f,fieldnames=["case_id","label"]);w.writeheader();w.writerows(covered)
    with pa.open("w",newline="") as f:
        w=csv.DictWriter(f,fieldnames=["case_id","score"]);w.writeheader()
        w.writerows([{"case_id":r["case_id"],"score":pred_by_id[r["case_id"]]["score"]} for r in covered])
    report=evaluate(ta,pa)
    report.update({"dataset":"PneumoniaMNIST-224","split":"official_test",
            "overall_n":len(truth),"covered_n":len(covered),"abstained_n":abstained,
            "coverage":len(covered)/len(truth),"experimental":True,
            "clinical_validity":"NOT ESTABLISHED"})
    (RESULT/"pneumonia_medgemma_metrics.json").write_text(json.dumps(report,indent=2)+"\\n")
    print(json.dumps(report,indent=2))
def main():
    p=argparse.ArgumentParser()
    flags=p.add_mutually_exclusive_group(required=True)
    flags.add_argument("--download",action="store_true")
    flags.add_argument("--infer",action="store_true")
    flags.add_argument("--score",action="store_true")
    p.add_argument("--limit",type=int,default=20)
    p.add_argument("--model-path",default="models/weights/medgemma-1.5-4b-it")
    a=p.parse_args()
    if a.limit<1 or a.limit>624:p.error("limit must be between 1 and 624")
    if a.download:fetch()
    elif a.infer:inference(a.limit,a.model_path)
    else:score()
if __name__=="__main__":main()
