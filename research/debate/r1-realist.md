# r1 — operations and cost realist (attack on proposal draft v0)

Citations: `ledger` = %TEMP%\blogbert2-completion-20261008\ledger.md (L=line); `orchestration.md` = BlogBERT\encantado\docs\orchestration.md. INFERENCE = my reasoning.

## 1. Stance

The doctrine's content mostly survives; its eval plan is unfundable and underpowered, and it omits the failure modes that actually killed the user's runs — quota, rotation, lifecycle.

## 2. Top 5 attacks (ranked)

### A1. The eval suite cannot resolve the effects it targets and would burn months of quota.

Draft §5 ≈25 arms × 10 tasks × 3 reps ≈ **750 team-runs** (each spawning 2–16 workers). Power: detecting a 15-pt completion gap at 80% power, α=.05 needs ~167 tasks/arm (INFERENCE; n≈8·(p1(1−p1)+p2(1−p2))/Δ²); Kim's coding cells used 20 tasks and still produced "CIs typically ±20 points" (2512.08296 note, Validity). Every effect justifying a rule is 3–9 pts: MasDrift +4.2 completion / +9.0 unauthorized (2608.07556 note), Samway width +3.2→+7.1 (2610.17471 note). Three reps on ten tasks cannot separate these from noise. Quota reality: the user's one real depth-2 project (BlogBERT sprint) took 4 days, stalled when "Individual quota reached" stopped all six Gemini terminals (ledger L34, L75), and hit weekly caps on Antigravity and Claude (L213, L276). 750 runs is months at that cadence. **Change:** staged eval with kill criteria, starting with $0 mining of existing runs — `run-list` today shows 35 rows, 33 substantive (1 legacy, 1 unbound), not "31".

### A2. The doctrine ignores the failures the ledger actually shows.

Recurring killers: provider quota exhaustion (L34, L75); context rotation where both generals failed to emit worker_done (L19, L25); launch receipts "input accepted/turn unobserved" (L7, L26); lifecycle deviations — a worker merging outside the sole-integrator rule (L144), retries refused by settled-task states (L18); head-truncated delivery reads (L117). The draft (§1) waves these away: "Orca already provides runs, dispatch, inbox". **Change:** add the §3 rules; without them the doctrine is a theory the user's stack has disproven.

### A3. Four seats on one vendor's quota re-creates the single point of failure.

Draft §3 puts Gemini Flash in four of eleven seats (scout, fill-in builder, polisher, grader). The sprint died there: individual quota stopped all Gemini workers simultaneously (L34, L75); the user then ordered reducing Gemini pressure before exhaustion (L73). **Change:** every seat needs a named second provider; launch only after a headroom check (`orca account list` rateLimits — also the user's own rule, orchestration.md §Setup 2). Measure quota-minutes, not dollars.

### A4. Depth-2 triggers are unverifiable, and depth 2's real cost is supervision.

"Root context would overflow" and "~2.4× tokens" (§2) need per-run context/capacity data nobody collects. The depth-2 sprint's actual cost: repeated rotations, a 313-line management ledger for one project, days of slippage. The draft also gives generals edit authority ("bounded repair", §3) while the user's operative rule is soldier-owned code (ledger L59; orchestration.md §Acceptance). **Change:** depth 2 only with a rotation budget and quota proof; keep single-writer discipline; test bounded repair, don't legislate it.

### A5. "Equal budget" is undefined, and the authorization gate may not exist in Orca.

MasDrift itself was "not token/call matched" (2608.07556 note, Validity); in a subscription stack the binding currencies are quota-minutes and human interventions, not dollars. "Deterministic hook" on every consequential tool call (§3) presumes an Orca per-call hook; the ledger achieved zero paid calls via fakes/fixtures and withheld credentials (L54; common-brief.md), not call-time gates. **Change:** define cost units first; verify hook feasibility; otherwise substitute env-level denial + allowlists + transcript audit.

## 3. Alternative plan

**Depth policy.** Depth 1 default. Depth 2 only when: (a) ≥2 sub-projects each meeting SPOQ's "5+ parallelizable tasks spanning 4+ hours" (txt 2606.03115 L1573); (b) a rotation budget exists — 2 generals, each expected to rotate once via structured handover; (c) ≥2× provider headroom; (d) marshal and generals frontier. Never depth 3.

**Seat→agent.** Marshal ×1 (Sol xhigh / Opus). Generals ≤2 (Sonnet), review/route only by default. Scouts ≤4–8 (Flash, read-only). Builders: Sonnet default; Flash only with skeleton+tests, ≤3, provider headroom ≥30%. Reviewer: Sonnet executing tests (Flash work), ≥builder tier otherwise, ≤2. Grader/router/status: script or Flash. Gate: script. Integrator: one seat.

**Rules to add (evidence).** (R1) Capacity gate + ≥2-provider spread (L34/75/213; orchestration.md). (R2) Launch proof = effective model + turnStart observed; accepted ≠ running (orchestration.md §Launch; L26). (R3) Planned rotation before context death, structured handover (SPOQ 70% alerts; Żywot −43% tokens, D2-4; L19/25). (R4) One waiter, ack all, process every row (orchestration.md; L117). (R5) Single writer per branch, ownership-transfer receipt, never force-clean worktrees (L12/144/311). (R6) Runaway guards: 5+ repeated commands halt, per-task cap, ≤20-line remediation (SPOQ note). (R7) Per-run quota ledger (provider, session/weekly before/after).

**Cut from draft §5.** Reviewer-tier sweep (SWE-Review: only +3.0 on the strongest generator); scout-width sweep (Samway swept 2–16; quota says don't); authorization-drift-per-depth sweep (replace with one fixture test).

**Staged eval (vs ~750 runs).** Stage 0: mine 33 runs + ledger — $0 — extract base rates (quota stalls, rotations, launch failures, rejections) and preregister metrics. Stage 1: 16 team-runs (2 tasks × {d1,d2} × 4 reps) — variance, cost, interventions; compute MDE; kill if MDE at ~48 runs >20 pts (fall back to case studies + process metrics). Stage 2: 36 runs (3 sub-project tasks × {d1,d2} × 6 reps); primary outcomes: quota-stall-free completion, interventions/run, wall-clock; secondary: tests, unauthorized actions. Stage 3 (conditional): 24 runs (builder arms × 2 tasks × 4 reps) only if a workhorse question survives. Total ≤76 runs, ≈10× cheaper, with kill gates.

## 4. What would change my mind

≥10× more quota headroom than the ledger implies; a depth-2 run rotation-free and under budget, twice; interventions/run <0.5; an Orca per-call authorization hook.

## 5. Verdict

**Adopt-with-changes.** The synthesis is honest and the core rules — depth-1 default, strongest lead, structured handoffs, verified completion, barrier waits — survive scrutiny (depth-and-seats §1–4; 2610.17471; 2512.08296). But the draft reads like a funded lab program: rewrite §5 into the staged ≤76-run plan, add the seven ledger-mined operational rules, resolve A3–A5, and keep depth 2 probationary until it completes once under the new quota/rotation discipline. Ship ops-first; the evidence table can follow.
