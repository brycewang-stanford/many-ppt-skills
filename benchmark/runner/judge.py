#!/usr/bin/env python3
"""Blind panel scoring — an executable version of rubric.md's scoring procedure.

The first run in this repo was scored by the same operator who generated it
(`blind: false`, `operator_conflict: true`). That is disclosed honestly, and it
is still the one thing that stops a score being a ranking. This script exists to
remove the conflict rather than keep disclosing it.

It implements the five steps the rubric already publishes, without improvising:

  1. **Blind.** Judges receive screenshots under an opaque entry label. The skill
     name, repo, template names and `run.json` never enter the judge's directory.
  2. **Mechanical dimensions first.** Data fidelity (4) is taken from
     `check_fidelity.py`, not from an opinion. Deliverable integrity (6) is
     handed the measured facts — remote dependency count, file count, size — so
     the judge maps anchors rather than guesses.
  3. **Dimensions 1-3 from screenshots only.** The judge is given images. It is
     never given the deck source, because the audience does not read source and
     because CSS comments leak the skill's identity.
  4. **Evidence required.** The output schema makes an empty citation invalid, so
     "no citation, no score" is enforced by the parser rather than by good
     intentions.
  5. **Two independent judges.** Where they differ by >=2 on a dimension, the
     lower score stands and the disagreement is published.

Dimension 7 (effort to acceptable) is *not* scored. It counts correction turns,
and this harness runs single-shot with zero correction turns — emitting 5 would
mean "perfect first time" when the truth is "never asked for a revision". It is
recorded as null with that reason attached.

    python judge.py --run run-01 --skill frontend-slides --corpus 02-quarterly-review

Writes `score.judged.json` beside the deck. Never overwrites a human `score.json`.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
RESULTS = ROOT / "benchmark" / "results"
RUBRIC = ROOT / "benchmark" / "rubric.md"

# Scored by the panel from images. Dimension 4 is mechanical; 7 is unmeasurable
# single-shot. Keeping this list explicit stops a future edit from quietly
# handing a gating dimension to an opinion.
JUDGED_DIMS = [
    "visual_distinctiveness",
    "typographic_craft",
    "hierarchy_density",
    "content_fidelity",
    "deliverable_integrity",
]

SCHEMA = {
    "type": "object",
    "properties": {
        d: {
            "type": "object",
            "properties": {
                "score": {"type": "integer", "minimum": 0, "maximum": 5},
                "evidence": {"type": "string", "minLength": 40},
            },
            "required": ["score", "evidence"],
            "additionalProperties": False,
        }
        for d in JUDGED_DIMS
    },
    "required": JUDGED_DIMS,
    "additionalProperties": False,
}

PROMPT = """\
You are scoring one anonymous presentation deck against a published rubric.

Read `rubric.md` in full first. It is the only standard that applies; do not
substitute your own taste for its anchors.

Then look at **every** screenshot in `shots/`. These are the delivered slides at
presentation size. Score dimensions 1-3 from these images alone — that is how the
audience meets this deck.

`corpus.md` is the source material the deck was generated from. Use it to score
content fidelity (dimension 5): whether the argument survived, and whether
anything was invented.

`measured.json` contains facts already established mechanically. Treat them as
ground truth and map them onto the dimension-6 anchors rather than re-deriving
them.

You do not know which skill produced this deck, and you must not guess or
speculate about it in your evidence.

Score these five dimensions, 0-5, strictly against the rubric's anchors:

  visual_distinctiveness  (rubric 1 — apply the automatic deductions)
  typographic_craft       (rubric 2)
  hierarchy_density       (rubric 3 — score against the density the corpus asks
                           for, and run the action-title check if it applies)
  content_fidelity        (rubric 5 — gating; 0 if substantive content is invented)
  deliverable_integrity   (rubric 6 — use measured.json)

Every score needs evidence citing a specific screenshot filename or a specific
measured fact. A score whose evidence does not name concrete observations is
worthless. Be specific about what you actually see, and state what kept a score
from being one point higher.

Anchor discipline matters more than generosity. A 3 means "competent and
inoffensive" and is a normal, respectable score. Reserve 5 for work that meets
the rubric's own description of a 5.
"""


def sha16(text: str) -> str:
    return hashlib.sha256(text.encode()).hexdigest()[:16]


def measure_deliverable(deck_dir: Path) -> dict:
    """Facts for dimension 6. Counting, not judging.

    Only the delivered artifact counts. Screenshots and harness output live
    alongside it in a results directory but are not part of what a recipient
    receives, and counting them would inflate both the file count and the size.
    """
    HARNESS = {"shots", "workspace", "_blind"}
    HARNESS_FILES = {"fidelity.json", "score.json", "score.judged.json",
                     "run.json", "agent.log", "README.md"}
    files = [
        p for p in deck_dir.rglob("*")
        if p.is_file()
        and not (HARNESS & set(p.relative_to(deck_dir).parts))
        and p.name not in HARNESS_FILES
    ]
    html = [p for p in files if p.suffix.lower() == ".html"]
    text = "\n".join(p.read_text(errors="replace") for p in html)

    # Remote runtime dependencies: the rubric's own objective metric is "count of
    # non-data: remote URLs in the artifact".
    urls = re.findall(r"""(?:src|href)\s*=\s*["'](https?://[^"']+)""", text)
    hosts = sorted({re.sub(r"^https?://([^/]+).*$", r"\1", u) for u in urls})

    return {
        "file_count": len(files),
        "html_file_count": len(html),
        "total_kb": round(sum(p.stat().st_size for p in files) / 1024, 1),
        "remote_dependency_count": len(urls),
        "remote_hosts": hosts,
        "self_contained": len(urls) == 0 and len(files) == 1,
        "note": (
            "remote_dependency_count > 0 means the deck breaks offline or when the "
            "CDN moves — rubric 6 anchor 3."
        ),
    }


def build_judge_dir(shots: list[Path], corpus: Path, measured: dict) -> Path:
    """A judging directory outside the repo, holding only what a blind judge may see.

    Deliberately not under benchmark/results: an agent with filesystem access and
    a cwd inside the repo can read its way to the answer, and the point of this
    directory is that the answer is not reachable from it.
    """
    d = Path(tempfile.mkdtemp(prefix="ppt-judge-"))
    (d / "shots").mkdir()
    for i, s in enumerate(sorted(shots), 1):
        shutil.copyfile(s, d / "shots" / f"slide-{i:02d}{s.suffix}")
    shutil.copyfile(RUBRIC, d / "rubric.md")
    shutil.copyfile(corpus, d / "corpus.md")
    (d / "measured.json").write_text(json.dumps(measured, indent=2))
    return d


def run_judge(judge_dir: Path, model: str, budget: float) -> dict | None:
    """One independent judge. Returns parsed scores, or None if it failed."""
    proc = subprocess.run(
        [
            "claude", "-p", PROMPT,
            "--setting-sources", "project",   # empty here: no skills reach the judge
            "--strict-mcp-config",
            "--permission-mode", "bypassPermissions",
            "--model", model,
            "--max-budget-usd", str(budget),
            "--no-session-persistence",
            "--json-schema", json.dumps(SCHEMA),
            "--output-format", "json",
        ],
        cwd=judge_dir, capture_output=True, text=True,
    )
    if proc.returncode != 0:
        print(f"  judge failed (exit {proc.returncode}): {proc.stderr[:300]}",
              file=sys.stderr)
        return None
    try:
        envelope = json.loads(proc.stdout)
    except json.JSONDecodeError as exc:
        print(f"  unparseable judge envelope: {exc}", file=sys.stderr)
        return None

    # `result` holds the agent's prose summary; the schema-validated object lands
    # in `structured_output`. Reading `result` here would silently discard every
    # score, so treat a missing key as a failed judge rather than falling back.
    payload = envelope.get("structured_output")
    if payload is None:
        print("  judge returned no structured_output — discarding", file=sys.stderr)
        return None
    if isinstance(payload, str):
        try:
            payload = json.loads(payload)
        except json.JSONDecodeError as exc:
            print(f"  unparseable structured_output: {exc}", file=sys.stderr)
            return None
    if not all(d in payload for d in JUDGED_DIMS):
        print("  judge output missing dimensions — discarding", file=sys.stderr)
        return None
    return payload


def reconcile(verdicts: list[dict]) -> tuple[dict, list[dict]]:
    """Rubric step 5: where judges differ, the lower score stands, and a spread
    of >=2 is published rather than averaged away.

    The lower score stands on *any* disagreement, not just a spread of 2. The
    obvious alternative — average the panel and round — is worse than it looks:
    Python's round() is banker's rounding, so a [4,3] split silently becomes 4
    while a [3,2] split becomes 2. A benchmark cannot have a tie-break rule whose
    direction depends on whether the scores happen to straddle an even number.
    Taking the lower is deterministic, matches the rubric's stated direction for
    the case it does specify, and errs against the deck under test.
    """
    final, disagreements = {}, []
    for dim in JUDGED_DIMS:
        scores = [v[dim]["score"] for v in verdicts]
        spread = max(scores) - min(scores)
        chosen = min(scores)
        final[dim] = {
            "score": chosen,
            "panel": scores,
            "evidence": [v[dim]["evidence"] for v in verdicts],
        }
        if spread >= 2:
            disagreements.append({
                "dimension": dim, "scores": scores, "spread": spread,
                "resolution": "lower score stands (rubric scoring procedure, step 5)",
            })
    return final, disagreements


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--run", required=True)
    ap.add_argument("--skill", required=True)
    ap.add_argument("--corpus", required=True, help="corpus id, e.g. 02-quarterly-review")
    ap.add_argument("--judges", type=int, default=2, help="rubric requires two")
    ap.add_argument("--model", default="sonnet")
    ap.add_argument("--budget", type=float, default=2.0)
    ap.add_argument("--keep-judge-dir", action="store_true")
    args = ap.parse_args()

    entry = RESULTS / args.run / args.skill / args.corpus
    if not entry.is_dir():
        return print(f"no such entry: {entry}", file=sys.stderr) or 2

    shots = sorted(p for p in entry.rglob("shots/*.png")
                   if "contact-sheet" not in p.name)
    if not shots:
        return print(f"no screenshots under {entry}", file=sys.stderr) or 2

    corpus_file = next(
        (p for p in (ROOT / "benchmark" / "corpus").glob(f"{args.corpus}*.md")), None)
    if corpus_file is None:
        return print(f"no corpus file for {args.corpus}", file=sys.stderr) or 2

    deck_dir = entry / "deck" if (entry / "deck").is_dir() else entry
    measured = measure_deliverable(deck_dir)

    fidelity_file = entry / "fidelity.json"
    fidelity = json.loads(fidelity_file.read_text()) if fidelity_file.exists() else None

    print(f"▶ judging {args.skill} × {args.corpus} — {len(shots)} slides, "
          f"{args.judges} blind judges ({args.model})", flush=True)

    judge_dir = build_judge_dir(shots, corpus_file, measured)
    verdicts = []
    for i in range(args.judges):
        print(f"  judge {i + 1}/{args.judges} ...", flush=True)
        v = run_judge(judge_dir, args.model, args.budget)
        if v:
            verdicts.append(v)
    if not args.keep_judge_dir:
        shutil.rmtree(judge_dir, ignore_errors=True)

    if len(verdicts) < 2:
        print(f"only {len(verdicts)} judge(s) returned — the rubric requires two. "
              f"Not writing a score.", file=sys.stderr)
        return 1

    final, disagreements = reconcile(verdicts)

    out = {
        "skill": args.skill,
        "corpus": args.corpus,
        "run_id": args.run,
        "blind": True,
        "scored_by": [f"llm-judge:{args.model}"] * len(verdicts),
        "operator_conflict": False,
        "self_reported": False,
        "judge_count": len(verdicts),
        "judge_prompt_sha256": sha16(PROMPT),
        "rubric_sha256": sha16(RUBRIC.read_text()),
        "scores": {d: final[d]["score"] for d in JUDGED_DIMS},
        "data_fidelity": {
            "score": None if fidelity is None else (
                5 if fidelity.get("coverage_pct") == 100.0
                and not fidelity.get("fabricated") else None),
            "source": "check_fidelity.py (mechanical)",
            "coverage_pct": None if fidelity is None else fidelity.get("coverage_pct"),
            "fabricated": None if fidelity is None else fidelity.get("fabricated"),
        },
        "effort_to_acceptable": {
            "score": None,
            "reason": (
                "Not measurable. This dimension counts correction turns; the "
                "automated harness runs single-shot and never requests a revision, "
                "so any score here would be an artifact of the method."
            ),
        },
        "measured": measured,
        "disagreements": disagreements,
        "evidence": {d: final[d]["evidence"] for d in JUDGED_DIMS},
        "panel_scores": {d: final[d]["panel"] for d in JUDGED_DIMS},
    }

    dest = entry / "score.judged.json"
    dest.write_text(json.dumps(out, indent=2) + "\n")

    judged_total = sum(out["scores"].values())
    print(f"  judged subtotal {judged_total}/25 across {len(JUDGED_DIMS)} dimensions")
    for d in JUDGED_DIMS:
        print(f"    {d:24s} {final[d]['score']}  panel={final[d]['panel']}")
    if disagreements:
        print(f"  {len(disagreements)} disagreement(s) >=2 — lower score stood")
    print(f"  wrote {dest.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
