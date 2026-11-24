---
name: hannibals-army
description: >-
  Use when the user asks to start, resume or run an orchestration campaign (solo or with Orca workers),
  including overnight QA and fix loops. Not for dispatched workers.
---

# Hannibal's Army

If you are a dispatched worker, follow your Orca preamble and brief instead of this skill.

Resolve this file's directory as `TOOLKIT`. Identify the target repo and campaign; obtain a goal and what done means from the user or context. Create `<repo>/.army/<campaign>/`, exclude `.army/` via git's info/exclude, and save the brief there. Read `DOCTRINE.md` and `prompts/hannibal.md` in full, then follow them. Assemble the latter with `python "<TOOLKIT>/muster.py" assemble --seat hannibal --var CAMPAIGN=<campaign> --var REPO_PATH=<repo> --var ARMY_DIR=<repo>/.army/<campaign> --var TOOLKIT=<TOOLKIT> -o "<repo>/.army/<campaign>/orders.md"`.

After compaction or on resuming, read the campaign's `handover.md` and append-only `log.md` first, then the orders and brief; check the Orca inbox before changing work. If the campaign is unknown, identify it before continuing.
