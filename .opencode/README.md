# OpenCode disease pipeline agents

The repository includes:
- [disease-factory](agents/disease-factory.md), **primary** agent to build one disease pathway at a time.
- [medical-disease-architect](agents/medical-disease-architect.md), primary research architecture and clinical-evidence rules.
- [build-disease](commands/build-disease.md), a reusable OpenCode slash command.
- [audit-disease](commands/audit-disease.md), a research quality check.

OpenCode recognizes project-level agents at `.opencode/agents/*.md` according to its [agent documentation](https://opencode.ai/docs/agents/).

## Use

Run OpenCode from the **repository root**, with the project downloaded:

```bash
cd ~/projects/medical-ai-labo-analysis
git pull origin main
opencode
```

Select `disease-factory` as the primary agent (agent selection in OpenCode) and use:

```text
/build-disease abdominal-aortic-aneurysm
```

Or ask the agent directly: `Research the next unresearched disease in the registry.`

For a review, use `/audit-disease abdominal-aortic-aneurysm`.

When you want the entire 50-disease **scaffold** (not 50 completed clinical reviews), execute:

```bash
python3 scripts/scaffold_diseases.py
```

## Files created per condition

```text
diseases/<slug>/
  README.md
  clinical-presentation.md
  examination-selection.md
  acquisition-quality.md
  anatomy-findings.md
  open-models.md
  interpretation-report.md
  management-evidence.md
  follow-up.md
  validation.md
  pipeline.yaml
```

The agent is intentionally incremental. It works one condition at a time and flags nonvalidated medical claims. It does not provide autonomous diagnosis or medical prescribing.
