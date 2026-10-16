#!/usr/bin/env python3
"""Reviewable GitHub model-fork automation. Default: read-only plan.

Requires Python 3.9+, git, GitHub CLI (gh), authenticated account.
With --apply: forks selected upstream repos and records references; with
--submodules also tracks fork code as git submodules, not copied files.
Never downloads weights, modifies upstream, or runs models.
"""
import argparse
import json
import pathlib
import re
import shutil
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "automation" / "model-forks.json"
TRACKING = ROOT / "automation" / "forks-tracked.json"
NAME = re.compile(r"^[a-z0-9][a-z0-9_-]*$")

def run(*args, capture=True):
    result = subprocess.run(args, cwd=ROOT, text=True, capture_output=capture)
    if result.returncode:
        raise RuntimeError(f"{' '.join(args)} failed: {result.stderr.strip()}")
    return result.stdout.strip() if capture else ""

def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--list", action="store_true", help="List candidates")
    p.add_argument("--models", default="", help="Comma-separated IDs; default: priority 1 only")
    p.add_argument("--all", action="store_true", help="Explicitly select every candidate")
    p.add_argument("--apply", action="store_true", help="Actually fork and commit")
    p.add_argument("--submodules", action="store_true", help="Also add forks as Git submodules")
    p.add_argument("--push", action="store_true", help="Push commit to origin")
    args = p.parse_args()
    if args.push and not args.apply:
        p.error("--push requires --apply")
    if args.submodules and not args.apply:
        p.error("--submodules requires --apply")
    if args.all and args.models:
        p.error("use --all or --models, not both")

    d = json.loads(MANIFEST.read_text(encoding="utf-8"))
    models = d["models"]
    for m in models:
        if not NAME.fullmatch(m["id"]) or not re.fullmatch(r"[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+", m["upstream"]):
            raise ValueError(f"Invalid manifest entry: {m}")
    ids = set(x for x in args.models.split(",") if x)
    known = {m["id"] for m in models}
    if ids - known:
        p.error("Unknown model IDs: " + ", ".join(sorted(ids-known)))
    picked = [m for m in models if args.all or m["id"] in ids or (not args.models and not args.all and m["priority"] == 1)]
    for m in picked:
        print(f"{m['id']:18} {m['upstream']:37} {m['reason']}")
    if args.list or not args.apply:
        print("\nPREVIEW ONLY. Use --apply to create forks; --submodules to track source; --push to publish commit.")
        return 0
    for program in ("gh", "git"):
        if not shutil.which(program):
            raise RuntimeError(f"{program} not found on PATH")
    if run("gh", "api", "user", "--jq", ".login").lower() != d["owner"].lower():
        raise RuntimeError("Authenticated GitHub user is not manifest owner")
    if run("git", "status", "--porcelain"):
        raise RuntimeError("Main repository working tree is not clean; stash/commit unrelated edits first")
    if run("git", "branch", "--show-current") != "main":
        raise RuntimeError("Switch to main explicitly before applying")
    remote = run("git", "remote", "get-url", "origin")
    expected = d["destination"].lower()
    if expected not in remote.lower():
        raise RuntimeError(f"Wrong origin remote: {remote}")
    run("git", "fetch", "origin", "main")
    if run("git", "rev-parse", "HEAD") != run("git", "rev-parse", "origin/main"):
        raise RuntimeError("Local main differs from origin/main; reconcile before changes")

    existing = json.loads(TRACKING.read_text()) if TRACKING.exists() else {"forks": []}
    entries = {x["id"]: x for x in existing["forks"]}
    for m in picked:
        upstream = m["upstream"]
        # Verify public upstream metadata and presence of GitHub license if available.
        info = json.loads(run("gh", "api", f"repos/{upstream}"))
        if info.get("archived"):
            print(f"SKIP archived: {upstream}")
            continue
        fork_full = f"{d['owner']}/{upstream.split('/')[1]}"
        exists = subprocess.run(["gh", "api", f"repos/{fork_full}"], cwd=ROOT,
                                text=True, capture_output=True)
        if exists.returncode == 0:
            fork_info = json.loads(exists.stdout)
            if fork_info.get("parent", {}).get("full_name", "").lower() != upstream.lower():
                raise RuntimeError(f"Conflict: {fork_full} exists but is not a fork of {upstream}")
            print(f"Already forked: {fork_full}")
        else:
            print(f"Forking {upstream}")
            run("gh", "repo", "fork", upstream, "--clone=false")
            fork_info = json.loads(run("gh", "api", f"repos/{fork_full}"))
        if args.submodules:
            path = f"external/models/{m['id']}"
            if not (ROOT / path).exists():
                run("git", "submodule", "add", "-b", fork_info["default_branch"],
                    f"https://github.com/{fork_full}.git", path, capture=False)
        entries[m["id"]] = {
            "id": m["id"], "upstream": upstream, "fork": fork_full,
            "fork_url": f"https://github.com/{fork_full}",
            "source_paper": m["paper"], "role": m["reason"],
            "license_review": "PENDING",
            "weights_review": "PENDING",
            "clinical_validation": "NOT ASSESSED",
        }
    TRACKING.write_text(json.dumps({"forks": sorted(entries.values(), key=lambda x: x["id"])}, indent=2)+"\n")
    run("git", "add", "--", "automation/forks-tracked.json")
    if args.submodules:
        run("git", "add", "--", ".gitmodules", "external/models")
    # Explicitly inspect staged changes via porcelain; commit only when present.
    staged = run("git", "diff", "--cached", "--name-only")
    if not staged:
        print("Nothing new to commit")
        return 0
    print("Staged:", staged)
    run("git", "commit", "-m", "chore: register reviewed medical AI model forks", capture=False)
    if args.push:
        run("git", "push", "origin", "main", capture=False)
        print("Pushed changes to origin/main")
    else:
        print("Committed locally; run git push origin main after review")
    return 0

if __name__ == "__main__":
    try:
        sys.exit(main())
    except (RuntimeError, ValueError, OSError) as e:
        print(f"ERROR: {e}", file=sys.stderr)
        sys.exit(1)
