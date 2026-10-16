#!/usr/bin/env python3
"""Fail-closed dataset governance check. Never downloads or uploads data."""
import argparse
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
REGISTRY=ROOT/"evaluation"/"dataset-registry.json"

def validate_registry(registry, require_approved=None):
    if registry.get("schema_version") != 1 or not isinstance(registry.get("datasets"),list):
        raise ValueError("Invalid registry schema")
    seen=set()
    for item in registry["datasets"]:
        for key in ("id","url","modality","task","access","approved","version","sha256"):
            if key not in item:
                raise ValueError(f"Missing {key} on {item.get('id', '?')}")
        if item["id"] in seen:
            raise ValueError("Duplicate dataset ID")
        seen.add(item["id"])
        if type(item["approved"]) is not bool:
            raise ValueError("approved must be a boolean")
        if item["approved"] and (not item["version"] or not item["sha256"] or len(item["sha256"])!=64):
            raise ValueError(f"{item['id']}: approved dataset needs version and SHA256 manifest checksum")
    if require_approved:
        item=next((d for d in registry["datasets"] if d["id"]==require_approved),None)
        if not item:
            raise ValueError("Unknown dataset ID")
        if not item["approved"]:
            raise ValueError(f"{require_approved}: not approved for evaluation; complete rights audit first")
    return len(seen)

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("--require-approved",help="Fail unless dataset ID is approved and versioned")
    args=p.parse_args()
    n=validate_registry(json.loads(REGISTRY.read_text()),args.require_approved)
    print(f"Validated metadata for {n} datasets; no data downloaded")
if __name__=="__main__":
    main()
