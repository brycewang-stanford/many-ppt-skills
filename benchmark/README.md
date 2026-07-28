# The Benchmark

Every "best AI PPT skill" ranking on the internet is a re-sort of GitHub star counts.
Stars measure how well an author tweets. They do not measure whether the deck invents
your revenue figures.

This is an attempt at the other thing: **the same material, through every skill, scored
against a published rubric, with the screenshots attached.**

---

## Status

| | |
|---|---|
| Corpus | ✅ 3 materials, complete |
| Rubric | ✅ 7 dimensions, anchored, 2 gating |
| Harness | ✅ fidelity checker, screenshotter, scorecard — all working |
| **Runs** | 🟡 **1 of 78** possible skill × corpus pairings |

Current results: [`results/scorecard.md`](results/scorecard.md) ·
write-up: [`run-01`](results/run-01/README.md)

**[run-01](results/run-01/README.md)** — frontend-slides × quarterly-review, 28/35. Deck,
12 screenshots and per-dimension evidence all committed, so the run can be re-scored by
anyone without trusting the number.

It is one run, by an operator who also wrote the corpus and the rubric, and it is labelled
as such in the score file. It is evidence the harness works. It is not a ranking, and this
page will keep saying so until enough independent runs exist to support one.

The run also broke the harness twice — `check_fidelity.py` was counting figures out of the
operator brief, and was reporting sign-convention differences as fabrication. Both are
fixed; both are written up rather than quietly patched, because a benchmark that hides its
own tooling bugs is not worth reading.

---

## What is being tested

Three [corpus](corpus/) materials, each built to provoke a different failure mode:

| Corpus | Stresses | Exposes |
|---|---|---|
| [01 · Product launch](corpus/01-product-launch.md) | Hero moments, low density, brand personality | Generic templates, timid color, bullet-walls where one idea belongs |
| [02 · Quarterly review](corpus/02-quarterly-review.md) | Data fidelity, tables, charts, action titles | **Fabricated figures**, truncated tables, decorative styling that fights readability |
| [03 · Tech talk](corpus/03-tech-talk.md) | Code blocks, diagrams, progressive build | Code as images, destroyed indentation, lost syntax highlighting |

All three are fictional. Corpus 02 states inside the material that any figure not present
in the source is a hallucination — a skill that reads its input carefully has been warned.

Scoring: [`rubric.md`](rubric.md) — 7 dimensions × 0–5, max 35. Data fidelity and content
fidelity are **gating**: a zero on either caps the total at 17 regardless of how good the
deck looks.

---

## Running it

### 1. Set up

```bash
pip install playwright Pillow && playwright install chromium
# PPTX-route skills additionally need LibreOffice and poppler:
#   brew install --cask libreoffice && brew install poppler
```

### 2. Generate a deck

Install the skill per its own instructions, then hand it the corpus verbatim:

```
Read benchmark/corpus/02-quarterly-review.md and build the deck it describes.
Follow the brief exactly, including the target length and audience.
```

**Rules that keep runs comparable:**

- Paste the corpus **unmodified**. No hints, no style steering beyond what the corpus states.
- Answering the skill's own interview questions is **not** a correction turn — that is its
  intended workflow. Answer as a reasonable user would and log what you said.
- Every subsequent instruction **is** a correction turn. Log each one verbatim.
- Cap at **20 correction turns**. Not converged by then → score 0 on effort, record where
  it stuck, move on.
- Record the skill's **commit SHA**. These projects change weekly; a score without a SHA
  is unfalsifiable.

Save output to `results/<run-id>/<skill-id>/<corpus-id>/`.

### 3. Check fidelity — before you look at the design

```bash
python benchmark/runner/check_fidelity.py \
  --corpus benchmark/corpus/02-quarterly-review.md \
  --deck   benchmark/results/run-01/frontend-slides/02-quarterly-review/ \
  --json   benchmark/results/run-01/frontend-slides/02-quarterly-review/fidelity.json
```

Exits 1 on any fabricated figure. Do this **first**, mechanically, before the typography
seduces you. Not every flagged number is a defect — page numbers, computed totals and axis
ticks are legitimate — but every one gets reviewed by hand.

### 4. Screenshot

```bash
python benchmark/runner/screenshot.py \
  --deck benchmark/results/run-01/frontend-slides/02-quarterly-review/deck.html \
  --out  benchmark/results/run-01/frontend-slides/02-quarterly-review/shots/ \
  --contact-sheet
```

For PPTX output:

```bash
soffice --headless --convert-to pdf deck.pptx
pdftoppm -png -r 96 deck.pdf shots/slide
```

### 5. Score

Write `score.json` next to the deck. Shape is documented at the top of
[`runner/scorecard.py`](runner/scorecard.py). Then:

```bash
python benchmark/runner/scorecard.py --validate   # check the file
python benchmark/runner/scorecard.py              # rebuild the scorecard
```

Score dimensions 1–3 **from the screenshots at full size**, not by scrolling source. The
audience will not read the source.

---

## Methodology commitments

These exist to make the benchmark falsifiable. Without them it is just a louder opinion.

1. **Blind scoring.** Skill names are masked during scoring. Knowing you are looking at
   the 26k-star project moves scores, by more than anyone expects.
2. **Two scorers, disagreements published.** Where they differ by ≥2 on any dimension,
   the lower score stands and both notes are published. Disagreement is signal about the
   rubric, not noise to smooth away.
3. **Evidence or it did not happen.** Every score cites a slide number or screenshot.
   Uncited scores are stripped in review.
4. **Every artifact committed.** Decks, screenshots and transcripts all land in
   `results/`. Anyone can re-score from the raw material and reach a different conclusion.
5. **Version-pinned.** Every run records the skill's commit SHA, the agent, and the model.
6. **Re-run, don't defend.** These projects ship weekly. Stale scores get re-run. A score
   older than 90 days is marked stale in the scorecard.
7. **Author right of reply.** Any skill author may open an issue disputing a run. If the
   run was flawed, it gets re-run and the original stays visible in git history.

---

## Known limits

Stated up front, because a benchmark that oversells itself is worse than none:

- **Sample size is small.** Three corpora cannot represent every deck anyone makes.
- **Generative variance is real.** The same skill, same prompt, same model produces
  different output run to run. Multiple runs per pairing are needed before small score
  gaps mean anything. Until run counts are in the double digits, treat a 2-point gap as
  noise.
- **Model-dependent.** A skill run on a different model is a different system. The model
  is recorded per run; cross-model comparison is not valid.
- **Taste is not measured.** Dimension 1 scores distinctiveness, not whether you like it.
- **The scorer is not neutral.** I did the research that produced the registry. Blind
  scoring mitigates this; it does not eliminate it. Independent scorers welcome — that is
  the single most valuable contribution anyone can make here.

---

## Contributing a run

Runs from people who are not me are worth more than runs from me. See
[CONTRIBUTING.md](../CONTRIBUTING.md).

Most valuable, in order:

1. **An independent second score** on a pairing already run — directly tests scorer bias.
2. **A run on a skill with no runs yet** — especially PPTX-route skills, which are
   under-covered relative to how many people actually need editable output.
3. **A corpus that breaks skills in a way the current three do not** — RTL languages,
   dense CJK typography, and accessibility requirements are all uncovered gaps.
