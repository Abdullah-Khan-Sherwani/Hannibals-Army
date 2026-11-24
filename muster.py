#!/usr/bin/env python3
"""New Carthage: muster helper for Hannibal's Army (stdlib only).

  python muster.py assemble --seat hannibal --var CAMPAIGN=x --var REPO_PATH=... -o hannibal.txt
  python muster.py assemble --seat builder --card brief.md --var SEAT_PLAIN=builder ... [--vars v.json] -o spec.txt
  python muster.py launch --spec spec.txt --agent codex --model <id> [--effort xhigh] [--worktree current]
                          [--name card-1 --base-branch skel] [--run run_x] [--title "..."]
  python muster.py selftest
"""
import argparse, json, re, shutil, subprocess, sys, time
from pathlib import Path

PROMPTS = Path(__file__).resolve().parent / "prompts"
SEATS = {"builder": "builder", "scout": "scout", "qa-tester": "QA tester",
         "red-team": "red-team tester", "general": "sub-project lead"}
PLACEHOLDER = re.compile(r"\{\{[A-Z_]+\}\}")
COMMENT = re.compile(r"<!--.*?-->\s*", re.S)


def orca(*args, check=True):
    exe = shutil.which("orca") or sys.exit("orca not found on PATH")
    p = subprocess.run([exe, *args], capture_output=True, text=True, encoding="utf-8")
    if check and p.returncode not in (0, 1):  # worker-start exits 1 for outcome_unknown, still a receipt
        sys.exit(f"orca {' '.join(args[:3])} failed ({p.returncode}): {p.stderr or p.stdout}")
    return p.stdout


def orca_json(*args):
    out = orca(*args, "--json")
    try:
        return json.loads(out)
    except json.JSONDecodeError:
        sys.exit(f"orca {' '.join(args[:3])} returned non-JSON:\n{out[:500]}")


# ---------- assemble ----------
def assemble(seat, card_text, values, templates=PROMPTS):
    if seat == "hannibal":  # the commander's own prompt: no common block, no card
        parts = [(templates / "hannibal.md").read_text(encoding="utf-8")]
    elif seat in SEATS:
        values = {"SEAT_PLAIN": SEATS[seat], **values}
        parts = [(templates / "_common.md").read_text(encoding="utf-8"),
                 (templates / f"{seat}.md").read_text(encoding="utf-8"), card_text]
    else:
        sys.exit(f"unknown seat {seat!r}; one of hannibal, {', '.join(SEATS)}")
    text = "\n\n".join(COMMENT.sub("", p).strip() for p in parts)
    text = PLACEHOLDER.sub(lambda m: values.get(m.group()[2:-2], m.group()), text)
    return text, sorted(set(PLACEHOLDER.findall(text)))


def cmd_assemble(a):
    values = json.loads(Path(a.vars).read_text(encoding="utf-8")) if a.vars else {}
    for kv in a.var:
        k, _, v = kv.partition("=")
        values[k] = v
    card = Path(a.card).read_text(encoding="utf-8") if a.card else ""
    text, left = assemble(a.seat, card, values, Path(a.templates))
    if left:
        sys.exit("unfilled placeholders: " + " ".join(left))
    Path(a.out).parent.mkdir(parents=True, exist_ok=True)
    Path(a.out).write_text(text, encoding="utf-8")
    print(f"wrote {a.out} ({len(text)} chars)")


# ---------- launch + launch proof ----------
def cmd_launch(a):
    spec = Path(a.spec).read_text(encoding="utf-8")
    if PLACEHOLDER.search(spec):
        sys.exit("spec still has placeholders; run assemble first")
    args = ["orchestration", "worker-start", "--spec", spec, "--agent", a.agent, "--worktree", a.worktree]
    for flag, val in (("--model", a.model), ("--effort", a.effort), ("--name", a.name),
                      ("--base-branch", a.base_branch), ("--run", a.run), ("--task-title", a.title)):
        if val:
            args += [flag, val]
    r = orca_json(*args).get("result", {})
    dispatch = r.get("dispatchId") or sys.exit(f"worker-start gave no dispatch: {json.dumps(r)[:800]}")
    turn = r.get("turnStart") or "unknown"  # "input accepted" is not proof of a turn start

    show = orca_json("orchestration", "worker-show", "--dispatch", dispatch)["result"]
    worker = show.get("worker", {})
    handle = worker.get("agentTerminalHandle")
    eff = worker.get("startOptions", {}).get("launch", {}).get("effective", {})
    screen = orca("terminal", "read", "--terminal", handle, check=False) if handle else ""
    if turn != "observed" and "[Pasted Content" in screen[-1500:]:  # codex sometimes leaves the task unsent
        orca("terminal", "send", "--terminal", handle, "--enter")
        time.sleep(5)
        screen = orca("terminal", "read", "--terminal", handle, check=False)
        turn = "enter-sent"
    proof = {
        "dispatch": dispatch, "terminal": handle, "branch": (show.get("terminal") or {}).get("branch"),
        "agent": eff.get("agent"), "model": eff.get("model"), "turn": turn,
        "screen_tail": [l for l in screen.splitlines() if l.strip()][-4:],
    }
    print(json.dumps(proof, indent=2))
    if a.model and eff.get("model") not in (None, a.model):
        sys.exit(f"launch proof FAILED: asked for {a.model}, effective {eff.get('model')}")
    if eff.get("model") is None:
        print("effective model not reported: confirm it from screen_tail before counting this seat live", file=sys.stderr)


# ---------- self-check ----------
def cmd_selftest(_):
    text, left = assemble("scout", "Goal: {{GOAL}} at {{REPORT_PATH}}", {"GOAL": "map auth"})
    assert "You are a scout" in text and "map auth" in text and "<!--" not in text, text[:300]
    assert "{{REPORT_PATH}}" in left and "{{GOAL}}" not in left, left
    text, left = assemble("hannibal", "", {})
    assert text.startswith("<hannibal>") and "{{TOOLKIT}}" in left, left
    text, left = assemble("qa-tester", "", {})
    assert "synthetic users" in text.lower() and not left
    for seat, name in (("red-team", "red-team tester"), ("general", "sub-project lead")):
        text, left = assemble(seat, "", {})
        assert f"You are a {name}" in text and not left
    print("selftest ok")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    s = sub.add_parser("assemble")
    s.add_argument("--seat", required=True); s.add_argument("--card")
    s.add_argument("--var", action="append", default=[]); s.add_argument("--vars")
    s.add_argument("--templates", default=str(PROMPTS)); s.add_argument("-o", "--out", required=True)
    l = sub.add_parser("launch")
    l.add_argument("--spec", required=True); l.add_argument("--agent", required=True)
    for f in ("--model", "--effort", "--name", "--base-branch", "--run", "--title"):
        l.add_argument(f)
    l.add_argument("--worktree", default="current")
    sub.add_parser("selftest")
    a = ap.parse_args()
    {"assemble": cmd_assemble, "launch": cmd_launch, "selftest": cmd_selftest}[a.cmd](a)


if __name__ == "__main__":
    main()
