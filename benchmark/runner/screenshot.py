#!/usr/bin/env python3
"""Capture every slide of an HTML deck as a PNG at 1920x1080.

Screenshots are the point of this benchmark. Rubric dimensions 1-3 are scored
from images at presentation size, never by reading source, because that is how
an audience meets the deck.

    pip install playwright && playwright install chromium
    python screenshot.py --deck ../results/run-01/frontend-slides/deck.html \\
                         --out  ../results/run-01/frontend-slides/shots/

Navigation is auto-detected: decks that expose sibling slide elements are walked
directly; anything else falls back to pressing ArrowRight.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

# Selectors covering the conventions this ecosystem has converged on. Ordered
# most- to least- specific.
SLIDE_SELECTORS = [
    ".slide",
    "section.slide",
    "[data-slide]",
    ".reveal .slides > section",
    "section",
    ".page",
]


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--deck", required=True, type=Path, help=".html file to capture")
    ap.add_argument("--out", required=True, type=Path, help="output directory for PNGs")
    ap.add_argument("--width", type=int, default=1920)
    ap.add_argument("--height", type=int, default=1080)
    ap.add_argument("--max-slides", type=int, default=60, help="safety cap")
    ap.add_argument("--settle-ms", type=int, default=700, help="wait for entrance animations")
    ap.add_argument("--contact-sheet", action="store_true", help="also write a tiled contact sheet")
    args = ap.parse_args()

    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        print(
            "playwright not installed:\n"
            "  pip install playwright && playwright install chromium",
            file=sys.stderr,
        )
        return 1

    if not args.deck.exists():
        print(f"deck not found: {args.deck}", file=sys.stderr)
        return 1

    args.out.mkdir(parents=True, exist_ok=True)
    shots: list[Path] = []

    with sync_playwright() as pw:
        browser = pw.chromium.launch()
        page = browser.new_page(viewport={"width": args.width, "height": args.height})
        page.goto(args.deck.resolve().as_uri(), wait_until="networkidle")
        page.wait_for_timeout(args.settle_ms)

        # Find the selector that yields the most elements — decks nest <section>
        # inside .slide often enough that "first match wins" picks wrong.
        best, count = None, 0
        for sel in SLIDE_SELECTORS:
            n = page.locator(sel).count()
            if n > count:
                best, count = sel, n

        if best and count > 1:
            print(f"  {count} slides via `{best}`")
            total = min(count, args.max_slides)
            for i in range(total):
                # Reveal one slide at a time. Decks gate visibility on .active /
                # .visible rather than display:none precisely so transitions work,
                # so drive those classes instead of style.
                page.evaluate(
                    """([sel, idx]) => {
                        const els = document.querySelectorAll(sel);
                        els.forEach((el, i) => {
                            el.classList.toggle('active',  i === idx);
                            el.classList.toggle('visible', i === idx);
                            el.style.visibility = i === idx ? 'visible' : 'hidden';
                        });
                        window.scrollTo(0, 0);
                    }""",
                    [best, i],
                )
                page.wait_for_timeout(args.settle_ms)
                p = args.out / f"slide-{i + 1:02d}.png"
                page.screenshot(path=str(p))
                shots.append(p)
        else:
            print("  no slide elements found — walking with ArrowRight")
            seen: set[bytes] = set()
            for i in range(args.max_slides):
                p = args.out / f"slide-{i + 1:02d}.png"
                page.screenshot(path=str(p))
                data = p.read_bytes()
                # An unchanged frame means we ran off the end of the deck.
                if data in seen:
                    p.unlink()
                    break
                seen.add(data)
                shots.append(p)
                page.keyboard.press("ArrowRight")
                page.wait_for_timeout(args.settle_ms)

        browser.close()

    print(f"  wrote {len(shots)} screenshots to {args.out}")

    if args.contact_sheet and shots:
        _contact_sheet(shots, args.out / "contact-sheet.png")
    return 0


def _contact_sheet(shots: list[Path], dest: Path, cols: int = 4, thumb_w: int = 480) -> None:
    """Tile the slides into one shareable image. Optional — needs Pillow."""
    try:
        from PIL import Image
    except ImportError:
        print("  (skipping contact sheet — pip install Pillow)", file=sys.stderr)
        return

    thumbs = []
    for p in shots:
        im = Image.open(p).convert("RGB")
        h = int(im.height * thumb_w / im.width)
        thumbs.append(im.resize((thumb_w, h), Image.LANCZOS))

    tw, th = thumbs[0].size
    rows = (len(thumbs) + cols - 1) // cols
    gap = 12
    sheet = Image.new(
        "RGB",
        (cols * tw + (cols + 1) * gap, rows * th + (rows + 1) * gap),
        (18, 18, 20),
    )
    for i, t in enumerate(thumbs):
        r, c = divmod(i, cols)
        sheet.paste(t, (gap + c * (tw + gap), gap + r * (th + gap)))
    sheet.save(dest)
    print(f"  wrote contact sheet {dest}")


if __name__ == "__main__":
    raise SystemExit(main())
