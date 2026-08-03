# Add 10-20 new PPT/slide skills to the registry — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add 10-20 strictly-curated new slide / presentation / deck skills to `data/skills.json`, attach an upstream preview image to each in `data/samples.json`, regenerate the READMEs, and push to `main`.

**Architecture:** Hand-edited changes to two data files (`data/skills.json` and `data/samples.json`); pipeline scripts regenerate READMEs and validate. The agent acts as a curator: it searches the web, verifies each candidate against a strict acceptance bar, and only then writes entries. No local install of any new skill.

**Tech Stack:** Python 3, JSON, the existing repo scripts under `scripts/` (`validate_registry.py`, `render.py`, `sync_plugin.py`, `check_links.py`), `WebSearch` and `WebFetch` for discovery.

## Global Constraints

- Acceptance bar (strict): public GitHub repo; ships a `SKILL.md` / `AGENTS.md` / equivalent; core purpose is slides / decks; not already in `data/skills.json`; license known; README contains at least one preview image. From the spec.
- Valid `route` values are exactly the eight in `scripts/validate_registry.py`: `html`, `pptx`, `hybrid`, `image`, `suite`, `framework`, `templates`, `list`. From the spec.
- Route emphasis: `templates` (currently 3) and `framework` (currently 6) first. Up to 10 extras to whichever under-represented route has the strongest candidates. From the spec.
- Required fields per new entry: `id`, `repo`, `name`, `route`, `tagline_en` (≥15, <100, no "powerful"/"seamlessly"), `tagline_zh` (≥6, translation of `tagline_en`), `lang` ∈ {`en`,`zh`,`bilingual`}, `license_note`, `source: "discovered"`. From the spec.
- Hand-grade 2-3 entries with the strongest `SKILL.md` by also adding `install` (`method` ∈ `clone` / `plugin` / `skills-cli` / `python` / `npx`), `requires`, `highlights_en`, `highlights_zh`, `best_for_en`, `best_for_zh`. From the spec.
- AGPL rows MUST include `license_warning`. From the spec and existing convention.
- Samples are produced by `scripts/fetch_samples.py --only <ids>` after `data/skills.json` is updated. We do not hand-edit `data/samples.json`. The script populates per-sample `style` and `label` itself; we do not pick them. From the spec.
- Total new entries: 10-20. Stop at 20 or one week, whichever comes first. If fewer than 10 candidates pass, ship whatever does. From the spec.
- Do not modify `scripts/`, `principles/`, `.claude-plugin/`, CI workflows, schema file, `data/samples.json`, or any other generated output. From the spec.
- Do not install or run any new skill. From the spec.
- Commit on `main`, message `chore: add 10-20 new slide skills with samples to registry`, then `git push origin main`. From the spec and user pre-authorization.

---

## Task 1: Pre-flight inventory of repo state

**Files:**
- Read: `data/skills.json` (first 200 lines to see structure, not the whole file)
- Read: `data/samples.json` (whole file, small, just to confirm shape)
- Read: `scripts/validate_registry.py`
- Read: `scripts/render.py` (top of file + the section that consumes `data/samples.json`)
- Read: `scripts/fetch_samples.py` (top of file + the section that classifies images)

**Goal:** Lock in the existing repo set and confirm `scripts/fetch_samples.py` is the writer for `data/samples.json`. (The brief originally assumed a flat sample schema; Task 1 already surfaced that `data/samples.json` is script-generated. Confirmed and resolved: this plan treats `fetch_samples.py` as the writer.)

- [ ] **Step 1.1: Read `data/samples.json` shape**

  ```bash
  wc -l data/samples.json
  python -c "import json; d=json.load(open('data/samples.json')); print('top-level keys:', list(d.keys())); rec = d['skills'][next(iter(d['skills']))]; print('per-skill keys:', list(rec.keys())); print('first sample keys:', list(rec['samples'][0].keys()) if rec.get('samples') else 'no samples')"
  ```

  Expected: top-level `skills` (not a flat object), per-skill wrapper, nested `samples[]` array.

- [ ] **Step 1.2: Confirm `fetch_samples.py` is the writer**

  ```bash
  head -30 scripts/fetch_samples.py
  ```

  Expected: module docstring ends with usage and notes "every URL is pinned to the commit SHA that was cloned". The `--only` flag is exposed for targeted runs.

- [ ] **Step 1.3: Existing `repo` set**

  ```bash
  python -c "import json; d=json.load(open('data/skills.json')); print('count:', len(d['skills'])); print('repos:', sorted({s['repo'] for s in d['skills']}))" > /tmp/existing_repos.txt
  wc -l /tmp/existing_repos.txt
  ```

  Expected: count 203, plus 2 list entries (not used here). The 200+ repo strings are the dedup set for the next task.

- [ ] **Step 1.4: Pre-flight `gh` and shallow-clone availability**

  `scripts/fetch_samples.py` clones repos. Confirm `gh` and `git` are on PATH and we have network access to `github.com`:

  ```bash
  command -v gh
  command -v git
  gh auth status 2>&1 | head -5
  ```

  If `gh` is missing, park the sample-driven flow and surface that to the user; we will not hand-pad samples. (Entries still land in `data/skills.json` so the README table includes them, just without preview thumbnails.)

- [ ] **Step 1.5: No commit**

  Pre-flight reads only. Do not commit.

---

## Task 2: Discovery batch 1 — find 3-5 strict candidates

**Files:** none changed yet. Search results recorded in chat only.

**Goal:** Produce a working list of 3-5 candidates that pass the strict bar. Do not write any JSON until Task 3.

- [ ] **Step 2.1: WebSearch round 1**

  Use `WebSearch` with the keyword set from the spec:

  - `SKILL.md slide deck`
  - `AGENTS.md presentation`
  - `claude skill pptx`
  - `claude skill template presentation`
  - `slide generator skill`
  - Chinese: `幻灯片 skill`, `演示文稿 模板 Claude`

  Collect 10-20 candidate `owner/name` strings. Skip results that are clearly not GitHub repos.

- [ ] **Step 2.2: WebSearch round 2 — aggregators**

  ```text
  awesome claude skills slide
  awesome ai agents skills presentation
  ```

  Fetch one or both of these and extract any slide / presentation skill entries.

- [ ] **Step 2.3: Dedup against existing set**

  Compare each candidate `owner/name` against `/tmp/existing_repos.txt` (Task 1.4). Drop matches. Keep the survivors as the working list.

- [ ] **Step 2.4: For each candidate, run the strict verification**

  For each surviving candidate:

  - `WebFetch` the repo root README.
  - Confirm it contains a SKILL.md / AGENTS.md / equivalent (look for the filename, the file's first 30 lines, or a `## Install` / `## Usage` section).
  - Confirm the core purpose is slide / deck / presentation (look for "slide", "deck", "presentation", "pptx", "ppt", "keynote", "beamer", "revealjs", "marp", "remark", "slides", "演示", "幻灯").
  - Confirm the README contains at least one preview image — collect the absolute `https://` URL.
  - Note the license (look for `LICENSE`, `LICENSE.md`, or a badge in the README).
  - Note the primary language(s) used in the README.

  Mark each candidate: `PASS` (with the values chosen for each field) or `REJECT` (with the reason).

- [ ] **Step 2.5: Pick 2-3 hand-grade candidates**

  Among the `PASS` set, choose 2-3 whose SKILL.md is the most concrete (install command + a runnable example). Mark them `HAND-GRADE`. The rest are `DISCOVERED`.

- [ ] **Step 2.6: No commit**

  Batch 1 is search-only.

---

## Task 3: Apply batch 1 to `data/skills.json` and populate samples via the script

**Files:**
- Modify: `data/skills.json` (add 3-5 entries to `skills` array)
- Regenerate: `data/samples.json` (via `scripts/fetch_samples.py`; do not hand-edit)

**Goal:** First batch landed in the registry; samples will be populated by the script. READMEs not regenerated yet (Task 4).

- [ ] **Step 3.1: Build the new skill entries**

  For each `PASS` candidate from Task 2.4, write the entry dict:

  ```json
  {
    "id": "<slug>",
    "repo": "<owner/name>",
    "name": "<display name>",
    "route": "<one of the eight valid routes>",
    "tagline_en": "<15-99 char tagline>",
    "tagline_zh": "<Chinese translation, ≥6 chars>",
    "lang": "<en|zh|bilingual>",
    "license_note": "<short license name>",
    "source": "discovered"
  }
  ```

  For `HAND-GRADE` candidates, also include:

  ```json
  "install": { "method": "<clone|plugin|skills-cli|python|npx>", "command": "<command string>" },
  "requires": ["<tool or runtime>"],
  "highlights_en": ["<3-6 short bullets>"],
  "highlights_zh": ["<Chinese versions of the same bullets>"],
  "best_for_en": "<single sentence>",
  "best_for_zh": "<Chinese version>"
  ```

  Optional but useful: `author`, `author_url`, `homepage` (only if visible on the repo).

- [ ] **Step 3.2: Slug uniqueness check**

  ```bash
  python -c "import json; d=json.load(open('data/skills.json')); print(sorted({s['id'] for s in d['skills']}))"
  ```

  Verify each new `id` is not already present. If collision, prefix with owner per the spec (`ingest_discovered.py` rule).

- [ ] **Step 3.3: Repo uniqueness check**

  ```bash
  python -c "import json; d=json.load(open('data/skills.json')); print(sorted({s['repo'] for s in d['skills']}))" | grep -F "<owner/name>"
  ```

  No output means the repo is not yet listed.

- [ ] **Step 3.4: Edit `data/skills.json`**

  Insert each new entry into the `skills` array. Use `Edit` with `old_string` being a unique chunk near the end of the array, or add a new top-level insertion if `Edit` proves fragile. The file is large; the safest pattern is to find the closing `]` of `skills` and insert before it. If the file is too long for a single `Edit`, do one entry per `Edit` and re-read between edits.

- [ ] **Step 3.5: Populate samples for the new entries via the script**

  ```bash
  python scripts/fetch_samples.py --only <id1> <id2> <id3> <id4> <id5>
  ```

  Expected: the script shallow-clones each repo, parses `README.md` / `SKILL.md` / `AGENTS.md` / `CLAUDE.md` for image references, and writes per-skill records into `data/samples.json`. If a single id fails to clone, the script exits non-zero for that id but continues with the others; capture per-id status from the log and decide whether to retry or drop. **Do not hand-edit `data/samples.json`.** If `gh` is missing or no candidate can be cloned, the batch moves on without samples and the user is told in Task 4's report.

- [ ] **Step 3.6: JSON validity check**

  ```bash
  python -c "import json; json.load(open('data/skills.json')); json.load(open('data/samples.json')); print('ok')"
  ```

  Expected: `ok`.

- [ ] **Step 3.7: `validate_registry.py` must pass**

  ```bash
  python scripts/validate_registry.py
  ```

  Expected: 0 errors. If it fails, read the message, fix the offending entry, re-run. Most common cause is `tagline_en` length or missing `license_warning` on an AGPL row.

- [ ] **Step 3.8: No commit yet**

  Wait for Task 4 to regenerate READMEs in the same commit.

---

## Task 4: Regenerate READMEs and run the full validation gate

**Files:**
- Regenerate: `README.md`, `README.en.md` (via `scripts/render.py`)
- No manual edits to the READMEs

**Goal:** The two READMEs reflect the new entries; the gallery shows previews for the entries whose samples were harvested. The full validation pipeline passes.

- [ ] **Step 4.1: Render the READMEs**

  ```bash
  python scripts/render.py
  ```

  Expected: writes `README.md` and `README.en.md`. If it errors, read the message; the most likely cause is a `data/samples.json` shape mismatch from a partial script run, which is fixed by re-running the script for the missing ids.

- [ ] **Step 4.2: Confirm the new entries appear in the rendered READMEs**

  ```bash
  for id in <id1> <id2> ...; do printf "%s: en=%d zh=%d\n" "$id" "$(grep -c "$id" README.md)" "$(grep -c "$id" README.en.md)"; done
  ```

  Expected: at least 1 in each file for every new id. Entries whose sample harvest failed will still appear in the table section but not in the gallery section — that is acceptable.

- [ ] **Step 4.3: Validation gate**

  ```bash
  python scripts/validate_registry.py
  python scripts/render.py --check
  python scripts/sync_plugin.py --check
  python scripts/check_links.py
  ```

  All four must pass with 0 errors. If any fail, fix and re-run.

- [ ] **Step 4.4: Git status review**

  ```bash
  git status --porcelain
  ```

  Expected: `data/skills.json`, `data/samples.json`, `README.md`, `README.en.md` are modified. No other files. If `data/samples.json` shows no diff, the script harvest failed; either retry or accept the batch without samples and tell the user.

- [ ] **Step 4.5: Commit**

  ```bash
  git add data/skills.json data/samples.json README.md README.en.md
  git commit -m "chore: add <N> new slide skills with samples to registry (batch 1)"
  ```

  `<N>` is the number of entries added in this batch.

- [ ] **Step 4.6: Push to main**

  ```bash
  git push origin main
  ```

  Expected: success. If it fails, stop and report the exact error to the user.

- [ ] **Step 4.7: Pause point**

  Stop here. Do not start Task 5 in the same session unless the user says so. The spec allows daily batches; this respects the "一天一个批次" rhythm.

---

## Task 5: Discovery batch 2 — find 3-5 more strict candidates

**Files:** none changed.

**Goal:** Keep the registry growing; do not yet push to 20 in one go.

- [ ] **Step 5.1: Re-read the existing repo set**

  The 203 → 203+`N1` set is now in `data/skills.json`. Re-export it:

  ```bash
  python -c "import json; d=json.load(open('data/skills.json')); print('\n'.join(sorted({s['repo'] for s in d['skills']})))" > /tmp/existing_repos.txt
  ```

- [ ] **Step 5.2: WebSearch round 3**

  Use the keyword set again, but rotate to less-used angles:

  - `beamer skill claude`
  - `revealjs skill`
  - `marp skill`
  - `keynote skill claude`
  - `pdf presentation skill agent`
  - Chinese: `PPT 模板 Claude 技能`, `幻灯片生成 智能体`

  Collect 10-20 fresh candidates.

- [ ] **Step 5.3: Verify each candidate**

  Repeat the verification protocol from Task 2.4. Reject anything already in `/tmp/existing_repos.txt`.

- [ ] **Step 5.4: Hand-grade selection**

  Pick 1 more `HAND-GRADE` candidate if the batch has a standout `SKILL.md`. Otherwise all `DISCOVERED`.

- [ ] **Step 5.5: No commit**

  This task is search-only.

---

## Task 6: Apply batch 2 to the registry

**Files:**
- Modify: `data/skills.json`
- Regenerate: `data/samples.json` (via `scripts/fetch_samples.py`; do not hand-edit)

**Goal:** Land the second batch in the same shape as batch 1.

- [ ] **Step 6.1-6.2: Build entries; slug + repo uniqueness**

  Same as Task 3.1-3.3.

- [ ] **Step 6.3: Edit `data/skills.json`; run `fetch_samples.py`**

  Same as Task 3.4-3.5. Insert each new entry into `data/skills.json`, then run `python scripts/fetch_samples.py --only <id1> <id2> ...` to populate samples. (Space-separated ids; comma form is a silent no-op.)

- [ ] **Step 6.4: JSON validity + `validate_registry.py`**

  Same as Task 3.6-3.7.

- [ ] **Step 6.5: No commit yet**

  Wait for Task 7 to regenerate READMEs in the same commit.

---

## Task 7: Render, validate, commit, push (batch 2)

**Files:**
- Regenerate: `README.md`, `README.en.md`

- [ ] **Step 7.1-7.4: Render, grep, full validation gate**

  Same as Task 4.1-4.4. Adjust the commit message: `chore: add <N2> new slide skills with samples to registry (batch 2)`.

- [ ] **Step 7.5: Commit and push**

  ```bash
  git add data/skills.json data/samples.json README.md README.en.md
  git commit -m "chore: add <N2> new slide skills with samples to registry (batch 2)"
  git push origin main
  ```

- [ ] **Step 7.6: Pause point**

  Same as Task 4.7.

---

## Task 8: Batches 3-5 as needed (loop until 20 or one week)

**Files:**
- Modify: `data/skills.json`
- Regenerate: `data/samples.json` (via `scripts/fetch_samples.py`)
- Regenerate: `README.md`, `README.en.md` (via `scripts/render.py`)

**Goal:** Fill out the registry up to 20 entries, or stop when the strict bar dries up, or stop at one week.

- [ ] **Step 8.1: Repeat Tasks 5-7 verbatim** with `batch 3`, `batch 4`, `batch 5`.

  Each iteration:
  1. Re-export existing `repo` set.
  2. Run a different slice of the keyword space (rotate to keep finding new candidates).
  3. Verify strictly.
  4. Apply to `data/skills.json` + `data/samples.json`.
  5. Render + validate + commit + push.

- [ ] **Step 8.2: Stop conditions**

  Stop when **any** of:
  - Total new entries reaches 20.
  - One week (counted from the start of Task 1) has elapsed.
  - Two consecutive search rounds return 0 strict candidates.

  When stopping, run `python scripts/validate_registry.py` once more to confirm a clean state, then report the final count and push status to the user.

- [ ] **Step 8.3: Final report to the user**

  Message: total entries added (target 10-20), batches (1-5), commits pushed, any `REJECT` reasons worth noting, and whether the 20 cap or the one-week cap was hit first.

---

## Self-review

- **Spec coverage:**
  - "Add 10-20 new entries" → Tasks 2-8.
  - "Strict bar" → Task 2.4 verification protocol is referenced from every batch.
  - "Sample in `data/samples.json`" → Task 3.5, 6.3, 8.1.
  - "Regenerate READMEs" → Tasks 4.1, 7.1, 8.1.
  - "Validate / render --check / sync_plugin --check / check_links" → Tasks 4.3, 7.1, 8.1.
  - "Commit on main, push" → Tasks 4.5-4.6, 7.5, 8.1.
  - "Do not modify scripts, principles, CI, plugin.json, schema" → Out-of-scope list, not touched in any task.
  - "Time budget one week" → Task 8.2 stop conditions.
- **Placeholder scan:** no TBD/TODO. The `style_id` vocabulary is read at execution time and intentionally not hard-coded.
- **Type consistency:** `id` / `repo` / `route` / `tagline_en` / `tagline_zh` / `lang` / `license_note` / `source` are spelled the same in every task. `style_id` / `commit` / `image_url` / `credit` are spelled the same in every sample-record block.
- **One ambiguity check:** the plan assumes the existing `data/samples.json` record uses `id`, `style_id`, `commit`, `image_url`, `credit` (Task 1.3 verifies; spec inline-adjusts if different). This is the only deferral and is bounded to a 30-second read.
