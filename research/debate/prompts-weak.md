# Adversarial Review: Weak-Seat Simulation (Light Cavalry & Auxiliaries)

Simulation: (1) Light Cavalry mapping Django auth; (2) Auxiliaries implementing 3 stubs in `billing/parse.py` across 8 tests.

### F1: Report Heading Schema Collision
- File: `prompts/_common.md:36` vs `prompts/light-cavalry.md:17`
- Problem: `_common.md:36` commands "using exactly these headings...", while `light-cavalry.md:17` orders "add these headings after 'What I did'...". Weak models treat "exactly these headings" as exclusionary.
- Concrete Failure Scenario: In Django auth scouting, Gemini 3.8 Flash prioritizes the strict negative constraint in `_common.md` and drops `## Findings`, `## Risks`, and `## Not checked`. It outputs only file listings and "not run" under `## Evidence`. Zero architectural recon is delivered.
- Replacement text:
In `prompts/_common.md:36`:
`Write your report to {{REPORT_PATH}} using your seat's schema, ending with ## Blocked / open.`
In `prompts/light-cavalry.md:17-23`:
`Headings for {{REPORT_PATH}}: ## Outcome (one line), ## Findings (facts, code locations, architecture flows), ## Risks, ## Not checked, ## Blocked / open.`

### F2: Disconnected Failure and Exit Semantics
- File: `prompts/_common.md:28-32` and `prompts/auxiliaries.md:16,18`
- Problem: Prompts order workers to "stop and report" without linking halts to Orca preamble lifecycle command `worker_done`.
- Concrete Failure Scenario: In `billing/parse.py`, an auxiliary encounters an ambiguous stub. Obeying `auxiliaries.md:16` ("stop and say so in your report"), it appends notes to `reports/task.md` and halts. It never runs `worker_done`. The coordinator hangs until dispatch timeout.
- Replacement text:
In `prompts/_common.md:28-32`:
`- Quota/loop/spec blocker: write {{REPORT_PATH}}, then run: orca orchestration send --from <TERM> --type worker_done --task-id {{TASK_ID}} --dispatch-id {{DISPATCH_ID}} --outcome failed --report-path {{REPORT_PATH}}`

### F3: Omission of Git Commit from Sequential Steps
- File: `prompts/auxiliaries.md:7-11, 21`
- Problem: "Steps, in order: 1-4" ends at report writing; commit instruction is detached at line 21.
- Concrete Failure Scenario: An auxiliary fills 3 stubs in `billing/parse.py`, passes 8 tests, writes `reports/task.md`, and sends `worker_done`. Because commit was omitted from steps 1-4, code changes remain uncommitted. Hannibal merges an empty branch.
- Replacement text:
In `prompts/auxiliaries.md:7-12`:
`Steps: 1. Read stubs/tests. 2. Implement stubs until tests pass. 3. Run test command. 4. Git commit: git add <files> && git commit -m "feat: implement stubs". 5. Write report to {{REPORT_PATH}}.`

### F4: Mandatory Assumptions Invites Spec Guessing
- File: `prompts/_common.md:44-45` and `prompts/auxiliaries.md:3, 18`
- Problem: `auxiliaries.md:3` forbids design ("You do not design"). `_common.md:44-45` demands `## Assumptions` ("Every guess you made").
- Concrete Failure Scenario: In `billing/parse.py`, an auxiliary encounters ambiguous timestamp parsing. Instead of halting for `orca ask`, it invents a fallback heuristic, notes the guess under `## Assumptions`, and marks the task done. Unverified weak-tier design enters production.
- Replacement text:
In `prompts/_common.md:44-45`:
`## Assumptions (Heavy infantry only. Auxiliaries never guess; use Orca ask).`

### F5: Single-Line Anchor Breaks Architectural Flows
- File: `prompts/light-cavalry.md:14`
- Problem: "Every finding needs a location: `path:line`... No location, no finding."
- Concrete Failure Scenario: In Django auth scouting, tracing request lifecycle across middleware, auth backends, and sessions spans multiple files. Forced into single-line citations, the model deletes flow analysis and returns disconnected line numbers.
- Replacement text:
In `prompts/light-cavalry.md:14`:
`4. Anchor code facts to path:line. For architectural flows, trace the sequence and cite primary files.`

### F6: Premature Task-Card Dependencies
- File: `prompts/task-card.md:15-18`
- Problem: Task card mandates reading `{{ARMY_DIR}}/ARCH.md`. During Phase 1 Reconnaissance, `ARCH.md` does not exist. For auxiliaries, reading global architecture overloads context.
- Concrete Failure Scenario: Django auth scout halts on missing `ARCH.md`. Billing auxiliary ingests global architecture and refactors module boundaries.
- Replacement text:
In `prompts/task-card.md:15`:
`Read first: {{STUB_AND_TEST_PATHS}} (Auxiliaries); {{CONTRACT_PATH}}#{{SECTION}} (Builders); {{SCOUT_TARGET}} (Scouts).`

### F7: Thematic Jargon and Safety Triggers
- File: `prompts/_common.md:6-10, 30` and `prompts/light-cavalry.md:3`
- Problem: Metaphors ("Hannibal", "Encampment", "Light cavalry") cause confusion. INFERENCE: Military vocabulary ("army", "attack") triggers safety refusals in weak models.
- Concrete Failure Scenario: On rate limit, a model reads "This is Encampment" (`_common.md:30`) and attempts shell command `encampment`.
- Replacement text:
Replace roleplay terms: Hannibal -> Coordinator; Light Cavalry -> Scout; Auxiliaries -> Stub Implementer; Encampment -> Quota Pause.

### F8: Unenforceable Caps and Parallelism
- File: `prompts/_common.md:32`, `prompts/task-card.md:27`, `prompts/light-cavalry.md:12`
- Problem: Requiring weak models to monitor output tokens and minutes, or run lookups "in parallel".
- Concrete Failure Scenario: In single-terminal shell, scout appends `&` to grep commands, creating detached background processes and lost output.
- Replacement text:
In `prompts/light-cavalry.md:12-13`:
`2. Run lookups sequentially. 3. Budget: {{TOOL_BUDGET}} tool calls max.`
In `prompts/task-card.md:27`:
`Caps: {{TOOL_BUDGET}} tool calls max.`

## Top 3 changes
1. **Unify report schema per seat (F1):** Eliminate contradictory "using exactly these headings" in `_common.md` so scout findings are not discarded.
2. **Explicitly link all termination paths to Orca CLI (F2):** Provide exact `worker_done` commands for error and loop exits.
3. **Add git commit to auxiliary sequential steps (F3):** Ensure weak fill-in builders commit working code before reporting completion.
