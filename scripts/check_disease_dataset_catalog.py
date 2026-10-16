#!/usr/bin/env python3
"""Validate 50-disease dataset discovery mapping; metadata only, no downloads."""
import csv, json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
catalog=json.loads((ROOT/"evaluation/disease-dataset-catalog.json").read_text())
with (ROOT/"diseases/registry.csv").open(newline="") as fh:
    slugs={row["slug"] for row in csv.DictReader(fh)}
sources={s["id"] for s in catalog["sources"]}
mapping={d["disease"] for d in catalog["diseases"]}
assert len(sources)==len(catalog["sources"]), "Duplicate source ID"
assert len(mapping)==len(catalog["diseases"]), "Duplicate disease ID"
assert slugs==mapping, f"Registry mismatch: missing {slugs-mapping}, unexpected {mapping-slugs}"
for entry in catalog["diseases"]:
    assert entry["candidates"], entry["disease"]
    assert entry["status"]=="EVIDENCE_PENDING", entry["disease"]
    for c in entry["candidates"]:
        assert c["dataset_id"] in sources, c
        assert c["match"] in ("task_relevant_check_labels","related_or_proxy_not_disease_validated"), c
for source in catalog["sources"]:
    assert not source["approved"], "Source unexpectedly approved without dataset governance audit"
print(f"Validated {len(catalog['sources'])} candidate sources and {len(mapping)} disease mappings; no datasets downloaded.")
