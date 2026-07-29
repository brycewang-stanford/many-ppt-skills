#!/usr/bin/env python3
"""Keep the packaged copy of SKILL.md identical to the canonical one.

The repository is installable two ways, and they want the file in two places:

  * `git clone ... ~/.claude/skills/many-ppt-skills` reads `SKILL.md` at the root
  * `/plugin marketplace add` reads `skills/<name>/SKILL.md`

The root file is canonical and hand-edited; the packaged one is a copy. Two
hand-maintained copies of the same document is precisely the failure this
repository exists to complain about, so the copy is generated and CI fails if
someone edits one and not the other.

    python scripts/sync_plugin.py           # write the copy
    python scripts/sync_plugin.py --check   # exit 1 if it has drifted
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CANONICAL = ROOT / "SKILL.md"
PACKAGED = ROOT / "skills" / "many-ppt-skills" / "SKILL.md"

BANNER = (
    "<!-- Generated from the SKILL.md at the repository root by\n"
    "     scripts/sync_plugin.py. Edit that file, not this copy. -->\n\n"
)


def build() -> str:
    text = CANONICAL.read_text(encoding="utf-8")
    # The banner goes after the YAML front matter, which must stay on line 1.
    if text.startswith("---\n"):
        end = text.find("\n---\n", 4)
        if end != -1:
            head, body = text[: end + 5], text[end + 5:]
            return head + "\n" + BANNER + body.lstrip("\n")
    return BANNER + text


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true")
    args = ap.parse_args()

    if not CANONICAL.exists():
        print("SKILL.md missing at the repository root", file=sys.stderr)
        return 1

    want = build()
    have = PACKAGED.read_text(encoding="utf-8") if PACKAGED.exists() else None

    if have == want:
        print(f"  = {PACKAGED.relative_to(ROOT)} already current")
        return 0
    if args.check:
        what = "out of date" if have is not None else "missing"
        print(f"{PACKAGED.relative_to(ROOT)} is {what} — "
              "run `python scripts/sync_plugin.py`", file=sys.stderr)
        return 1

    PACKAGED.parent.mkdir(parents=True, exist_ok=True)
    PACKAGED.write_text(want, encoding="utf-8")
    print(f"  ✎ {PACKAGED.relative_to(ROOT)} updated")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
