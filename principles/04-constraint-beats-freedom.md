# 4 · Constraint beats freedom

**Lock the palette. Fix the layouts. Agents get more consistent, not less capable.**

Evidence: ★★★★☆ — several projects go all the way to hard locks, and the most constrained
project in the registry is also among the most starred.

---

## The principle

The intuition is that a more capable model deserves more freedom. For generated design, the
opposite holds. Given an open field, a model makes locally reasonable choices that do not
add up: eleven slides, eleven slightly different blues, three competing type scales, and a
deck that is individually fine and collectively incoherent.

Constraints do not reduce what the model can do. They reduce the number of places it can
be inconsistent.

---

## The evidence

**`guizang-ppt-skill`** (22.5k stars) is the strongest case, because it is the most
restrictive project in the registry and it did not lose for it:

- Two visual systems: Style A with 10 narrative layouts, Style B with **22 locked** grid layouts
- Theme colors are **presets only** — Style A has 5, Style B has 4, and **custom hex values
  are not permitted**
- Automated validation runs against those constraints

Forbidding custom colors sounds like a defect. It is the design. Every deck from Style B
looks like it belongs to the same publication, and that is the product.

**`likaku/Mck-ppt-design-skill`** codifies **70 fixed layout patterns**, because consulting
decks derive their authority partly from looking like every other deck from that firm.
Novelty is a bug in that context.

**Anthropic's official `pptx` skill** is a wall of prohibitions and mandated procedures:
never share an options object across `add*` calls, set layout before adding slides, hex
without `#`, duplicate slides only via `scripts/add_slide.py`, run `clean.py` after
deletion. It reads like a style guide because it is one.

**`frontend-slides`** occupies the interesting middle. It offers 12 presets plus 34
templates — wide choice — but once a direction is picked, the rules within it are firm, and
the fixed-stage constraints ([principle 3](03-fixed-stage.md)) never relax. **Choose freely,
then commit fully.**

---

## Why it works

**Consistency is most of what "designed" means.** A viewer cannot articulate a type scale,
but they feel it when the deck holds together. Coherence is largely the *absence* of
unmotivated variation, and variation is exactly what an unconstrained generator produces.

**Every free parameter is a chance to drift.** With 5 preset colors there are 5 outcomes.
With free hex there are 16 million, and the model will use several of them in one deck
without noticing.

**Constraints compress the instruction budget.** "Pick from these five" is shorter and less
ambiguous than any prose description of a good palette. That directly buys context back
(see [principle 5](05-progressive-disclosure.md)).

**Validation becomes possible.** You can mechanically check "is every color in the preset
list". You cannot mechanically check "is the palette tasteful". Constraints are what make
[principle 7](07-render-and-look.md)'s automated audit tractable.

---

## How to apply it

**Constrain the system, not the content.** Lock palette, type scale, spacing, layout
inventory. Never constrain what the user is allowed to say. The mistake is inverting this —
skills that force content into a fixed narrative arc produce decks that fight the material.

**Prefer enumerations to ranges.** Five named colors beat "a harmonious palette". Six
spacing steps beat "consistent spacing". Nine type sizes beat "a clear hierarchy".

**Lock hardest where inconsistency is most visible.** Color and type scale first — those
are what a viewer notices. Layout inventory next. Illustration style last.

**Give the escape hatch a cost.** If custom values are permitted, make them explicit and
loud — a documented override rather than a silent default. `guizang` removes the hatch
entirely; that is defensible, but so is making it deliberate.

**Validate the constraint, do not just state it.** A rule nobody checks is a suggestion.
`guizang` ships automated validation for exactly this reason.

---

## The counter-position

[`frontend-slides`](https://github.com/zarazhangrui/frontend-slides) and
[`guizang-ppt-skill`](https://github.com/op7418/guizang-ppt-skill) sit at opposite ends —
maximum design freedom versus locked systems — and both cleared 22,000 stars.

That is worth sitting with rather than resolving. They are serving different needs:

- **Freedom** wins when the deck should feel *personal* — a founder pitch, a conference
  talk, a personal brand. Distinctiveness is the point.
- **Constraint** wins when the deck should feel *institutional* — consulting output,
  recurring internal reporting, anything under brand governance. Recognizability is the point.

The real principle is not "constrain always". It is: **decide which of those you are
building, and then commit.** The failure mode is the muddled middle — enough freedom to
drift, not enough to be distinctive.

---

## Where it breaks

**Constraints encode their author's taste, permanently.** `guizang`'s five presets are
five good choices by one designer. If none of them fits your brand, the skill has no answer
and you are stuck.

**They date.** A locked 2026 palette will look like 2026 in 2029. Freedom ages more
gracefully because it re-derives from current context each time.

**Over-constraint produces sameness.** The same property that makes every Style B deck
cohere makes every Style B deck look alike. For a publication that is brand; for a
marketplace of decks it is monotony.

**Constraints can fight the content.** 22 locked layouts are 22 shapes the argument must
fit into. When the material does not fit any of them, something has to give, and it should
be the layout — but a hard lock means it will be the argument instead.
