# R1 — skeptic

## 1. Stance

**INFERENCE:** Default to one strong coding agent; make a small, strong-only depth-1 team earn its overhead before formalizing an army.

Paper paths below are relative to `research/papers/`; numerical citations include local text lines. Interpretations, recommendations and proposed budgets are **INFERENCE**, not measured results.

## 2. Top five attacks, ranked

1. **INFERENCE — The default is unsupported and internally contradictory.** Two separable pieces satisfy depth 1, while fewer than five qualify for depth 0 (`research/proposal-draft.md`, §2). Kim's published coding results favor solo: SWE-bench 48.8% versus centralized 47.5%; Terminal-Bench 31.2% versus 25.0% (`txt/2512.08296-journal.txt:193–202`). Its coding cells have only 20 tasks (`notes/2512.08296.md`, Setup); its unseen-domain prediction R²=−2.09 cautions against transferring architecture rules (`txt/2512.08296-journal.txt:904–914`). **Change:** depth 0 by default; separability permits an experiment, not automatic dispatch.

2. **INFERENCE — Samway cannot establish a universal cheap-worker doctrine.** η=−12.0 is verified, but means reward points per $100 of *additional* inference relative to solo, not a general Flash coefficient; the paper explicitly does **not** match budgets (`txt/2610.17471.txt:181–202,518–520`). ProgramBench requires black-box specification discovery; Commit0 supplies skeletons/tests and reverses the favored delegation stage, with only 16 tasks and one run (`txt/2610.17471.txt:2269–2285`). The width sweep also uses one run (`txt/2610.17471.txt:570–572`). **Change:** calibrate complete workflows locally; charge skeleton/test authorship, dispatch, review and repair. Do not infer safety from supplying stubs.

3. **INFERENCE — Depth-2 permission and its supposed safety net outrun the evidence.** MasDrift varies agent count with depth and tests synthetic productivity, not coding (`notes/2608.07556.md`, Setup/Validity). “All-Sol L2 was fine” hides 37.0% constraint loss alongside 100% completion and 1.5% unauthorized actions (`txt/2608.07556.txt:402–418`). **Incorrect attribution:** its source-policy compiler is an authorization agent, not purely deterministic (`txt/2608.07556.txt:325–334`). **Change:** exclude generals initially; distinguish deterministic enforcement from fallible policy interpretation.

4. **INFERENCE — More approval seats do not establish reliability.** A weak generator plus frontier review reaches 52.6%, below the strong generator's unreviewed 72.2%; review is not a substitute for implementation capability (`notes/2607.06065.md`, Findings, Table 2). AsynCodeBench's “green” counterexample means ≥80% test pass, not entirely passing suites. MAST's taxonomy is not a causal estimate of a termination rule's benefit; memory savings do not require more managers (audit below). **Change:** retain execution and interface checks; add one strong reviewer selectively, not approval bureaucracy everywhere.

5. **INFERENCE — Grades and counter-positions deserve equal skepticism.** The synthesis downgrades Żywot/AgentRouter/Planner-as-Router relative to their notes, showing that an “A” label is not settled provenance (`research/depth-and-seats.md`, §8). [Cognition](https://cognition.com/blog/dont-build-multi-agents) argues that summaries miss consequential decisions and parallel actors make incompatible assumptions. [Anthropic](https://www.anthropic.com/engineering/multi-agent-research-system) explicitly identifies coding's dependency/shared-context problem; its ~15× tokens compares multi-agent runs with **chats**, while agents use ~4× chats. These are engineering counter-positions, not controlled coding trials. **Change:** test context-preserving solo execution before building a seat-specific skill pack.

**Numerical audit — draft claims checked against full texts:**

| Draft claim | Check and scope |
|---|---|
| Kim −50% to −70% | Confirmed: −50.3%/−70.0% relative PlanCraft changes, not coding (`txt/2512.08296-journal.txt:136–137`). |
| Co-Coder +14.0 points, 0.65× cost | Confirmed: 20.1→34.1% average test pass; $1.03→$0.67, homogeneous GPT-5-mini (`txt/2606.00953.txt:458,512`). |
| Samway half cost; −6 points async | Confirmed, respectively P versus PIV and minimally guided async versus blocking (`txt/2610.17471.txt:339–342,369–373`). |
| Messaging −4.4 to −7.1 | Confirmed for Luna; Sol/Terra unchanged within noise, weakening a universal ban (`txt/2610.17471.txt:609–621`). |
| MasDrift +4.2 completion, +9.0 UA | Confirmed as rounded five-model L1→L2 means (`txt/2608.07556.txt:411–414`). |
| MasDrift ~2.4× tokens | Confirmed for Sol: 111.3k/46.6k≈2.39; not a coding budget prediction (`txt/2608.07556.txt:1259–1266`). |
| MasDrift +0.5 completion at L3 | Rounding-sensitive, not a demonstrated error: displayed rows yield +0.44 points; implied 600-task counts yield ~+0.47, rounding to +0.5 (`txt/2608.07556.txt:411–414,1150–1159`; calculation **INFERENCE**). |
| 88.2% first-handoff losses | Confirmed among 3,950 localized losses, not all runs (`txt/2608.07556.txt:1341–1354`). |
| AsynCodeBench 26/190 | Confirmed in manager-read-only outcomes with ≥80% test pass and zero dependencies resolved (`txt/2609.32662.txt:363–369`). |
| Żywot −43%; MAST 12.4% | Confirmed versus Direct+Think token replay, and as taxonomy prevalence, respectively (`txt/2601.11327.txt:328–331`; `txt/2503.13657.txt:71,88–92`). |

## 3. Alternative plan

**INFERENCE:** Depth 0 normally; depth 1 only for an isolated question/module, maximum two workers; no depth 2 pending evidence.

| Seat | Agent |
|---|---|
| Owner, planner, builder, integrator | One GPT-6.1-Sol |
| Optional scout or isolated builder | One additional Sol |
| Selective independent reviewer | Sol or Opus |
| Tests, permissions, termination | Existing harness/Orca mechanisms |

Keep bounded ownership, original boundaries, execution evidence, explicit completion and spending caps. Remove permanent generals, graders, polishers, wide scout defaults and blanket wave barriers; wait on actual dependencies.

**Proposed pilot:** six representative real tasks × two repetitions × three configurations: solo, solo+strong scout, solo+strong builder = **36 runs**. Give solo compact state and parallel tool calls too. Freeze acceptance checks and initial information; randomize configuration order. Cap each whole run at $5 equivalent spend, including planning/repair; reserve $20 for common acceptance preparation: **$200 maximum**, not a cost forecast. Record actual quota use, dollars per accepted task, elapsed and human intervention time, defects and boundary violations. Treat this as screening; confirm promising results on held-out tasks.

## 4. Evidence that would change my mind

**INFERENCE:** Repeated held-out comparisons showing ≥20% lower cost per accepted task, or ≥20% less time at equal spend, without worse defects/violations. Depth 2 must additionally beat the best shallow configuration after all general and integration costs.

## 5. Verdict

**Reject the proposed default and rollout; adopt the evaluation objective. INFERENCE:** Validate the smallest strong-agent workflow first, then formalize only additions with demonstrated marginal value. Correct numbers mostly survive scrutiny; their transfer into universal operating rules does not.

Scope: no experiments rerun or venue claims independently authenticated; only the two counter-position posts were opened online.
Risk: the proposed pilot can screen alternatives, not establish a universal technique.

