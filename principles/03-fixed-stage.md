# 3 · Slides are print, not web

**Fixed 1920×1080. Scale to fit. Letterbox the remainder. Give up responsive design.**

Evidence: ★★★★★ — near-universal across the HTML route, and `frontend-slides` marks it
**non-negotiable**.

---

## The principle

A slide is a fixed-aspect composition that will be projected. It is closer to a poster
than to a web page. Every instinct a web developer has about fluid layout is wrong here,
and following those instincts is the single most common way agent-generated HTML decks
break in the room.

So: build on a fixed canvas, scale it uniformly, and accept bars on the sides.

---

## The evidence

**`frontend-slides`** states it as a hard rule, in these terms:

- Every slide lives inside a fixed **1920×1080** canvas that scales uniformly to the viewport
- Content **never reflows for mobile** — letterboxing and pillarboxing preserve 16:9
- Slide visibility toggles `.active` / `.visible` classes, **not `display: none`**
- **No responsive breakpoints** that rearrange slide content
- A `viewport-base.css` must be inlined verbatim into every generated deck

**`open-slide`** builds its entire runtime around it: arbitrary React components rendered
to a fixed 1920×1080 canvas, with scaling handled by the framework so authors never touch it.

**`Phlegonlabs/Powerpoint-fancy-design`** uses 1600×900 — same 16:9 ratio, different
absolute size, identical principle.

Essentially every HTML-route project in [the registry](../README.md) does some version of
this. It is the closest thing the category has to a settled standard.

---

## Why it works

**What you saw is what they see.** With a fixed stage, the deck you approved in your browser
is pixel-identical to the deck on the projector. With responsive layout it is a different
composition at every width, and you cannot preview all of them. Presenting is a live
performance with no undo — surprise is the enemy.

**Design decisions become absolute.** "This headline is 96px" means something on a fixed
canvas. On a fluid one, every size is a function of viewport and every relationship between
elements is contingent. Fixed dimensions are why print designers can make precise
decisions, and they buy the same thing here.

**Projectors are 16:9 anyway.** The responsive machinery solves a problem that does not
exist. Nobody presents to a phone.

**Overflow becomes visible instead of silent.** On a fixed canvas, too much content
overflows the frame and you *see* it immediately. Fluid layout absorbs overflow by
reflowing — hiding the problem until it appears on someone else's screen at a width you
never tested.

### The `display: none` detail

This one looks like a nitpick and is not. Hidden slides must remain in the layout — hidden
via `visibility`, `opacity` or a class toggle — because `display: none` removes an element
from the box model entirely. An element that was never laid out cannot transition *in*: it
has no starting geometry to animate from, so entrance animations either snap or fail.

This is exactly the kind of rule that is obvious in hindsight, invisible in advance, and
worth encoding because a model will otherwise reach for `display: none` every time.

---

## How to apply it

The whole mechanism is about fifteen lines:

```css
/* The stage: a fixed 1920x1080 world, centered in whatever viewport exists. */
.stage {
  position: fixed;
  inset: 0;
  display: grid;
  place-items: center;
  overflow: hidden;
  background: #000;          /* the letterbox */
}

.deck {
  width: 1920px;
  height: 1080px;
  position: relative;
  transform-origin: center center;
  /* Scale to whichever axis binds first. Never exceed 1:1 — upscaling a
     1920px canvas past its native size only softens the type. */
  transform: scale(min(100vw / 1920, 100vh / 1080));
}

.slide {
  position: absolute;
  inset: 0;
  visibility: hidden;        /* NOT display:none — preserves geometry for transitions */
  opacity: 0;
  transition: opacity 400ms ease;
}

.slide.active {
  visibility: visible;
  opacity: 1;
}
```

**Use `min()` in CSS rather than a resize listener.** It is declarative, runs on the
compositor, and cannot fall out of sync with the actual viewport.

**Design at 1:1.** Author as though the canvas is exactly 1920×1080, because it is. Scaling
is the runtime's problem, not the author's.

**Type at presentation scale.** Body text below ~24px at 1920 wide is unreadable from the
back of a room. The fixed canvas makes this checkable: it is a number, not a judgement.

**Provide a print path.** PDF export at exactly 1920×1080 per page is trivial on a fixed
stage and fiddly on a fluid one. It falls out for free — take it.

---

## Where it breaks

**Genuine mobile reading.** If a deck is primarily consumed by scrolling on a phone, a
16:9 canvas scaled to a 390px-wide screen is illegible. That is a different artifact — a
document, or a scrollytelling page — and it should be built as one. Do not compromise the
deck to half-serve it.

**Accessibility.** A fixed stage resists browser zoom and text resizing, both of which
low-vision users depend on. This is a real cost, and this principle mostly ignores it. The
honest mitigation is to ship an accessible HTML transcript alongside the deck rather than
to pretend the deck is accessible.

**Non-16:9 venues.** Ultrawide, 4:3 legacy projectors, LED walls. Letterboxing handles them
correctly but wastes real estate. If you know the venue, author to its ratio instead.

**Very long-form content.** Some decks are really documents. Forcing 40 slides of dense
reference material into 16:9 fights the material — [corpus 02](../benchmark/corpus/02-quarterly-review.md)
in the benchmark exists partly to probe where that line sits.
