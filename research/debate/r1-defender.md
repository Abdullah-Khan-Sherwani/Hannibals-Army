# Adversarial Review (Round 1): Defender of the Current Army

## 1. Stance
**Defender of the current Army:** Retain Depth-2 multi-vendor hierarchy (Sol marshal -> Sonnet generals [review only] -> Gemini 3.8 Flash soldiers [builders]); reject demoting Flash to fill-in scouts and reject general code-repair authority.

## 2. Top 5 Attacks on the Draft

### 1. Depth-1 Collapses Multi-Vendor Quotas and Halts Production
- **Claim:** Forcing Depth-1 Sol/Sonnet builders concentrates compute on OpenAI/Anthropic, rapidly exhausting weekly quotas while leaving Google Antigravity idle.
- **Evidence:** User logs show vendor limits are the primary bottleneck: in BlogBERT (`orchestration.md#L20-L31`, `ledger.md#07:43 UTC`), Claude weekly quota hit 69% and Codex 19%, while Antigravity ran independently. `SellIt/orca/AGENTS.md#L19-L21` mandates preserving weekly allowances. In `capacity-handover.md#L2`, Gemini quota exhaustion was survived by cross-vendor routing. Running 4 Sol/Sonnet builders per lead (draft §3) burns weekly allowances in hours [INFERENCE].
- **What to change:** Retain Depth 2 for sprints to spread quota across OpenAI (Sol), Anthropic (Sonnet), and Google (Gemini 3.8 Flash).

### 2. Demoting Gemini 3.8 Flash Based on Samway's Luna Is Methodologically Flawed
- **Claim:** Demoting Gemini Flash based on negative implementation efficiency ($\eta_I = -12.0$) conflates GPT-5.6-Luna ($0.05/M) on black-box reverse engineering with Gemini 3.8 Flash on structured tasks.
- **Evidence:** Samway (note `2610.17471.md#L25,L44`; txt `2610.17471.txt#L493-495`) tested ProgramBench (zero code). On Commit0-Lite (skeleton provided), implementation became "the most effective stage for delegation" (+0.10 lift). Gandhi (note `2505.20182.md#L25-L26`) showed plans boost weak implementers +91% (15.3% -> 29.3%), and "Strong LM First" closed 75–95% of the gap. In user runs (`review-c2-sonnet-20261011.md`, `review-backlink-prereq-sonnet-20261011.md`), Gemini Flash soldiers implemented atomic transactions, row locking, and pipeline fixes verified by Sonnet.
- **What to change:** Restore Gemini 3.8 Flash as the primary builder for modular tasks with test criteria; reserve Sol/Sonnet for ambiguous core design.

### 3. Granting Generals "Bounded Repair Authority" Destroys Review Integrity
- **Claim:** Granting Sonnet generals code-repair authority destroys review independence and introduces regressions.
- **Evidence:** In BlogBERT (`review-phase1-sonnet-20261011.md`), commit `b869523` (general repair) broke 5 test mocks across `orchestrate.py` and `approve_post`. User doctrine strictly forbids general edits: `common-brief.md#L3`, `discovery-general.md#L1`, and `safety-general.md#L1` mandate "management/review ONLY... Delegate to visible Orca Antigravity gemini-3.8-flash-high soldiers." SWE-Review (note `2607.06065.md`; depth-and-seats §6) found 62% of false approvals involved tests written by the same agent. AsynCodeBench (note `2609.32662.md#L10,L35`) tested manager repair only on homogeneous models.
- **What to change:** Strip repair authority from generals. Keep generals read-only; require all fixes to be delegated to soldiers with failing tests.

### 4. Depth-1 Root Overflows Context in Complex Multi-Module Repositories
- **Claim:** A Depth-1 root supervising 8–16 workers suffers context blowout, attention dilution, and coordination locks.
- **Evidence:** In `ledger.md#07:43 UTC`, a Sonnet general consumed 41k output tokens in 48 minutes managing one sub-team, requiring handover (`capacity-handover.md#L1`) and child Run rebinding. BlogBERT tracked 22 worker rows across 5 worktrees (`bw-spend`, `bw-controls`, etc.). Under Depth 1, one Sol root managing 22 dispatches stalls from attention degradation (Kim et al., note `2512.08296.md#L29`; Samway note `2610.17471.md#L30`). Depth 2 insulates the marshal: Sonnet generals absorb noise and emit compact summaries (Żywot, note `2601.11327.md`: -43% tokens).
- **What to change:** Mandate Depth 2 whenever a project has $\ge 2$ sub-domains (e.g., Discovery vs. Safety) or $\ge 4$ concurrent workers.

### 5. Misapplying MasDrift's Nano Drift to Frontier Sonnet Generals
- **Claim:** Rejection of Depth 2 relies on MasDrift's unauthorized actions (+9.0 UA mean, 32.0% in Sol–Nano), caused by weak GPT-5.4 Nano supervisors, not Claude Sonnet.
- **Evidence:** In MasDrift (note `2608.07556.md#L26`; txt `2608.07556.txt#Table 3`), homogeneous Sol at Depth 2 had 100.0% completion with 1.5% UA; 32.0% UA occurred only with GPT-5.4 Nano in supervisor and worker seats. The user's generals are Claude Sonnet. Furthermore, MasDrift showed Source checks cut constraint loss from 44.69% to 1.06% (`2608.07556.md#L27`), which the user implements by copying `common-brief.md` boundaries verbatim into every soldier dispatch (`common-brief.md#L5-L14`).
- **What to change:** Decouple authorization preservation from hierarchy depth. Enforce deterministic policy gates while retaining Depth 2 for organizational structure.

## 3. Alternative Plan: Multi-Vendor Depth-2 Army

### Depth Policy
- **Depth 0:** Sequential tasks < 2 files [INFERENCE].
- **Depth 1:** Single-module tasks with 2–3 files in one quota pool [INFERENCE].
- **Depth 2 (Default for Sprints):** Projects with $\ge 2$ sub-domains or $\ge 4$ workers, balancing OpenAI, Anthropic, and Google quotas.
- **Depth 3+:** Never (MasDrift: +0.5 completion for +8.1 UA and 2× tokens).

### Seat -> Agent Allocation
- **Marshal (GPT-6.1-Sol xhigh):** Architecture, multi-general routing, root ledger [INFERENCE].
- **General (Claude Sonnet 4.6):** Sub-team orchestration, spec authoring, diff/test review ONLY.
- **Soldier (Gemini 3.8 Flash High):** Implementation, unit tests, refactoring in disjoint worktrees.
- **Integrator (Gemini Soldier under Sonnet review):** Merges worktrees, candidate gates, dependency checks.
- **Reviewer (Claude Sonnet independent):** Executes live tests, diff audit, security/spend verification.
- **Gatekeeper (Deterministic Hook):** Blocks forbidden branches (`main`), secrets, and paid APIs.

### Rules & Mitigations
- **Remove:** General repair authority; builder restriction to frontier models.
- **Add:** Multi-vendor quota checks (`orchestration.md#L20`); child Run rotation at 40k tokens (`ledger.md#07:43 UTC`).
- **Mitigate Failures:** (1) Quota cliffs (`capacity-handover.md#L2`): canary calls; (2) Shell hangs (`common-brief.md#L9`): `.venv` paths; (3) Mock breakages (`review-phase1-sonnet-20261011.md`): isolate fixes to soldiers.

### Eval Plan & Cost
- **Benchmark:** 4 tasks from BlogBERT/SellIt (2 reps = 16 runs): Current Army (Sol -> Sonnet review -> Flash build) vs. Draft Army (Sol -> Sonnet build/repair).
- **Metrics:** Wall-clock time, quota headroom (% allowance remaining), dollar cost, test pass rate.
- **Cost:** ~$120 total; within allowances [INFERENCE].

## 4. What Evidence Would Change My Mind
1. Budget-matched repo trials showing Depth-1 Sol/Sonnet builders finish 5+ concurrent tasks faster without exhausting weekly quotas.
2. Empirical proof that Gemini 3.8 Flash exhibits $\eta_I < 0$ given disjoint files and failing tests (Commit0 condition).
3. Evidence that general repair achieves fewer regressions than review plus soldier remediation.

## 5. Verdict
**Adopt with changes.** Adopt deterministic gates, barrier waits, and cohesion partitioning, but reject demoting Gemini Flash, abandoning Depth 2, and granting repair authority to generals. Under real vendor rate limits and context bounds, the user's multi-vendor Depth-2 hierarchy is an optimal, battle-tested production architecture.
