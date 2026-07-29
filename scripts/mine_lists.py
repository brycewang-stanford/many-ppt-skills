#!/usr/bin/env python3
"""Mine curated skill lists for repositories GitHub search did not surface.

Search saturates. Three waves and 137 queries returned 377 candidates, and the
third wave contributed 8 of them — at that point the remaining coverage is not
behind another query, it is behind somebody else's list.

This walks the markdown of known skill directories, pulls every GitHub link with
the line it sits on, and keeps the ones whose surrounding text is about slides.
The line matters: these lists catalogue every kind of agent skill, so a bare repo
URL carries no signal, while "**deck-builder** — turns a brief into a slide deck"
carries plenty.

    python scripts/mine_lists.py --out mined.json

Output feeds the same funnel as discover.py: verify_candidates.py checks for a
SKILL.md, then classification decides whether slides are the actual job. Nothing
here is trusted enough to enter the registry directly.
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# Directories worth walking. The two PPT-specific ones are small but dense; the
# general ones are huge and mostly irrelevant, which the line filter handles.
SOURCE_LISTS = [
    "VoltAgent/awesome-agent-skills",
    "ComposioHQ/awesome-claude-skills",
    "travisvn/awesome-claude-skills",
    "BehiSecc/awesome-claude-skills",
    "libukai/awesome-agent-skills",
    "heilcheng/awesome-agent-skills",
    "helloianneo/awesome-claude-code-skills",
    "chujianyun/awesome-gpt-image2-ppt-skills",
    "stevenjinlong/awesome-ppt-skills",
    "KerberosClaw/kc_ai_skills",
    "KKKKhazix/khazix-skills",
    "rohitg00/awesome-claude-code-toolkit",
    "ToseaAI/awesome-html-slide-skills",
    "software-ai-life/Awesome-PPT-Design-Skills",
]

REPO_LINK = re.compile(r"https?://github\.com/([A-Za-z0-9_.-]+)/([A-Za-z0-9_.-]+)")

# The line has to be about slides. Deliberately broad — a false positive costs
# one wasted SKILL.md check, a false negative loses a project permanently.
SLIDE_WORDS = (
    "slide", "slides", "deck", "decks", "presentation", "presentations",
    "powerpoint", "pptx", "ppt", "keynote", "reveal.js", "marp", "slidev",
    "beamer", "幻灯", "演示", "簡報", "投影片", "汇报", "答辩", "路演", "演講",
)

# Owners whose repos are the list itself, or infrastructure around it.
SKIP_OWNERS = {"github", "shields", "img", "raw", "gist", "sponsors"}


def gh_markdown(repo: str) -> list[tuple[str, str]]:
    """Every markdown file in a repo, as (path, text)."""
    meta = subprocess.run(["gh", "api", f"repos/{repo}"], capture_output=True,
                          text=True, timeout=45)
    if meta.returncode != 0:
        print(f"  ! {repo}: unreachable", file=sys.stderr)
        return []
    branch = json.loads(meta.stdout).get("default_branch", "main")

    tree = subprocess.run(["gh", "api", f"repos/{repo}/git/trees/{branch}?recursive=1"],
                          capture_output=True, text=True, timeout=60)
    if tree.returncode != 0:
        return []
    paths = [t["path"] for t in json.loads(tree.stdout).get("tree", [])
             if t["type"] == "blob" and t["path"].lower().endswith(".md")][:25]

    out = []
    for p in paths:
        raw = subprocess.run(
            ["gh", "api", f"repos/{repo}/contents/{p}",
             "-H", "Accept: application/vnd.github.raw"],
            capture_output=True, text=True, timeout=45)
        if raw.returncode == 0 and raw.stdout:
            out.append((p, raw.stdout))
    return out


def harvest(text: str) -> dict[str, str]:
    """repo -> the line that mentioned it, for lines that are about slides."""
    found: dict[str, str] = {}
    for line in text.splitlines():
        low = line.lower()
        if not any(w in low for w in SLIDE_WORDS):
            continue
        for owner, name in REPO_LINK.findall(line):
            if owner.lower() in SKIP_OWNERS:
                continue
            name = name.rstrip(".git")
            found.setdefault(f"{owner}/{name}", line.strip()[:200])
    return found


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", required=True, type=Path)
    ap.add_argument("--exclude", nargs="*", type=Path, default=[],
                    help="candidate files whose repos are already known")
    args = ap.parse_args()

    registry = json.loads((ROOT / "data" / "skills.json").read_text())
    known = {s["repo"].lower() for s in registry["skills"]}
    known |= {s["repo"].lower() for s in registry.get("lists", [])}
    for f in args.exclude:
        if f.exists():
            known |= {c["repo"].lower() for c in json.loads(f.read_text())}

    mined: dict[str, dict] = {}
    for src in SOURCE_LISTS:
        docs = gh_markdown(src)
        hits = {}
        for path, text in docs:
            hits.update(harvest(text))
        fresh = {r: line for r, line in hits.items() if r.lower() not in known}
        print(f"  {src:48s} {len(docs):2d} md · {len(hits):4d} slide links · "
              f"{len(fresh):3d} new", file=sys.stderr, flush=True)
        for repo, line in fresh.items():
            if repo in mined:
                mined[repo]["sources"].append(src)
            else:
                mined[repo] = {"repo": repo, "context": line, "sources": [src]}

    out = sorted(mined.values(), key=lambda m: -len(m["sources"]))
    args.out.write_text(json.dumps(out, indent=2, ensure_ascii=False) + "\n")
    print(f"\n{len(out)} repo(s) not already known, mined from "
          f"{len(SOURCE_LISTS)} lists")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
