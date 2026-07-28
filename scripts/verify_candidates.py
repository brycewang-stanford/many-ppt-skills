#!/usr/bin/env python3
"""Decide which discovery candidates are actually agent skills.

`discover.py` searches text, so it returns presentation *frameworks* (reveal.js,
Slidev, Marp), web *applications* that generate decks, document converters, and
the occasional reading list. None of those belong in a registry of skills, and
sorting them by hand across 300 rows is where a curated list starts rotting.

The objective test is whether the repository ships a `SKILL.md`. That is the
file an agent actually loads, and it is what makes something a skill rather than
a tool a human drives.

    python scripts/verify_candidates.py --in candidates.json --out verified.json

Repos are classified, never silently dropped — a framework that got filtered out
is recorded as a framework, so the next person does not re-research it.
"""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def gh(endpoint: str) -> dict | None:
    try:
        out = subprocess.run(["gh", "api", endpoint], capture_output=True,
                             text=True, timeout=45).stdout
        return json.loads(out) if out.strip() else None
    except (subprocess.SubprocessError, json.JSONDecodeError):
        return None


def classify(repo: str) -> dict:
    """One tree listing per repo tells us everything we need."""
    meta = gh(f"repos/{repo}")
    if not meta:
        return {"kind": "unreachable"}
    branch = meta.get("default_branch", "main")

    tree = gh(f"repos/{repo}/git/trees/{branch}?recursive=1")
    if not tree or "tree" not in tree:
        return {"kind": "unreachable", "default_branch": branch}

    paths = [t["path"] for t in tree["tree"] if t["type"] == "blob"]
    skill_files = [p for p in paths
                   if p.split("/")[-1].upper() == "SKILL.MD"
                   and "node_modules" not in p]

    if not skill_files:
        return {
            "kind": "not-a-skill",
            "default_branch": branch,
            "truncated": tree.get("truncated", False),
            "file_count": len(paths),
        }

    # A repo holding many SKILL.md files is a collection; one is a single skill.
    # Both are worth listing, but they are different things and the registry
    # already distinguishes them.
    return {
        "kind": "skill-collection" if len(skill_files) > 3 else "skill",
        "default_branch": branch,
        "skill_files": skill_files[:12],
        "skill_count": len(skill_files),
        "has_python": any(p.endswith(".py") for p in paths),
        "has_node": any(p.endswith("package.json") for p in paths),
        "file_count": len(paths),
    }


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--in", dest="src", required=True, type=Path)
    ap.add_argument("--out", required=True, type=Path)
    ap.add_argument("--limit", type=int, default=400)
    args = ap.parse_args()

    candidates = json.loads(args.src.read_text())[: args.limit]
    results = []
    for i, c in enumerate(candidates, 1):
        info = classify(c["repo"])
        results.append({**c, **info})
        mark = {"skill": "SKILL", "skill-collection": "COLL"}.get(info["kind"], "  · ")
        print(f"[{i:3d}/{len(candidates)}] {mark} {c['stars']:>6,}  {c['repo']}",
              file=sys.stderr, flush=True)
        args.out.write_text(json.dumps(results, indent=2, ensure_ascii=False) + "\n")

    kinds: dict[str, int] = {}
    for r in results:
        kinds[r["kind"]] = kinds.get(r["kind"], 0) + 1
    print("\nclassification:")
    for k, v in sorted(kinds.items(), key=lambda kv: -kv[1]):
        print(f"  {k:20s} {v}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
