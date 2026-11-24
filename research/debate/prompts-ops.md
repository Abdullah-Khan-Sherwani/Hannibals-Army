# Ops feasibility: Hannibal's Army prompts (Orca + git on Windows)

Verified live 2026-10-15 (CLI help + skill refs, `account list --json`, `worktree list`, git 2.56, my dispatch `ctx_ad3e9ae4c282`).

## OPS-1 (blocker) — prompts/hannibal.md:37-38, prompts/task-card.md:10
No prompt says where a worker runs. `--worktree current` resolves to the coordinator's checkout: my dispatch shows `startOptions.worktree:"current"`, `terminal.branch:"refs/heads/main"`. Four heavy infantry each `git checkout -b` in that one checkout overwrite each other's HEAD while Hannibal merges; "one branch per module" never exists. Replace hannibal.md:37 with: "Every writing seat gets its own worktree: `worker-start --task <id> --worktree new-child --name <module> --base-branch main --agent <agent> --json`. Never place two writers on `--worktree current` (read-only seats only). Orca names branches `<git-username>/<name>` (observed), so take `{{BRANCH}}` after the receipt from `worker-show --dispatch <id> --json` → `terminal.branch`, never from a guess."

## OPS-2 (blocker) — prompts/handover.md:3-6, prompts/hannibal.md:70-71
Handover names no Orca command. The Run binds to a coordinator handle and carries `consumer_generation` (`run-list --json`: `run_666b6d46286e` reads `coordinator_handle:null, consumer_generation:2`). A successor who only reads the doc and `git log` consumes nothing: queued `ask`s and `worker_done`s stay in the old Run, or both Hannibals ack the same FIFO batch. Orca routes the word "handover" to `orca-cli`, absent here. Replace handover.md:3 with: "Successor protocol: predecessor records `orca orchestration run-current --json` `run_id` here and stops calling `check`; new session runs `orca orchestration run-use --id <run_id> --json`; confirm with `run-current --json` (handle, `consumer_generation` changed); then `orca orchestration check --run <run_id> --json` to drain pending asks and settlements before touching git."

## OPS-3 (high) — prompts/hannibal.md:23
`orca account list` prints accounts only; limits exist only under `--json` → `result.rateLimits` (live: claude 46%, codex 52%, antigravity weekly 100% used; gemini/grok/cursor unavailable). Hannibal's ≥2× gate then has no numbers. Replace hannibal.md:23 with: "Run `orca account list --json` on the seat host; read `result.rateLimits.<provider>.[session|weekly].usedPercent` (keys `claude`, `codex`, `antigravity`, `opencode-go`). A provider with `status:"unavailable"` has no measurable headroom and cannot take a seat."

## OPS-4 (high) — prompts/_common.md:30, prompts/hannibal.md:68-69
"Pause, resume after the muster gate" has no Orca path, and Orca circuit-breaks a Task after three consecutive failures, forbidding routing around it; a quota-dead agent may send nothing at all. Append to _common.md:30: "If quota kills you before `worker_done`, Hannibal finds the attempt with `orca orchestration worker-list --run <run_id> --json`." Replace hannibal.md:69 with: "Resume a quota-stopped Task with `worker-start --task <id> --retry-of <failed_dispatch_id> --worktree <same explicit selector> --agent <agent> --json`; placement is never inherited, and a new Task is not a retry. Count failures per Task; at three, stop dispatching and take it to the user."

## OPS-5 (high) — prompts/general.md:11,15,20; prompts/hannibal.md:73
Generals can dispatch (my preamble allows it; Hannibal's workers record `depth: 1`, so a general's builders are depth 2) but may not go deeper (`nested_worker_depth_exceeded`; cap unpublished — INFERENCE: refused at depth 3). General.md never has the general create a Run, so its sub-workers' `ask`s default to their owning Run — Hannibal's inbox — and the general stalls. Replace general.md:11 with: "First `orca orchestration run-create --objective \"<subproject>\" --json`; dispatch every card with `--run <run_id>`; read your workers with `check --run <run_id> --wait --types question,escalation --json`. If `worker-start` refuses with `nested_worker_depth_exceeded`, stop, write the cards to `{{ARMY_DIR}}/cards/`, and send them to Hannibal by `ask`." Add each general's `run_id` to handover.md:15.

## OPS-6 (high) — prompts/hannibal.md:24,57; prompts/task-card.md:9
No mapping from banner models to launch flags; the "effective model" gate has no command. My launch shows `launch.effective.model:null` — a seat silently runs on the user's default. Replace hannibal.md:24 with: "Launch proof = `worker-show --dispatch <id> --json`; require `launch.effective.agent` and `launch.effective.model` to equal the banner — `requested` alone is not proof. Launch with `--agent <claude|codex|antigravity|opencode> --model <id> [--effort <level>]`; `--effort` requires `--model`; OpenCode model override needs `--worktree current` or an existing worktree, so place DeepSeek seats on one."

## OPS-7 (medium) — prompts/hannibal.md:16
A literal `.git/info/exclude` write fails when the campaign repo is a linked worktree (`.git` is a file there), and `.army/` dies under `git clean -xfd`. Verified: in a linked worktree `git rev-parse --git-path info/exclude` returns the common dir, so one line covers every worktree. Replace with: "`echo .army/ >> \"$(git rev-parse --git-path info/exclude)\"`"; add to _common.md rules: "Never run `git clean -xfd`." Quote every absolute path; `Hannibal's Army` has a space and apostrophe that break unquoted shells.

## OPS-8 (medium) — prompts/hundred-and-four.md:8
The reviewer must run the builder's branch but gets no placement. Orca worktrees accept a local branch as base (observed `baseRef:"Abdullah-Khan-Sherwani/bw-spend"`), so add: "Placement: `worker-start --task <review_task> --worktree new-child --name review-<task_id> --base-branch <builder-branch> --agent <agent> --json`; never review inside the coordinator's checkout."

## Top 3 changes
1. A `new-child` worktree per writing seat; `{{BRANCH}}` read from `terminal.branch` (OPS-1, OPS-8).
2. The successor protocol in handover.md: `run-current` → `run-use --id` → `run-current` → `check --run` (OPS-2).
3. Muster/Encampment against real verbs: limits via `account list --json`, retries via `--retry-of`, model proof via `launch.effective` (OPS-3, OPS-4, OPS-6).
