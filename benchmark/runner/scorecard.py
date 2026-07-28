#!/usr/bin/env python3
"""Aggregate per-run score files into a scorecard.

Reads every benchmark/results/<run-id>/<skill>/<corpus>/score.json, applies the
gating rules from rubric.md, and emits both machine-readable JSON and the
markdown table that goes in the README.

    python scorecard.py                    # rebuild results/scorecard.{json,md}
    python scorecard.py --validate         # check score files, write nothing

Score file shape (see ../rubric.md for the anchors):

    {
      "skill": "frontend-slides",
      "corpus": "02-quarterly-review",
      "commit": "a1b2c3d",
      "scored_by": ["alice", "bob"],
      "scores": {
        "visual_distinctiveness": 4,
        "typographic_craft":      4,
        "hierarchy_density":      3,
        "data_fidelity":          5,
        "content_fidelity":       5,
        "deliverable_integrity":  4,
        "effort_to_acceptable":   4
      },
      "evidence": {"visual_distinctiveness": "slide-03.png, committed palette"},
      "metrics": {"seconds_to_first_output": 214, "correction_turns": 2},
      "notes": "..."
    }
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RESULTS = ROOT / "results"

DIMENSIONS = [
    ("visual_distinctiveness", "Visual", False),
    ("typographic_craft", "Type", False),
    ("hierarchy_density", "Density", False),
    ("data_fidelity", "Data", True),
    ("content_fidelity", "Content", True),
    ("deliverable_integrity", "Deliver", False),
    ("effort_to_acceptable", "Effort", False),
]
MAX_TOTAL = len(DIMENSIONS) * 5
GATED_CAP = 17  # rubric.md: a 0 on either gating dimension caps the total here


def load_scores() -> tuple[list[dict], list[str]]:
    rows, problems = [], []
    if not RESULTS.exists():
        return rows, ["benchmark/results/ does not exist yet"]

    for path in sorted(RESULTS.rglob("score.json")):
        try:
            d = json.loads(path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as e:
            problems.append(f"{path.relative_to(ROOT)}: invalid JSON ({e})")
            continue

        missing = [k for k, _, _ in DIMENSIONS if k not in d.get("scores", {})]
        if missing:
            problems.append(f"{path.relative_to(ROOT)}: missing {', '.join(missing)}")
            continue

        bad = [
            k
            for k, _, _ in DIMENSIONS
            if not isinstance(d["scores"][k], int) or not 0 <= d["scores"][k] <= 5
        ]
        if bad:
            problems.append(f"{path.relative_to(ROOT)}: out-of-range {', '.join(bad)}")
            continue

        if not d.get("evidence"):
            problems.append(
                f"{path.relative_to(ROOT)}: no evidence — rubric requires a citation per score"
            )

        d["_path"] = str(path.relative_to(ROOT))
        rows.append(d)
    return rows, problems


def total_for(row: dict) -> tuple[int, bool]:
    """Returns (total, gated). Gating is what stops a pretty deck with invented
    numbers from out-ranking an honest one."""
    raw = sum(row["scores"][k] for k, _, _ in DIMENSIONS)
    gated = any(row["scores"][k] == 0 for k, _, is_gate in DIMENSIONS if is_gate)
    return (min(raw, GATED_CAP), True) if gated else (raw, False)


def aggregate(rows: list[dict]) -> dict:
    by_skill: dict[str, list[dict]] = {}
    for r in rows:
        by_skill.setdefault(r["skill"], []).append(r)

    out = {}
    for skill, runs in by_skill.items():
        totals = [total_for(r) for r in runs]
        out[skill] = {
            "runs": len(runs),
            "corpora": sorted({r["corpus"] for r in runs}),
            "mean_total": round(sum(t for t, _ in totals) / len(totals), 1),
            "gated_runs": sum(1 for _, g in totals if g),
            "per_dimension": {
                key: round(sum(r["scores"][key] for r in runs) / len(runs), 1)
                for key, _, _ in DIMENSIONS
            },
        }
    return dict(sorted(out.items(), key=lambda kv: -kv[1]["mean_total"]))


def markdown(agg: dict) -> str:
    if not agg:
        return (
            "> **No benchmark runs recorded yet.** The harness, corpus and rubric are\n"
            "> complete and reproducible; scores land here as runs are completed.\n"
            "> See [the benchmark protocol](../README.md) to contribute a run."
        )

    head = "| Skill | Mean | " + " | ".join(lbl for _, lbl, _ in DIMENSIONS) + " | Runs |"
    sep = "|---|---:|" + "---:|" * len(DIMENSIONS) + "---:|"
    lines = [head, sep]
    for skill, a in agg.items():
        cells = " | ".join(f"{a['per_dimension'][k]}" for k, _, _ in DIMENSIONS)
        flag = " ⚠️" if a["gated_runs"] else ""
        lines.append(
            f"| **{skill}**{flag} | **{a['mean_total']}**/{MAX_TOTAL} | {cells} | {a['runs']} |"
        )
    lines.append("")
    lines.append(
        "<sub>⚠️ = at least one run gated to zero on data or content fidelity "
        "(fabricated or lost figures). See [rubric.md](../rubric.md).</sub>"
    )
    return "\n".join(lines)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--validate", action="store_true", help="check score files only")
    args = ap.parse_args()

    rows, problems = load_scores()

    for p in problems:
        print(f"  !! {p}", file=sys.stderr)

    if args.validate:
        hard = [p for p in problems if "does not exist yet" not in p]
        print(f"{len(rows)} valid score file(s), {len(hard)} problem(s)")
        return 1 if hard else 0

    agg = aggregate(rows)
    RESULTS.mkdir(parents=True, exist_ok=True)
    (RESULTS / "scorecard.json").write_text(
        json.dumps({"max_total": MAX_TOTAL, "skills": agg}, indent=2) + "\n", encoding="utf-8"
    )
    (RESULTS / "scorecard.md").write_text(markdown(agg) + "\n", encoding="utf-8")
    print(f"  {len(rows)} run(s) across {len(agg)} skill(s)")
    print(f"  wrote results/scorecard.json and results/scorecard.md")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
