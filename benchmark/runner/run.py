#!/usr/bin/env python3
"""Drive one skill over one corpus in an isolated workspace, headlessly.

This is the part of the benchmark that has to be boring and identical for every
skill, because everything downstream inherits its bias. Four things are held
fixed across every run:

  * **The agent.** Same model, same effort, same permission mode.
  * **The prompt.** One neutral instruction, byte-identical for all skills. Its
    sha256 goes into the manifest so a reader can prove it was not tuned per
    skill.
  * **The environment.** `--setting-sources project` so only the skill under
    test is visible. Verified empirically: the operator's ~/.claude/skills does
    not leak in, which matters because a stray `frontend-design` skill would
    quietly improve every deck.
  * **The material.** The corpus file, copied in verbatim as `input.md`.

What is *not* held fixed is how the skill gets invoked. A skill whose frontmatter
`description` does not fire on a plain "make a deck from this" request has a real
usability problem, so the neutral prompt runs first. If the skill never loads, the
run is retried once naming it explicitly and the manifest records
`invocation: "explicit"` — a fact for the scorecard, not a silent fixup.

    python run_skill.py --skill frontend-slides \\
                        --corpus ../corpus/01-product-launch.md \\
                        --run run-01

Every run writes `run.json` next to the deck: skill commit sha, model, wall
time, cost, whether the skill fired, and the prompt hash.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import shutil
import subprocess
import sys
import tempfile
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CACHE = ROOT / "benchmark" / ".cache" / "skills"
RESULTS = ROOT / "benchmark" / "results"

# The one instruction every skill receives. Deliberately plain: it names no
# skill, requests no style, and repeats none of the corpus's own constraints
# (corpus 02 already carries its own anti-fabrication warning inside the
# material, which is where a real user's constraints would live).
PROMPT = (
    "Read `input.md` in this directory and turn it into a presentation deck.\n"
    "\n"
    "Write every output file into this directory. When you are finished, state "
    "the filename of the deck you produced."
)

# Retry wording used only when the neutral prompt failed to load the skill.
EXPLICIT_SUFFIX = "\n\nUse the `{name}` skill to do this."

# Where SKILL.md lives, for repos that do not keep it at the root. Discovered by
# inspection; the resolver falls back to a search when an id is absent here.
SKILL_SUBDIR = {
    "ppt-master": "skills/ppt-master",
    "visual-explainer": "plugins/visual-explainer",
}

# Skills that are not a drop-in SKILL.md and cannot be run by this harness as-is.
# Recorded rather than silently skipped — see benchmark/README.md.
UNSUPPORTED = {
    "open-slide": (
        "A React framework plus a vendored set of third-party design skills, not "
        "a single installable slide skill. Needs a different harness."
    ),
    "anthropic-pptx": (
        "Lives inside the anthropics/skills monorepo and is distributed through "
        "the Claude Code plugin marketplace rather than as a cloneable skill dir."
    ),
}

# Anything that looks like a finished deck. Ordered by how strongly it signals
# "this is the deliverable".
DECK_GLOBS = ["*.html", "*.pptx", "*.pdf", "slides/**/*.html", "dist/**/*.html"]


def sh(cmd: list[str], cwd: Path | None = None) -> str:
    return subprocess.run(
        cmd, cwd=cwd, check=True, capture_output=True, text=True
    ).stdout.strip()


def repo_fingerprint() -> str:
    """Hash the files a run must not be able to change: the corpus it is being
    tested on, the rubric it will be scored against, and the harness itself.

    Not a hash of the whole repo. Other sessions commit to this repository while
    runs are in flight, and a check that fires on unrelated commits gets ignored,
    which is worse than no check. These paths are the ones where a change during
    a run would silently invalidate the result.
    """
    parts = []
    for pattern in ("benchmark/corpus/*.md", "benchmark/rubric*.md",
                    "benchmark/runner/*.py"):
        for f in sorted(ROOT.glob(pattern)):
            st = f.stat()
            parts.append(f"{f.relative_to(ROOT)}:{st.st_size}:{st.st_mtime_ns}")
    return hashlib.sha256("\n".join(parts).encode()).hexdigest()[:16]


def load_registry() -> dict:
    data = json.loads((ROOT / "data" / "skills.json").read_text())
    return {s["id"]: s for s in data["skills"]}


def ensure_clone(skill: dict) -> Path:
    """Shallow-clone the skill repo into the cache if it is not there yet."""
    dest = CACHE / skill["id"]
    if not dest.exists():
        dest.parent.mkdir(parents=True, exist_ok=True)
        print(f"  cloning {skill['repo']} ...", flush=True)
        sh(["git", "clone", "--depth", "1", "-q",
            f"https://github.com/{skill['repo']}", str(dest)])
    return dest


def resolve_skill_dir(skill: dict, repo_dir: Path) -> Path:
    """Find the directory containing the SKILL.md that is the skill itself."""
    if skill["id"] in SKILL_SUBDIR:
        return repo_dir / SKILL_SUBDIR[skill["id"]]
    if (repo_dir / "SKILL.md").exists():
        return repo_dir
    candidates = [
        p.parent
        for p in repo_dir.rglob("SKILL.md")
        if "node_modules" not in p.parts and ".git" not in p.parts
    ]
    if not candidates:
        raise SystemExit(f"no SKILL.md found in {repo_dir}")
    # Shallowest wins: a skill vendored deep inside a repo is a dependency of the
    # thing being tested, not the thing itself.
    return min(candidates, key=lambda p: len(p.relative_to(repo_dir).parts))


def copy_tree(src: Path, dst: Path) -> None:
    """Copy a skill into the workspace, preferring APFS clones for the big ones.

    ppt-master's skill directory is ~100MB of templates. `cp -c` makes that a
    copy-on-write clone: instant, and it costs no disk until something is
    modified. Falls back to a real copy anywhere clonefile is unavailable.
    """
    dst.parent.mkdir(parents=True, exist_ok=True)
    if sys.platform == "darwin":
        r = subprocess.run(["cp", "-Rc", str(src), str(dst)], capture_output=True)
        if r.returncode == 0:
            return
    shutil.copytree(src, dst, dirs_exist_ok=True)


def build_workspace(ws: Path, skill_dir: Path, skill_id: str, corpus: Path) -> None:
    if ws.exists():
        shutil.rmtree(ws)
    ws.mkdir(parents=True)
    copy_tree(skill_dir, ws / ".claude" / "skills" / skill_id)
    shutil.copyfile(corpus, ws / "input.md")


def skill_name(skill_dir: Path) -> str:
    """Read the frontmatter `name:` — what the agent will actually call it."""
    text = (skill_dir / "SKILL.md").read_text(errors="replace")
    if text.startswith("---"):
        end = text.find("\n---", 3)
        for line in text[3:end if end > 0 else 400].splitlines():
            if line.strip().startswith("name:"):
                return line.split(":", 1)[1].strip().strip("\"'")
    return skill_dir.name


def invoke(ws: Path, prompt: str, model: str, budget: float, log: Path) -> dict:
    """Run the agent headlessly, streaming events to `log`. Never raises on a
    non-zero exit — a skill that crashes the agent is a result, not an error."""
    cmd = [
        "claude", "-p", prompt,
        "--setting-sources", "project",
        "--strict-mcp-config",
        "--permission-mode", "bypassPermissions",
        "--model", model,
        "--max-budget-usd", str(budget),
        "--no-session-persistence",
        "--output-format", "stream-json",
        "--verbose",  # stream-json emits nothing useful without it
    ]
    started = time.time()
    with log.open("w") as fh:
        proc = subprocess.run(cmd, cwd=ws, stdout=fh, stderr=subprocess.STDOUT,
                              text=True)
    elapsed = round(time.time() - started, 1)

    fired, cost, turns, result_text = False, None, None, None
    for line in log.read_text(errors="replace").splitlines():
        if not line.startswith("{"):
            continue
        try:
            ev = json.loads(line)
        except json.JSONDecodeError:
            continue
        if ev.get("type") == "result":
            cost = ev.get("total_cost_usd")
            turns = ev.get("num_turns")
            result_text = ev.get("result")
        blob = json.dumps(ev)
        if '"name": "Skill"' in blob or '"name":"Skill"' in blob:
            fired = True
    return {
        "exit_code": proc.returncode,
        "elapsed_s": elapsed,
        "skill_fired": fired,
        "cost_usd": cost,
        "num_turns": turns,
        "agent_final_message": result_text,
    }


def collect(ws: Path, deck_dir: Path) -> list[str]:
    """Move produced artifacts out of the workspace, leaving inputs behind."""
    deck_dir.mkdir(parents=True, exist_ok=True)
    found: list[Path] = []
    for pattern in DECK_GLOBS:
        for p in ws.glob(pattern):
            if ".claude" in p.parts or p.name == "input.md":
                continue
            found.append(p)
    seen, out = set(), []
    for p in sorted(set(found)):
        rel = p.relative_to(ws)
        target = deck_dir / rel
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(p, target)
        if str(rel) not in seen:
            seen.add(str(rel))
            out.append(str(rel))
    return out


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--skill", required=True)
    ap.add_argument("--corpus", required=True, type=Path)
    ap.add_argument("--run", default="run-01")
    ap.add_argument("--rep", type=int, default=1,
                    help="repetition index; generative variance is real")
    ap.add_argument("--model", default="sonnet")
    ap.add_argument("--budget", type=float, default=3.0,
                    help="hard USD ceiling per run")
    ap.add_argument("--keep-workspace", action="store_true")
    args = ap.parse_args()

    registry = load_registry()
    if args.skill not in registry:
        print(f"unknown skill id: {args.skill}", file=sys.stderr)
        return 2
    if args.skill in UNSUPPORTED:
        print(f"{args.skill}: {UNSUPPORTED[args.skill]}", file=sys.stderr)
        return 3

    skill = registry[args.skill]
    corpus = args.corpus.resolve()
    corpus_id = corpus.stem

    repo_dir = ensure_clone(skill)
    sha = sh(["git", "rev-parse", "HEAD"], cwd=repo_dir)
    skill_dir = resolve_skill_dir(skill, repo_dir)
    name = skill_name(skill_dir)

    out_dir = RESULTS / args.run / args.skill / corpus_id / f"rep-{args.rep:02d}"
    out_dir.mkdir(parents=True, exist_ok=True)

    # The workspace lives outside the repository, deliberately.
    #
    # The agent under test runs with bypassPermissions, because a skill that
    # needs to run its own scripts cannot be driven any other way. Given a cwd
    # inside this repo it can read its way up to the corpus, the rubric, the
    # results of other runs, and the harness itself — none of which a skill being
    # asked "turn input.md into a deck" should ever see. Putting the workspace in
    # a temp directory removes the reachability rather than trusting restraint.
    ws = Path(tempfile.mkdtemp(prefix=f"ppt-run-{args.skill}-"))

    repo_before = repo_fingerprint()

    print(f"▶ {args.skill} × {corpus_id} (rep {args.rep}, {args.model})", flush=True)
    build_workspace(ws, skill_dir, args.skill, corpus)

    telemetry = invoke(ws, PROMPT, args.model, args.budget, out_dir / "agent.log")
    invocation = "auto"
    if not telemetry["skill_fired"]:
        print("  skill did not fire on the neutral prompt — retrying explicitly",
              flush=True)
        build_workspace(ws, skill_dir, args.skill, corpus)
        telemetry = invoke(ws, PROMPT + EXPLICIT_SUFFIX.format(name=name),
                           args.model, args.budget, out_dir / "agent.log")
        invocation = "explicit" if telemetry["skill_fired"] else "never-fired"

    artifacts = collect(ws, out_dir / "deck")
    repo_after = repo_fingerprint()

    manifest = {
        "skill": args.skill,
        "skill_name": name,
        "repo": skill["repo"],
        "commit": sha,
        "corpus": corpus.name,
        "run": args.run,
        "rep": args.rep,
        "model": args.model,
        "invocation": invocation,
        "prompt_sha256": hashlib.sha256(PROMPT.encode()).hexdigest()[:16],
        "artifacts": artifacts,
        "workspace_outside_repo": True,
        "harness_fingerprint": repo_before,
        "harness_unchanged_during_run": repo_before == repo_after,
        **telemetry,
    }
    (out_dir / "run.json").write_text(json.dumps(manifest, indent=2) + "\n")

    if args.keep_workspace:
        print(f"  workspace kept at {ws}", flush=True)
    else:
        shutil.rmtree(ws, ignore_errors=True)

    if repo_before != repo_after:
        print("  WARNING: corpus, rubric or harness changed while this run was in "
              "flight — the result is not reproducible from the recorded inputs",
              file=sys.stderr)

    status = "ok" if artifacts else "NO ARTIFACTS"
    cost = f"${telemetry['cost_usd']:.2f}" if telemetry["cost_usd"] else "?"
    print(f"  {status} · {len(artifacts)} file(s) · {telemetry['elapsed_s']}s · "
          f"{cost} · invocation={invocation}", flush=True)
    return 0 if artifacts else 1


if __name__ == "__main__":
    raise SystemExit(main())
