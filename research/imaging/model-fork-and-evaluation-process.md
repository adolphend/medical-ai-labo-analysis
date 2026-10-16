# Fork, benchmark and integration process

[Integration registry](model-integration-registry.md) · [Research index](README.md)

**Current state:** fork documentation only. No external GitHub forks were created by this update. Fork selectively: licensing, maintainability and model interfaces differ. For unmodified packages, prefer upstream dependency with pinned version/commit to avoid 40 separate forks.

## Standard workflow for each eligible upstream project

1. Verify repository URL, code license, weight terms, academic source, maintenance and resource needs. If commercial use is incompatible, document and exclude from proprietary deployment until resolved.
2. Check whether upstream repo already exists under our GitHub account, to avoid accidental duplicates.
3. Fork via GitHub UI (repository page → **Fork**) or authenticated GitHub CLI: `gh repo fork OWNER/REPO --clone=false`. A GitHub fork retains the original repository license.
4. Clone the **fork** in a separate development directory: `git clone https://github.com/adolphend/REPO.git`; `cd REPO`; `git remote add upstream https://github.com/OWNER/REPO.git`.
5. Record upstream commit hash, environment/dependency lock, checkpoint source, hash, legal terms and provenance.
6. Run the upstream's inference smoke test *without* patient data; measure latency, peak RAM and failures on the actual CPU. If impractical, report as unsuitable rather than promise CPU performance.
7. Add an adapter to **our main repository** (separate codebase) with stable input/output schema. Do not merge unrelated upstream code into the research repository.
8. Implement deterministic quality guards; give every output provenance and unambiguous 'research only' marking.
9. Benchmark accuracy/reliability against published test data, external sites and expert references. Compare clinically meaningful error types, not just aggregate accuracy.
10. Upstream maintenance: fetch upstream updates deliberately, rerun tests, keep local patches minimal, document conflicts and security updates.

## Example GitHub CLI commands (only after user has authenticated `gh`)

```bash
gh auth status
gh repo fork echonet/dynamic --clone=false
gh repo fork baumgach/SonoNet-weights --clone=false
gh repo fork mlmed/torchxrayvision --clone=false
gh repo fork rajpurkarlab/CheXzero --clone=false
gh repo fork nipreps/mriqc --clone=false
gh repo fork wasserth/TotalSegmentator --clone=false
```

These are examples **not commands already executed**. Repository owners, eligibility and account namespace must be verified at execution; some forks may require user confirmation. Do not blindly fork every framework.

## Recommended forks vs dependencies

- **Fork when customizing inference code:** EchoNet-Dynamic, SonoNet, specialized CXR classifier, MRIQC or TotalSegmentator *if and only if* a patch is necessary and licensing is acceptable.
- **Use pinned dependencies when unmodified:** pydicom, OpenCV, medSpaCy, NeuroKit2, SimpleITK and ordinary libraries.
- **Use independent managed installations:** Orthanc, OHIF, HAPI FHIR; avoid copying their entire histories into the research repo.
- **Avoid inferring permission from public GitHub access:** code, weights, training data and patient data have separate rights.

## Adapter requirements

Define one input/output contract per task, not a shared 'universal diagnosis' schema:

```json
{
  "task": "echo_lv_ef_research",
  "modality": "ultrasound",
  "study_id": "synthetic-study-001",
  "input_provenance": "deidentified",
  "model_repo": "echonet/dynamic",
  "model_commit": "PIN_EXACT_SHA",
  "weights_sha256": "VERIFY",
  "result": {"ejection_fraction": null},
  "uncertainty": null,
  "review_status": "research_only"
}
```

The example contains no prediction. Values remain null until reproducible inference runs.

## Integration priorities

**Wave 1:** rule-based DICOM QC, ultrasound plane check or echo EF, clinical text extraction.  
**Wave 2:** selected radiology anatomy/observation models; draft report consistency checks.  
**Wave 3:** disease-specific clinical validation, multimodality synthesis and clinician-governed follow-up.

Do not deploy automatic treatment recommendations, population screening or image-to-image synthetic substitution from research-only results.
