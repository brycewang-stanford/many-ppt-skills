#!/usr/bin/env python3
"""Build a comparable capability grid from what each skill's own docs claim.

The registry tables answer "what is this". They do not answer the question people
actually arrive with — *does this one handle my code blocks, and can the CFO edit
slide 12* — because that information is buried in 26 different READMEs written in
two languages.

This reads every skill's own documentation and extracts a fixed set of
capabilities into one comparable shape.

    python scripts/extract_capabilities.py        # writes data/capabilities.json
    python scripts/extract_capabilities.py --diff # show what changed, write nothing

**What this measures, stated plainly.** These are *documented* capabilities —
what a project says about itself. Nothing here has been verified by running the
skill. A project that does something well but never mentions it will read as
"not mentioned", and a project that overclaims will be believed. That is a real
limit, and it is why every cell carries the line of documentation it came from:
the claim is checkable even when it is wrong.

Absence of evidence is recorded as `null` ("not mentioned"), never as `false`.
The difference matters — one is "this skill says it cannot", the other is "its
docs are silent", and collapsing them would invent facts.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CACHE = ROOT / "benchmark" / ".cache" / "skills"
OUT = ROOT / "data" / "capabilities.json"

# Docs worth reading, in priority order. SKILL.md is the contract the agent
# actually follows, so it outranks marketing copy in README.
DOC_NAMES = ("SKILL.md", "README.md", "README.zh-CN.md", "README_CN.md",
             "README.en.md", "AGENTS.md", "CLAUDE.md")

# Each capability is a list of alternative regexes. Written to be specific:
# "chart" alone matches "flowchart" and every roadmap slide in every README, so
# the patterns name concrete libraries and concrete phrases instead.
CAPABILITIES: dict[str, dict] = {
    "native_charts": {
        "label_en": "Data charts",
        "label_zh": "数据图表",
        "why": "Whether numbers become a real chart rather than a picture of one.",
        "patterns": [
            r"\bnative[- ]charts?\b", r"\becharts\b", r"\bchart\.js\b", r"\bd3\.js\b",
            r"\brecharts\b", r"\bchartjs\b", r"\bplotly\b",
            r"\b(bar|line|pie|donut)\s+charts?\b", r"原生图表", r"数据图表",
        ],
    },
    "code_highlighting": {
        "label_en": "Code blocks",
        "label_zh": "代码高亮",
        "why": "Whether a tech talk's code survives with indentation and colour.",
        "patterns": [
            r"\bsyntax[- ]highlight", r"\bhighlight\.js\b", r"\bprism(?:\.js)?\b",
            r"\bshiki\b", r"\bhljs\b", r"代码高亮", r"语法高亮",
        ],
    },
    "diagrams": {
        "label_en": "Diagrams",
        "label_zh": "图示",
        "why": "Architecture and flow diagrams, not just boxes of text.",
        "patterns": [
            r"\bmermaid\b", r"\bgraphviz\b", r"\bexcalidraw\b",
            r"\b(architecture|flow|sequence)\s+diagrams?\b", r"流程图", r"架构图",
        ],
    },
    "animation": {
        "label_en": "Motion",
        "label_zh": "动效",
        "why": "Transitions and build-ups. Cheap on HTML, constrained on PPTX.",
        "patterns": [
            r"\banimations?\b", r"\btransitions?\b", r"\bgsap\b", r"@keyframes",
            r"\bframer[- ]motion\b", r"动画", r"转场",
        ],
    },
    "speaker_notes": {
        "label_en": "Speaker notes",
        "label_zh": "演讲备注",
        "why": "Needed if anyone but you will present it.",
        "patterns": [
            r"\bspeaker[- ]notes?\b", r"\bpresenter[- ]notes?\b", r"\bnotesSlide\b",
            r"演讲者?备注", r"备注页",
        ],
    },
    "presenter_mode": {
        "label_en": "Presenter mode",
        "label_zh": "演讲者模式",
        "why": "Second-screen view with notes and a timer.",
        "patterns": [
            r"\bpresenter[- ]mode\b", r"\bpresentation[- ]mode\b", r"演讲者模式",
        ],
    },
    "pptx_export": {
        "label_en": "→ PPTX",
        "label_zh": "→ PPTX",
        "why": "Whether the recipient can open and edit it in PowerPoint.",
        "patterns": [
            r"\bpython-pptx\b", r"\bpptxgenjs\b", r"\.pptx\b", r"\bPowerPoint\b",
            r"导出\s*PPTX", r"转\s*PPTX",
        ],
    },
    "pdf_export": {
        "label_en": "→ PDF",
        "label_zh": "→ PDF",
        "why": "The universal handoff format.",
        "patterns": [
            r"\bexport\w*\s+to\s+PDF\b", r"\bPDF\s+export\b", r"\bprint\s+to\s+PDF\b",
            r"\bpdftoppm\b", r"\bweasyprint\b", r"导出\s*PDF", r"转\s*PDF",
        ],
    },
    "custom_template": {
        "label_en": "Your template",
        "label_zh": "自定义模板",
        "why": "Whether a mandated corporate deck template is respected.",
        "patterns": [
            r"\bslide[- ]master\b", r"\bcustom\s+templates?\b", r"\bbrand\s+(kit|guidelines?)\b",
            r"\byour\s+own\s+templates?\b", r"母版", r"自定义模板", r"品牌\s*(色|规范)",
        ],
    },
    "self_contained": {
        "label_en": "Offline",
        "label_zh": "离线可用",
        "why": "A single file with no CDN still opens in ten years.",
        "patterns": [
            r"\bzero[- ]dependenc", r"\bself[- ]contained\b", r"\bno\s+external\s+dependenc",
            r"\bsingle[- ]file\b", r"\boffline\b", r"零依赖", r"单文件", r"离线",
        ],
    },
}

# Runtime is decided by what is in the directory, not by what the docs claim.
RUNTIME_MARKERS = {
    "python": ("requirements.txt", "pyproject.toml", "setup.py"),
    "node": ("package.json",),
}


def read_docs(skill_dir: Path) -> list[tuple[str, str]]:
    """Return (filename, text) for the skill's own documentation."""
    docs = []
    for name in DOC_NAMES:
        for path in sorted(skill_dir.rglob(name)):
            if any(p in path.parts for p in ("node_modules", ".git", "examples")):
                continue
            try:
                docs.append((str(path.relative_to(skill_dir)),
                             path.read_text(errors="replace")))
            except OSError:
                continue
            if len(docs) >= 12:  # a few repos vendor dozens of nested READMEs
                return docs
    return docs


def find(patterns: list[str], docs: list[tuple[str, str]]) -> dict | None:
    """First match wins, and it carries its evidence back."""
    for name, text in docs:
        for pattern in patterns:
            m = re.search(pattern, text, re.IGNORECASE)
            if not m:
                continue
            line = next(
                (ln.strip() for ln in text.splitlines()
                 if re.search(pattern, ln, re.IGNORECASE)), "")
            return {
                "value": True,
                "source": name,
                "matched": m.group(0),
                "evidence": (line[:180] + "…") if len(line) > 180 else line,
            }
    return None


def detect_runtime(skill_dir: Path) -> list[str]:
    found = []
    for runtime, markers in RUNTIME_MARKERS.items():
        if any((skill_dir / m).exists() for m in markers) or any(
            list(skill_dir.rglob(m))[:1] for m in markers
        ):
            found.append(runtime)
    return found


def resolve_skill_dir(skill_id: str, repo_dir: Path) -> Path:
    """Mirrors the runner's resolver so both look at the same directory."""
    subdirs = {"ppt-master": "skills/ppt-master",
               "visual-explainer": "plugins/visual-explainer"}
    if skill_id in subdirs and (repo_dir / subdirs[skill_id]).is_dir():
        return repo_dir / subdirs[skill_id]
    if (repo_dir / "SKILL.md").exists():
        return repo_dir
    candidates = [p.parent for p in repo_dir.rglob("SKILL.md")
                  if "node_modules" not in p.parts]
    return min(candidates, key=lambda p: len(p.parts)) if candidates else repo_dir


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--diff", action="store_true", help="report changes, write nothing")
    args = ap.parse_args()

    registry = json.loads((ROOT / "data" / "skills.json").read_text())
    result: dict = {
        "$comment": (
            "Documented capabilities — what each project's own docs claim, with the "
            "line they claim it on. Nothing here was verified by running the skill. "
            "null means the docs are silent, NOT that the skill lacks the feature. "
            "Generated by scripts/extract_capabilities.py; do not hand-edit."
        ),
        "capabilities": {k: {kk: v[kk] for kk in ("label_en", "label_zh", "why")}
                         for k, v in CAPABILITIES.items()},
        "skills": {},
    }

    missing = []
    for skill in registry["skills"]:
        sid = skill["id"]
        repo_dir = CACHE / sid
        if not repo_dir.is_dir():
            missing.append(sid)
            continue
        skill_dir = resolve_skill_dir(sid, repo_dir)
        docs = read_docs(skill_dir)
        entry = {
            "docs_read": [d[0] for d in docs],
            "runtime": detect_runtime(skill_dir),
            "caps": {name: find(spec["patterns"], docs)
                     for name, spec in CAPABILITIES.items()},
        }
        result["skills"][sid] = entry

    if missing:
        print(f"not cloned, skipped: {', '.join(missing)}", file=sys.stderr)

    if args.diff and OUT.exists():
        old = json.loads(OUT.read_text()).get("skills", {})
        for sid, entry in result["skills"].items():
            for cap, val in entry["caps"].items():
                was = (old.get(sid, {}).get("caps", {}) or {}).get(cap)
                if bool(was) != bool(val):
                    print(f"  {sid}.{cap}: {bool(was)} -> {bool(val)}")
        return 0

    OUT.write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n")

    n = len(result["skills"])
    print(f"{n} skill(s) scanned -> {OUT.relative_to(ROOT)}")
    for cap in CAPABILITIES:
        hits = sum(1 for e in result["skills"].values() if e["caps"][cap])
        print(f"  {cap:20s} documented by {hits:2d}/{n}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
