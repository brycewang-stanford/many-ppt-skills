<div align="center">

# many-ppt-skills

**Every AI slide-deck skill worth knowing, gathered and compared on one page — so you can pick the right one and get on with it.**

[简体中文](README.md) · [English](README.en.md)

<!-- BEGIN:COUNTS -->
**26 skills tracked** · **143,031 combined stars** · 13 HTML-native · 7 native PPTX · 4 both · data refreshed **2026-07-28**
<!-- END:COUNTS -->

</div>

---

Coding agents got good at CSS, and in six months a whole category appeared: skills that
turn a document into a deck that does not look machine-made. There are now 30+ serious
projects and four of them have over 20,000 stars each.

Every ranking of them is a re-sort of those star counts. Stars measure how well an author
tweets. They do not tell you which one handles your code blocks, or whether the CFO will
be able to edit slide 12.

This repo exists to answer that in one page:

1. **Everything gathered** — every skill worth knowing, both routes, with live stats.
   Regenerated from [`data/skills.json`](data/skills.json), so the numbers cannot quietly
   rot.
2. **Compared on what actually decides it** — the [route question](#start-here-which-route-are-you-on)
   first, then what each one is genuinely for. Facts you can check, not scores I made up.
3. **[Eight principles](principles/)** distilled from reading these projects' source — the
   patterns 30 teams converged on independently, which is the closest thing this field has
   to evidence.

Pick one, install it, move on. That is the whole intent.

---

## Let an agent pick for you

This repository is also a skill. Install it and you do not have to read this page:
say "I need a deck for investors" and it asks the route question first, then names a
skill, its install command, and the style ids you can ask for.

```bash
# as a Claude Code plugin
/plugin marketplace add https://github.com/brycewang-stanford/many-ppt-skills
/plugin install many-ppt-skills@many-ppt-skills

# or clone it as a personal skill
git clone https://github.com/brycewang-stanford/many-ppt-skills ~/.claude/skills/many-ppt-skills
```

Underneath is a query CLI you can use directly:

```bash
python scripts/pick.py route                  # the route question, plus counts
python scripts/pick.py list --route pptx      # skills on one route
python scripts/pick.py show ppt-master        # install command, style ids, capabilities
python scripts/pick.py styles frontend-slides # every style id with its sample image
python scripts/pick.py find editorial         # search style ids and descriptions
```

**It chooses, it does not generate** — and it will not invent another project's
invocation syntax; that project's own `SKILL.md` is the authority. See
[`SKILL.md`](SKILL.md).

---

## Start here: which route are you on?

This is the only decision that really matters, and it is not about aesthetics.

> **Will anyone need to open your deliverable in PowerPoint and edit it?**

| | **HTML-native** | **Native PPTX** |
|---|---|---|
| **Output** | One `.html` file, presented in a browser | A real `.pptx` |
| **Design ceiling** | ★★★★★ anything Chrome renders | ★★★☆☆ bounded by OOXML |
| **Motion** | ★★★★★ CSS, WebGL | ★★☆☆☆ native transitions |
| **Handoff** | Recipient cannot edit in Office | Recipient edits normally |
| **Version control** | ★★★★★ plain text diffs | ★☆☆☆☆ binary |
| **Fits corporate template** | ✗ | ✓ |
| **Start with** | [Frontend Slides](https://github.com/zarazhangrui/frontend-slides) | [PPT Master](https://github.com/hugohe3/ppt-master) |

**No → HTML route.** Higher ceiling, and it is not close. Zero-dependency single files
still open in ten years.
**Yes → PPTX route.** Nothing else matters if the CFO cannot edit slide 12.

These are not old versus new. They are different jobs.

<details>
<summary><b>Full decision tree</b></summary>

```
Must the recipient edit it in PowerPoint?
├─ YES ──▶ Native PPTX
│   ├─ Best visuals + genuinely native objects ····· ppt-master
│   ├─ Mandated corporate template, strict ········· pptx-from-layouts-skill
│   ├─ Programmatic surgery on existing decks ······ Anthropic pptx (official)
│   ├─ Consulting / board / investment memo ········ Mck-ppt-design-skill
│   └─ Conference talk, thesis, grant ·············· academic-pptx-skill
│
└─ NO ───▶ HTML-native
    ├─ Don't know what style you want ·············· frontend-slides
    ├─ Editorial consistency, CN-first (AGPL!) ····· guizang-ppt-skill
    ├─ Also need prototypes / motion / infographics · huashu-design
    ├─ Team, recurring decks, presenter mode ······· open-slide
    ├─ Diagrams, diff reviews, project recaps ······ visual-explainer
    ├─ Teaching / training, retention matters ······ visual-cognition-slides
    └─ Want HTML *and* editable PPTX ··············· huashu-design · frontend-slides-editable
```

</details>

### If you install exactly one

[**Frontend Slides**](https://github.com/zarazhangrui/frontend-slides) by
[Zara Zhang](https://github.com/zarazhangrui). It defined the category's interaction model
— it does not ask what style you want, it generates three real previews of *your* deck and
lets you point. Largest community, so problems are searchable.

Add [**PPT Master**](https://github.com/hugohe3/ppt-master) as the second and you cover
essentially every scenario.

---

## The registry

<!-- BEGIN:REGISTRY -->
### Tier S — Battle-tested (5k+ stars)

| Skill | ⭐ | Route | License | What it is |
|---|---:|---|---|---|
| **[PPT Master](https://github.com/hugohe3/ppt-master)**<br><sub>hugohe3</sub> | 41,516 | PPTX | MIT | Documents or topics into genuinely native, editable PowerPoint decks. |
| **[Frontend Slides](https://github.com/zarazhangrui/frontend-slides)**<br><sub>Zara Zhang</sub> | 26,461 | HTML | MIT | Beautiful slides on the web using a coding agent's frontend skills. |
| **[Guizang PPT Skill](https://github.com/op7418/guizang-ppt-skill)**<br><sub>op7418 (歸藏)</sub> | 22,564 | HTML | ⚠️ AGPL-3.0 | Editorial-magazine and Swiss-International HTML decks, with design locked down by constraint. |
| **[Huashu Design](https://github.com/alchaincyf/huashu-design)**<br><sub>花生 (alchaincyf)</sub> | 22,135 | Both | MIT | HTML-native design skill — prototypes, decks, motion and design critique, not just slides. |
| **[Visual Explainer](https://github.com/nicobailon/visual-explainer)**<br><sub>nicobailon</sub> | 9,346 | HTML | MIT | Rich HTML pages or decks for diagrams, diff reviews, plan audits, data tables and project recaps. |
| **[HTML PPT Studio](https://github.com/lewislulu/html-ppt-skill)**<br><sub>lewislulu</sub> | 7,437 | HTML | MIT | 24 themes, 31 layouts and 20+ animations for professional HTML presentations. |
| **[open-slide](https://github.com/1weiho/open-slide)**<br><sub>1weiho</sub> | 6,027 | Framework | MIT | A slide framework built for agents — React components on a fixed 1920x1080 canvas. |
| **[Anthropic PPTX (official)](https://github.com/anthropics/skills/tree/main/skills/pptx)**<br><sub>Anthropic</sub> | 164,681* | PPTX | See repo | The official baseline — create, read, edit and combine PowerPoint files. |

### Tier A — Production-ready (100–5k stars)

| Skill | ⭐ | Route | License | What it is |
|---|---:|---|---|---|
| **[Beautiful HTML Templates](https://github.com/zarazhangrui/beautiful-html-templates)**<br><sub>Zara Zhang</sub> | 3,918 | Templates | MIT | 34 HTML slide templates with index.json metadata so any agent can pick the right one. |
| **[Claude Office Skills](https://github.com/tfriedel/claude-office-skills)**<br><sub>tfriedel</sub> | 798 | PPTX | Unspecified | PPTX, DOCX, XLSX and PDF workflows with automation support. |
| **[Academic PPTX](https://github.com/Gabberflast/academic-pptx-skill)**<br><sub>Gabberflast</sub> | 722 | PPTX | MIT | Conference talks, seminar slides, thesis defenses and grant briefings. |
| **[PPT Agent Workflow San](https://github.com/mucsbr/ppt-agent-workflow-san)**<br><sub>mucsbr</sub> | 617 | HTML | Unspecified | Progressive, interactive deck generation. |
| **[Frontend Slides Editable](https://github.com/archlizheng/frontend-slides-editable)**<br><sub>archlizheng</sub> | 445 | Both | MIT | Editable HTML decks with drag-resize, reordering, local save and PPTX conversion. |
| **[PPT SVG Generator](https://github.com/vigorX777/ppt-svg-generator)**<br><sub>vigorX777</sub> | 248 | PPTX | MIT | Markdown to PPT or PDF via SVG, with preset styles. |
| **[Mck PPT Design System](https://github.com/likaku/Mck-ppt-design-skill)**<br><sub>likaku</sub> | 229 | PPTX | Apache-2.0 | Consulting-firm-style design system: 70 layout patterns, flat design, python-pptx. |
| **[PPT Agent Skill](https://github.com/Akxan/ppt-agent-skill)**<br><sub>Akxan</sub> | 114 | HTML | MIT | 26 styles and 18 chart types benchmarked against Linear, Anthropic, Stripe, Apple and NYT. |

### Tier B — Specialized & emerging (<100 stars)

| Skill | ⭐ | Route | License | What it is |
|---|---:|---|---|---|
| **[Visual Cognition Slides](https://github.com/edu-ai-builders/visual-cognition-slides)**<br><sub>edu-ai-builders</sub> | 81 | HTML | MIT | Slide design grounded in cognitive science and instructional design, optimized for retention. |
| **[HTML Slides](https://github.com/bluedusk/html-slides)**<br><sub>bluedusk</sub> | 70 | HTML | MIT | HTML slides with speaker notes, plus a companion presentation app. |
| **[KingDee PPT Skill](https://github.com/WayneZhon/KingDee-PPT-Skill)**<br><sub>WayneZhon</sub> | 56 | HTML | MIT | KingDee corporate style decks. |
| **[Huawei Style PPT Skill](https://github.com/zuiho-kai/huawei-style-ppt-skill)**<br><sub>zuiho-kai</sub> | 52 | HTML | Custom | High-information-density decks in the Huawei corporate idiom. |
| **[Slide Creator](https://github.com/kaisersong/slide-creator)**<br><sub>kaisersong</sub> | 46 | Both | Unspecified | AI planning, style discovery and PPTX export. |
| **[next-slide](https://github.com/codesstar/next-slide)**<br><sub>codesstar</sub> | 43 | HTML | MIT | 26+ styles, zero dependencies, bilingual. |
| **[Slide Writer](https://github.com/FeeiCN/slide-writer)**<br><sub>FeeiCN</sub> | 40 | HTML | MIT | Enterprise HTML decks from ideas, outlines, documents or speech drafts. |
| **[Skills Slides](https://github.com/nghiahsgs/skills-slides)**<br><sub>nghiahsgs</sub> | 30 | HTML | Unspecified | 50 aesthetics x 20 palettes x 10 fonts x 5 layouts x 30+ effects. |
| **[PowerPoint Fancy Design](https://github.com/Phlegonlabs/Powerpoint-fancy-design)**<br><sub>Phlegonlabs</sub> | 27 | Both | Unspecified | Page-structured Markdown into styled 1600x900 HTML slides, PNG renders and exports. |
| **[PPTX from Layouts](https://github.com/tristan-mcinnis/pptx-from-layouts-skill)**<br><sub>tristan-mcinnis</sub> | 9 | PPTX | MIT | Generate decks from markdown strictly through a template's slide master layouts. |

### Other curated lists

| Skill | ⭐ | Route | License | What it is |
|---|---:|---|---|---|
| **[awesome-html-slide-skills](https://github.com/ToseaAI/awesome-html-slide-skills)**<br><sub>ToseaAI</sub> | 104 | List | Custom | Curated list of HTML slide skills and template libraries. A primary lead source for this registry. |
| **[Awesome-PPT-Design-Skills](https://github.com/software-ai-life/Awesome-PPT-Design-Skills)**<br><sub>software-ai-life</sub> | 71 | List | Unspecified | Agent-agnostic PPT design skills for high-end editable presentation styles. |

<sub>`*` monorepo star count — reflects the whole repo, not this one skill. `~` stale value, last refresh failed. `⚠️` copyleft license, check before commercial use.</sub>
<!-- END:REGISTRY -->
---

## What each one actually does

The registry above says what each project *is*. This says what its documentation
*claims it does* — the columns that usually decide the choice.

<!-- BEGIN:CAPABILITIES -->
| Skill | → PPTX | → PDF | Data charts | Code blocks | Diagrams | Motion | Speaker notes | Presenter mode | Your template | Offline |
|---|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| **Anthropic PPTX (official)** | ✅ | ✅ | ✅ | · | · | · | ✅ | · | ✅ | n/a |
| **PPT Master** | ✅ | · | ✅ | · | ✅ | ✅ | ✅ | · | ✅ | n/a |
| **Frontend Slides** | · | ✅ | · | · | · | ✅ | · | · | · | · |
| **Guizang PPT Skill** | — | · | · | · | ✅ | ✅ | · | · | — | · |
| **Huashu Design** | ✅ | ✅ | · | · | · | ✅ | ✅ | · | · | · |
| **Visual Explainer** | · | · | · | · | ✅ | ✅ | · | · | · | ✅ |
| **HTML PPT Studio** | · | · | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | · | — |
| **open-slide** | · | · | · | · | · | · | · | · | · | · |
| **Beautiful HTML Templates** | · | · | · | · | · | · | · | · | · | — |
| **Claude Office Skills** | ✅ | · | · | · | · | · | ✅ | · | ✅ | n/a |

<sub>✅ the docs claim it · — the docs say it does not · · the docs are silent, which is not the same as no · n/a the question does not apply to that route. Read from each project's own SKILL.md and README, never from running it; every ✅ carries the sentence it came from in [`data/capabilities.json`](data/capabilities.json).</sub>
<!-- END:CAPABILITIES -->

Read the middle column carefully: `·` means the docs never address it, which is not the
same as "no". Several of these projects do more than they write down. Where a capability
matters to you, the quote in [`data/capabilities.json`](data/capabilities.json) tells you
exactly which sentence to go and check.


---

## What they look like

The two tables above say what each project *is* and what it *claims*. Neither answers
the question you actually walked in with, which is whether you like what comes out. So
here is every picture these projects publish of their own work.

**Everything is shown full size, not as thumbnails.** A slide is a dense object; shrunk
into a contact sheet it tells you the palette and nothing else — not the type, not the
hierarchy, not the whitespace, which are the things you are choosing between. That makes
for a long page, so there is a jump index below.

The names are **read from each project's own filenames and captions**, never invented
here. Every image cites the file it came from and links back to it, so a wrong label is
one click from being caught.

Read them for what they are: **each frame is the one that team chose**. A wall of
marketing shots is not a like-for-like comparison — no two of these decks are even on
the same content. The use is elsewhere. It eliminates half the registry in thirty
seconds, which is the decision most people came here to make.

### You like one of these. Now what?

**1. Take the two things under the image.** Every caption reads like this:

> **Soft Editorial · 4** · `soft-editorial` · [`screenshots/soft-editorial-4.png`](https://github.com/zarazhangrui/beautiful-html-templates)

Bold is the readable name. The `monospace` one is the **style ID** — that is the string
you are going to name. Last is the source file, which you can open and check.

**2. Install the skill it belongs to.** The command sits under that skill's heading in
this section, ready to copy. But **the five install methods do different things**, and
installing into the wrong place is the usual reason nothing happens:

<!-- BEGIN:INSTALLMETHODS -->
| Install method | What it actually does | Skills |
|---|---|---:|
| `clone` | Clones into `~/.claude/skills/`, where Claude Code looks for personal skills. Restart the session and it is available. | 20 |
| `plugin` | Two commands typed **inside Claude Code**, not in a terminal. Adds the marketplace, then installs from it. | 2 |
| `skills-cli` | Agent-agnostic installer. Works outside Claude Code too. | 2 |
| `python` | Needs Python on your machine. Clone it, install the dependencies, then point your agent at the cloned directory. | 1 |
| `npx` | Scaffolds a project rather than installing a skill — you get a working directory to build in. | 1 |
<!-- END:INSTALLMETHODS -->

**3. Talk to your agent in plain language, and name the style ID.** It is not a
command-line flag; it is part of what you ask for:

```text
Use the soft-editorial template. Turn docs/roadmap.md into a 12-slide deck
for investors. I'll be speaking over it, so keep the text light.
```

**4. Know what naming it skips.** Some skills show you options first — frontend-slides'
SKILL.md says it generates 3 previews by default (one safe preset, one bold template,
one wildcard). **Naming a template ID skips that**: it reads that template's `design.md`
and builds from it. Want the options instead? Don't name one — just ask for a deck.

> **Two honest notes.** Install commands come from the hand-maintained
> [`data/skills.json`](data/skills.json); style IDs come from the projects' own files — I
> checked that `soft-editorial` and its neighbours really are slugs in frontend-slides'
> bundled `bold-template-pack/selection-index.json` (34 of them). But **this registry has
> not run all 26 skills**, so each project's own SKILL.md is the authority on its trigger
> phrases and arguments. Step 4's description of previews was read out of
> frontend-slides' SKILL.md and holds for that skill only.

<!-- BEGIN:GALLERY -->
**Jump to:** [PPT Master](#gallery-ppt-master) <sub>24</sub> · [Frontend Slides](#gallery-frontend-slides) <sub>24</sub> · [Guizang PPT Skill](#gallery-guizang-ppt-skill) <sub>13</sub> · [Huashu Design](#gallery-huashu-design) <sub>24</sub> · [HTML PPT Studio](#gallery-html-ppt-skill) <sub>24</sub> · [open-slide](#gallery-open-slide) <sub>16</sub> · [Beautiful HTML Templates](#gallery-beautiful-html-templates) <sub>24</sub> · [PPT Agent Workflow San](#gallery-ppt-agent-workflow-san) <sub>10</sub> · [Frontend Slides Editable](#gallery-frontend-slides-editable) <sub>24</sub> · [PPT SVG Generator](#gallery-ppt-svg-generator) <sub>2</sub> · [Mck PPT Design System](#gallery-mck-ppt-design-skill) <sub>6</sub> · [PPT Agent Skill](#gallery-ppt-agent-skill) <sub>24</sub> · [HTML Slides](#gallery-html-slides-bluedusk) <sub>4</sub> · [KingDee PPT Skill](#gallery-kingdee-ppt-skill) <sub>1</sub> · [Slide Creator](#gallery-slide-creator) <sub>23</sub> · [next-slide](#gallery-next-slide) <sub>1</sub> · [Slide Writer](#gallery-slide-writer) <sub>5</sub> · [Skills Slides](#gallery-skills-slides) <sub>4</sub> · [PowerPoint Fancy Design](#gallery-powerpoint-fancy-design) <sub>24</sub> · [PPTX from Layouts](#gallery-pptx-from-layouts) <sub>1</sub>

<a id="gallery-ppt-master"></a>

#### [PPT Master](https://github.com/hugohe3/ppt-master) · 41,516 ⭐ · PPTX

<sub>Documents or topics into genuinely native, editable PowerPoint decks.</sub>

<sub>24 of 46 images in [`hugohe3/ppt-master`](https://github.com/hugohe3/ppt-master) · the leading frames are the ones the project puts in its own README</sub>

```bash
git clone https://github.com/hugohe3/ppt-master && pip install -r requirements.txt
```

<sub><b>Styles below</b> `global-ai-capital` · `swiss-grid` · `glassmorphism-demo` · `sugar-rush-memphis` · `indie-bookstore-zine` · `pritzker-2026` · `academic-medical` · `dark-art-mv` · `launch-xiaomi` · `magazine-garden` · `nature-wildlife` · `tech-claude-plans` — name one when you ask for a deck. These are the project's own strings, taken from the filenames and captions linked under each image, not names this registry made up.</sub>

<img src="https://raw.githubusercontent.com/hugohe3/ppt-master/7ae3721c856fedb921d6acec52c7de69181f5194/docs/assets/screenshots/preview_global_ai_capital.png" width="100%" alt="Data journalism — Global AI Capital 2026">

<sub><b>Data journalism — Global AI Capital 2026</b> · <a href="https://github.com/hugohe3/ppt-master/blob/7ae3721c856fedb921d6acec52c7de69181f5194/docs/assets/screenshots/preview_global_ai_capital.png"><code>docs/assets/screenshots/preview_global_ai_capital.png</code></a></sub>

<img src="https://raw.githubusercontent.com/hugohe3/ppt-master/7ae3721c856fedb921d6acec52c7de69181f5194/docs/assets/screenshots/preview_swiss_grid.png" width="100%" alt="Swiss typographic grid — Grid Systems primer">

<sub><b>Swiss typographic grid — Grid Systems primer</b> · <code>swiss-grid</code> · <a href="https://github.com/hugohe3/ppt-master/blob/7ae3721c856fedb921d6acec52c7de69181f5194/docs/assets/screenshots/preview_swiss_grid.png"><code>docs/assets/screenshots/preview_swiss_grid.png</code></a></sub>

<img src="https://raw.githubusercontent.com/hugohe3/ppt-master/7ae3721c856fedb921d6acec52c7de69181f5194/docs/assets/screenshots/preview_glassmorphism_demo.png" width="100%" alt="Glassmorphism SaaS — AI Agent engineering demo">

<sub><b>Glassmorphism SaaS — AI Agent engineering demo</b> · <code>glassmorphism-demo</code> · <a href="https://github.com/hugohe3/ppt-master/blob/7ae3721c856fedb921d6acec52c7de69181f5194/docs/assets/screenshots/preview_glassmorphism_demo.png"><code>docs/assets/screenshots/preview_glassmorphism_demo.png</code></a></sub>

<img src="https://raw.githubusercontent.com/hugohe3/ppt-master/7ae3721c856fedb921d6acec52c7de69181f5194/docs/assets/screenshots/preview_sugar_rush_memphis.png" width="100%" alt="Memphis pop — Sugar Rush festival">

<sub><b>Memphis pop — Sugar Rush festival</b> · <code>sugar-rush-memphis</code> · <a href="https://github.com/hugohe3/ppt-master/blob/7ae3721c856fedb921d6acec52c7de69181f5194/docs/assets/screenshots/preview_sugar_rush_memphis.png"><code>docs/assets/screenshots/preview_sugar_rush_memphis.png</code></a></sub>

<img src="https://raw.githubusercontent.com/hugohe3/ppt-master/7ae3721c856fedb921d6acec52c7de69181f5194/docs/assets/screenshots/preview_indie_bookstore_zine.png" width="100%" alt="Risograph zine — Indie bookstore guide">

<sub><b>Risograph zine — Indie bookstore guide</b> · <code>indie-bookstore-zine</code> · <a href="https://github.com/hugohe3/ppt-master/blob/7ae3721c856fedb921d6acec52c7de69181f5194/docs/assets/screenshots/preview_indie_bookstore_zine.png"><code>docs/assets/screenshots/preview_indie_bookstore_zine.png</code></a></sub>

<img src="https://raw.githubusercontent.com/hugohe3/ppt-master/7ae3721c856fedb921d6acec52c7de69181f5194/docs/assets/screenshots/preview_pritzker_2026.png" width="100%" alt="杂志风 — 普利兹克奖 2026">

<sub><b>杂志风 — 普利兹克奖 2026</b> · <code>pritzker-2026</code> · <a href="https://github.com/hugohe3/ppt-master/blob/7ae3721c856fedb921d6acec52c7de69181f5194/docs/assets/screenshots/preview_pritzker_2026.png"><code>docs/assets/screenshots/preview_pritzker_2026.png</code></a></sub>

<img src="https://raw.githubusercontent.com/hugohe3/ppt-master/7ae3721c856fedb921d6acec52c7de69181f5194/docs/assets/screenshots/archive/preview_academic_medical.png" width="100%" alt="PPT Master sample">

<sub><b>Academic Medical</b> · <a href="https://github.com/hugohe3/ppt-master/blob/7ae3721c856fedb921d6acec52c7de69181f5194/docs/assets/screenshots/archive/preview_academic_medical.png"><code>docs/assets/screenshots/archive/preview_academic_medical.png</code></a></sub>

<img src="https://raw.githubusercontent.com/hugohe3/ppt-master/7ae3721c856fedb921d6acec52c7de69181f5194/docs/assets/screenshots/archive/preview_dark_art_mv.png" width="100%" alt="PPT Master sample">

<sub><b>Dark Art Mv</b> · <a href="https://github.com/hugohe3/ppt-master/blob/7ae3721c856fedb921d6acec52c7de69181f5194/docs/assets/screenshots/archive/preview_dark_art_mv.png"><code>docs/assets/screenshots/archive/preview_dark_art_mv.png</code></a></sub>

<img src="https://raw.githubusercontent.com/hugohe3/ppt-master/7ae3721c856fedb921d6acec52c7de69181f5194/docs/assets/screenshots/archive/preview_launch_xiaomi.png" width="100%" alt="PPT Master sample">

<sub><b>Launch Xiaomi</b> · <a href="https://github.com/hugohe3/ppt-master/blob/7ae3721c856fedb921d6acec52c7de69181f5194/docs/assets/screenshots/archive/preview_launch_xiaomi.png"><code>docs/assets/screenshots/archive/preview_launch_xiaomi.png</code></a></sub>

<img src="https://raw.githubusercontent.com/hugohe3/ppt-master/7ae3721c856fedb921d6acec52c7de69181f5194/docs/assets/screenshots/archive/preview_magazine_garden.png" width="100%" alt="PPT Master sample">

<sub><b>Magazine Garden</b> · <a href="https://github.com/hugohe3/ppt-master/blob/7ae3721c856fedb921d6acec52c7de69181f5194/docs/assets/screenshots/archive/preview_magazine_garden.png"><code>docs/assets/screenshots/archive/preview_magazine_garden.png</code></a></sub>

<img src="https://raw.githubusercontent.com/hugohe3/ppt-master/7ae3721c856fedb921d6acec52c7de69181f5194/docs/assets/screenshots/archive/preview_nature_wildlife.png" width="100%" alt="PPT Master sample">

<sub><b>Nature Wildlife</b> · <a href="https://github.com/hugohe3/ppt-master/blob/7ae3721c856fedb921d6acec52c7de69181f5194/docs/assets/screenshots/archive/preview_nature_wildlife.png"><code>docs/assets/screenshots/archive/preview_nature_wildlife.png</code></a></sub>

<img src="https://raw.githubusercontent.com/hugohe3/ppt-master/7ae3721c856fedb921d6acec52c7de69181f5194/docs/assets/screenshots/archive/preview_tech_claude_plans.png" width="100%" alt="PPT Master sample">

<sub><b>Tech Claude Plans</b> · <a href="https://github.com/hugohe3/ppt-master/blob/7ae3721c856fedb921d6acec52c7de69181f5194/docs/assets/screenshots/archive/preview_tech_claude_plans.png"><code>docs/assets/screenshots/archive/preview_tech_claude_plans.png</code></a></sub>

<img src="https://raw.githubusercontent.com/hugohe3/ppt-master/7ae3721c856fedb921d6acec52c7de69181f5194/examples/ppt169_home_design_trends_2026/images/retro_style.png" width="100%" alt="PPT Master sample">

<sub><b>Retro Style</b> · <a href="https://github.com/hugohe3/ppt-master/blob/7ae3721c856fedb921d6acec52c7de69181f5194/examples/ppt169_home_design_trends_2026/images/retro_style.png"><code>examples/ppt169_home_design_trends_2026/images/retro_style.png</code></a></sub>

<img src="https://raw.githubusercontent.com/hugohe3/ppt-master/7ae3721c856fedb921d6acec52c7de69181f5194/examples/ppt169_home_design_trends_2026/images/cream_style.png" width="100%" alt="PPT Master sample">

<sub><b>Cream Style</b> · <a href="https://github.com/hugohe3/ppt-master/blob/7ae3721c856fedb921d6acec52c7de69181f5194/examples/ppt169_home_design_trends_2026/images/cream_style.png"><code>examples/ppt169_home_design_trends_2026/images/cream_style.png</code></a></sub>

<img src="https://raw.githubusercontent.com/hugohe3/ppt-master/7ae3721c856fedb921d6acec52c7de69181f5194/examples/ppt169_home_design_trends_2026/images/bohemian_style.png" width="100%" alt="PPT Master sample">

<sub><b>Bohemian Style</b> · <a href="https://github.com/hugohe3/ppt-master/blob/7ae3721c856fedb921d6acec52c7de69181f5194/examples/ppt169_home_design_trends_2026/images/bohemian_style.png"><code>examples/ppt169_home_design_trends_2026/images/bohemian_style.png</code></a></sub>

<img src="https://raw.githubusercontent.com/hugohe3/ppt-master/7ae3721c856fedb921d6acec52c7de69181f5194/docs/assets/hero-liziqi-colors.gif" width="100%" alt="PPT Master sample">

<sub><b>Liziqi Colors</b> · <a href="https://github.com/hugohe3/ppt-master/blob/7ae3721c856fedb921d6acec52c7de69181f5194/docs/assets/hero-liziqi-colors.gif"><code>docs/assets/hero-liziqi-colors.gif</code></a></sub>

<img src="https://raw.githubusercontent.com/hugohe3/ppt-master/7ae3721c856fedb921d6acec52c7de69181f5194/skills/ppt-master/references/ai-image-comparison/rendering/3d-isometric.png" width="100%" alt="PPT Master sample">

<sub><b>3d Isometric</b> · <a href="https://github.com/hugohe3/ppt-master/blob/7ae3721c856fedb921d6acec52c7de69181f5194/skills/ppt-master/references/ai-image-comparison/rendering/3d-isometric.png"><code>skills/ppt-master/references/ai-image-comparison/rendering/3d-isometric.png</code></a></sub>

<img src="https://raw.githubusercontent.com/hugohe3/ppt-master/7ae3721c856fedb921d6acec52c7de69181f5194/skills/ppt-master/references/ai-image-comparison/rendering/blueprint.png" width="100%" alt="PPT Master sample">

<sub><b>Blueprint</b> · <a href="https://github.com/hugohe3/ppt-master/blob/7ae3721c856fedb921d6acec52c7de69181f5194/skills/ppt-master/references/ai-image-comparison/rendering/blueprint.png"><code>skills/ppt-master/references/ai-image-comparison/rendering/blueprint.png</code></a></sub>

<img src="https://raw.githubusercontent.com/hugohe3/ppt-master/7ae3721c856fedb921d6acec52c7de69181f5194/skills/ppt-master/references/ai-image-comparison/rendering/chalkboard.png" width="100%" alt="PPT Master sample">

<sub><b>Chalkboard</b> · <a href="https://github.com/hugohe3/ppt-master/blob/7ae3721c856fedb921d6acec52c7de69181f5194/skills/ppt-master/references/ai-image-comparison/rendering/chalkboard.png"><code>skills/ppt-master/references/ai-image-comparison/rendering/chalkboard.png</code></a></sub>

<img src="https://raw.githubusercontent.com/hugohe3/ppt-master/7ae3721c856fedb921d6acec52c7de69181f5194/skills/ppt-master/references/ai-image-comparison/rendering/corporate-photo.png" width="100%" alt="PPT Master sample">

<sub><b>Corporate Photo</b> · <a href="https://github.com/hugohe3/ppt-master/blob/7ae3721c856fedb921d6acec52c7de69181f5194/skills/ppt-master/references/ai-image-comparison/rendering/corporate-photo.png"><code>skills/ppt-master/references/ai-image-comparison/rendering/corporate-photo.png</code></a></sub>

<img src="https://raw.githubusercontent.com/hugohe3/ppt-master/7ae3721c856fedb921d6acec52c7de69181f5194/skills/ppt-master/references/ai-image-comparison/rendering/digital-dashboard.png" width="100%" alt="PPT Master sample">

<sub><b>Digital Dashboard</b> · <a href="https://github.com/hugohe3/ppt-master/blob/7ae3721c856fedb921d6acec52c7de69181f5194/skills/ppt-master/references/ai-image-comparison/rendering/digital-dashboard.png"><code>skills/ppt-master/references/ai-image-comparison/rendering/digital-dashboard.png</code></a></sub>

<img src="https://raw.githubusercontent.com/hugohe3/ppt-master/7ae3721c856fedb921d6acec52c7de69181f5194/skills/ppt-master/references/ai-image-comparison/rendering/editorial.png" width="100%" alt="PPT Master sample">

<sub><b>Editorial</b> · <a href="https://github.com/hugohe3/ppt-master/blob/7ae3721c856fedb921d6acec52c7de69181f5194/skills/ppt-master/references/ai-image-comparison/rendering/editorial.png"><code>skills/ppt-master/references/ai-image-comparison/rendering/editorial.png</code></a></sub>

<img src="https://raw.githubusercontent.com/hugohe3/ppt-master/7ae3721c856fedb921d6acec52c7de69181f5194/skills/ppt-master/references/ai-image-comparison/rendering/fantasy-animation.png" width="100%" alt="PPT Master sample">

<sub><b>Fantasy Animation</b> · <a href="https://github.com/hugohe3/ppt-master/blob/7ae3721c856fedb921d6acec52c7de69181f5194/skills/ppt-master/references/ai-image-comparison/rendering/fantasy-animation.png"><code>skills/ppt-master/references/ai-image-comparison/rendering/fantasy-animation.png</code></a></sub>

<img src="https://raw.githubusercontent.com/hugohe3/ppt-master/7ae3721c856fedb921d6acec52c7de69181f5194/skills/ppt-master/references/ai-image-comparison/rendering/flat.png" width="100%" alt="PPT Master sample">

<sub><b>Flat</b> · <a href="https://github.com/hugohe3/ppt-master/blob/7ae3721c856fedb921d6acec52c7de69181f5194/skills/ppt-master/references/ai-image-comparison/rendering/flat.png"><code>skills/ppt-master/references/ai-image-comparison/rendering/flat.png</code></a></sub>

<a id="gallery-frontend-slides"></a>

#### [Frontend Slides](https://github.com/zarazhangrui/frontend-slides) · 26,461 ⭐ · HTML

<sub>Beautiful slides on the web using a coding agent's frontend skills.</sub>

<sub>24 of 102 images in [`zarazhangrui/frontend-slides`](https://github.com/zarazhangrui/frontend-slides) · the leading frames are the ones the project puts in its own README</sub>

```bash
/plugin marketplace add https://github.com/zarazhangrui/frontend-slides
/plugin install frontend-slides@frontend-slides
```

<sub><b>Styles below</b> `soft-editorial` · `editorial-forest` · `pin-and-paper` · `sakura-chroma` · `stencil-tablet` · `cobalt-grid` · `vellum` · `emerald-editorial` — name one when you ask for a deck. These are the project's own strings, taken from the filenames and captions linked under each image, not names this registry made up.</sub>

<img src="https://raw.githubusercontent.com/zarazhangrui/beautiful-html-templates/e5e204fb1f3b06290846e7dcd7aceddabeceec8c/screenshots/soft-editorial-4.png" width="100%" alt="Soft Editorial — slide 4">

<sub><b>Soft Editorial — slide 4</b> · <a href="https://github.com/zarazhangrui/beautiful-html-templates/blob/e5e204fb1f3b06290846e7dcd7aceddabeceec8c/screenshots/soft-editorial-4.png"><code>screenshots/soft-editorial-4.png</code></a></sub>

<img src="https://raw.githubusercontent.com/zarazhangrui/beautiful-html-templates/e5e204fb1f3b06290846e7dcd7aceddabeceec8c/screenshots/soft-editorial-6.png" width="100%" alt="Soft Editorial — slide 6">

<sub><b>Soft Editorial — slide 6</b> · <a href="https://github.com/zarazhangrui/beautiful-html-templates/blob/e5e204fb1f3b06290846e7dcd7aceddabeceec8c/screenshots/soft-editorial-6.png"><code>screenshots/soft-editorial-6.png</code></a></sub>

<img src="https://raw.githubusercontent.com/zarazhangrui/beautiful-html-templates/e5e204fb1f3b06290846e7dcd7aceddabeceec8c/screenshots/soft-editorial-10.png" width="100%" alt="Soft Editorial — slide 10">

<sub><b>Soft Editorial — slide 10</b> · <a href="https://github.com/zarazhangrui/beautiful-html-templates/blob/e5e204fb1f3b06290846e7dcd7aceddabeceec8c/screenshots/soft-editorial-10.png"><code>screenshots/soft-editorial-10.png</code></a></sub>

<img src="https://raw.githubusercontent.com/zarazhangrui/beautiful-html-templates/e5e204fb1f3b06290846e7dcd7aceddabeceec8c/screenshots/editorial-forest-1.png" width="100%" alt="Editorial Forest — slide 1">

<sub><b>Editorial Forest — slide 1</b> · <a href="https://github.com/zarazhangrui/beautiful-html-templates/blob/e5e204fb1f3b06290846e7dcd7aceddabeceec8c/screenshots/editorial-forest-1.png"><code>screenshots/editorial-forest-1.png</code></a></sub>

<img src="https://raw.githubusercontent.com/zarazhangrui/beautiful-html-templates/e5e204fb1f3b06290846e7dcd7aceddabeceec8c/screenshots/editorial-forest-2.png" width="100%" alt="Editorial Forest — slide 2">

<sub><b>Editorial Forest — slide 2</b> · <a href="https://github.com/zarazhangrui/beautiful-html-templates/blob/e5e204fb1f3b06290846e7dcd7aceddabeceec8c/screenshots/editorial-forest-2.png"><code>screenshots/editorial-forest-2.png</code></a></sub>

<img src="https://raw.githubusercontent.com/zarazhangrui/beautiful-html-templates/e5e204fb1f3b06290846e7dcd7aceddabeceec8c/screenshots/editorial-forest-5.png" width="100%" alt="Editorial Forest — slide 5">

<sub><b>Editorial Forest — slide 5</b> · <a href="https://github.com/zarazhangrui/beautiful-html-templates/blob/e5e204fb1f3b06290846e7dcd7aceddabeceec8c/screenshots/editorial-forest-5.png"><code>screenshots/editorial-forest-5.png</code></a></sub>

<img src="https://raw.githubusercontent.com/zarazhangrui/beautiful-html-templates/e5e204fb1f3b06290846e7dcd7aceddabeceec8c/screenshots/pin-and-paper-1.png" width="100%" alt="Pin & Paper — slide 1">

<sub><b>Pin & Paper — slide 1</b> · <code>pin-and-paper</code> · <a href="https://github.com/zarazhangrui/beautiful-html-templates/blob/e5e204fb1f3b06290846e7dcd7aceddabeceec8c/screenshots/pin-and-paper-1.png"><code>screenshots/pin-and-paper-1.png</code></a></sub>

<img src="https://raw.githubusercontent.com/zarazhangrui/beautiful-html-templates/e5e204fb1f3b06290846e7dcd7aceddabeceec8c/screenshots/pin-and-paper-11.png" width="100%" alt="Pin & Paper — slide 11">

<sub><b>Pin & Paper — slide 11</b> · <code>pin-and-paper</code> · <a href="https://github.com/zarazhangrui/beautiful-html-templates/blob/e5e204fb1f3b06290846e7dcd7aceddabeceec8c/screenshots/pin-and-paper-11.png"><code>screenshots/pin-and-paper-11.png</code></a></sub>

<img src="https://raw.githubusercontent.com/zarazhangrui/beautiful-html-templates/e5e204fb1f3b06290846e7dcd7aceddabeceec8c/screenshots/pin-and-paper-3.png" width="100%" alt="Pin & Paper — slide 3">

<sub><b>Pin & Paper — slide 3</b> · <code>pin-and-paper</code> · <a href="https://github.com/zarazhangrui/beautiful-html-templates/blob/e5e204fb1f3b06290846e7dcd7aceddabeceec8c/screenshots/pin-and-paper-3.png"><code>screenshots/pin-and-paper-3.png</code></a></sub>

<img src="https://raw.githubusercontent.com/zarazhangrui/beautiful-html-templates/e5e204fb1f3b06290846e7dcd7aceddabeceec8c/screenshots/sakura-chroma-1.png" width="100%" alt="Sakura Chroma — slide 1">

<sub><b>Sakura Chroma — slide 1</b> · <a href="https://github.com/zarazhangrui/beautiful-html-templates/blob/e5e204fb1f3b06290846e7dcd7aceddabeceec8c/screenshots/sakura-chroma-1.png"><code>screenshots/sakura-chroma-1.png</code></a></sub>

<img src="https://raw.githubusercontent.com/zarazhangrui/beautiful-html-templates/e5e204fb1f3b06290846e7dcd7aceddabeceec8c/screenshots/sakura-chroma-3.png" width="100%" alt="Sakura Chroma — slide 3">

<sub><b>Sakura Chroma — slide 3</b> · <a href="https://github.com/zarazhangrui/beautiful-html-templates/blob/e5e204fb1f3b06290846e7dcd7aceddabeceec8c/screenshots/sakura-chroma-3.png"><code>screenshots/sakura-chroma-3.png</code></a></sub>

<img src="https://raw.githubusercontent.com/zarazhangrui/beautiful-html-templates/e5e204fb1f3b06290846e7dcd7aceddabeceec8c/screenshots/sakura-chroma-4.png" width="100%" alt="Sakura Chroma — slide 4">

<sub><b>Sakura Chroma — slide 4</b> · <a href="https://github.com/zarazhangrui/beautiful-html-templates/blob/e5e204fb1f3b06290846e7dcd7aceddabeceec8c/screenshots/sakura-chroma-4.png"><code>screenshots/sakura-chroma-4.png</code></a></sub>

<img src="https://raw.githubusercontent.com/zarazhangrui/beautiful-html-templates/e5e204fb1f3b06290846e7dcd7aceddabeceec8c/screenshots/stencil-tablet-1.png" width="100%" alt="Stencil & Tablet — slide 1">

<sub><b>Stencil & Tablet — slide 1</b> · <code>stencil-tablet</code> · <a href="https://github.com/zarazhangrui/beautiful-html-templates/blob/e5e204fb1f3b06290846e7dcd7aceddabeceec8c/screenshots/stencil-tablet-1.png"><code>screenshots/stencil-tablet-1.png</code></a></sub>

<img src="https://raw.githubusercontent.com/zarazhangrui/beautiful-html-templates/e5e204fb1f3b06290846e7dcd7aceddabeceec8c/screenshots/stencil-tablet-3.png" width="100%" alt="Stencil & Tablet — slide 3">

<sub><b>Stencil & Tablet — slide 3</b> · <code>stencil-tablet</code> · <a href="https://github.com/zarazhangrui/beautiful-html-templates/blob/e5e204fb1f3b06290846e7dcd7aceddabeceec8c/screenshots/stencil-tablet-3.png"><code>screenshots/stencil-tablet-3.png</code></a></sub>

<img src="https://raw.githubusercontent.com/zarazhangrui/beautiful-html-templates/e5e204fb1f3b06290846e7dcd7aceddabeceec8c/screenshots/stencil-tablet-8.png" width="100%" alt="Stencil & Tablet — slide 8">

<sub><b>Stencil & Tablet — slide 8</b> · <code>stencil-tablet</code> · <a href="https://github.com/zarazhangrui/beautiful-html-templates/blob/e5e204fb1f3b06290846e7dcd7aceddabeceec8c/screenshots/stencil-tablet-8.png"><code>screenshots/stencil-tablet-8.png</code></a></sub>

<img src="https://raw.githubusercontent.com/zarazhangrui/beautiful-html-templates/e5e204fb1f3b06290846e7dcd7aceddabeceec8c/screenshots/cobalt-grid-1.png" width="100%" alt="Cobalt Grid — slide 1">

<sub><b>Cobalt Grid — slide 1</b> · <a href="https://github.com/zarazhangrui/beautiful-html-templates/blob/e5e204fb1f3b06290846e7dcd7aceddabeceec8c/screenshots/cobalt-grid-1.png"><code>screenshots/cobalt-grid-1.png</code></a></sub>

<img src="https://raw.githubusercontent.com/zarazhangrui/beautiful-html-templates/e5e204fb1f3b06290846e7dcd7aceddabeceec8c/screenshots/cobalt-grid-3.png" width="100%" alt="Cobalt Grid — slide 3">

<sub><b>Cobalt Grid — slide 3</b> · <a href="https://github.com/zarazhangrui/beautiful-html-templates/blob/e5e204fb1f3b06290846e7dcd7aceddabeceec8c/screenshots/cobalt-grid-3.png"><code>screenshots/cobalt-grid-3.png</code></a></sub>

<img src="https://raw.githubusercontent.com/zarazhangrui/beautiful-html-templates/e5e204fb1f3b06290846e7dcd7aceddabeceec8c/screenshots/cobalt-grid-5.png" width="100%" alt="Cobalt Grid — slide 5">

<sub><b>Cobalt Grid — slide 5</b> · <a href="https://github.com/zarazhangrui/beautiful-html-templates/blob/e5e204fb1f3b06290846e7dcd7aceddabeceec8c/screenshots/cobalt-grid-5.png"><code>screenshots/cobalt-grid-5.png</code></a></sub>

<img src="https://raw.githubusercontent.com/zarazhangrui/beautiful-html-templates/e5e204fb1f3b06290846e7dcd7aceddabeceec8c/screenshots/vellum-1.png" width="100%" alt="Vellum — slide 1">

<sub><b>Vellum — slide 1</b> · <a href="https://github.com/zarazhangrui/beautiful-html-templates/blob/e5e204fb1f3b06290846e7dcd7aceddabeceec8c/screenshots/vellum-1.png"><code>screenshots/vellum-1.png</code></a></sub>

<img src="https://raw.githubusercontent.com/zarazhangrui/beautiful-html-templates/e5e204fb1f3b06290846e7dcd7aceddabeceec8c/screenshots/vellum-4.png" width="100%" alt="Vellum — slide 4">

<sub><b>Vellum — slide 4</b> · <a href="https://github.com/zarazhangrui/beautiful-html-templates/blob/e5e204fb1f3b06290846e7dcd7aceddabeceec8c/screenshots/vellum-4.png"><code>screenshots/vellum-4.png</code></a></sub>

<img src="https://raw.githubusercontent.com/zarazhangrui/beautiful-html-templates/e5e204fb1f3b06290846e7dcd7aceddabeceec8c/screenshots/vellum-8.png" width="100%" alt="Vellum — slide 8">

<sub><b>Vellum — slide 8</b> · <a href="https://github.com/zarazhangrui/beautiful-html-templates/blob/e5e204fb1f3b06290846e7dcd7aceddabeceec8c/screenshots/vellum-8.png"><code>screenshots/vellum-8.png</code></a></sub>

<img src="https://raw.githubusercontent.com/zarazhangrui/beautiful-html-templates/e5e204fb1f3b06290846e7dcd7aceddabeceec8c/screenshots/emerald-editorial-1.png" width="100%" alt="Emerald Editorial — slide 1">

<sub><b>Emerald Editorial — slide 1</b> · <a href="https://github.com/zarazhangrui/beautiful-html-templates/blob/e5e204fb1f3b06290846e7dcd7aceddabeceec8c/screenshots/emerald-editorial-1.png"><code>screenshots/emerald-editorial-1.png</code></a></sub>

<img src="https://raw.githubusercontent.com/zarazhangrui/beautiful-html-templates/e5e204fb1f3b06290846e7dcd7aceddabeceec8c/screenshots/emerald-editorial-3.png" width="100%" alt="Emerald Editorial — slide 3">

<sub><b>Emerald Editorial — slide 3</b> · <a href="https://github.com/zarazhangrui/beautiful-html-templates/blob/e5e204fb1f3b06290846e7dcd7aceddabeceec8c/screenshots/emerald-editorial-3.png"><code>screenshots/emerald-editorial-3.png</code></a></sub>

<img src="https://raw.githubusercontent.com/zarazhangrui/beautiful-html-templates/e5e204fb1f3b06290846e7dcd7aceddabeceec8c/screenshots/emerald-editorial-6.png" width="100%" alt="Emerald Editorial — slide 6">

<sub><b>Emerald Editorial — slide 6</b> · <a href="https://github.com/zarazhangrui/beautiful-html-templates/blob/e5e204fb1f3b06290846e7dcd7aceddabeceec8c/screenshots/emerald-editorial-6.png"><code>screenshots/emerald-editorial-6.png</code></a></sub>

<a id="gallery-guizang-ppt-skill"></a>

#### [Guizang PPT Skill](https://github.com/op7418/guizang-ppt-skill) · 22,564 ⭐ · HTML

<sub>Editorial-magazine and Swiss-International HTML decks, with design locked down by constraint.</sub>

<sub>13 of 13 images in [`op7418/guizang-ppt-skill`](https://github.com/op7418/guizang-ppt-skill) · the leading frames are the ones the project puts in its own README</sub>

```bash
npx skills add https://github.com/op7418/guizang-ppt-skill --skill guizang-ppt-skill
```

<sub><b>Styles below</b> `ppt-skill-showcase` — name one when you ask for a deck. These are the project's own strings, taken from the filenames and captions linked under each image, not names this registry made up.</sub>

<img src="https://github.com/user-attachments/assets/5dc316a2-401c-4e37-9123-ea081b6ae470" width="100%" alt="Style A 电子杂志风效果展示">

<sub><b>Style A 电子杂志风效果展示</b> · GitHub attachment</sub>

<img src="https://github.com/user-attachments/assets/8960e78c-69bb-4b7e-aa95-6fad64b70314" width="100%" alt="Style B 瑞士国际主义效果展示">

<sub><b>Style B 瑞士国际主义效果展示</b> · GitHub attachment</sub>

<img src="https://github.com/user-attachments/assets/df21dbcb-5fe4-4852-a91a-a9cf00aceeb4" width="100%" alt="墨水经典主题预览">

<sub><b>墨水经典主题预览</b> · GitHub attachment</sub>

<img src="https://github.com/user-attachments/assets/99ce0fd2-72a6-4368-a75a-a8e21657a537" width="100%" alt="靛蓝瓷主题预览">

<sub><b>靛蓝瓷主题预览</b> · GitHub attachment</sub>

<img src="https://github.com/user-attachments/assets/bcc1cc4c-5e8e-4467-ae8d-f5801ae73657" width="100%" alt="森林墨主题预览">

<sub><b>森林墨主题预览</b> · GitHub attachment</sub>

<img src="https://github.com/user-attachments/assets/dfea080e-e916-417e-93cd-0a3628de84ca" width="100%" alt="牛皮纸主题预览">

<sub><b>牛皮纸主题预览</b> · GitHub attachment</sub>

<img src="https://github.com/user-attachments/assets/f3705592-9a72-4dbc-9818-df3aea61bc75" width="100%" alt="沙丘主题预览">

<sub><b>沙丘主题预览</b> · GitHub attachment</sub>

<img src="https://github.com/user-attachments/assets/c02d02f7-ce6f-4e16-b8a6-778c96851f94" width="100%" alt="克莱因蓝瑞士主题预览">

<sub><b>克莱因蓝瑞士主题预览</b> · GitHub attachment</sub>

<img src="https://github.com/user-attachments/assets/c310a8c4-5d28-450e-b49a-6ac5b6ba4785" width="100%" alt="柠檬黄瑞士主题预览">

<sub><b>柠檬黄瑞士主题预览</b> · GitHub attachment</sub>

<img src="https://github.com/user-attachments/assets/65f7b3f9-3358-419e-b513-f7f2cc24ec76" width="100%" alt="柠檬绿瑞士主题预览">

<sub><b>柠檬绿瑞士主题预览</b> · GitHub attachment</sub>

<img src="https://github.com/user-attachments/assets/9c3319c9-a134-4657-9a56-211c23411f7f" width="100%" alt="安全橙瑞士主题预览">

<sub><b>安全橙瑞士主题预览</b> · GitHub attachment</sub>

<img src="https://github.com/user-attachments/assets/81138fad-31b9-49ab-8e38-23b2bc48edc4" width="100%" alt="360 安全龙虾 / Kimi work / Cola Skill 金牌赞助">

<sub><b>360 安全龙虾 / Kimi work / Cola Skill 金牌赞助</b> · GitHub attachment</sub>

<img src="https://raw.githubusercontent.com/op7418/guizang-ppt-skill/929c2ecb63a22b54d400c4911ed70bf96c2b355d/assets/ppt-skill-showcase.png" width="100%" alt="Guizang PPT Skill sample">

<sub><b>Ppt Skill Showcase</b> · <a href="https://github.com/op7418/guizang-ppt-skill/blob/929c2ecb63a22b54d400c4911ed70bf96c2b355d/assets/ppt-skill-showcase.png"><code>assets/ppt-skill-showcase.png</code></a></sub>

<a id="gallery-huashu-design"></a>

#### [Huashu Design](https://github.com/alchaincyf/huashu-design) · 22,135 ⭐ · Both

<sub>HTML-native design skill — prototypes, decks, motion and design critique, not just slides.</sub>

<sub>24 of 24 images in [`alchaincyf/huashu-design`](https://github.com/alchaincyf/huashu-design)</sub>

```bash
npx skills add alchaincyf/huashu-design
```

<sub><b>Styles below</b> `ppt-build` · `ppt-pentagram` · `ppt-takram` · `ainav-build` · `ainav-pentagram` · `ainav-takram` · `aiwriting-build` · `aiwriting-pentagram` · `aiwriting-takram` · `devdocs-build` · `devdocs-pentagram` · `devdocs-takram` — name one when you ask for a deck. These are the project's own strings, taken from the filenames and captions linked under each image, not names this registry made up.</sub>

<img src="https://raw.githubusercontent.com/alchaincyf/huashu-design/1572d431f1411c82ec0baea94dea6a45f6063b26/assets/showcases/ppt/ppt-build.png" width="100%" alt="Huashu Design sample">

<sub><b>Ppt Build</b> · <a href="https://github.com/alchaincyf/huashu-design/blob/1572d431f1411c82ec0baea94dea6a45f6063b26/assets/showcases/ppt/ppt-build.png"><code>assets/showcases/ppt/ppt-build.png</code></a></sub>

<img src="https://raw.githubusercontent.com/alchaincyf/huashu-design/1572d431f1411c82ec0baea94dea6a45f6063b26/assets/showcases/ppt/ppt-pentagram.png" width="100%" alt="Huashu Design sample">

<sub><b>Ppt Pentagram</b> · <a href="https://github.com/alchaincyf/huashu-design/blob/1572d431f1411c82ec0baea94dea6a45f6063b26/assets/showcases/ppt/ppt-pentagram.png"><code>assets/showcases/ppt/ppt-pentagram.png</code></a></sub>

<img src="https://raw.githubusercontent.com/alchaincyf/huashu-design/1572d431f1411c82ec0baea94dea6a45f6063b26/assets/showcases/ppt/ppt-takram.png" width="100%" alt="Huashu Design sample">

<sub><b>Ppt Takram</b> · <a href="https://github.com/alchaincyf/huashu-design/blob/1572d431f1411c82ec0baea94dea6a45f6063b26/assets/showcases/ppt/ppt-takram.png"><code>assets/showcases/ppt/ppt-takram.png</code></a></sub>

<img src="https://raw.githubusercontent.com/alchaincyf/huashu-design/1572d431f1411c82ec0baea94dea6a45f6063b26/assets/showcases/website-ai-nav/ainav-build.png" width="100%" alt="Huashu Design sample">

<sub><b>Ainav Build</b> · <a href="https://github.com/alchaincyf/huashu-design/blob/1572d431f1411c82ec0baea94dea6a45f6063b26/assets/showcases/website-ai-nav/ainav-build.png"><code>assets/showcases/website-ai-nav/ainav-build.png</code></a></sub>

<img src="https://raw.githubusercontent.com/alchaincyf/huashu-design/1572d431f1411c82ec0baea94dea6a45f6063b26/assets/showcases/website-ai-nav/ainav-pentagram.png" width="100%" alt="Huashu Design sample">

<sub><b>Ainav Pentagram</b> · <a href="https://github.com/alchaincyf/huashu-design/blob/1572d431f1411c82ec0baea94dea6a45f6063b26/assets/showcases/website-ai-nav/ainav-pentagram.png"><code>assets/showcases/website-ai-nav/ainav-pentagram.png</code></a></sub>

<img src="https://raw.githubusercontent.com/alchaincyf/huashu-design/1572d431f1411c82ec0baea94dea6a45f6063b26/assets/showcases/website-ai-nav/ainav-takram.png" width="100%" alt="Huashu Design sample">

<sub><b>Ainav Takram</b> · <a href="https://github.com/alchaincyf/huashu-design/blob/1572d431f1411c82ec0baea94dea6a45f6063b26/assets/showcases/website-ai-nav/ainav-takram.png"><code>assets/showcases/website-ai-nav/ainav-takram.png</code></a></sub>

<img src="https://raw.githubusercontent.com/alchaincyf/huashu-design/1572d431f1411c82ec0baea94dea6a45f6063b26/assets/showcases/website-ai-writing/aiwriting-build.png" width="100%" alt="Huashu Design sample">

<sub><b>Aiwriting Build</b> · <a href="https://github.com/alchaincyf/huashu-design/blob/1572d431f1411c82ec0baea94dea6a45f6063b26/assets/showcases/website-ai-writing/aiwriting-build.png"><code>assets/showcases/website-ai-writing/aiwriting-build.png</code></a></sub>

<img src="https://raw.githubusercontent.com/alchaincyf/huashu-design/1572d431f1411c82ec0baea94dea6a45f6063b26/assets/showcases/website-ai-writing/aiwriting-pentagram.png" width="100%" alt="Huashu Design sample">

<sub><b>Aiwriting Pentagram</b> · <a href="https://github.com/alchaincyf/huashu-design/blob/1572d431f1411c82ec0baea94dea6a45f6063b26/assets/showcases/website-ai-writing/aiwriting-pentagram.png"><code>assets/showcases/website-ai-writing/aiwriting-pentagram.png</code></a></sub>

<img src="https://raw.githubusercontent.com/alchaincyf/huashu-design/1572d431f1411c82ec0baea94dea6a45f6063b26/assets/showcases/website-ai-writing/aiwriting-takram.png" width="100%" alt="Huashu Design sample">

<sub><b>Aiwriting Takram</b> · <a href="https://github.com/alchaincyf/huashu-design/blob/1572d431f1411c82ec0baea94dea6a45f6063b26/assets/showcases/website-ai-writing/aiwriting-takram.png"><code>assets/showcases/website-ai-writing/aiwriting-takram.png</code></a></sub>

<img src="https://raw.githubusercontent.com/alchaincyf/huashu-design/1572d431f1411c82ec0baea94dea6a45f6063b26/assets/showcases/website-devdocs/devdocs-build.png" width="100%" alt="Huashu Design sample">

<sub><b>Devdocs Build</b> · <a href="https://github.com/alchaincyf/huashu-design/blob/1572d431f1411c82ec0baea94dea6a45f6063b26/assets/showcases/website-devdocs/devdocs-build.png"><code>assets/showcases/website-devdocs/devdocs-build.png</code></a></sub>

<img src="https://raw.githubusercontent.com/alchaincyf/huashu-design/1572d431f1411c82ec0baea94dea6a45f6063b26/assets/showcases/website-devdocs/devdocs-pentagram.png" width="100%" alt="Huashu Design sample">

<sub><b>Devdocs Pentagram</b> · <a href="https://github.com/alchaincyf/huashu-design/blob/1572d431f1411c82ec0baea94dea6a45f6063b26/assets/showcases/website-devdocs/devdocs-pentagram.png"><code>assets/showcases/website-devdocs/devdocs-pentagram.png</code></a></sub>

<img src="https://raw.githubusercontent.com/alchaincyf/huashu-design/1572d431f1411c82ec0baea94dea6a45f6063b26/assets/showcases/website-devdocs/devdocs-takram.png" width="100%" alt="Huashu Design sample">

<sub><b>Devdocs Takram</b> · <a href="https://github.com/alchaincyf/huashu-design/blob/1572d431f1411c82ec0baea94dea6a45f6063b26/assets/showcases/website-devdocs/devdocs-takram.png"><code>assets/showcases/website-devdocs/devdocs-takram.png</code></a></sub>

<img src="https://raw.githubusercontent.com/alchaincyf/huashu-design/1572d431f1411c82ec0baea94dea6a45f6063b26/assets/showcases/website-homepage/homepage-build.png" width="100%" alt="Huashu Design sample">

<sub><b>Homepage Build</b> · <a href="https://github.com/alchaincyf/huashu-design/blob/1572d431f1411c82ec0baea94dea6a45f6063b26/assets/showcases/website-homepage/homepage-build.png"><code>assets/showcases/website-homepage/homepage-build.png</code></a></sub>

<img src="https://raw.githubusercontent.com/alchaincyf/huashu-design/1572d431f1411c82ec0baea94dea6a45f6063b26/assets/showcases/website-homepage/homepage-pentagram.png" width="100%" alt="Huashu Design sample">

<sub><b>Homepage Pentagram</b> · <a href="https://github.com/alchaincyf/huashu-design/blob/1572d431f1411c82ec0baea94dea6a45f6063b26/assets/showcases/website-homepage/homepage-pentagram.png"><code>assets/showcases/website-homepage/homepage-pentagram.png</code></a></sub>

<img src="https://raw.githubusercontent.com/alchaincyf/huashu-design/1572d431f1411c82ec0baea94dea6a45f6063b26/assets/showcases/website-homepage/homepage-takram.png" width="100%" alt="Huashu Design sample">

<sub><b>Homepage Takram</b> · <a href="https://github.com/alchaincyf/huashu-design/blob/1572d431f1411c82ec0baea94dea6a45f6063b26/assets/showcases/website-homepage/homepage-takram.png"><code>assets/showcases/website-homepage/homepage-takram.png</code></a></sub>

<img src="https://raw.githubusercontent.com/alchaincyf/huashu-design/1572d431f1411c82ec0baea94dea6a45f6063b26/assets/showcases/website-saas/saas-build.png" width="100%" alt="Huashu Design sample">

<sub><b>Saas Build</b> · <a href="https://github.com/alchaincyf/huashu-design/blob/1572d431f1411c82ec0baea94dea6a45f6063b26/assets/showcases/website-saas/saas-build.png"><code>assets/showcases/website-saas/saas-build.png</code></a></sub>

<img src="https://raw.githubusercontent.com/alchaincyf/huashu-design/1572d431f1411c82ec0baea94dea6a45f6063b26/assets/showcases/website-saas/saas-pentagram.png" width="100%" alt="Huashu Design sample">

<sub><b>Saas Pentagram</b> · <a href="https://github.com/alchaincyf/huashu-design/blob/1572d431f1411c82ec0baea94dea6a45f6063b26/assets/showcases/website-saas/saas-pentagram.png"><code>assets/showcases/website-saas/saas-pentagram.png</code></a></sub>

<img src="https://raw.githubusercontent.com/alchaincyf/huashu-design/1572d431f1411c82ec0baea94dea6a45f6063b26/assets/showcases/website-saas/saas-takram.png" width="100%" alt="Huashu Design sample">

<sub><b>Saas Takram</b> · <a href="https://github.com/alchaincyf/huashu-design/blob/1572d431f1411c82ec0baea94dea6a45f6063b26/assets/showcases/website-saas/saas-takram.png"><code>assets/showcases/website-saas/saas-takram.png</code></a></sub>

<img src="https://raw.githubusercontent.com/alchaincyf/huashu-design/1572d431f1411c82ec0baea94dea6a45f6063b26/assets/showcases/infographic/infographic-build.png" width="100%" alt="Huashu Design sample">

<sub><b>Infographic Build</b> · <a href="https://github.com/alchaincyf/huashu-design/blob/1572d431f1411c82ec0baea94dea6a45f6063b26/assets/showcases/infographic/infographic-build.png"><code>assets/showcases/infographic/infographic-build.png</code></a></sub>

<img src="https://raw.githubusercontent.com/alchaincyf/huashu-design/1572d431f1411c82ec0baea94dea6a45f6063b26/assets/showcases/infographic/infographic-pentagram.png" width="100%" alt="Huashu Design sample">

<sub><b>Infographic Pentagram</b> · <a href="https://github.com/alchaincyf/huashu-design/blob/1572d431f1411c82ec0baea94dea6a45f6063b26/assets/showcases/infographic/infographic-pentagram.png"><code>assets/showcases/infographic/infographic-pentagram.png</code></a></sub>

<img src="https://raw.githubusercontent.com/alchaincyf/huashu-design/1572d431f1411c82ec0baea94dea6a45f6063b26/assets/showcases/infographic/infographic-takram.png" width="100%" alt="Huashu Design sample">

<sub><b>Infographic Takram</b> · <a href="https://github.com/alchaincyf/huashu-design/blob/1572d431f1411c82ec0baea94dea6a45f6063b26/assets/showcases/infographic/infographic-takram.png"><code>assets/showcases/infographic/infographic-takram.png</code></a></sub>

<img src="https://raw.githubusercontent.com/alchaincyf/huashu-design/1572d431f1411c82ec0baea94dea6a45f6063b26/assets/showcases/cover/cover-build.png" width="100%" alt="Huashu Design sample">

<sub><b>Cover Build</b> · <a href="https://github.com/alchaincyf/huashu-design/blob/1572d431f1411c82ec0baea94dea6a45f6063b26/assets/showcases/cover/cover-build.png"><code>assets/showcases/cover/cover-build.png</code></a></sub>

<img src="https://raw.githubusercontent.com/alchaincyf/huashu-design/1572d431f1411c82ec0baea94dea6a45f6063b26/assets/showcases/cover/cover-pentagram.png" width="100%" alt="Huashu Design sample">

<sub><b>Cover Pentagram</b> · <a href="https://github.com/alchaincyf/huashu-design/blob/1572d431f1411c82ec0baea94dea6a45f6063b26/assets/showcases/cover/cover-pentagram.png"><code>assets/showcases/cover/cover-pentagram.png</code></a></sub>

<img src="https://raw.githubusercontent.com/alchaincyf/huashu-design/1572d431f1411c82ec0baea94dea6a45f6063b26/assets/showcases/cover/cover-takram.png" width="100%" alt="Huashu Design sample">

<sub><b>Cover Takram</b> · <a href="https://github.com/alchaincyf/huashu-design/blob/1572d431f1411c82ec0baea94dea6a45f6063b26/assets/showcases/cover/cover-takram.png"><code>assets/showcases/cover/cover-takram.png</code></a></sub>

<a id="gallery-html-ppt-skill"></a>

#### [HTML PPT Studio](https://github.com/lewislulu/html-ppt-skill) · 7,437 ⭐ · HTML

<sub>24 themes, 31 layouts and 20+ animations for professional HTML presentations.</sub>

<sub>24 of 63 images in [`lewislulu/html-ppt-skill`](https://github.com/lewislulu/html-ppt-skill) · the leading frames are the ones the project puts in its own README</sub>

```bash
git clone https://github.com/lewislulu/html-ppt-skill ~/.claude/skills/html-ppt-skill
```

<sub><b>Styles below</b> `themes` · `templates` · `layouts` · `layouts-live` · `hero` · `presenter-mode` · `animations` · `animation-showcase` — name one when you ask for a deck. These are the project's own strings, taken from the filenames and captions linked under each image, not names this registry made up.</sub>

<img src="https://raw.githubusercontent.com/lewislulu/html-ppt-skill/f3a8435d3901697d5ac5e64d356c933637e43107/docs/readme/themes.png" width="100%" alt="36 themes · 8 of them">

<sub><b>36 themes · 8 of them</b> · <a href="https://github.com/lewislulu/html-ppt-skill/blob/f3a8435d3901697d5ac5e64d356c933637e43107/docs/readme/themes.png"><code>docs/readme/themes.png</code></a></sub>

<img src="https://raw.githubusercontent.com/lewislulu/html-ppt-skill/f3a8435d3901697d5ac5e64d356c933637e43107/docs/readme/templates.png" width="100%" alt="14 full-deck templates">

<sub><b>14 full-deck templates</b> · <a href="https://github.com/lewislulu/html-ppt-skill/blob/f3a8435d3901697d5ac5e64d356c933637e43107/docs/readme/templates.png"><code>docs/readme/templates.png</code></a></sub>

<img src="https://raw.githubusercontent.com/lewislulu/html-ppt-skill/f3a8435d3901697d5ac5e64d356c933637e43107/docs/readme/layouts.png" width="100%" alt="31 single-page layouts">

<sub><b>31 single-page layouts</b> · <a href="https://github.com/lewislulu/html-ppt-skill/blob/f3a8435d3901697d5ac5e64d356c933637e43107/docs/readme/layouts.png"><code>docs/readme/layouts.png</code></a></sub>

<img src="https://raw.githubusercontent.com/lewislulu/html-ppt-skill/f3a8435d3901697d5ac5e64d356c933637e43107/docs/readme/layouts-live.gif" width="100%" alt="31 layouts auto-cycling through real template files">

<sub><b>31 layouts auto-cycling through real template files</b> · <code>layouts-live</code> · <a href="https://github.com/lewislulu/html-ppt-skill/blob/f3a8435d3901697d5ac5e64d356c933637e43107/docs/readme/layouts-live.gif"><code>docs/readme/layouts-live.gif</code></a></sub>

<img src="https://raw.githubusercontent.com/lewislulu/html-ppt-skill/f3a8435d3901697d5ac5e64d356c933637e43107/docs/readme/hero.gif" width="100%" alt="html-ppt — cover with live previews">

<sub><b>html-ppt — cover with live previews</b> · <code>hero</code> · <a href="https://github.com/lewislulu/html-ppt-skill/blob/f3a8435d3901697d5ac5e64d356c933637e43107/docs/readme/hero.gif"><code>docs/readme/hero.gif</code></a></sub>

<img src="https://raw.githubusercontent.com/lewislulu/html-ppt-skill/f3a8435d3901697d5ac5e64d356c933637e43107/docs/readme/presenter-mode.png" width="100%" alt="Presenter mode with 4 magnetic cards">

<sub><b>Presenter mode with 4 magnetic cards</b> · <a href="https://github.com/lewislulu/html-ppt-skill/blob/f3a8435d3901697d5ac5e64d356c933637e43107/docs/readme/presenter-mode.png"><code>docs/readme/presenter-mode.png</code></a></sub>

<img src="https://raw.githubusercontent.com/lewislulu/html-ppt-skill/f3a8435d3901697d5ac5e64d356c933637e43107/docs/readme/animations.png" width="100%" alt="47 animations — 27 CSS + 20 canvas FX">

<sub><b>47 animations — 27 CSS + 20 canvas FX</b> · <a href="https://github.com/lewislulu/html-ppt-skill/blob/f3a8435d3901697d5ac5e64d356c933637e43107/docs/readme/animations.png"><code>docs/readme/animations.png</code></a></sub>

<img src="https://raw.githubusercontent.com/lewislulu/html-ppt-skill/f3a8435d3901697d5ac5e64d356c933637e43107/scripts/verify-output/animation-showcase/animation-showcase_01.png" width="100%" alt="HTML PPT Studio sample">

<sub><b>Animation Showcase · 01</b> · <a href="https://github.com/lewislulu/html-ppt-skill/blob/f3a8435d3901697d5ac5e64d356c933637e43107/scripts/verify-output/animation-showcase/animation-showcase_01.png"><code>scripts/verify-output/animation-showcase/animation-showcase_01.png</code></a></sub>

<img src="https://raw.githubusercontent.com/lewislulu/html-ppt-skill/f3a8435d3901697d5ac5e64d356c933637e43107/scripts/verify-output/animation-showcase/animation-showcase_02.png" width="100%" alt="HTML PPT Studio sample">

<sub><b>Animation Showcase · 02</b> · <a href="https://github.com/lewislulu/html-ppt-skill/blob/f3a8435d3901697d5ac5e64d356c933637e43107/scripts/verify-output/animation-showcase/animation-showcase_02.png"><code>scripts/verify-output/animation-showcase/animation-showcase_02.png</code></a></sub>

<img src="https://raw.githubusercontent.com/lewislulu/html-ppt-skill/f3a8435d3901697d5ac5e64d356c933637e43107/scripts/verify-output/animation-showcase/animation-showcase_03.png" width="100%" alt="HTML PPT Studio sample">

<sub><b>Animation Showcase · 03</b> · <a href="https://github.com/lewislulu/html-ppt-skill/blob/f3a8435d3901697d5ac5e64d356c933637e43107/scripts/verify-output/animation-showcase/animation-showcase_03.png"><code>scripts/verify-output/animation-showcase/animation-showcase_03.png</code></a></sub>

<img src="https://raw.githubusercontent.com/lewislulu/html-ppt-skill/f3a8435d3901697d5ac5e64d356c933637e43107/scripts/verify-output/animation-showcase/animation-showcase_04.png" width="100%" alt="HTML PPT Studio sample">

<sub><b>Animation Showcase · 04</b> · <a href="https://github.com/lewislulu/html-ppt-skill/blob/f3a8435d3901697d5ac5e64d356c933637e43107/scripts/verify-output/animation-showcase/animation-showcase_04.png"><code>scripts/verify-output/animation-showcase/animation-showcase_04.png</code></a></sub>

<img src="https://raw.githubusercontent.com/lewislulu/html-ppt-skill/f3a8435d3901697d5ac5e64d356c933637e43107/scripts/verify-output/animation-showcase/animation-showcase_05.png" width="100%" alt="HTML PPT Studio sample">

<sub><b>Animation Showcase · 05</b> · <a href="https://github.com/lewislulu/html-ppt-skill/blob/f3a8435d3901697d5ac5e64d356c933637e43107/scripts/verify-output/animation-showcase/animation-showcase_05.png"><code>scripts/verify-output/animation-showcase/animation-showcase_05.png</code></a></sub>

<img src="https://raw.githubusercontent.com/lewislulu/html-ppt-skill/f3a8435d3901697d5ac5e64d356c933637e43107/scripts/verify-output/animation-showcase/animation-showcase_06.png" width="100%" alt="HTML PPT Studio sample">

<sub><b>Animation Showcase · 06</b> · <a href="https://github.com/lewislulu/html-ppt-skill/blob/f3a8435d3901697d5ac5e64d356c933637e43107/scripts/verify-output/animation-showcase/animation-showcase_06.png"><code>scripts/verify-output/animation-showcase/animation-showcase_06.png</code></a></sub>

<img src="https://raw.githubusercontent.com/lewislulu/html-ppt-skill/f3a8435d3901697d5ac5e64d356c933637e43107/scripts/verify-output/animation-showcase/animation-showcase_07.png" width="100%" alt="HTML PPT Studio sample">

<sub><b>Animation Showcase · 07</b> · <a href="https://github.com/lewislulu/html-ppt-skill/blob/f3a8435d3901697d5ac5e64d356c933637e43107/scripts/verify-output/animation-showcase/animation-showcase_07.png"><code>scripts/verify-output/animation-showcase/animation-showcase_07.png</code></a></sub>

<img src="https://raw.githubusercontent.com/lewislulu/html-ppt-skill/f3a8435d3901697d5ac5e64d356c933637e43107/scripts/verify-output/animation-showcase/animation-showcase_08.png" width="100%" alt="HTML PPT Studio sample">

<sub><b>Animation Showcase · 08</b> · <a href="https://github.com/lewislulu/html-ppt-skill/blob/f3a8435d3901697d5ac5e64d356c933637e43107/scripts/verify-output/animation-showcase/animation-showcase_08.png"><code>scripts/verify-output/animation-showcase/animation-showcase_08.png</code></a></sub>

<img src="https://raw.githubusercontent.com/lewislulu/html-ppt-skill/f3a8435d3901697d5ac5e64d356c933637e43107/scripts/verify-output/animation-showcase/animation-showcase_09.png" width="100%" alt="HTML PPT Studio sample">

<sub><b>Animation Showcase · 09</b> · <a href="https://github.com/lewislulu/html-ppt-skill/blob/f3a8435d3901697d5ac5e64d356c933637e43107/scripts/verify-output/animation-showcase/animation-showcase_09.png"><code>scripts/verify-output/animation-showcase/animation-showcase_09.png</code></a></sub>

<img src="https://raw.githubusercontent.com/lewislulu/html-ppt-skill/f3a8435d3901697d5ac5e64d356c933637e43107/scripts/verify-output/animation-showcase/animation-showcase_10.png" width="100%" alt="HTML PPT Studio sample">

<sub><b>Animation Showcase · 10</b> · <a href="https://github.com/lewislulu/html-ppt-skill/blob/f3a8435d3901697d5ac5e64d356c933637e43107/scripts/verify-output/animation-showcase/animation-showcase_10.png"><code>scripts/verify-output/animation-showcase/animation-showcase_10.png</code></a></sub>

<img src="https://raw.githubusercontent.com/lewislulu/html-ppt-skill/f3a8435d3901697d5ac5e64d356c933637e43107/scripts/verify-output/animation-showcase/animation-showcase_11.png" width="100%" alt="HTML PPT Studio sample">

<sub><b>Animation Showcase · 11</b> · <a href="https://github.com/lewislulu/html-ppt-skill/blob/f3a8435d3901697d5ac5e64d356c933637e43107/scripts/verify-output/animation-showcase/animation-showcase_11.png"><code>scripts/verify-output/animation-showcase/animation-showcase_11.png</code></a></sub>

<img src="https://raw.githubusercontent.com/lewislulu/html-ppt-skill/f3a8435d3901697d5ac5e64d356c933637e43107/scripts/verify-output/animation-showcase/animation-showcase_12.png" width="100%" alt="HTML PPT Studio sample">

<sub><b>Animation Showcase · 12</b> · <a href="https://github.com/lewislulu/html-ppt-skill/blob/f3a8435d3901697d5ac5e64d356c933637e43107/scripts/verify-output/animation-showcase/animation-showcase_12.png"><code>scripts/verify-output/animation-showcase/animation-showcase_12.png</code></a></sub>

<img src="https://raw.githubusercontent.com/lewislulu/html-ppt-skill/f3a8435d3901697d5ac5e64d356c933637e43107/scripts/verify-output/animation-showcase/animation-showcase_13.png" width="100%" alt="HTML PPT Studio sample">

<sub><b>Animation Showcase · 13</b> · <a href="https://github.com/lewislulu/html-ppt-skill/blob/f3a8435d3901697d5ac5e64d356c933637e43107/scripts/verify-output/animation-showcase/animation-showcase_13.png"><code>scripts/verify-output/animation-showcase/animation-showcase_13.png</code></a></sub>

<img src="https://raw.githubusercontent.com/lewislulu/html-ppt-skill/f3a8435d3901697d5ac5e64d356c933637e43107/scripts/verify-output/animation-showcase/animation-showcase_14.png" width="100%" alt="HTML PPT Studio sample">

<sub><b>Animation Showcase · 14</b> · <a href="https://github.com/lewislulu/html-ppt-skill/blob/f3a8435d3901697d5ac5e64d356c933637e43107/scripts/verify-output/animation-showcase/animation-showcase_14.png"><code>scripts/verify-output/animation-showcase/animation-showcase_14.png</code></a></sub>

<img src="https://raw.githubusercontent.com/lewislulu/html-ppt-skill/f3a8435d3901697d5ac5e64d356c933637e43107/scripts/verify-output/animation-showcase/animation-showcase_15.png" width="100%" alt="HTML PPT Studio sample">

<sub><b>Animation Showcase · 15</b> · <a href="https://github.com/lewislulu/html-ppt-skill/blob/f3a8435d3901697d5ac5e64d356c933637e43107/scripts/verify-output/animation-showcase/animation-showcase_15.png"><code>scripts/verify-output/animation-showcase/animation-showcase_15.png</code></a></sub>

<img src="https://raw.githubusercontent.com/lewislulu/html-ppt-skill/f3a8435d3901697d5ac5e64d356c933637e43107/scripts/verify-output/animation-showcase/animation-showcase_16.png" width="100%" alt="HTML PPT Studio sample">

<sub><b>Animation Showcase · 16</b> · <a href="https://github.com/lewislulu/html-ppt-skill/blob/f3a8435d3901697d5ac5e64d356c933637e43107/scripts/verify-output/animation-showcase/animation-showcase_16.png"><code>scripts/verify-output/animation-showcase/animation-showcase_16.png</code></a></sub>

<img src="https://raw.githubusercontent.com/lewislulu/html-ppt-skill/f3a8435d3901697d5ac5e64d356c933637e43107/scripts/verify-output/animation-showcase/animation-showcase_17.png" width="100%" alt="HTML PPT Studio sample">

<sub><b>Animation Showcase · 17</b> · <a href="https://github.com/lewislulu/html-ppt-skill/blob/f3a8435d3901697d5ac5e64d356c933637e43107/scripts/verify-output/animation-showcase/animation-showcase_17.png"><code>scripts/verify-output/animation-showcase/animation-showcase_17.png</code></a></sub>

<a id="gallery-open-slide"></a>

#### [open-slide](https://github.com/1weiho/open-slide) · 6,027 ⭐ · Framework

<sub>A slide framework built for agents — React components on a fixed 1920x1080 canvas.</sub>

<sub>16 of 16 images in [`1weiho/open-slide`](https://github.com/1weiho/open-slide) · the leading frames are the ones the project puts in its own README</sub>

```bash
npx @open-slide/cli init my-slide
```

<sub><b>Styles below</b> `replit-features-result` · `create-slide-skill` · `openslide-home` · `replit-agent-home` · `assets-manager` · `inspector` · `presenter` · `theme` · `svgl` · `open-slide` · `replit-deploy` · `init-command` — name one when you ask for a deck. These are the project's own strings, taken from the filenames and captions linked under each image, not names this registry made up.</sub>

<img src="https://github.com/user-attachments/assets/02f5e6d7-12a7-4a8e-88e7-ae8770a96584" width="100%" alt="open-slide github cover">

<sub><b>open-slide github cover</b> · GitHub attachment</sub>

<img src="https://raw.githubusercontent.com/1weiho/open-slide/35dc46ca27716ea86f8a76710bbd3640e9590628/apps/demo/slides/open-slide-on-replit/assets/replit-features-result.webp" width="100%" alt="open-slide sample">

<sub><b>Replit Features Result</b> · <a href="https://github.com/1weiho/open-slide/blob/35dc46ca27716ea86f8a76710bbd3640e9590628/apps/demo/slides/open-slide-on-replit/assets/replit-features-result.webp"><code>apps/demo/slides/open-slide-on-replit/assets/replit-features-result.webp</code></a></sub>

<img src="https://raw.githubusercontent.com/1weiho/open-slide/35dc46ca27716ea86f8a76710bbd3640e9590628/apps/demo/slides/open-slide-on-replit/assets/create-slide-skill.webp" width="100%" alt="open-slide sample">

<sub><b>Create Slide Skill</b> · <a href="https://github.com/1weiho/open-slide/blob/35dc46ca27716ea86f8a76710bbd3640e9590628/apps/demo/slides/open-slide-on-replit/assets/create-slide-skill.webp"><code>apps/demo/slides/open-slide-on-replit/assets/create-slide-skill.webp</code></a></sub>

<img src="https://raw.githubusercontent.com/1weiho/open-slide/35dc46ca27716ea86f8a76710bbd3640e9590628/apps/demo/slides/open-slide-on-replit/assets/openslide-home.webp" width="100%" alt="open-slide sample">

<sub><b>Openslide Home</b> · <a href="https://github.com/1weiho/open-slide/blob/35dc46ca27716ea86f8a76710bbd3640e9590628/apps/demo/slides/open-slide-on-replit/assets/openslide-home.webp"><code>apps/demo/slides/open-slide-on-replit/assets/openslide-home.webp</code></a></sub>

<img src="https://raw.githubusercontent.com/1weiho/open-slide/35dc46ca27716ea86f8a76710bbd3640e9590628/apps/demo/slides/open-slide-on-replit/assets/replit-agent-home.webp" width="100%" alt="open-slide sample">

<sub><b>Replit Agent Home</b> · <a href="https://github.com/1weiho/open-slide/blob/35dc46ca27716ea86f8a76710bbd3640e9590628/apps/demo/slides/open-slide-on-replit/assets/replit-agent-home.webp"><code>apps/demo/slides/open-slide-on-replit/assets/replit-agent-home.webp</code></a></sub>

<img src="https://raw.githubusercontent.com/1weiho/open-slide/35dc46ca27716ea86f8a76710bbd3640e9590628/apps/web/public/assets/screenshots/assets-manager.webp" width="100%" alt="open-slide sample">

<sub><b>Assets Manager</b> · <a href="https://github.com/1weiho/open-slide/blob/35dc46ca27716ea86f8a76710bbd3640e9590628/apps/web/public/assets/screenshots/assets-manager.webp"><code>apps/web/public/assets/screenshots/assets-manager.webp</code></a></sub>

<img src="https://raw.githubusercontent.com/1weiho/open-slide/35dc46ca27716ea86f8a76710bbd3640e9590628/apps/web/public/assets/screenshots/inspector.webp" width="100%" alt="open-slide sample">

<sub><b>Inspector</b> · <a href="https://github.com/1weiho/open-slide/blob/35dc46ca27716ea86f8a76710bbd3640e9590628/apps/web/public/assets/screenshots/inspector.webp"><code>apps/web/public/assets/screenshots/inspector.webp</code></a></sub>

<img src="https://raw.githubusercontent.com/1weiho/open-slide/35dc46ca27716ea86f8a76710bbd3640e9590628/apps/web/public/assets/screenshots/presenter.webp" width="100%" alt="open-slide sample">

<sub><b>Presenter</b> · <a href="https://github.com/1weiho/open-slide/blob/35dc46ca27716ea86f8a76710bbd3640e9590628/apps/web/public/assets/screenshots/presenter.webp"><code>apps/web/public/assets/screenshots/presenter.webp</code></a></sub>

<img src="https://raw.githubusercontent.com/1weiho/open-slide/35dc46ca27716ea86f8a76710bbd3640e9590628/apps/web/public/assets/screenshots/theme.webp" width="100%" alt="open-slide sample">

<sub><b>Theme</b> · <a href="https://github.com/1weiho/open-slide/blob/35dc46ca27716ea86f8a76710bbd3640e9590628/apps/web/public/assets/screenshots/theme.webp"><code>apps/web/public/assets/screenshots/theme.webp</code></a></sub>

<img src="https://raw.githubusercontent.com/1weiho/open-slide/35dc46ca27716ea86f8a76710bbd3640e9590628/apps/web/public/assets/screenshots/svgl.webp" width="100%" alt="open-slide sample">

<sub><b>Svgl</b> · <a href="https://github.com/1weiho/open-slide/blob/35dc46ca27716ea86f8a76710bbd3640e9590628/apps/web/public/assets/screenshots/svgl.webp"><code>apps/web/public/assets/screenshots/svgl.webp</code></a></sub>

<img src="https://raw.githubusercontent.com/1weiho/open-slide/35dc46ca27716ea86f8a76710bbd3640e9590628/apps/web/public/assets/screenshots/open-slide-cover.webp" width="100%" alt="open-slide sample">

<sub><b>Open Slide</b> · cover · <a href="https://github.com/1weiho/open-slide/blob/35dc46ca27716ea86f8a76710bbd3640e9590628/apps/web/public/assets/screenshots/open-slide-cover.webp"><code>apps/web/public/assets/screenshots/open-slide-cover.webp</code></a></sub>

<img src="https://raw.githubusercontent.com/1weiho/open-slide/35dc46ca27716ea86f8a76710bbd3640e9590628/apps/demo/slides/open-slide-on-replit/assets/replit-deploy.webp" width="100%" alt="open-slide sample">

<sub><b>Replit Deploy</b> · <a href="https://github.com/1weiho/open-slide/blob/35dc46ca27716ea86f8a76710bbd3640e9590628/apps/demo/slides/open-slide-on-replit/assets/replit-deploy.webp"><code>apps/demo/slides/open-slide-on-replit/assets/replit-deploy.webp</code></a></sub>

<img src="https://raw.githubusercontent.com/1weiho/open-slide/35dc46ca27716ea86f8a76710bbd3640e9590628/apps/demo/slides/open-slide-on-replit/assets/init-command.webp" width="100%" alt="open-slide sample">

<sub><b>Init Command</b> · <a href="https://github.com/1weiho/open-slide/blob/35dc46ca27716ea86f8a76710bbd3640e9590628/apps/demo/slides/open-slide-on-replit/assets/init-command.webp"><code>apps/demo/slides/open-slide-on-replit/assets/init-command.webp</code></a></sub>

<img src="https://raw.githubusercontent.com/1weiho/open-slide/35dc46ca27716ea86f8a76710bbd3640e9590628/apps/demo/slides/open-slide-launch/assets/open-slide.png" width="100%" alt="open-slide sample">

<sub><b>Open Slide</b> · <a href="https://github.com/1weiho/open-slide/blob/35dc46ca27716ea86f8a76710bbd3640e9590628/apps/demo/slides/open-slide-launch/assets/open-slide.png"><code>apps/demo/slides/open-slide-launch/assets/open-slide.png</code></a></sub>

<img src="https://raw.githubusercontent.com/1weiho/open-slide/35dc46ca27716ea86f8a76710bbd3640e9590628/apps/web/public/open-slide.png" width="100%" alt="open-slide sample">

<sub><b>Open Slide</b> · <a href="https://github.com/1weiho/open-slide/blob/35dc46ca27716ea86f8a76710bbd3640e9590628/apps/web/public/open-slide.png"><code>apps/web/public/open-slide.png</code></a></sub>

<img src="https://raw.githubusercontent.com/1weiho/open-slide/35dc46ca27716ea86f8a76710bbd3640e9590628/apps/web/app/opengraph-image.png" width="100%" alt="open-slide sample">

<sub><b>Opengraph Image</b> · <a href="https://github.com/1weiho/open-slide/blob/35dc46ca27716ea86f8a76710bbd3640e9590628/apps/web/app/opengraph-image.png"><code>apps/web/app/opengraph-image.png</code></a></sub>

<a id="gallery-beautiful-html-templates"></a>

#### [Beautiful HTML Templates](https://github.com/zarazhangrui/beautiful-html-templates) · 3,918 ⭐ · Templates

<sub>34 HTML slide templates with index.json metadata so any agent can pick the right one.</sub>

<sub>24 of 102 images in [`zarazhangrui/beautiful-html-templates`](https://github.com/zarazhangrui/beautiful-html-templates) · the leading frames are the ones the project puts in its own README</sub>

```bash
git clone https://github.com/zarazhangrui/beautiful-html-templates
```

<sub><b>Styles below</b> `soft-editorial` · `editorial-forest` · `pin-and-paper` · `sakura-chroma` · `stencil-tablet` · `cobalt-grid` · `vellum` · `emerald-editorial` — name one when you ask for a deck. These are the project's own strings, taken from the filenames and captions linked under each image, not names this registry made up.</sub>

<img src="https://raw.githubusercontent.com/zarazhangrui/beautiful-html-templates/e5e204fb1f3b06290846e7dcd7aceddabeceec8c/screenshots/soft-editorial-4.png" width="100%" alt="Soft Editorial — slide 4">

<sub><b>Soft Editorial — slide 4</b> · <a href="https://github.com/zarazhangrui/beautiful-html-templates/blob/e5e204fb1f3b06290846e7dcd7aceddabeceec8c/screenshots/soft-editorial-4.png"><code>screenshots/soft-editorial-4.png</code></a></sub>

<img src="https://raw.githubusercontent.com/zarazhangrui/beautiful-html-templates/e5e204fb1f3b06290846e7dcd7aceddabeceec8c/screenshots/soft-editorial-6.png" width="100%" alt="Soft Editorial — slide 6">

<sub><b>Soft Editorial — slide 6</b> · <a href="https://github.com/zarazhangrui/beautiful-html-templates/blob/e5e204fb1f3b06290846e7dcd7aceddabeceec8c/screenshots/soft-editorial-6.png"><code>screenshots/soft-editorial-6.png</code></a></sub>

<img src="https://raw.githubusercontent.com/zarazhangrui/beautiful-html-templates/e5e204fb1f3b06290846e7dcd7aceddabeceec8c/screenshots/soft-editorial-10.png" width="100%" alt="Soft Editorial — slide 10">

<sub><b>Soft Editorial — slide 10</b> · <a href="https://github.com/zarazhangrui/beautiful-html-templates/blob/e5e204fb1f3b06290846e7dcd7aceddabeceec8c/screenshots/soft-editorial-10.png"><code>screenshots/soft-editorial-10.png</code></a></sub>

<img src="https://raw.githubusercontent.com/zarazhangrui/beautiful-html-templates/e5e204fb1f3b06290846e7dcd7aceddabeceec8c/screenshots/editorial-forest-1.png" width="100%" alt="Editorial Forest — slide 1">

<sub><b>Editorial Forest — slide 1</b> · <a href="https://github.com/zarazhangrui/beautiful-html-templates/blob/e5e204fb1f3b06290846e7dcd7aceddabeceec8c/screenshots/editorial-forest-1.png"><code>screenshots/editorial-forest-1.png</code></a></sub>

<img src="https://raw.githubusercontent.com/zarazhangrui/beautiful-html-templates/e5e204fb1f3b06290846e7dcd7aceddabeceec8c/screenshots/editorial-forest-2.png" width="100%" alt="Editorial Forest — slide 2">

<sub><b>Editorial Forest — slide 2</b> · <a href="https://github.com/zarazhangrui/beautiful-html-templates/blob/e5e204fb1f3b06290846e7dcd7aceddabeceec8c/screenshots/editorial-forest-2.png"><code>screenshots/editorial-forest-2.png</code></a></sub>

<img src="https://raw.githubusercontent.com/zarazhangrui/beautiful-html-templates/e5e204fb1f3b06290846e7dcd7aceddabeceec8c/screenshots/editorial-forest-5.png" width="100%" alt="Editorial Forest — slide 5">

<sub><b>Editorial Forest — slide 5</b> · <a href="https://github.com/zarazhangrui/beautiful-html-templates/blob/e5e204fb1f3b06290846e7dcd7aceddabeceec8c/screenshots/editorial-forest-5.png"><code>screenshots/editorial-forest-5.png</code></a></sub>

<img src="https://raw.githubusercontent.com/zarazhangrui/beautiful-html-templates/e5e204fb1f3b06290846e7dcd7aceddabeceec8c/screenshots/pin-and-paper-1.png" width="100%" alt="Pin & Paper — slide 1">

<sub><b>Pin & Paper — slide 1</b> · <code>pin-and-paper</code> · <a href="https://github.com/zarazhangrui/beautiful-html-templates/blob/e5e204fb1f3b06290846e7dcd7aceddabeceec8c/screenshots/pin-and-paper-1.png"><code>screenshots/pin-and-paper-1.png</code></a></sub>

<img src="https://raw.githubusercontent.com/zarazhangrui/beautiful-html-templates/e5e204fb1f3b06290846e7dcd7aceddabeceec8c/screenshots/pin-and-paper-11.png" width="100%" alt="Pin & Paper — slide 11">

<sub><b>Pin & Paper — slide 11</b> · <code>pin-and-paper</code> · <a href="https://github.com/zarazhangrui/beautiful-html-templates/blob/e5e204fb1f3b06290846e7dcd7aceddabeceec8c/screenshots/pin-and-paper-11.png"><code>screenshots/pin-and-paper-11.png</code></a></sub>

<img src="https://raw.githubusercontent.com/zarazhangrui/beautiful-html-templates/e5e204fb1f3b06290846e7dcd7aceddabeceec8c/screenshots/pin-and-paper-3.png" width="100%" alt="Pin & Paper — slide 3">

<sub><b>Pin & Paper — slide 3</b> · <code>pin-and-paper</code> · <a href="https://github.com/zarazhangrui/beautiful-html-templates/blob/e5e204fb1f3b06290846e7dcd7aceddabeceec8c/screenshots/pin-and-paper-3.png"><code>screenshots/pin-and-paper-3.png</code></a></sub>

<img src="https://raw.githubusercontent.com/zarazhangrui/beautiful-html-templates/e5e204fb1f3b06290846e7dcd7aceddabeceec8c/screenshots/sakura-chroma-1.png" width="100%" alt="Sakura Chroma — slide 1">

<sub><b>Sakura Chroma — slide 1</b> · <a href="https://github.com/zarazhangrui/beautiful-html-templates/blob/e5e204fb1f3b06290846e7dcd7aceddabeceec8c/screenshots/sakura-chroma-1.png"><code>screenshots/sakura-chroma-1.png</code></a></sub>

<img src="https://raw.githubusercontent.com/zarazhangrui/beautiful-html-templates/e5e204fb1f3b06290846e7dcd7aceddabeceec8c/screenshots/sakura-chroma-3.png" width="100%" alt="Sakura Chroma — slide 3">

<sub><b>Sakura Chroma — slide 3</b> · <a href="https://github.com/zarazhangrui/beautiful-html-templates/blob/e5e204fb1f3b06290846e7dcd7aceddabeceec8c/screenshots/sakura-chroma-3.png"><code>screenshots/sakura-chroma-3.png</code></a></sub>

<img src="https://raw.githubusercontent.com/zarazhangrui/beautiful-html-templates/e5e204fb1f3b06290846e7dcd7aceddabeceec8c/screenshots/sakura-chroma-4.png" width="100%" alt="Sakura Chroma — slide 4">

<sub><b>Sakura Chroma — slide 4</b> · <a href="https://github.com/zarazhangrui/beautiful-html-templates/blob/e5e204fb1f3b06290846e7dcd7aceddabeceec8c/screenshots/sakura-chroma-4.png"><code>screenshots/sakura-chroma-4.png</code></a></sub>

<img src="https://raw.githubusercontent.com/zarazhangrui/beautiful-html-templates/e5e204fb1f3b06290846e7dcd7aceddabeceec8c/screenshots/stencil-tablet-1.png" width="100%" alt="Stencil & Tablet — slide 1">

<sub><b>Stencil & Tablet — slide 1</b> · <code>stencil-tablet</code> · <a href="https://github.com/zarazhangrui/beautiful-html-templates/blob/e5e204fb1f3b06290846e7dcd7aceddabeceec8c/screenshots/stencil-tablet-1.png"><code>screenshots/stencil-tablet-1.png</code></a></sub>

<img src="https://raw.githubusercontent.com/zarazhangrui/beautiful-html-templates/e5e204fb1f3b06290846e7dcd7aceddabeceec8c/screenshots/stencil-tablet-3.png" width="100%" alt="Stencil & Tablet — slide 3">

<sub><b>Stencil & Tablet — slide 3</b> · <code>stencil-tablet</code> · <a href="https://github.com/zarazhangrui/beautiful-html-templates/blob/e5e204fb1f3b06290846e7dcd7aceddabeceec8c/screenshots/stencil-tablet-3.png"><code>screenshots/stencil-tablet-3.png</code></a></sub>

<img src="https://raw.githubusercontent.com/zarazhangrui/beautiful-html-templates/e5e204fb1f3b06290846e7dcd7aceddabeceec8c/screenshots/stencil-tablet-8.png" width="100%" alt="Stencil & Tablet — slide 8">

<sub><b>Stencil & Tablet — slide 8</b> · <code>stencil-tablet</code> · <a href="https://github.com/zarazhangrui/beautiful-html-templates/blob/e5e204fb1f3b06290846e7dcd7aceddabeceec8c/screenshots/stencil-tablet-8.png"><code>screenshots/stencil-tablet-8.png</code></a></sub>

<img src="https://raw.githubusercontent.com/zarazhangrui/beautiful-html-templates/e5e204fb1f3b06290846e7dcd7aceddabeceec8c/screenshots/cobalt-grid-1.png" width="100%" alt="Cobalt Grid — slide 1">

<sub><b>Cobalt Grid — slide 1</b> · <a href="https://github.com/zarazhangrui/beautiful-html-templates/blob/e5e204fb1f3b06290846e7dcd7aceddabeceec8c/screenshots/cobalt-grid-1.png"><code>screenshots/cobalt-grid-1.png</code></a></sub>

<img src="https://raw.githubusercontent.com/zarazhangrui/beautiful-html-templates/e5e204fb1f3b06290846e7dcd7aceddabeceec8c/screenshots/cobalt-grid-3.png" width="100%" alt="Cobalt Grid — slide 3">

<sub><b>Cobalt Grid — slide 3</b> · <a href="https://github.com/zarazhangrui/beautiful-html-templates/blob/e5e204fb1f3b06290846e7dcd7aceddabeceec8c/screenshots/cobalt-grid-3.png"><code>screenshots/cobalt-grid-3.png</code></a></sub>

<img src="https://raw.githubusercontent.com/zarazhangrui/beautiful-html-templates/e5e204fb1f3b06290846e7dcd7aceddabeceec8c/screenshots/cobalt-grid-5.png" width="100%" alt="Cobalt Grid — slide 5">

<sub><b>Cobalt Grid — slide 5</b> · <a href="https://github.com/zarazhangrui/beautiful-html-templates/blob/e5e204fb1f3b06290846e7dcd7aceddabeceec8c/screenshots/cobalt-grid-5.png"><code>screenshots/cobalt-grid-5.png</code></a></sub>

<img src="https://raw.githubusercontent.com/zarazhangrui/beautiful-html-templates/e5e204fb1f3b06290846e7dcd7aceddabeceec8c/screenshots/vellum-1.png" width="100%" alt="Vellum — slide 1">

<sub><b>Vellum — slide 1</b> · <a href="https://github.com/zarazhangrui/beautiful-html-templates/blob/e5e204fb1f3b06290846e7dcd7aceddabeceec8c/screenshots/vellum-1.png"><code>screenshots/vellum-1.png</code></a></sub>

<img src="https://raw.githubusercontent.com/zarazhangrui/beautiful-html-templates/e5e204fb1f3b06290846e7dcd7aceddabeceec8c/screenshots/vellum-4.png" width="100%" alt="Vellum — slide 4">

<sub><b>Vellum — slide 4</b> · <a href="https://github.com/zarazhangrui/beautiful-html-templates/blob/e5e204fb1f3b06290846e7dcd7aceddabeceec8c/screenshots/vellum-4.png"><code>screenshots/vellum-4.png</code></a></sub>

<img src="https://raw.githubusercontent.com/zarazhangrui/beautiful-html-templates/e5e204fb1f3b06290846e7dcd7aceddabeceec8c/screenshots/vellum-8.png" width="100%" alt="Vellum — slide 8">

<sub><b>Vellum — slide 8</b> · <a href="https://github.com/zarazhangrui/beautiful-html-templates/blob/e5e204fb1f3b06290846e7dcd7aceddabeceec8c/screenshots/vellum-8.png"><code>screenshots/vellum-8.png</code></a></sub>

<img src="https://raw.githubusercontent.com/zarazhangrui/beautiful-html-templates/e5e204fb1f3b06290846e7dcd7aceddabeceec8c/screenshots/emerald-editorial-1.png" width="100%" alt="Emerald Editorial — slide 1">

<sub><b>Emerald Editorial — slide 1</b> · <a href="https://github.com/zarazhangrui/beautiful-html-templates/blob/e5e204fb1f3b06290846e7dcd7aceddabeceec8c/screenshots/emerald-editorial-1.png"><code>screenshots/emerald-editorial-1.png</code></a></sub>

<img src="https://raw.githubusercontent.com/zarazhangrui/beautiful-html-templates/e5e204fb1f3b06290846e7dcd7aceddabeceec8c/screenshots/emerald-editorial-3.png" width="100%" alt="Emerald Editorial — slide 3">

<sub><b>Emerald Editorial — slide 3</b> · <a href="https://github.com/zarazhangrui/beautiful-html-templates/blob/e5e204fb1f3b06290846e7dcd7aceddabeceec8c/screenshots/emerald-editorial-3.png"><code>screenshots/emerald-editorial-3.png</code></a></sub>

<img src="https://raw.githubusercontent.com/zarazhangrui/beautiful-html-templates/e5e204fb1f3b06290846e7dcd7aceddabeceec8c/screenshots/emerald-editorial-6.png" width="100%" alt="Emerald Editorial — slide 6">

<sub><b>Emerald Editorial — slide 6</b> · <a href="https://github.com/zarazhangrui/beautiful-html-templates/blob/e5e204fb1f3b06290846e7dcd7aceddabeceec8c/screenshots/emerald-editorial-6.png"><code>screenshots/emerald-editorial-6.png</code></a></sub>

<a id="gallery-ppt-agent-workflow-san"></a>

#### [PPT Agent Workflow San](https://github.com/mucsbr/ppt-agent-workflow-san) · 617 ⭐ · HTML

<sub>Progressive, interactive deck generation.</sub>

<sub>10 of 10 images in [`mucsbr/ppt-agent-workflow-san`](https://github.com/mucsbr/ppt-agent-workflow-san) · the leading frames are the ones the project puts in its own README</sub>

```bash
git clone https://github.com/mucsbr/ppt-agent-workflow-san
```

<sub><b>Styles below</b> `html-slide-to-pptx-preview` · `ppt-workflow-preview` · `ppt-workflow` · `02-core-conclusion` · `03-positioning` · `04-users-scenarios` · `05-growth-flywheel` · `06-competition` · `07-risks` · `08-conclusion` — name one when you ask for a deck. These are the project's own strings, taken from the filenames and captions linked under each image, not names this registry made up.</sub>

<img src="https://raw.githubusercontent.com/mucsbr/ppt-agent-workflow-san/801cd2bd46c3cc4ca2c846ff28da2d9284816cd9/2.png" width="100%" alt="html-slide-to-pptx-preview">

<sub><b>html-slide-to-pptx-preview</b> · <a href="https://github.com/mucsbr/ppt-agent-workflow-san/blob/801cd2bd46c3cc4ca2c846ff28da2d9284816cd9/2.png"><code>2.png</code></a></sub>

<img src="https://raw.githubusercontent.com/mucsbr/ppt-agent-workflow-san/801cd2bd46c3cc4ca2c846ff28da2d9284816cd9/1.png" width="100%" alt="ppt-workflow-preview">

<sub><b>ppt-workflow-preview</b> · <a href="https://github.com/mucsbr/ppt-agent-workflow-san/blob/801cd2bd46c3cc4ca2c846ff28da2d9284816cd9/1.png"><code>1.png</code></a></sub>

<img src="https://raw.githubusercontent.com/mucsbr/ppt-agent-workflow-san/801cd2bd46c3cc4ca2c846ff28da2d9284816cd9/ppt-workflow/01-cover.png" width="100%" alt="PPT Agent Workflow San sample">

<sub><b>Ppt Workflow</b> · cover · <a href="https://github.com/mucsbr/ppt-agent-workflow-san/blob/801cd2bd46c3cc4ca2c846ff28da2d9284816cd9/ppt-workflow/01-cover.png"><code>ppt-workflow/01-cover.png</code></a></sub>

<img src="https://raw.githubusercontent.com/mucsbr/ppt-agent-workflow-san/801cd2bd46c3cc4ca2c846ff28da2d9284816cd9/ppt-workflow/02-core-conclusion.png" width="100%" alt="PPT Agent Workflow San sample">

<sub><b>02 Core Conclusion</b> · <a href="https://github.com/mucsbr/ppt-agent-workflow-san/blob/801cd2bd46c3cc4ca2c846ff28da2d9284816cd9/ppt-workflow/02-core-conclusion.png"><code>ppt-workflow/02-core-conclusion.png</code></a></sub>

<img src="https://raw.githubusercontent.com/mucsbr/ppt-agent-workflow-san/801cd2bd46c3cc4ca2c846ff28da2d9284816cd9/ppt-workflow/03-positioning.png" width="100%" alt="PPT Agent Workflow San sample">

<sub><b>03 Positioning</b> · <a href="https://github.com/mucsbr/ppt-agent-workflow-san/blob/801cd2bd46c3cc4ca2c846ff28da2d9284816cd9/ppt-workflow/03-positioning.png"><code>ppt-workflow/03-positioning.png</code></a></sub>

<img src="https://raw.githubusercontent.com/mucsbr/ppt-agent-workflow-san/801cd2bd46c3cc4ca2c846ff28da2d9284816cd9/ppt-workflow/04-users-scenarios.png" width="100%" alt="PPT Agent Workflow San sample">

<sub><b>04 Users Scenarios</b> · <a href="https://github.com/mucsbr/ppt-agent-workflow-san/blob/801cd2bd46c3cc4ca2c846ff28da2d9284816cd9/ppt-workflow/04-users-scenarios.png"><code>ppt-workflow/04-users-scenarios.png</code></a></sub>

<img src="https://raw.githubusercontent.com/mucsbr/ppt-agent-workflow-san/801cd2bd46c3cc4ca2c846ff28da2d9284816cd9/ppt-workflow/05-growth-flywheel.png" width="100%" alt="PPT Agent Workflow San sample">

<sub><b>05 Growth Flywheel</b> · <a href="https://github.com/mucsbr/ppt-agent-workflow-san/blob/801cd2bd46c3cc4ca2c846ff28da2d9284816cd9/ppt-workflow/05-growth-flywheel.png"><code>ppt-workflow/05-growth-flywheel.png</code></a></sub>

<img src="https://raw.githubusercontent.com/mucsbr/ppt-agent-workflow-san/801cd2bd46c3cc4ca2c846ff28da2d9284816cd9/ppt-workflow/06-competition.png" width="100%" alt="PPT Agent Workflow San sample">

<sub><b>06 Competition</b> · <a href="https://github.com/mucsbr/ppt-agent-workflow-san/blob/801cd2bd46c3cc4ca2c846ff28da2d9284816cd9/ppt-workflow/06-competition.png"><code>ppt-workflow/06-competition.png</code></a></sub>

<img src="https://raw.githubusercontent.com/mucsbr/ppt-agent-workflow-san/801cd2bd46c3cc4ca2c846ff28da2d9284816cd9/ppt-workflow/07-risks.png" width="100%" alt="PPT Agent Workflow San sample">

<sub><b>07 Risks</b> · <a href="https://github.com/mucsbr/ppt-agent-workflow-san/blob/801cd2bd46c3cc4ca2c846ff28da2d9284816cd9/ppt-workflow/07-risks.png"><code>ppt-workflow/07-risks.png</code></a></sub>

<img src="https://raw.githubusercontent.com/mucsbr/ppt-agent-workflow-san/801cd2bd46c3cc4ca2c846ff28da2d9284816cd9/ppt-workflow/08-conclusion.png" width="100%" alt="PPT Agent Workflow San sample">

<sub><b>08 Conclusion</b> · <a href="https://github.com/mucsbr/ppt-agent-workflow-san/blob/801cd2bd46c3cc4ca2c846ff28da2d9284816cd9/ppt-workflow/08-conclusion.png"><code>ppt-workflow/08-conclusion.png</code></a></sub>

<a id="gallery-frontend-slides-editable"></a>

#### [Frontend Slides Editable](https://github.com/archlizheng/frontend-slides-editable) · 445 ⭐ · Both

<sub>Editable HTML decks with drag-resize, reordering, local save and PPTX conversion.</sub>

<sub>24 of 114 images in [`archlizheng/frontend-slides-editable`](https://github.com/archlizheng/frontend-slides-editable) · the leading frames are the ones the project puts in its own README</sub>

```bash
git clone https://github.com/archlizheng/frontend-slides-editable
```

<sub><b>Styles below</b> `cobalt-grid` · `studio-volt` · `soft-editorial` · `bold-signal` · `electric-studio` · `creative-voltage` · `dark-botanical` · `notebook-tabs` · `pastel-geometry` · `split-pastel` · `vintage-editorial` · `neon-cyber` — name one when you ask for a deck. These are the project's own strings, taken from the filenames and captions linked under each image, not names this registry made up.</sub>

<img src="https://raw.githubusercontent.com/archlizheng/frontend-slides-editable/e5663e6a0bdc2c2a673198bab3fb61036a7f20ee/docs/preset-previews/cobalt-grid-cover.png" width="100%" alt="Cobalt Grid editable deck preview">

<sub><b>Cobalt Grid editable deck preview</b> · cover · <a href="https://github.com/archlizheng/frontend-slides-editable/blob/e5663e6a0bdc2c2a673198bab3fb61036a7f20ee/docs/preset-previews/cobalt-grid-cover.png"><code>docs/preset-previews/cobalt-grid-cover.png</code></a></sub>

<img src="https://raw.githubusercontent.com/archlizheng/frontend-slides-editable/e5663e6a0bdc2c2a673198bab3fb61036a7f20ee/docs/preset-previews/studio-volt-cover.png" width="100%" alt="Studio editable deck preview">

<sub><b>Studio editable deck preview</b> · <code>studio-volt</code> · cover · <a href="https://github.com/archlizheng/frontend-slides-editable/blob/e5663e6a0bdc2c2a673198bab3fb61036a7f20ee/docs/preset-previews/studio-volt-cover.png"><code>docs/preset-previews/studio-volt-cover.png</code></a></sub>

<img src="https://raw.githubusercontent.com/archlizheng/frontend-slides-editable/e5663e6a0bdc2c2a673198bab3fb61036a7f20ee/docs/preset-previews/soft-editorial-cover.png" width="100%" alt="Soft Editorial editable deck preview">

<sub><b>Soft Editorial editable deck preview</b> · cover · <a href="https://github.com/archlizheng/frontend-slides-editable/blob/e5663e6a0bdc2c2a673198bab3fb61036a7f20ee/docs/preset-previews/soft-editorial-cover.png"><code>docs/preset-previews/soft-editorial-cover.png</code></a></sub>

<img src="https://raw.githubusercontent.com/archlizheng/frontend-slides-editable/e5663e6a0bdc2c2a673198bab3fb61036a7f20ee/docs/preset-previews/bold-signal-cover.png" width="100%" alt="Bold Signal — first slide">

<sub><b>Bold Signal — first slide</b> · cover · <a href="https://github.com/archlizheng/frontend-slides-editable/blob/e5663e6a0bdc2c2a673198bab3fb61036a7f20ee/docs/preset-previews/bold-signal-cover.png"><code>docs/preset-previews/bold-signal-cover.png</code></a></sub>

<img src="https://raw.githubusercontent.com/archlizheng/frontend-slides-editable/e5663e6a0bdc2c2a673198bab3fb61036a7f20ee/docs/preset-previews/electric-studio-cover.png" width="100%" alt="Electric Studio — first slide">

<sub><b>Electric Studio — first slide</b> · cover · <a href="https://github.com/archlizheng/frontend-slides-editable/blob/e5663e6a0bdc2c2a673198bab3fb61036a7f20ee/docs/preset-previews/electric-studio-cover.png"><code>docs/preset-previews/electric-studio-cover.png</code></a></sub>

<img src="https://raw.githubusercontent.com/archlizheng/frontend-slides-editable/e5663e6a0bdc2c2a673198bab3fb61036a7f20ee/docs/preset-previews/creative-voltage-cover.png" width="100%" alt="Creative Voltage — first slide">

<sub><b>Creative Voltage — first slide</b> · cover · <a href="https://github.com/archlizheng/frontend-slides-editable/blob/e5663e6a0bdc2c2a673198bab3fb61036a7f20ee/docs/preset-previews/creative-voltage-cover.png"><code>docs/preset-previews/creative-voltage-cover.png</code></a></sub>

<img src="https://raw.githubusercontent.com/archlizheng/frontend-slides-editable/e5663e6a0bdc2c2a673198bab3fb61036a7f20ee/docs/preset-previews/dark-botanical-cover.png" width="100%" alt="Dark Botanical — first slide">

<sub><b>Dark Botanical — first slide</b> · cover · <a href="https://github.com/archlizheng/frontend-slides-editable/blob/e5663e6a0bdc2c2a673198bab3fb61036a7f20ee/docs/preset-previews/dark-botanical-cover.png"><code>docs/preset-previews/dark-botanical-cover.png</code></a></sub>

<img src="https://raw.githubusercontent.com/archlizheng/frontend-slides-editable/e5663e6a0bdc2c2a673198bab3fb61036a7f20ee/docs/preset-previews/notebook-tabs-cover.png" width="100%" alt="Notebook Tabs — first slide">

<sub><b>Notebook Tabs — first slide</b> · cover · <a href="https://github.com/archlizheng/frontend-slides-editable/blob/e5663e6a0bdc2c2a673198bab3fb61036a7f20ee/docs/preset-previews/notebook-tabs-cover.png"><code>docs/preset-previews/notebook-tabs-cover.png</code></a></sub>

<img src="https://raw.githubusercontent.com/archlizheng/frontend-slides-editable/e5663e6a0bdc2c2a673198bab3fb61036a7f20ee/docs/preset-previews/pastel-geometry-cover.png" width="100%" alt="Pastel Geometry — first slide">

<sub><b>Pastel Geometry — first slide</b> · cover · <a href="https://github.com/archlizheng/frontend-slides-editable/blob/e5663e6a0bdc2c2a673198bab3fb61036a7f20ee/docs/preset-previews/pastel-geometry-cover.png"><code>docs/preset-previews/pastel-geometry-cover.png</code></a></sub>

<img src="https://raw.githubusercontent.com/archlizheng/frontend-slides-editable/e5663e6a0bdc2c2a673198bab3fb61036a7f20ee/docs/preset-previews/split-pastel-cover.png" width="100%" alt="Split Pastel — first slide">

<sub><b>Split Pastel — first slide</b> · cover · <a href="https://github.com/archlizheng/frontend-slides-editable/blob/e5663e6a0bdc2c2a673198bab3fb61036a7f20ee/docs/preset-previews/split-pastel-cover.png"><code>docs/preset-previews/split-pastel-cover.png</code></a></sub>

<img src="https://raw.githubusercontent.com/archlizheng/frontend-slides-editable/e5663e6a0bdc2c2a673198bab3fb61036a7f20ee/docs/preset-previews/vintage-editorial-cover.png" width="100%" alt="Vintage Editorial — first slide">

<sub><b>Vintage Editorial — first slide</b> · cover · <a href="https://github.com/archlizheng/frontend-slides-editable/blob/e5663e6a0bdc2c2a673198bab3fb61036a7f20ee/docs/preset-previews/vintage-editorial-cover.png"><code>docs/preset-previews/vintage-editorial-cover.png</code></a></sub>

<img src="https://raw.githubusercontent.com/archlizheng/frontend-slides-editable/e5663e6a0bdc2c2a673198bab3fb61036a7f20ee/docs/preset-previews/neon-cyber-cover.png" width="100%" alt="Neon Cyber — first slide">

<sub><b>Neon Cyber — first slide</b> · cover · <a href="https://github.com/archlizheng/frontend-slides-editable/blob/e5663e6a0bdc2c2a673198bab3fb61036a7f20ee/docs/preset-previews/neon-cyber-cover.png"><code>docs/preset-previews/neon-cyber-cover.png</code></a></sub>

<img src="https://raw.githubusercontent.com/archlizheng/frontend-slides-editable/e5663e6a0bdc2c2a673198bab3fb61036a7f20ee/docs/preset-previews/terminal-green-cover.png" width="100%" alt="Terminal Green — first slide">

<sub><b>Terminal Green — first slide</b> · cover · <a href="https://github.com/archlizheng/frontend-slides-editable/blob/e5663e6a0bdc2c2a673198bab3fb61036a7f20ee/docs/preset-previews/terminal-green-cover.png"><code>docs/preset-previews/terminal-green-cover.png</code></a></sub>

<img src="https://raw.githubusercontent.com/archlizheng/frontend-slides-editable/e5663e6a0bdc2c2a673198bab3fb61036a7f20ee/docs/preset-previews/swiss-modern-cover.png" width="100%" alt="Swiss Modern — first slide">

<sub><b>Swiss Modern — first slide</b> · cover · <a href="https://github.com/archlizheng/frontend-slides-editable/blob/e5663e6a0bdc2c2a673198bab3fb61036a7f20ee/docs/preset-previews/swiss-modern-cover.png"><code>docs/preset-previews/swiss-modern-cover.png</code></a></sub>

<img src="https://raw.githubusercontent.com/archlizheng/frontend-slides-editable/e5663e6a0bdc2c2a673198bab3fb61036a7f20ee/docs/preset-previews/paper-ink-cover.png" width="100%" alt="Paper and Ink — first slide">

<sub><b>Paper and Ink — first slide</b> · <code>paper-ink</code> · cover · <a href="https://github.com/archlizheng/frontend-slides-editable/blob/e5663e6a0bdc2c2a673198bab3fb61036a7f20ee/docs/preset-previews/paper-ink-cover.png"><code>docs/preset-previews/paper-ink-cover.png</code></a></sub>

<img src="https://raw.githubusercontent.com/archlizheng/frontend-slides-editable/e5663e6a0bdc2c2a673198bab3fb61036a7f20ee/docs/preset-previews/8-bit-orbit-cover.png" width="100%" alt="8-Bit Orbit — cover slide">

<sub><b>8-Bit Orbit — cover slide</b> · cover · <a href="https://github.com/archlizheng/frontend-slides-editable/blob/e5663e6a0bdc2c2a673198bab3fb61036a7f20ee/docs/preset-previews/8-bit-orbit-cover.png"><code>docs/preset-previews/8-bit-orbit-cover.png</code></a></sub>

<img src="https://raw.githubusercontent.com/archlizheng/frontend-slides-editable/e5663e6a0bdc2c2a673198bab3fb61036a7f20ee/docs/preset-previews/8-bit-orbit-mid.png" width="100%" alt="8-Bit Orbit — mid slide">

<sub><b>8-Bit Orbit — mid slide</b> · <code>8-bit-orbit-mid</code> · <a href="https://github.com/archlizheng/frontend-slides-editable/blob/e5663e6a0bdc2c2a673198bab3fb61036a7f20ee/docs/preset-previews/8-bit-orbit-mid.png"><code>docs/preset-previews/8-bit-orbit-mid.png</code></a></sub>

<img src="https://raw.githubusercontent.com/archlizheng/frontend-slides-editable/e5663e6a0bdc2c2a673198bab3fb61036a7f20ee/docs/preset-previews/8-bit-orbit-later.png" width="100%" alt="8-Bit Orbit — later slide">

<sub><b>8-Bit Orbit — later slide</b> · <code>8-bit-orbit-later</code> · <a href="https://github.com/archlizheng/frontend-slides-editable/blob/e5663e6a0bdc2c2a673198bab3fb61036a7f20ee/docs/preset-previews/8-bit-orbit-later.png"><code>docs/preset-previews/8-bit-orbit-later.png</code></a></sub>

<img src="https://raw.githubusercontent.com/archlizheng/frontend-slides-editable/e5663e6a0bdc2c2a673198bab3fb61036a7f20ee/docs/preset-previews/biennale-yellow-cover.png" width="100%" alt="Biennale Yellow — cover slide">

<sub><b>Biennale Yellow — cover slide</b> · cover · <a href="https://github.com/archlizheng/frontend-slides-editable/blob/e5663e6a0bdc2c2a673198bab3fb61036a7f20ee/docs/preset-previews/biennale-yellow-cover.png"><code>docs/preset-previews/biennale-yellow-cover.png</code></a></sub>

<img src="https://raw.githubusercontent.com/archlizheng/frontend-slides-editable/e5663e6a0bdc2c2a673198bab3fb61036a7f20ee/docs/preset-previews/biennale-yellow-mid.png" width="100%" alt="Biennale Yellow — mid slide">

<sub><b>Biennale Yellow — mid slide</b> · <code>biennale-yellow-mid</code> · <a href="https://github.com/archlizheng/frontend-slides-editable/blob/e5663e6a0bdc2c2a673198bab3fb61036a7f20ee/docs/preset-previews/biennale-yellow-mid.png"><code>docs/preset-previews/biennale-yellow-mid.png</code></a></sub>

<img src="https://raw.githubusercontent.com/archlizheng/frontend-slides-editable/e5663e6a0bdc2c2a673198bab3fb61036a7f20ee/docs/preset-previews/biennale-yellow-later.png" width="100%" alt="Biennale Yellow — later slide">

<sub><b>Biennale Yellow — later slide</b> · <code>biennale-yellow-later</code> · <a href="https://github.com/archlizheng/frontend-slides-editable/blob/e5663e6a0bdc2c2a673198bab3fb61036a7f20ee/docs/preset-previews/biennale-yellow-later.png"><code>docs/preset-previews/biennale-yellow-later.png</code></a></sub>

<img src="https://raw.githubusercontent.com/archlizheng/frontend-slides-editable/e5663e6a0bdc2c2a673198bab3fb61036a7f20ee/docs/preset-previews/block-frame-cover.png" width="100%" alt="BlockFrame — cover slide">

<sub><b>BlockFrame — cover slide</b> · <code>block-frame</code> · cover · <a href="https://github.com/archlizheng/frontend-slides-editable/blob/e5663e6a0bdc2c2a673198bab3fb61036a7f20ee/docs/preset-previews/block-frame-cover.png"><code>docs/preset-previews/block-frame-cover.png</code></a></sub>

<img src="https://raw.githubusercontent.com/archlizheng/frontend-slides-editable/e5663e6a0bdc2c2a673198bab3fb61036a7f20ee/docs/preset-previews/block-frame-mid.png" width="100%" alt="BlockFrame — mid slide">

<sub><b>BlockFrame — mid slide</b> · <code>block-frame-mid</code> · <a href="https://github.com/archlizheng/frontend-slides-editable/blob/e5663e6a0bdc2c2a673198bab3fb61036a7f20ee/docs/preset-previews/block-frame-mid.png"><code>docs/preset-previews/block-frame-mid.png</code></a></sub>

<img src="https://raw.githubusercontent.com/archlizheng/frontend-slides-editable/e5663e6a0bdc2c2a673198bab3fb61036a7f20ee/docs/preset-previews/block-frame-later.png" width="100%" alt="BlockFrame — later slide">

<sub><b>BlockFrame — later slide</b> · <code>block-frame-later</code> · <a href="https://github.com/archlizheng/frontend-slides-editable/blob/e5663e6a0bdc2c2a673198bab3fb61036a7f20ee/docs/preset-previews/block-frame-later.png"><code>docs/preset-previews/block-frame-later.png</code></a></sub>

<a id="gallery-ppt-svg-generator"></a>

#### [PPT SVG Generator](https://github.com/vigorX777/ppt-svg-generator) · 248 ⭐ · PPTX

<sub>Markdown to PPT or PDF via SVG, with preset styles.</sub>

<sub>2 of 2 images in [`vigorX777/ppt-svg-generator`](https://github.com/vigorX777/ppt-svg-generator) · the leading frames are the ones the project puts in its own README</sub>

```bash
git clone https://github.com/vigorX777/ppt-svg-generator
```

<img src="https://github.com/user-attachments/assets/2454e688-d3b8-40a2-a3f8-893bbe5060ee" width="100%" alt="image">

<sub><b>image</b> · GitHub attachment</sub>

<img src="https://github.com/user-attachments/assets/97847c7f-5dc3-4a39-b4d8-ee3dc7d0396b" width="100%" alt="PixPin_2026-01-25_15-58-40">

<sub><b>PixPin_2026-01-25_15-58-40</b> · GitHub attachment</sub>

<a id="gallery-mck-ppt-design-skill"></a>

#### [Mck PPT Design System](https://github.com/likaku/Mck-ppt-design-skill) · 229 ⭐ · PPTX

<sub>Consulting-firm-style design system: 70 layout patterns, flat design, python-pptx.</sub>

<sub>6 of 6 images in [`likaku/Mck-ppt-design-skill`](https://github.com/likaku/Mck-ppt-design-skill) · the leading frames are the ones the project puts in its own README</sub>

```bash
git clone https://github.com/likaku/Mck-ppt-design-skill
```

<img src="https://github.com/user-attachments/assets/075ec46d-dd73-4454-92d0-84184b78d276" width="100%" alt="Cover">

<sub><b>Cover</b> · GitHub attachment</sub>

<img src="https://github.com/user-attachments/assets/3b25f071-8a81-48e3-a62b-9d9be9026f2e" width="100%" alt="Content">

<sub><b>Content</b> · GitHub attachment</sub>

<img src="https://github.com/user-attachments/assets/be327c14-aff9-459f-89b0-d4a8bffaabfc" width="100%" alt="Table">

<sub><b>Table</b> · GitHub attachment</sub>

<img src="https://github.com/user-attachments/assets/687cee47-13bb-4d6b-840f-77f8e001a62b" width="100%" alt="4-Column">

<sub><b>4-Column</b> · GitHub attachment</sub>

<img src="https://github.com/user-attachments/assets/41371c47-608f-4857-9bfe-791121ec1579" width="100%" alt="Colors">

<sub><b>Colors</b> · GitHub attachment</sub>

<img src="https://github.com/user-attachments/assets/c5b6e52a-fd91-4c28-88a4-82fdfedfd956" width="100%" alt="Summary">

<sub><b>Summary</b> · GitHub attachment</sub>

<a id="gallery-ppt-agent-skill"></a>

#### [PPT Agent Skill](https://github.com/Akxan/ppt-agent-skill) · 114 ⭐ · HTML

<sub>26 styles and 18 chart types benchmarked against Linear, Anthropic, Stripe, Apple and NYT.</sub>

<sub>24 of 32 images in [`Akxan/ppt-agent-skill`](https://github.com/Akxan/ppt-agent-skill) · the leading frames are the ones the project puts in its own README</sub>

```bash
git clone https://github.com/Akxan/ppt-agent-skill
```

<sub><b>Styles below</b> `all` · `vibrant` · `natural-retro` · `dark-professional` · `light-premium` · `cultural-oriental` · `bauhaus-block` · `blue-white` · `botanic-forest` · `candy-pastel` · `champagne-gold` · `chrome-y2k` — name one when you ask for a deck. These are the project's own strings, taken from the filenames and captions linked under each image, not names this registry made up.</sub>

<img src="https://raw.githubusercontent.com/Akxan/ppt-agent-skill/01825dee2ad40a8c719824252605396b9a570d57/assets/hero-all.png" width="100%" alt="26 风格预览">

<sub><b>26 风格预览</b> · <code>all</code> · <a href="https://github.com/Akxan/ppt-agent-skill/blob/01825dee2ad40a8c719824252605396b9a570d57/assets/hero-all.png"><code>assets/hero-all.png</code></a></sub>

<img src="https://raw.githubusercontent.com/Akxan/ppt-agent-skill/01825dee2ad40a8c719824252605396b9a570d57/assets/hero-vibrant.png" width="100%" alt="活力鲜明 4 风格">

<sub><b>活力鲜明 4 风格</b> · <code>vibrant</code> · <a href="https://github.com/Akxan/ppt-agent-skill/blob/01825dee2ad40a8c719824252605396b9a570d57/assets/hero-vibrant.png"><code>assets/hero-vibrant.png</code></a></sub>

<img src="https://raw.githubusercontent.com/Akxan/ppt-agent-skill/01825dee2ad40a8c719824252605396b9a570d57/assets/hero-natural-retro.png" width="100%" alt="自然/复古 4 风格">

<sub><b>自然/复古 4 风格</b> · <code>natural-retro</code> · <a href="https://github.com/Akxan/ppt-agent-skill/blob/01825dee2ad40a8c719824252605396b9a570d57/assets/hero-natural-retro.png"><code>assets/hero-natural-retro.png</code></a></sub>

<img src="https://raw.githubusercontent.com/Akxan/ppt-agent-skill/01825dee2ad40a8c719824252605396b9a570d57/assets/hero-dark-professional.png" width="100%" alt="暗色专业 7 风格">

<sub><b>暗色专业 7 风格</b> · <code>dark-professional</code> · <a href="https://github.com/Akxan/ppt-agent-skill/blob/01825dee2ad40a8c719824252605396b9a570d57/assets/hero-dark-professional.png"><code>assets/hero-dark-professional.png</code></a></sub>

<img src="https://raw.githubusercontent.com/Akxan/ppt-agent-skill/01825dee2ad40a8c719824252605396b9a570d57/assets/hero-light-premium.png" width="100%" alt="浅色高级 8 风格">

<sub><b>浅色高级 8 风格</b> · <code>light-premium</code> · <a href="https://github.com/Akxan/ppt-agent-skill/blob/01825dee2ad40a8c719824252605396b9a570d57/assets/hero-light-premium.png"><code>assets/hero-light-premium.png</code></a></sub>

<img src="https://raw.githubusercontent.com/Akxan/ppt-agent-skill/01825dee2ad40a8c719824252605396b9a570d57/assets/hero-cultural-oriental.png" width="100%" alt="东方文化 3 风格">

<sub><b>东方文化 3 风格</b> · <code>cultural-oriental</code> · <a href="https://github.com/Akxan/ppt-agent-skill/blob/01825dee2ad40a8c719824252605396b9a570d57/assets/hero-cultural-oriental.png"><code>assets/hero-cultural-oriental.png</code></a></sub>

<img src="https://raw.githubusercontent.com/Akxan/ppt-agent-skill/01825dee2ad40a8c719824252605396b9a570d57/ppt-output/style-gallery/bauhaus_block.png" width="100%" alt="PPT Agent Skill sample">

<sub><b>Bauhaus Block</b> · <a href="https://github.com/Akxan/ppt-agent-skill/blob/01825dee2ad40a8c719824252605396b9a570d57/ppt-output/style-gallery/bauhaus_block.png"><code>ppt-output/style-gallery/bauhaus_block.png</code></a></sub>

<img src="https://raw.githubusercontent.com/Akxan/ppt-agent-skill/01825dee2ad40a8c719824252605396b9a570d57/ppt-output/style-gallery/blue_white.png" width="100%" alt="PPT Agent Skill sample">

<sub><b>Blue White</b> · <a href="https://github.com/Akxan/ppt-agent-skill/blob/01825dee2ad40a8c719824252605396b9a570d57/ppt-output/style-gallery/blue_white.png"><code>ppt-output/style-gallery/blue_white.png</code></a></sub>

<img src="https://raw.githubusercontent.com/Akxan/ppt-agent-skill/01825dee2ad40a8c719824252605396b9a570d57/ppt-output/style-gallery/botanic_forest.png" width="100%" alt="PPT Agent Skill sample">

<sub><b>Botanic Forest</b> · <a href="https://github.com/Akxan/ppt-agent-skill/blob/01825dee2ad40a8c719824252605396b9a570d57/ppt-output/style-gallery/botanic_forest.png"><code>ppt-output/style-gallery/botanic_forest.png</code></a></sub>

<img src="https://raw.githubusercontent.com/Akxan/ppt-agent-skill/01825dee2ad40a8c719824252605396b9a570d57/ppt-output/style-gallery/candy_pastel.png" width="100%" alt="PPT Agent Skill sample">

<sub><b>Candy Pastel</b> · <a href="https://github.com/Akxan/ppt-agent-skill/blob/01825dee2ad40a8c719824252605396b9a570d57/ppt-output/style-gallery/candy_pastel.png"><code>ppt-output/style-gallery/candy_pastel.png</code></a></sub>

<img src="https://raw.githubusercontent.com/Akxan/ppt-agent-skill/01825dee2ad40a8c719824252605396b9a570d57/ppt-output/style-gallery/champagne_gold.png" width="100%" alt="PPT Agent Skill sample">

<sub><b>Champagne Gold</b> · <a href="https://github.com/Akxan/ppt-agent-skill/blob/01825dee2ad40a8c719824252605396b9a570d57/ppt-output/style-gallery/champagne_gold.png"><code>ppt-output/style-gallery/champagne_gold.png</code></a></sub>

<img src="https://raw.githubusercontent.com/Akxan/ppt-agent-skill/01825dee2ad40a8c719824252605396b9a570d57/ppt-output/style-gallery/chrome_y2k.png" width="100%" alt="PPT Agent Skill sample">

<sub><b>Chrome Y2k</b> · <a href="https://github.com/Akxan/ppt-agent-skill/blob/01825dee2ad40a8c719824252605396b9a570d57/ppt-output/style-gallery/chrome_y2k.png"><code>ppt-output/style-gallery/chrome_y2k.png</code></a></sub>

<img src="https://raw.githubusercontent.com/Akxan/ppt-agent-skill/01825dee2ad40a8c719824252605396b9a570d57/ppt-output/style-gallery/cyberpunk_neon.png" width="100%" alt="PPT Agent Skill sample">

<sub><b>Cyberpunk Neon</b> · <a href="https://github.com/Akxan/ppt-agent-skill/blob/01825dee2ad40a8c719824252605396b9a570d57/ppt-output/style-gallery/cyberpunk_neon.png"><code>ppt-output/style-gallery/cyberpunk_neon.png</code></a></sub>

<img src="https://raw.githubusercontent.com/Akxan/ppt-agent-skill/01825dee2ad40a8c719824252605396b9a570d57/ppt-output/style-gallery/dark_tech.png" width="100%" alt="PPT Agent Skill sample">

<sub><b>Dark Tech</b> · <a href="https://github.com/Akxan/ppt-agent-skill/blob/01825dee2ad40a8c719824252605396b9a570d57/ppt-output/style-gallery/dark_tech.png"><code>ppt-output/style-gallery/dark_tech.png</code></a></sub>

<img src="https://raw.githubusercontent.com/Akxan/ppt-agent-skill/01825dee2ad40a8c719824252605396b9a570d57/ppt-output/style-gallery/earth_concrete.png" width="100%" alt="PPT Agent Skill sample">

<sub><b>Earth Concrete</b> · <a href="https://github.com/Akxan/ppt-agent-skill/blob/01825dee2ad40a8c719824252605396b9a570d57/ppt-output/style-gallery/earth_concrete.png"><code>ppt-output/style-gallery/earth_concrete.png</code></a></sub>

<img src="https://raw.githubusercontent.com/Akxan/ppt-agent-skill/01825dee2ad40a8c719824252605396b9a570d57/ppt-output/style-gallery/fresh_green.png" width="100%" alt="PPT Agent Skill sample">

<sub><b>Fresh Green</b> · <a href="https://github.com/Akxan/ppt-agent-skill/blob/01825dee2ad40a8c719824252605396b9a570d57/ppt-output/style-gallery/fresh_green.png"><code>ppt-output/style-gallery/fresh_green.png</code></a></sub>

<img src="https://raw.githubusercontent.com/Akxan/ppt-agent-skill/01825dee2ad40a8c719824252605396b9a570d57/ppt-output/style-gallery/gov_authority.png" width="100%" alt="PPT Agent Skill sample">

<sub><b>Gov Authority</b> · <a href="https://github.com/Akxan/ppt-agent-skill/blob/01825dee2ad40a8c719824252605396b9a570d57/ppt-output/style-gallery/gov_authority.png"><code>ppt-output/style-gallery/gov_authority.png</code></a></sub>

<img src="https://raw.githubusercontent.com/Akxan/ppt-agent-skill/01825dee2ad40a8c719824252605396b9a570d57/ppt-output/style-gallery/ink_jade.png" width="100%" alt="PPT Agent Skill sample">

<sub><b>Ink Jade</b> · <a href="https://github.com/Akxan/ppt-agent-skill/blob/01825dee2ad40a8c719824252605396b9a570d57/ppt-output/style-gallery/ink_jade.png"><code>ppt-output/style-gallery/ink_jade.png</code></a></sub>

<img src="https://raw.githubusercontent.com/Akxan/ppt-agent-skill/01825dee2ad40a8c719824252605396b9a570d57/ppt-output/style-gallery/kindergarten_pop.png" width="100%" alt="PPT Agent Skill sample">

<sub><b>Kindergarten Pop</b> · <a href="https://github.com/Akxan/ppt-agent-skill/blob/01825dee2ad40a8c719824252605396b9a570d57/ppt-output/style-gallery/kindergarten_pop.png"><code>ppt-output/style-gallery/kindergarten_pop.png</code></a></sub>

<img src="https://raw.githubusercontent.com/Akxan/ppt-agent-skill/01825dee2ad40a8c719824252605396b9a570d57/ppt-output/style-gallery/liquid_glass.png" width="100%" alt="PPT Agent Skill sample">

<sub><b>Liquid Glass</b> · <a href="https://github.com/Akxan/ppt-agent-skill/blob/01825dee2ad40a8c719824252605396b9a570d57/ppt-output/style-gallery/liquid_glass.png"><code>ppt-output/style-gallery/liquid_glass.png</code></a></sub>

<img src="https://raw.githubusercontent.com/Akxan/ppt-agent-skill/01825dee2ad40a8c719824252605396b9a570d57/ppt-output/style-gallery/luxury_purple.png" width="100%" alt="PPT Agent Skill sample">

<sub><b>Luxury Purple</b> · <a href="https://github.com/Akxan/ppt-agent-skill/blob/01825dee2ad40a8c719824252605396b9a570d57/ppt-output/style-gallery/luxury_purple.png"><code>ppt-output/style-gallery/luxury_purple.png</code></a></sub>

<img src="https://raw.githubusercontent.com/Akxan/ppt-agent-skill/01825dee2ad40a8c719824252605396b9a570d57/ppt-output/style-gallery/medical_pulse.png" width="100%" alt="PPT Agent Skill sample">

<sub><b>Medical Pulse</b> · <a href="https://github.com/Akxan/ppt-agent-skill/blob/01825dee2ad40a8c719824252605396b9a570d57/ppt-output/style-gallery/medical_pulse.png"><code>ppt-output/style-gallery/medical_pulse.png</code></a></sub>

<img src="https://raw.githubusercontent.com/Akxan/ppt-agent-skill/01825dee2ad40a8c719824252605396b9a570d57/ppt-output/style-gallery/minimal_gray.png" width="100%" alt="PPT Agent Skill sample">

<sub><b>Minimal Gray</b> · <a href="https://github.com/Akxan/ppt-agent-skill/blob/01825dee2ad40a8c719824252605396b9a570d57/ppt-output/style-gallery/minimal_gray.png"><code>ppt-output/style-gallery/minimal_gray.png</code></a></sub>

<img src="https://raw.githubusercontent.com/Akxan/ppt-agent-skill/01825dee2ad40a8c719824252605396b9a570d57/ppt-output/style-gallery/mocha_editorial.png" width="100%" alt="PPT Agent Skill sample">

<sub><b>Mocha Editorial</b> · <a href="https://github.com/Akxan/ppt-agent-skill/blob/01825dee2ad40a8c719824252605396b9a570d57/ppt-output/style-gallery/mocha_editorial.png"><code>ppt-output/style-gallery/mocha_editorial.png</code></a></sub>

<a id="gallery-html-slides-bluedusk"></a>

#### [HTML Slides](https://github.com/bluedusk/html-slides) · 70 ⭐ · HTML

<sub>HTML slides with speaker notes, plus a companion presentation app.</sub>

<sub>4 of 4 images in [`bluedusk/html-slides`](https://github.com/bluedusk/html-slides)</sub>

```bash
git clone https://github.com/bluedusk/html-slides
```

<sub><b>Styles below</b> `screenshot` · `hero` — name one when you ask for a deck. These are the project's own strings, taken from the filenames and captions linked under each image, not names this registry made up.</sub>

<img src="https://raw.githubusercontent.com/bluedusk/html-slides/d8289f4c317905cc5d0ca265d32b791e6cb387b7/eval/content/assets/screenshot.jpg" width="100%" alt="HTML Slides sample">

<sub><b>Screenshot</b> · <a href="https://github.com/bluedusk/html-slides/blob/d8289f4c317905cc5d0ca265d32b791e6cb387b7/eval/content/assets/screenshot.jpg"><code>eval/content/assets/screenshot.jpg</code></a></sub>

<img src="https://raw.githubusercontent.com/bluedusk/html-slides/d8289f4c317905cc5d0ca265d32b791e6cb387b7/testing/assets/screenshot.jpg" width="100%" alt="HTML Slides sample">

<sub><b>Screenshot</b> · <a href="https://github.com/bluedusk/html-slides/blob/d8289f4c317905cc5d0ca265d32b791e6cb387b7/testing/assets/screenshot.jpg"><code>testing/assets/screenshot.jpg</code></a></sub>

<img src="https://raw.githubusercontent.com/bluedusk/html-slides/d8289f4c317905cc5d0ca265d32b791e6cb387b7/eval/content/assets/hero.jpg" width="100%" alt="HTML Slides sample">

<sub><b>Hero</b> · <a href="https://github.com/bluedusk/html-slides/blob/d8289f4c317905cc5d0ca265d32b791e6cb387b7/eval/content/assets/hero.jpg"><code>eval/content/assets/hero.jpg</code></a></sub>

<img src="https://raw.githubusercontent.com/bluedusk/html-slides/d8289f4c317905cc5d0ca265d32b791e6cb387b7/testing/assets/hero.jpg" width="100%" alt="HTML Slides sample">

<sub><b>Hero</b> · <a href="https://github.com/bluedusk/html-slides/blob/d8289f4c317905cc5d0ca265d32b791e6cb387b7/testing/assets/hero.jpg"><code>testing/assets/hero.jpg</code></a></sub>

<a id="gallery-kingdee-ppt-skill"></a>

#### [KingDee PPT Skill](https://github.com/WayneZhon/KingDee-PPT-Skill) · 56 ⭐ · HTML

<sub>KingDee corporate style decks.</sub>

<sub>1 of 1 images in [`WayneZhon/KingDee-PPT-Skill`](https://github.com/WayneZhon/KingDee-PPT-Skill)</sub>

```bash
git clone https://github.com/WayneZhon/KingDee-PPT-Skill
```

<sub><b>Styles below</b> `closing` — name one when you ask for a deck. These are the project's own strings, taken from the filenames and captions linked under each image, not names this registry made up.</sub>

<img src="https://raw.githubusercontent.com/WayneZhon/KingDee-PPT-Skill/28ca93aadeefc91fcc64152714ddeece15f13e1d/assets/closing_thanks.png" width="100%" alt="KingDee PPT Skill sample">

<sub><b>Closing</b> · closing · <a href="https://github.com/WayneZhon/KingDee-PPT-Skill/blob/28ca93aadeefc91fcc64152714ddeece15f13e1d/assets/closing_thanks.png"><code>assets/closing_thanks.png</code></a></sub>

<a id="gallery-slide-creator"></a>

#### [Slide Creator](https://github.com/kaisersong/slide-creator) · 46 ⭐ · Both

<sub>AI planning, style discovery and PPTX export.</sub>

<sub>23 of 23 images in [`kaisersong/slide-creator`](https://github.com/kaisersong/slide-creator) · the leading frames are the ones the project puts in its own README</sub>

```bash
git clone https://github.com/kaisersong/slide-creator
```

<sub><b>Styles below</b> `strategy-consulting` · `blue-sky` · `bold-signal` · `electric-studio` · `creative-voltage` · `dark-botanical` · `notebook-tabs` · `pastel-geometry` · `split-pastel` · `vintage-editorial` · `neon-cyber` · `terminal-green` — name one when you ask for a deck. These are the project's own strings, taken from the filenames and captions linked under each image, not names this registry made up.</sub>

<img src="https://raw.githubusercontent.com/kaisersong/slide-creator/d0cf041e3a87db2ac75f8f583fc91a600e369e70/demos/screenshots/strategy-consulting.png" width="100%" alt="Strategy Consulting">

<sub><b>Strategy Consulting</b> · <a href="https://github.com/kaisersong/slide-creator/blob/d0cf041e3a87db2ac75f8f583fc91a600e369e70/demos/screenshots/strategy-consulting.png"><code>demos/screenshots/strategy-consulting.png</code></a></sub>

<img src="https://raw.githubusercontent.com/kaisersong/slide-creator/d0cf041e3a87db2ac75f8f583fc91a600e369e70/demos/screenshots/blue-sky.png" width="100%" alt="Blue Sky">

<sub><b>Blue Sky</b> · <a href="https://github.com/kaisersong/slide-creator/blob/d0cf041e3a87db2ac75f8f583fc91a600e369e70/demos/screenshots/blue-sky.png"><code>demos/screenshots/blue-sky.png</code></a></sub>

<img src="https://raw.githubusercontent.com/kaisersong/slide-creator/d0cf041e3a87db2ac75f8f583fc91a600e369e70/demos/screenshots/bold-signal.png" width="100%" alt="Bold Signal">

<sub><b>Bold Signal</b> · <a href="https://github.com/kaisersong/slide-creator/blob/d0cf041e3a87db2ac75f8f583fc91a600e369e70/demos/screenshots/bold-signal.png"><code>demos/screenshots/bold-signal.png</code></a></sub>

<img src="https://raw.githubusercontent.com/kaisersong/slide-creator/d0cf041e3a87db2ac75f8f583fc91a600e369e70/demos/screenshots/electric-studio.png" width="100%" alt="Electric Studio">

<sub><b>Electric Studio</b> · <a href="https://github.com/kaisersong/slide-creator/blob/d0cf041e3a87db2ac75f8f583fc91a600e369e70/demos/screenshots/electric-studio.png"><code>demos/screenshots/electric-studio.png</code></a></sub>

<img src="https://raw.githubusercontent.com/kaisersong/slide-creator/d0cf041e3a87db2ac75f8f583fc91a600e369e70/demos/screenshots/creative-voltage.png" width="100%" alt="Creative Voltage">

<sub><b>Creative Voltage</b> · <a href="https://github.com/kaisersong/slide-creator/blob/d0cf041e3a87db2ac75f8f583fc91a600e369e70/demos/screenshots/creative-voltage.png"><code>demos/screenshots/creative-voltage.png</code></a></sub>

<img src="https://raw.githubusercontent.com/kaisersong/slide-creator/d0cf041e3a87db2ac75f8f583fc91a600e369e70/demos/screenshots/dark-botanical.png" width="100%" alt="Dark Botanical">

<sub><b>Dark Botanical</b> · <a href="https://github.com/kaisersong/slide-creator/blob/d0cf041e3a87db2ac75f8f583fc91a600e369e70/demos/screenshots/dark-botanical.png"><code>demos/screenshots/dark-botanical.png</code></a></sub>

<img src="https://raw.githubusercontent.com/kaisersong/slide-creator/d0cf041e3a87db2ac75f8f583fc91a600e369e70/demos/screenshots/notebook-tabs.png" width="100%" alt="Notebook Tabs">

<sub><b>Notebook Tabs</b> · <a href="https://github.com/kaisersong/slide-creator/blob/d0cf041e3a87db2ac75f8f583fc91a600e369e70/demos/screenshots/notebook-tabs.png"><code>demos/screenshots/notebook-tabs.png</code></a></sub>

<img src="https://raw.githubusercontent.com/kaisersong/slide-creator/d0cf041e3a87db2ac75f8f583fc91a600e369e70/demos/screenshots/pastel-geometry.png" width="100%" alt="Pastel Geometry">

<sub><b>Pastel Geometry</b> · <a href="https://github.com/kaisersong/slide-creator/blob/d0cf041e3a87db2ac75f8f583fc91a600e369e70/demos/screenshots/pastel-geometry.png"><code>demos/screenshots/pastel-geometry.png</code></a></sub>

<img src="https://raw.githubusercontent.com/kaisersong/slide-creator/d0cf041e3a87db2ac75f8f583fc91a600e369e70/demos/screenshots/split-pastel.png" width="100%" alt="Split Pastel">

<sub><b>Split Pastel</b> · <a href="https://github.com/kaisersong/slide-creator/blob/d0cf041e3a87db2ac75f8f583fc91a600e369e70/demos/screenshots/split-pastel.png"><code>demos/screenshots/split-pastel.png</code></a></sub>

<img src="https://raw.githubusercontent.com/kaisersong/slide-creator/d0cf041e3a87db2ac75f8f583fc91a600e369e70/demos/screenshots/vintage-editorial.png" width="100%" alt="Vintage Editorial">

<sub><b>Vintage Editorial</b> · <a href="https://github.com/kaisersong/slide-creator/blob/d0cf041e3a87db2ac75f8f583fc91a600e369e70/demos/screenshots/vintage-editorial.png"><code>demos/screenshots/vintage-editorial.png</code></a></sub>

<img src="https://raw.githubusercontent.com/kaisersong/slide-creator/d0cf041e3a87db2ac75f8f583fc91a600e369e70/demos/screenshots/neon-cyber.png" width="100%" alt="Neon Cyber">

<sub><b>Neon Cyber</b> · <a href="https://github.com/kaisersong/slide-creator/blob/d0cf041e3a87db2ac75f8f583fc91a600e369e70/demos/screenshots/neon-cyber.png"><code>demos/screenshots/neon-cyber.png</code></a></sub>

<img src="https://raw.githubusercontent.com/kaisersong/slide-creator/d0cf041e3a87db2ac75f8f583fc91a600e369e70/demos/screenshots/terminal-green.png" width="100%" alt="Terminal Green">

<sub><b>Terminal Green</b> · <a href="https://github.com/kaisersong/slide-creator/blob/d0cf041e3a87db2ac75f8f583fc91a600e369e70/demos/screenshots/terminal-green.png"><code>demos/screenshots/terminal-green.png</code></a></sub>

<img src="https://raw.githubusercontent.com/kaisersong/slide-creator/d0cf041e3a87db2ac75f8f583fc91a600e369e70/demos/screenshots/swiss-modern.png" width="100%" alt="Swiss Modern">

<sub><b>Swiss Modern</b> · <a href="https://github.com/kaisersong/slide-creator/blob/d0cf041e3a87db2ac75f8f583fc91a600e369e70/demos/screenshots/swiss-modern.png"><code>demos/screenshots/swiss-modern.png</code></a></sub>

<img src="https://raw.githubusercontent.com/kaisersong/slide-creator/d0cf041e3a87db2ac75f8f583fc91a600e369e70/demos/screenshots/paper-ink.png" width="100%" alt="Paper & Ink">

<sub><b>Paper & Ink</b> · <code>paper-ink</code> · <a href="https://github.com/kaisersong/slide-creator/blob/d0cf041e3a87db2ac75f8f583fc91a600e369e70/demos/screenshots/paper-ink.png"><code>demos/screenshots/paper-ink.png</code></a></sub>

<img src="https://raw.githubusercontent.com/kaisersong/slide-creator/d0cf041e3a87db2ac75f8f583fc91a600e369e70/demos/screenshots/aurora-mesh.png" width="100%" alt="Aurora Mesh">

<sub><b>Aurora Mesh</b> · <a href="https://github.com/kaisersong/slide-creator/blob/d0cf041e3a87db2ac75f8f583fc91a600e369e70/demos/screenshots/aurora-mesh.png"><code>demos/screenshots/aurora-mesh.png</code></a></sub>

<img src="https://raw.githubusercontent.com/kaisersong/slide-creator/d0cf041e3a87db2ac75f8f583fc91a600e369e70/demos/screenshots/enterprise-dark.png" width="100%" alt="Enterprise Dark">

<sub><b>Enterprise Dark</b> · <a href="https://github.com/kaisersong/slide-creator/blob/d0cf041e3a87db2ac75f8f583fc91a600e369e70/demos/screenshots/enterprise-dark.png"><code>demos/screenshots/enterprise-dark.png</code></a></sub>

<img src="https://raw.githubusercontent.com/kaisersong/slide-creator/d0cf041e3a87db2ac75f8f583fc91a600e369e70/demos/screenshots/glassmorphism.png" width="100%" alt="Glassmorphism">

<sub><b>Glassmorphism</b> · <a href="https://github.com/kaisersong/slide-creator/blob/d0cf041e3a87db2ac75f8f583fc91a600e369e70/demos/screenshots/glassmorphism.png"><code>demos/screenshots/glassmorphism.png</code></a></sub>

<img src="https://raw.githubusercontent.com/kaisersong/slide-creator/d0cf041e3a87db2ac75f8f583fc91a600e369e70/demos/screenshots/neo-brutalism.png" width="100%" alt="Neo-Brutalism">

<sub><b>Neo-Brutalism</b> · <a href="https://github.com/kaisersong/slide-creator/blob/d0cf041e3a87db2ac75f8f583fc91a600e369e70/demos/screenshots/neo-brutalism.png"><code>demos/screenshots/neo-brutalism.png</code></a></sub>

<img src="https://raw.githubusercontent.com/kaisersong/slide-creator/d0cf041e3a87db2ac75f8f583fc91a600e369e70/demos/screenshots/chinese-chan.png" width="100%" alt="Chinese Chan">

<sub><b>Chinese Chan</b> · <a href="https://github.com/kaisersong/slide-creator/blob/d0cf041e3a87db2ac75f8f583fc91a600e369e70/demos/screenshots/chinese-chan.png"><code>demos/screenshots/chinese-chan.png</code></a></sub>

<img src="https://raw.githubusercontent.com/kaisersong/slide-creator/d0cf041e3a87db2ac75f8f583fc91a600e369e70/demos/screenshots/data-story.png" width="100%" alt="Data Story">

<sub><b>Data Story</b> · <a href="https://github.com/kaisersong/slide-creator/blob/d0cf041e3a87db2ac75f8f583fc91a600e369e70/demos/screenshots/data-story.png"><code>demos/screenshots/data-story.png</code></a></sub>

<img src="https://raw.githubusercontent.com/kaisersong/slide-creator/d0cf041e3a87db2ac75f8f583fc91a600e369e70/demos/screenshots/modern-newspaper.png" width="100%" alt="Modern Newspaper">

<sub><b>Modern Newspaper</b> · <a href="https://github.com/kaisersong/slide-creator/blob/d0cf041e3a87db2ac75f8f583fc91a600e369e70/demos/screenshots/modern-newspaper.png"><code>demos/screenshots/modern-newspaper.png</code></a></sub>

<img src="https://raw.githubusercontent.com/kaisersong/slide-creator/d0cf041e3a87db2ac75f8f583fc91a600e369e70/demos/screenshots/neo-retro-dev.png" width="100%" alt="Neo-Retro Dev Deck">

<sub><b>Neo-Retro Dev Deck</b> · <a href="https://github.com/kaisersong/slide-creator/blob/d0cf041e3a87db2ac75f8f583fc91a600e369e70/demos/screenshots/neo-retro-dev.png"><code>demos/screenshots/neo-retro-dev.png</code></a></sub>

<img src="https://raw.githubusercontent.com/kaisersong/slide-creator/d0cf041e3a87db2ac75f8f583fc91a600e369e70/demos/screenshots/japanese-zen.png" width="100%" alt="Slide Creator sample">

<sub><b>Japanese Zen</b> · <a href="https://github.com/kaisersong/slide-creator/blob/d0cf041e3a87db2ac75f8f583fc91a600e369e70/demos/screenshots/japanese-zen.png"><code>demos/screenshots/japanese-zen.png</code></a></sub>

<a id="gallery-next-slide"></a>

#### [next-slide](https://github.com/codesstar/next-slide) · 43 ⭐ · HTML

<sub>26+ styles, zero dependencies, bilingual.</sub>

<sub>1 of 1 images in [`codesstar/next-slide`](https://github.com/codesstar/next-slide)</sub>

```bash
git clone https://github.com/codesstar/next-slide
```

<sub><b>Styles below</b> `motion-brand-showcase` — name one when you ask for a deck. These are the project's own strings, taken from the filenames and captions linked under each image, not names this registry made up.</sub>

<img src="https://raw.githubusercontent.com/codesstar/next-slide/e92c1b2506e6cf5acff7d2b92339ba0c0ce2af22/scenarios/images/motion-brand-showcase.webp" width="100%" alt="next-slide sample">

<sub><b>Motion Brand Showcase</b> · <a href="https://github.com/codesstar/next-slide/blob/e92c1b2506e6cf5acff7d2b92339ba0c0ce2af22/scenarios/images/motion-brand-showcase.webp"><code>scenarios/images/motion-brand-showcase.webp</code></a></sub>

<a id="gallery-slide-writer"></a>

#### [Slide Writer](https://github.com/FeeiCN/slide-writer) · 40 ⭐ · HTML

<sub>Enterprise HTML decks from ideas, outlines, documents or speech drafts.</sub>

<sub>5 of 5 images in [`FeeiCN/slide-writer`](https://github.com/FeeiCN/slide-writer) · the leading frames are the ones the project puts in its own README</sub>

```bash
git clone https://github.com/FeeiCN/slide-writer
```

<sub><b>Styles below</b> `before-after` · `writer` · `test-antgroup-eric` · `test-tencent-pony-ma` · `test-alibaba-jack-ma` — name one when you ask for a deck. These are the project's own strings, taken from the filenames and captions linked under each image, not names this registry made up.</sub>

<img src="https://raw.githubusercontent.com/FeeiCN/slide-writer/3c4524c4abb3310fdee106282d0a64f156fd4ff6/examples/before-after.png" width="100%" alt="Slide-Writer Demo">

<sub><b>Slide-Writer Demo</b> · <code>before-after</code> · <a href="https://github.com/FeeiCN/slide-writer/blob/3c4524c4abb3310fdee106282d0a64f156fd4ff6/examples/before-after.png"><code>examples/before-after.png</code></a></sub>

<img src="https://raw.githubusercontent.com/FeeiCN/slide-writer/3c4524c4abb3310fdee106282d0a64f156fd4ff6/examples/slide-writer.png" width="100%" alt="Slide-Writer">

<sub><b>Slide-Writer</b> · <a href="https://github.com/FeeiCN/slide-writer/blob/3c4524c4abb3310fdee106282d0a64f156fd4ff6/examples/slide-writer.png"><code>examples/slide-writer.png</code></a></sub>

<img src="https://raw.githubusercontent.com/FeeiCN/slide-writer/3c4524c4abb3310fdee106282d0a64f156fd4ff6/examples/test-antgroup-eric.png" width="100%" alt="Slide Writer sample">

<sub><b>Test Antgroup Eric</b> · <a href="https://github.com/FeeiCN/slide-writer/blob/3c4524c4abb3310fdee106282d0a64f156fd4ff6/examples/test-antgroup-eric.png"><code>examples/test-antgroup-eric.png</code></a></sub>

<img src="https://raw.githubusercontent.com/FeeiCN/slide-writer/3c4524c4abb3310fdee106282d0a64f156fd4ff6/examples/test-tencent-pony-ma.png" width="100%" alt="Slide Writer sample">

<sub><b>Test Tencent Pony Ma</b> · <a href="https://github.com/FeeiCN/slide-writer/blob/3c4524c4abb3310fdee106282d0a64f156fd4ff6/examples/test-tencent-pony-ma.png"><code>examples/test-tencent-pony-ma.png</code></a></sub>

<img src="https://raw.githubusercontent.com/FeeiCN/slide-writer/3c4524c4abb3310fdee106282d0a64f156fd4ff6/examples/test-alibaba-jack-ma.png" width="100%" alt="Slide Writer sample">

<sub><b>Test Alibaba Jack Ma</b> · <a href="https://github.com/FeeiCN/slide-writer/blob/3c4524c4abb3310fdee106282d0a64f156fd4ff6/examples/test-alibaba-jack-ma.png"><code>examples/test-alibaba-jack-ma.png</code></a></sub>

<a id="gallery-skills-slides"></a>

#### [Skills Slides](https://github.com/nghiahsgs/skills-slides) · 30 ⭐ · HTML

<sub>50 aesthetics x 20 palettes x 10 fonts x 5 layouts x 30+ effects.</sub>

<sub>4 of 4 images in [`nghiahsgs/skills-slides`](https://github.com/nghiahsgs/skills-slides) · the leading frames are the ones the project puts in its own README</sub>

```bash
git clone https://github.com/nghiahsgs/skills-slides
```

<sub><b>Styles below</b> `06-features` · `07-checklist` · `03-50k` — name one when you ask for a deck. These are the project's own strings, taken from the filenames and captions linked under each image, not names this registry made up.</sub>

<img src="https://raw.githubusercontent.com/nghiahsgs/skills-slides/c271d3cda03bf79733cc91ba28e25716196638b7/examples/screenshots/slide-06-features.png" width="100%" alt="Feature grid — 6 cards with 3D tilt hover">

<sub><b>Feature grid — 6 cards with 3D tilt hover</b> · <code>06-features</code> · <a href="https://github.com/nghiahsgs/skills-slides/blob/c271d3cda03bf79733cc91ba28e25716196638b7/examples/screenshots/slide-06-features.png"><code>examples/screenshots/slide-06-features.png</code></a></sub>

<img src="https://raw.githubusercontent.com/nghiahsgs/skills-slides/c271d3cda03bf79733cc91ba28e25716196638b7/examples/screenshots/slide-07-checklist.png" width="100%" alt="Anti-slop checklist — 10-point quality gate">

<sub><b>Anti-slop checklist — 10-point quality gate</b> · <code>07-checklist</code> · <a href="https://github.com/nghiahsgs/skills-slides/blob/c271d3cda03bf79733cc91ba28e25716196638b7/examples/screenshots/slide-07-checklist.png"><code>examples/screenshots/slide-07-checklist.png</code></a></sub>

<img src="https://raw.githubusercontent.com/nghiahsgs/skills-slides/c271d3cda03bf79733cc91ba28e25716196638b7/examples/screenshots/slide-01-title.png" width="100%" alt="Skills Slides sample">

<sub><b>Title</b> · title · <a href="https://github.com/nghiahsgs/skills-slides/blob/c271d3cda03bf79733cc91ba28e25716196638b7/examples/screenshots/slide-01-title.png"><code>examples/screenshots/slide-01-title.png</code></a></sub>

<img src="https://raw.githubusercontent.com/nghiahsgs/skills-slides/c271d3cda03bf79733cc91ba28e25716196638b7/examples/screenshots/slide-03-50k.png" width="100%" alt="Skills Slides sample">

<sub><b>03 50k</b> · <a href="https://github.com/nghiahsgs/skills-slides/blob/c271d3cda03bf79733cc91ba28e25716196638b7/examples/screenshots/slide-03-50k.png"><code>examples/screenshots/slide-03-50k.png</code></a></sub>

<a id="gallery-powerpoint-fancy-design"></a>

#### [PowerPoint Fancy Design](https://github.com/Phlegonlabs/Powerpoint-fancy-design) · 27 ⭐ · Both

<sub>Page-structured Markdown into styled 1600x900 HTML slides, PNG renders and exports.</sub>

<sub>24 of 30 images in [`Phlegonlabs/Powerpoint-fancy-design`](https://github.com/Phlegonlabs/Powerpoint-fancy-design) · the leading frames are the ones the project puts in its own README</sub>

```bash
git clone https://github.com/Phlegonlabs/Powerpoint-fancy-design
```

<sub><b>Styles below</b> `swiss-international` · `east-asian-minimalism` · `risograph-print` · `bauhaus-geometry` · `organic-handcrafted` · `art-deco-luxury` · `neo-brutalism` · `retro-futurism` · `dark-editorial` · `memphis-pop` — name one when you ask for a deck. These are the project's own strings, taken from the filenames and captions linked under each image, not names this registry made up.</sub>

<img src="https://raw.githubusercontent.com/Phlegonlabs/Powerpoint-fancy-design/d6167dbc5d1ee9a0f3b2b90b399156322e9178ae/assets/style-preview-a.png" width="100%" alt="Swiss International">

<sub><b>Swiss International</b> · <a href="https://github.com/Phlegonlabs/Powerpoint-fancy-design/blob/d6167dbc5d1ee9a0f3b2b90b399156322e9178ae/assets/style-preview-a.png"><code>assets/style-preview-a.png</code></a></sub>

<img src="https://raw.githubusercontent.com/Phlegonlabs/Powerpoint-fancy-design/d6167dbc5d1ee9a0f3b2b90b399156322e9178ae/assets/style-preview-b.png" width="100%" alt="East Asian Minimalism">

<sub><b>East Asian Minimalism</b> · <a href="https://github.com/Phlegonlabs/Powerpoint-fancy-design/blob/d6167dbc5d1ee9a0f3b2b90b399156322e9178ae/assets/style-preview-b.png"><code>assets/style-preview-b.png</code></a></sub>

<img src="https://raw.githubusercontent.com/Phlegonlabs/Powerpoint-fancy-design/d6167dbc5d1ee9a0f3b2b90b399156322e9178ae/assets/style-preview-c.png" width="100%" alt="Risograph Print">

<sub><b>Risograph Print</b> · <a href="https://github.com/Phlegonlabs/Powerpoint-fancy-design/blob/d6167dbc5d1ee9a0f3b2b90b399156322e9178ae/assets/style-preview-c.png"><code>assets/style-preview-c.png</code></a></sub>

<img src="https://raw.githubusercontent.com/Phlegonlabs/Powerpoint-fancy-design/d6167dbc5d1ee9a0f3b2b90b399156322e9178ae/assets/style-preview-d.png" width="100%" alt="Bauhaus Geometry">

<sub><b>Bauhaus Geometry</b> · <a href="https://github.com/Phlegonlabs/Powerpoint-fancy-design/blob/d6167dbc5d1ee9a0f3b2b90b399156322e9178ae/assets/style-preview-d.png"><code>assets/style-preview-d.png</code></a></sub>

<img src="https://raw.githubusercontent.com/Phlegonlabs/Powerpoint-fancy-design/d6167dbc5d1ee9a0f3b2b90b399156322e9178ae/assets/style-preview-e.png" width="100%" alt="Organic Handcrafted">

<sub><b>Organic Handcrafted</b> · <a href="https://github.com/Phlegonlabs/Powerpoint-fancy-design/blob/d6167dbc5d1ee9a0f3b2b90b399156322e9178ae/assets/style-preview-e.png"><code>assets/style-preview-e.png</code></a></sub>

<img src="https://raw.githubusercontent.com/Phlegonlabs/Powerpoint-fancy-design/d6167dbc5d1ee9a0f3b2b90b399156322e9178ae/assets/style-preview-f.png" width="100%" alt="Art Deco Luxury">

<sub><b>Art Deco Luxury</b> · <a href="https://github.com/Phlegonlabs/Powerpoint-fancy-design/blob/d6167dbc5d1ee9a0f3b2b90b399156322e9178ae/assets/style-preview-f.png"><code>assets/style-preview-f.png</code></a></sub>

<img src="https://raw.githubusercontent.com/Phlegonlabs/Powerpoint-fancy-design/d6167dbc5d1ee9a0f3b2b90b399156322e9178ae/assets/style-preview-g.png" width="100%" alt="Neo Brutalism">

<sub><b>Neo Brutalism</b> · <a href="https://github.com/Phlegonlabs/Powerpoint-fancy-design/blob/d6167dbc5d1ee9a0f3b2b90b399156322e9178ae/assets/style-preview-g.png"><code>assets/style-preview-g.png</code></a></sub>

<img src="https://raw.githubusercontent.com/Phlegonlabs/Powerpoint-fancy-design/d6167dbc5d1ee9a0f3b2b90b399156322e9178ae/assets/style-preview-h.png" width="100%" alt="Retro Futurism">

<sub><b>Retro Futurism</b> · <a href="https://github.com/Phlegonlabs/Powerpoint-fancy-design/blob/d6167dbc5d1ee9a0f3b2b90b399156322e9178ae/assets/style-preview-h.png"><code>assets/style-preview-h.png</code></a></sub>

<img src="https://raw.githubusercontent.com/Phlegonlabs/Powerpoint-fancy-design/d6167dbc5d1ee9a0f3b2b90b399156322e9178ae/assets/style-preview-i.png" width="100%" alt="Dark Editorial">

<sub><b>Dark Editorial</b> · <a href="https://github.com/Phlegonlabs/Powerpoint-fancy-design/blob/d6167dbc5d1ee9a0f3b2b90b399156322e9178ae/assets/style-preview-i.png"><code>assets/style-preview-i.png</code></a></sub>

<img src="https://raw.githubusercontent.com/Phlegonlabs/Powerpoint-fancy-design/d6167dbc5d1ee9a0f3b2b90b399156322e9178ae/assets/style-preview-j.png" width="100%" alt="Memphis Pop">

<sub><b>Memphis Pop</b> · <a href="https://github.com/Phlegonlabs/Powerpoint-fancy-design/blob/d6167dbc5d1ee9a0f3b2b90b399156322e9178ae/assets/style-preview-j.png"><code>assets/style-preview-j.png</code></a></sub>

<img src="https://raw.githubusercontent.com/Phlegonlabs/Powerpoint-fancy-design/d6167dbc5d1ee9a0f3b2b90b399156322e9178ae/assets/style-preview-zh-a.png" width="100%" alt="PowerPoint Fancy Design sample">

<sub><a href="https://github.com/Phlegonlabs/Powerpoint-fancy-design/blob/d6167dbc5d1ee9a0f3b2b90b399156322e9178ae/assets/style-preview-zh-a.png"><code>assets/style-preview-zh-a.png</code></a></sub>

<img src="https://raw.githubusercontent.com/Phlegonlabs/Powerpoint-fancy-design/d6167dbc5d1ee9a0f3b2b90b399156322e9178ae/assets/style-preview-zh-b.png" width="100%" alt="PowerPoint Fancy Design sample">

<sub><a href="https://github.com/Phlegonlabs/Powerpoint-fancy-design/blob/d6167dbc5d1ee9a0f3b2b90b399156322e9178ae/assets/style-preview-zh-b.png"><code>assets/style-preview-zh-b.png</code></a></sub>

<img src="https://raw.githubusercontent.com/Phlegonlabs/Powerpoint-fancy-design/d6167dbc5d1ee9a0f3b2b90b399156322e9178ae/assets/style-preview-zh-c.png" width="100%" alt="PowerPoint Fancy Design sample">

<sub><a href="https://github.com/Phlegonlabs/Powerpoint-fancy-design/blob/d6167dbc5d1ee9a0f3b2b90b399156322e9178ae/assets/style-preview-zh-c.png"><code>assets/style-preview-zh-c.png</code></a></sub>

<img src="https://raw.githubusercontent.com/Phlegonlabs/Powerpoint-fancy-design/d6167dbc5d1ee9a0f3b2b90b399156322e9178ae/assets/style-preview-zh-d.png" width="100%" alt="PowerPoint Fancy Design sample">

<sub><a href="https://github.com/Phlegonlabs/Powerpoint-fancy-design/blob/d6167dbc5d1ee9a0f3b2b90b399156322e9178ae/assets/style-preview-zh-d.png"><code>assets/style-preview-zh-d.png</code></a></sub>

<img src="https://raw.githubusercontent.com/Phlegonlabs/Powerpoint-fancy-design/d6167dbc5d1ee9a0f3b2b90b399156322e9178ae/assets/style-preview-zh-e.png" width="100%" alt="PowerPoint Fancy Design sample">

<sub><a href="https://github.com/Phlegonlabs/Powerpoint-fancy-design/blob/d6167dbc5d1ee9a0f3b2b90b399156322e9178ae/assets/style-preview-zh-e.png"><code>assets/style-preview-zh-e.png</code></a></sub>

<img src="https://raw.githubusercontent.com/Phlegonlabs/Powerpoint-fancy-design/d6167dbc5d1ee9a0f3b2b90b399156322e9178ae/assets/style-preview-zh-f.png" width="100%" alt="PowerPoint Fancy Design sample">

<sub><a href="https://github.com/Phlegonlabs/Powerpoint-fancy-design/blob/d6167dbc5d1ee9a0f3b2b90b399156322e9178ae/assets/style-preview-zh-f.png"><code>assets/style-preview-zh-f.png</code></a></sub>

<img src="https://raw.githubusercontent.com/Phlegonlabs/Powerpoint-fancy-design/d6167dbc5d1ee9a0f3b2b90b399156322e9178ae/assets/style-preview-zh-g.png" width="100%" alt="PowerPoint Fancy Design sample">

<sub><a href="https://github.com/Phlegonlabs/Powerpoint-fancy-design/blob/d6167dbc5d1ee9a0f3b2b90b399156322e9178ae/assets/style-preview-zh-g.png"><code>assets/style-preview-zh-g.png</code></a></sub>

<img src="https://raw.githubusercontent.com/Phlegonlabs/Powerpoint-fancy-design/d6167dbc5d1ee9a0f3b2b90b399156322e9178ae/assets/style-preview-zh-h.png" width="100%" alt="PowerPoint Fancy Design sample">

<sub><a href="https://github.com/Phlegonlabs/Powerpoint-fancy-design/blob/d6167dbc5d1ee9a0f3b2b90b399156322e9178ae/assets/style-preview-zh-h.png"><code>assets/style-preview-zh-h.png</code></a></sub>

<img src="https://raw.githubusercontent.com/Phlegonlabs/Powerpoint-fancy-design/d6167dbc5d1ee9a0f3b2b90b399156322e9178ae/assets/style-preview-zh-i.png" width="100%" alt="PowerPoint Fancy Design sample">

<sub><a href="https://github.com/Phlegonlabs/Powerpoint-fancy-design/blob/d6167dbc5d1ee9a0f3b2b90b399156322e9178ae/assets/style-preview-zh-i.png"><code>assets/style-preview-zh-i.png</code></a></sub>

<img src="https://raw.githubusercontent.com/Phlegonlabs/Powerpoint-fancy-design/d6167dbc5d1ee9a0f3b2b90b399156322e9178ae/assets/style-preview-zh-j.png" width="100%" alt="PowerPoint Fancy Design sample">

<sub><a href="https://github.com/Phlegonlabs/Powerpoint-fancy-design/blob/d6167dbc5d1ee9a0f3b2b90b399156322e9178ae/assets/style-preview-zh-j.png"><code>assets/style-preview-zh-j.png</code></a></sub>

<img src="https://raw.githubusercontent.com/Phlegonlabs/Powerpoint-fancy-design/d6167dbc5d1ee9a0f3b2b90b399156322e9178ae/assets/style-preview-zh-tw-a.png" width="100%" alt="PowerPoint Fancy Design sample">

<sub><a href="https://github.com/Phlegonlabs/Powerpoint-fancy-design/blob/d6167dbc5d1ee9a0f3b2b90b399156322e9178ae/assets/style-preview-zh-tw-a.png"><code>assets/style-preview-zh-tw-a.png</code></a></sub>

<img src="https://raw.githubusercontent.com/Phlegonlabs/Powerpoint-fancy-design/d6167dbc5d1ee9a0f3b2b90b399156322e9178ae/assets/style-preview-zh-tw-b.png" width="100%" alt="PowerPoint Fancy Design sample">

<sub><a href="https://github.com/Phlegonlabs/Powerpoint-fancy-design/blob/d6167dbc5d1ee9a0f3b2b90b399156322e9178ae/assets/style-preview-zh-tw-b.png"><code>assets/style-preview-zh-tw-b.png</code></a></sub>

<img src="https://raw.githubusercontent.com/Phlegonlabs/Powerpoint-fancy-design/d6167dbc5d1ee9a0f3b2b90b399156322e9178ae/assets/style-preview-zh-tw-c.png" width="100%" alt="PowerPoint Fancy Design sample">

<sub><a href="https://github.com/Phlegonlabs/Powerpoint-fancy-design/blob/d6167dbc5d1ee9a0f3b2b90b399156322e9178ae/assets/style-preview-zh-tw-c.png"><code>assets/style-preview-zh-tw-c.png</code></a></sub>

<img src="https://raw.githubusercontent.com/Phlegonlabs/Powerpoint-fancy-design/d6167dbc5d1ee9a0f3b2b90b399156322e9178ae/assets/style-preview-zh-tw-d.png" width="100%" alt="PowerPoint Fancy Design sample">

<sub><a href="https://github.com/Phlegonlabs/Powerpoint-fancy-design/blob/d6167dbc5d1ee9a0f3b2b90b399156322e9178ae/assets/style-preview-zh-tw-d.png"><code>assets/style-preview-zh-tw-d.png</code></a></sub>

<a id="gallery-pptx-from-layouts"></a>

#### [PPTX from Layouts](https://github.com/tristan-mcinnis/pptx-from-layouts-skill) · 9 ⭐ · PPTX

<sub>Generate decks from markdown strictly through a template's slide master layouts.</sub>

<sub>1 of 1 images in [`tristan-mcinnis/pptx-from-layouts-skill`](https://github.com/tristan-mcinnis/pptx-from-layouts-skill)</sub>

```bash
git clone https://github.com/tristan-mcinnis/pptx-from-layouts-skill
```

<sub><b>Styles below</b> `thumbnail` — name one when you ask for a deck. These are the project's own strings, taken from the filenames and captions linked under each image, not names this registry made up.</sub>

<img src="https://raw.githubusercontent.com/tristan-mcinnis/pptx-from-layouts-skill/53b0e750694d807e3510c2017744197c3c5089b0/examples/q1-strategy/thumbnail.jpg" width="100%" alt="PPTX from Layouts sample">

<sub><b>Thumbnail</b> · <a href="https://github.com/tristan-mcinnis/pptx-from-layouts-skill/blob/53b0e750694d807e3510c2017744197c3c5089b0/examples/q1-strategy/thumbnail.jpg"><code>examples/q1-strategy/thumbnail.jpg</code></a></sub>

<sub>No imagery in the repositories of: Anthropic PPTX (official), Visual Explainer, Claude Office Skills, Academic PPTX, Visual Cognition Slides, Huawei Style PPT Skill.</sub>

<sub>**278 images, all of them the projects' own**, shown full size rather than as thumbnails — a slide is too dense to judge at 300px. Each was read from its repository at a pinned commit, credited in the caption above it, and served from that repository rather than copied here. Nothing was produced by running a skill, so treat it as what each team chose to show off — not as a like-for-like comparison. Regenerate with `python scripts/fetch_samples.py`.</sub>
<!-- END:GALLERY -->

---

## The benchmark — parked

An earlier plan was to score every skill against a published rubric. The harness exists and
works: three [corpora](benchmark/corpus/), a [seven-dimension rubric](benchmark/rubric.md),
mechanical fidelity and chart checks, and blind two-judge scoring.

It is **parked**, and the reason is arithmetic. One PPTX-route deck costs roughly $10 of
agent time to generate and did not converge at that. A single pass across Tier S runs to a
few hundred dollars — and the rubric itself says scores mean nothing below double-digit run
counts. That is months and real money before the first defensible ranking, which is the
wrong thing for this repo to be spending itself on. **Use the tables above to choose; they
are facts, not scores.**

What came out of the attempt is worth more than the scores would have been — the
measurement tools, and one finding that is now
[principle 7's evidence](principles/07-render-and-look.md).

<details>
<summary>The one run that was completed</summary>

<!-- BEGIN:SCORECARD -->
| Skill | Mean | Visual | Type | Density | Data | Content | Deliver | Effort | Runs |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| **frontend-slides** | **25.0**/35 | 3.0 | 4.0 | 3.0 | 3.0 | 5.0 | 3.0 | 4.0 | 1 |

<sub>1 run(s) so far — far too few to rank anything. Scores are provisional and every run discloses its conflicts. ⚠️ = a run gated to zero on data or content fidelity.</sub>
<!-- END:SCORECARD -->

n=1, non-blind originally, and [corrected downward twice](benchmark/results/run-01/README.md#corrections)
once measured properly. Not a ranking. → [Harness, corpus and rubric](benchmark/)

</details>

---

## Eight principles

Thirty-odd teams solved this problem in parallel. Where they independently converged is
the most reliable signal in the field. [**Read the principles →**](principles/)

| | Principle | The one-line version |
|---|---|---|
| 1 | [Show, don't tell](principles/01-show-dont-tell.md) | Never ask about taste. Generate options and let people point. |
| 2 | [Anti-slop is a banned list](principles/02-anti-ai-slop.md) | "Make it beautiful" does nothing. "Never use Inter" does. |
| 3 | [Slides are print, not web](principles/03-fixed-stage.md) | Fixed 1920×1080, scale to fit, letterbox. Give up responsive. |
| 4 | [Constraint beats freedom](principles/04-constraint-beats-freedom.md) | Lock the palette. Agents get more consistent, not less capable. |
| 5 | [SKILL.md is a table of contents](principles/05-progressive-disclosure.md) | Zara cut 1,625 lines to 183. Same features, 89% less context. |
| 6 | [Single file outlasts frameworks](principles/06-single-file.md) | Dependencies are debt. Inline everything. |
| 7 | [Render it and look at it](principles/07-render-and-look.md) | Visual output needs visual QA. Screenshot, then let the model see. |
| 8 | [Distill, don't design](principles/08-distill-dont-design.md) | Do it by hand 30 times, *then* write the skill. |

Principle 2 has the strongest evidence: `frontend-slides` and Anthropic's official `pptx`
skill both ban decorative accent lines under titles, in almost the same words, having
arrived there independently. When a community and a model vendor converge on the same
oddly specific prohibition, that is a real fingerprint of machine-generated design.

---

## How this stays accurate

Hand-maintained lists rot. This one is generated:

```
data/skills.json       ──▶ curated research, the only file written by hand
data/stats.json        ──▶ live GitHub numbers, refreshed daily by CI
data/capabilities.json ──▶ documented capabilities, with the quote each rests on
data/samples.json      ──▶ sample imagery, pinned to the commit it was read at
        │
        └──▶ scripts/render.py ──▶ tables and galleries in README.md + README.en.md
```

```bash
python scripts/fetch_stats.py       # refresh stars, forks, licenses, activity
python scripts/fetch_samples.py     # re-harvest sample imagery from each repo
python scripts/fetch_samples.py --verify   # every pinned image still exists
python scripts/render.py            # regenerate every table in both READMEs
python scripts/render.py --check    # CI gate: fails if the READMEs drifted
```

Gallery images are never copied into this repository. Each one is a link to the
source project's own file at a fixed commit, so the picture cannot change under the
caption and the attribution cannot be lost.

A GitHub Action runs this daily and opens a PR when numbers move. Editing a table by hand
is a no-op — the next run overwrites it. Edit `data/skills.json`.

---

## Contributing

New skills, corrections, and especially **benchmark runs** — see
[CONTRIBUTING.md](CONTRIBUTING.md).

If you wrote one of these skills and this repo describes it wrongly, open an issue. It gets
fixed, and if a benchmark run was flawed it gets re-run with the original left visible in
git history.

---

## Honest limits

- **Star counts measure attention, not quality.** Several of these projects grew on their
  authors' considerable social reach. That is real signal about community size and nothing
  else. It is why the benchmark exists.
- **No runs yet.** The rankings on this page are *not* quality rankings. They are a
  registry sorted by popularity, clearly labeled as such, until scores exist.
- **Generative variance is real.** Same skill, same prompt, different output. Small score
  gaps will not mean anything until run counts are in the double digits.
- **Descriptions come from documentation**, not from having personally shipped a deck with
  all 26. Where I have run something, the dossier says so.
- **This is a fast-moving field.** Everything here carries a date. Check it.

---

## Sources & prior art

Two curated lists came before this one and were leads into it —
[ToseaAI/awesome-html-slide-skills](https://github.com/ToseaAI/awesome-html-slide-skills)
and [software-ai-life/Awesome-PPT-Design-Skills](https://github.com/software-ai-life/Awesome-PPT-Design-Skills).
Both are HTML-route focused; this registry also covers the PPTX route, which is where the
single most-starred project in the field actually lives.

Longer research notes, including the primary-source reading behind the principles:
[`docs/research-notes-2026-07.md`](docs/research-notes-2026-07.md).

Every star, fork, license and activity figure is fetched live from the GitHub REST API —
never copied from another list.

---

<div align="center">
<sub>

Registry content licensed [CC BY 4.0](LICENSE) · code licensed [MIT](LICENSE-CODE)
Linked projects carry their own licenses — **check them**, one is AGPL-3.0.

</sub>
</div>
