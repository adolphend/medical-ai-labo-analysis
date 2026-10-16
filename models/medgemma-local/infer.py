#!/usr/bin/env python3
"""Research-only local 4-bit MedGemma inference for 8GB NVIDIA GPUs.
Never makes autonomous clinical decisions. Generates output JSON for auditing.
"""
import argparse
import json
from pathlib import Path
import time

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--model-path", default="models/weights/medgemma-1.5-4b-it")
    p.add_argument("--prompt", default="Extract the stated facts from this synthetic vignette: A fictional patient reports a headache for two days. Do not diagnose or recommend treatment.")
    p.add_argument("--max-new-tokens", type=int, default=128)
    p.add_argument("--output", default="evaluation/results/medgemma-local-smoke.json")
    args=p.parse_args()
    if not 1 <= args.max_new_tokens <= 256: p.error("max-new-tokens must be 1..256 for memory safety")
    if not Path(args.model_path).exists():
        p.error("Model not downloaded. First run download.py --apply after accepting model terms.")
    import torch
    if not torch.cuda.is_available():
        p.error("CUDA unavailable; this 8GB GPU profile requires a working NVIDIA CUDA environment")
    props=torch.cuda.get_device_properties(0)
    vram_gib=props.total_memory/(1024**3)
    print(f"GPU: {props.name}; total VRAM {vram_gib:.2f} GiB")
    if vram_gib < 7.0: p.error("This configuration was designed for approximately 8GB VRAM")
    from transformers import AutoProcessor, AutoModelForImageTextToText, BitsAndBytesConfig
    config=BitsAndBytesConfig(load_in_4bit=True, bnb_4bit_quant_type="nf4",
                              bnb_4bit_compute_dtype=torch.float16,
                              bnb_4bit_use_double_quant=True)
    processor=AutoProcessor.from_pretrained(args.model_path)
    model=AutoModelForImageTextToText.from_pretrained(
        args.model_path, device_map={"":0}, quantization_config=config,
        torch_dtype=torch.float16, low_cpu_mem_usage=True)
    messages=[{"role":"user","content":[{"type":"text","text":args.prompt}]}]
    inputs=processor.apply_chat_template(messages,add_generation_prompt=True,
                                         tokenize=True,return_dict=True,return_tensors="pt").to("cuda:0")
    torch.cuda.reset_peak_memory_stats()
    start=time.perf_counter()
    with torch.inference_mode():
        out=model.generate(**inputs,max_new_tokens=args.max_new_tokens,do_sample=False)
    torch.cuda.synchronize()
    duration=time.perf_counter()-start
    output=processor.decode(out[0][inputs["input_ids"].shape[1]:],skip_special_tokens=True)
    artifact={"model":"google/medgemma-1.5-4b-it","local_path":str(Path(args.model_path)),
        "quantization":"bitsandbytes_nf4_double_quant","task":"synthetic_text_smoke",
        "generated_text":output,"elapsed_seconds":round(duration,3),
        "peak_allocated_gpu_gib":round(torch.cuda.max_memory_allocated()/(1024**3),3),
        "gpu":props.name,"clinical_validation":"NOT_VALIDATED"}
    dest=Path(args.output);dest.parent.mkdir(parents=True,exist_ok=True)
    dest.write_text(json.dumps(artifact,indent=2)+"\n",encoding="utf-8")
    print(f"Saved {dest}; peak GPU allocation {artifact['peak_allocated_gpu_gib']} GiB")

if __name__=="__main__":main()
