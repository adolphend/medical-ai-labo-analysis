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
