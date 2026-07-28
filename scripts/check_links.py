#!/usr/bin/env python3
"""Verify every relative markdown link in the repo resolves to a real file.

Only internal links are checked. External URLs are deliberately left alone —
network checks in CI are flaky, and a 404 on someone else's site is not a
reason to fail this repo's build.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parent.parent

LINK = re.compile(r"\[[^\]]*\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)")
SKIP_PREFIXES = ("http://", "https://", "mailto:", "#", "data:")
SKIP_DIRS = {".git", "node_modules", "__pycache__", ".venv"}


def anchors_in(path: Path) -> set[str]:
    """GitHub's heading -> anchor slugging, close enough for our own headings."""
    out: set[str] = set()
    for line in path.read_text(encoding="utf-8", errors="replace").splitlines():
        if not line.startswith("#"):
            continue
        title = line.lstrip("#").strip()
        slug = re.sub(r"[^\w\s-]", "", title.lower())
        slug = re.sub(r"[\s_]+", "-", slug).strip("-")
        if slug:
            out.add(slug)
    return out


def main() -> int:
    md_files = [
        p
        for p in ROOT.rglob("*.md")
        if not any(part in SKIP_DIRS for part in p.parts)
    ]

    broken: list[str] = []
    checked = 0

    for md in md_files:
        text = md.read_text(encoding="utf-8", errors="replace")
        for raw in LINK.findall(text):
            if raw.startswith(SKIP_PREFIXES):
                continue

            target, _, frag = raw.partition("#")
            if not target:
                continue

            checked += 1
            dest = (md.parent / unquote(target)).resolve()

            if not dest.exists():
                broken.append(f"{md.relative_to(ROOT)} -> {raw}  (no such path)")
                continue

            if frag and dest.suffix == ".md":
                if frag.lower() not in anchors_in(dest):
                    broken.append(
                        f"{md.relative_to(ROOT)} -> {raw}  (no heading #{frag})"
                    )

    for b in broken:
        print(f"  BROKEN: {b}", file=sys.stderr)

    print(f"{checked} internal link(s) across {len(md_files)} file(s) — {len(broken)} broken")
    return 1 if broken else 0


if __name__ == "__main__":
    raise SystemExit(main())
