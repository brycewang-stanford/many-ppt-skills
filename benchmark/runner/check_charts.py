#!/usr/bin/env python3
"""Check that charts actually encode their data, by measuring rendered geometry.

`check_fidelity.py` proves every number reached the deck. It cannot prove the
chart drawn from those numbers means anything, and the difference is not
academic. The first run in this repo produced a bar chart whose markup was
arithmetically perfect:

    36.1 -> height:76.5%   ...   47.2 -> height:100%

A genuine zero-baseline encoding, with a source comment saying so. Every bar
then rendered at exactly 288px, because the percentage heights resolved against
a flex column of indefinite height and CSS silently dropped them. Numeric
fidelity: 100%. Chart: meaningless.

Nothing that reads source catches this. The values are right *in the source* —
that is the whole trap. Only rendering the deck and measuring the marks catches
it, which is why this script drives a real browser.

    python check_charts.py --deck ../results/run-01/<skill>/<corpus>/deck.html

Exits non-zero when a chart's marks are measurably flat against varying data.

**Scope, stated honestly.** This finds grouped marks — bars and columns — whose
size should track a printed number. It does not check line charts, pie slices,
axis truncation, or whether the chart was the right chart. A clean exit means
"no flat bar groups found", not "the charts are good".
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

# Ratio thresholds. A value spread below this is legitimately flat data, and
# flagging it would fire on charts that are simply showing near-equal values.
MIN_VALUE_SPREAD = 1.08
# Rendered marks this uniform, against data that is not, means the encoding was
# dropped somewhere between the markup and the pixels.
MAX_FLAT_SPREAD = 1.02

# Runs in the page. Finds sibling groups where each member prints a number and
# draws a box, then reports the numbers next to the measured geometry. It stays
# deliberately structure-agnostic: keying on class names like `.bar` would only
# ever work for the one skill they came from.
PROBE = r"""
() => {
  const num = t => {
    const m = (t || "").replace(/[, ]/g, "").match(/-?\d+(?:\.\d+)?/);
    return m ? parseFloat(m[0]) : null;
  };
  const groups = [];
  for (const parent of document.querySelectorAll("*")) {
    const kids = [...parent.children];
    if (kids.length < 3) continue;
    const marks = [];
    for (const kid of kids) {
      const value = num(kid.textContent);
      if (value === null) { marks.length = 0; break; }
      // The mark is the largest painted box inside this child. For a bar column
      // that is the bar; for a plain table row there is no such box and the
      // group is discarded below.
      let best = null;
      for (const el of [kid, ...kid.querySelectorAll("*")]) {
        const r = el.getBoundingClientRect();
        const st = getComputedStyle(el);
        const painted = st.backgroundImage !== "none" ||
          (st.backgroundColor && !/rgba\(0, 0, 0, 0\)|transparent/.test(st.backgroundColor));
        if (!painted || r.height < 4 || r.width < 2) continue;
        if (!best || r.height * r.width > best.h * best.w)
          best = { h: r.height, w: r.width, declared: el.style.height || el.style.width || "" };
      }
      if (!best) { marks.length = 0; break; }
      marks.push({ value, h: +best.h.toFixed(1), w: +best.w.toFixed(1), declared: best.declared });
    }
    if (marks.length >= 3 && new Set(marks.map(m => m.value)).size >= 3)
      groups.push({ tag: parent.tagName.toLowerCase(), cls: parent.className || "", marks,
                    viewport: window.innerWidth * window.innerHeight });
  }
  return groups;
}
"""


def ratio(xs: list[float]) -> float:
    lo, hi = min(xs), max(xs)
    return hi / lo if lo > 0 else float("inf")


def analyse(group: dict) -> dict | None:
    """Decide whether one candidate group is a chart with a dropped encoding."""
    values = [m["value"] for m in group["marks"]]
    if min(values) <= 0:
        return None  # ratios are meaningless across zero or negatives

    # A deck's own slide containers are siblings, are painted, and each contain a
    # number somewhere — a page number is enough. They are therefore a perfect
    # decoy for this probe, and on the first deck tested they produced a
    # confident finding about twelve "marks" that were the twelve slides. A real
    # bar occupies a small fraction of the stage; a slide occupies all of it.
    viewport = group.get("viewport") or (1920 * 1080)
    if min(m["h"] * m["w"] for m in group["marks"]) > 0.25 * viewport:
        return None
    v_spread = ratio(values)
    if v_spread < MIN_VALUE_SPREAD:
        return None  # the data really is flat; nothing to encode

    # Bars may be vertical or horizontal. Whichever axis varies is the encoding
    # axis; if neither varies, the encoding was dropped.
    h_spread, w_spread = ratio([m["h"] for m in group["marks"]]), ratio([m["w"] for m in group["marks"]])
    axis, spread = ("height", h_spread) if h_spread >= w_spread else ("width", w_spread)
    if spread > MAX_FLAT_SPREAD:
        return None  # something varies; treat it as encoded

    return {
        "container": f"{group['tag']}.{group['cls']}".strip("."),
        "mark_count": len(values),
        "values": values,
        "value_spread": round(v_spread, 4),
        "rendered_axis": axis,
        "rendered_spread": round(spread, 4),
        "rendered_sizes": [m[axis[0]] for m in group["marks"]],
        "declared": [m["declared"] for m in group["marks"] if m["declared"]],
        "verdict": (
            f"{len(values)} marks span {v_spread:.2f}x in value but "
            f"{spread:.4f}x in rendered {axis} — the encoding is not reaching the pixels"
        ),
    }


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--deck", required=True, type=Path)
    ap.add_argument("--out", type=Path, help="write findings as JSON")
    ap.add_argument("--settle-ms", type=int, default=800)
    args = ap.parse_args()

    if not args.deck.exists():
        print(f"deck not found: {args.deck}", file=sys.stderr)
        return 2
    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        print("playwright not installed:\n  pip install playwright && playwright install chromium",
              file=sys.stderr)
        return 2

    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(viewport={"width": 1920, "height": 1080})
        page.goto(f"file://{args.deck.resolve()}")
        page.wait_for_timeout(args.settle_ms)
        groups = page.evaluate(PROBE)
        browser.close()

    findings = [f for f in (analyse(g) for g in groups) if f]

    # Nested containers surface the same marks more than once; keep one finding
    # per distinct value sequence so a single broken chart is reported once.
    seen, unique = set(), []
    for f in findings:
        key = tuple(f["values"])
        if key not in seen:
            seen.add(key)
            unique.append(f)

    report = {
        "deck": str(args.deck),
        "candidate_groups": len(groups),
        "broken_charts": len(unique),
        "findings": unique,
        "scope": "grouped bar/column marks only; line, pie and axis truncation are not checked",
    }
    if args.out:
        args.out.write_text(json.dumps(report, indent=2) + "\n")

    print(f"deck   : {args.deck}")
    print(f"groups : {len(groups)} candidate mark group(s) measured")
    if not unique:
        print("result : no flat bar groups found")
        print("         (this does not mean the charts are good — see --help for scope)")
        return 0

    print(f"result : {len(unique)} chart(s) whose encoding is not reaching the pixels\n")
    for f in unique:
        print(f"  {f['container']}")
        print(f"    values   {f['values']}")
        print(f"    rendered {f['rendered_axis']} {f['rendered_sizes']}")
        if f["declared"]:
            print(f"    declared {f['declared']}")
        print(f"    {f['verdict']}\n")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
