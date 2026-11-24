# <arXiv ID> — <short title>

## Citation
- Title / authors / first arXiv date / latest version:
- Venue + status (e.g. "ICLR 2026, accepted — verified at <URL>" or "preprint"):
- PDF: research/papers/pdf/<id>.pdf · Text: research/papers/txt/<id>.txt

## Setup
- Tasks / benchmarks (coding? repo-level? research? planning?):
- Models used (per role):
- Baselines (single agent? flat team? budget-matched? yes/no + how):

## Topology tested
- Depth: 0 = single agent · 1 = orchestrator → workers · 2 = orchestrator → sub-orchestrators → workers · recursive
- Width (workers per orchestrator) and how it was varied:
- Roles (planner, implementer, verifier, reviewer, integrator, router, ...):
- Communication / handoff format; who can write code/files:

## Findings (quote numbers with table/figure/page refs)
- Depth (when does more depth help or hurt?):
- Width (where does adding workers plateau?):
- Role → model placement (which tier where, cost vs quality):
- Verification / review effects:
- Cost / tokens / latency:
- Failure modes observed:

## Implications for Hannibal's Army (label each as INFERENCE)
- Depth-1 design:
- Depth-2 design:
- Which agent/model type goes in which seat:

## Validity
- Evidence grade: A = peer-reviewed + controlled · B = preprint + controlled · C = case study / uncontrolled
- Threats (contamination, not budget-matched, toy tasks, single model family, ...):
