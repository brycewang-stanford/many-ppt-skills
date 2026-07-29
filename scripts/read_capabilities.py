#!/usr/bin/env python3
"""Fill the capability grid by reading each skill's docs, with a quote per cell.

The regex version of this (`extract_capabilities.py`) is kept because it is fast
and free, but it cannot be trusted on prose. Auditing its output found three
failure modes it has no way to avoid:

  * **Negation.** slide-writer's README says "不生成 .pptx，只输出单个 HTML" —
    *does not* generate pptx. The regex recorded pptx export as supported.
  * **Disparagement.** guizang-ppt-skill says a bad slide "掉到 PowerPoint".
    Matching `PowerPoint` read an insult as a feature.
  * **Input versus output.** frontend-slides ships `extract-pptx.py <input.pptx>`
    for *reading* decks. Matching `python-pptx` read that as an export path.

Six of eleven cells in one column were wrong, one of them exactly inverted. So
this reads the documentation properly instead, and makes every cell carry a
verbatim quote so a reader can overrule it.

    python scripts/read_capabilities.py                    # all skills
    python scripts/read_capabilities.py --only frontend-slides ppt-master

Still *documented* capability, not verified behaviour — a project that overclaims
is still believed here. The quote is the defence: a wrong cell is visibly wrong.
"""

from __future__ import annotations

import argparse
import json
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CACHE = ROOT / "benchmark" / ".cache" / "skills"
OUT = ROOT / "data" / "capabilities.json"

sys.path.insert(0, str(Path(__file__).parent))
from extract_capabilities import (  # noqa: E402
    CAPABILITIES, DOC_NAMES, detect_runtime, resolve_skill_dir,
)

MAX_DOC_CHARS = 60_000  # SKILL.md plus a README, which is what decides these

VERDICTS = ["yes", "no", "unclear"]

SCHEMA = {
    "type": "object",
    "properties": {
        name: {
            "type": "object",
            "properties": {
                "verdict": {"type": "string", "enum": VERDICTS},
                "quote": {"type": "string"},
            },
            "required": ["verdict", "quote"],
            "additionalProperties": False,
        }
        for name in CAPABILITIES
    },
    "required": list(CAPABILITIES),
    "additionalProperties": False,
}

PROMPT_HEAD = """\
Read every file in `docs/`. It is one project's own documentation for a skill
that turns documents into presentation decks.

For each capability below, decide what these documents actually claim, and give a
verbatim quote from them as evidence.

  yes      — the docs claim the skill does this
  no       — the docs explicitly say it does NOT do this
  unclear  — the docs do not settle it

`unclear` is the correct and expected answer whenever the documentation simply
does not address a capability. Do not infer from what a skill of this type
"probably" does. Only the text in front of you counts.

Three traps, each of which has already produced a wrong answer here:

  1. **Negation.** "不生成 .pptx，只输出单个 HTML" means it does NOT export PPTX.
     That is `no`, not `yes`.
  2. **Disparagement.** "a bad deck looks like PowerPoint" is an insult about
     PowerPoint, not a claim of PowerPoint export. That is not evidence.
  3. **Input versus output.** A script that *reads* an existing .pptx to extract
     its content is not PPTX export. Export means the skill *produces* a .pptx.

For `quote`: copy the sentence the verdict rests on, verbatim, in its original
language. If the verdict is `unclear`, use the empty string.

Capabilities:

"""


def build_prompt() -> str:
    lines = []
    for name, spec in CAPABILITIES.items():
        lines.append(f"  {name}\n    {spec['label_en']} — {spec['why']}")
    return PROMPT_HEAD + "\n".join(lines) + "\n"


def read_docs_text(skill_dir: Path) -> list[tuple[str, str]]:
    docs, total = [], 0
    for name in DOC_NAMES:
        for path in sorted(skill_dir.rglob(name)):
            if any(p in path.parts for p in ("node_modules", ".git", "examples")):
                continue
            try:
                text = path.read_text(errors="replace")
            except OSError:
                continue
            if total + len(text) > MAX_DOC_CHARS:
                text = text[: max(0, MAX_DOC_CHARS - total)]
            if not text:
                continue
            docs.append((str(path.relative_to(skill_dir)).replace("/", "__"), text))
            total += len(text)
            if total >= MAX_DOC_CHARS:
                return docs
    return docs


def ask(docs: list[tuple[str, str]], prompt: str, model: str,
        budget: float) -> tuple[dict | None, float, int]:
    """Returns (verdicts, cost_usd, input_tokens).

    The cost comes back from the CLI on every call and used to be thrown away,
    which meant the only honest answer to "what will the rest of this cost" was
    a guess. It is recorded per skill now.
    """
    work = Path(tempfile.mkdtemp(prefix="cap-read-"))
    (work / "docs").mkdir()
    for name, text in docs:
        (work / "docs" / name).write_text(text)
    try:
        proc = subprocess.run(
            ["claude", "-p", prompt,
             "--setting-sources", "project", "--strict-mcp-config",
             "--permission-mode", "bypassPermissions", "--model", model,
             "--max-budget-usd", str(budget), "--no-session-persistence",
             "--json-schema", json.dumps(SCHEMA), "--output-format", "json"],
            cwd=work, capture_output=True, text=True, timeout=900,
        )
    except subprocess.TimeoutExpired:
        return None, 0.0, 0
    finally:
        shutil.rmtree(work, ignore_errors=True)

    if proc.returncode != 0:
        return None, 0.0, 0
    try:
        env = json.loads(proc.stdout)
    except json.JSONDecodeError:
        return None, 0.0, 0
    usage = env.get("usage") or {}
    tokens = (usage.get("input_tokens", 0)
              + usage.get("cache_creation_input_tokens", 0)
              + usage.get("cache_read_input_tokens", 0))
    # The schema-validated object is in `structured_output`; `result` is the
    # model's prose summary and reading it would discard every verdict.
    return env.get("structured_output"), env.get("total_cost_usd") or 0.0, tokens


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--only", nargs="*", help="limit to these skill ids")
    ap.add_argument("--model", default="sonnet")
    ap.add_argument("--budget", type=float, default=0.60, help="USD ceiling per skill")
    args = ap.parse_args()

    registry = json.loads((ROOT / "data" / "skills.json").read_text())
    existing = json.loads(OUT.read_text()) if OUT.exists() else {}
    prompt = build_prompt()

    result = {
        "$comment": (
            "Documented capabilities — what each project's own docs claim, with the "
            "sentence it claims it on. Read from the docs, not verified by running "
            "anything. 'unclear' means the documentation is silent, which is not the "
            "same as unsupported. Generated by scripts/read_capabilities.py."
        ),
        "capabilities": {k: {kk: v[kk] for kk in ("label_en", "label_zh", "why")}
                         for k, v in CAPABILITIES.items()},
        "skills": existing.get("skills", {}) if args.only else {},
    }

    targets = [s for s in registry["skills"]
               if not args.only or s["id"] in args.only]
    spent = 0.0
    read = 0
    for i, skill in enumerate(targets, 1):
        sid = skill["id"]
        repo_dir = CACHE / sid
        if not repo_dir.is_dir():
            print(f"[{i}/{len(targets)}] {sid}: not cloned, skipped", file=sys.stderr)
            continue
        skill_dir = resolve_skill_dir(sid, repo_dir, skill.get("path"))
        docs = read_docs_text(skill_dir)
        if not docs:
            print(f"[{i}/{len(targets)}] {sid}: no docs found", file=sys.stderr)
            continue

        verdicts, cost, tokens = ask(docs, prompt, args.model, args.budget)
        spent += cost
        read += 1
        if verdicts is None:
            print(f"[{i}/{len(targets)}] {sid}: read failed", file=sys.stderr)
            continue

        result["skills"][sid] = {
            "docs_read": [d[0].replace("__", "/") for d in docs],
            "runtime": detect_runtime(skill_dir),
            "cost_usd": round(cost, 4),
            "input_tokens": tokens,
            "caps": verdicts,
        }
        yes = sum(1 for v in verdicts.values() if v["verdict"] == "yes")
        no = sum(1 for v in verdicts.values() if v["verdict"] == "no")
        print(f"[{i}/{len(targets)}] {sid:24s} {yes} yes · {no} no · "
              f"{len(CAPABILITIES) - yes - no} unclear · "
              f"${cost:.3f} · {tokens:,} tok", flush=True)
        OUT.write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n")

    done = len(result["skills"])
    print(f"\nwrote {OUT.relative_to(ROOT)} — {done} skill(s)")
    print(f"spent ${spent:.2f} on this run across {read} read(s)")
    remaining = len(registry["skills"]) - done
    if remaining > 0 and read > 0:
        # Divide by what was actually read, not by len(targets). Most targets
        # bail out before ask() because they were never cloned, so averaging
        # over all of them understates the true per-skill price by the ratio
        # between the two -- and this number exists precisely to answer "what
        # will the rest cost", where being 50x low is worse than saying nothing.
        per = spent / read
        print(f"~${per:.3f}/skill measured — {remaining} left "
              f"would be about ${per * remaining:.2f}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
