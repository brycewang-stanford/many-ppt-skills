#!/usr/bin/env python3
"""Diff every number in a generated deck against the corpus that produced it.

Dimensions 4 and 5 of the rubric are gating, and eyeballing them does not work —
a fabricated figure looks exactly like a real one. This extracts numeric tokens
from both sides and reports what went missing and what got invented.

Handles .html, .pptx, .pdf (via pdftotext) and .md decks.

    python check_fidelity.py --corpus ../corpus/02-quarterly-review.md \\
                             --deck   ../results/run-01/frontend-slides/

Exit code is 1 when anything was fabricated, so it can gate CI.
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
import zipfile
from html.parser import HTMLParser
from pathlib import Path

# Matches money, percentages, decimals, thousands-separated integers and bare
# integers, with an optional trailing unit. Ordered longest-first so "$47.2M"
# is captured whole rather than as "47.2".
NUM = re.compile(
    r"""
    (?P<sign>[-−+]?)
    (?P<cur>[$€£¥])?
    (?P<num>\d{1,3}(?:,\d{3})+(?:\.\d+)?   # 1,122  47,200.5
        |\d+\.\d+                           # 47.2
        |\d+)                               # 812
    \s*
    (?P<unit>%|bps|[MBK]\b|hrs?\b|GB\b|MB\b|sq\ ft\b|ms\b|s\b)?
    """,
    re.VERBOSE,
)

# Numbers that carry no factual weight and would drown the signal.
IGNORE_BARE = set(range(0, 33))  # slide numbers, list indices, small counts
YEAR = re.compile(r"^(19|20)\d{2}$")


class _Text(HTMLParser):
    """Strip tags, dropping script/style content entirely."""

    def __init__(self) -> None:
        super().__init__()
        self.parts: list[str] = []
        self._skip = 0

    def handle_starttag(self, tag: str, attrs) -> None:
        if tag in ("script", "style"):
            self._skip += 1

    def handle_endtag(self, tag: str) -> None:
        if tag in ("script", "style") and self._skip:
            self._skip -= 1

    def handle_data(self, data: str) -> None:
        if not self._skip:
            self.parts.append(data)

    def text(self) -> str:
        return " ".join(self.parts)


def from_html(p: Path) -> str:
    parser = _Text()
    parser.feed(p.read_text(encoding="utf-8", errors="replace"))
    return parser.text()


def from_pptx(p: Path) -> str:
    """Pull text from slide XML. Avoids a python-pptx dependency on purpose —
    the harness should run anywhere without a virtualenv."""
    out: list[str] = []
    with zipfile.ZipFile(p) as z:
        names = sorted(n for n in z.namelist() if re.match(r"ppt/slides/slide\d+\.xml$", n))
        for n in names:
            xml = z.read(n).decode("utf-8", errors="replace")
            # <a:t> holds every run of visible text.
            out.extend(re.findall(r"<a:t>(.*?)</a:t>", xml, re.DOTALL))
    return " ".join(out)


def from_pdf(p: Path) -> str:
    try:
        r = subprocess.run(
            ["pdftotext", str(p), "-"], capture_output=True, text=True, timeout=120
        )
        if r.returncode == 0:
            return r.stdout
        print(f"  !! pdftotext failed on {p.name}: {r.stderr.strip()[:120]}", file=sys.stderr)
    except FileNotFoundError:
        print("  !! pdftotext not installed — skipping PDF (brew install poppler)", file=sys.stderr)
    except subprocess.TimeoutExpired:
        print(f"  !! pdftotext timed out on {p.name}", file=sys.stderr)
    return ""


EXTRACTORS = {
    ".html": from_html,
    ".htm": from_html,
    ".pptx": from_pptx,
    ".pdf": from_pdf,
    ".md": lambda p: p.read_text(encoding="utf-8", errors="replace"),
    ".txt": lambda p: p.read_text(encoding="utf-8", errors="replace"),
}


# Corpus files open with a brief addressed to the operator — target length,
# failure modes, worked examples of action titles. Those numbers are
# instructions, not content to reproduce, and counting them makes every honest
# run look like it dropped figures. Everything from this heading onward is the
# material under test.
CONTENT_MARKER = "## Content"


def content_only(text: str) -> str:
    """Trim a corpus file to the part a deck is actually expected to carry."""
    idx = text.find(CONTENT_MARKER)
    return text[idx:] if idx != -1 else text


def read_any(target: Path) -> tuple[str, list[Path]]:
    """Concatenate text from a file, or from every supported file in a directory."""
    if not target.exists():
        sys.exit(f"path does not exist: {target}")
    if target.is_file():
        fn = EXTRACTORS.get(target.suffix.lower())
        if not fn:
            sys.exit(f"unsupported file type: {target.suffix}")
        return fn(target), [target]

    chunks, used = [], []
    for p in sorted(target.rglob("*")):
        fn = EXTRACTORS.get(p.suffix.lower())
        if fn and p.is_file():
            chunks.append(fn(p))
            used.append(p)
    if not used:
        sys.exit(f"no supported files found under {target}")
    return "\n".join(chunks), used


def normalize(m: re.Match) -> str:
    """Canonical form so '$47.2M', '47.2M' and '47.2 M' compare equal."""
    num = m.group("num").replace(",", "")
    # Trailing zeros are not meaningful: 12.40 == 12.4
    if "." in num:
        num = num.rstrip("0").rstrip(".")
    unit = (m.group("unit") or "").strip().lower()
    unit = {"hr": "hrs", "b": "B", "m": "M", "k": "K"}.get(unit, unit)
    sign = "-" if m.group("sign") in ("-", "−") else ""
    return f"{sign}{num}{unit}"


def extract(text: str) -> dict[str, int]:
    counts: dict[str, int] = {}
    for m in NUM.finditer(text):
        tok = normalize(m)
        bare = not (m.group("unit") or m.group("cur"))
        if bare:
            stripped = tok.lstrip("-")
            if YEAR.match(stripped):
                continue
            try:
                if float(stripped) in IGNORE_BARE:
                    continue
            except ValueError:
                pass
        counts[tok] = counts.get(tok, 0) + 1
    return counts


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--corpus", required=True, type=Path)
    ap.add_argument("--deck", required=True, type=Path)
    ap.add_argument("--json", type=Path, help="write the report here as JSON")
    ap.add_argument(
        "--strict",
        action="store_true",
        help="also fail on missing figures, not just fabricated ones",
    )
    args = ap.parse_args()

    corpus_text, _ = read_any(args.corpus)
    deck_text, deck_files = read_any(args.deck)

    want = extract(content_only(corpus_text))

    # Pointing --deck at the corpus itself is the harness self-test: it proves
    # the extractor round-trips. Trim both sides there, or the operator brief
    # leaks into the deck side and reads as fabrication.
    self_test = args.deck.resolve() == args.corpus.resolve()
    got = extract(content_only(deck_text) if self_test else deck_text)

    missing = sorted(k for k in want if k not in got)
    kept = sorted(k for k in want if k in got)

    # A deck legitimately writes "customs declined 15.8%" where the source table
    # says "-15.8%". Same fact, opposite sign convention. Reporting that as
    # fabrication would fire on almost every honest run, so split it out: these
    # need a wording check, not a fabrication verdict.
    def unsigned(tok: str) -> str:
        return tok.lstrip("-")

    want_unsigned = {unsigned(k) for k in want}
    fabricated, sign_diffs = [], []
    for k in sorted(got):
        if k in want:
            continue
        (sign_diffs if unsigned(k) in want_unsigned else fabricated).append(k)

    coverage = len(kept) / len(want) * 100 if want else 100.0

    print(f"corpus : {args.corpus}")
    print(f"deck   : {args.deck}  ({len(deck_files)} file(s))")
    print(f"\n  figures in corpus : {len(want)}")
    print(f"  reproduced        : {len(kept)}  ({coverage:.0f}%)")
    print(f"  missing           : {len(missing)}")
    print(f"  FABRICATED        : {len(fabricated)}")

    if missing:
        print("\n  Missing from deck:")
        for k in missing:
            print(f"    − {k}")

    if sign_diffs:
        print("\n  Sign/direction differences (check the wording, not fabrication):")
        for k in sign_diffs:
            print(f"    ± {k}  (x{got[k]})")

    if fabricated:
        print("\n  ⚠️  Present in deck but NOT in corpus:")
        for k in fabricated:
            print(f"    + {k}  (x{got[k]})")
        print(
            "\n  Review each one by hand before scoring. Page numbers, computed\n"
            "  totals and axis ticks are legitimate; a new business figure is not.\n"
            "  Rubric dimension 4 gates to 0 on any fabricated figure."
        )

    if args.json:
        args.json.parent.mkdir(parents=True, exist_ok=True)
        args.json.write_text(
            json.dumps(
                {
                    "corpus": str(args.corpus),
                    "deck": str(args.deck),
                    "coverage_pct": round(coverage, 1),
                    "kept": kept,
                    "missing": missing,
                    "fabricated": {k: got[k] for k in fabricated},
                    "sign_diffs": {k: got[k] for k in sign_diffs},
                },
                indent=2,
            )
            + "\n",
            encoding="utf-8",
        )
        print(f"\n  wrote {args.json}")

    if fabricated:
        return 1
    if args.strict and missing:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
