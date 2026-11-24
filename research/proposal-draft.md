# Hannibal's Army — proposal draft v0 (for adversarial review)

Author: lead (Claude). Date: 2026-10-15. Evidence: `research/depth-and-seats.md` and the 22 notes in
`research/papers/notes/`. This draft is meant to be attacked.

## 0. Scope (set by the user, 2026-10-15)

This system is for **building full systems from scratch and making major updates**, not small tasks.
Evidence from single-issue fixes (SWE-bench-style) transfers weakly; project-scale evidence
(ProgramBench, Commit0, CodeProjectEval, SPOQ epics, the user's multi-day sprints) is primary.
"Depth 0 for small tasks" is out of scope: small tasks are not given to the army at all.

## 1. What the deliverable is

A formalized, tool-agnostic orchestration technique, shipped as three parts:

1. **DOCTRINE.md** (~150 lines): the rules below, each tagged with its evidence or as INFERENCE.
2. **Skill pack** (Agent Skills `SKILL.md` format, works in Claude Code / Codex / OpenCode / Gemini CLI):
   one skill per seat (commander, general, scout, builder, reviewer, integrator) + `assets/` templates
   (worker spec, skeleton spec, report, ledger) + `adapters/orca.md` for Orca mechanics.
3. **Eval suite**: budget-matched comparisons on the user's real tasks that validate or kill each rule.

Not a workflow engine: Orca already provides runs, dispatch, inbox, worktrees.

## 2. Depth policy

| Depth | Use when | Evidence |
|---|---|---|
| 0 — one strong agent | Task is sequential / tightly coupled, or < ~5 parallelizable pieces / < ~4 h of work | Kim (A): −50% to −70% on sequential planning; AsynCodeBench (B): strongest models regress under decomposition; SPOQ (C+) threshold |
| 1 — commander → workers | **Default** whenever work has ≥2 separable parts | Samway, Co-Coder, AsynCodeBench, SWE-Review, Gandhi |
| 2 — marshal → generals → soldiers | Only if: ≥2 sub-projects each depth-1-sized; root context would overflow; budget allows ~2.4× worker tokens; every general is a frontier model | MasDrift (B): +4.2 completion, +9.0 unauthorized actions (5-model mean), 2.4× tokens; all-Sol L2 was fine (100% completion, 1.5% UA) |
| 3+ | Never | MasDrift: +0.5 completion, +8.1 UA, ~2× tokens again |

## 3. Seats and who sits in them

| Seat | Agent | Rule |
|---|---|---|
| Commander / Marshal | Codex GPT-6.1-Sol (xhigh) or Claude Opus | Decomposes, writes the skeleton, builds the hard core, integrates. Highest reasoning effort. |
| General (depth 2) | Claude Opus / Sonnet, or Sol | Runs a depth-1 team. Has bounded repair authority (can edit to fix integration), not management-only. |
| Scout / planner | Antigravity Gemini Flash, up to 8–16, low reasoning effort | Reads code, maps interfaces, runs the reference, reports. Never writes product code. |
| Builder — design work | Sol / Opus / Sonnet, ≤4 per lead | Anything where the spec is not fully given. |
| Builder — fill-in work | Gemini Flash, ≤4 per lead | Only when the spec ships file layout + stubs/signatures + tests to pass. |
| Polisher | Gemini Flash | Repairs/format after a strong model's draft. |
| Reviewer | ≥ builder tier, executes tests/app, ≤4 | Writes or uses tests the builder did not write. Approval = done. |
| Acceptance-criteria author | Sol / Opus / Sonnet | Writes the rubric + tests before dispatch. |
| Grader | Gemini Flash | Scores outputs against written criteria. |
| Sole integrator | Commander (or one strong dedicated seat) | Merges, checks cross-worker interfaces, bounded repair. |
| Authorization gate | Deterministic hook, not an agent | Every consequential tool call checked against the original user policy. |

OpenCode's default model is placed only after calibration.

## 4. Operating rules

1. Delegate planning/exploration first; commander builds and verifies the core itself (Samway: same reward as full delegation at half the cost).
2. Partition ownership by cohesion (module), not per file; write an interface contract file before dispatch (Co-Coder: +14.0 pts, 0.65× cost).
3. Barrier waits: the lead acts only after all reports for a wave are in (Samway: −6 pts otherwise).
4. No worker-to-worker messaging (Samway −4.4 to −7.1; Co-Coder self-organized teams worst).
5. Original user boundaries are copied verbatim into every spec at every level and enforced at call time (MasDrift: 88.2% of losses at first handoff).
6. Completion = reviewer approval with execution evidence; interface checks at integration (AsynCodeBench: 26/190 green-test runs resolved zero dependencies).
7. Guards: halt on 5+ identical repeated commands; per-task time/token cap; remediation feedback ≤20 lines (SPOQ).
8. One seat owns termination; explicit stop conditions in every spec (MAST: 12.4% of failures).
9. Structured state handoffs (ledger, status records), not raw transcripts (Żywot: −43% tokens).
10. Width caps: builders and reviewers ≤4 per lead; scouts may go wider.

## 5. Eval suite (validates the above before v1)

Tasks: 6–10 real tasks from the user's repos (BlogBERT, SellIt, FYP), 3 reps each, budget-matched.
Metrics: tests pass, interface/dependency checks, reviewer rejections, unauthorized actions, tokens/$,
wall-clock, MAST failure tags.

Experiments, in priority order:
1. Depth 0 vs 1 vs 2 at equal budget.
2. Workhorse calibration: builders {Flash, Sonnet, Sol} × spec level {goal, prose plan, skeleton+tests}.
3. General: Sonnet vs Opus vs Sol leading the same depth-1 team.
4. Reviewer tier sweep (Sonnet reviewing Flash vs reviewing Sol work).
5. Scout width 2/4/8/16 with Flash.
6. Authorization drift per depth with and without the source gate.

## 6. Rollout

1. DOCTRINE.md v0 from this draft (after review).
2. Run experiments 1–2 first (they decide depth and workhorse); revise doctrine.
3. Write the skill pack from the revised doctrine.
4. Run 3–6; publish v1 with an evidence table.

## 7. Known weaknesses of this draft

- Repo-level coding evidence is mostly preprints (grade B); A-grade papers use short benchmarks.
- No paper tests depth 2 vs 1 on coding at equal budget.
- Model tiers in papers (Luna, Nano, 4o-mini, Qwen) may not match Gemini 3.8 Flash or Sonnet 5.5.
- The user's own 31 Orca runs are not yet mined as evidence.
- Eval suite cost: 10 tasks × 3 reps × several configs is expensive in tokens and quota.
