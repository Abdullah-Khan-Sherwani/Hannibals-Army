# R2 — operations and cost realist, project-build scope

`ledger` = %TEMP%\blogbert2-completion-20261008\ledger.md (L=line, read today); `run-list` =
`orca orchestration run-list --json`, 2026-10-15; counts mine, INFERENCE. Paths repo-relative.

## 1. What changed

Scope kills my r1 eval sizing: the user's one project-scale datum, a major update, ran ~4 days
(started 2026-10-07T20:45:05Z, `run-list`; accepted L302), with four quota stalls (L34–36, L75, L176, L276)
and ≥5 leadership rotations (L68–69, L98–102, L150–157, L267–276). No affordable run-matrix exists;
re-sized below. Evidence shifts: issue-scale work (Kim's 20-task coding cells;
SWE-bench papers) transfers weakly (proposal-draft.md:9–10); primary is ProgramBench
(notes/2610.17471.md:9), Co-Coder's 2,371-LOC projects (notes/2606.00953.md:9), SPOQ epics
(notes/2606.03115.md:24), Commit0, and the user's sprints. Capacity/rotation/lifecycle bound the only
in-scope run: ops-first, not depth-first.

## 2. Concessions

- **Skeptic:** adopt all four corrections — MasDrift's Source check is an authorization *agent*, not a
  deterministic hook (txt/2608.07556.txt:325–334; r1-skeptic.md:15), so the draft's "deterministic gate"
  cannot cite it; the messaging penalty is Luna-only; all-Sol L2 hid 37.0% constraint loss; weak builder +
  frontier review 52.6% < strong builder alone 72.2% (notes/2607.06065.md Table 2). His default fails (§3).
- **Defender:** his quota-spread point is the board's strongest empirical claim, strengthened by scope: one
  update pushed Claude weekly to 87% and Gemini to 77–100% (L213, L276); all six Gemini seats died together
  twice (L34, L75; L36 "no other approved Gemini route exposed"). Per-seat second provider + headroom gate is
  first-class. His width logic holds: ≤4 builders + ≤2 reviewers per lead (depth-and-seats.md:98), so more
  demand implies a second lead, not wider fan-out.
- **Lead:** "long work forces handoffs anyway" (r1-lead.md:16) is decisive: solo over four days is itself a
  rotating thread; Kim never tested rotation. Verified: b869523 was a sole-integrator
  cherry-pick (L243); cross-vendor routing did not rescue the stall (L36). In-scope papers favor delegation:
  Co-Coder +14.0 pts, 0.65× cost (notes/2606.00953.md:20); SPOQ 17 repos/1,822 tasks, 12-component wave
  at 5.3× (notes/2606.03115.md:21–24); caveat 2.4k LOC.

## 3. Rebuttals

- **Defender: Flash as primary builder.** In-scope: η_I = −12.0 (notes/2610.17471.md:25). Sprint:
  Gemini-authored branches cycled BLOCKs — C1 reclaim theft and duplicate-slug errors (L30), C2 deleted its
  concurrency test (L244); final acceptance found a missing wiring path (L293). Flash stays
  scout/grader/polish/fill-in.
- **Defender: "$120 total, within allowances" (r1-defender.md:55–57).** API dollars were $0 (L54, L303);
  quota-minutes and interventions bind; one update exhausted several weekly caps. Dollars are fake
  precision.
- **Defender: no repair authority anywhere.** Both fail: bounded-repair managers beat read-only/no-manager
  (depth-and-seats.md:103), but repair is a write; keep it at the sole integrator, merge boundaries only,
  generals review-only mid-wave. Test, don't legislate.
- **Skeptic: depth-0 default and the 36-run pilot (r1-skeptic.md:38, 49).** All in-scope work clears SPOQ's
  5-task/4-hour gate by construction (notes/2606.03115.md:32); project-scale papers favor delegation, so
  depth 0 is a control arm, not a default. His pilot lacks parallel-builder and depth-2 arms
  and is unfundable at scope.
- **Draft: §5's ~690–750 team-runs and §2's depth-0 row.** Rejected: full builds take days;
  depth-0-vs-1 "at equal budget" is ill-defined when depth 0 rotates internally.

## 4. Recommended plan

**Depth.** Depth 1 default — scope clears SPOQ's threshold; the live question is lean (0–1 builder) vs
wide (≤4 cohesion builders). Depth 2 probationary: ≥2 depth-1-sized sub-projects;
planned rotation budget; ≥2× headroom, second provider per seat; frontier generals. Depth 3 never
(MasDrift +0.5 completion / +8.1 UA / 2× tokens, notes/2608.07556.md:24). Depth 0: serial chains only, as
commander+scouts.

**Seats.**

| Seat | Agent |
|---|---|
| Commander/marshal | Sol xhigh or Opus |
| General (D2) | Sonnet or Sol; route/review only |
| Scouts ≤8 / grader / router | Flash (read-only) / script |
| Builders-design ≤4 | Sol/Opus/Sonnet; cohesion partition + interface contract |
| Builder-fill-in ≤3 | Flash; only with layout+signatures+tests |
| Reviewer ≤2 | ≥builder tier, executes |
| Integrator | one seat, bounded repair, sole merger |
| Gate / OpenCode default | script / Stage-3 calibration |

**Rules.** R1 headroom gate + second provider per seat; pause the wave on quota.
R2 launch proof = effective model + observed turn (L7, L20, L210). R3 planned rotation with structured
handover before ~70% context (notes/2606.03115.md:25; −43% tokens, r1-skeptic.md:34). R4 one waiter, all rows
read fully (L117). R5 single writer per branch, integrator-only merge (L144 deviation). R6 wave barriers;
completion = reviewer execution + interface check (depth-and-seats.md:104–105). R7 halt on repeats,
≤20-line remediation, task caps (notes/2606.03115.md:25). R8 quota-minutes ledger per run.

**Staged eval (≤12 team-runs, dual-use).** Cost unit: quota-minutes per accepted sub-project +
interventions/day + rotations/24h.
- S0, 0 runs: mine 33 substantive runs (run-list: 35 − 1 legacy − 1 unbound) + blogbert2-* handovers + ledger;
  preregister rubrics. Gate: <2 in-scope campaigns ⇒ ops rules only, no causal claims.
- S1, 2 runs: one real major update split into two comparable sub-projects; lean vs wide. Gate: suspend the
  builder pack if wide loses on quota-minutes-to-rubric or needs >2 interface-failure cycles.
- S2, 4–6 runs: two more split campaigns (n=3/arm) plus D2 on the campaign that meets triggers; bounded-repair
  test. Gate: kill D2 unless both reps finish with zero rotation-loss at ≤1.5× quota-minutes.
- S3, ≤4 runs (conditional): Flash+skeleton vs Sonnet on real sub-tasks; OpenCode calibration; D2 re-test.
  Gate: no promotion without beating the incumbent on quota-minutes per accepted sub-project.

## 5. Vote

1. **Lead** — right scope reading, ops-first rules, D2 probation; eval fixed here.
2. **Realist** — right architecture, ops-first; pre-scope sizing.
3. **Draft** — best evidence-tagged doctrine, correct §0; unfundable §5, under-weighted ops.
4. **Skeptic** — audit right; depth-0 default and issue-scale pilot out of scope.
