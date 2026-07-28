# 6 · Single file outlasts frameworks

**Dependencies are debt. Inline everything.**

Evidence: ★★★★☆ — the default across the HTML route, with one prominent and instructive
exception.

---

## The principle

A generated deck should be one `.html` file with every stylesheet, script, font and image
inlined. No build step, no `npm install`, no CDN, no server. Double-click and it opens.

The framing from `frontend-slides`:

> "Dependencies represent technical debt; **single HTML files outlast frameworks**."

---

## The evidence

Nearly every HTML-route project in [the registry](../README.md) ships self-contained
output. `frontend-slides`, `guizang-ppt-skill`, `next-slide` and `skills-slides` all state
"zero dependencies" as a headline property rather than an implementation detail.

`frontend-slides` requires `viewport-base.css` to be **inlined verbatim** into every
generated deck rather than linked — the scaling behavior must survive the file being moved,
emailed, or opened offline five years later.

### The exception worth studying

[`open-slide`](https://github.com/1weiho/open-slide) (6k stars) goes the other way: an npm
package, a React runtime, a build step. In exchange it gets things single files cannot
have — hot reload, presenter mode with notes and timers, an asset manager, and a
browser inspector where you click an element, type a comment, and the agent applies it.

That is a real trade, honestly made. It buys collaboration affordances and pays in
portability. Which is right depends on whether your deck is **an artifact** (make it, send
it, done — single file) or **a living project** (a team edits it over months — framework).

Most decks are artifacts. That is why single-file is the default.

---

## Why it works

**Presentations are performed live, with no undo.** A CDN that is slow, blocked by
conference wifi, or simply gone is a failure in front of an audience. Every external
request is a chance to fail at the worst possible moment. Zero requests, zero chances.

**Ten-year durability.** An inlined HTML file opens in 2036. An npm project from 2026 will
not `npm install` in 2029 — a transitive dependency will have been unpublished, a
peer-dependency range will have gone incompatible, or the Node version will have moved on.
This is not hypothetical; it is the observed lifecycle of every JS project.

**Sharing becomes trivial.** Email it. Drop it in Slack. Put it on a USB stick. Every
alternative — "clone this and run npm install" — is friction that ends with someone asking
for a PDF.

**Agents are good at generating one big file and bad at managing dependency trees.** A
model writing self-contained HTML is working in its strongest mode: no version resolution,
no lockfile, no install step to get wrong. This is an underrated reason the pattern won.

---

## How to apply it

**Inline everything, in this order of importance:**

| Asset | How |
|---|---|
| CSS | `<style>` in `<head>` |
| JS | `<script>` at end of `<body>` |
| Images | `data:` URIs, base64 |
| Fonts | `data:` URI in `@font-face`, subset to the glyphs actually used |
| Icons | Inline `<svg>`, never an icon font or sprite sheet |

**Subset fonts aggressively.** A full weight of a variable font is 200 KB+; subset to used
glyphs and it is often under 20 KB. For CJK decks this matters enormously — an unsubsetted
CJK font can exceed 10 MB, which is the one case where inlining can genuinely be wrong.

**Verify, do not assume.** A remote reference is easy to leave in by accident:

```bash
# Any hit here is an external dependency the deck will need at runtime.
grep -oE '(src|href)="https?://[^"]+"' deck.html
grep -oE 'url\(https?://[^)]+\)' deck.html
grep -c 'fonts.googleapis.com' deck.html      # a very common leak
```

[The benchmark rubric](../benchmark/rubric.md) scores this directly: a deck with external
runtime dependencies caps at 3 on deliverable integrity, no matter how it looks.

**Watch the size ceiling.** Past roughly 15 MB, browsers get sluggish parsing one file.
Compress images, subset fonts, and if you are still over, that is a signal the deck has too
many raster assets rather than a signal to start linking.

**Ship a PDF path anyway.** Some recipients want a PDF regardless of how portable the HTML
is. Playwright at 1920×1080 handles it, and [principle 3](03-fixed-stage.md) makes it
trivial.

---

## Where it breaks

**Heavy media.** A deck with video cannot inline it sensibly. Link it, and accept that the
deck now has a network dependency — or drop the video.

**CJK typography.** Full CJK font files are megabytes. Subsetting works but requires
knowing the glyph set in advance, which is fragile if the deck is later edited. This is the
strongest legitimate case for a linked font.

**Genuinely collaborative decks.** If five people edit a deck over three months, one giant
HTML file is a terrible diff surface and a merge nightmare. That is `open-slide`'s case,
and it is correct there.

**Interactive data.** A deck that queries a live API is not an artifact. It is an
application, and the single-file constraint stops making sense.

**Very large decks.** 100+ slides with rich imagery will exceed what one file should hold.
Split by section, or reconsider whether it should be a deck.
