#!/usr/bin/env python3
"""Query the registry: which slide skill, and which style.

This is the lookup layer behind SKILL.md. It exists so an agent can answer
"which one, and what do I call the style" by running one command, instead of
reading three JSON files totalling ~200KB into its context — the repository's
own principle 5, applied to itself.

Everything printed here is read from data/. Nothing is inferred, and nothing
about how to *invoke* another project is asserted: that belongs to each
project's own SKILL.md and is the one thing this registry cannot verify.

    python scripts/pick.py route                 # the HTML vs PPTX decision
    python scripts/pick.py list --route pptx --ready   # installable, one route
    python scripts/pick.py show ppt-master       # one skill, in full
    python scripts/pick.py styles frontend-slides
    python scripts/pick.py find editorial        # search styles and blurbs
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"

# What each install method actually does. Duplicated in scripts/render.py for
# the README table; kept here because the agent reading this output is usually
# not the one reading the README, and "install it" without this is the step
# people get wrong.
INSTALL_NOTE = {
    "clone": "clones into ~/.claude/skills/ — restart the session to pick it up",
    "plugin": "type these INSIDE Claude Code, not in a terminal",
    "skills-cli": "agent-agnostic installer, works outside Claude Code too",
    "python": "needs Python locally; install deps, then point your agent at the clone",
    "npx": "scaffolds a project rather than installing a skill",
}

# Every route value that appears in data/skills.json needs an entry here: the
# key set is also what `list --route` will accept, so a missing one silently
# makes those skills unreachable from the CLI. validate_registry.py enforces it.
ROUTE_NAME = {
    "html": "HTML-native", "pptx": "native PPTX", "hybrid": "both routes",
    "suite": "skill suite", "image": "image-first",
    "framework": "framework", "templates": "template library",
}


def load(name: str) -> dict:
    path = DATA / name
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def registry() -> tuple[list[dict], dict, dict, dict]:
    skills = load("skills.json").get("skills", [])
    stats = load("stats.json").get("repos", {})
    samples = load("samples.json").get("skills", {})
    caps = load("capabilities.json")
    return skills, stats, samples, caps


def stars(skill: dict, stats: dict) -> int:
    return (stats.get(skill["repo"]) or {}).get("stars", 0)


def by_id(skills: list[dict], sid: str) -> dict | None:
    for s in skills:
        if s["id"] == sid:
            return s
    # Tolerate a repo name or a display name, since an agent may have either.
    low = sid.lower()
    for s in skills:
        if low in (s["repo"].lower(), s["name"].lower()):
            return s
    return None


def installable(skill: dict) -> bool:
    """True when this registry actually knows how to install the skill.

    177 of the entries came from the automated discovery sweep and carry no
    install command. They are worth listing, but recommending one as *the*
    answer leaves the user with nothing to run.
    """
    return bool((skill.get("install") or {}).get("command"))


def style_ids(entry: dict) -> list[str]:
    out: list[str] = []
    for s in entry.get("samples", []):
        st = s.get("style")
        if st and st not in out:
            out.append(st)
    return out


# --------------------------------------------------------------------------
# Commands
# --------------------------------------------------------------------------

def cmd_route(args, skills, stats, samples, caps) -> int:
    print("""\
The one question that decides it:

    Will anyone need to open your deliverable in PowerPoint and edit it?

  YES -> native PPTX route
         The recipient edits normally. Design ceiling is bounded by OOXML.
         Start with: ppt-master

  NO  -> HTML-native route
         One .html file presented in a browser. Much higher design ceiling,
         plain-text diffs, but the recipient cannot edit it in Office.
         Start with: frontend-slides

Ask the user this before recommending anything. It is not about taste, and
guessing it wrong makes every later recommendation wrong.""")
    counts: dict[str, int] = {}
    for s in skills:
        counts[s["route"]] = counts.get(s["route"], 0) + 1
    print("\nTracked: " + ", ".join(
        f"{n} {ROUTE_NAME.get(r, r)}" for r, n in sorted(counts.items(), key=lambda kv: -kv[1])))
    return 0


def cmd_list(args, skills, stats, samples, caps) -> int:
    rows = sorted(skills, key=lambda s: -stars(s, stats))
    if args.route:
        rows = [s for s in rows if s["route"] == args.route]
    if args.ready:
        rows = [s for s in rows if (s.get("install") or {}).get("command")]
    if args.limit:
        rows = rows[: args.limit]
    if not rows:
        print("no skills match that filter", file=sys.stderr)
        return 1

    for s in rows:
        n = len((samples.get(s["id"]) or {}).get("samples", []))
        img = f"{n} samples" if n else "no samples"
        mark = "" if installable(s) else " †"
        print(f"{s['id']:26s} {stars(s, stats):>7,}*  {ROUTE_NAME.get(s['route'], s['route']):<14} {img}{mark}")
        print(f"{'':26s} {s['tagline_en']}")
    unread = sum(1 for s in rows if not installable(s))
    print(f"\n{len(rows)} skill(s). `pick.py show <id>` for install command and styles.")
    if unread:
        print(f"† {unread} of them came from automated discovery — listed, but not yet "
              "read by hand, so there is no install command for them.")
        print("  Do not recommend a † entry as the answer; `list --ready` hides them.")
    return 0


def cmd_show(args, skills, stats, samples, caps) -> int:
    s = by_id(skills, args.skill)
    if not s:
        print(f"unknown skill: {args.skill} — try `pick.py list`", file=sys.stderr)
        return 1

    print(f"{s['name']}  ({s['id']})")
    print(f"  repo      https://github.com/{s['repo']}")
    print(f"  stars     {stars(s, stats):,}")
    print(f"  route     {ROUTE_NAME.get(s['route'], s['route'])}")
    print(f"  license   {s.get('license_note', '—')}"
          + ("   ** copyleft, check before commercial use **"
             if s.get("license_warning") else ""))
    print(f"  what      {s['tagline_en']}")
    print(f"  best for  {s.get('best_for_en', '—')}")

    install = s.get("install") or {}
    if install.get("command"):
        note = INSTALL_NOTE.get(install.get("method", ""), "")
        print(f"\n  install ({install.get('method')}) — {note}")
        for line in install["command"].splitlines():
            print(f"      {line}")
    else:
        # Silence here reads as "no install needed", which is wrong. Say plainly
        # that the gap is in this registry, not in the project.
        print("\n  install   NOT RECORDED. This entry came from the automated")
        print("            discovery sweep — the tagline and licence above are")
        print("            read from the repository, but nobody has read its")
        print("            SKILL.md yet. Get the command from the repo itself:")
        print(f"            https://github.com/{s['repo']}")

    entry = samples.get(s["id"]) or {}
    ids = style_ids(entry)
    if ids:
        print(f"\n  style ids ({len(ids)}), as the project itself names them:")
        for chunk in (ids[i:i + 4] for i in range(0, len(ids), 4)):
            print("      " + "  ".join(f"{c:22s}" for c in chunk).rstrip())
        print("      -> name one of these when you ask for a deck")

    entry_caps = (caps.get("skills", {}).get(s["id"]) or {}).get("caps", {})
    claimed = [k for k, v in entry_caps.items()
               if isinstance(v, dict) and v.get("verdict") == "yes"]
    if claimed:
        labels = caps.get("capabilities", {})
        print("\n  documented capabilities (what its docs claim, not tested here):")
        print("      " + ", ".join(labels.get(c, {}).get("label_en", c) for c in claimed))

    print("\n  NOTE: how to phrase the request is defined by this project's own")
    print("        SKILL.md, not by this registry. Read it if the style id alone")
    print("        does not get you what you want.")
    return 0


def cmd_styles(args, skills, stats, samples, caps) -> int:
    s = by_id(skills, args.skill)
    if not s:
        print(f"unknown skill: {args.skill}", file=sys.stderr)
        return 1
    entry = samples.get(s["id"]) or {}
    picks = entry.get("samples", [])
    if not picks:
        print(f"{s['name']} ships no sample imagery in its repo.")
        return 0

    print(f"{s['name']} — {len(picks)} samples, "
          f"{len(style_ids(entry))} distinct style ids\n")
    for p in picks:
        st = p.get("style") or "—"
        label = p.get("label") or ""
        print(f"  {st:24s} {label[:52]}")
        print(f"  {'':24s} {p['url']}")
    return 0


def cmd_find(args, skills, stats, samples, caps) -> int:
    q = args.text.lower()
    hits: list[tuple[int, dict, list[str]]] = []
    for s in skills:
        entry = samples.get(s["id"]) or {}
        ids = style_ids(entry)
        matched = [i for i in ids if q in i]
        score = len(matched) * 2
        blurb = " ".join(str(s.get(k, "")) for k in
                         ("tagline_en", "tagline_zh", "best_for_en", "name", "id"))
        if q in blurb.lower():
            score += 1
        if score:
            hits.append((score, s, matched))

    if not hits:
        print(f"nothing matches {args.text!r}", file=sys.stderr)
        return 1
    for _, s, matched in sorted(hits, key=lambda h: -h[0]):
        print(f"{s['id']:26s} {ROUTE_NAME.get(s['route'], s['route']):<14} "
              f"{stars(s, stats):>7,}*")
        if matched:
            print(f"{'':26s} styles: " + ", ".join(matched[:8]))
        else:
            print(f"{'':26s} {s['tagline_en'][:70]}")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    sub = ap.add_subparsers(dest="cmd", required=True)

    sub.add_parser("route", help="the HTML vs PPTX decision, asked first")

    p = sub.add_parser("list", help="skills, most-starred first")
    p.add_argument("--route", choices=sorted(ROUTE_NAME))
    p.add_argument("--limit", type=int)
    p.add_argument("--ready", action="store_true",
                   help="only entries with a recorded install command")

    p = sub.add_parser("show", help="one skill: install command, styles, capabilities")
    p.add_argument("skill")

    p = sub.add_parser("styles", help="every style id and sample image for one skill")
    p.add_argument("skill")

    p = sub.add_parser("find", help="search style ids and descriptions")
    p.add_argument("text")

    args = ap.parse_args()
    skills, stats, samples, caps = registry()
    if not skills:
        print("data/skills.json missing or empty", file=sys.stderr)
        return 1

    return {
        "route": cmd_route, "list": cmd_list, "show": cmd_show,
        "styles": cmd_styles, "find": cmd_find,
    }[args.cmd](args, skills, stats, samples, caps)


if __name__ == "__main__":
    raise SystemExit(main())
