#!/usr/bin/env python3
"""Measure how *native* a .pptx actually is. Facts for rubric dimension 6.

The HTML route can be checked for self-containment by counting remote URLs. The
PPTX route turns on a different question that no screenshot can answer:

    Are these real PowerPoint objects, or is it a picture of a deck?

A deck that renders beautifully and is nine full-slide images scores 2 on
deliverable integrity ("substantially image-based, text is not selectable or
editable"), and it looks identical to a 5 in a screenshot. So this unzips the
file and counts.

    python probe_pptx.py deck.pptx --json probe.json

Emits counts, a native-text ratio, and the anchor those facts support. It does
not assign the score — the judge maps facts to anchors, and this keeps the facts
out of the judge's opinion.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import zipfile
from pathlib import Path

SLIDE = re.compile(r"^ppt/slides/slide\d+\.xml$")
CHART = re.compile(r"^ppt/charts/chart\d+\.xml$")
EMBED = re.compile(r"^ppt/embeddings/.*\.(xlsx|xls)$")
FONT = re.compile(r"^ppt/fonts/.*\.(fntdata|ttf|otf)$", re.I)
MEDIA = re.compile(r"^ppt/media/.*\.(png|jpe?g|gif|bmp|tiff?|emf|wmf|svg)$", re.I)

# Drawing-ML element names that mean "a real object the user can select".
COUNTERS = {
    "text_runs": r"<a:t>",           # a run of editable text
    "shapes": r"<p:sp[ >]",          # autoshape / textbox
    "pictures": r"<p:pic[ >]",       # embedded raster or vector picture
    "tables": r"<a:tbl[ >]",         # native table
    "graphic_frames": r"<p:graphicFrame[ >]",  # charts, tables, SmartArt
    "connectors": r"<p:cxnSp[ >]",   # native connector lines
    "group_shapes": r"<p:grpSp[ >]",
}


def probe(path: Path) -> dict:
    if not zipfile.is_zipfile(path):
        return {"error": "not a zip — file is not a valid .pptx", "opens": False}

    out: dict = {"file": path.name, "size_kb": round(path.stat().st_size / 1024, 1)}
    try:
        with zipfile.ZipFile(path) as z:
            bad = z.testzip()
            if bad:
                return {"error": f"corrupt member: {bad}", "opens": False}

            names = z.namelist()
            slides = sorted(n for n in names if SLIDE.match(n))
            if not slides:
                return {"error": "no ppt/slides/slideN.xml — not a presentation",
                        "opens": False}

            xml = "".join(z.read(n).decode("utf-8", errors="replace") for n in slides)

            out["opens"] = True
            out["slide_count"] = len(slides)
            out["native_charts"] = len([n for n in names if CHART.match(n)])
            out["embedded_workbooks"] = len([n for n in names if EMBED.match(n)])
            out["embedded_fonts"] = len([n for n in names if FONT.match(n)])
            out["media_files"] = len([n for n in names if MEDIA.match(n)])
            for key, pattern in COUNTERS.items():
                out[key] = len(re.findall(pattern, xml))

            # Characters living in real text runs. A deck of full-slide images has
            # a handful (or zero); a genuine deck has thousands.
            chars = sum(len(t) for t in re.findall(r"<a:t>(.*?)</a:t>", xml, re.DOTALL))
            out["text_characters"] = chars
            out["text_chars_per_slide"] = round(chars / len(slides), 1)
            out["pictures_per_slide"] = round(out["pictures"] / len(slides), 2)

            out["has_speaker_notes"] = any(
                n.startswith("ppt/notesSlides/notesSlide") for n in names
            )
    except (zipfile.BadZipFile, KeyError, OSError) as exc:
        return {"error": f"{type(exc).__name__}: {exc}", "opens": False}

    out["assessment"] = assess(out)
    return out


def assess(m: dict) -> dict:
    """Map counts to the dimension-6 PPTX anchors. Deliberately conservative:
    it reports what the counts support and leaves the score to the judge."""
    signals, concerns = [], []

    # ~1 picture per slide with almost no text is the image-dump signature.
    image_based = m["text_chars_per_slide"] < 80 and m["pictures_per_slide"] >= 0.8
    if image_based:
        concerns.append(
            "Substantially image-based: under 80 text characters per slide with "
            "roughly one picture per slide. Text is likely not selectable. "
            "Supports anchor 2."
        )
    else:
        signals.append(
            f"{m['text_chars_per_slide']} text characters per slide in real "
            f"<a:t> runs — text is selectable and editable."
        )

    if m["native_charts"]:
        signals.append(
            f"{m['native_charts']} native chart part(s), "
            f"{m['embedded_workbooks']} embedded workbook(s) — chart data is editable."
        )
    elif m["graphic_frames"] == 0 and m["pictures"]:
        concerns.append("No native charts or tables; any data viz is a picture.")

    if m["tables"]:
        signals.append(f"{m['tables']} native table(s).")
    if m["connectors"]:
        signals.append(f"{m['connectors']} native connector(s).")
    if m["embedded_fonts"]:
        signals.append(
            f"{m['embedded_fonts']} embedded font file(s) — typography survives "
            "on a machine without those fonts installed."
        )
    if m["has_speaker_notes"]:
        signals.append("Carries speaker notes.")

    return {
        "likely_image_based": image_based,
        "supports_anchor": 2 if image_based else None,
        "signals": signals,
        "concerns": concerns,
        "note": (
            "Counts only. Cross-application rendering (PowerPoint vs Keynote vs "
            "LibreOffice) is not checked here and still needs a human or a "
            "converted render."
        ),
    }


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("deck", type=Path, help=".pptx file, or a directory to search")
    ap.add_argument("--json", type=Path, help="write the report here")
    args = ap.parse_args()

    if not args.deck.exists():
        sys.exit(f"path does not exist: {args.deck}")

    if args.deck.is_dir():
        found = sorted(args.deck.rglob("*.pptx"))
        if not found:
            sys.exit(f"no .pptx under {args.deck}")
        reports = [probe(p) for p in found]
        report = reports[0] if len(reports) == 1 else {"decks": reports}
    else:
        report = probe(args.deck)

    print(json.dumps(report, indent=2))
    if args.json:
        args.json.parent.mkdir(parents=True, exist_ok=True)
        args.json.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
        print(f"\nwrote {args.json}", file=sys.stderr)

    return 0 if report.get("opens") or "decks" in report else 1


if __name__ == "__main__":
    raise SystemExit(main())
