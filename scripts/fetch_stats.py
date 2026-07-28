#!/usr/bin/env python3
"""Refresh live GitHub stats for every repo in data/skills.json.

Curated content lives in data/skills.json and is never touched here.
Derived numbers land in data/stats.json. Keeping them apart means a failed
or rate-limited fetch can never corrupt hand-written research.

Usage:
    python scripts/fetch_stats.py              # refresh all
    python scripts/fetch_stats.py --check      # exit 1 if stats are stale/missing
"""

from __future__ import annotations

import argparse
import json
import os
import sys
import time
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILLS = ROOT / "data" / "skills.json"
STATS = ROOT / "data" / "stats.json"
API = "https://api.github.com/repos/{repo}"


def _headers() -> dict[str, str]:
    h = {
        "Accept": "application/vnd.github+json",
        "User-Agent": "many-ppt-skills-stats-bot",
    }
    # GITHUB_TOKEN lifts the rate limit from 60/hr to 5000/hr. Optional locally,
    # always present in CI.
    token = os.environ.get("GITHUB_TOKEN")
    if token:
        h["Authorization"] = f"Bearer {token}"
    return h


def fetch(repo: str, retries: int = 3) -> dict | None:
    req = urllib.request.Request(API.format(repo=repo), headers=_headers())
    for attempt in range(retries):
        try:
            with urllib.request.urlopen(req, timeout=30) as resp:
                d = json.load(resp)
            return {
                "stars": d["stargazers_count"],
                "forks": d["forks_count"],
                "open_issues": d["open_issues_count"],
                "license": (d.get("license") or {}).get("spdx_id"),
                "created_at": d["created_at"][:10],
                "pushed_at": d["pushed_at"][:10],
                "archived": d["archived"],
                "homepage": d.get("homepage") or None,
                "default_branch": d.get("default_branch", "main"),
            }
        except urllib.error.HTTPError as e:
            if e.code == 404:
                print(f"  !! {repo}: not found (renamed or deleted?)", file=sys.stderr)
                return None
            if e.code in (403, 429) and attempt < retries - 1:
                wait = 2 ** (attempt + 3)
                print(f"  .. {repo}: rate limited, sleeping {wait}s", file=sys.stderr)
                time.sleep(wait)
                continue
            print(f"  !! {repo}: HTTP {e.code}", file=sys.stderr)
            return None
        except (urllib.error.URLError, KeyError, json.JSONDecodeError) as e:
            if attempt < retries - 1:
                time.sleep(2)
                continue
            print(f"  !! {repo}: {e}", file=sys.stderr)
            return None
    return None


def all_repos(data: dict) -> list[str]:
    seen, out = set(), []
    for entry in data["skills"] + data.get("lists", []):
        repo = entry["repo"]
        if repo not in seen:
            seen.add(repo)
            out.append(repo)
    return out


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true", help="verify stats exist, do not fetch")
    args = ap.parse_args()

    data = json.loads(SKILLS.read_text(encoding="utf-8"))
    repos = all_repos(data)

    if args.check:
        if not STATS.exists():
            print("stats.json missing — run scripts/fetch_stats.py", file=sys.stderr)
            return 1
        stats = json.loads(STATS.read_text(encoding="utf-8"))
        missing = [r for r in repos if r not in stats.get("repos", {})]
        if missing:
            print(f"stats missing for: {', '.join(missing)}", file=sys.stderr)
            return 1
        print(f"ok — {len(repos)} repos, refreshed {stats.get('refreshed_at')}")
        return 0

    print(f"Fetching stats for {len(repos)} repos...")
    out: dict[str, dict] = {}
    failed: list[str] = []
    for repo in repos:
        result = fetch(repo)
        if result is None:
            failed.append(repo)
            continue
        out[repo] = result
        print(f"  {result['stars']:>7,}  {repo}")

    # Preserve prior values for repos that failed this run, so a transient
    # outage degrades to stale data rather than blank data.
    if STATS.exists():
        prior = json.loads(STATS.read_text(encoding="utf-8")).get("repos", {})
        for repo in failed:
            if repo in prior:
                stale = dict(prior[repo])
                stale["stale"] = True
                out[repo] = stale
                print(f"  (kept stale value for {repo})")

    STATS.write_text(
        json.dumps(
            {
                "refreshed_at": datetime.now(timezone.utc).strftime("%Y-%m-%d"),
                "failed": failed,
                "repos": dict(sorted(out.items(), key=lambda kv: -kv[1]["stars"])),
            },
            indent=2,
            ensure_ascii=False,
        )
        + "\n",
        encoding="utf-8",
    )
    print(f"\nWrote {STATS.relative_to(ROOT)} — {len(out)} repos, {len(failed)} failed")
    return 1 if failed and not out else 0


if __name__ == "__main__":
    raise SystemExit(main())
