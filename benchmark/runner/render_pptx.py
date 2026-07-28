#!/usr/bin/env python3
"""Rasterise a .pptx to one PNG per slide, so the PPTX route can be judged.

`screenshot.py` drives a browser and only handles the HTML route. `probe_pptx.py`
answers whether the objects inside a .pptx are native, which no image can show.
Neither of them lets anyone *look* at a PPTX deck, and rubric dimensions 1-3 are
scored from images at presentation size for both routes.

This closes that gap the way the rubric already prescribes:

    soffice --headless --convert-to pdf deck.pptx && pdftoppm -png -r 96 deck.pdf

    python render_pptx.py --deck deck.pptx --out shots/

The renderer is LibreOffice, not PowerPoint, and that is a real limitation rather
than a detail: LibreOffice substitutes fonts it does not have and can lay out
text slightly differently. Font substitutions are detected and reported, because
a deck judged on a substituted font is being judged on something its author did
not ship. Where a run's typography score depends on it, open the file in
PowerPoint before trusting the images.
"""

from __future__ import annotations

import argparse
import json
import re
import shutil
import subprocess
import sys
import tempfile
import zipfile
from pathlib import Path


def require(binary: str, hint: str) -> str:
    path = shutil.which(binary)
    if not path:
        sys.exit(f"{binary} not found on PATH — {hint}")
    return path


def embedded_fonts(deck: Path) -> list[str]:
    """Fonts the deck ships. Anything it asks for but does not ship is a
    substitution risk in LibreOffice."""
    with zipfile.ZipFile(deck) as z:
        return [n for n in z.namelist() if re.match(r"^ppt/fonts/", n)]


def requested_fonts(deck: Path) -> list[str]:
    with zipfile.ZipFile(deck) as z:
        xml = "\n".join(
            z.read(n).decode("utf-8", "replace")
            for n in z.namelist()
            if n.startswith("ppt/slides/slide") and n.endswith(".xml")
        )
    return sorted({m for m in re.findall(r'typeface="([^"]+)"', xml)
                   if m and not m.startswith("+")})


def installed_fonts() -> set[str]:
    try:
        out = subprocess.run(["fc-list", "--format", "%{family}\n"],
                             capture_output=True, text=True, timeout=30).stdout
    except (FileNotFoundError, subprocess.SubprocessError):
        return set()
    return {f.strip().lower() for line in out.splitlines() for f in line.split(",")}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--deck", required=True, type=Path)
    ap.add_argument("--out", required=True, type=Path)
    ap.add_argument("--dpi", type=int, default=144,
                    help="144 gives ~1920px wide for a 13.3in slide")
    ap.add_argument("--json", type=Path, help="write a render report")
    args = ap.parse_args()

    if not args.deck.exists():
        sys.exit(f"deck not found: {args.deck}")
    soffice = require("soffice", "install LibreOffice")
    require("pdftoppm", "install poppler (brew install poppler)")

    args.out.mkdir(parents=True, exist_ok=True)
    work = Path(tempfile.mkdtemp(prefix="pptx-render-"))

    # LibreOffice writes into --outdir using the source basename. A dedicated
    # profile directory keeps a headless run from colliding with a desktop
    # LibreOffice the operator happens to have open.
    proc = subprocess.run(
        [soffice, "--headless", "--norestore",
         f"-env:UserInstallation=file://{work / 'profile'}",
         "--convert-to", "pdf", "--outdir", str(work), str(args.deck.resolve())],
        capture_output=True, text=True, timeout=600,
    )
    pdf = work / (args.deck.stem + ".pdf")
    if not pdf.exists():
        print(proc.stdout, proc.stderr, file=sys.stderr)
        shutil.rmtree(work, ignore_errors=True)
        sys.exit("LibreOffice produced no PDF")

    subprocess.run(["pdftoppm", "-png", "-r", str(args.dpi), str(pdf),
                    str(args.out / "slide")], check=True, timeout=600)

    # pdftoppm writes slide-1.png / slide-01.png depending on page count; restate
    # them zero-padded so lexical order is slide order for every downstream tool.
    shots = sorted(args.out.glob("slide-*.png"),
                   key=lambda p: int(re.search(r"(\d+)", p.stem).group(1)))
    for i, p in enumerate(shots, 1):
        target = args.out / f"slide-{i:02d}.png"
        if p != target:
            p.rename(target)
    shots = sorted(args.out.glob("slide-*.png"))

    have = installed_fonts()
    wanted = requested_fonts(args.deck)
    missing = [f for f in wanted if f.lower() not in have] if have else []

    report = {
        "deck": str(args.deck),
        "slides_rendered": len(shots),
        "dpi": args.dpi,
        "renderer": "LibreOffice (not PowerPoint)",
        "fonts_requested": wanted,
        "fonts_embedded": embedded_fonts(args.deck),
        "fonts_missing_locally": missing,
        "substitution_risk": bool(missing),
        "caveat": (
            "Rendered by LibreOffice. Missing fonts are substituted, so typography "
            "scored from these images may not be the typography the deck ships."
        ),
    }
    if args.json:
        args.json.write_text(json.dumps(report, indent=2) + "\n")

    shutil.rmtree(work, ignore_errors=True)

    print(f"deck   : {args.deck}")
    print(f"slides : {len(shots)} PNG(s) at {args.dpi} dpi -> {args.out}")
    if missing:
        print(f"WARNING: {len(missing)} requested font(s) not installed and not embedded:")
        for f in missing:
            print(f"         {f}")
        print("         typography in these images is a substitution, not the deck's own")
    return 0 if shots else 1


if __name__ == "__main__":
    raise SystemExit(main())
