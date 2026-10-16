# Disease JSON workflow contract

**One disease = one declarative `procedure.json`.** It defines the starting event, ordered steps, per-step evaluation, model reference, input/output contracts and dependencies. The interpreter performs **static validation and safe simulation**, not medical inference or autonomous treatment.

Each step contains:
- `id`, `kind`, `depends_on`, `required`
- `input_keys`, `output_keys` for typed data handoffs
- `executor`: `human`, `rule`, `model`, or `none`
- `model`: explicit `registry_id` and `version` for model steps, or null
- `evaluation`: `dataset_id`, `metric`, `target`, `status`, `result_path` (per-step, never inherited from another model)
- `evidence_status`: `pending` or `verified`
- `approval_required`: true at clinical interpretation and management steps

A model step with missing evaluation, weights or adapter must **not run**. An evaluation status of `passed` is a recorded assertion requiring independent evidence; this interpreter does not trust it as clinical authorization. A model output is never interpreted as a final diagnosis. Checkup eligibility and imaging must be evaluated per disease and patient context.

## Commands

```bash
python3 scripts/scaffold_diseases.py --disease heart-failure
python3 scripts/interpret_procedure.py diseases/heart-failure/procedure.json
python3 scripts/interpret_procedure.py diseases/heart-failure/procedure.json --json
python3 -m unittest discover -s tests -p 'test_procedure*.py' -v
```

The output contains a validated ordered list of steps, runnable/planned/blocked flags and reasons. It does **not** execute model code; integration must use separately tested, permissioned adapters and per-step evaluation artifacts.
