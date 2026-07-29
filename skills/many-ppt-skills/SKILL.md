---
name: many-ppt-skills
description: Pick an AI slide-deck skill and a concrete visual style from a curated registry, filtering on the requirements that decide it — editable in PowerPoint, speaker notes, a mandated corporate template, offline, PDF — with sample imagery and the style ids each project actually uses. Use when the user wants to make a presentation, deck or slides and has not already chosen a tool; asks which slide skill to use or what the difference between them is; wants to know what a style looks like before committing; or names a style id such as soft-editorial or swiss-grid. This skill routes to the skill that makes the deck — it does not make decks itself.
---

<!-- Generated from the SKILL.md at the repository root by
     scripts/sync_plugin.py. Edit that file, not this copy. -->

# many-ppt-skills

A registry of AI slide-deck skills, the imagery they publish, the style ids they
name that imagery with, and what their own documentation claims they can do.
Your job with it is to get someone from "I need a deck" to an installed skill and
a style id, quickly, without guessing.

Counts are not written down here — `pick.py` prints them live, and a number
copied into prose is a number that goes stale.

**This skill does not generate decks.** It chooses which one will, and hands
over.

## Query the registry — do not read the JSON

The data files total roughly 200KB. Reading them into context to answer one
question is the mistake this repository has a whole principle about
(`principles/05-progressive-disclosure.md`). Use the CLI.

**Run it by absolute path.** Your working directory is the user's project, not
this skill — a bare `scripts/pick.py` resolves against their repo and fails with
"can't open file". Build the path from this skill's own directory, which the
loader gives you when this file opens (Claude Code prints it as *Base directory
for this skill*; a plugin install exposes it as `${CLAUDE_PLUGIN_ROOT}`). Set it
once, and never `cd` into the skill directory — that would move the user's shell
out of their project. The script finds its own data files relative to itself, so
only the path to the script matters.

```bash
SKILL_DIR=~/.claude/skills/many-ppt-skills   # or ${CLAUDE_PLUGIN_ROOT}, or the base directory printed above
python "$SKILL_DIR/scripts/pick.py" route
```

A separate shell call does not remember `SKILL_DIR`, so keep the assignment and
the query in one command, or substitute the literal path.

The five steps are the whole method. Steps 0 and 1 are cheap and decide
everything after them, so do not skip ahead to `list`.

## Step 0 — check what the user already has

```bash
python "$SKILL_DIR/scripts/pick.py" installed
```

If a deck skill is already installed and covers what they are asking for, say so
and use it. Do not re-litigate the choice or install a second one alongside it.
This is a directory-name match, so treat a hit as a strong hint and a miss as
inconclusive rather than proof of nothing.

## Step 1 — ask the route question

There is one question that decides everything downstream, and it is not about
taste:

> **Will anyone need to open the deliverable in PowerPoint and edit it?**

- **Yes → native PPTX.** The recipient edits normally. The design ceiling is
  bounded by what OOXML can express.
- **No → HTML-native.** A single `.html` file, far higher design ceiling, plain
  text in git. The recipient cannot edit it in Office.

Ask it. Do not infer it from the topic of the deck — a board update and a
conference talk can land on either side, and getting this wrong makes every
recommendation after it wrong. The `route` subcommand prints this question along
with the current per-route counts.

## Step 2 — ask which requirements are real

```bash
python "$SKILL_DIR/scripts/pick.py" caps
```

This prints the requirements you can filter on, how many skills document each,
and one line on why each matters. Read it and ask the user about the two or
three that plausibly apply — speaker notes if someone else presents, a custom
template if their employer mandates one, offline if the venue has no wifi, PDF
if it gets emailed.

Ask before filtering, not after. Every `--cap` flag also discards skills whose
docs merely never mentioned that feature, so filtering on a requirement the user
does not have throws away good candidates for nothing.

## Step 3 — shortlist

```bash
python "$SKILL_DIR/scripts/pick.py" list --route pptx --ready --cap speaker_notes --cap custom_template
python "$SKILL_DIR/scripts/pick.py" list --route html --ready --lang en --limit 10
```

- `--route` — `html`, `pptx`, `hybrid`, `suite`, `image`, `framework`,
  `templates`. From step 1.
- `--ready` — **use this by default.** Most entries came from an automated
  discovery sweep: real repositories, read for tagline and licence, but nobody
  has read their `SKILL.md`, so this registry holds no install command for them.
  `list` marks them `†`. Recommending a `†` entry leaves the user with nothing to
  run; mention one only as a "there is also…" aside, pointing at its repo.
- `--cap` — repeatable, from step 2. Only the hand-read skills carry verdicts at
  all, so this narrows to those; a requirement can only be checked where someone
  checked it.
- `--lang` — the language the project's *own* documentation is written in. Worth
  setting: the handover in step 5 asks the user to read that project's trigger
  phrases, and a Chinese-only `SKILL.md` handed to someone who reads no Chinese
  is a dead end.

## Step 4 — decide between what survived

```bash
python "$SKILL_DIR/scripts/pick.py" compare ppt-master frontend-slides slide-creator
python "$SKILL_DIR/scripts/pick.py" show ppt-master --why
```

`compare` puts candidates side by side on stars, route, licence, doc language,
install method, prerequisites, style count, and the capability grid. Reach for it
the moment more than one candidate survives step 3 — it is faster than three
`show` calls and it makes the differences visible instead of remembered.

`show` is the full record for one skill: the install command and what that
method actually does, hard prerequisites, style ids, what its docs single out,
and the capability grid. `--why` adds the verbatim quote each capability claim
rests on, which is what you want before telling a user a skill does something.

Read the capability verdicts precisely — they are not shades of the same thing:

| verdict | means |
| --- | --- |
| `yes` | its documentation says it does this |
| `NO` | its documentation says it does **not** — decision-changing, e.g. HTML skills that explicitly cannot export PPTX |
| `?` | its docs are silent. **Not** the same as the feature being absent |
| `not read` | nobody has assessed this project for the registry at all |

Never report a `?` as a missing feature. Say the docs do not mention it.

## Style ids

```bash
python "$SKILL_DIR/scripts/pick.py" styles frontend-slides      # every style id for one skill, with its sample image URL
python "$SKILL_DIR/scripts/pick.py" find editorial              # search style ids and descriptions
```

**If the user opens by naming a style id**, start from `find <id>` instead of
step 1. A style id is not unique — several projects ship a `soft-editorial`, and
they are different decks. `find` prints every skill using the name; choose
between them on the route question, then confirm with `styles <skill>` so the
user is looking at the image that actually belongs to the skill you are about to
recommend.

## Step 5 — report and hand over

Give the user, in this order:

1. **The route**, and the one-line reason it followed from their answer.
2. **One skill**, not a shortlist. A second only if the first genuinely does not
   cover a stated requirement.
3. **Any prerequisite** `show` printed under `requires` — a Python version or a
   CLI version is the difference between an install that works and one that
   half-works.
4. **The install command exactly as `show` prints it**, including which of the
   five install methods it is — `plugin` commands are typed inside Claude Code,
   not a terminal, and `clone` lands in `~/.claude/skills/` and needs a session
   restart. This is the step people get wrong.
5. **Style ids**, when the user wants a particular look. Offer a few and say they
   can look at the images in the registry README to choose.

Then the user asks that skill for a deck in plain language, naming the style id
in the request. A style id is not a command-line flag.

```text
Use the soft-editorial template. Turn docs/roadmap.md into a 12-slide deck
for investors. I'll be speaking over it, so keep the text light.
```

Naming a style id also *skips* whatever selection step that project would
otherwise run — frontend-slides, for instance, generates three previews by
default and naming a template goes straight to it. If the user wants to be shown
options, tell them not to name one.

## Rules

- **Never invent another project's invocation syntax.** This registry has not
  run these skills. Their own `SKILL.md` is the authority on trigger phrases,
  flags and arguments. Say so rather than producing a plausible-looking command.
- **Never invent a style id.** They come from `data/samples.json`, derived from
  each project's own filenames and captions. If `pick.py` does not list one,
  it does not exist here. Several skills ship no imagery at all.
- **Capabilities are documented, not tested.** The grid reports what a project's
  docs claim, and a project that overclaims will be believed. Every cell carries
  the quote it rests on so the claim is checkable even when it is wrong —
  `show --why` prints them.
- **Star counts measure attention, not quality.** They order the list; they do
  not justify a recommendation on their own. Where a row links into a
  subdirectory of a monorepo, the stars belong to the parent repo.
- **Check the licence before recommending for commercial work.** `show` and
  `compare` flag copyleft. One skill in the registry is AGPL-3.0.

## What else is here

- `README.md` (Chinese) / `README.en.md` — the registry, the documented
  capability grid, and the full sample gallery with usage instructions.
- `principles/` — eight patterns extracted from reading these projects' source.
  Worth reading if the user is *writing* a skill rather than choosing one.
- `data/skills.json` — the only hand-maintained data file. Everything else is
  generated; see `README.md` for the pipeline.
