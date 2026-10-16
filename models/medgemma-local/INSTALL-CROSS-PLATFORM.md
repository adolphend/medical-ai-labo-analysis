# Install MedGemma locally on Windows, Ubuntu/WSL or macOS

[MedGemma local overview](README.md) · [Cross-platform installer](install.py) · [Google official model page](https://huggingface.co/google/medgemma-1.5-4b-it)

This installer provides a **preview by default**, installs a Python virtual environment only with `--apply`, and **does not automatically download restricted model weights**. All systems need internet access for packages; Google model terms must be accepted on Hugging Face before downloading. The local 4-bit inference script currently targets **NVIDIA CUDA**, especially an 8 GB RTX 4060. Apple MPS does not use the same bitsandbytes NF4 approach.

## Requirements

- Python **3.11 recommended** (3.10–3.13 accepted by the script), Git, adequate disk space.
- Windows 11 or Ubuntu with NVIDIA RTX GPU: working `nvidia-smi` and CUDA-enabled PyTorch wheels; driver must support installed CUDA runtime.
- macOS: Apple Silicon recommended for MPS, sufficient unified memory (16 GB+ advisable for experimentation with 4B full-precision weights, not a tested minimum). Intel Mac may be CPU-only and slow.
- Dataset and model weights remain outside Git. Download only after separately accepting Google's model-specific license.

## Windows PowerShell

```powershell
cd C:\path\to\medical-ai-labo-analysis
py -3.11 models/medgemma-local/install.py --backend cuda
.\models\medgemma-local\install.ps1 -Backend cuda -Apply
.\.venv-medgemma\Scripts\python.exe models/medgemma-local/verify.py
.\.venv-medgemma\Scripts\python.exe models/medgemma-local/download.py
```

Verify the PyTorch CUDA wheel index against [official PyTorch installation instructions](https://pytorch.org/get-started/locally/) for your GPU/driver; override the index with `-TorchIndex` if necessary. PowerShell invocation via `py -3.11` requires the Python Launcher and Python 3.11 installed. Install script invokes Python, not PowerShell policy-changing commands.

## Ubuntu / WSL2 (recommended for RTX 4060 development)

```bash
cd ~/projects/medical-ai-labo-analysis
git pull origin main
nvidia-smi
python3 models/medgemma-local/install.py --backend cuda
bash models/medgemma-local/install.sh --backend cuda --apply
.venv-medgemma/bin/python models/medgemma-local/verify.py
.venv-medgemma/bin/python models/medgemma-local/download.py
```

If `python3 -m venv` is unavailable, install the Ubuntu package `python3-venv`. Prefer Python 3.11 explicitly (`PYTHON=python3.11 bash ...`) if the default is incompatible.

## macOS (Apple Silicon)

```bash
cd medical-ai-labo-analysis
python3 models/medgemma-local/install.py --backend mps
bash models/medgemma-local/install.sh --backend mps --apply
.venv-medgemma/bin/python models/medgemma-local/verify.py
```

This installs standard PyTorch MPS and Transformers **without bitsandbytes**. **The existing `infer.py` is CUDA-only**; on macOS you must use a separately tested MPS-compatible model loader (for example `infer_mps.py` if introduced later) with adequate unified memory, or an officially supported compatible quantized local runtime. Do not use the CUDA command on Mac.

## Download the gated weights — optional and separate

1. Open [Google MedGemma Hugging Face](https://huggingface.co/google/medgemma-1.5-4b-it) and accept the Health AI Developer Foundations model access terms.
2. Authenticate using `.venv-medgemma/bin/hf auth login` (Windows: `.venv-medgemma\Scripts\hf.exe auth login`), or securely provide a token in environment variables; never paste it into scripts or commit it.
3. Run `download.py` without flags for preview.
4. Run `download.py --apply --revision EXACT_COMMIT_SHA` after verifying rights and storage. The download can be several GB and may include full-precision weights even if CUDA inference later uses 4-bit quantization.

## Test on RTX 4060

```bash
.venv-medgemma/bin/python models/medgemma-local/infer.py
```

Windows: substitute `.venv-medgemma\Scripts\python.exe`. The script performs a **fabricated vignette smoke test**, records elapsed time and GPU allocation, and outputs `evaluation/results/medgemma-local-smoke.json`. It does not produce medical validation scores. Model download, load and runtime have not been tested on your GPU via this ChatGPT session.

## Failure handling

- **CUDA unavailable:** verify `nvidia-smi`, NVIDIA driver and that PyTorch was installed from a compatible official CUDA wheel index.
- **Import or missing dependency:** inspect virtual environment, Python version, installed `transformers` and `bitsandbytes` support.
- **Out of memory:** close other GPU applications, use shorter prompts/fewer tokens, avoid image/volume workloads, inspect actual VRAM; no promised 8GB fit.
- **Gated 403:** accept terms and authenticate; installation script cannot bypass model access restrictions.
- **Mac MPS unavailable:** check Apple Silicon/Metal and `torch.backends.mps.is_available()`; consider CPU-only demonstration with appropriate memory.
- **Restricted/research data:** never upload patient data or confidential datasets through default prompts, telemetry or public Git.
