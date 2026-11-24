# R1 — lead position (Claude), written after reading r1-skeptic and r1-realist

## 1. Stance

A lean depth-1 army is the default for full-system builds and major updates; depth 2 is a probation
config for multi-sub-project campaigns. Scope (user): full systems from scratch and major updates only.

## 2. Responses to round 1

- **Skeptic's solo evidence is issue-scale and noisy.** Kim's coding cells (SWE-bench 48.8 vs 47.5) are
  20 tasks with ~±20-pt CIs (2512.08296 note, Validity), single-issue fixes, shared filesystem, homogeneous
  seats. Out of scope for full builds. Project-scale evidence points the other way: Co-Coder on
  CodeProjectEval (project generation) +14.0 pts at 0.48× latency and 0.65× cost vs sequential solo
  (2606.00953 note); Samway ProgramBench (whole-program reconstruction) teams beat solo; Commit0
  (library from skeleton) makes implementation the best stage to delegate (2610.17471 txt 2269–2285).
- **Long work forces handoffs anyway.** A multi-day build exceeds any context; a "solo" agent rotates
  into fresh instances of itself via self-summaries. The question is handoff structure, not solo vs team.
- **Read-only delegation is compatible with Cognition's single-writer objection.** Scouts don't write,
  so they can't make conflicting decisions. Samway: planning-only delegation (lead writes and verifies
  all code) matched full delegation at half the cost.
- **Independent verification needs a second agent.** 62% of false approvals involved the builder's own
  tests (2607.06065 note). Skeptic's own plan keeps one reviewer.
- **Skeptic's corrections accepted:** MasDrift's Source check is an authorization *agent*, not purely
  deterministic; the messaging penalty was measured on Luna only; all-Sol L2 hid 37.0% constraint loss;
  weak builder + frontier review (52.6%) < strong builder alone (72.2%).
- **Realist's points accepted:** eval as drafted is unfundable/underpowered; doctrine must include the
  ledger's real failure modes (quota, rotation, launch receipts, single-writer violations); every seat
  needs a second provider; "budget" must be in quota-minutes and human interventions.

## 2b. Lead fact-check of r1-defender (checked against the user's docs)

- **Confirmed:** the Safety general hit 48 min / 41k output tokens and was rotated
  (`%TEMP%\blogbert2-completion-20261008\ledger.md` line 98).
- **Not supported:** "commit b869523 (general repair) broke 5 test mocks". The review file
  (`review-phase1-sonnet-20261011.md` lines 11–21) says b869523 is a later commit outside the reviewed set
  that broke 5 tests; it does **not** say a general authored it. No evidence found that generals made repairs.
- **Contradicted:** "Gemini quota exhaustion was survived by cross-vendor routing". `capacity-handover.md`
  says quota was reached on **all** active soldiers, "No other Gemini route exposed… No bypass used", and
  lists work stalled (steward retry "hit quota before any edit").
- **Relevant to the Flash-builder question, same file:** Flash-built branches S1 (bw-spend) got
  "Independent review BLOCK B1–B4", and C1 (bw-controls) "4 defects + root lease amendment". These are
  data points, not a rate; the realist's Stage 0 mining should count them.

## 3. Lead's plan

- **Default (depth 1, lean):** one strong lead (Sol/Opus) owns architecture, skeleton, interface contract,
  hard core, integration. Read-only scouts in parallel. One independent strong reviewer that executes tests.
- **Parallel builders:** only on cohesion-partitioned modules with owned files + interface contract +
  stubs + tests; ≤4; strong/mid by default, Flash only after calibration on skeleton work.
- **Depth 2 (probation):** only for campaigns with ≥2 sub-projects each depth-1-sized, frontier generals,
  rotation budget, provider headroom. Promoted only after completing cleanly under the realist's rules.
- **Eval:** realist's staged plan (mine existing runs first, then small pilots with kill gates), but the
  pilot tasks must be full builds / major updates, and must include a parallel-builder arm on a large
  multi-module task, or the design can only show solo winning.
