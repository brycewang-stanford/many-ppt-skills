#!/usr/bin/env python3
"""Validate data/skills.json before it reaches the generator.

The registry is the only hand-written data file, so it is the only place a typo
can silently corrupt every table in both READMEs. This catches that at PR time.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILLS = ROOT / "data" / "skills.json"

REQUIRED = ["id", "repo", "name", "route", "tagline_en", "tagline_zh"]
VALID_ROUTES = {"html", "pptx", "hybrid", "image", "suite",
                "framework", "templates", "list"}
VALID_LANG = {"en", "zh", "bilingual"}


def main() -> int:
    data = json.loads(SKILLS.read_text(encoding="utf-8"))
    errors: list[str] = []
    warnings: list[str] = []

    entries = data["skills"] + data.get("lists", [])
    seen_ids: dict[str, str] = {}
    seen_repos: dict[str, str] = {}

    for e in entries:
        label = e.get("id") or e.get("repo") or "<unnamed entry>"

        for field in REQUIRED:
            if field == "tagline_zh" and e in data.get("lists", []):
                continue  # list entries carry lighter metadata
            if not e.get(field):
                errors.append(f"{label}: missing required field `{field}`")

        if e.get("route") and e["route"] not in VALID_ROUTES:
            errors.append(
                f"{label}: route `{e['route']}` not one of {sorted(VALID_ROUTES)}"
            )

        if e.get("lang") and e["lang"] not in VALID_LANG:
            errors.append(f"{label}: lang `{e['lang']}` not one of {sorted(VALID_LANG)}")

        repo = e.get("repo", "")
        if repo.count("/") != 1:
            errors.append(f"{label}: repo `{repo}` must be exactly owner/name")
        if repo.startswith("http"):
            errors.append(f"{label}: repo must be owner/name, not a URL")

        # Duplicate ids would silently collapse rows; duplicate repos are
        # legitimate only when one entry points at a subpath of a monorepo.
        if (i := e.get("id")) in seen_ids:
            errors.append(f"duplicate id `{i}` (also on {seen_ids[i]})")
        elif i:
            seen_ids[i] = label

        if repo in seen_repos and not e.get("path"):
            errors.append(f"duplicate repo `{repo}` (also on {seen_repos[repo]})")
        elif repo:
            seen_repos.setdefault(repo, label)

        if e.get("license_note", "").upper().startswith("AGPL") and not e.get(
            "license_warning"
        ):
            warnings.append(
                f"{label}: AGPL license without `license_warning: true` — "
                "readers should be flagged before commercial use"
            )

        for key in ("highlights_en", "highlights_zh"):
            if key in e and not isinstance(e[key], list):
                errors.append(f"{label}: `{key}` must be a list")

    for w in warnings:
        print(f"  warning: {w}", file=sys.stderr)
    for err in errors:
        print(f"  ERROR: {err}", file=sys.stderr)

    print(
        f"{len(data['skills'])} skills + {len(data.get('lists', []))} lists checked — "
        f"{len(errors)} error(s), {len(warnings)} warning(s)"
    )
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
