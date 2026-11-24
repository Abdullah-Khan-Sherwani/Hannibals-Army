# Adversarial Review (Round 2): Defender

## 1. What Changed Given the Scope
Restricting Hannibal's Army to full-system builds and major updates (`proposal-draft.md:8–11`) invalidates the skeptic's solo Depth-0 baseline (`r1-skeptic.md:11,38`). At project scale, sequential solo is impossible: multi-day builds exceed context limits, forcing lossy self-rotations (`r1-lead.md:16–17`). Co-Coder shows modular teams dominate sequential solo on project generation (+14.0 pts, 0.48× latency, 0.65× cost, `notes/2606.00953.md:20`, `txt/2606.00953.txt:458,512`). However, project-scale builds amplify unguided cheap builder hazards (Samway: $\eta_I = -12.0$, `txt/2610.17471.txt:493–495`; BlogBERT S1 blocked B1–B4, C1 had 4 defects, `capacity-handover.md:4–5,17–18`). I update my stance: Depth 1 is default for cohesive projects; Depth 2 is reserved for multi-subsystem campaigns crossing domain boundaries (e.g. Safety vs. Discovery, `ledger.md:98`).

## 2. Concessions
1. **Lead's BlogBERT checks:** Commit `b869523` was not general repair (`review-phase1-sonnet-20261011.md:11–21`); generals never edited code. Gemini quota exhaustion stalled all active Gemini terminals simultaneously (`capacity-handover.md:2`). Resilience requires pre-dispatch vendor balancing [INFERENCE].
2. **Realist's ops and eval:** Draft §5's ~750 runs is unexecutable (`r1-realist.md:13`). I adopt Realist's staged eval ($\le 76$ runs with kill gates, starting with $0 mining; `r1-realist.md:13,41`). Quota tracking (`ledger.md:34,75`), launch receipts (`ledger.md:26`), 40k-token rotation (`ledger.md:98`), and single-writer discipline (`capacity-handover.md:12`) are essential.
3. **Skeptic's auth and limits:** MasDrift's Source defense is an LLM agent, not a deterministic hook (`txt/2608.07556.txt:325–334`); all-Sol L2 lost 37.0% of constraints (`txt/2608.07556.txt:402–418`). Weak builders + strong reviewers (52.6%) trail strong builders alone (72.2%) (`notes/2607.06065.md`, Table 2). Flash cannot design core systems.

## 3. Rebuttals
1. **Skeptic's Depth-0 solo default:** Solo fails for full systems (`r1-skeptic.md:11,38`). Kim's solo gain (−50% to −70%, `txt/2512.08296-journal.txt:136–137`) was on toy planning; coding cells had 20 small tasks with wide noise ($\pm 20$ pts, `notes/2512.08296.md`; $R^2 = -2.09$, `txt/2512.08296-journal.txt:904–914`). Co-Coder proves cohesion teams beat solo on projects (+14.0 pts, `txt/2606.00953.txt:458,512`). Solo collapses from context exhaustion in multi-day builds [INFERENCE].
2. **General repair authority:** Giving generals edit power (`proposal-draft.md:39`; `depth-and-seats.md:103,147`) destroys review independence: 62% of false approvals involved tests written by the authoring agent (`notes/2607.06065.md`). User doctrine mandated "management/review ONLY" (`safety-general.md:1`) and a single mutator (`capacity-handover.md:12`). Repairs must return to builders with failing tests [INFERENCE].
3. **Banning Depth 2 entirely:** Skeptic eliminates Depth 2 (`r1-skeptic.md:38`). In multi-subsystem builds, a Depth-1 root supervising 10+ workers suffers context blowout; Safety general consumed 41k output tokens in 48 minutes (`ledger.md:98`). Depth 2 is required for multi-domain campaigns with rotation budgets (Żywot: handoffs cut tokens 43%, `txt/2601.11327.txt:328–331`).
4. **Single-vendor concentration:** Assigning Flash to four seats re-creates the quota stall that froze BlogBERT (`ledger.md:34,75`; `r1-realist.md:21`). Seats require multi-vendor alternatives [INFERENCE].
5. **Number checks:** Skeptic questioning MasDrift L3 gain as "+0.44 or ~+0.47" (`r1-skeptic.md:31`) ignores Table 3's printed delta of +0.5 pts (82.9% $\to$ 83.4%, `txt/2608.07556.txt:411–414`).

## 4. Final Recommended Plan

### Depth Policy
- **Depth 1 (Default):** 2–5 cohesive modules. Sol Commander decomposes, writes contracts, builds core, integrates; parallel builders implement modules; Sonnet independently reviews.
- **Depth 2 (Campaign Mode):** $\ge 2$ sub-projects meeting SPOQ ($\ge 5$ tasks, $\ge 4$ hours, `txt/2606.03115.txt:1573`), root context > 40k tokens, multi-vendor headroom exists. Sol Marshal $\to$ Sonnet Generals (read-only) $\to$ Builders.
- **Depth 3+:** Never (MasDrift: +0.5 completion, +8.1 UA, 2× tokens, `txt/2608.07556.txt:411–414`).

### Seat Allocation Table
| Seat | Agent (Primary/Backup) | Rules |
|---|---|---|
| Commander | Sol (xhigh) / Opus | Architecture, contracts, core build, root integration. |
| General (D2) | Sonnet / Opus | Orchestration, review; read-only (`safety-general.md:1`). |
| Scout | Flash / OpenCode | Search, mapping; read-only; width $\le 8$ (`txt/2610.17471.txt:570–572`). |
| Builder (Core) | Sol / Sonnet | Unspecified design; $\le 3$ per lead (`depth-and-seats.md:149`). |
| Builder (Fill-in) | Flash / OpenCode | Needs layout+stubs+tests (`txt/2610.17471.txt:2269–2285`); $\le 4$/lead. |
| Reviewer | Sonnet / Sol | Independent; executes live tests (`notes/2607.06065.md`). |
| Integrator | Commander (D1) / Flash Steward (D2) | Sole Git mutator (`capacity-handover.md:12`). |
| Auth Gate | Hook / Prompt Injector | Blocks main/secrets; injects boundaries (`txt/2608.07556.txt:1341–1354`). |

### Operating Rules
1. *Quota Pre-Flight:* Check `rateLimits`; spread seats across OpenAI, Anthropic, Google (`ledger.md:34,75`; `orchestration.md:20–31`).
2. *Read-Only Management:* Generals/reviewers never edit code; fixes return to builders with failing tests (`safety-general.md:1`; `capacity-handover.md:12`).
3. *Cohesion Contracts:* Partition by cohesion; commit interface stubs before dispatch (Co-Coder, `txt/2606.00953.txt:458,512`).
4. *Supervisor Rotation:* Rotate generals at 40k output tokens / 70% context via handovers (Żywot, `txt/2601.11327.txt:328–331`; `ledger.md:98`).
5. *Execution-Gated Done:* Completion requires independent test execution and interface resolution (Agentless, `notes/2407.01489.md`; AsynCodeBench, `txt/2609.32662.txt:363–369`).
6. *Runaway Halts:* Stop on 5 repeated tool calls; cap remediation $\le 20$ lines (SPOQ, `txt/2606.03115.txt`; MAST, `txt/2503.13657.txt:71`).

### Staged Eval
- *Stage 0 ($0):* Mine 33 substantive Orca runs for stall, rotation, rejection baselines (`r1-realist.md:13,41`).
- *Stage 1 (16 runs):* 2 tasks $\times$ {D1, D2} $\times$ 4 reps. Kill gate: stop if 48-run MDE $>20$ pts (`r1-realist.md:41`).
- *Stage 2 (36 runs):* 3 tasks $\times$ {Sol core builders, Sonnet/Flash hybrid} $\times$ 6 reps.
- *Cost Unit:* Quota-minutes and human interventions per accepted build; secondary dollar tracking (`r1-realist.md:29,41`).

## 5. Vote
1. **Lead (r1-lead §3):** Best project-scale synthesis, lean Depth-1 baseline with Depth-2 probation, and realistic eval; requires removing general repair authority.
2. **Realist (r1-realist §3):** Indispensable operational guardrails and fundable staged eval, but understates Depth 2's necessity for multi-subsystem builds.
3. **Draft (proposal-draft.md):** Strong literature base, but crippled by unexecutable 750-run eval, general repair authority, and single-vendor Flash concentration.
4. **Skeptic (r1-skeptic §3):** Incompatible with project-scale scope; Depth-0 solo collapses under context limits and relies on noisy single-issue benchmarks.
