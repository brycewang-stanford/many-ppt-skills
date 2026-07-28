#!/usr/bin/env python3
"""Search GitHub for slide/deck skills that are not in the registry yet.

Coverage is the whole point of a registry, and the two prior lists in this space
were both HTML-route-focused, so anything found only by searching "html slides"
inherits their blind spot. The query set below deliberately sweeps several
different angles — output format, agent vocabulary, and Chinese terms, since a
large share of this category is written in Chinese first.

    python scripts/discover.py                 # print candidates, write nothing
    python scripts/discover.py --json out.json # machine-readable

Requires `gh` to be authenticated (5000 req/hr instead of 60).

Output is *candidates*, not additions. Search matches things that merely mention
slides, so every row still needs a human to decide whether it is a skill, a
template pack, a full application, or noise.
"""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# Each angle catches things the others miss. "ppt" alone misses English-first
# projects; "presentation" alone misses the entire Chinese-language cluster;
# topic searches catch well-tagged repos that use none of the obvious words.
QUERIES = [
    "ppt skill", "pptx skill", "slide skill", "slides skill",
    "presentation skill", "deck skill", "ppt agent skill",
    "claude skill ppt", "claude skill slides", "agent skill presentation",
    "html slides skill", "html ppt", "ai ppt generator skill",
    "slide generation agent", "presentation generator claude",
    "PPT 技能", "幻灯片 skill", "PPT skill 中文", "演示文稿 skill",
    "topic:claude-skill ppt", "topic:claude-skills slides",
    "topic:agent-skills presentation", "topic:claude-code-skill slides",
    "topic:ppt-generator", "topic:slides",
    "markdown to pptx", "markdown to slides agent",
    "python-pptx skill", "pptxgenjs skill", "reveal.js skill",
    "beamer skill", "keynote skill agent",
]

# Obvious non-matches. Search for "slides" and GitHub cheerfully returns every
# lecture-notes repository ever pushed.
NOISE_WORDS = (
    "lecture", "course", "homework", "assignment", "my slides", "conference talk",
    "presentation for", "notes", "tutorial slides", "seminar",
)


def gh_search(query: str, per_page: int = 30) -> list[dict]:
    try:
        out = subprocess.run(
            ["gh", "api", "-X", "GET", "search/repositories",
             "-f", f"q={query}", "-f", "sort=stars", "-f", "order=desc",
             "-F", f"per_page={per_page}"],
            capture_output=True, text=True, timeout=60, check=True,
        ).stdout
    except (subprocess.CalledProcessError, subprocess.TimeoutExpired) as exc:
        print(f"  ! {query}: {exc}", file=sys.stderr)
        return []
    return json.loads(out).get("items", [])


def looks_like_noise(repo: dict) -> bool:
    blob = f"{repo['full_name']} {repo.get('description') or ''}".lower()
    return any(w in blob for w in NOISE_WORDS)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--json", type=Path)
    ap.add_argument("--min-stars", type=int, default=3)
    args = ap.parse_args()

    registry = json.loads((ROOT / "data" / "skills.json").read_text())
    known = {s["repo"].lower() for s in registry["skills"]}
    known |= {s["repo"].lower() for s in registry.get("lists", [])}

    found: dict[str, dict] = {}
    for q in QUERIES:
        items = gh_search(q)
        print(f"  {q:42s} {len(items):3d} hit(s)", file=sys.stderr)
        for r in items:
            name = r["full_name"]
            if name.lower() in known or r["stargazers_count"] < args.min_stars:
                continue
            if r.get("archived") or looks_like_noise(r):
                continue
            prev = found.get(name)
            if prev:
                prev["queries"].append(q)
                continue
            found[name] = {
                "repo": name,
                "stars": r["stargazers_count"],
                "forks": r["forks_count"],
                "description": (r.get("description") or "").strip(),
                "license": (r.get("license") or {}).get("spdx_id"),
                "pushed_at": (r.get("pushed_at") or "")[:10],
                "created_at": (r.get("created_at") or "")[:10],
                "topics": r.get("topics", []),
                "queries": [q],
            }

    ranked = sorted(found.values(), key=lambda c: -c["stars"])
    if args.json:
        args.json.write_text(json.dumps(ranked, indent=2, ensure_ascii=False) + "\n")

    print(f"\n{len(ranked)} candidate(s) not already in the registry\n")
    for c in ranked:
        print(f"{c['stars']:>7,}  {c['repo']}")
        if c["description"]:
            print(f"         {c['description'][:110]}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
