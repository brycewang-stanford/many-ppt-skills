#!/usr/bin/env python3
"""Harvest sample imagery for every skill in the registry.

The tables answer "what is this" and "what does it claim". They cannot answer
the question that actually decides a slide skill, which is *what does the output
look like*. Prose is a bad medium for that. This collects the pictures.

Two sources, and the distinction is the whole point of the ranking:

  * **showcase** — an image the project embeds in its own README or SKILL.md.
    Somebody chose this frame to represent the project. It is marketing, and it
    is also the single most informative image available.
  * **repo** — an image file sitting in the repository that no document points
    at. Often a whole template gallery. Less curated, sometimes more honest.

Both are the projects' own screenshots, not decks this registry generated.
That is stated in the README next to every gallery; see the note in render.py.

Every URL is pinned to the commit SHA that was cloned, so an upstream file move
cannot silently turn the gallery into broken images — the same reason the star
counts live in a generated file rather than in prose.

Usage:
    python scripts/fetch_samples.py                 # all skills
    python scripts/fetch_samples.py --only ppt-master frontend-slides
    python scripts/fetch_samples.py --verify        # re-check every pinned blob exists
"""

from __future__ import annotations

import argparse
import json
import re
import struct
import subprocess
import sys
import urllib.parse
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CACHE = ROOT / "benchmark" / ".cache" / "skills"
SKILLS = ROOT / "data" / "skills.json"
OUT = ROOT / "data" / "samples.json"

RAW = "https://raw.githubusercontent.com/{repo}/{sha}/{path}"

# Docs whose embedded images count as the project's own showcase.
DOC_NAMES = ("README.md", "README.zh-CN.md", "README_CN.md", "README.en.md",
             "README_EN.md", "SKILL.md", "AGENTS.md", "CLAUDE.md")

# SVG is deliberately absent. raw.githubusercontent serves it as text/plain,
# so GitHub's image proxy refuses to render it and the gallery would show a
# broken frame — worse than showing nothing.
IMAGE_EXT = {".png", ".jpg", ".jpeg", ".gif", ".webp"}

# Directories that never hold a sample of the output. The second row is raw
# design material: one project ships a folder of 1920x1080 background plates,
# which pass every size check and render in a gallery as blank beige rectangles.
# They are ingredients, not output.
SKIP_DIRS = {".git", "node_modules", "dist", "build", ".next", "venv",
             ".venv", "__pycache__", "vendor", "fonts", "font",
             "backgrounds", "background", "textures", "texture", "patterns",
             "wallpapers", "icons", "logos", "brand", "swatches", "colors"}

# Hosts that serve chrome, not screenshots.
SKIP_HOSTS = ("shields.io", "badge.fury.io", "badgen.net", "codecov.io",
              "travis-ci", "circleci.com", "app.netlify.com", "vercel.com",
              "api.star-history.com", "star-history.com", "visitor-badge",
              "hits.seeyoufarm.com", "forthebadge.com", "img.buymeacoffee.com")

# Filename fragments that mark an asset as identity or solicitation rather than
# output. Matched against the whole path, so `assets/logo/hero.png` is caught.
# `wordmark` and `brand-asset` are here because a project that ships a brand kit
# names those files after the mark, not after "logo" — starry-slides' four
# `…-brand-assets/…-mark-*.png` sailed past every fragment above and would have
# shown up in the gallery as if they were slides. A bare "mark" is not safe to
# add: it is inside "markdown" and "watermark".
SKIP_NAME = ("logo", "icon", "favicon", "badge", "avatar", "banner",
             "wordmark", "brand-asset", "brand_asset",
             "qrcode", "qr-code", "qr_code", "wechat", "weixin", "donate",
             "sponsor", "coffee", "star-history", "contributors", "profile",
             "watermark", "placeholder", "二维码", "赞赏", "打赏", "公众号",
             "background", "texture", "gradient", "wallpaper", "swatch",
             "palette", "底纹", "背景图", "alipay", "paypal", "payment",
             # Diagrams about how the skill works. Real documentation, but this
             # gallery answers "what does the output look like", and an
             # architecture chart answers a different question.
             "architecture", "pipeline", "flowchart", "架构", "流程图", "示意图")

# Same job, but where a bare substring would do damage. "qr" inside "square" and
# "sq" inside anything are the reason these need word boundaries; `image_7.png`
# is the naming convention tools use when they rip assets out of a source
# document, and those are ingredients of a deck rather than pictures of one.
SKIP_PATTERNS = (
    re.compile(r"(?<![a-z])qr(?![a-z])"),
    # `bg_cover.jpeg`, `cover-bg.png`: another spelling of a background plate.
    re.compile(r"(?<![a-z])bg(?![a-z])"),
    re.compile(r"(?:^|/)(?:image|img|figure|fig|pic)[-_]?\d+\.[a-z]+$"),
)

# Folders holding what goes *into* a deck rather than a picture *of* one. The
# projects that ship worked examples put the deck's own illustrations here —
# stock photography, AI-generated spots, per-page art — and they sail through
# every size and aspect check because they are full-bleed 16:9 by design. One
# project's entire sample set was stock photos of people at laptops.
#
# Applied only to repo-scanned files. An image the author embedded in their own
# README is a deliberate choice and is trusted wherever it lives.
INGREDIENT_DIRS = {"images", "img", "photos", "pics", "pictures", "media"}

# ...unless the file names itself as a picture of a deck, which is the escape
# hatch for a project that files its screenshots under `docs/images/`.
#
# "cover" is deliberately absent. It is ambiguous in exactly the wrong way —
# `p01_cover.png` and `book-cover1.png` are cover *artwork* drawn for a slide,
# not a picture of a cover slide, and admitting them puts `book-cover1` in the
# list of styles an agent is told it can ask for.
#
# Bounded, because "lifestyle" contains "style" — an unbounded match let a
# folder of stock photography back in under exactly that spelling. The trailing
# `s?` keeps `themes.png` and `slides.png` working.
PREVIEW_HINT = re.compile(
    r"(?<![a-z])(?:screenshots?|previews?|slides?|decks?|themes?|styles?|"
    r"layouts?|showcases?)(?![a-z])|截图|预览"
)

# Fragments that mark an asset as very likely to *be* the output. Used only to
# rank, never to exclude — a project that names its screenshots `1.png` should
# not be punished for it.
GOOD_NAME = ("screenshot", "preview", "demo", "example", "sample", "slide",
             "deck", "case", "showcase", "gallery", "result", "output",
             "cover", "theme", "template", "layout", "style", "effect",
             "示例", "效果", "预览", "案例", "截图", "封面", "模板", "样例")

MIN_WIDTH = 480      # narrower than this is an icon or a diagram fragment
MIN_PIXELS = 200_000 # guards against wide-but-short header strips
MAX_PER_SKILL = 24   # a gallery, not a file listing


# --------------------------------------------------------------------------
# Naming what is in the picture
# --------------------------------------------------------------------------
#
# A gallery of unlabelled screenshots is a mood board. To be reproducible, each
# image has to say which style produced it — and the projects already know: they
# name the file `soft-editorial-4.png` or caption it "Bauhaus Geometry". Both are
# read here rather than invented, and the source path travels with every caption
# so a wrong label is visibly wrong.

# Words that describe the file's role, not the design in it.
LABEL_NOISE = re.compile(
    r"^(?:style[-_ ]?preview|preview|screenshot|shot|demo|sample|hero|slide|"
    r"page|img|image|case|example)[-_ ]+", re.IGNORECASE)

# `soft-editorial-4` -> style `soft-editorial`, slide 4.
TRAILING_INDEX = re.compile(r"[-_ ]+(\d{1,3})$")

# Folder names that describe filing, not design — useless as a style label.
GENERIC_DIRS = {"images", "image", "img", "assets", "asset", "screenshots",
                "screenshot", "docs", "doc", "examples", "example", "static",
                "public", "media", "preview", "previews", "demos", "demo",
                "readme", "resources", "res", "pics", "photos", "content"}

# Roles that a filename gives a frame within one style, worth keeping in the
# caption but never part of the style token itself.
ROLE_SUFFIX = re.compile(
    r"[-_ ]+(cover|title|toc|closing|end|thanks|opening|index|contents)$",
    re.IGNORECASE)


def prettify(token: str) -> str:
    """`arc-electric-lifestyle` -> `Arc Electric Lifestyle`, CJK left alone."""
    parts = [p for p in re.split(r"[-_\s]+", token) if p]
    out = []
    for p in parts:
        out.append(p[:1].upper() + p[1:] if p.isascii() and p.islower() else p)
    return " ".join(out)


def derive_naming(alt: str, path: str | None) -> tuple[str, str | None, str | None]:
    """(label, style token, frame role) for one image.

    The style token is always taken from the filename when there is one: it is
    the string the project itself uses, so it is the string worth repeating back
    to an agent. The label prefers the author's own caption, which reads better
    than any filename.
    """
    style = role = None
    index = None

    if path:
        stem = Path(path).stem
        stem = LABEL_NOISE.sub("", stem) or Path(path).stem
        m = TRAILING_INDEX.search(stem)
        if m:
            index, stem = m.group(1), TRAILING_INDEX.sub("", stem)
        m = ROLE_SUFFIX.search(stem)
        if m:
            role, stem = m.group(1).lower(), ROLE_SUFFIX.sub("", stem)
        style = re.sub(r"[_\s]+", "-", stem.strip("-_ ").lower()) or None

    alt = " ".join((alt or "").split())

    # `style-preview-a.png` reduces to "a" and `style-preview-zh-a.png` to
    # "zh-a": filing codes, not names. Where the author captioned the image, the
    # caption is the real name — that project's "a" is "Swiss International",
    # and only the caption knows it. Where they did not, this drops the token
    # rather than print a code as though it were a style you could ask for. The
    # image keeps its linked path, so the reader can still go and look.
    if style and (len(style) < 3 or len(style.rsplit("-", 1)[-1]) == 1):
        slug = re.sub(r"[^a-z0-9]+", "-", alt.lower()).strip("-")
        style = slug or None

    # `ppt-workflow/01-cover.png`: the number names nothing, the folder does.
    if not style and path:
        parent = Path(path).parent.name.lower()
        if parent and parent not in GENERIC_DIRS and not parent.isdigit():
            style = re.sub(r"[_\s]+", "-", parent)

    if len(alt) >= 2:
        label = alt[:110]
    elif style:
        label = prettify(style)
        if index:
            label = f"{label} · {index}"
    elif role:
        label = prettify(role)
    else:
        label = ""

    return label, style, role


# --------------------------------------------------------------------------
# Image dimensions, without Pillow
# --------------------------------------------------------------------------

def image_size(head: bytes) -> tuple[int, int] | None:
    """Width and height from a file header. None if it cannot be read.

    Pure stdlib on purpose: this script runs in CI next to fetch_stats.py,
    which has no dependencies either, and adding Pillow to read four integers
    would be the largest dependency in the repository.
    """
    if head[:8] == b"\x89PNG\r\n\x1a\n" and head[12:16] == b"IHDR":
        return struct.unpack(">II", head[16:24])

    if head[:6] in (b"GIF87a", b"GIF89a"):
        w, h = struct.unpack("<HH", head[6:10])
        return w, h

    if head[:4] == b"RIFF" and head[8:12] == b"WEBP":
        fmt = head[12:16]
        if fmt == b"VP8X":
            w = int.from_bytes(head[24:27], "little") + 1
            h = int.from_bytes(head[27:30], "little") + 1
            return w, h
        if fmt == b"VP8 ":
            return struct.unpack("<HH", head[26:30])
        if fmt == b"VP8L":
            b = int.from_bytes(head[21:25], "little")
            return (b & 0x3FFF) + 1, ((b >> 14) & 0x3FFF) + 1
        return None

    if head[:2] == b"\xff\xd8":
        # Walk the JPEG segment chain to the first frame header.
        i = 2
        while i + 9 < len(head):
            if head[i] != 0xFF:
                i += 1
                continue
            marker = head[i + 1]
            if marker in (0xD8, 0x01) or 0xD0 <= marker <= 0xD7:
                i += 2
                continue
            length = int.from_bytes(head[i + 2:i + 4], "big")
            if 0xC0 <= marker <= 0xCF and marker not in (0xC4, 0xC8, 0xCC):
                h, w = struct.unpack(">HH", head[i + 5:i + 9])
                return w, h
            i += 2 + length
    return None


def local_size(path: Path) -> tuple[int, int] | None:
    try:
        with path.open("rb") as fh:
            return image_size(fh.read(65_536))
    except OSError:
        return None


# Deliberately no remote fetch. Every image is measured from a local clone, so
# a recorded sample is one whose bytes were read at a known commit — the URL is
# then derived from that commit rather than trusted. It also means the harvest
# needs nothing but git, and cannot be fooled by a URL that 200s with a
# placeholder.


# --------------------------------------------------------------------------
# Repo access
# --------------------------------------------------------------------------

def _clone(repo: str, dest: Path) -> Path | None:
    if dest.is_dir():
        return dest
    dest.parent.mkdir(parents=True, exist_ok=True)
    print(f"  cloning {repo} ...", flush=True)
    proc = subprocess.run(
        ["git", "clone", "--depth", "1", "-q",
         f"https://github.com/{repo}", str(dest)],
        capture_output=True, text=True, timeout=600,
    )
    if proc.returncode != 0:
        print(f"  !! {repo}: clone failed — {proc.stderr.strip()[:120]}",
              file=sys.stderr)
        return None
    return dest


def ensure_clone(repo: str, sid: str) -> Path | None:
    return _clone(repo, CACHE / sid)


# Several projects host their screenshots in a sibling repository — frontend-slides
# shows off beautiful-html-templates, which is itself in this registry. Following
# that reference is the difference between a rich gallery and an empty one.
#
# It is followed ONLY into repos the registry already tracks. Following arbitrary
# links is how a harvest turns into a download of the whole internet: one project
# here serves its screenshots out of a general-purpose asset repo that is 5 GB of
# unrelated media, and cloning it filled the disk before anything was harvested.
# Bounded to the 26 repos this registry reads anyway, the cost is known.

# Images dragged straight into a README get rehosted on GitHub's attachment CDN
# under an opaque UUID: no repository, no path, no file extension, and nothing to
# clone. They cannot be measured the way everything else here is — but they are
# permanent, GitHub-served, and by construction they are exactly the frames the
# author chose to open their README with. One Tier S project publishes all twelve
# of its screenshots this way and would otherwise show a single image.
#
# They are kept, and flagged `measured: false` so the distinction survives into
# the data rather than being quietly averaged away.
GH_ATTACHMENT = re.compile(
    r"^https?://github\.com/user-attachments/assets/[0-9a-f-]{16,}$"
)

GH_RAW = re.compile(
    r"^https?://raw\.githubusercontent\.com/(?P<repo>[^/]+/[^/]+)/"
    r"(?:refs/heads/)?[^/]+/(?P<path>.+)$"
)
GH_BLOB = re.compile(
    r"^https?://github\.com/(?P<repo>[^/]+/[^/]+)/(?:raw|blob)/"
    r"(?:refs/heads/)?[^/]+/(?P<path>.+)$"
)


def parse_github_image(url: str) -> tuple[str, str] | None:
    """Split a GitHub file URL into (repo, path). Any ref is discarded — the
    image is re-pinned to whatever commit we actually clone and read."""
    for pattern in (GH_RAW, GH_BLOB):
        m = pattern.match(url.split("?")[0].split("#")[0])
        if m:
            return m.group("repo"), urllib.parse.unquote(m.group("path"))
    return None


def sibling_clone(repo: str, registry_ids: dict[str, str]) -> Path | None:
    """A clone of another *registry* repo, cloning it if this is the first ask.

    Returns None for anything outside the registry, which is the guard rail —
    see the note above.
    """
    sid = registry_ids.get(repo)
    if not sid:
        return None
    return _clone(repo, CACHE / sid)


def head_sha(repo_dir: Path) -> str | None:
    proc = subprocess.run(["git", "-C", str(repo_dir), "rev-parse", "HEAD"],
                          capture_output=True, text=True)
    return proc.stdout.strip() or None


# --------------------------------------------------------------------------
# Finding images
# --------------------------------------------------------------------------

MD_IMAGE = re.compile(r"!\[(?P<alt>[^\]]*)\]\((?P<url>[^)\s]+)(?:\s+\"[^\"]*\")?\)")
HTML_IMAGE = re.compile(r"<img\b[^>]*?\bsrc=[\"'](?P<url>[^\"']+)[\"'][^>]*>",
                        re.IGNORECASE)
HTML_ALT = re.compile(r"\balt=[\"'](?P<alt>[^\"']*)[\"']", re.IGNORECASE)


def is_skippable(path_or_url: str) -> bool:
    low = path_or_url.lower()
    if any(host in low for host in SKIP_HOSTS):
        return True
    if any(frag in low for frag in SKIP_NAME):
        return True
    return any(p.search(low) for p in SKIP_PATTERNS)


def doc_images(skill_dir: Path, repo_dir: Path) -> list[dict]:
    """Images a project embeds in its own documentation, in document order."""
    found: list[dict] = []
    for name in DOC_NAMES:
        doc = skill_dir / name
        if not doc.is_file():
            continue
        try:
            text = doc.read_text(errors="replace")
        except OSError:
            continue
        rel_doc = doc.relative_to(repo_dir).as_posix()

        hits: list[tuple[int, str, str]] = []
        for m in MD_IMAGE.finditer(text):
            hits.append((m.start(), m.group("url").strip(), m.group("alt").strip()))
        for m in HTML_IMAGE.finditer(text):
            alt = HTML_ALT.search(m.group(0))
            hits.append((m.start(), m.group("url").strip(),
                         alt.group("alt").strip() if alt else ""))

        for pos, url, alt in sorted(hits):
            if url.startswith("data:") or is_skippable(url) or is_skippable(alt):
                continue
            found.append({
                "raw": url,
                "alt": alt,
                "doc": rel_doc,
                "order": pos,
                "source": "showcase",
            })
    return found


def repo_images(repo_dir: Path) -> list[dict]:
    """Image files present in the repo that no document points at."""
    out: list[dict] = []
    for path in sorted(repo_dir.rglob("*")):
        if not path.is_file() or path.suffix.lower() not in IMAGE_EXT:
            continue
        rel = path.relative_to(repo_dir)
        if any(part in SKIP_DIRS for part in rel.parts):
            continue
        if is_skippable(rel.as_posix()):
            continue
        if any(part.lower() in INGREDIENT_DIRS for part in rel.parts[:-1]) and \
                not PREVIEW_HINT.search(rel.name.lower()):
            continue
        out.append({
            "raw": rel.as_posix(),
            "alt": "",
            "doc": None,
            "order": 0,
            "source": "repo",
        })
    return out


def resolve(entry: dict, repo: str, sha: str, repo_dir: Path, doc_dir: str,
            registry_ids: dict[str, str], skipped: dict[str, int]) -> dict | None:
    """Turn a reference into a pinned URL, measured from bytes on disk.

    Three shapes arrive here: a path relative to a document, a GitHub URL into
    another repository, and everything else. Only the first two can be read and
    measured, so only those are kept — an unmeasurable image is one that could
    be a 40px icon or a dead link, and either would show up in the gallery as a
    defect.
    """
    raw, host_repo, host_dir = entry["raw"], repo, repo_dir

    if raw.startswith(("http://", "https://")):
        if GH_ATTACHMENT.match(raw.split("?")[0]):
            if entry["source"] != "showcase":
                return None
            label, _, _ = derive_naming(entry["alt"], None)
            return {
                "url": raw,
                "repo": None,
                "path": None,
                "label": label,
                "style": None,
                "role": None,
                "alt": entry["alt"][:200],
                "from_doc": entry["doc"],
                "source": "showcase",
                "measured": False,
                "width": None,
                "height": None,
            }
        parsed = parse_github_image(raw)
        if not parsed:
            skipped["offsite"] += 1
            return None
        host_repo, rel_path = parsed
        host_dir = sibling_clone(host_repo, registry_ids)
        if host_dir is None:
            skipped["offsite"] += 1
            return None
        host_sha = head_sha(host_dir)
        if not host_sha:
            return None
        candidate = host_dir / rel_path
    else:
        host_sha = sha
        rel_path = raw.split("?")[0].split("#")[0].lstrip("./")
        rel_path = urllib.parse.unquote(rel_path)
        if raw.startswith("/"):
            candidate = repo_dir / rel_path.lstrip("/")
        else:
            candidate = (repo_dir / doc_dir / rel_path) if doc_dir else repo_dir / rel_path

    try:
        candidate = candidate.resolve()
        candidate.relative_to(host_dir.resolve())
    except (ValueError, OSError):
        return None
    if not candidate.is_file() or candidate.suffix.lower() not in IMAGE_EXT:
        skipped["missing"] += 1
        return None

    rel = candidate.relative_to(host_dir.resolve()).as_posix()
    size = local_size(candidate)
    if not size:
        return None
    w, h = size
    if w < MIN_WIDTH or w * h < MIN_PIXELS:
        skipped["too_small"] += 1
        return None

    label, style, role = derive_naming(entry["alt"], rel)
    return {
        "url": RAW.format(repo=host_repo, sha=host_sha,
                          path=urllib.parse.quote(rel)),
        "repo": host_repo,
        "sha": host_sha,
        "path": rel,
        "label": label,
        "style": style,
        "role": role,
        "alt": entry["alt"][:200],
        "from_doc": entry["doc"],
        "source": entry["source"],
        "measured": True,
        "width": w,
        "height": h,
    }


def score(item: dict) -> tuple:
    """Ranking. A README screenshot outranks a stray asset; a landscape frame
    outranks a portrait one because a deck is 16:9 and the tall images in these
    repos are nearly always full-page marketing shots."""
    showcase = item["source"] == "showcase"
    named = any(g in (item["path"] or item["url"]).lower() or g in item["alt"].lower()
                for g in GOOD_NAME)
    w, h = item.get("width"), item.get("height")
    if not (w and h):
        # Unmeasurable attachment. Sorted as a plausible 16:9 screenshot rather
        # than last, because being in a README is itself strong evidence.
        return (showcase, named, True, 1920 * 1080)
    return (showcase, named, 1.2 <= w / max(h, 1) <= 2.2, w * h)


def collect(skill: dict, registry_ids: dict[str, str]) -> dict:
    sid, repo = skill["id"], skill["repo"]
    repo_dir = ensure_clone(repo, sid)
    if repo_dir is None:
        return {"error": "clone failed", "samples": []}
    sha = head_sha(repo_dir)
    if not sha:
        return {"error": "no HEAD", "samples": []}

    sub = skill.get("path") or ""
    skill_dir = repo_dir / sub if sub and (repo_dir / sub).is_dir() else repo_dir

    refs = doc_images(skill_dir, repo_dir) + repo_images(repo_dir)
    skipped = {"offsite": 0, "missing": 0, "too_small": 0}

    resolved: list[dict] = []
    seen: set[str] = set()
    for ref in refs:
        doc_dir = str(Path(ref["doc"]).parent) if ref["doc"] else ""
        doc_dir = "" if doc_dir == "." else doc_dir
        item = resolve(ref, repo, sha, repo_dir, doc_dir, registry_ids, skipped)
        if not item:
            continue
        key = f"{item['repo']}:{item['path']}" if item["path"] else item["url"]
        if key in seen:
            continue
        seen.add(key)
        resolved.append(item)

    resolved.sort(key=score, reverse=True)
    return {
        "repo": repo,
        "sha": sha,
        "found": len(resolved),
        # Kept so the README's "n of m" is honest about what was left out
        # rather than quietly presenting a filtered set as the whole picture.
        "skipped": {k: v for k, v in skipped.items() if v},
        "samples": resolved[:MAX_PER_SKILL],
    }


# --------------------------------------------------------------------------
# Verification
# --------------------------------------------------------------------------

def blob_exists(clone: Path, sha: str, path: str) -> bool:
    """Whether `path` is a real blob in commit `sha` of this clone."""
    proc = subprocess.run(
        ["git", "-C", str(clone), "cat-file", "-e", f"{sha}:{path}"],
        capture_output=True,
    )
    return proc.returncode == 0


def find_clone(repo: str, registry_ids: dict[str, str]) -> Path | None:
    sid = registry_ids.get(repo)
    return CACHE / sid if sid and (CACHE / sid).is_dir() else None


def verify(card: dict, registry_ids: dict[str, str]) -> int:
    """Confirm every recorded URL names a blob that really exists at that commit.

    Checked against the clones rather than over the network, so it is exact and
    works offline. A URL built from a commit that contains the blob is a URL
    raw.githubusercontent will serve — GitHub keeps content addressed by SHA
    reachable even after the branch moves on.
    """
    checked = missing = unmeasured = 0
    unresolved: list[str] = []
    for sid, entry in card["skills"].items():
        for s in entry.get("samples", []):
            if not s.get("path"):
                # A GitHub attachment: no repo, no blob, nothing local to check.
                unmeasured += 1
                continue
            clone = find_clone(s["repo"], registry_ids)
            if clone is None:
                unresolved.append(f"{sid}: no clone for {s['repo']}")
                continue
            sha = s["sha"]
            checked += 1
            if not blob_exists(clone, sha, s["path"]):
                missing += 1
                print(f"  !! {sid}: {s['repo']}@{sha[:8]}:{s['path']}",
                      file=sys.stderr)

    for line in unresolved:
        print(f"  ?? {line} — re-run the harvest to check it", file=sys.stderr)
    print(f"{checked - missing}/{checked} samples confirmed present at their "
          f"pinned commit"
          + (f", {unmeasured} GitHub attachments not checkable offline" if unmeasured else "")
          + (f", {len(unresolved)} unchecked" if unresolved else ""))
    return 1 if missing else 0


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--only", nargs="*", help="limit to these skill ids")
    ap.add_argument("--verify", action="store_true",
                    help="re-check every recorded blob still exists at its pinned commit")
    args = ap.parse_args()

    registry = json.loads(SKILLS.read_text(encoding="utf-8"))
    registry_ids = {s["repo"]: s["id"] for s in registry["skills"]}

    if args.verify:
        if not OUT.exists():
            print("samples.json missing — run without --verify first", file=sys.stderr)
            return 1
        return verify(json.loads(OUT.read_text(encoding="utf-8")), registry_ids)

    targets = registry["skills"]
    if args.only:
        wanted = set(args.only)
        targets = [s for s in targets if s["id"] in wanted]

    prior = (json.loads(OUT.read_text(encoding="utf-8")).get("skills", {})
             if OUT.exists() else {})

    out: dict[str, dict] = dict(prior)
    for i, skill in enumerate(targets, 1):
        print(f"[{i}/{len(targets)}] {skill['id']}", flush=True)
        entry = collect(skill, registry_ids)
        out[skill["id"]] = entry
        n, found = len(entry["samples"]), entry.get("found", 0)
        note = f" (of {found} found)" if found > n else ""
        print(f"    {n} sample(s){note}"
              + (f" — {entry['error']}" if entry.get("error") else ""))

    OUT.write_text(
        json.dumps(
            {
                "$comment": (
                    "Sample imagery for each registry skill. Every image is the "
                    "project's OWN screenshot, taken from its repository — none "
                    "were produced by running the skill, so they are marketing, "
                    "not measurement. URLs are pinned to the commit SHA that was "
                    "read. Generated by scripts/fetch_samples.py; do not hand-edit."
                ),
                "refreshed_at": datetime.now(timezone.utc).strftime("%Y-%m-%d"),
                "skills": out,
            },
            indent=2, ensure_ascii=False,
        ) + "\n",
        encoding="utf-8",
    )
    total = sum(len(e.get("samples", [])) for e in out.values())
    withany = sum(1 for e in out.values() if e.get("samples"))
    print(f"\nWrote {OUT.relative_to(ROOT)} — {total} samples across "
          f"{withany}/{len(out)} skills")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
