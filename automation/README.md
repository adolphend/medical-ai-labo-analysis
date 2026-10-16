# Medical AI model forking agent

[Research index](../research/README.md) · [Model integration registry](../research/imaging/model-integration-registry.md) · [Fork policy](../research/imaging/model-fork-and-evaluation-process.md)

**Purpose:** fork upstream sources under `adolphend`, record the exact fork URLs in this main repository, and optionally attach each fork as a Git **submodule**. This is an automation *script*, not an unattended hosted agent. It only runs when launched on your machine. It does not download pretrained weights or train models. **No forks have been created by this commit.**

## Prerequisites

- Python 3.9+, Git, [GitHub CLI](https://cli.github.com/), network access and Git credentials
- Run `gh auth login` and `gh auth status` as your own user; don't paste access tokens into chat
- Clone `https://github.com/adolphend/medical-ai-labo-analysis`
- Work on a **clean** `main` branch exactly synchronized with `origin/main`
- Verify code **and weights** licenses before commercial incorporation; original fork licenses are preserved

## Safe use

```bash
cd medical-ai-labo-analysis
python3 automation/fork_models.py --list
python3 automation/fork_models.py --models echonet,sononet
```

**Actually create two forks and commit the manifest (no model code vendored):**

```bash
python3 automation/fork_models.py --models echonet,sononet --apply --push
```

**Create two forks and add Git submodules to the main repository:**

```bash
python3 automation/fork_models.py --models echonet,sononet --apply --submodules --push
```

To include all reviewed candidates (not advised until legal/hardware verification):

```bash
python3 automation/fork_models.py --all
# inspect the preview before adding --apply
```

If `--models` is omitted the agent previews or processes **priority-1 models only**. The `--apply` option is required for any mutation, and `--push` additionally publishes its commit to `origin/main`.

## Per-model processes

Each uses the same verification → fork → pin → CPU smoke-test → adapter → benchmark sequence, but the scientific target and installation method differ.

| ID | Upstream and paper | Specific evaluation process | Priority |
|---|---|---|---|
| `echonet` | [echonet/dynamic](https://github.com/echonet/dynamic), [Ouyang 2020](https://doi.org/10.1038/s41586-020-2145-8) | Fork if modifying inference; acquire lawfully usable echo videos; test LV mask and EF on video; validate per-view and dataset; record CPU memory/time; do not import noncommercial dataset into a commercial product. | 1 |
| `sononet` | [baumgach/SonoNet-weights](https://github.com/baumgach/SonoNet-weights), [Baumgartner 2017](https://doi.org/10.1109/TMI.2017.2712367) | Fork weight-access example if changes needed; establish compatible legacy framework/port and weight rights; verify fetal-plane predictions on known planes; do not call it fetal anomaly detection. | 1 |
| `torchxrayvision` | [mlmed/torchxrayvision](https://github.com/mlmed/torchxrayvision), [repository citations](https://github.com/mlmed/torchxrayvision#citation) | Check individual pretrained model architecture, dataset, labels and licenses; normalize DICOM to expected input; benchmark observation labels with patient-wise holdout. | 1 |
| `mriqc` | [nipreps/mriqc](https://github.com/nipreps/mriqc), [Esteban 2017](https://doi.org/10.1371/journal.pone.0184661) | Use neuro-MRI image-quality workflows; evaluate artifact metrics, site shift, CPU time and expert study acceptance; not generic MRI QC. | 1 |
| `chexzero` | [rajpurkarlab/CheXzero](https://github.com/rajpurkarlab/CheXzero), [Tiu 2022](https://doi.org/10.1038/s41551-022-00936-9) | Verify checkpoint and zero-shot text prompts; test a bounded chest finding vocabulary; calibration and external validation mandatory. | 2 |
| `totalsegmentator` | [wasserth/TotalSegmentator](https://github.com/wasserth/TotalSegmentator), [Wasserthal 2023](https://doi.org/10.1148/ryai.230024) | Verify each task's commercial rights; choose few CT regions; benchmark Dice, masks, CPU time/RAM and preprocessing. | 2 |
| `medsam` | [bowang-lab/MedSAM](https://github.com/bowang-lab/MedSAM), [Ma 2024](https://doi.org/10.1038/s41467-024-44824-z) | Choose exact pretrained checkpoint including Lite variant; evaluate prompt-to-mask quality; note outputs aren't automatic organ names. | 2 |
| `radgraph` | [Stanford-AIMI/radgraph](https://github.com/Stanford-AIMI/radgraph), [Jain 2021](https://arxiv.org/abs/2106.14463) | Extract report entities and relations; validate negation, anatomy and contradictions; compare against specialist-annotated reports. | 2 |
| `chexbert` | [stanfordmlgroup/CheXbert](https://github.com/stanfordmlgroup/CheXbert), [Smit 2020](https://aclanthology.org/2020.emnlp-main.117/) | Extract labeled chest radiograph observations from report text; check checkpoints, clinical uncertainty labels and error rates. | 2 |
| `hovernet` | [vqdang/hover_net](https://github.com/vqdang/hover_net), [Graham 2019](https://doi.org/10.1016/j.media.2019.101563) | Test pretrained nuclei segmentation/classification on licensed slide patches; estimate patch memory, scanner and stain shift. | 2 |

## What the agent commits

- `automation/forks-tracked.json`: fork URL, upstream, paper, review-pending license/weights/clinical validation flags.
- If `--submodules`: `.gitmodules` and `external/models/<id>` Git submodule pointers. The external fork code **is not copied** into the parent repository: GitHub uses pointers to other repositories.
- It never commits model checkpoints, datasets, patient records, API tokens or untracked unrelated work.
- The script refuses dirty worktrees, unexpected GitHub user, mismatched `origin`, non-`main` branches and unsynchronized upstream state.

## Important limitations

A public GitHub fork may carry licenses prohibiting commercial use of certain weights, datasets, tasks or derivative materials. Forking is not permission to commercially deploy. Some upstream forks may fail because of GitHub settings, permissions or conflicts. Each execution should be reviewed and errors resolved individually. Check model architecture and checkpoint compatibility, and obtain clinical validation before patient-facing diagnostic/treatment use.

## Complete external inventory (41 repositories)

The [machine-readable manifest](model-forks.json) now covers **all 40 repositories in the diagnostic research catalog plus EchoNet-Dynamic**, which was referenced in the ultrasound research separately. Each entry has a unique ID, upstream source, purpose, modality, and default action. There are **13 fork candidates, 20 prefer-dependency candidates, and 8 require-review candidates**.

**Note:** `--all --apply` explicitly attempts forks of **all 41**, including frameworks normally best used as dependencies, and is **not recommended**. The priority-1 default attempts four forks. You can select an individual model or subset safely with `--models`.

| Default action | IDs | Process |
|---|---|---|
| Fork candidate | echonet, sononet, torchxrayvision, chexzero, mriqc, totalsegmentator, medsam, radgraph, chexbert, hovernet, antspynet, cellpose, histoqc | Verify academic paper, licenses, availability of weights and local utility. Fork under `adolphend` only when code modifications are needed; execute smoke test and benchmark. |
| Pinned dependency | ants, cellprofiler, nnunet, wfdb, ohif, monai, simpleitk, slicer, synthrad-metrics, scispacy, hapi-fhir, medplum, medspacy, neurokit, whisper, opencv, openmrs, pydicom, itksnap, qupath | Check license/security; install from package or exact upstream SHA; register a reproducible adapter. No fork unless customization is required. |
| Review before fork | medgemma, monai-generative, monai-zoo, openfold, luna16-code, sononet-port, us-metrics, colabfold | Verify paper/maintainer identity, checkpoint/weight rights, architecture compatibility, maintenance, hardware and intended use. Fork only if justified. |

### Entire inventory: preview and optional execution

```bash
python3 automation/fork_models.py --all            # preview all 41
python3 automation/fork_models.py --models medsam   # preview one
# Explicit, potentially large-scale fork operation:
python3 automation/fork_models.py --all --apply --push
```

**Do not run the third command without evaluating the license and compute suitability of each project.** GitHub may restrict large batches, duplicate names may conflict, and a partially completed run may require manual recovery. The automation is not a clinical validation tool.

### Model-specific acceptance workflow

For **each manifest entry** the work sequence is:
1. Open `https://github.com/OWNER/REPO`; verify exact origin, branch, active maintenance, license and security status.
2. Read the linked *peer-reviewed paper* when available, making a note if the paper evidence is pending.
3. Find exact pretrained model checkpoint (if this is a trained model) and document checksum, data/license, input/output schema.
4. Measure whether inference works on the available CPU/RAM (and optional GPU) with no training; distinguish unavailable weights from unsupported modality.
5. Decide: fork to maintain patches; install pinned dependency for unmodified code; or defer.
6. If forking, use the agent and record fork metadata; optionally create submodule in `external/models/`.
7. Add a **separate** wrapper/adapter and test in the product codebase. Commit `git add`, `git commit`, `git push` only after reviewing changes.
8. Document clinically relevant accuracy, domain shift, test set, external validation, failures and clinician review, or explicitly mark **not yet verified**.

**No forks or CPU benchmarks have been executed from ChatGPT.**
