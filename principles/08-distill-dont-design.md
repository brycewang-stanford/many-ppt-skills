# 8 · Distill, don't design

**Do it by hand thirty times, *then* write the skill.**

Evidence: ★★★☆☆ — stated explicitly by the author of the most-copied skill in the category;
corroborated by the shape of the projects that worked.

---

## The principle

The natural way to build a skill is to sit down and write instructions for how the task
*should* be done. This mostly produces skills that sound right and work badly.

The approach that produced the category's reference implementation is the inverse: do the
task manually, with an agent, many times, until the output is genuinely good — then ask the
agent to write down what you just did.

---

## The evidence

Zara Zhang's account of building `frontend-slides`, which now has 26,000+ stars and defined
the category's interaction model:

> 1. Get Claude Code to create a website that looks like a slide deck
> 2. **Iterate dozens of times, until it meets my criteria for "good slides"**
> 3. Tell Claude to turn the workflow & best practices that we just went through into a skill

Three steps, and the second one carries all the weight.

Notice what is absent: no upfront design document, no feature specification, no attempt to
enumerate cases in advance. The skill is a *recording* of a process that was already
producing good output.

The evolution supports this. The "show, don't tell" preview flow ([principle 1](01-show-dont-tell.md))
is not something you would specify from first principles — it reads as strange until you
have watched people fail to answer "what style do you want?" a dozen times. It is a
discovered solution to an observed problem.

**`huashu-design`**'s Brand Asset Protocol has the same fingerprint. Its five steps — ask,
search, download, grep the colors, document the spec — are far too specific to be
theoretical. That is a procedure someone built after watching an agent hallucinate brand
colors repeatedly, with each step patching a failure they actually hit.

**Anthropic's official `pptx` skill** reads the same way. "Never share one `shadow` or
options object across two `add*` calls" is not a rule anyone writes from first principles.
It is a bug someone hit, diagnosed, and wrote down.

---

## Why it works

**Real failures are stranger than imagined ones.** Sitting down to design a skill, you
enumerate the problems you can think of. Doing the task thirty times surfaces the problems
that actually occur, which are consistently weirder and more specific: `display: none`
breaking transitions, options objects being mutated across calls, brand colors being
confidently invented.

**You cannot specify quality you have not achieved.** "Make it beautiful" is what you write
when you have not yet made something beautiful. Once you have, you can say what you actually
did — the font, the scale, the palette structure, the animation timing. Specificity requires
prior success.

**The agent already knows the process.** After thirty iterations, the transcript contains
the whole workflow. Asking the model to summarize what it just did produces something
grounded in real steps rather than in a description of steps.

**It naturally produces prohibitions.** Iterating means repeatedly saying "no, not like
that". Those corrections become the banned list from [principle 2](02-anti-ai-slop.md),
which is the part that does the most work.

---

## How to apply it

**Phase 1 — Do the task manually.** With an agent, without a skill. Push until the output is
something you would genuinely use. Not "acceptable" — *good*. If you stop at acceptable, the
skill encodes acceptable.

**Phase 2 — Keep the transcript.** The corrections are the raw material. "No, that font is
too generic" and "don't put a line under the title" are the future skill.

**Phase 3 — Notice the repeats.** By the tenth iteration you are giving the same corrections
over and over. Every repeated correction is a rule. Every rule you only gave once is
probably situational and should stay out.

**Phase 4 — Have the agent write it up.** Literally: *"Turn the workflow and best practices
we just went through into a SKILL.md."* It has the context; you do not have to reconstruct it.

**Phase 5 — Edit hard for structure.** The first draft will be a flat wall. Restructure it
per [principle 5](05-progressive-disclosure.md) — map in front, detail deferred. This is
where `frontend-slides` went from 1,625 lines to 183.

**Phase 6 — Test on something new.** Run the skill on material it was not distilled from.
Everything it gets wrong is a gap between what you did and what you wrote down. Fix, repeat.

---

## The tell

You can usually spot which approach produced a skill by reading it.

| Designed | Distilled |
|---|---|
| "Use appropriate typography" | "Never Inter, Roboto or Arial — source from Fontshare" |
| "Ensure good visual hierarchy" | "Body text ≥ 24px at 1920 wide, or it is unreadable from row 20" |
| "Handle errors gracefully" | "Run `clean.py` after deleting slides or you leave orphaned media" |
| "Follow best practices" | "Never share one options object across two `add*` calls" |

The left column is what you write before doing the work. The right column is what you write
after. Specificity is the signature of experience, and it is also what actually changes
model behavior.

---

## Where it breaks

**It does not scale to domains you do not know.** Distillation requires being able to
recognize good output. You cannot distill a skill for academic citation formatting if you
cannot tell a correct citation from an incorrect one. In an unfamiliar domain, find someone
who can judge, or do not build the skill.

**It overfits to your taste.** Thirty iterations against your own preferences produce a
skill encoding *your* preferences. That is fine for a personal skill and a real limitation
for a public one. `guizang`'s five locked presets are five good choices by one designer —
excellent if they fit you, a dead end if they do not.

**It is slow.** Thirty iterations is genuinely thirty iterations. There is no shortcut, and
this is the main reason people skip it.

**It can encode workarounds for bugs that got fixed.** A rule that patched a model behavior
from six months ago may now be unnecessary or actively harmful. Date your rules and re-test
them when models change.

**Some things really are knowable up front.** OOXML requires certain element ordering. That
is a fact you can look up, not something to discover through thirty failures. Distillation
is for judgement and workflow, not for specifications.
