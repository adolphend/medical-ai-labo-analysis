#!/usr/bin/env python3
"""Download an explicitly approved evaluation artifact, verify SHA256, and stage for DVC.
No credentials, dataset archives or patient information are stored in Git.
"""
import argparse, hashlib, json, os, pathlib, shutil, subprocess, tempfile, urllib.parse, urllib.request
ROOT=pathlib.Path(__file__).resolve().parents[1]
REG=ROOT/"evaluation/dataset-registry.json"
def download(dataset_id, dry_run=True, max_bytes=2_000_000_000, track=False):
    records=json.loads(REG.read_text())["datasets"]
    record=next((d for d in records if d["id"]==dataset_id),None)
    if record is None: raise ValueError("Unknown dataset")
    if not record.get("approved") or not record.get("version") or not record.get("sha256"):
        raise ValueError("Dataset not approved/versioned. Review rights and enter a verified SHA256 first.")
    source=record.get("download_url")
    if not source or urllib.parse.urlparse(source).scheme!="https":
        raise ValueError("No direct approved HTTPS download_url; portal pages and logins cannot be downloaded automatically")
    expected=record["sha256"].lower()
    if len(expected)!=64 or any(c not in "0123456789abcdef" for c in expected):
        raise ValueError("Invalid expected SHA256")
    name=pathlib.PurePosixPath(urllib.parse.urlparse(source).path).name
    if not name or name in (".",".."): raise ValueError("Invalid source filename")
    destination=ROOT/"data/raw"/dataset_id/name
    if dry_run:
        print(json.dumps({"dataset":dataset_id,"source":source,"destination":str(destination),"action":"PREVIEW"}))
        return
    destination.parent.mkdir(parents=True,exist_ok=True)
    fd,tmp=tempfile.mkstemp(prefix=".download-",dir=destination.parent)
    os.close(fd)
    try:
        digest=hashlib.sha256()
        total=0
        req=urllib.request.Request(source,headers={"User-Agent":"Medical-AI-Research-Dataset-Fetcher/1.0"})
        with urllib.request.urlopen(req,timeout=60) as response,open(tmp,"wb") as out:
            final_url=response.geturl()
            if urllib.parse.urlparse(final_url).scheme!="https":
                raise ValueError("Redirected to non-HTTPS endpoint")
            while True:
                chunk=response.read(1024*1024)
                if not chunk: break
                total+=len(chunk)
                if total>max_bytes: raise ValueError("Download exceeds max-bytes")
                digest.update(chunk);out.write(chunk)
        if digest.hexdigest()!=expected: raise ValueError("SHA256 mismatch: refusing unverified data")
        os.replace(tmp,destination)
        print(f"Verified {dataset_id}: {total} bytes, SHA256 {expected}")
        if track:
            if shutil.which("dvc") is None: raise RuntimeError("DVC not installed; downloaded file verified but not tracked")
            subprocess.run(["dvc","add",str(destination.relative_to(ROOT))],cwd=ROOT,check=True)
            print("DVC pointer created locally; review metadata before git add/commit")
    finally:
        if os.path.exists(tmp): os.unlink(tmp)
def main():
    a=argparse.ArgumentParser()
    a.add_argument("--dataset",required=True)
    a.add_argument("--apply",action="store_true")
    a.add_argument("--dvc-add",action="store_true")
    a.add_argument("--max-bytes",type=int,default=2_000_000_000)
    args=a.parse_args()
    if args.max_bytes<1: a.error("max-bytes must be positive")
    if args.dvc_add and not args.apply: a.error("--dvc-add requires --apply")
    download(args.dataset,not args.apply,args.max_bytes,args.dvc_add)
if __name__=="__main__": main()
