#!/usr/bin/env python3
"""Validate data/skills.json before it reaches the generator.

The registry is the only hand-written data file, so it is the only place a typo
can silently corrupt every table in both READMEs. This catches that at PR time.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILLS = ROOT / "data" / "skills.json"
STATS = ROOT / "data" / "stats.json"

REQUIRED = ["id", "repo", "name", "route", "tagline_en", "tagline_zh"]
VALID_ROUTES = {"html", "pptx", "hybrid", "image", "suite",
                "framework", "templates", "list"}
VALID_LANG = {"en", "zh", "bilingual"}
VALID_MOTION_KINDS = {"pptx", "html", "video"}

# Words a project uses when it is talking about motion, in either language. Used
# only to answer one question: did *this project* raise the subject, or did we?
#
# Deliberately excludes "canvas": in this corpus it almost always means the fixed
# 1920x1080 stage, not a drawing surface being animated, and letting it in made
# the check pass for a skill whose docs say nothing about motion at all.
MOTION_WORDS = re.compile(
    r"anim|动画|动效|transition|转场|motion|gsap|three\.js|framer|"
    r"reveal|keyframe|video|视频|mp4|gif|webgl",
    re.I,
)

# GitHub's licence key vs. the prose we write in `license_note`. Only listed
# here when the two spellings differ enough that a substring test would fail.
LICENSE_ALIASES = {
    "NOASSERTION": {"custom", "unspecified", "see repo", "noassertion"},
    "Unlicense": {"unlicense", "public domain"},
}


def license_matches(note: str, api: str) -> bool:
    """Does the hand-written note still agree with what GitHub reports?"""
    note = (note or "").strip().lower()
    if not note:
        return True
    if api in LICENSE_ALIASES:
        return note in LICENSE_ALIASES[api]
    # "MIT" vs "MIT License", "AGPL-3.0" vs "⚠️ AGPL-3.0" — a prefix match on
    # the family is enough, and avoids churn over cosmetic spellings.
    return api.lower().split("-")[0] in note


def main() -> int:
    data = json.loads(SKILLS.read_text(encoding="utf-8"))
    stats = (json.loads(STATS.read_text(encoding="utf-8")).get("repos", {})
             if STATS.exists() else {})
    errors: list[str] = []
    warnings: list[str] = []

    caps_path = ROOT / "data" / "capabilities.json"
    caps = (json.loads(caps_path.read_text(encoding="utf-8"))
            if caps_path.exists() else {})

    def animation_verified(sid: str) -> bool:
        cell = ((caps.get("skills") or {}).get(sid, {}).get("caps", {})
                or {}).get("animation") or {}
        return isinstance(cell, dict) and cell.get("verdict") == "yes"

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

        # Pointing at a subdirectory means the star count on the row belongs to
        # the parent repo, not to the one skill we are linking. Saying so is the
        # whole argument of this registry, so it is enforced rather than trusted.
        if e.get("path") and e.get("stars_note") != "monorepo":
            errors.append(
                f"{label}: has `path` (links into a subdirectory) but no "
                "`stars_note: monorepo` — its stars are not this skill's"
            )

        # `license_note` is hand-written and drifts as upstream adds a LICENSE
        # file. stats.json already holds the authoritative answer, so compare.
        api_license = (stats.get(repo) or {}).get("license")
        if api_license and not license_matches(e.get("license_note", ""), api_license):
            warnings.append(
                f"{label}: license_note `{e.get('license_note')}` but GitHub "
                f"reports `{api_license}` — re-check and update the note"
            )

        for key in ("highlights_en", "highlights_zh"):
            if key in e and not isinstance(e[key], list):
                errors.append(f"{label}: `{key}` must be a list")

        # A `motion` note is prose *we* write, which makes it the one field in
        # here that can quietly become a claim nobody can trace. So it has to
        # rest on something: either the capability grid already recorded a
        # quote, or the project raised the subject itself in its own tagline or
        # highlights. A note about a project that never mentions motion is this
        # registry inventing a feature, and that is an error, not a warning.
        if (m := e.get("motion")) is not None:
            if not isinstance(m, dict):
                errors.append(f"{label}: `motion` must be an object")
            elif m.get("kind") not in VALID_MOTION_KINDS:
                errors.append(
                    f"{label}: motion.kind `{m.get('kind')}` not one of "
                    f"{sorted(VALID_MOTION_KINDS)}"
                )
            elif not (m.get("note_en") and m.get("note_zh")):
                errors.append(f"{label}: `motion` needs both note_en and note_zh")
            elif not animation_verified(e.get("id", "")):
                own = " ".join([
                    e.get("tagline_en", ""), e.get("tagline_zh", ""),
                    *e.get("highlights_en", []), *e.get("highlights_zh", []),
                ])
                if not MOTION_WORDS.search(own):
                    errors.append(
                        f"{label}: has a `motion` note, but neither "
                        "capabilities.json nor the project's own tagline/highlights "
                        "mention motion — the note has nothing behind it"
                    )

    # `pick.py list --route` builds its choices from ROUTE_NAME, so a route in
    # use here but missing there makes those skills unreachable from the CLI —
    # which is how `suite` and `image` went unqueryable for 18 entries.
    sys.path.insert(0, str(ROOT / "scripts"))
    from pick import ROUTE_NAME  # noqa: E402

    unlabelled = {e["route"] for e in data["skills"] if e.get("route")} - set(ROUTE_NAME)
    for r in sorted(unlabelled):
        errors.append(f"route `{r}` is used in skills.json but has no label in "
                      "pick.py ROUTE_NAME — `pick.py list --route` will reject it")

    # The capability grid is generated by read_capabilities.py, so it is checked
    # rather than corrected here — a hand edit would be overwritten on the next
    # run. Two things can go wrong that the generator cannot see on its own.
    if caps:
        vocab = set(caps.get("capabilities", {}))
        route_of = {e["id"]: e.get("route") for e in data["skills"]}
        for sid, entry in (caps.get("skills") or {}).items():
            if sid not in route_of:
                errors.append(f"capabilities.json has `{sid}`, absent from skills.json")
            for key, cell in (entry.get("caps") or {}).items():
                if key not in vocab:
                    errors.append(f"{sid}: capability `{key}` is not in the "
                                  "`capabilities` vocabulary")
                    continue
                if not isinstance(cell, dict):
                    continue
                # A `yes` or `no` is a claim about the project, so it must carry
                # the sentence it rests on — that is the grid's whole defence.
                if cell.get("verdict") in ("yes", "no") and not cell.get("quote"):
                    warnings.append(f"{sid}: `{key}` verdict `{cell['verdict']}` "
                                    "with no supporting quote")
            # self_contained is defined as an HTML-route question ("whether the
            # *delivered deck* runs with no CDN"), so a yes on a PPTX-only skill
            # means the reader matched a build artifact instead.
            sc = (entry.get("caps") or {}).get("self_contained") or {}
            if (isinstance(sc, dict) and sc.get("verdict") == "yes"
                    and route_of.get(sid) not in ("html", "hybrid", None)):
                warnings.append(
                    f"{sid}: `self_contained: yes` on a {route_of[sid]}-route skill — "
                    "that capability is defined for the HTML route only, and an "
                    "intermediate preview being self-contained does not count. "
                    "Re-run scripts/read_capabilities.py --only " + sid)

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
