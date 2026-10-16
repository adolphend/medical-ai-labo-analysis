---
name: context-safety
description: Assess clinical context extraction and workflow safety
compatibility: opencode
---

# context-safety

Read evaluation/README.md and scripts/evaluate_context.py. Compare facts, missing information, examination candidates, contraindication flags, human review escalation and evidence ID traceability against expert-labeled gold JSON. Document chronology and context contradictions that exact match misses. Include abstention and false urgency/missed urgency in clinical validation design. Human decision required.

## Output
Record inputs, citations, artifact SHA, test commands, numerical results only when actually measured, safety limitations and next unresolved checks. Never mark unexecuted tests as passed.
