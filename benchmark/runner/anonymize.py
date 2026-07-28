#!/usr/bin/env python3
"""Build a blinded copy of a benchmark run for scoring.

Knowing you are looking at the 26k-star project moves scores, and it moves them
by more than anyone expects. This copies screenshots into a flat directory under
opaque labels, writes the mapping to a separate file, and leaves it to the
scorer not to read that file until they are done.

    python anonymize.py --run ../results/run-01 --out ../results/run-01/_blind

Scoring happens in _blind/. The key lives at _blind/KEY.json — which is
git-ignored by default so it cannot leak through a PR diff.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import shutil
import sys
from pathlib import Path

IMAGE_SUFFIXES = {".png", ".jpg", ".jpeg", ".webp"}


def label_for(skill: str, corpus: str, salt: str) -> str:
    """Stable but non-obvious label. Deterministic so re-running gives the same
    labels — a scorer who steps away can come back to the same directory."""
    h = hashlib.sha256(f"{salt}:{skill}:{corpus}".encode()).hexdigest()
    return f"entry-{h[:8]}"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--run", required=True, type=Path, help="results/<run-id> directory")
    ap.add_argument("--out", type=Path, help="defaults to <run>/_blind")
    ap.add_argument("--salt", default="many-ppt-skills", help="changes the label mapping")
    args = ap.parse_args()

    run_dir: Path = args.run
    if not run_dir.is_dir():
        sys.exit(f"not a directory: {run_dir}")

    out: Path = args.out or (run_dir / "_blind")
    if out.exists():
        shutil.rmtree(out)
    out.mkdir(parents=True)

    key: dict[str, dict[str, str]] = {}
    copied = 0

    # results/<run-id>/<skill>/<corpus>/...
    for skill_dir in sorted(p for p in run_dir.iterdir() if p.is_dir()):
        if skill_dir.name.startswith("_"):
            continue
        for corpus_dir in sorted(p for p in skill_dir.iterdir() if p.is_dir()):
            label = label_for(skill_dir.name, corpus_dir.name, args.salt)
            dest = out / label
            dest.mkdir(parents=True, exist_ok=True)

            images = [
                p
                for p in sorted(corpus_dir.rglob("*"))
                if p.suffix.lower() in IMAGE_SUFFIXES
            ]
            if not images:
                print(f"  (no screenshots under {corpus_dir} — skipping)", file=sys.stderr)
                continue

            for i, img in enumerate(images, 1):
                # Renaming strips filenames that would give the skill away.
                shutil.copy2(img, dest / f"{i:02d}{img.suffix.lower()}")
                copied += 1

            key[label] = {
                "skill": skill_dir.name,
                "corpus": corpus_dir.name,
                "source": str(corpus_dir.relative_to(run_dir)),
                "images": len(images),
            }
            print(f"  {label}  <-  {skill_dir.name}/{corpus_dir.name}  ({len(images)} shots)")

    if not key:
        sys.exit("nothing to anonymize — expected results/<run>/<skill>/<corpus>/*.png")

    (out / "KEY.json").write_text(json.dumps(key, indent=2) + "\n", encoding="utf-8")
    (out / "README.md").write_text(
        "# Blind scoring set\n\n"
        f"{len(key)} entries, {copied} screenshots.\n\n"
        "Score each `entry-*` directory against [the rubric](../../rubric.md) "
        "**without opening `KEY.json`**.\n\n"
        "Write one `score.json` per entry here, keyed by the entry label. "
        "Un-blind only after every entry is scored.\n",
        encoding="utf-8",
    )

    print(f"\n  {len(key)} entries, {copied} screenshots -> {out}")
    print("  Do not open KEY.json until scoring is finished.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
