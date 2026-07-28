# 1 · Show, don't tell

**Never ask a user about taste. Generate options and let them point.**

Evidence: ★★★★★ — encoded by at least four independent projects, one of which calls it a
required phase.

---

## The principle

"What visual style would you like?" is a broken question. Most people cannot answer it.
They have taste — they know instantly whether they like something — but the vocabulary
to *specify* it in advance is a separate, rarer skill that has nothing to do with knowing
what they want.

So don't ask. Generate two to four real options and let them react.

---

## The evidence

**`frontend-slides`** makes this a numbered phase, not an optional nicety. Phase 2, Style
Discovery, generates exactly three previews:

1. A **safe preset** — the closest match from 12 curated styles
2. A **bold template** — from the 34-template pack
3. A **wildcard** — a second bold template, or a fully custom design

Its `SKILL.md` adds a constraint that matters more than the count: **preview authenticity**.
Each preview must look like a real first slide of *the user's actual deck*. Not a color
swatch, not a placeholder, not lorem ipsum. The user must be reacting to their own content
wearing the style, because that is the only thing that predicts how they will feel about
the finished deck.

Zara Zhang's own framing:

> "You don't need to be a designer to make beautiful things.
> **You just need to react to what you see.**"

**`huashu-design`** arrived at the same structure under a different name — the *Fallback
Advisor*. When a brief is vague, it generates three parallel visual directions, and it adds
a refinement: each direction is derived from a **different logic system**, not merely a
different color scheme. Three variations on one idea teach the user nothing; three
genuinely different premises let them discover which premise they respond to.

**`open-slide`** inverts the timing. Rather than previewing up front, it ships a
browser inspector: click any element, type "make this red", and `/apply-comments` applies
it. Same principle — reaction over specification — moved to after the first draft.

**`kaisersong/slide-creator`** lists "style discovery" as a headline feature, adopting the
pattern directly.

---

## Why it works

Three mechanisms, all of which survive contact with real users:

**Recognition beats recall.** Choosing from options shown is a fundamentally easier
cognitive task than retrieving a description from memory. This is why restaurants have
menus rather than asking what you feel like eating.

**It removes the vocabulary barrier.** A user who cannot say "Swiss International with a
warm neutral ground" can still point at it in two seconds. Requiring the words gates good
outcomes behind design education.

**It surfaces disagreement early, when it is cheap.** The expensive failure is generating
a complete 20-slide deck in a direction the user hates. Three cheap previews move that
discovery to minute two instead of minute twenty.

---

## How to apply it

**Generate 3.** Two feels like a forced binary; five is a paralysis of choice. Every
project that has iterated on this landed on three.

**Make the options genuinely different.** Three variations on one idea waste the
interaction. Vary the underlying premise — the type system, the density, the compositional
logic — not just the hue.

**Use the user's real content.** This is the part most implementations skip, and it is the
part that makes the difference. A preview built from placeholder text tests nothing.

**Include a wildcard.** `frontend-slides` reserves one slot for something the user probably
would not have asked for. It is the slot that produces the "oh, *that* one" reaction, and
it is where the taste discovery actually happens.

**Let them mix.** "The type from A, the palette from C" is a common and useful response.
Handle it.

**Never render the machinery.** `frontend-slides` explicitly bans workflow metadata from
appearing on slides — no "Option A" label, no template name, no internal note. The user
should see three decks, not three labeled specimens.

---

## Where it breaks

**When the user genuinely knows.** A brand designer with a spec sheet does not need to be
shown three options; making them sit through a discovery phase is condescending and slow.
Detect a specific brief and skip straight to generation.

**When previews cost too much.** Three previews mean three generations. On an expensive
model, or where each preview takes minutes, the economics can invert. Generating one slide
per option rather than a full deck keeps the cost proportional.

**When the options are all bad.** Show-don't-tell surfaces preference; it does not create
quality. Three mediocre previews produce a confidently chosen mediocre deck. This principle
sits on top of [principle 2](02-anti-ai-slop.md) — it does not substitute for it.

**When choice is not the bottleneck.** If the user's real problem is that their content is
unstructured, style discovery is premature. Fix the argument first.

---

## Generalizing beyond slides

Nothing here is about slides. Any agent task with a subjective decision point — naming,
copy tone, architecture trade-offs, color, layout, API shape — can use it. The question
"would you rather describe it, or point at it?" almost always answers itself.

The general form: **when a decision depends on taste, spend tokens generating options
instead of tokens asking questions.**
