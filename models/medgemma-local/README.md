# MedGemma 1.5 4B — local 8 GB RTX 4060 evaluation

[MedGemma comparison research](../../evaluation/medgemma-50-disease-pipeline.md) · [Model card](https://developers.google.com/health-ai-developer-foundations/medgemma/model-card) · [Official weights](https://huggingface.co/google/medgemma-1.5-4b-it)

## Suitability

Google's 4B model is the appropriate local candidate for an NVIDIA RTX 4060 with **8 GB VRAM**. Google's approximate 4-bit static weight footprint is **3.4 GB**, with runtime, activation/image encoder and KV-cache overhead additional. The 27B model is not a sensible fit for 8 GB. Local operation is free of per-request API charges, but **requires acceptance of Google's Health AI Developer Foundations terms**, internet download, disk space and compatible CUDA drivers. No commercial or clinical clearance implied.

**Use:** Start with text-only structured clinical context on *fabricated* cases. MedGemma supports images but CT/MRI 3D and whole slide pathology require special preprocessing and may not fit this 8GB configuration; do not assume all modality paths work.

## Step 1: Prepare WSL Python and GPU

```bash
cd ~/projects/medical-ai-labo-analysis
git pull origin main
nvidia-smi                    # confirm 8 GB NVIDIA GPU is exposed in WSL
python3 -m venv .venv-medgemma
source .venv-medgemma/bin/activate
python -m pip install --upgrade pip
# Install CUDA-enabled PyTorch for your NVIDIA driver/CUDA compatibility:
# https://pytorch.org/get-started/locally/
python -m pip install -r models/medgemma-local/requirements.txt
python -c 'import torch; print(torch.__version__,torch.cuda.is_available())'
```

On some Windows/WSL Python versions or NVIDIA architectures, torch/bitsandbytes binary wheels are incompatible; resolve that before downloading many GB. Avoid running a model simultaneously with memory-heavy emulators.

## Step 2: Accept model terms and sign in

Open [google/medgemma-1.5-4b-it](https://huggingface.co/google/medgemma-1.5-4b-it), accept the model agreement with your own account, and log in locally:

```bash
hf auth login
python3 models/medgemma-local/download.py                   # preview, no transfer
python3 models/medgemma-local/download.py --apply            # actual gated download
```

Downloads default to `models/weights/medgemma-1.5-4b-it/`, which is Git-ignored. Use `--revision COMMIT_SHA` to pin an exact model revision, and record this plus hashes for reproducible evaluation. Download uses the official Hugging Face client and gated authentication; it cannot bypass terms/access rules.

## Step 3: 4-bit test

```bash
python3 models/medgemma-local/infer.py
```

The script loads the official weights using Transformers + bitsandbytes 4-bit NF4 double quantization, one CUDA GPU, and small `max_new_tokens`. It tests a **synthetic text-only vignette**. It writes generated text, runtime and measured PyTorch peak allocated VRAM to `evaluation/results/medgemma-local-smoke.json` (Git-ignored). Peak allocation is not total `nvidia-smi` VRAM consumption. The script has **not** been executed on your RTX 4060, so actual memory fit and output validity are unknown. If out of memory: free other GPU processes, reduce prompt/image complexity, use fewer new tokens or an officially compatible prequantized runtime after verifying format/rights. Do not silently offload large fractions to limited system RAM.

## Step 4: Compare, don't assume

The smoke JSON is **not** a medical accuracy result. An adapter must first convert actual expert-labeled independent evaluation cases into the same structured schema as `scripts/evaluate_context.py`. Do not reuse training cases for test. Run an identical specialist or rule-based baseline, measure field-level F1, missed safety flags, guideline appropriateness, abstention, RAM, latency and generalization. Use `scripts/compare_context_models.py` only after both systems produce **case-matched structured predictions**.

## Practical boundaries
- 8 GB **GPU VRAM** does not equal 8 GB total system RAM; WSL may also have strict RAM caps.
- No patient data should be entered into smoke prompts, committed to Git, or sent to outside services.
- For CT/MRI/ultrasound, verify image/volume preprocessing and independently validate each pathway.
- MedGemma is research infrastructure, not a doctor or treatment recommender.
