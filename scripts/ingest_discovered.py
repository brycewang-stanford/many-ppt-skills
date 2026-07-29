#!/usr/bin/env python3
"""Turn verified discovery results into registry entries.

The pipeline that feeds this:

    discover.py          search GitHub from many angles      -> candidates
    verify_candidates.py does it ship a SKILL.md             -> skills, not apps
    (classification)     is making slides its actual job     -> slide-relevant
    ingest_discovered.py write registry entries              -> data/skills.json

Only the last step is here. It writes bilingual one-liners, because the registry
renders in two languages and a GitHub description only ever comes in one.

    python scripts/ingest_discovered.py --in shortlist.json --classified cls.json

Existing entries are never touched. A repo already in the registry is skipped,
so this is safe to re-run as discovery widens.

**RESCUES.** The classifier is stricter than this registry's own precedent: it
rejects design skills that produce decks among other artifacts, while
`huashu-design` — "prototypes, decks, motion and design critique, not just
slides" — has been in Tier S since day one. Applying two standards to the same
question is the thing that makes a curated list untrustworthy, so the repos below
are re-included by hand, named individually rather than pattern-matched, so the
judgement stays visible and arguable.
"""

from __future__ import annotations

import argparse
import json
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "data" / "skills.json"

# repo -> route. Decks are a named output for every one of these; the classifier
# discounted them for also doing something else.
RESCUE = {
    "JimLiu/baoyu-design": "html",
    "jiji262/claude-design-skill": "html",
    "iamgio/quarkdown": "framework",
    "nexu-io/html-anything": "suite",
    "zLanqing/codex-claude-academic-skills": "suite",
    "SkyworkAI/Skywork-Skills": "suite",
    "QuZhan51496/paper2anything": "suite",
    "huangserva/servasyy_skills": "suite",
    "staruhub/ClaudeSkills": "suite",
}

ROUTE_FALLBACK = {"other": "html", "image": "image", "suite": "suite"}

TAGLINE_SCHEMA = {
    "type": "object",
    "properties": {
        "results": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "repo": {"type": "string"},
                    "name": {"type": "string", "minLength": 2},
                    "tagline_en": {"type": "string", "minLength": 15},
                    "tagline_zh": {"type": "string", "minLength": 6},
                },
                "required": ["repo", "name", "tagline_en", "tagline_zh"],
                "additionalProperties": False,
            },
        }
    },
    "required": ["results"],
    "additionalProperties": False,
}

TAGLINE_PROMPT = """\
`repos.txt` lists GitHub repositories that are agent skills for making
presentation decks. Each line is: repo | route | description.

For each one write:

  name        A short display name, in Title Case. Use the project's real name,
              cleaned up — "GordenSun/GordenPPTSkill" becomes "Gorden PPT Skill".
              Never just echo the owner/name path.
  tagline_en  One sentence, English, describing what it does. Under 100
              characters. No marketing language, no "powerful", no "seamlessly".
              Say the concrete thing: what goes in, what comes out.
  tagline_zh  The same sentence in Simplified Chinese. A translation of the
              English, not a different claim.

Base both taglines only on the description given. Where a description is empty or
uninformative, say plainly what the repo name implies and nothing more — do not
invent features.

Answer for EVERY repo, using the exact repo string given.
"""


def slug(repo: str, taken: set[str]) -> str:
    base = re.sub(r"[^a-z0-9]+", "-", repo.split("/")[-1].lower()).strip("-")
    if base not in taken:
        return base
    owner = re.sub(r"[^a-z0-9]+", "-", repo.split("/")[0].lower()).strip("-")
    cand = f"{base}-{owner}"
    n = 2
    while cand in taken:
        cand, n = f"{base}-{owner}-{n}", n + 1
    return cand


def write_taglines(rows: list[dict], model: str, batch: int = 20) -> dict[str, dict]:
    """Batches are kept small on purpose. At 40 repos a batch the model answered
    for most of them and silently dropped the rest — 31 of 111 entries went
    missing that way, with no error anywhere, because a short array is still a
    schema-valid array."""
    out: dict[str, dict] = {}
    for i in range(0, len(rows), batch):
        chunk = rows[i: i + batch]
        work = Path(tempfile.mkdtemp(prefix="tagline-"))
        (work / "repos.txt").write_text("\n".join(
            f"{r['repo']} | {r['route']} | {(r.get('description') or '')[:220]}"
            for r in chunk))
        try:
            proc = subprocess.run(
                ["claude", "-p", TAGLINE_PROMPT,
                 "--setting-sources", "project", "--strict-mcp-config",
                 "--permission-mode", "bypassPermissions", "--model", model,
                 "--max-budget-usd", "1.5", "--no-session-persistence",
                 "--json-schema", json.dumps(TAGLINE_SCHEMA),
                 "--output-format", "json"],
                cwd=work, capture_output=True, text=True, timeout=900)
            payload = json.loads(proc.stdout).get("structured_output") or {}
            for r in payload.get("results", []):
                out[r["repo"]] = r
        except (subprocess.SubprocessError, json.JSONDecodeError) as exc:
            print(f"  batch {i // batch + 1} failed: {exc}", file=sys.stderr)
        finally:
            shutil.rmtree(work, ignore_errors=True)
        print(f"  batch {i // batch + 1}: {len(out)} written so far",
              file=sys.stderr, flush=True)
    return out


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--in", dest="src", required=True, type=Path)
    ap.add_argument("--classified", required=True, type=Path)
    ap.add_argument("--model", default="sonnet")
    ap.add_argument("--min-stars", type=int, default=10)
    ap.add_argument("--batch", type=int, default=20)
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    meta = {c["repo"]: c for c in json.loads(args.src.read_text())}
    verdicts = {c["repo"]: c for c in json.loads(args.classified.read_text())}

    registry = json.loads(SKILLS.read_text())
    known_repos = {s["repo"].lower() for s in registry["skills"]}
    known_repos |= {s["repo"].lower() for s in registry.get("lists", [])}
    taken_ids = {s["id"] for s in registry["skills"]}

    rows = []
    for repo, v in verdicts.items():
        if repo.lower() in known_repos or repo not in meta:
            continue
        if meta[repo]["stars"] < args.min_stars:
            continue
        if repo in RESCUE:
            route = RESCUE[repo]
        elif v["slide_relevant"]:
            route = ROUTE_FALLBACK.get(v["route"], v["route"])
        else:
            continue
        rows.append({**meta[repo], "route": route})

    rows.sort(key=lambda r: -r["stars"])
    print(f"{len(rows)} new entries "
          f"({sum(1 for r in rows if r['repo'] in RESCUE)} rescued by hand)")
    if args.dry_run:
        for r in rows[:20]:
            print(f"  {r['stars']:>6,} {r['route']:10s} {r['repo']}")
        return 0

    print("writing bilingual taglines ...")
    taglines = write_taglines(rows, args.model, args.batch)

    added = 0
    for r in rows:
        t = taglines.get(r["repo"])
        if not t:
            print(f"  no tagline for {r['repo']}, skipped", file=sys.stderr)
            continue
        sid = slug(r["repo"], taken_ids)
        taken_ids.add(sid)
        entry = {
            "id": sid,
            "repo": r["repo"],
            "name": t["name"],
            "author": r["repo"].split("/")[0],
            "route": r["route"],
            "license_note": r.get("license") or "Unspecified",
            "lang": "zh" if re.search(r"[一-鿿]", r.get("description") or "")
                    else "en",
            "tagline_en": t["tagline_en"],
            "tagline_zh": t["tagline_zh"],
            "source": "discovered",
        }
        registry["skills"].append(entry)
        added += 1

    SKILLS.write_text(json.dumps(registry, indent=2, ensure_ascii=False) + "\n")
    print(f"\nadded {added} entries — registry now holds {len(registry['skills'])}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
