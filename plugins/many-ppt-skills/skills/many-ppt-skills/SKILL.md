---
name: many-ppt-skills
description: Pick an AI slide-deck skill and a concrete visual style from a curated registry, with sample imagery and the style ids each project actually uses. Use when the user wants to make a presentation, deck or slides and has not already chosen a tool; asks which slide skill to use or what the difference is; wants to know what a style looks like before committing; or names a style id such as soft-editorial or swiss-grid. This skill routes to the skill that makes the deck — it does not make decks itself.
---

<!-- Generated from the SKILL.md at the repository root by
     scripts/sync_plugin.py. Edit that file, not this copy. -->

# many-ppt-skills

A registry of AI slide-deck skills, the imagery they publish, and the style ids
they name that imagery with. Your job with it is to get someone from "I need a
deck" to an installed skill and a style id, quickly, without guessing.

Counts are not written down here — `pick.py` prints them live, and a number
copied into prose is a number that goes stale.

**This skill does not generate decks.** It chooses which one will, and hands
over. If a deck skill is already installed and the user is happy with it, say so
and step aside rather than re-litigating the choice.

## Do this first: ask the route question

There is one question that decides everything downstream, and it is not about
taste:

> **Will anyone need to open the deliverable in PowerPoint and edit it?**

- **Yes → native PPTX.** The recipient edits normally. The design ceiling is
  bounded by what OOXML can express.
- **No → HTML-native.** A single `.html` file, far higher design ceiling, plain
  text in git. The recipient cannot edit it in Office.

Ask it. Do not infer it from the topic of the deck — a board update and a
conference talk can land on either side, and getting this wrong makes every
recommendation after it wrong. `python scripts/pick.py route` prints this along
with the current per-route counts.

## Then query the registry — do not read the JSON

The data files total roughly 200KB. Reading them into context to answer one
question is the mistake this repository has a whole principle about
(`principles/05-progressive-disclosure.md`). Use the CLI:

```bash
python scripts/pick.py route                  # the decision above, plus counts
python scripts/pick.py list --route pptx      # skills on one route, most-starred first
python scripts/pick.py show ppt-master        # install command, style ids, capabilities
python scripts/pick.py styles frontend-slides # every style id with its sample image URL
python scripts/pick.py find editorial         # search style ids and descriptions
```

`show` is the one to reach for once a candidate exists: it prints the install
command, what that install method actually does, the style ids the project uses,
and the capabilities its own documentation claims.

## Reporting a recommendation

Give the user, in this order:

1. **The route**, and the one-line reason it followed from their answer.
2. **One skill**, not a shortlist. A second only if the first genuinely does not
   cover a stated requirement.
3. **The install command exactly as `show` prints it**, including which of the
   five install methods it is — `plugin` commands are typed inside Claude Code,
   not a terminal, and `clone` lands in `~/.claude/skills/` and needs a session
   restart. This is the step people get wrong.
4. **Style ids**, when the user wants a particular look. Offer a few and say
   they can look at the images in the registry README to choose.

## Handing over

Once the skill is installed, the user asks it for a deck in plain language and
names the style id in that request. A style id is not a command-line flag.

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
- **Capabilities are documented, not tested.** `show` prints what a project's
  docs claim. A missing capability means its docs are silent, which is not the
  same as the feature being absent. `data/capabilities.json` carries the quote
  each claim rests on.
- **Star counts measure attention, not quality.** They order the list; they do
  not justify a recommendation on their own.
- **Check the licence before recommending for commercial work.** `show` flags
  copyleft. One skill in the registry is AGPL-3.0.

## What else is here

- `README.md` (Chinese) / `README.en.md` — the registry, the documented
  capability grid, and the full sample gallery with usage instructions.
- `principles/` — eight patterns extracted from reading these projects' source.
  Worth reading if the user is *writing* a skill rather than choosing one.
- `data/skills.json` — the only hand-maintained file. Everything else is
  generated; see `README.md` for the pipeline.
