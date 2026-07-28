# Scoring Rubric

[English](rubric.md) · [简体中文](rubric.zh-CN.md)

Seven dimensions, scored **0–5**, for a maximum of **35**. Every score must cite
evidence — a slide number, a screenshot, a specific missing figure. A score with no
citation is not a score, it is an opinion, and it gets stripped in review.

The anchors below exist so that two people scoring the same deck independently land
within one point of each other. If you find yourself hesitating between two levels,
pick the lower one and say why in the note.

---

## Why these seven

Each dimension isolates a failure mode that the [corpus](corpus/) is built to provoke.
They are scored separately because skills fail asymmetrically: a skill can produce a
gorgeous deck that invents numbers, or a factually perfect deck that looks like a 2009
template. Collapsing those into one number hides exactly the information you need to
choose between them.

| # | Dimension | Weight | The question it answers |
|---|---|---|---|
| 1 | [Visual distinctiveness](#1-visual-distinctiveness) | ×1 | Does it look designed, or does it look generated? |
| 2 | [Typographic craft](#2-typographic-craft) | ×1 | Would a designer wince? |
| 3 | [Hierarchy & density fit](#3-hierarchy--density-fit) | ×1 | Does the density match the stated audience? |
| 4 | [Data fidelity](#4-data-fidelity) | ×1 | Did every number, table and code block survive intact? |
| 5 | [Content fidelity](#5-content-fidelity) | ×1 | Did it keep the content — and invent nothing? |
| 6 | [Deliverable integrity](#6-deliverable-integrity) | ×1 | Does the artifact actually work where it must work? |
| 7 | [Effort to acceptable](#7-effort-to-acceptable) | ×1 | How much correction did it take to get there? |

Dimensions 4 and 5 are **gating**. A score of 0 on either caps the total at 17 no matter
how the rest scored, and the skill is flagged. A beautiful deck with fabricated financials
is worse than no deck — it is a liability, and the ranking must say so.

---

## 1. Visual distinctiveness

Whether the output reads as a deliberate design or as the statistical average of every
deck in the training set. This is the "AI slop" axis.

| Score | Anchor |
|---:|---|
| **5** | Could plausibly be attributed to a named design studio. Committed palette with a dominant tone and a sharp accent. Atmospheric backgrounds. A visual idea that recurs and develops across slides. |
| **4** | Clearly designed and coherent. A distinct point of view, executed consistently, but without a memorable signature. |
| **3** | Competent and inoffensive. Reads as a good template. Nothing wrong; nothing anyone will remember. |
| **2** | Generic. Default-adjacent palette, flat backgrounds, stock layout rhythm. Recognizably machine-made on a glance. |
| **1** | Actively dated or incoherent. Clashing colors, mismatched decorative elements, or three unrelated styles in one deck. |
| **0** | No discernible design intent. Unstyled or near-unstyled output. |

**Automatic deductions (−1 each, floor 0).** These are the tells that the field has
independently converged on — both `frontend-slides` and Anthropic's official `pptx`
skill ban them by name:

- Decorative accent line under the title, or a decorative color bar, carrying no information
- Flat single-color background on every slide with no atmospheric variation
- A palette distributed so evenly that no color dominates — what `frontend-slides`
  calls a "timid" palette
- Icon set applied ornamentally, one icon per bullet, adding no meaning
- Workflow metadata leaking onto a slide ("Option A", a template name, an internal note)

---

## 2. Typographic craft

| Score | Anchor |
|---:|---|
| **5** | Deliberate type pairing with real contrast. Optical alignment. Considered measure (~45–75 characters). Tabular figures in tables. Hierarchy legible at a glance from across a room. |
| **4** | Good pairing and a clean scale. Minor spacing or alignment inconsistencies on a few slides. |
| **3** | One serviceable typeface used sensibly. Hierarchy present but blunt — mostly size, little weight or spacing. |
| **2** | Default system stack. Inter, Roboto, Arial, Helvetica or the PowerPoint default, unmodified. Cramped or unconsidered line height. |
| **1** | Actively broken. Text overflows its container, clips, or overlaps another element on any slide. |
| **0** | Illegible at presentation size. |

**Note on banned fonts.** `frontend-slides` bans Inter, Roboto and Arial outright, on the
grounds that a default font signals no choice was made. This rubric does not ban them —
Inter set with genuine care beats a distinctive face set badly. But reaching for the
default *and* not compensating elsewhere lands you at 2.

---

## 3. Hierarchy & density fit

Scored against the density the corpus **asks for**, not against a universal ideal.
Corpus 01 is speaker-led and wants air. Corpus 02 is reading-first and wants substance.
Punishing 02 for being dense is a scoring error.

| Score | Anchor |
|---:|---|
| **5** | Density matches the brief exactly. Every slide has one clear entry point. Grouping is visual, not merely spatial. Where the corpus specifies action titles, every title asserts a finding. |
| **4** | Density is right; one or two slides drift from the target. Hierarchy holds throughout. |
| **3** | Roughly right, with several slides noticeably over or under target. Hierarchy is inconsistent. |
| **2** | Systematically wrong for the audience — a speaker-led deck stuffed with bullets, or a reading-first deck so sparse it is unusable circulated. |
| **1** | No hierarchy. Undifferentiated bullet lists throughout. |
| **0** | Content dumped onto slides with no structural transformation at all. |

**Action-title check** (Corpus 02 only). Count titles that assert a finding versus titles
that label a topic. "Q3 revenue grew 12.4% on enterprise renewals" asserts.
"Q3 Revenue" labels. Below 70% asserting caps this dimension at 3.

---

## 4. Data fidelity · **gating**

Every number, table, chart and code listing from the corpus, reproduced correctly.

| Score | Anchor |
|---:|---|
| **5** | Every figure present and exact. Tables complete with all rows and columns. Charts plot the actual supplied values. Code retains syntax highlighting and exact indentation. |
| **4** | All figures correct. One cosmetic loss — a table split awkwardly across slides, or a chart missing axis labels. |
| **3** | All figures correct, but a table was truncated or a chart was rendered as a static image that cannot be verified against source. |
| **2** | A figure is misplaced, mislabeled, or attached to the wrong segment. Recoverable but wrong on the slide. |
| **1** | Multiple figures wrong, or a table materially altered. |
| **0** | **Any fabricated figure.** Any number in the deck that is not in the corpus. Also 0 if code is rendered as an image, or if indentation is destroyed. |

**How to check.** Do not eyeball this. Extract every numeric token from the deck and diff
it against the corpus:

```bash
python benchmark/runner/check_fidelity.py \
    --corpus benchmark/corpus/02-quarterly-review.md \
    --deck   benchmark/results/<skill>/02-quarterly-review/
```

Corpus 02 states the rule inside the material itself, so a skill that reads its input
carefully has been warned.

---

## 5. Content fidelity · **gating**

Whether the argument survived. Distinct from dimension 4: a deck can preserve every
number while destroying the reasoning that connects them.

| Score | Anchor |
|---:|---|
| **5** | Every substantive point represented. Structure and emphasis preserved. Nothing invented. Editorial compression is fine — dropping meaning is not. |
| **4** | Complete, with one minor point compressed away. |
| **3** | One substantive section dropped or flattened enough to lose its point. |
| **2** | Multiple sections missing, or emphasis inverted so a minor point reads as the headline. |
| **1** | Reduced to a topical summary. The specific argument is gone. |
| **0** | **Invented substantive content** — a claim, quote, source or recommendation not in the corpus. |

**On the fictional-source markers.** Each corpus marks its sources as fictional. A skill
that silently strips those markers and presents the figures as real is not penalized
here — that is a judgement call, not a defect — but note it. A skill that *preserves*
them shows unusual care and is worth a mention in the writeup.

---

## 6. Deliverable integrity

Does the artifact work in the context it was built for. Route-specific, because the two
routes make different promises.

**HTML route**

| Score | Anchor |
|---:|---|
| **5** | Single self-contained file. Opens with no server. Keyboard navigation works. Correct at 1920×1080 and letterboxes cleanly at other ratios. PDF export preserves layout. |
| **4** | Self-contained and correct; one export path or navigation affordance is rough. |
| **3** | Works but has external dependencies — a CDN link, a remote font, a fetch — that will break offline or when the CDN moves. |
| **2** | Requires a build step or local server that was not disclosed up front. |
| **1** | Renders with visible breakage — overflow, clipping, broken transitions. |
| **0** | Does not open or does not present. |

**PPTX route**

| Score | Anchor |
|---:|---|
| **5** | Opens clean in PowerPoint, Keynote and LibreOffice. All elements are native objects — real text frames, real shapes, real charts with editable data. Template and master respected where supplied. |
| **4** | Opens clean everywhere. One element flattened to an image where it need not have been. |
| **3** | Opens clean in PowerPoint only. Degrades visibly in Keynote or LibreOffice. |
| **2** | Substantially image-based. Text is not selectable or editable. |
| **1** | Opens with a repair prompt, or with visible corruption. |
| **0** | Does not open. |

Verify PPTX output with the validator from Anthropic's official skill, then render and
look at it — a file can be schema-valid and visually broken:

```bash
soffice --headless --convert-to pdf deck.pptx && pdftoppm -png -r 96 deck.pdf slide
```

---

## 7. Effort to acceptable

How much correction stood between the first output and something you would actually
present. Measured in **correction turns**: one turn is one instruction to the agent
asking it to change something. Answering the skill's own interview questions is not a
correction turn — that is the intended workflow.

| Score | Turns | Anchor |
|---:|---:|---|
| **5** | 0 | First output was presentable as-is. |
| **4** | 1–2 | Minor polish. |
| **3** | 3–5 | Normal iteration. |
| **2** | 6–10 | Substantial rework. |
| **1** | 11–20 | Faster to have started over. |
| **0** | >20 or never | Never reached acceptable within budget. |

Cap every run at **20 correction turns**. If it has not converged by then, score 0, record
where it was stuck, and move on. Log every turn verbatim in `run.jsonl` — the transcript
is more informative than the score.

---

## Objective metrics

Recorded alongside the scores, not scored themselves. These are facts, and facts age
better than judgements.

| Metric | Unit | How |
|---|---|---|
| Wall-clock to first output | seconds | Harness timer |
| Correction turns | count | Manual log |
| Output size | KB | `du -k` |
| External runtime dependencies | count | Count of non-`data:` remote URLs in the artifact |
| Slide count delivered vs. requested | ratio | Manual |
| Peak agent context | tokens | If the agent reports it |

---

## Scoring procedure

1. **Blind the run.** Score from `results/<run-id>/<corpus>/` with the skill name masked.
   `runner/anonymize.py` handles this. Knowing you are looking at the 26k-star project
   moves scores, and it moves them by more than you think.
2. **Score dimensions 4 and 5 first**, mechanically, before looking at the design. If
   either gates to 0, the deck is flagged regardless of how good it looks — and knowing
   that before you fall for the typography keeps the aesthetic score honest.
3. **Score 1–3 from screenshots only**, at presentation size, not by scrolling source.
   The audience will not read the source.
4. **Cite evidence for every score.** Slide number or screenshot filename. No citation,
   no score.
5. **Two independent scorers.** Where they differ by ≥2 on any dimension, both write a
   note and the lower score stands. Publish the disagreement — it is signal about the
   rubric, not noise to be smoothed away.

---

## What this rubric deliberately does not measure

Stated plainly so nobody mistakes the ranking for more than it is:

- **Taste.** Dimension 1 measures distinctiveness, not whether *you* like it. A brutalist
  deck and a soft-editorial deck can both score 5.
- **Breadth of features.** A skill with 50 themes and one with 3 are scored on the deck
  they produced, not the menu they offer.
- **Suitability for your brand.** No rubric can score that. Run the corpus yourself with
  your own materials.
- **Cost.** Token spend varies too much by model and context to compare fairly.
- **How it will score next month.** These are fast-moving projects. Every score carries
  the commit SHA it was run against, and stale scores are re-run, not defended.
