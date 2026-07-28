# 7 · Render it and look at it

**Visual output needs visual QA. Screenshot the result and let the model see its own work.**

Evidence: ★★★☆☆ — Anthropic's official skill mandates it; most community skills skip it,
and it shows.

---

## The principle

A model that writes 800 lines of CSS has no idea what it looks like. It can verify the code
is syntactically valid, that class names match, that the palette variables were used. It
cannot tell you that the headline overflows its container on slide 7, or that the chart
legend landed on top of the last data point.

Those are the defects that matter, and they are only visible in an image.

So: render the output, convert it to images, and put the images back in front of the model.

---

## The evidence

**Anthropic's official `pptx` skill** ships this as a mandated QA pipeline:

1. `markitdown deck.pptx` — verify the content is present
2. `python scripts/office/validate.py` — schema, relationships, content checks
   (`--original` when derived from a template)
3. `soffice --convert-to pdf`, then `pdftoppm` — **convert to images and inspect visually**

Step 3 is the one almost nobody else does. Steps 1 and 2 prove the file is well-formed.
Only step 3 catches the deck being *ugly or broken*.

The skill also ships `scripts/thumbnail.py`, which generates a labeled grid of slide
layouts — an image built specifically so the model can reason about layout rather than
about XML.

**`frontend-slides`** ships Playwright-based PDF export at 1920×1080. It is framed as a
delivery feature, but it is the same capability, and it can be pointed at QA.

**`huashu-design`** goes furthest on the evaluation side with its 5-dimension expert
critique — philosophical consistency, visual hierarchy, execution detail, functionality,
innovation, each scored 0–10 with a radar chart and a Keep / Fix / Quick Wins punch list.
It is a structured self-review of the rendered artifact rather than of the source.

**`Phlegonlabs/Powerpoint-fancy-design`** emits PNG renders as a first-class output.

That is roughly it. Four projects out of thirty. **This is the largest quality gap in the
ecosystem** — and the cheapest one to close.

---

## Why it works

**The model's failure modes are spatial, and source is not spatial.** Overflow, collision,
contrast failure, awkward line breaks, a chart legend covering data, text clipped at a
container edge — none of these are visible in CSS. All of them are obvious in a screenshot.

**Vision-capable models are genuinely good at this.** Shown a rendered slide, a model
reliably spots "the subtitle is colliding with the image" — a judgement it cannot make from
the markup that produced it.

**It closes the loop.** Without rendering, the model's last observation is "I wrote the
code I intended to write". With rendering, it is "here is what actually happened". Those are
different claims, and only the second one is about the artifact the user receives.

**It catches environment drift.** A font that failed to load, a CSS feature the renderer
does not support, a `data:` URI that got truncated. The code is correct; the output is not.

---

## How to apply it

**HTML route:**

```bash
python benchmark/runner/screenshot.py --deck deck.html --out shots/ --contact-sheet
```

Then read the images back. The [screenshotter](../benchmark/runner/screenshot.py) in this
repo handles slide-by-slide capture and can tile a contact sheet — one image showing the
whole deck, which is the fastest way to spot a slide that does not belong.

**PPTX route:**

```bash
soffice --headless --convert-to pdf deck.pptx
pdftoppm -png -r 96 deck.pdf shots/slide
```

**Give the model a checklist, not "does this look good?"** An open question gets a generous
answer. A specific one gets a useful answer:

```
Review each screenshot against this list. Cite the slide number for every issue.
- Does any text overflow, clip, or collide with another element?
- Is body text legible at presentation size (>= 24px at 1920 wide)?
- Does every slide use the committed palette, with no stray colors?
- Is there a decorative line under any title, or a decorative color bar? (banned)
- Does any slide carry workflow metadata that should not ship?
- Is the type hierarchy consistent slide to slide?
```

**Check the contact sheet for rhythm.** Individual slides can each be fine while the deck
has no pacing — six dense slides in a row, or three consecutive slides with identical
structure. Only the tiled view shows this.

**Automate what is mechanical.** Overflow detection does not need a model:

```javascript
// Anything wider or taller than the stage is overflowing it.
[...document.querySelectorAll('.slide *')]
  .filter(el => el.scrollWidth > 1920 || el.scrollHeight > 1080)
  .map(el => el.className);
```

Reserve the model's attention for judgement, and let code catch the deterministic failures.

---

## Where it breaks

**Cost.** Rendering 20 slides and feeding 20 images back is a lot of tokens. Mitigate with
a contact sheet first, then full-resolution only on the slides that look wrong.

**Renderer fidelity.** LibreOffice's PPTX rendering is not PowerPoint's. A slide can look
broken in the screenshot and fine in PowerPoint, or the reverse. Treat LibreOffice output
as a smoke test, not as ground truth.

**Animation is invisible in stills.** Screenshots capture one moment. Entrance animations,
transitions and timing-dependent layout are not covered. Video capture exists but is rarely
worth the complexity.

**It needs vision.** A text-only model cannot do this step. The pipeline still helps —
overflow detection and validators run either way — but the judgement half requires a
vision-capable model.

**It cannot fix bad ideas.** Rendering catches execution defects. A deck that is well-laid-
out and makes a bad argument will pass every visual check.
