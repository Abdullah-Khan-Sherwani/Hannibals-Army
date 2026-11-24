# Depth and seats: evidence for 1-depth and 2-depth agent armies

Status: v0, 2026-10-15. Built from 22 paper notes in `research/papers/notes/` (template:
`research/papers/TEMPLATE.md`). Key numbers in each note were spot-checked against the
downloaded full text in `research/papers/txt/`; corrections are listed in §8.

Grades: **A** peer-reviewed + controlled · **B** preprint (or workshop) + controlled · **C** case study / weak controls.
Anything marked **INFERENCE** is our design call, not a paper result.

---

## 1. Bottom line

1. **Depth 1 is the default.** Orchestrator → workers is the only depth with controlled,
   repo-level coding evidence (Samway, Co-Coder, AsynCodeBench, SWE-Review, Gandhi).
2. **Depth 2 is unproven for coding.** No paper compares depth 2 against depth 1 at equal budget on
   coding. The one direct depth-1-vs-2 test (MasDrift, B, non-coding) found **+4.2 pts completion
   but +9.0 pts unauthorized actions and ~2.4× worker tokens**. Use depth 2 only when the trigger
   conditions in §4 hold, and with the extra safeguards listed there.
3. **The lead sets the ceiling.** The seat that decomposes and integrates must be the strongest model.
   This is the most consistent placement result across papers.
4. **Cheap models scout; they build only fill-in work.** Cheap models are excellent as planners/explorers,
   routers, formatters and graders. As implementers who must discover the spec they have *negative*
   return; given a skeleton (file layout + stubs/signatures + tests) the harm disappears (directional).
   A prose plan alone recovers only ~40% of the gap to the strong model (§6b).
5. **Verification must be independent, execution-grounded, and at least as strong as what it checks.**

---

## 2. Evidence base

| Paper (arXiv) | Venue / grade | What it actually tests | Coding? |
|---|---|---|---|
| Samway et al. 2610.17471 — teams of coding agents | preprint, **B** | depth-1 lead→workers; role (P/I/V) × model tier (GPT-5.6 Sol/Terra/Luna) × width 2–16; peer messaging | yes, repo-level |
| Kim et al. 2512.08296 — science of scaling agent systems | Nature Mach. Intell. 2026, **A** | single vs independent/centralized/decentralized/hybrid; 3 workers; no depth 2 | partly (20-task SWE/Terminal) |
| Xu et al. 2608.07556 — MasDrift | preprint, **B** | **depth 1/2/3** (binary tree), peers N2/4/8, Sol root + Nano below; authorization drift | no (synthetic productivity) |
| Gandhi et al. 2505.20182 — strong-weak collaboration | EMNLP 2025, **A** | 14 strong/weak pipelines on SWE-bench Lite, cost-equated | yes, repo-level |
| SWE-Review 2607.06065 | preprint, **B** | reviewer in the loop; reviewer strength vs generator strength | yes, repo-level |
| Agentic Rubrics 2601.04171 | preprint, **B** | who authors vs who grades verification artifacts | yes, repo-level |
| Co-Coder 2606.00953 | preprint, **B** | per-file vs cohesion-aware partitioning vs self-organized teams | yes, project-level |
| AsynCodeBench 2609.32662 | preprint, **B** | async protocols; manager with bounded repair vs read-only vs none | yes, small repos |
| MAST 2503.13657 | NeurIPS 2025 D&B, **A** | failure taxonomy over 1,642 traces | mixed |
| Agentless 2407.01489 | FSE 2025, **A** | fixed pipeline + execution-gated selection vs agents | yes |
| Żywot et al. 2601.11327 — small agents vs one large | ICLR 2026 workshop, **B** | orchestrator size vs sub-agent size; where thinking goes | tool QA, not repo |
| Critique-and-routing controller 2605.08686 | preprint, **B** | small critic/router over 1B–30B pool, usage caps | math only |
| Planner-as-Router 2609.32917 | AIxSET 2026 (author-stated), **B−** | plan-time tier routing on a DAG, 54 tasks | DB queries |
| AgentRouter 2609.22951 | unverified venue, **C** | step-level tier routing | mixed, synthetic |
| MasRouter 2502.11133 | ACL 2025, **A** | learned role→LLM routing | short benchmarks |
| Puppeteer 2505.19591 | NeurIPS 2025, **A** | learned orchestrator, reasoning-chain depth/width | short benchmarks |
| MaAS 2502.04180 | ICML 2025, **A** | workflow search, early exit, cost penalty | short benchmarks |
| G-Designer 2410.11782 | ICML 2025, **A** | communication topology; 5/10/20 agents | short benchmarks |
| MAS² 2509.24323 | ICLR 2026, **A** | meta-team generates/repairs target MAS | short benchmarks |
| OrgAgent 2604.01020 | preprint, **B** | company-style governance vs flat peers | QA, not code |
| Agyn 2602.01465 | preprint, **C** | production manager/engineer/reviewer team | yes |
| SPOQ 2606.03115 | preprint, **C+** | wave dispatch, validation gates, field deployment | yes |

Note: the "A" papers mostly test short benchmarks; the repo-level coding evidence is mostly B.
That is the main weakness of this whole base and the reason for the eval suite (§7).

---

## 3. When to use depth 0, 1, or 2

**Depth 0 (one strong agent)** when the task is sequential or tightly coupled:
- Kim (A): centralized teams lost **−50.3%** vs single agent on sequential planning (PlanCraft),
  independent teams **−70.0%**; gains appear only on separable work (Finance **+80.8%**).
- AsynCodeBench (B): the *strongest* single models regress under decomposition (93.6% → 86.7–89.9%).
- Co-Coder (B): near-complete coupling collapses partitioning to one group anyway.
- SPOQ (C+): orchestration overhead pays off only at ≥5 parallelizable tasks / ≥4 hours of work.

**Depth 1** when the work has ≥2 separable parts *and* a strong lead is available. This is the default army.

**Depth 2** only when **all** of these hold (INFERENCE):
1. The work splits into ≥2 sub-projects that are each depth-1-sized on their own (SPOQ threshold, per sub-team).
2. The root's context would otherwise overflow from holding every worker's detail.
3. You can afford roughly **2.4× the worker tokens** (MasDrift Sol L1→L2: 46.6k → 111.3k tokens/run).
4. Every general can be a strong model (see §5).

Never go to depth 3: MasDrift L2→L3 added **+0.5 pts** completion for **+8.1 pts** unauthorized
actions and another ~2× tokens (230.5k).

---

## 4. Depth-1 design (the default army)

```
            Commander (strongest model; decomposes, implements hard core, integrates)
           /        |          \              \
     Scouts ×N   Builders ≤4   Reviewer(s) ≤4   [deterministic gates: tests, authz, schema]
     (cheap)     (strong/mid)  (≥ builder tier, executes code)
```

Rules, each with its source:

| # | Rule | Evidence |
|---|---|---|
| D1-1 | **Delegate planning/exploration first.** Having workers do planning only, while the lead implements and verifies itself, matched full P+I+V delegation at **half the cost** (η_P 3.8 vs η_PIV 1.4). | Samway (B) |
| D1-2 | **Scout width can be large; builder and reviewer width cap at 4.** Planners improved monotonically to 16 workers (+3.2% → +7.1%); implementers and verifiers plateau or drop beyond 4. | Samway (B); Kim (A): curves non-monotonic, Flash centralized peaked near 7 |
| D1-3 | **Barrier waits.** The lead must wait for all reports before acting; async leads under minimal guidance lost ~6 reward points by acting on partial results. | Samway (B) |
| D1-4 | **No peer-to-peer chatter between workers.** Direct messaging cost weaker models **4.4–7.1 pts**, and 84% of messages went back to the lead anyway. Self-organized Claude Code Agent Teams were fastest/cheapest but had the *lowest* pass rate (16.3% vs sequential 20.1%). | Samway (B); Co-Coder (B) |
| D1-5 | **Partition by cohesion, not per file.** Per-file fan-out: +44–60% cost for +0.9–3.2 pts. Cohesion-aware partitioning: **+14.0 pts, 0.48× latency, 0.65× cost**. Shared interface contract written before dispatch. | Co-Coder (B) |
| D1-6 | **Give builders an instance-level plan, not repo summaries.** A strong model's plan lifted a weak implementer **15.3% → 29.3%**; repo summaries/FAQs/few-shot did not help or hurt. | Gandhi (A) |
| D1-7 | **The integrator has bounded repair authority.** Manager with bounded repair beat read-only manager and no manager in most model rows; async workers without a manager were usually worst (−14.9 to −33.3%). | AsynCodeBench (B) |
| D1-8 | **Completion = verified, not self-reported.** Execution-gated selection gave Agentless +6.3 pts; "approved by reviewer" defined done in Agyn; explicit completion signals fixed manager stalls. | Agentless (A); Agyn (C) |
| D1-9 | **Check cross-worker interfaces, not just tests.** 26 of 190 runs had ≥80% green tests with **zero** dependencies resolved. | AsynCodeBench (B) |
| D1-10 | **Guardrails against runaway workers.** Halt on 5+ identical repeated commands, per-task time/budget caps, ≤20-line remediation feedback. | SPOQ (C+); MAST (A): step repetition = 15.7% of failures |
| D1-11 | **Explicit termination conditions owned by one seat.** "Unaware of termination" is 12.4% of failures and appears almost only in failed runs. | MAST (A) |
| D1-12 | **Cheap paths and early exit.** Removing early exit raised cost 1.01 → 1.67 m$/query *and* lowered accuracy. | MaAS (A) |

---

## 5. Depth-2 design (conditional)

```
                       Marshal (strongest model; splits into sub-projects, final integration)
                      /                                  \
        General A (strong; runs a depth-1 team)     General B (strong; runs a depth-1 team)
        scouts / builders ≤4 / reviewer              scouts / builders ≤4 / reviewer
                      \                                  /
            [source-based authorization gate: every tool call checked against the ORIGINAL user policy]
```

Everything in §4 applies inside each general's team. Depth 2 adds:

| # | Rule | Evidence |
|---|---|---|
| D2-1 | **Generals must be strong models.** The lead sets the team ceiling (Luna→Terra lead **+20.9%**, Terra→Sol **+15.4%**; Terra lead + Luna workers trailed solo Sol by 10.3%). A general *is* a depth-1 lead, so the same rule applies to it (INFERENCE). | Samway (B) |
| D2-2 | **A strong root does not protect weaker seats below it.** Sol root + Nano generals/workers: unauthorized actions **32.0%** at L2 vs **1.5%** for all-Sol. What predicts constraint loss is which model leads the decomposition. | MasDrift (B) |
| D2-3 | **Pass the original user boundaries verbatim to every level, and enforce them outside the chain.** **88.2%** of constraint losses happen at the first handoff. "Source" checks (against the original user policy) cost **−1.6 pts** completion; "Chain" checks (each level narrows) cost up to **−36.3 pts**. | MasDrift (B) |
| D2-4 | **Hand off structured state, not raw transcripts.** Structured memory cut token build-up by 43% vs replaying history. | Żywot (B) |
| D2-5 | **Typed QA/compliance workers don't fix drift.** Adding typed QA + compliance seats left unauthorized actions at 12.6% vs 11.7%. Use deterministic gates, not more agents. | MasDrift (B); OrgAgent (B): compliance checker checks structure, not truth |
| D2-6 | **Barrier and integration checkpoint at each level.** Integrate at wave boundaries with a git checkpoint; most dependency closure lands 50–75% of the way through the run, so put an interface check there too. | SPOQ (C+); AsynCodeBench (B) |
| D2-7 | **One coordination point per sub-team.** Generals talk to the marshal, not to each other. | Agyn (C); Samway (B) |

---

## 6. Seat → agent placement

Tiers used in the papers map onto our agents roughly as: **strong** = GPT-6.1-Sol (Codex), Claude Opus;
**mid** = Claude Sonnet; **cheap** = Gemini Flash (Antigravity). OpenCode's default model must be placed
by measurement. No paper tests these exact brands in these seats, so the brand column is **INFERENCE**;
the tier column is the evidence.

| Seat | Tier (evidence) | Our agent (INFERENCE) | Key sources |
|---|---|---|---|
| Commander / Marshal | **strongest**, with high reasoning effort | Codex GPT-6.1-Sol (xhigh) or Claude Opus | Samway lead ceiling; MasDrift decomposition leader; Żywot: orchestrator-only thinking +18.2 GAIA / +36.7 AIME |
| General (depth 2 only) | **strong**; must be able to implement and repair, not management-only | Claude Opus, Sol, or Sonnet (Sonnet is frontier-class; see §6c) | Samway; AsynCodeBench bounded repair |
| Scout / planner / explorer | **cheap**, many (up to 8–16), low reasoning effort | Antigravity Gemini Flash | Samway: Sol lead + Luna planners got 47.5% of the all-Sol gain at 13.9% of the extra cost; 1 Sol lead + 16 Luna planners within 1.4 pts of all-Sol at −70% cost; Żywot: sub-agent size barely mattered for tool executors, sub-agent thinking added 77% latency |
| Builder (core / high fan-in code) | **strong or mid** | Codex Sol, Claude Opus/Sonnet | Samway: Luna implementers had *negative* marginal efficiency (η_I = −12.0); Kim: all 7 centralized mixed teams trailed strong homogeneous baselines (mean −12.6 pts); PaR: high fan-in nodes routed to mid/frontier |
| Builder (fill-in: skeleton given) | **cheap** allowed when the spec ships file layout, stubs/signatures and tests | Gemini Flash | Samway Commit0: Sol lead + Luna implementers ≈ +0.10 async / ≈ −0.02 blocking vs solo (CIs cross 0) instead of negative; Gandhi: prose plan closes only 13–47% of the weak→strong gap (§6b) |
| Builder repair / polish after a strong draft | **cheap** | Gemini Flash | Gandhi "Strong LM First": closes 75–95% of the gap, cheapest per solved issue |
| Reviewer / verifier | **≥ the builder's tier**, execute access, independent tests, ≤4 | Claude Opus/Sonnet; Codex for Gemini-built work | SWE-Review: Opus reviewer lifted weak generator 27.5% → 52.6%, but only +3.0 on the strongest generator; 8B reviewer useless on strong patches; 62% of false approvals involved tests written by the same agent; MAST: verification failures don't go away with a stronger model, so the review structure matters too |
| Acceptance-criteria author | **strong** | Claude Opus / Sol | Agentic Rubrics: frontier rubric authors ~54% vs 30B-class ~45%; non-agentic rubrics −4.0 pts |
| Grader (scores against written criteria) | **cheap** | Gemini Flash | Agentic Rubrics: GPT-5-mini judge only −1.6 pts vs GPT-5 low (−2.4 vs high) |
| Sole integrator | **strong**, single seat, bounded repair | the Commander, or a strong dedicated seat | AsynCodeBench; Co-Coder leader; PaR high fan-in |
| Router / dispatcher / format, status, JSON | **cheap** or deterministic | Gemini Flash or a script | Gandhi: weak router beat strong router (24.0% at $17.9 vs 21.3% at $36.3); PaR (B−), AgentRouter (C) |
| Authorization gate | **not an LLM seat** — deterministic check against the original user policy | Orca/harness hook | MasDrift Source defense |

### 6a. What this changes in the current army

Practice observed in the user's runs vs the evidence:

| Current practice | Verdict | Change |
|---|---|---|
| Gemini Flash "soldiers" do routine implementation | **Contradicted** when the soldier must discover the design (η_I = −12.0); **OK (directional)** for fill-in work | Flash → scouts, graders, fill-in tasks whose spec ships stubs + tests, polish after a strong draft. Anything needing design → Sol / Opus / Sonnet. Calibrate Flash's real tier (§7 Q2). |
| Sonnet "generals" do management + review only, never edit | **Weakened** | Planning-only delegation (lead builds + verifies itself) was the cost-efficient config; a manager with bounded repair beat a read-only one. Give generals bounded repair authority, and make them strong. |
| Depth 2 by default (marshal → generals → soldiers) | **Unsupported** | Default to depth 1; depth 2 only under §3 triggers. |
| Read-only reviewers audit diffs | **Partly supported** | Keep independent reviewers, but they must *execute* (tests, app, rules) and be ≥ builder tier. Compile-level review passed a broken chess program (MAST). |
| Disjoint worktrees, owned files, sole integrator | **Supported** | Cut ownership by cohesion (module/community), not per file. Add an interface contract file. |
| Minimal fan-out; ~40-agent fan-out stopped | **Supported** | Builders/reviewers ≤4 per lead; scouts can go wider. |
| One waiter, ack every delivery, observed turn start | **Supported** | Matches barrier waits (Samway), explicit completion signals (Agyn), termination ownership (MAST). |
| Shared `common.md` injected into specs | **Supported, extend** | Put the original user boundaries in it verbatim and enforce them at call time (MasDrift). |

### 6b. Validating "cheap builders hurt when they must work out the design themselves"

Three levels of design handed to a cheap builder, from the papers:

| What the cheap builder is given | Result | Source |
|---|---|---|
| A task, must discover the spec | Below the strong solo agent, η = −12.0 (each extra dollar lowers reward). Lead still wrote "essentially all" code; Luna's share of edits rose 54% → 85% as implementers were added, while the lead's final check did not grow. | Samway ProgramBench §6, App. (B) |
| A prose plan from the strong model | Gap closed (weak → strong): O4-mini+4o-mini 47%, O3-mini+4o-mini 40%, O3-mini+Qwen-14B 41%, +Qwen-32B 37%, +Qwen-7B 13%. Cost per solved issue *worse* than strong solo ($101 vs $74, O4-mini pair). | Gandhi Tables 3–7 (A) |
| A skeleton: file layout, function stubs, full unit tests | Sol lead + Luna implementers no longer negative: ≈ +0.10 (async), ≈ −0.02 (blocking) vs solo; CIs cross zero; implementation becomes the best stage to delegate in 8/10 settings. | Samway Commit0-Lite, Fig. 30 (B, 16 tasks, 1 run, Sol saturates 12/16) |
| A strong model's first draft to repair/format | Gap closed 75–95%; cheapest per solved issue ($61 vs $74). | Gandhi "Strong LM First" (A) |

Verdict: **confirmed in a sharper form.** The harm comes from cheap builders discovering the spec,
and a prose plan does not fix it. A *skeleton* (interfaces + stubs + tests) is what makes cheap
building safe, and the evidence for that is directional only. Rule (INFERENCE): a cheap soldier gets a
task only if its spec contains the file layout, signatures, and the tests it must pass.

Limits: the cheap models tested (Luna, GPT-4o-mini, Qwen 7–32B) may sit well below Gemini 3.8 Flash.
The papers validate the *mechanism*; Flash's tier must be measured (§7 Q2).

### 6c. "Strong" is relative; Sonnet is not a weak seat

The papers' tiers are positions inside one family (Sol > Terra > Luna; o3/o4-mini > 4o-mini > Qwen),
not absolute grades. MasDrift's heterogeneous team was **GPT-5.6 Sol at the root and GPT-5.4 Nano in
every seat below** (generals and workers); it did not test a frontier model in the middle. So the
current Sol → Sonnet → Flash army is *not* the MasDrift worst case. Sonnet is frontier-class: as
rubric author, Sonnet-4.5 scored on par with Opus-4.5 and Gemini-3-Pro (~54% BEST@16, Agentic
Rubrics Fig 6a), and Sonnet 4.5 was the strongest family in Kim et al. Whether Sonnet 5.5 leads as
well as Sol or Opus on our tasks is unmeasured.

The MasDrift lesson that does transfer: constraint loss is driven by **who decomposes**, while
unauthorized actions are **executed at the bottom**. Homogeneous Sol had the highest constraint loss
(44.7%) but near-zero unauthorized actions, because Sol executors held back. The risk in our army is
therefore the Flash soldiers with tool access, and the fix is the source-based authorization gate,
not a different general.

---

## 7. Open questions for the eval suite

Ordered by how much they would change the design:

1. **Depth 2 vs depth 1 at equal budget on real repo tasks.** No paper answers this. Primary experiment.
2. **Workhorse calibration.** Builders {Flash, Sonnet, Sol} × spec level {goal only, prose plan,
   skeleton + tests} on the same tasks; measure pass rate, reviewer rejections, cost per accepted task.
   This decides which model is the workhorse at each spec level (§6b).
3. **Sonnet vs Opus/Sol as general.** Is mid-tier enough for a depth-1 lead inside a depth-2 army?
4. **Reviewer tier sweep.** Does Sonnet reviewing Sol/Opus output add value, or only reviewing Flash output (SWE-Review pattern)?
5. **Scout width curve** for Flash on our tasks (Samway says up to 16; Kim's Flash curve peaked near 7).
6. **Authorization drift** in our harness: count actions outside the user's stated boundaries at each depth (MasDrift metric).
7. Record per run: completion, interface/dependency resolution, unauthorized actions, tokens, wall-clock,
   MAST failure tags. Budget-match every comparison.

---

## 8. Verification log

Spot-checked against `research/papers/txt/`:

- **Confirmed:** Samway (all headline numbers); SWE-Review 27.5 → 52.6 (Opus 4.6 reviewer, Qwen3-30B-A3B
  generator, Table 2; the 56.9 in Fig 1 is a different series); Co-Coder 14.0 / 2.10× / 20.1 vs 16.3;
  Gandhi (all Table 3 pairings); MasRouter; MasDrift Table 3; Żywot; critique-router (Table 1 as decimals).
- **Corrected:** Agentic Rubrics: the cheap-judge gap is 1.6 pts vs GPT-5 *Low* (54.2), 2.4 vs *High* (55.0);
  the note said "vs high-reasoning".
- **Downgraded:** AgentRouter: note claimed an ICML 2026 workshop; the PDF never mentions a workshop and
  "PMLR 306" is the ICML template footer → grade **C**. Planner-as-Router: acceptance is the authors' own
  statement on the PDF, 54 tasks, ±6 pt CIs → **B−**. Żywot: workshop paper → **B** (note said A).
- **Not reproduced:** no experiment was rerun. Most depth comparisons in the base are not budget-matched.
