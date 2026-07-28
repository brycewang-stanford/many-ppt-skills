# run-01 · frontend-slides × 02-quarterly-review

**Date:** 2026-07-28 · **Agent:** Claude Code · **Model:** claude-opus-5
**Skill commit:** [`9906a34`](https://github.com/zarazhangrui/frontend-slides/commit/9906a34d640d2111f724544cbc50f7f130569ae1)
**Result:** [25.0 / 35](frontend-slides/02-quarterly-review/score.json) — *corrected down from 28.0; see [Corrections](#corrections)*

> **Read this as harness validation, not as a verdict on the skill.** The operator who
> executed the skill also wrote the corpus and the rubric, and then scored the output.
> That is not an independent measurement, and the score file records
> `operator_conflict: true` for exactly that reason. n=1 against known generative
> variance. **An independent re-score of this pairing from the committed artifacts is the
> most valuable contribution anyone can make to this repo.**

---

## Corrections

The original scoring was done by the operator who generated the deck. The same artifacts
were later re-scored by a [blind two-judge panel](../../runner/judge.py) — screenshots
only, no skill name, no deck source — and measured with
[`check_charts.py`](../../runner/check_charts.py). Two claims did not survive. Both
corrections went **against** the deck, and the originals are intact in git history at
`27a8244`.

| Dimension | Was | Now | Why |
|---|---:|---:|---|
| Visual distinctiveness | 4 | **3** | The original said "No automatic deductions apply". A decorative gold rule sits under the section label on every interior slide, carrying no information — the first automatic deduction this dimension lists, and the same accent line frontend-slides' own docs ban by name. Both blind judges found it independently and cited slides. |
| Data fidelity | 5 | **3** | The original said slide 4 "plots all eight supplied quarterly values from a genuine zero baseline". True of the markup, false of the pixels: all eight bars render at exactly 288px. The anchor for 5 requires that charts plot the actual supplied values. |

The chart is the more interesting failure. Declared heights are perfect —
`36.1 → 76.5%` through `47.2 → 100%` — and the percentages then resolve against a flex
column of indefinite height, so CSS drops them. Values span 1.31×, rendered heights span
1.0000×. `check_fidelity.py` scores that slide 100% because every number is present, and
reading the source finds nothing wrong because the source *is* right.

Note what this says about the original scoring: the claim cited `slide-04.png`, a
screenshot, and described something the screenshot does not show. Looking is not the same
as measuring, and an operator scoring their own output does both less carefully.

---

## What was run

[Corpus 02 — Quarterly Business Review](../../corpus/02-quarterly-review.md) pasted
unmodified into an agent following
[frontend-slides](https://github.com/zarazhangrui/frontend-slides)' `SKILL.md`.

The skill's Phase 1 asks four questions (purpose, length, content readiness, density).
Those were answered from the corpus brief — internal presentation, 10–20 slides, all
content ready, **high density / reading-first** — and are *not* counted as correction
turns, per [the protocol](../../README.md#running-it).

Phase 2 (style discovery) selected from the skill's own template metadata. `Signal` was
the strongest match on the index: `formality: high`, `density: high`, and a `best_for`
that literally names board presentations. Phase 3 generated from
`bold-template-pack/templates/signal/design.md`.

## Score

| Dimension | Score | One-line reason |
|---|---:|---|
| Visual distinctiveness | **4** / 5 | Signal executed coherently; inherited rather than authored for this brief |
| Typographic craft | **4** / 5 | Deliberate three-face ladder; an orphaned line and detached chart labels |
| Hierarchy & density fit | **3** / 5 | Reading-first brief, speaker-led result. ~55% empty canvas on several slides |
| **Data fidelity** | **5** / 5 | 56/56 figures, 0 fabricated, 0 missing |
| **Content fidelity** | **5** / 5 | All ten sections present, nothing invented |
| Deliverable integrity | **3** / 5 | Three remote font dependencies — not self-contained |
| Effort to acceptable | **4** / 5 | 1 correction turn |

Full reasoning with citations: [`score.json`](frontend-slides/02-quarterly-review/score.json)

## Artifacts

```
frontend-slides/02-quarterly-review/
├── deck.html          the deliverable (36 KB, single file)
├── fidelity.json      check_fidelity.py output
├── score.json         scores, evidence, findings
└── shots/
    ├── contact-sheet.png   all 12 slides tiled — start here
    └── slide-01..12.png    full-resolution, 1920×1080
```

Re-score from these directly. Nothing here requires trusting the numbers above.

---

## Findings

### 1 · "Zero dependencies" is not what the skill actually produces · *notable*

The skill's **Core Principle #1** is *"Zero Dependencies — Single HTML files with inline
CSS/JS. No npm, no build tools."*

Its own `html-template.md:16` prescribes:

```html
<link rel="stylesheet" href="https://api.fontshare.com/v2/css?f[]=...">
```

and `templates/signal/design.md:467` documents a Google Fonts preconnect pattern. So every
deck the skill produces carries a **network dependency for its typography**. Offline, or
once the CDN moves, the type falls back to Georgia and system stacks — which is precisely
what the skill's own anti-slop rules forbid.

The two instructions are in genuine conflict, and the output inherits the conflict.
This is what caps deliverable integrity at 3.

*Fixable by the user:* subset the three families and inline them as `data:` URIs. Roughly
40–60 KB for the weights actually used here.

### 2 · The template's own metadata contradicts its design recipe · *notable*

`bold-template-pack/selection-index.json` labels Signal:

```json
"formality": "high", "density": "high"
```

`templates/signal/design.md` says:

> **Density philosophy: medium-low and asymmetric.** ... A slide that feels broken in
> Signal is one that fills the canvas edge-to-edge with content.

and, in its Don'ts:

> Don't fill more than half a typical slide with content.

Selecting Signal for a reading-first brief **because the index says `density: high`**, then
generating from `design.md`, produces a sparse speaker-led deck for a dense reading-first
request. Following the skill correctly at every step still lands the density wrong.

This is the most transferable finding here: **selection metadata and design recipes have to
agree, or the selection step actively misleads.**

### 3 · A layout bug only the screenshot caught · *defect*

The em-dash bullet was implemented as a two-column grid on the `<li>`:

```css
.list li { display: grid; grid-template-columns: 1.2em 1fr; }
```

Every inline `<em>` then becomes its own **grid item**, wrapping onto a new row and landing
on top of the adjacent text — `$2.4M` over "capex", `60%` over "of projected volume".

The source reads as correct. Only the render shows it. This is
[principle 07](../../../principles/07-render-and-look.md) earning its place, and it is why
the protocol screenshots before scoring.

### 4 · An honest chart that communicates little · *minor*

The eight-quarter trend runs 36.1 → 47.2 plotted from a true zero baseline, so all eight
bars are within 24% of each other and look nearly identical. Every value is printed, so
nothing is misleading — but the chart carries almost no information the numbers don't.

A truncated axis would read far better and would need an explicit break marker to stay
honest. Worth noting that no skill in the registry appears to handle this trade-off
deliberately.

---

## Harness defects this run exposed

Both found and fixed while running. Recorded here because a benchmark that hides its own
tooling bugs is not worth reading.

**`check_fidelity.py` counted the operator brief as expected content.** Each corpus opens
with instructions to the operator — target length, failure modes, and a worked *example* of
an action title containing "12%". The checker treated that example figure as content the
deck must reproduce, so an honest deck showed as having dropped a figure. Fixed by trimming
the corpus to everything from `## Content` onward.

**`check_fidelity.py` reported sign conventions as fabrication.** The deck writes "customs
declined 15.8%"; the corpus table says "−15.8%". Same fact. The checker called it a
fabricated figure — which, under the gating rule, would have forced this run to 0 on data
fidelity and capped it at 17/35. Fixed: magnitude matches with differing sign now report
separately as sign/direction differences needing a wording check.

The second one matters. Left in, it would have fired on nearly every honest run and made
the gating dimension worthless.

---

## What this run does not tell you

- **Whether frontend-slides is better than any other skill.** n=1, one corpus, one skill.
- **Whether a second run would score the same.** It very likely would not — generative
  variance is real and unmeasured here.
- **How it handles the other two corpora.** The product-launch and tech-talk corpora stress
  entirely different things (hero moments; code and diagrams) and are unrun.
- **Anything about the PPTX route**, which is still completely uncovered.
