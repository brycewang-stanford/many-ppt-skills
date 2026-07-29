#!/usr/bin/env python3
"""Generate the registry tables inside README.md (Chinese) and README.en.md.

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


def sort_key(entry: dict, stats: dict) -> int:
    """Ordering weight. A monorepo's headline count belongs to the whole repo,
    not to the one skill inside it, so ranking by it would put the official
    baseline above projects with 40x its actual following. Sort those last
    within their tier and let the footnote explain the asterisk."""
    if entry.get("stars_note") == "monorepo":
        return -1
    return stars_of(entry, stats)


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
    skills = sorted(data["skills"], key=lambda e: -sort_key(e, stats))
    out: list[str] = []
    for tier in ("S", "A", "B"):
        group = [e for e in skills if tier_of(e, stats) == tier]
        if not group:
            continue
        out.append(f"### {TIER_LABEL[tier][0 if lang == 'en' else 1]}\n")
        out.append(table(group, stats, lang))
        out.append("")

    lists = sorted(data.get("lists", []), key=lambda e: -sort_key(e, stats))
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


SCORECARD = ROOT / "benchmark" / "results" / "scorecard.json"

DIM_LABELS = [
    ("visual_distinctiveness", "Visual", "视觉"),
    ("typographic_craft", "Type", "字体"),
    ("hierarchy_density", "Density", "密度"),
    ("data_fidelity", "Data", "数据"),
    ("content_fidelity", "Content", "内容"),
    ("deliverable_integrity", "Deliver", "交付"),
    ("effort_to_acceptable", "Effort", "代价"),
]


def render_scorecard(data: dict, stats: dict, lang: str) -> str:
    """Benchmark results, or an honest statement that there are none yet.

    Never fabricates a placeholder row — a benchmark that ships with invented
    numbers refutes its own premise.
    """
    card = json.loads(SCORECARD.read_text(encoding="utf-8")) if SCORECARD.exists() else {}
    skills = card.get("skills", {})
    max_total = card.get("max_total", 35)

    if not skills:
        return (
            "> **No runs recorded yet.** The corpus, rubric and harness are complete and\n"
            "> reproducible; scores land here as runs complete."
            if lang == "en"
            else "> **尚无实测记录。** 语料、评分卡与工具链已完成且可复现，跑分结果会陆续落在这里。"
        )

    i = 1 if lang == "en" else 2
    head = ("| Skill | Mean | " if lang == "en" else "| 项目 | 总分 | ") + " | ".join(
        d[i] for d in DIM_LABELS
    ) + (" | Runs |" if lang == "en" else " | 次数 |")
    rows = [head, "|---|---:|" + "---:|" * len(DIM_LABELS) + "---:|"]

    total_runs = 0
    for skill, a in skills.items():
        total_runs += a["runs"]
        cells = " | ".join(str(a["per_dimension"][k]) for k, _, _ in DIM_LABELS)
        flag = " ⚠️" if a.get("gated_runs") else ""
        rows.append(
            f"| **{skill}**{flag} | **{a['mean_total']}**/{max_total} | {cells} | {a['runs']} |"
        )

    rows.append("")
    if lang == "en":
        rows.append(
            f"<sub>{total_runs} run(s) so far — far too few to rank anything. "
            "Scores are provisional and every run discloses its conflicts. "
            "⚠️ = a run gated to zero on data or content fidelity.</sub>"
        )
    else:
        rows.append(
            f"<sub>目前仅 {total_runs} 次实测 —— 远不足以给任何东西排名。"
            "分数均为暂定值，每次实测都公开披露其利益冲突。"
            "⚠️ = 该次实测在数据或内容保真上被一票否决。</sub>"
        )
    return "\n".join(rows)


CAPS = ROOT / "data" / "capabilities.json"

# Order the columns by how often they decide a choice, not alphabetically.
CAP_ORDER = [
    "pptx_export", "pdf_export", "native_charts", "code_highlighting",
    "diagrams", "animation", "speaker_notes", "presenter_mode",
    "custom_template", "self_contained",
]

CAP_MARK = {"yes": "✅", "no": "—", "unclear": "·"}


def render_capabilities(data: dict, stats: dict, lang: str) -> str:
    """What each skill's own documentation claims it does.

    Not scores. Every ✅ is backed by a quote in data/capabilities.json, and the
    middle value is deliberately "the docs are silent", not "no" — collapsing
    those two would invent facts about 26 projects at once.
    """
    if not CAPS.exists():
        return ("> Capability data not generated yet — run "
                "`python scripts/read_capabilities.py`.")
    card = json.loads(CAPS.read_text(encoding="utf-8"))
    caps, skills = card.get("capabilities", {}), card.get("skills", {})
    if not skills:
        return "> Capability data is empty."

    by_id = {s["id"]: s for s in data["skills"]}
    label_key = "label_en" if lang == "en" else "label_zh"

    # Only skills whose docs have actually been read. A skill that is merely
    # absent from the run would otherwise render as a full row of "the docs are
    # silent", which is a claim about 10 capabilities that nobody checked.
    def was_read(sid: str) -> bool:
        return any(isinstance(v, dict) and "verdict" in v
                   for v in skills[sid]["caps"].values())

    # Top of the registry only. A 26-row, 10-column grid is unreadable, and the
    # skills people actually choose between are the ones with a community.
    ranked = sorted(
        (s for s in data["skills"] if s["id"] in skills and was_read(s["id"])),
        key=lambda s: -(stats.get("repos", {}).get(s["repo"], {}).get("stars") or 0),
    )[:10]
    if not ranked:
        return "> No skill documentation has been read yet."

    head = ("| Skill | " if lang == "en" else "| 项目 | ") + " | ".join(
        caps[c][label_key] for c in CAP_ORDER if c in caps) + " |"
    rows = [head, "|---|" + ":-:|" * len([c for c in CAP_ORDER if c in caps])]

    for s in ranked:
        cells = []
        for c in CAP_ORDER:
            if c not in caps:
                continue
            # "Offline" is an HTML-route question. A .pptx is a file by
            # construction, so scoring it here invites a false ✅ — which is
            # exactly what happened when one skill's docs called an intermediate
            # SVG preview "self-contained".
            if c == "self_contained" and s.get("route") == "pptx":
                cells.append("n/a")
                continue
            v = (skills[s["id"]]["caps"].get(c) or {}).get("verdict", "unclear")
            cells.append(CAP_MARK.get(v, "·"))
        rows.append(f"| **{s['name']}** | " + " | ".join(cells) + " |")

    rows.append("")
    if lang == "en":
        rows.append(
            "<sub>✅ the docs claim it · — the docs say it does not · "
            "· the docs are silent, which is not the same as no · "
            "n/a the question does not apply to that route. "
            "Read from each project's own SKILL.md and README, never from running it; "
            "every ✅ carries the sentence it came from in "
            "[`data/capabilities.json`](data/capabilities.json).</sub>"
        )
    else:
        rows.append(
            "<sub>✅ 文档声明支持 · — 文档明确说明不支持 · "
            "· 文档未提及，这不等于不支持 · "
            "n/a 该问题对这条路线不适用。"
            "全部读自各项目自己的 SKILL.md 与 README，不是实跑验证；"
            "每个 ✅ 的出处引文都在 "
            "[`data/capabilities.json`](data/capabilities.json)。</sub>"
        )
    return "\n".join(rows)



BLOCKS = {
    "REGISTRY": render_registry,
    "COUNTS": render_counts,
    "SCORECARD": render_scorecard,
    "CAPABILITIES": render_capabilities,
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
    targets = [(ROOT / "README.md", "zh"), (ROOT / "README.en.md", "en")]

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
