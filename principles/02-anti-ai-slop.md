# 2 · Anti-slop is a banned list

**"Make it beautiful" does nothing. "Never use Inter" does.**

Evidence: ★★★★★ — the strongest in this collection. A community project and a model vendor
independently ban the *same oddly specific things*, in nearly the same words.

---

## The principle

A model's default output is the statistical center of its training data. For design, the
center is competent, inoffensive, and instantly recognizable as machine-made. Asking for
"beautiful" or "modern" or "professional" moves nothing, because the model already believes
its default *is* those things.

What moves output is **subtraction**. Naming specific things the model must not do removes
the default without requiring it to have taste.

---

## The evidence

This is the one place where a community consensus and a model vendor's own guidance
converge hard enough to be worth taking as fact.

### `frontend-slides` bans

| Banned | Stated reason |
|---|---|
| Inter, Roboto, Arial | A default font signals no choice was made. Use Fontshare or Google Fonts and pick something with a point of view. |
| Flat solid backgrounds | Every slide should have atmosphere — gradient, texture, pattern. |
| Evenly-distributed palettes | Called "timid". Requires a dominant tone plus a sharp accent. |
| Scattered micro-interactions | Prefers one high-impact staggered entrance reveal over many small hovers. |
| Workflow metadata on slides | No "Option A", no template names, no internal notes. |

### Anthropic's official `pptx` skill bans

| Banned | Stated reason |
|---|---|
| Accent lines under titles | *"these signal AI generation"* |
| Decorative color bars | Same |

**That convergence is the finding.** An independent developer optimizing for aesthetics and
a model vendor writing internal document guidance both landed on "decorative rule under the
title" as a tell. Neither was copying the other. It is a genuine fingerprint of generated
design — the visual equivalent of "delve".

### Others

`nghiahsgs/skills-slides` puts "Anti-AI-slop" directly in its repository description.
`Akxan/ppt-agent-skill` takes the positive-space approach instead, benchmarking explicitly
against Linear, Anthropic, Stripe, Apple and NYT — naming the target rather than the
forbidden, which is the same move from the other direction.

---

## Why it works

**Prohibitions are checkable; aspirations are not.** A model can verify "did I use Inter?"
It cannot verify "is this beautiful?" — and when it tries, it grades its own default
generously.

**The failure mode is convergence, not incompetence.** Models are not bad at design. They
are *average* at design, reliably, every time. The problem is not the ceiling but the
attractor. Banned lists work because they make the attractor unreachable, forcing a choice.

**Specificity carries information; adjectives do not.** "Distinctive typography" is a word
the model will happily believe it satisfied. "Not Inter, not Roboto, not Arial, source from
Fontshare" leaves nowhere to hide.

---

## How to apply it

**Write prohibitions, not aspirations.** Every rule should be mechanically checkable. If
you cannot write a grep or a test for it, rewrite it until you can.

**Ban the defaults specifically, by name.** Not "avoid generic fonts" — list them.

**Give a replacement whenever you ban something.** "Not Inter" without "source from
Fontshare" produces a model that reaches for Helvetica. Close the door and open a window.

**Prohibit ornament that carries no information.** Underlines beneath titles, color bars,
one-icon-per-bullet, drop shadows on everything. If removing it loses no meaning, it was
decoration, and decoration is where slop accumulates.

**Ban the leaks.** Internal workflow language — option labels, template names, "here is
your deck" — must never render. This is a correctness rule that happens to also be an
aesthetic one.

**Encode it as a checklist the model self-audits against** before declaring done. Pair it
with [principle 7](07-render-and-look.md) so the audit happens against a rendered image
rather than against source.

---

## A note on font bans

`frontend-slides` bans Inter outright. That is a good rule for a skill and a bad rule as
a universal law. Inter set with genuine care — real hierarchy, considered measure, tabular
figures — beats a distinctive face set carelessly every time.

The ban is a *proxy*. What it is really targeting is "reached for the default and stopped
thinking". [The benchmark rubric](../benchmark/rubric.md) reflects this: it does not
disqualify default fonts, but reaching for one *and* not compensating anywhere else scores
a 2.

Know which of your rules are the actual goal and which are proxies for it. Proxies should
be enforced strictly in a skill and held loosely in a review.

---

## Where it breaks

**Prohibitions do not create vision.** A deck that avoids every banned pattern can still be
dull. Banned lists remove the floor; they do not build a ceiling. Pair with strong positive
direction — templates, named references, or [principle 4](04-constraint-beats-freedom.md).

**The list ages.** These are fingerprints of *current* model defaults. As models change,
some entries become obsolete and new tells appear. Date your list, and re-derive it when
you notice output drifting.

**Over-banning produces incoherence.** Ban enough and the model starts making arbitrary
choices to satisfy constraints rather than coherent ones. A deck that avoids everything can
end up looking like it is avoiding everything.

**Context can invalidate a ban.** A corporate template may *mandate* the accent rule under
the title. Brand compliance outranks the anti-slop list, and your skill should say which
wins.
