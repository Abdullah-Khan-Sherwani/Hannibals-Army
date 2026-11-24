# Hannibal's Army — proposal v1 (after adversarial review)

Date: 2026-10-15. Scope (user): **full systems from scratch and major updates; not small tasks.**
Inputs: `research/depth-and-seats.md` (22 papers), `research/proposal-draft.md` (v0), and two debate rounds in
`research/debate/` (skeptic = Codex Sol, defender = Antigravity Gemini, realist = OpenCode, lead = Claude).
INFERENCE marks design calls not directly measured.

---

## 1. Recommendation in one paragraph

Adopt **Plan A: a lean depth-1 army with a probationary "campaign mode" (depth 2)**. One strong commander owns
architecture, interface contracts, the hard core and integration; read-only scouts explore in parallel; up to
four builders work on cohesion-partitioned modules; one independent reviewer executes tests. Depth 2 is used only
for campaigns with ≥2 depth-1-sized sub-projects, and stays on probation until it completes cleanly under the
operating rules. Ship the operating rules first (they address the failures that actually stopped the user's last
sprint), then validate with ≤12 runs that double as real project work.

**Vote:** all three panelists ranked the plans identically — **1. Lead, 2. Realist, 3. Draft, 4. Skeptic R1** —
including the skeptic and the defender, who each ranked another plan above their own. Plan A is the lead plan with the
realist's operations and eval folded in.

---

## 2. What the panel converged on (no remaining dissent)

| # | Point | Basis |
|---|---|---|
| C1 | **Depth 1 is the default for this scope.** The skeptic withdrew solo-by-default; the defender withdrew depth-2-by-default. | Co-Coder project generation +14.0 pts, 0.65× cost; Samway ProgramBench; Commit0; "long work forces handoffs anyway" (a 4-day solo agent rotates into itself) |
| C2 | **Depth 3 never.** | MasDrift: +0.5 completion, +8.1 pts unauthorized actions, ~2× tokens |
| C3 | **Strong commander** (Sol xhigh or Opus). | Samway lead ceiling (+20.9 / +15.4%); MasDrift: decomposer predicts constraint loss |
| C4 | **Flash does not design.** Flash is fine for scouts, graders, polish; building only on fill-in work with layout + signatures + tests. | Samway η_I = −12.0 when spec must be discovered; Commit0 skeleton result (directional); sprint: Flash branches S1 BLOCK B1–B4, C1 4 defects, C2 deleted its concurrency test (ledger L244), FR6.4 wiring gap at acceptance (L293) |
| C5 | **Review doesn't rescue weak building.** Weak builder + frontier reviewer 52.6% < strong builder alone 72.2%. | SWE-Review Table 2 |
| C6 | **Every seat needs a named second provider and a quota headroom check before launch.** | Sprint: all six Gemini seats died together twice (ledger L34, L75); "No other Gemini route exposed… No bypass used" (capacity-handover); Claude weekly 87%, Gemini 77–100% after one update (L213, L276) |
| C7 | **Planned rotation with structured handover** before ~70% context / ~40k output tokens for supervisors. | Safety general rotated at 48 min / 41k output (L98); ≥5 leadership rotations in one update; Żywot −43% tokens with structured state |
| C8 | **Launch proof = effective model + observed turn start**, not "input accepted". | Ledger L7, L20, L26, L210 |
| C9 | **Single writer per branch; integrator-only merge; ownership transfer receipts.** | Ledger L144 deviation; capacity-handover L12 |
| C10 | **Completion = independent executing review + interface check**, not green tests alone. | AsynCodeBench 26/190; Agentless; SWE-Review 62% |
| C11 | **Runaway guards:** halt on 5+ repeated commands, ≤20-line remediation, per-task caps. | SPOQ; MAST step repetition 15.7% |
| C12 | **The draft's eval (~750 runs) is dead.** Cost unit = quota-minutes + human interventions + rotations, not dollars (API spend was $0, L54, L303). | Realist r1/r2 |
| C13 | **Authorization is not a solved deterministic gate.** MasDrift's Source check is an LLM authorization agent; all-Sol depth 2 still lost 37.0% of constraints. | MasDrift txt 325–334, Table 3 |

---

## 3. Disputes that remained, and the ruling

### D1. May generals or integrators repair code?
- **Defender:** never; generals read-only, fixes go back to builders with failing tests (user doctrine: `safety-general.md:1`).
- **Lead / AsynCodeBench:** a manager with bounded repair beat read-only and no manager.
- **Realist + skeptic compromise:** repair only at the **sole integrator, at merge boundaries**; generals review/route
  mid-wave; any other repair requires an ownership transfer and a second reviewer.
- **New evidence (lead check):** the only in-scope repair-type breakage — cherry-pick b869523, which broke 5 tests —
  was done by the **sole integrator running "Luna high"** (ledger L243; review-phase1-sonnet L11–21). The problem
  there was a cheap model in a write seat, not repair authority as such.
- **Ruling:** adopt the compromise. **Generals are review/route only. The integrator may repair at merge boundaries,
  and the integrator must be a strong model.** Bounded repair by generals is tested in S2, not legislated.

### D2. How much building does Flash get?
- **Defender:** primary builder for modular work with tests. **Realist/skeptic:** fill-in only, ≤3, calibrate first.
- **Ruling:** fill-in only (layout + signatures + tests in the spec), ≤3 per lead, until S3 calibration. The
  defender's strongest point (vendor spread) is met by C6, not by giving Flash design work.

### D3. Wave barriers vs dependency release
- **Realist:** wave barriers. **Skeptic:** release downstream tasks when their dependencies finish (Co-Coder).
- **Ruling:** both. A lead waits for **every report it consumes** before integrating or declaring done (Samway −6
  pts otherwise); unrelated tasks are released on dependency completion, not held for the whole wave.

### D4. Depth-2 trigger
- **Defender:** ≥2 sub-domains or ≥4 concurrent workers, root context >40k. **Realist/skeptic:** ≥2 depth-1-sized
  sub-projects, stable contracts, rotation budget, ≥2× headroom, frontier generals, measured root blockage.
- **Ruling:** the stricter trigger. "≥4 workers" alone is width, handled by a second depth-1 lead or by waiting, not
  by adding a management layer.

### D5. Which eval?
- **Skeptic r2:** ≤28 screening runs. **Realist r2:** ≤12 dual-use runs. **Defender r2:** 16 + 36.
- **Ruling:** realist's ≤12 dual-use runs (each run is a real project you need anyway) with the skeptic's
  promotion gate (§7).

---

## 4. The three plans, for your decision

### Plan A — Lean depth 1 + probationary campaign mode (recommended)
- Commander builds core and integrates; scouts read; ≤4 builders on cohesion modules; 1 executing reviewer.
- Depth 2 only under the D4 trigger, on probation.
- **For:** best fit to the project-scale evidence; preserves your army for big campaigns; unanimous #1.
- **Against:** the commander seat (Sol/Opus) carries the most load and the most quota; depth 2 is not yet trusted.

### Plan B — Campaign-first army (defender's r2 position)
- Depth 1 for 2–5-module builds; depth 2 "campaign mode" for any multi-subsystem build; Sonnet generals read-only;
  Flash fill-in builders up to 4; Gemini steward as depth-2 integrator.
- **For:** closest to what you already run; best vendor spread; generals absorb coordination noise from the marshal.
- **Against:** puts a cheap model in the integrator seat (the b869523 pattern); depth 2 runs more often without
  evidence it beats depth 1; ~2.4× tokens and more rotations when it does.

### Plan C — Minimal strong team (skeptic's r2 position)
- Sol owner/integrator; 2 Flash scouts; 2 builders (Sonnet/Sol), max 4; one Opus/Sol reviewer; ≤2 experimental
  generals only after shallow delegation proves itself.
- **For:** fewest seats, least coordination failure surface, cleanest experiment baseline.
- **Against:** concentrates quota on OpenAI/Anthropic (the defender's main warning); slow on large separable builds.

**Choose A by default; B if the campaign is clearly multi-subsystem and quota spread matters most; C as the
control arm in evaluation.**

---

## 5. Plan A seat table

| Seat | Primary | Backup (calibrate before use) | Rule |
|---|---|---|---|
| Commander / Marshal | Codex GPT-6.1-Sol xhigh | Claude Opus | Architecture, interface contract, skeleton, hard core, sole integration |
| General (depth 2 only) | Claude Opus or Sonnet | Sol | Route + review only; ≤2 generals |
| Scout | Antigravity Gemini Flash, ≤8 | Sonnet | Read-only; reports to lead |
| Builder — design | Sol / Opus / Sonnet, ≤4 per lead | — | Owned module, contract, tests |
| Builder — fill-in | Gemini Flash, ≤3 per lead | Sonnet | Spec must ship layout + signatures + tests |
| Reviewer | ≥ builder tier, executes; ≤2 | Sol / Opus | Uses tests the builder didn't write |
| Integrator | the Commander, or one strong seat | Opus | Sole merger; may repair at merge boundaries only |
| Grader / router / status | script, else Flash | — | No new LLM seat if a script works |
| Authorization | environment controls: withheld credentials, branch protection, allowlists, fakes | transcript audit | Boundaries copied verbatim into every spec; residual semantic risk audited, not assumed solved |
| OpenCode default | unplaced | — | Identify effective model, calibrate in S3 |

---

## 6. Operating rules (ship first)

1. **R1 Capacity gate:** check `orca account list` rate limits before every wave; ≥2 providers across seats; pause the wave on quota rather than rerouting blindly.
2. **R2 Launch proof:** a worker counts as running only with effective model + observed turn start.
3. **R3 Planned rotation:** supervisors hand over with a structured record before ~70% context / ~40k output tokens.
4. **R4 One waiter, read every row:** one process waits on the inbox; every message is fully read and acked.
5. **R5 Single writer:** one writer per branch, integrator-only merge, ownership-transfer receipts.
6. **R6 Reports before integration:** the lead consumes all reports it depends on before integrating; independent tasks release on dependency completion.
7. **R7 Done = verified:** independent executing review + cross-module interface check.
8. **R8 Guards:** halt on 5+ identical repeated commands; per-task time/token caps; remediation feedback ≤20 lines.
9. **R9 Quota ledger:** record per run: provider allowance before/after, rotations, interventions.
10. **R10 Contracts before dispatch:** cohesion partition + interface contract file; no worker-to-worker messaging.

---

## 7. Validation plan (≤12 runs, each a real project)

| Stage | Runs | What | Kill / promote gate |
|---|---|---|---|
| S0 | 0 | Mine the 33 substantive Orca runs + BlogBERT ledger/handovers; count stalls, rotations, review BLOCKs, interventions; preregister rubrics | <2 in-scope campaigns found ⇒ ship ops rules only, no causal claims |
| S1 | 2 | One real major update split into two comparable sub-projects: lean (0–1 builder) vs wide (≤4 builders) | Suspend the builder pack if wide loses on quota-minutes per accepted sub-project or needs >2 interface-failure cycles |
| S2 | 4–6 | Two more campaigns (n=3 per arm) + depth 2 on a campaign meeting D4; bounded-repair test for generals | Kill depth 2 unless both reps finish with zero rotation loss at ≤1.5× quota-minutes |
| S3 | ≤4 | Flash + skeleton vs Sonnet builders on real sub-tasks; OpenCode calibration | No promotion without beating the incumbent |

**Promotion gate (all stages):** same acceptance checks, no critical regression or boundary violation, and ≥20%
lower quota-minutes or elapsed time without more human intervention. Small samples screen; they don't prove.

---

## 8. Fact-check log from the debate

- **Defender r1:** "b869523 (general repair)" — unsupported; it was the sole integrator's cherry-pick (L243).
  "Quota stall survived by cross-vendor routing" — contradicted (capacity-handover: no bypass, work stalled).
- **Defender r2:** "MasDrift Table 3 82.9% → 83.4%" — these numbers do not appear in the paper; the homogeneous
  means are 98.1% → 98.6%. The +0.5 conclusion stands, the cited figures don't.
- **Lead synthesis:** MasDrift's Source check is an authorization agent, not deterministic (skeptic); the
  messaging penalty was Luna-only (skeptic); "all-Sol depth 2 was fine" omitted 37.0% constraint loss (skeptic).
- **Realist:** "31 runs" is 33 substantive (35 rows − 1 legacy − 1 unbound).
- **New finding:** the BlogBERT sole integrator ran on "Luna high" (ledger L243), a cheap model in the most
  write-critical seat.

---

## 9. Decisions needed from you

1. Plan A, B, or C (or A with changes)?
2. Which real major update or greenfield build should be the S1 campaign?
3. Commit `research/` (notes, synthesis, debate, proposal) as you, with no AI co-author line?
4. Rewrite the first commit `44ac66c` to remove its `Co-Authored-By: Claude` line and force-push?
