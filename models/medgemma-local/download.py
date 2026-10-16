#!/usr/bin/env python3
"""Opt-in gated model snapshot download. No download without --apply."""
import argparse
import os
from pathlib import Path

MODEL = "google/medgemma-1.5-4b-it"

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--apply", action="store_true", help="Actually download (network + disk usage)")
    p.add_argument("--revision", default="main", help="Pin an exact revision for reproducibility")
    p.add_argument("--dest", default="models/weights/medgemma-1.5-4b-it")
    args = p.parse_args()
    dest = Path(args.dest).resolve()
    if not args.apply:
        print(f"PREVIEW: {MODEL}@{args.revision} -> {dest}. Requires approved Google model terms and Hugging Face login.")
        return
    if not (os.environ.get("HF_TOKEN") or os.environ.get("HUGGING_FACE_HUB_TOKEN")):
        print("Authenticate with 'hf auth login' or configure HF_TOKEN securely; cached login may also work.")
    from huggingface_hub import snapshot_download
    dest.mkdir(parents=True, exist_ok=True)
    path = snapshot_download(repo_id=MODEL, revision=args.revision,
                             local_dir=str(dest), token=True)
    print(f"Downloaded authorized model snapshot to {path}; do not add weights to Git.")

if __name__ == "__main__":
    main()
