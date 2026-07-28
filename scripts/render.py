#!/usr/bin/env python3
"""Generate the registry tables inside README.md and README.zh-CN.md.

Tables are written between <!-- BEGIN:BLOCK --> / <!-- END:BLOCK --> markers.
Everything outside the markers is hand-written prose and is never touched.

Usage:
    python scripts/render.py            # rewrite both READMEs in place
    python scripts/render.py --check    # exit 1 if the READMEs are out of date
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILLS = ROOT / "data" / "skills.json"
STATS = ROOT / "data" / "stats.json"

# Star thresholds for tiering. Deliberately coarse — the point is to separate
# "battle-tested by a lot of people" from "promising but unproven", not to
# imply the ordering within a tier is a quality ranking.
TIER_S_MIN = 5_000
TIER_A_MIN = 100

ROUTE_LABEL = {
    "html": ("HTML", "HTML"),
    "pptx": ("PPTX", "PPTX"),
    "hybrid": ("Both", "双路线"),
    "framework": ("Framework", "框架"),
    "templates": ("Templates", "模板库"),
    "list": ("List", "列表"),
}

TIER_LABEL = {
    "S": ("Tier S — Battle-tested (5k+ stars)", "Tier S — 大规模验证（5k+ star）"),
    "A": ("Tier A — Production-ready (100–5k stars)", "Tier A — 生产可用（100–5k star）"),
    "B": ("Tier B — Specialized & emerging (<100 stars)", "Tier B — 垂直与新兴（<100 star）"),
}


def load() -> tuple[dict, dict]:
    data = json.loads(SKILLS.read_text(encoding="utf-8"))
    stats = json.loads(STATS.read_text(encoding="utf-8")) if STATS.exists() else {"repos": {}}
    return data, stats


def stars_of(entry: dict, stats: dict) -> int:
    return stats["repos"].get(entry["repo"], {}).get("stars", 0)


def tier_of(entry: dict, stats: dict) -> str:
    # A monorepo's star count says nothing about the one skill inside it, so
    # anything flagged as such is pinned to Tier S by editorial judgement
    # rather than by its (meaningless here) headline number.
    if entry.get("stars_note") == "monorepo":
        return "S"
    s = stars_of(entry, stats)
    if s >= TIER_S_MIN:
        return "S"
    if s >= TIER_A_MIN:
        return "A"
    return "B"


def repo_link(entry: dict) -> str:
    url = f"https://github.com/{entry['repo']}"
    if entry.get("path"):
        branch = "main"
        url = f"{url}/tree/{branch}/{entry['path']}"
    return url


def fmt_stars(entry: dict, stats: dict) -> str:
    if entry.get("stars_note") == "monorepo":
        n = stars_of(entry, stats)
        return f"{n:,}*"
    s = stats["repos"].get(entry["repo"])
    if not s:
        return "—"
    val = f"{s['stars']:,}"
    return f"{val}~" if s.get("stale") else val


def license_cell(entry: dict, stats: dict) -> str:
    lic = stats["repos"].get(entry["repo"], {}).get("license")
    if lic in (None, "NOASSERTION"):
        lic = entry.get("license_note", "—")
    return f"⚠️ {lic}" if entry.get("license_warning") else lic


def table(entries: list[dict], stats: dict, lang: str) -> str:
    if lang == "en":
        head = "| Skill | ⭐ | Route | License | What it is |\n|---|---:|---|---|---|"
        tag_key, i = "tagline_en", 0
    else:
        head = "| 项目 | ⭐ | 路线 | License | 一句话 |\n|---|---:|---|---|---|"
        tag_key, i = "tagline_zh", 1

    rows = [head]
    for e in entries:
        name = f"**[{e['name']}]({repo_link(e)})**"
        author = e.get("author")
        by = f"<br><sub>{author}</sub>" if author else ""
        rows.append(
            f"| {name}{by} "
            f"| {fmt_stars(e, stats)} "
            f"| {ROUTE_LABEL[e['route']][i]} "
            f"| {license_cell(e, stats)} "
            f"| {e.get(tag_key, '')} |"
        )
    return "\n".join(rows)


def render_registry(data: dict, stats: dict, lang: str) -> str:
    skills = sorted(data["skills"], key=lambda e: -stars_of(e, stats))
    out: list[str] = []
    for tier in ("S", "A", "B"):
        group = [e for e in skills if tier_of(e, stats) == tier]
        if not group:
            continue
        out.append(f"### {TIER_LABEL[tier][0 if lang == 'en' else 1]}\n")
        out.append(table(group, stats, lang))
        out.append("")

    lists = sorted(data.get("lists", []), key=lambda e: -stars_of(e, stats))
    if lists:
        out.append("### " + ("Other curated lists" if lang == "en" else "其他精选列表") + "\n")
        out.append(table(lists, stats, lang))
        out.append("")

    if lang == "en":
        out.append(
            "<sub>`*` monorepo star count — reflects the whole repo, not this one skill. "
            "`~` stale value, last refresh failed. `⚠️` copyleft license, check before commercial use.</sub>"
        )
    else:
        out.append(
            "<sub>`*` monorepo star 数，反映整个仓库而非这一个 skill。"
            "`~` 上次刷新失败，为陈旧值。`⚠️` copyleft 协议，商用前请确认。</sub>"
        )
    return "\n".join(out)


def render_counts(data: dict, stats: dict, lang: str) -> str:
    n = len(data["skills"])
    total = sum(stars_of(e, stats) for e in data["skills"] if e.get("stars_note") != "monorepo")
    routes: dict[str, int] = {}
    for e in data["skills"]:
        routes[e["route"]] = routes.get(e["route"], 0) + 1
    when = stats.get("refreshed_at", "—")
    if lang == "en":
        return (
            f"**{n} skills tracked** · **{total:,} combined stars** · "
            f"{routes.get('html', 0)} HTML-native · {routes.get('pptx', 0)} native PPTX · "
            f"{routes.get('hybrid', 0)} both · data refreshed **{when}**"
        )
    return (
        f"**收录 {n} 个 skill** · **合计 {total:,} star** · "
        f"HTML 路线 {routes.get('html', 0)} 个 · PPTX 路线 {routes.get('pptx', 0)} 个 · "
        f"双路线 {routes.get('hybrid', 0)} 个 · 数据刷新于 **{when}**"
    )


BLOCKS = {
    "REGISTRY": render_registry,
    "COUNTS": render_counts,
}


def apply_blocks(text: str, data: dict, stats: dict, lang: str) -> str:
    for name, fn in BLOCKS.items():
        # Tolerate an empty block: with the markers on adjacent lines there is
        # only one newline between them, so neither delimiter can claim it.
        pattern = re.compile(
            rf"(<!-- BEGIN:{name} -->)(.*?)(<!-- END:{name} -->)",
            re.DOTALL,
        )
        if not pattern.search(text):
            print(f"  (no {name} block in this file, skipping)", file=sys.stderr)
            continue
        body = fn(data, stats, lang)
        text = pattern.sub(
            lambda m: f"{m.group(1)}\n{body}\n{m.group(3)}",
            text,
        )
    return text


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true")
    args = ap.parse_args()

    data, stats = load()
    targets = [(ROOT / "README.md", "en"), (ROOT / "README.zh-CN.md", "zh")]

    stale = []
    for path, lang in targets:
        if not path.exists():
            print(f"  !! {path.name} missing", file=sys.stderr)
            continue
        original = path.read_text(encoding="utf-8")
        updated = apply_blocks(original, data, stats, lang)
        if original == updated:
            print(f"  = {path.name} already current")
            continue
        if args.check:
            stale.append(path.name)
            continue
        path.write_text(updated, encoding="utf-8")
        print(f"  ✎ {path.name} updated")

    if args.check and stale:
        print(f"\nout of date: {', '.join(stale)} — run `python scripts/render.py`", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
