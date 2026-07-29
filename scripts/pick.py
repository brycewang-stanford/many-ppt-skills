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
    python scripts/pick.py installed             # what the user already has
    python scripts/pick.py caps                  # requirements you can filter on
    python scripts/pick.py list --route pptx --ready --cap speaker_notes
    python scripts/pick.py compare ppt-master frontend-slides
    python scripts/pick.py show ppt-master --why # one skill, with the evidence
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

# Which language the project's own documentation is written in. It decides
# whether the user can read the trigger phrases they are being handed off to.
LANG_NAME = {"en": "English", "zh": "Chinese", "bilingual": "English + Chinese"}


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


def cap_verdicts(sid: str, caps: dict) -> dict[str, dict]:
    """This skill's capability verdicts, or {} if nobody has read its docs.

    Three verdicts, and the difference matters when recommending: `yes` and
    `no` are both things the project's own documentation says, `unclear` only
    means the docs are silent — never that the feature is absent.
    """
    entry = caps.get("skills", {}).get(sid) or {}
    return {k: v for k, v in (entry.get("caps") or {}).items() if isinstance(v, dict)}


def claims(sid: str, caps: dict, verdict: str = "yes") -> list[str]:
    return [k for k, v in cap_verdicts(sid, caps).items() if v.get("verdict") == verdict]


def cap_label(key: str, caps: dict) -> str:
    return (caps.get("capabilities", {}).get(key) or {}).get("label_en", key)


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
        rows = [s for s in rows if installable(s)]
    if args.lang:
        # zh-only documentation is a real handover problem, not a detail: the
        # user ends up reading trigger phrases they cannot read. `bilingual`
        # satisfies either request.
        rows = [s for s in rows
                if s.get("lang") in (args.lang, "bilingual")]
    if args.cap:
        # Only the 30 hand-read skills have verdicts at all, so this filter
        # implicitly restricts to those. That is the honest behaviour: a
        # requirement can only be checked where someone checked it.
        rows = [s for s in rows
                if all(c in claims(s["id"], caps) for c in args.cap)]
    if args.limit:
        rows = rows[: args.limit]
    if not rows:
        print("no skills match that filter", file=sys.stderr)
        if args.cap:
            print("Capability filters only match the skills whose docs have been "
                  "read by hand — try fewer --cap flags, or `pick.py caps` to see "
                  "how many skills document each one.", file=sys.stderr)
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
    print(f"  docs in   {LANG_NAME.get(s.get('lang', ''), '—')}")

    # Hard prerequisites, from two sources: `requires` is hand-recorded from the
    # project's install instructions, `runtime` is what reading its docs turned
    # up. Both are the difference between an install that works and one that
    # half-works, so they go above the command, not in a footnote.
    entry_caps = caps.get("skills", {}).get(s["id"]) or {}
    needs = list(s.get("requires") or []) + [
        r for r in (entry_caps.get("runtime") or [])
        if not any(r.lower() in q.lower() for q in (s.get("requires") or []))
    ]
    if needs:
        print(f"  requires  {', '.join(needs)}")

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

    hl = s.get("highlights_en") or []
    if hl:
        print("\n  what its docs single out:")
        for h in hl[:4]:
            print(f"      - {h if len(h) < 96 else h[:93] + '...'}")

    verdicts = cap_verdicts(s["id"], caps)
    if verdicts:
        print("\n  capabilities as its own docs describe them (not tested here):")
        for verdict, gloss in (("yes", "documented"),
                               ("no", "documented as NOT supported"),
                               ("unclear", "docs silent — not the same as absent")):
            hits = [k for k, v in verdicts.items() if v.get("verdict") == verdict]
            if hits:
                print(f"      {verdict:8s} {', '.join(cap_label(k, caps) for k in hits)}")
                if verdict != "yes":
                    print(f"      {'':8s} ({gloss})")
        if args.why:
            print("\n  the quote each claim rests on:")
            for k, v in verdicts.items():
                if v.get("verdict") in ("yes", "no") and v.get("quote"):
                    print(f"      {cap_label(k, caps)} [{v['verdict']}]")
                    print(f"        \"{v['quote'][:160]}\"")
        else:
            print("      -> `show --why` prints the quote each claim rests on")
    else:
        print("\n  capabilities NOT ASSESSED — nobody has read this project's docs")
        print("      for this registry. Absence here says nothing about the project.")

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


def cmd_caps(args, skills, stats, samples, caps) -> int:
    """The requirement vocabulary, so the agent knows what it can ask about."""
    labels = caps.get("capabilities", {})
    if not labels:
        print("data/capabilities.json missing or empty", file=sys.stderr)
        return 1

    assessed = [s for s in skills if cap_verdicts(s["id"], caps)]
    print(f"Requirements you can filter on. {len(assessed)} of {len(skills)} skills\n"
          f"have had their docs read; the rest cannot be filtered at all.\n")
    for key, meta in labels.items():
        yes = sum(1 for s in assessed if key in claims(s["id"], caps))
        no = sum(1 for s in assessed if key in claims(s["id"], caps, "no"))
        print(f"  {key:20s} {meta.get('label_en', key)}")
        print(f"  {'':20s} {yes} document it, {no} document its absence, "
              f"{len(assessed) - yes - no} are silent")
        print(f"  {'':20s} why it matters: {meta.get('why', '—')}")
    print("\n  pick.py list --cap speaker_notes --cap native_charts --ready")
    print("  -> ask the user which of these they actually need before filtering.")
    print("     Filtering on a requirement they do not have throws away good")
    print("     skills whose docs simply did not mention it.")
    return 0


def cmd_compare(args, skills, stats, samples, caps) -> int:
    """Side by side, for when more than one candidate survived the route test."""
    picked: list[dict] = []
    for sid in args.skills:
        s = by_id(skills, sid)
        if not s:
            print(f"unknown skill: {sid} — try `pick.py list`", file=sys.stderr)
            return 1
        picked.append(s)

    w = 24
    def row(label: str, values: list[str]) -> None:
        print(f"  {label:16s}" + "".join(f"{v[:w - 2]:{w}s}" for v in values))

    print()
    row("", [s["id"] for s in picked])
    row("", ["-" * (w - 3) for _ in picked])
    row("stars", [f"{stars(s, stats):,}" for s in picked])
    row("route", [ROUTE_NAME.get(s["route"], s["route"]) for s in picked])
    row("license", [(s.get("license_note") or "—")
                    + (" (copyleft)" if s.get("license_warning") else "")
                    for s in picked])
    row("docs in", [LANG_NAME.get(s.get("lang", ""), "—") for s in picked])
    row("install", [((s.get("install") or {}).get("method") or "NOT RECORDED")
                    for s in picked])
    row("requires", [", ".join(s.get("requires") or []) or "—" for s in picked])
    row("styles", [str(len(style_ids(samples.get(s["id"]) or {}))) or "0"
                   for s in picked])

    labels = caps.get("capabilities", {})
    if labels:
        print()
        for key, meta in labels.items():
            cells = []
            for s in picked:
                v = cap_verdicts(s["id"], caps).get(key) or {}
                cells.append({"yes": "yes", "no": "NO", "unclear": "?"}
                             .get(v.get("verdict"), "not read"))
            if set(cells) == {"not read"}:
                continue
            row(meta.get("label_en", key)[:15], cells)
        print("\n  yes = its docs say so   NO = its docs say it does not")
        print("  ?   = docs silent, which is not the same as absent")
        print("  not read = nobody has assessed this project for the registry")

    print("\n  `pick.py show <id> --why` for install commands and the quotes.")
    return 0


# Where the deck skills in this registry land once installed. Checked in this
# order; a plugin install and a clone can both be present.
INSTALL_ROOTS = (
    "~/.claude/skills", "~/.claude/plugins", ".claude/skills", ".claude/plugins",
)


def cmd_installed(args, skills, stats, samples, caps) -> int:
    """Which registry skills are already on this machine.

    SKILL.md says to step aside if the user already has a deck skill they are
    happy with. That instruction needs a way to find out, and guessing from the
    conversation is how an agent ends up re-installing what is already there.
    """
    # Ids first, and they win: 12 repo basenames are shared by two or three
    # entries (forks and copies of ppt-master, frontend-slides and friends), so
    # a basename match on those would confidently name the wrong project. Drop
    # the ambiguous ones rather than picking whichever came last.
    names: dict[str, dict] = {s["id"].lower(): s for s in skills}
    basenames: dict[str, list[dict]] = {}
    for s in skills:
        basenames.setdefault(s["repo"].split("/")[-1].lower(), []).append(s)
    for base, owners in basenames.items():
        if len(owners) == 1 and base not in names:
            names[base] = owners[0]

    found: dict[str, list[str]] = {}
    roots_seen: list[str] = []
    for root in INSTALL_ROOTS:
        p = Path(root).expanduser()
        if not p.is_dir():
            continue
        roots_seen.append(str(p))
        # Skill directories sit one or two levels down: ~/.claude/skills/<name>,
        # and ~/.claude/plugins/<plugin>/skills/<name> for a plugin install.
        candidates = [c for c in p.iterdir() if c.is_dir()]
        for c in list(candidates):
            nested = c / "skills"
            if nested.is_dir():
                candidates += [g for g in nested.iterdir() if g.is_dir()]
        for child in candidates:
            hit = names.get(child.name.lower())
            if hit:
                found.setdefault(hit["id"], []).append(str(child))

    if not roots_seen:
        print("None of the usual skill directories exist here, so nothing is")
        print("installed for this user — or they install somewhere custom.")
        print("Looked in: " + ", ".join(INSTALL_ROOTS))
        return 0

    if not found:
        print(f"No registry skill found in: {', '.join(roots_seen)}")
        print("\nThis is a directory-name match, so a skill installed under a")
        print("renamed folder will not show up. Ask before assuming nothing is there.")
        return 0

    print("Already installed (directory-name match, so treat as a strong hint):\n")
    for sid, paths in found.items():
        s = by_id(skills, sid)
        print(f"  {sid:26s} {ROUTE_NAME.get(s['route'], s['route'])}")
        print(f"  {'':26s} {s['tagline_en']}")
        for path in paths:
            print(f"  {'':26s} {path}")
    print("\nIf one of these covers what the user is asking for, say so and use it.")
    print("Do not re-litigate the choice or install a second deck skill alongside it.")
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
    p.add_argument("--lang", choices=("en", "zh"),
                   help="documentation language the user can read")
    p.add_argument("--cap", action="append", metavar="KEY",
                   help="require a documented capability; repeat to require several "
                        "(`pick.py caps` lists the keys)")

    sub.add_parser("caps", help="the requirements you can filter on, and why each matters")

    p = sub.add_parser("show", help="one skill: install command, styles, capabilities")
    p.add_argument("skill")
    p.add_argument("--why", action="store_true",
                   help="also print the doc quote each capability claim rests on")

    p = sub.add_parser("compare", help="two or more skills side by side")
    p.add_argument("skills", nargs="+", metavar="ID")

    sub.add_parser("installed", help="which registry skills are already on this machine")

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
        "styles": cmd_styles, "find": cmd_find, "caps": cmd_caps,
        "compare": cmd_compare, "installed": cmd_installed,
    }[args.cmd](args, skills, stats, samples, caps)


if __name__ == "__main__":
    raise SystemExit(main())
