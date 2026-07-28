# 5 · SKILL.md is a table of contents

**1,625 lines → 183. Same features, 89% less context.**

Evidence: ★★★★☆ — one project measured it precisely, and it is now the standard structure
for large skills.

---

## The principle

The instinct when writing a skill is to put everything the agent might need into one file.
That file loads on every invocation, whether or not any given run needs the PowerPoint
conversion section, the animation reference, or the deployment steps.

Instead: the main file is a **map**. It describes the workflow and says which file to read
when. Everything else loads on demand.

---

## The evidence

The clearest measurement comes from Zara Zhang, who restructured `frontend-slides` when it
was at 7,800 stars:

> "I just restructured it following the 'progressive disclosure' pattern: went from
> **1,625 lines loaded every time to 183**. Same functionality, **89% less context bloat**.
> **Treat your instruction file like a table of contents.**"

The resulting structure:

```
SKILL.md              28 KB   the map — always loaded
STYLE_PRESETS.md       8 KB   12 presets — loaded only during style discovery
bold-template-pack/           34 design systems + compact metadata — one gets loaded
html-template.md      11 KB   HTML structure — loaded at generation time
viewport-base.css    2.7 KB   inlined verbatim into every output
animation-patterns.md  4 KB   reference — loaded only if animating
scripts/                      PPT extraction, deploy, PDF export — executed, never read
```

The `bold-template-pack` detail is the sharp one. Thirty-four full design systems is far
too much to load. So each carries **compact metadata** — enough for the agent to *choose*
— and only the chosen template's full definition is ever read. Selection and content are
deliberately separated.

**`beautiful-html-templates`** takes this further, making the index a machine-readable
artifact: a 41 KB `index.json` of template metadata, with `AGENTS.md` as the operating
manual for querying it. The agent reads an index, matches a brief, then clones exactly one
template.

**Anthropic's official `pptx` skill** has the same shape: a `SKILL.md` that describes three
workflows and delegates to `scripts/` — `thumbnail.py`, `add_slide.py`, `clean.py`,
`validate.py`, `soffice.py`. Those scripts are *executed*, never loaded into context. Their
implementation costs zero tokens.

---

## Why it works

**Context is a budget shared with the actual work.** Tokens spent on the deployment section
during a run that never deploys are tokens unavailable for the user's content. On long
tasks this is the difference between a deck that holds together and one that forgets its
own first slide.

**Instructions dilute each other.** This matters more than the raw token cost. A rule
buried on line 1,400 of an always-loaded file competes for attention with 1,399 other lines.
The same rule, loaded at the moment it applies, is the most salient thing in view. Less
context does not merely cost less — it *works better*.

**Scripts are the ultimate compression.** A 200-line Python file loaded into context costs
200 lines. Invoked as `python scripts/clean.py`, it costs one. Anything deterministic
should be code the agent runs, never prose it reads.

---

## How to apply it

**Structure the main file as a decision tree, not a manual.** Each step: what to do, and
which file to read for detail. Aim for something a reader can hold in their head.

```markdown
## Phase 3 · Style discovery
Generate three previews. Read STYLE_PRESETS.md for the 12 presets.
For bold options, read bold-template-pack/index.json — metadata only —
then read the full definition for the ONE template you select.
```

**Split index from content.** Anything with many options needs a compact index for choosing
and separate files for the chosen one. This is the single highest-leverage move.

**Push determinism into scripts.** File manipulation, format conversion, validation,
deployment. If it has one correct answer, it should be code, not instructions.

**Load reference material lazily, by name.** Animation patterns, edge cases, format specs.
Name the file and say when it is needed.

**Inline only what every single output requires.** `viewport-base.css` is 2.7 KB and every
deck needs all of it, so it is always loaded. That is the correct exception, and it is
small.

**Measure it.** Count the lines that load on a minimal run. That number is your real
instruction size — not the repo's total.

---

## The general pattern

```
Always loaded    →  workflow map, universal constraints, the decision tree
Loaded on demand →  option catalogs, format references, edge cases
Never loaded     →  deterministic scripts (executed), templates (cloned)
```

This applies to every agent skill, not just slide skills. It is probably the most portable
principle in this collection: any `SKILL.md` past a few hundred lines is likely carrying
material that most runs never use.

---

## Where it breaks

**Round trips cost something too.** Every deferred file is another read. Splitting a
300-line file into six 50-line files buys nothing and adds five round trips. Progressive
disclosure pays off at scale — below roughly 500 lines, one file is usually right.

**Deferred rules can be missed.** A constraint in a file the agent decides not to read is a
constraint that does not apply. Anything genuinely universal — the fixed-stage rules, the
anti-slop bans — belongs in the always-loaded file even when it is long. Deferring is for
*reference*, not for *rules*.

**The map must be honest.** If `SKILL.md` says a file covers something it does not, the
agent reads it, finds nothing, and proceeds without the constraint. Index drift is silent
and nasty; when you move content, update the map in the same commit.

**It optimizes the wrong thing if the skill is small.** A 150-line skill does not have a
context problem. Restructuring it is procrastination dressed as engineering.
