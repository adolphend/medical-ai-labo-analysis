#!/usr/bin/env python3
"""Cross-platform opt-in MedGemma environment installer (no model download by default)."""
import argparse, os, pathlib, platform, shutil, subprocess, sys

ROOT=pathlib.Path(__file__).resolve().parents[2]
VENV=ROOT/".venv-medgemma"
def call(args):
    print("+", " ".join(map(str,args)),flush=True)
    subprocess.run(list(map(str,args)),check=True,cwd=ROOT)
def main():
    p=argparse.ArgumentParser()
    p.add_argument("--apply",action="store_true",help="Create env and install packages")
    p.add_argument("--backend",choices=["auto","cuda","mps","cpu"],default="auto")
    p.add_argument("--torch-index",default="https://download.pytorch.org/whl/cu126",
                   help="Official CUDA PyTorch wheel index; verify against pytorch.org before install")
    a=p.parse_args()
    system=platform.system()
    backend=("mps" if system=="Darwin" else "cuda") if a.backend=="auto" else a.backend
    if backend=="mps" and system!="Darwin":p.error("MPS requires macOS")
    if backend=="cuda" and system=="Darwin":p.error("NVIDIA CUDA profile is not supported on macOS")
    if sys.version_info<(3,10) or sys.version_info>=(3,14):
        p.error("Use supported Python 3.10–3.13 (Python 3.11 recommended)")
    if backend=="cuda" and not shutil.which("nvidia-smi"):
        print("WARNING: nvidia-smi not on PATH; verify drivers and WSL GPU passthrough.")
    pip=VENV/("Scripts/python.exe" if system=="Windows" else "bin/python")
    print(f"OS={system}; backend={backend}; venv={VENV}; python={sys.version.split()[0]}")
    print("Model download is separate and requires accepting Google gated model terms.")
    if not a.apply:
        print("PREVIEW ONLY. Use --apply to install packages.")
        return
    if not pip.exists():
        call([sys.executable,"-m","venv",VENV])
    call([pip,"-m","pip","install","--upgrade","pip"])
    torch_args=[pip,"-m","pip","install","torch"]
    if backend=="cuda":
        if not a.torch_index.startswith("https://download.pytorch.org/whl/cu"):
            p.error("CUDA PyTorch index must be an official download.pytorch.org CUDA wheel URL")
        torch_args+=["--index-url",a.torch_index]
    if backend=="cpu":
        torch_args+=["--index-url","https://download.pytorch.org/whl/cpu"]
    call(torch_args)
    call([pip,"-m","pip","install","transformers>=4.50,<5","accelerate","huggingface_hub","pillow"])
    if backend=="cuda":
        call([pip,"-m","pip","install","bitsandbytes"])
    call([pip,"-c","import torch; print('torch:',torch.__version__,'CUDA:',torch.cuda.is_available(),'MPS:',getattr(torch.backends,'mps',None) and torch.backends.mps.is_available())"])
    print("Environment installed. Next: accept HF terms; authenticate; preview/run download.py; run infer.py for CUDA.")
    if backend=="mps":
        print("On Apple Silicon: no bitsandbytes NF4 here; full-precision 4B inference can require substantial unified memory.")
if __name__=="__main__":main()
