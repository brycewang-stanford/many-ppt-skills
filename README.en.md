<div align="center">

# many-ppt-skills

**Every AI slide-deck skill worth knowing, gathered and compared on one page — so you can pick the right one and get on with it.**

See one you like in the [gallery](#what-they-look-like)? **[Make your own in 60 seconds](#make-your-own-in-60-seconds)** — three steps.

[简体中文](README.md) · [English](README.en.md)

<!-- BEGIN:COUNTS -->
**227 skills tracked**, **39 of them read by hand** · **309,752 combined stars** · 83 HTML-native · 79 native PPTX · 25 both · data refreshed **2026-09-12**
<!-- END:COUNTS -->

</div>

---

Coding agents got good at CSS, and in six months a whole category appeared: skills that
turn a document into a deck that does not look machine-made. This page tracks
<!-- BEGIN:TRACKED -->227<!-- END:TRACKED --> of them, and four have over 20,000 stars each.

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

## Make your own in 60 seconds

Browse the [gallery](#what-they-look-like) first. Once something catches your eye, three
steps. Here is a real one, end to end.

**Step 1 — copy the style id out of the caption.** Every image has a line under it:

> **Soft Editorial · 4** · `soft-editorial` · [`screenshots/soft-editorial-4.png`](https://github.com/zarazhangrui/beautiful-html-templates)

The monospace `soft-editorial` is the **style id** — that is what you copy. Which skill it
belongs to is the heading above that set of images (here, **Frontend Slides**).

**Step 2 — install that skill.** The command is printed above its images, ready to copy.
This one is the `plugin` method, so **both lines are typed inside Claude Code, not in a
terminal**:

```text
/plugin marketplace add https://github.com/zarazhangrui/frontend-slides
/plugin install frontend-slides@frontend-slides
```

> There are five install methods and they do different things — `clone` lands in
> `~/.claude/skills/` and needs a session restart, `python` needs local dependencies,
> `npx` scaffolds a project instead of installing a skill. The table is in
> [You like one of these. Now what?](#you-like-one-of-these-now-what)

**Step 3 — put the style id in what you ask for.** It is not a flag; it is part of the
sentence:

```text
Use the soft-editorial template. Turn docs/roadmap.md into a 12-slide deck
for investors. I'll be speaking over it, so keep the text light.
```

That is it. **Naming the style id skips the picking step** — frontend-slides generates
three previews by default, and naming a template tells it not to ask. Want the options?
Don't name one; just ask for a deck.

Rather not read this page at all? The [next section](#let-an-agent-pick-for-you) installs
this repository as a skill and lets an agent choose for you.

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

<details open>
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
| **[PPT Master](https://github.com/hugohe3/ppt-master)**<br><sub>hugohe3</sub> | 53,817 | PPTX | MIT | Documents or topics into genuinely native, editable PowerPoint decks. |
| **[Slidev](https://github.com/slidevjs/slidev)**†<br><sub>slidevjs</sub> | 48,632 | Framework | MIT | A developer-focused framework for building presentation slides with Markdown and Vue. |
| **[Frontend Slides](https://github.com/zarazhangrui/frontend-slides)**<br><sub>Zara Zhang</sub> | 29,166 | HTML | MIT | Beautiful slides on the web using a coding agent's frontend skills. |
| **[Guizang PPT Skill](https://github.com/op7418/guizang-ppt-skill)**<br><sub>op7418 (歸藏)</sub> | 26,155 | HTML | ⚠️ AGPL-3.0 | Editorial-magazine and Swiss-International HTML decks, with design locked down by constraint. |
| **[Huashu Design](https://github.com/alchaincyf/huashu-design)**<br><sub>花生 (alchaincyf)</sub> | 24,084 | Both | MIT | HTML-native design skill — prototypes, decks, motion and design critique, not just slides. |
| **[Quarkdown](https://github.com/iamgio/quarkdown)**†<br><sub>iamgio</sub> | 16,105 | Framework | GPL-3.0 | A Markdown-based framework that produces papers, presentations, websites, and books from one source. |
| **[Banana Slides](https://github.com/Anionex/banana-slides)**†<br><sub>Anionex</sub> | 15,591 | PPTX | ⚠️ AGPL-3.0 | AI-native PPT generator that accepts templates, text prompts, or outlines and exports editable PPTX files. |
| **[Visual Explainer](https://github.com/nicobailon/visual-explainer)**<br><sub>nicobailon</sub> | 9,793 | HTML | MIT | Rich HTML pages or decks for diagrams, diff reviews, plan audits, data tables and project recaps. |
| **[HTML Anything](https://github.com/nexu-io/html-anything)**†<br><sub>nexu-io</sub> | 8,764 | Suite | Apache-2.0 | An agentic HTML editor with 75 skills across 9 surface types including decks, posters, and prototypes. |
| **[HTML PPT Studio](https://github.com/lewislulu/html-ppt-skill)**<br><sub>lewislulu</sub> | 8,331 | HTML | MIT | 24 themes, 31 layouts and 20+ animations for professional HTML presentations. |
| **[Dashi PPT Skill](https://github.com/chuspeeism/dashi-ppt-skill)**†<br><sub>chuspeeism</sub> | 8,067 | Both | ⚠️ AGPL-3.0 | Generates browser-editable presentations from multiple visual themes, exportable to HTML, PDF, and PPTX. |
| **[open-slide](https://github.com/1weiho/open-slide)**<br><sub>1weiho</sub> | 7,561 | Framework | MIT | A slide framework built for agents — React components on a fixed 1920x1080 canvas. |
| **[Codex PPT Skill](https://github.com/ningzimu/codex-ppt-skill)**†<br><sub>ningzimu</sub> | 5,809 | Image | MIT | Uses GPT-Image-2 to generate image-based PowerPoint slides within Codex and compatible agents. |
| **[Anthropic PPTX (official)](https://github.com/anthropics/skills/tree/main/skills/pptx)**<br><sub>Anthropic</sub> | 175,912* | PPTX | See repo | The official baseline — create, read, edit and combine PowerPoint files. |
| **[Baoyu Skills](https://github.com/JimLiu/baoyu-skills/tree/main/skills/baoyu-slide-deck)**†<br><sub>JimLiu (宝玉)</sub> | 25,847* | Suite | MIT | A 22-skill personal pack whose baoyu-slide-deck turns an article or outline into a deck. |

### Tier A — Production-ready (100–5k stars)

| Skill | ⭐ | Route | License | What it is |
|---|---:|---|---|---|
| **[Beautiful HTML Templates](https://github.com/zarazhangrui/beautiful-html-templates)**<br><sub>Zara Zhang</sub> | 4,545 | Templates | MIT | 34 HTML slide templates with index.json metadata so any agent can pick the right one. |
| **[Baoyu Design](https://github.com/JimLiu/baoyu-design)**†<br><sub>JimLiu</sub> | 4,016 | HTML | MIT | Runs Claude's Design system prompt locally to produce UI mockups, decks, and wireframes as self-contained HTML. |
| **[Codex Claude Academic Skills](https://github.com/zLanqing/codex-claude-academic-skills)**†<br><sub>zLanqing</sub> | 3,786 | Suite | MIT | Three-skill suite for researchers covering paper reading, PPT/Word generation, writing help, and scientific charts. |
| **[NanoBanana PPT Skills](https://github.com/op7418/NanoBanana-PPT-Skills)**†<br><sub>op7418</sub> | 3,245 | Image | Unspecified | AI skill that generates high-quality PPT slide images and videos with transitions and interactive playback. |
| **[Gorden PPT Skill](https://github.com/GordenSun/GordenPPTSkill)**†<br><sub>GordenSun</sub> | 3,076 | PPTX | NOASSERTION | Builds PPTX files from 17 Chinese templates by applying text edits defined in a JSON file, layouts intact. |
| **[Image to Editable PPT Skill](https://github.com/ningzimu/image-to-editable-ppt-skill)**†<br><sub>ningzimu</sub> | 2,466 | PPTX | MIT | Converts slide images, PDFs, and image-based PPTX files into editable PowerPoint decks. |
| **[Oh My PPT](https://github.com/arcsin1/oh-my-ppt)**†<br><sub>arcsin1</sub> | 1,953 | HTML | Apache-2.0 | Takes a text description and generates clean HTML slides locally, with no internet connection required. |
| **[Gorden Super PPT Skills](https://github.com/GordenSun/GordenSuperPPTSkills)**†<br><sub>GordenSun</sub> | 1,938 | PPTX | Unspecified | Generates high-quality PPT images with GPT and converts them into fully editable PPTX files. |
| **[CyberPPT](https://github.com/crazyykhllc-bit/CyberPPT)**†<br><sub>crazyykhllc-bit</sub> | 1,701 | PPTX | MIT | Codex skill for generating dense, editable consulting-style PowerPoint decks with SCR narrative and quality checks. |
| **[Ian Handdrawn PPT](https://github.com/helloianneo/ian-handdrawn-ppt)**†<br><sub>helloianneo</sub> | 1,412 | Image | MIT | Generates hand-drawn-style Chinese technical PPT slide images in PNG, with 21:9 covers and 16:9 body slides. |
| **[GPT Image2 PPT Skills](https://github.com/JuneYaooo/gpt-image2-ppt-skills)**†<br><sub>JuneYaooo</sub> | 1,271 | Image | Apache-2.0 | Clones a PPTX layout using gpt-image-2 so you can swap in your own content; includes 10 built-in styles. |
| **[PPT Image First](https://github.com/NyxTides/ppt-image-first)**†<br><sub>NyxTides</sub> | 1,208 | Image | Apache-2.0 | An image-first PPT generation skill for Codex, Claude Code, and Opencode CLI agents. |
| **[Humanize PPT](https://github.com/LearnPrompt/humanize-ppt)**†<br><sub>LearnPrompt</sub> | 934 | HTML | NOASSERTION | An AST-based outline director that structures human-centered AI presentation workflows. |
| **[PPT Agent Skills](https://github.com/sunbigfly/ppt-agent-skills)**†<br><sub>sunbigfly</sub> | 893 | HTML | NOASSERTION | A code-driven framework for generating presentations the same way you build software. |
| **[Codex Slides](https://github.com/nexu-io/codex-slides)** | 890 | Framework | MIT | AI slide studio for Codex: image-native decks, parallel render, and PDF/PPTX export. |
| **[Academic PPTX](https://github.com/Gabberflast/academic-pptx-skill)**<br><sub>Gabberflast</sub> | 869 | PPTX | MIT | Conference talks, seminar slides, thesis defenses and grant briefings. |
| **[Claude Office Skills](https://github.com/tfriedel/claude-office-skills)**<br><sub>tfriedel</sub> | 825 | PPTX | Unspecified | PPTX, DOCX, XLSX and PDF workflows with automation support. |
| **[Claude Skills](https://github.com/staruhub/ClaudeSkills)**†<br><sub>staruhub</sub> | 712 | Suite | MIT | A curated set of 13 Claude Code agent skills covering decks, research, PRDs, articles, and audits. |
| **[Power Design](https://github.com/ItsssssJack/power-design)**†<br><sub>ItsssssJack</sub> | 670 | HTML | NOASSERTION | A Claude skill that applies brand identity and 20 design principles to produce slides that look hand-crafted. |
| **[PPT Agent Workflow San](https://github.com/mucsbr/ppt-agent-workflow-san)**<br><sub>mucsbr</sub> | 638 | HTML | Unspecified | Progressive, interactive deck generation. |
| **[Frontend Slides Editable](https://github.com/archlizheng/frontend-slides-editable)**<br><sub>archlizheng</sub> | 497 | Both | MIT | Editable HTML decks with drag-resize, reordering, local save and PPTX conversion. |
| **[Paper2Anything](https://github.com/QuZhan51496/paper2anything)**†<br><sub>QuZhan51496</sub> | 423 | Suite | Apache-2.0 | Converts an academic paper PDF into slides, a poster, a webpage, a Xiaohongshu post, or a WeChat article. |
| **[RW Consulting PPT](https://github.com/Pikapika260214/rw-consulting-ppt)**†<br><sub>Pikapika260214</sub> | 422 | PPTX | MIT | A Codex skill for building editable consulting-style PowerPoint decks. |
| **[Reveal.js Skill](https://github.com/ryanbbrown/revealjs-skill)**†<br><sub>ryanbbrown</sub> | 405 | HTML | MIT | A coding agent skill for building reveal.js HTML presentations. |
| **[Visual Style PPT Skill](https://github.com/irenerachel/visual-style-ppt-skill)**†<br><sub>irenerachel</sub> | 386 | PPTX | Unspecified | A skill that runs a visual-style PPT generation workflow. |
| **[DOM to PPTX](https://github.com/atharva9167j/dom-to-pptx)**†<br><sub>atharva9167j</sub> | 350 | PPTX | MIT | Client-side library that converts any HTML element into a pixel-accurate, fully editable PowerPoint slide. |
| **[Beamer Skill](https://github.com/Noi1r/beamer-skill)**†<br><sub>Noi1r</sub> | 347 | HTML | MIT | Manages the full lifecycle of academic Beamer LaTeX slides: create, compile, review, quality score, and polish. |
| **[Marp Slides](https://github.com/robonuggets/marp-slides)**†<br><sub>robonuggets</sub> | 303 | HTML | Unspecified | MARP presentation skill with 22 example decks, SVG charts, and dark/light themes for Claude Code. |
| **[Beamer Academic](https://github.com/Faust-Donf/beamer-academic)**†<br><sub>Faust-Donf</sub> | 293 | HTML | MIT | Generates high-quality academic thesis defense Beamer slides from a paper with a single command. |
| **[Mck PPT Design System](https://github.com/likaku/Mck-ppt-design-skill)**<br><sub>likaku</sub> | 274 | PPTX | Apache-2.0 | Consulting-firm-style design system: 70 layout patterns, flat design, python-pptx. |
| **[Thesis Defense PPTX Skill](https://github.com/zouchenzhen/thesis-defense-pptx-skill)**†<br><sub>zouchenzhen</sub> | 260 | PPTX | Apache-2.0 | Generates an editable thesis-defense PPTX from a PDF or LaTeX source while preserving a chosen template. |
| **[PPT SVG Generator](https://github.com/vigorX777/ppt-svg-generator)**<br><sub>vigorX777</sub> | 258 | PPTX | MIT | Markdown to PPT or PDF via SVG, with preset styles. |
| **[Planners PPT Hell](https://github.com/thePlannerIvan/planners-ppt-hell)**†<br><sub>thePlannerIvan</sub> | 231 | PPTX | ⚠️ AGPL-3.0 | A PPT generation skill aimed at planners. |
| **[Apple Bento Grid](https://github.com/hubeiqiao/apple-bento-grid)**†<br><sub>hubeiqiao</sub> | 222 | HTML | MIT | Generates Apple-inspired bento grid presentation cards as HTML output. |
| **[Hands on Deck](https://github.com/EveryInc/hands-on-deck)**†<br><sub>EveryInc</sub> | 213 | PPTX | MIT | CLI tool that lets AI agents inspect, edit, create, and verify PPTX files through atomic JSON patches. |
| **[Codex PPT Skill](https://github.com/Ronnie2025/codex-ppt-skill)**†<br><sub>Ronnie2025</sub> | 212 | Image | MIT | Codex workflow for generating, composing, and SVG-decomposing Chinese business presentation slides. |
| **[Skywork Skills](https://github.com/SkyworkAI/Skywork-Skills)**†<br><sub>SkyworkAI</sub> | 204 | Suite | MIT | Agent skill suite covering AI PPT, documents, Excel, images, deep research, and music for any compatible agent. |
| **[PPT Image2 Editable Rebuild](https://github.com/wwe-dog/ppt-image2-editable-rebuild)**†<br><sub>wwe-dog</sub> | 201 | PPTX | Unlicense | Rebuilds editable PPTX files from screenshots or reference images by combining generated visuals with text shapes. |
| **[Claude Design Skill](https://github.com/jiji262/claude-design-skill)**†<br><sub>jiji262</sub> | 194 | HTML | MIT | Adapts Claude.ai's internal Design prompt locally to produce HTML decks, landing pages, prototypes, and posters. |
| **[Slide Image to Editable PPTX](https://github.com/w1163222589-coder/slide-image-to-editable-pptx)**†<br><sub>w1163222589-coder</sub> | 190 | PPTX | MIT | Converts slide screenshots into editable PowerPoint decks. |
| **[Magic Slide](https://github.com/daniel-style/magic-slide)**†<br><sub>daniel-style</sub> | 171 | HTML | MIT | Generates self-contained HTML presentations with smooth Magic Move-style transitions between slides. |
| **[Presentation Skills](https://github.com/Sven-LI-sankyuu/presentation-skills)**†<br><sub>Sven-LI-sankyuu</sub> | 171 | Both | Unspecified | Codex CLI skill collection for editable PPT diagram collaboration and web demo video synthesis workflows. |
| **[Servasyy Skills](https://github.com/huangserva/servasyy_skills)**†<br><sub>huangserva</sub> | 164 | Suite | Unspecified | A suite of AI skills covering writing, illustration, PPT, podcast, video, and comic generation. |
| **[PPT Agent Skill](https://github.com/Akxan/ppt-agent-skill)**<br><sub>Akxan</sub> | 147 | HTML | MIT | 26 styles and 18 chart types benchmarked against Linear, Anthropic, Stripe, Apple and NYT. |
| **[Future Slide](https://github.com/bytonylee/future-slide)**†<br><sub>bytonylee</sub> | 147 | Suite | Apache-2.0 | Ten slide skills split across plan, prompt and render, for both HTML and GPT-image decks. |
| **[Slide Deck Generator](https://github.com/code-on-sunday/slide-deck-generator)**†<br><sub>code-on-sunday</sub> | 145 | HTML | MIT | Creates browser-based slide decks using React, Vite, and Framer Motion from a coding agent prompt. |
| **[Make Slide](https://github.com/Kuneosu/make-slide)**†<br><sub>Kuneosu</sub> | 123 | HTML | MIT | Generates standalone HTML slide decks from a prompt. |
| **[HTML PPT Designer](https://github.com/andyhuo520/html-ppt-designer)**†<br><sub>andyhuo520</sub> | 119 | HTML | Unspecified | Converts any content into polished HTML presentations. |
| **[PowerPoint Skill](https://github.com/Noi1r/powerpoint-skill)**†<br><sub>Noi1r</sub> | 118 | PPTX | MIT | Creates PPTX presentations with native math, LaTeX formulas, and Graphviz/Mermaid/TikZ diagrams. |
| **[Presentation Skills](https://github.com/pamelafox/presentation-skills)**†<br><sub>pamelafox</sub> | 117 | HTML | MIT | AI agent skills for processing and generating presentations, aimed at teachers and speakers. |
| **[Image to PPTX Skill](https://github.com/knight6669/knight-imagetopptx-skill)**†<br><sub>knight6669</sub> | 108 | PPTX | MIT | Converts slide images into editable PowerPoint files using semantic understanding. |
| **[Literature Report PPT Builder](https://github.com/fangyuanopus/literature-report-ppt-builder)**†<br><sub>fangyuanopus</sub> | 107 | PPTX | MIT | Generates academic literature-report PowerPoint decks from research content. |
| **[AI Skills (Cross-Platform)](https://github.com/sanjay3290/ai-skills/tree/main/skills/google-slides)**†<br><sub>sanjay3290</sub> | 422* | Suite | Apache-2.0 | 24 cross-platform agent skills for Claude Code, Cursor and Codex, including Google Slides. |

### Tier B — Specialized & emerging (<100 stars)

| Skill | ⭐ | Route | License | What it is |
|---|---:|---|---|---|
| **[CN Academic Spark](https://github.com/wycmochi/cn-academic-spark)**†<br><sub>wycmochi</sub> | 94 | PPTX | MIT | Generates editable academic PPTX from uploaded papers for thesis, lab, and course presentations. |
| **[Starry Slides](https://github.com/StarryKit/starry-slides)**<br><sub>StarryKit</sub> | 92 | Framework | MIT | Slide editor that gives your agent fully editable decks with HTML as the source file. |
| **[AI Paper to Slide Skill](https://github.com/Leo1998-Lu/ai-paper2slide-skill)**†<br><sub>Leo1998-Lu</sub> | 87 | PPTX | MIT | Converts AI research papers into conference-grade PowerPoint slide decks. |
| **[Lieflat HTML Design](https://github.com/larashero3-dotcom/lieflat-html-design)**†<br><sub>larashero3-dotcom</sub> | 86 | HTML | MIT | Produces HTML slide decks and Xiaohongshu cards via agent-ready design skills. |
| **[Knowledge Cat PPT Skill](https://github.com/gnipbao/knowledge-cat-ppt-skill)**†<br><sub>gnipbao</sub> | 84 | Both | MIT | Creates and QA-checks PPT, HTML, and image-first decks using a story-first approach. |
| **[Visual Cognition Slides](https://github.com/edu-ai-builders/visual-cognition-slides)**<br><sub>edu-ai-builders</sub> | 83 | HTML | MIT | Slide design grounded in cognitive science and instructional design, optimized for retention. |
| **[PPT Report Skills](https://github.com/myunwang/ppt-report-skills)**†<br><sub>myunwang</sub> | 81 | HTML | MIT | Builds web-based report decks with ECharts charts, per-slide files, and PDF/image export. |
| **[HTML Slides](https://github.com/bluedusk/html-slides)**<br><sub>bluedusk</sub> | 79 | HTML | MIT | HTML slides with speaker notes, plus a companion presentation app. |
| **[SJTU PPT Template Skill](https://github.com/ACTAshui/sjtu-ppt-template-skill)**†<br><sub>ACTAshui</sub> | 78 | PPTX | Unspecified | Creates editable PowerPoint decks styled after Shanghai Jiao Tong University templates. |
| **[Space Multi Design PPT](https://github.com/SpaceZephyr/space-multi-design-ppt)**†<br><sub>SpaceZephyr</sub> | 76 | PPTX | Unspecified | Generates branded slide decks following a design system via Codex. |
| **[Deck Factory](https://github.com/gongnyang/deck-factory)**†<br><sub>gongnyang</sub> | 75 | HTML | MIT | Turns a one-line prompt into a dark-editorial HTML presentation deck. |
| **[Awesome PPT Skills](https://github.com/stevenjinlong/awesome-ppt-skills)**†<br><sub>stevenjinlong</sub> | 65 | Image | Unspecified | Converts a text prompt into full-slide PPT decks rendered as images via gpt-image-2. |
| **[HTML to Editable PPTX](https://github.com/Hasasasa/html-to-editable-pptx)**†<br><sub>Hasasasa</sub> | 65 | PPTX | MIT | Converts HTML slide decks to PPTX with native text boxes rather than screenshot images. |
| **[Editable Image to PPT Skill](https://github.com/soulmujoco/EditableImage2PPTSkill)**†<br><sub>soulmujoco</sub> | 64 | PPTX | MIT | Converts PPT slide images into editable PowerPoint decks. |
| **[Huawei Style PPT Skill](https://github.com/zuiho-kai/huawei-style-ppt-skill)**<br><sub>zuiho-kai</sub> | 63 | HTML | Custom | High-information-density decks in the Huawei corporate idiom. |
| **[Presentation](https://github.com/appautomaton/presentation)**†<br><sub>appautomaton</sub> | 57 | Both | Unspecified | Turns a business question into a consulting-grade deck via four composable skills for PDF and PPTX. |
| **[KingDee PPT Skill](https://github.com/WayneZhon/KingDee-PPT-Skill)**<br><sub>WayneZhon</sub> | 56 | HTML | MIT | KingDee corporate style decks. |
| **[Presentation Skill](https://github.com/siril9/presentation-skill)**†<br><sub>siril9</sub> | 53 | PPTX | MIT | Source-first Codex skill that generates editable PPTX decks with style routing and QA. |
| **[next-slide](https://github.com/codesstar/next-slide)**<br><sub>codesstar</sub> | 50 | HTML | MIT | 26+ styles, zero dependencies, bilingual. |
| **[Slide Creator](https://github.com/kaisersong/slide-creator)**<br><sub>kaisersong</sub> | 49 | Both | Unspecified | AI planning, style discovery and PPTX export. |
| **[Baoyu Xuanyi Skills](https://github.com/xuanxuan1983/baoyu-xuanyi-skills)**†<br><sub>xuanxuan1983</sub> | 45 | Templates | Unspecified | Combines Baoyu's agent skills with seven PPT style templates. |
| **[Slide Wright](https://github.com/arifszn/slide-wright)**†<br><sub>arifszn</sub> | 45 | HTML | MIT | Generates unique reveal.js HTML slide decks with a distinct design for each prompt. |
| **[Slide Writer](https://github.com/FeeiCN/slide-writer)**<br><sub>FeeiCN</sub> | 41 | HTML | MIT | Enterprise HTML decks from ideas, outlines, documents or speech drafts. |
| **[Jiarui SVG Skills](https://github.com/shenxiaofeng-pro/jiarui-svg-skills)**†<br><sub>shenxiaofeng-pro</sub> | 41 | Image | Unspecified | Generates branded SVG slide images with company logo, colors, and logical structure for use in PPT. |
| **[Paper PPT Skill](https://github.com/xiao634zhang/paper-ppt-skill)**†<br><sub>xiao634zhang</sub> | 41 | PPTX | Unspecified | Generates clean academic slides from a PDF paper, supporting templates, speaker notes, and images. |
| **[Slidev Skills](https://github.com/yoanbernabeu/slidev-skills)**†<br><sub>yoanbernabeu</sub> | 39 | Framework | MIT | Twenty AI agent skills for building presentations with the Slidev framework. |
| **[Codex Image to Editable PPT](https://github.com/wiltonesten-web/codeximage-to-editable-ppt-v1)**†<br><sub>wiltonesten-web</sub> | 39 | PPTX | MIT | Rebuilds image-based PPT slides into editable PowerPoint decks via Codex. |
| **[30x McKinsey Research Deck](https://github.com/norahe0304-art/30x-mckinsey-research-deck)**†<br><sub>norahe0304-art</sub> | 39 | PPTX | MIT | Turns a research prompt into a McKinsey-style market research deck with adversarially verified data using a multi-agent pipeline. |
| **[Claude Code Codex Slide](https://github.com/phodal/claude-code-codex-slide)**†<br><sub>phodal</sub> | 38 | HTML | Unspecified | Analyzes Claude Code source code via Codex and presents findings as GPT-generated slides. |
| **[Slides AI Plugin](https://github.com/proyecto26/slides-ai-plugin)**†<br><sub>proyecto26</sub> | 38 | Both | MIT | Turns a single prompt into an animated HTML or editable PowerPoint presentation. |
| **[PPT Skill](https://github.com/AIPMAndy/PPTskill)**†<br><sub>AIPMAndy</sub> | 37 | PPTX | MIT | Generates native editable PowerPoint files without requiring any design skills. |
| **[HTML to PPT PDF](https://github.com/wangzan101/html-to-ppt-pdf)**†<br><sub>wangzan101</sub> | 36 | Both | MIT | Converts HTML slide decks to PDF and image-based PPTX for offline use. |
| **[Scholar PPT CN](https://github.com/deathcats4/scholar-ppt-cn)**†<br><sub>deathcats4</sub> | 36 | PPTX | MIT | Converts academic papers to editable PowerPoint with planning tables and mockup layouts via Codex. |
| **[Beautiful Hackathon Slides](https://github.com/Esther2524/beautiful-hackathon-slides)**†<br><sub>Esther2524</sub> | 35 | HTML | MIT | Creates bold-design HTML pitch decks suited for hackathon presentations. |
| **[BL Captain PPT Skill](https://github.com/dososo/blcaptain-ppt-skill)**†<br><sub>dososo</sub> | 35 | HTML | NOASSERTION | Produces single-file HTML decks across 7 design personas with machine-enforced WCAG compliance. |
| **[Image PPT King](https://github.com/TateZhouSiu/image-ppt-king)**†<br><sub>TateZhouSiu</sub> | 34 | PPTX | MIT | Converts slide screenshots and generated images into editable PPTX with OCR evidence and QA. |
| **[PowerPoint Fancy Design](https://github.com/Phlegonlabs/Powerpoint-fancy-design)**<br><sub>Phlegonlabs</sub> | 33 | Both | Unspecified | Page-structured Markdown into styled 1600x900 HTML slides, PNG renders and exports. |
| **[Skills Slides](https://github.com/nghiahsgs/skills-slides)**<br><sub>nghiahsgs</sub> | 32 | HTML | Unspecified | 50 aesthetics x 20 palettes x 10 fonts x 5 layouts x 30+ effects. |
| **[ImageGen PPTX Pipeline](https://github.com/eddyzzl/imagegen-pptx-pipeline)**†<br><sub>eddyzzl</sub> | 32 | PPTX | MIT | Generates editable PPTX decks using image generation and converts slide images to PowerPoint. |
| **[Narrative Engine](https://github.com/nraford7/Narrative-Engine)**†<br><sub>nraford7</sub> | 31 | HTML | Unspecified | Transforms content into HTML slide decks built on storytelling and communication frameworks. |
| **[PPT Design DNA](https://github.com/dakjdakd/PPT-Design-DNA)**†<br><sub>dakjdakd</sub> | 31 | HTML | Apache-2.0 | Extracts visual style from reference images into Design Profiles, then applies those to HTML decks. |
| **[PPTX from Layouts](https://github.com/tristan-mcinnis/pptx-from-layouts-skill)**<br><sub>tristan-mcinnis</sub> | 30 | PPTX | MIT | Generate decks from markdown strictly through a template's slide master layouts. |
| **[PPTX Template Skills](https://github.com/CxyZyr/PPTX-Template-Skills)**†<br><sub>CxyZyr</sub> | 29 | PPTX | MIT | Parses a PowerPoint template into a machine-readable contract, then fills it with new content to produce a completed deck. |
| **[PPT Creator Skills](https://github.com/Yu-0312/ppt-creater-skills)**†<br><sub>Yu-0312</sub> | 26 | PPTX | NOASSERTION | A Claude Code skill for creating PowerPoint presentations. |
| **[Presentation Skill](https://github.com/OrangeViolin/presentation-skill)**†<br><sub>OrangeViolin</sub> | 25 | HTML | Unspecified | Takes a topic and generates a playable HTML slideshow in one of 62 brand design styles. |
| **[Econ Empirical Paper PPT Skill](https://github.com/1793065778/econ-empirical-paper-ppt-skill)**†<br><sub>1793065778</sub> | 25 | PPTX | Unspecified | Converts empirical economics papers into structured presentation blueprints ready for PowerPoint. |
| **[Beamer Skill](https://github.com/JaxonJP/beamer-skill)**†<br><sub>JaxonJP</sub> | 23 | HTML | MIT | Full-lifecycle skill for academic Beamer LaTeX presentations: compile, review, QA, and TikZ audit. |
| **[Jingge Sense Deck](https://github.com/jxshow/Jingge-PPT-sense-deck-skill)**†<br><sub>jxshow</sub> | 23 | HTML | Unspecified | HTML deck skill focused on a consistent visual sense across slides. |
| **[Keynote Slides Skill](https://github.com/dbmcco/keynote-slides-skill)**†<br><sub>dbmcco</sub> | 22 | HTML | Unspecified | Generates HTML-based presentation slides in a Keynote style. |
| **[PPT Agent](https://github.com/joker-sxj/ppt-agent)**†<br><sub>joker-sxj</sub> | 22 | Both | MIT | Converts a topic into an editable .pptx file and full-page SVG web preview through a six-stage pipeline. |
| **[Slide Design Skill](https://github.com/SlideSpeak/slide-design-skill)**†<br><sub>SlideSpeak</sub> | 21 | HTML | MIT | Takes a deck description and renders 1920x1080 HTML slides with a derived style, real charts, tables, and images. |
| **[Claude HTML Slide Builder](https://github.com/mathruffian-dot/claude-html-slide-builder)**†<br><sub>mathruffian-dot</sub> | 21 | HTML | MIT | Converts teaching materials into interactive Reveal.js HTML slides and deploys them to GitHub Pages. |
| **[AI Draw Skill](https://github.com/stone-yu/ai-draw-skill)**†<br><sub>stone-yu</sub> | 21 | HTML | Unspecified | Turns text, links, images, or PDFs into an HTML slide deck or diagram, with 36 PPT themes and 12 diagram themes. |
| **[HTML to PPTX](https://github.com/Emily27-alt/html-to-pptx)**†<br><sub>Emily27-alt</sub> | 20 | PPTX | MIT | Converts HTML slide decks into editable .pptx files using native shapes, not screenshots. |
| **[Neon Slides](https://github.com/lqshow/neon-slides)**†<br><sub>lqshow</sub> | 20 | HTML | MIT | Turns a text outline into a neon-dark themed HTML slide deck for technical presentations. |
| **[Create HTML Deck](https://github.com/awesome-skills/create-html-deck)**†<br><sub>awesome-skills</sub> | 19 | HTML | MIT | Builds and verifies browser-native HTML presentations for display on laptops and projectors. |
| **[GZR NSFC PPT Skill](https://github.com/admithuman/gzr-nsfc-ppt-skill)**†<br><sub>admithuman</sub> | 19 | PPTX | MIT | Generates professional academic defense slides in the style of NSFC grant presentations. |
| **[Interactive Slides](https://github.com/sylvial928/interactive-slides)**†<br><sub>sylvial928</sub> | 18 | HTML | MIT | Creates animated, interactive web presentations with style presets, brand kit support, and one-click PowerPoint export. |
| **[Excalidraw Slides Generator](https://github.com/ZunbaRan/excalidraw-slides-skills)**†<br><sub>ZunbaRan</sub> | 18 | Framework | Unspecified | Two-phase workflow that turns text into 16:9 Excalidraw slides with generated SVG art. |
| **[MBB Decks](https://github.com/floflo11/mbb-decks)**†<br><sub>floflo11</sub> | 17 | PPTX | MIT | Produces MBB-style consulting .pptx decks with action-title slides, MECE bullets, and company logos as bullet markers. |
| **[KAI Presentation](https://github.com/yevvonlim/kai-presentation)**†<br><sub>yevvonlim</sub> | 16 | HTML | Unspecified | Generates KAI-branded HTML presentation decks from prompts. |
| **[Four-Up PPT Generator](https://github.com/woniuniuniu/four-up-ppt-generator)**†<br><sub>woniuniuniu</sub> | 15 | PPTX | ⚠️ AGPL-3.0 | Generates four-slide-per-page PPTX layouts, based on the guizang-ppt-skill. |
| **[Keynot](https://github.com/shawnzam/keynot)**†<br><sub>shawnzam</sub> | 15 | HTML | MIT | Converts any prompt into a self-contained HTML slide deck without requiring Keynote or PowerPoint. |
| **[Competition PPT Template Skill](https://github.com/che626/competition-ppt-template-first-skill)**†<br><sub>che626</sub> | 14 | PPTX | MIT | Generates editable PPTX competition and defense presentations with real evidence using a template-first approach. |
| **[NanoBanana PPT Skills](https://github.com/girish6055/NanoBanana-PPT-Skills)**†<br><sub>girish6055</sub> | 14 | PPTX | Unspecified | Generates PPT files with AI-driven smart transitions and interactive playback. |
| **[PPT Image Share Builder](https://github.com/uuoov/ppt-image-share-builder)**†<br><sub>uuoov</sub> | 14 | Image | MIT | Generates PPT page images, QA contact sheets, PPTX wrappers, and timed scripts from image inputs. |
| **[Japanese Corporate PPTX Skill](https://github.com/gonta223/japanese-corporate-pptx-skill)**†<br><sub>gonta223</sub> | 14 | PPTX | MIT | Generates corporate-style PPTX presentations in Japanese. |
| **[CyberBin PPT Skill](https://github.com/caikankan/cyberbin-ppt-skill)**†<br><sub>caikankan</sub> | 14 | HTML | ⚠️ AGPL-3.0 | Generates local HTML slide decks from prompts. |
| **[PPT Skill](https://github.com/lgwanai/ppt-skill)**†<br><sub>lgwanai</sub> | 14 | HTML | Unspecified | Generates HTML slide decks with style cloning, built-in commercial SVG assets, and expert layout knowledge. |
| **[Econ Slides Skill](https://github.com/hanlulong/econ-slides-skill)**<br><sub>hanlulong</sub> | 14 | Framework | MIT | Turns an economics paper into a Beamer seminar talk, with a timed speaker script. |
| **[NanoBanana PPT Skills](https://github.com/xj-bear/NanoBanana-PPT-Skills)**†<br><sub>xj-bear</sub> | 13 | PPTX | Unspecified | Generates PPT files with AI, including support for Veo video content. |
| **[Fudan University PPT Skill](https://github.com/JZCreative/Fudan-University-PPT-skill)**†<br><sub>JZCreative</sub> | 13 | Both | Unspecified | Generates Fudan University branded academic slides as native PPTX or self-contained HTML, with built-in logo and color assets. |
| **[OpenCode PPT Studio](https://github.com/Honghurumeng/oc_sdk_ppt)**†<br><sub>Honghurumeng</sub> | 13 | Both | Unspecified | Web app that drafts an outline, refines it in a second session, then builds HTML and PPTX. |
| **[HalfAI Gufa PPT](https://github.com/HalfAI1102/HalfAI-gufappt)**†<br><sub>HalfAI1102</sub> | 12 | PPTX | MIT | Generates traditional-style editable PPTX files suited for school, workplace, and defense presentations. |
| **[Better PPT HTML Deck](https://github.com/ziguishian/better-ppt-html-deck)**†<br><sub>ziguishian</sub> | 12 | HTML | MIT | Confirms visual direction first, then generates an editable, previewable, and exportable HTML presentation. |
| **[McKinsey HTML Design Skill](https://github.com/likaku/mck-html-design-skill)**†<br><sub>likaku</sub> | 12 | HTML | Apache-2.0 | Generates McKinsey-style HTML presentations using Python, with 68 built-in layouts and no dependencies. |
| **[TalkTrack](https://github.com/RuiqiWang-LGD/TalkTrack--)**†<br><sub>RuiqiWang-LGD</sub> | 12 | PPTX | Unspecified | Converts PDFs, PPTs, or images into a companion slide deck with readable speaking notes and page-turn cues. |
| **[AWS HTML Slides](https://github.com/lanceli93/aws-html-slides)**†<br><sub>lanceli93</sub> | 11 | HTML | MIT | Creates animation-rich HTML presentations from scratch or converts existing PowerPoint files. |
| **[Prada Slides](https://github.com/prodigeproject/pradaslides)**†<br><sub>prodigeproject</sub> | 11 | Both | MIT | Generates PPTX, HTML slides, and PDFs, and handles deck planning for a given audience. |
| **[Editable Leadership PPTX](https://github.com/CamelKing1997/editable-leadership-pptx)**†<br><sub>CamelKing1997</sub> | 11 | PPTX | Apache-2.0 | Builds editable leadership, executive, and project update PPTX slides with repo-backed evidence and screenshot QA. |
| **[Paper Figure PPTX Skill](https://github.com/fengting124/paper-figure-pptx-skill)**†<br><sub>fengting124</sub> | 11 | PPTX | MIT | Reconstructs figures from academic papers into editable, LibreOffice-validated PPTX slides. |
| **[Competition PPT Skill](https://github.com/2750527986liu-maker/competition-ppt-skill)**†<br><sub>2750527986liu-maker</sub> | 11 | PPTX | Unspecified | Generates pitch-deck slides for the China International College Student Innovation Competition using python-pptx and PIL. |
| **[SlideStage Pack](https://github.com/SlideStage/slidestage-pack)**†<br><sub>SlideStage</sub> | 10 | HTML | Unspecified | Packages HTML slides into a distributable bundle for sharing or deployment. |
| **[Deckset Claude Skill](https://github.com/doudou1337/deckset-claude-skill)**†<br><sub>doudou1337</sub> | 10 | HTML | MIT | Takes markdown input and generates Deckset presentation files with documentation and examples. |
| **[IML PPTX](https://github.com/tangonho/iml-pptx)**†<br><sub>tangonho</sub> | 10 | PPTX | Unspecified | Rebuilds text and slide images into fully editable PowerPoint files with native text boxes and shapes. |
| **[HTML to PPTX Skill](https://github.com/artifact-kit/html-to-pptx-skill)**†<br><sub>artifact-kit</sub> | 10 | PPTX | Unspecified | Converts HTML pages into downloadable, editable PowerPoint decks. |
| **[SlideSmith](https://github.com/aryankumawat/SlideSmith-Multi-Agent-AI-Slide-Maker-)**†<br><sub>aryankumawat</sub> | 10 | Both | Unspecified | Multi-agent system that generates slide decks with quality checks and export to multiple formats. |
| **[Guizang PPT Skill](https://github.com/alingowangxr/guizang-ppt-skill)**†<br><sub>alingowangxr</sub> | 10 | HTML | MIT | Generates web-based presentations, slide illustrations, and social media covers, with Traditional and Simplified Chinese support. |
| **[Aham PPT](https://github.com/Aham-AIAPP/aham-ppt)**†<br><sub>Aham-AIAPP</sub> | 10 | PPTX | MIT | A restrained AI skill with a parameterized layout library that outputs clean, editable .pptx files. |
| **[High Quality Slides](https://github.com/andyqiu847-ai/high-quality-slides)**†<br><sub>andyqiu847-ai</sub> | 10 | HTML | MIT | A research-first, narrative-driven 5-phase Claude Code skill that generates polished HTML presentations. |
| **[Bento PPT Skill](https://github.com/YingYveltal/bento-ppt-skill)**†<br><sub>YingYveltal</sub> | 9 | Both | MIT | Turns a topic into a 16:9 Bento Grid SVG slide deck with an HTML preview and editable PowerPoint export. |
| **[Presentation Chef](https://github.com/sacredvoid/presentation-chef)**†<br><sub>sacredvoid</sub> | 9 | HTML | MIT | Converts any content into an Apple Keynote-style self-contained HTML presentation with cinematic animations. |
| **[Paper to LaTeX PPT](https://github.com/moyoo0/paper-to-latex-ppt)**†<br><sub>moyoo0</sub> | 9 | HTML | MIT | Takes an academic paper as input and outputs a slide deck with speaker notes for group meeting presentations. |
| **[SOIL Deck Skills](https://github.com/mathruffian-dot/soil-deck-skills)**†<br><sub>mathruffian-dot</sub> | 9 | Both | MIT | Generates teaching slide decks as full-image PPTX, editable PPTX, or interactive HTML from a single agent skill. |
| **[Hand-Drawn PPT Skill](https://github.com/danny0926/ppt-skills)**†<br><sub>danny0926</sub> | 8 | Both | Unspecified | Generates text-to-PPTX slides in a hand-drawn rough.js style with visual-first layouts and dual editable layers. |
| **[HTML PPT Skill](https://github.com/chenyangji666/html-ppt-skill)**†<br><sub>chenyangji666</sub> | 8 | Framework | MIT | A pure HTML/CSS/JS presentation engine with an AI generation protocol for creating slide decks. |
| **[HTML to PPTX](https://github.com/nlj626/html-to-pptx)**†<br><sub>nlj626</sub> | 8 | PPTX | MIT | Converts HTML presentations made with html-ppt into downloadable PPTX files in one step. |
| **[PPT Expert Team](https://github.com/ThunderOne18/ppt-expert-team)**†<br><sub>ThunderOne18</sub> | 8 | Both | NOASSERTION | An eight-step workflow skill that turns articles or scripts into editable HTML, image, or PPTX slides across six styles. |
| **[Modern PPT](https://github.com/lainshao/modern-ppt)**†<br><sub>lainshao</sub> | 8 | HTML | ⚠️ AGPL-3.0 | Produces single-file HTML presentations with 12 layouts, 3 themes, and interactive charts, compatible with major AI coding agents. |
| **[Presentation Forge](https://github.com/thmsgo18/presentation-forge)**†<br><sub>thmsgo18</sub> | 8 | HTML | MIT | Builds self-contained HTML slide decks and imports brand themes from PowerPoint files, images, or descriptions. |
| **[Notrat PPT Studio](https://github.com/NestMold/notrat-ppt-studio-skill)**†<br><sub>NestMold</sub> | 8 | Both | MIT | Creates, edits, and reviews PowerPoint files with image, native-editable, and hybrid output modes plus animations. |
| **[USTC PPT Template](https://github.com/zsc58/ustc-ppt-template)**†<br><sub>zsc58</sub> | 8 | Templates | NOASSERTION | Provides a 15-slide blue academic PPT template for USTC with navigation links and a LaTeX pipeline. |
| **[AI Editable PPT Skill](https://github.com/iwbaga724-Hinda/ai-editable-ppt-skill)**†<br><sub>iwbaga724-Hinda</sub> | 7 | PPTX | Unspecified | Creates editable PowerPoint presentations from reports, outlines, templates, or AI-generated slide images. |
| **[Vela Slides](https://github.com/AgentiaPT/vela-slides)**†<br><sub>AgentiaPT</sub> | 7 | HTML | NOASSERTION | An AI-powered app and agent skill for generating HTML slide presentations. |
| **[Bruce PPTX Generator](https://github.com/bruc3van/bruce-pptx-generator)**†<br><sub>bruc3van</sub> | 7 | PPTX | Unspecified | An agent skill that generates professional PowerPoint files from scratch via code, based on user requirements. |
| **[Tekion Slide Generator](https://github.com/rsensui2/tekion-slide-generator)**†<br><sub>rsensui2</sub> | 7 | Both | MIT | Converts Markdown into 16:9 2K slides and exports to PPTX or PDF using OpenAI or Gemini image generation. |
| **[PPT Master](https://github.com/Categorytyy/ppt-master)**†<br><sub>Categorytyy</sub> | 6 | HTML | MIT | An agent skill for generating HTML slide presentations. |
| **[PPT Image to Editable](https://github.com/L-Luke-L/ppt-image-to-editable)**†<br><sub>L-Luke-L</sub> | 6 | PPTX | Unspecified | A Codex skill that splits AI-generated slide images and reconstructs them as editable PPTX files. |
| **[PPT Skills](https://github.com/CacinieP/ppt-skills)**†<br><sub>CacinieP</sub> | 6 | PPTX | MIT | Generates themed, CJK-aware, editable PPTX files via PptxGenJS. |
| **[Research Group PPT Skill](https://github.com/lirouroud/research-group-ppt-skill)**†<br><sub>lirouroud</sub> | 6 | HTML | Unspecified | Reads research progress materials, outputs a page-by-page outline for review, then generates a flippable HTML report. |
| **[Paper to Scholar Slides](https://github.com/ficooooo/Paper2ScholarSlides)**†<br><sub>ficooooo</sub> | 6 | PPTX | MIT | Converts a literature review draft and paper materials into a structured academic PPTX with citations and figures. |
| **[Xidian Slides Skill](https://github.com/perper999/xidian-slides-skill)**†<br><sub>perper999</sub> | 5 | HTML | Unspecified | Generates zero-dependency HTML presentations styled to Xidian University's official visual guidelines. |
| **[Paper to Slides Skill](https://github.com/inhyeoklee/paper2slides-skill)**†<br><sub>inhyeoklee</sub> | 5 | HTML | MIT | Takes a scientific paper PDF and produces a presentation slide deck. |
| **[Editable PPTX Skill](https://github.com/Liuguanyi2125/editable-pptx-skill)**†<br><sub>Liuguanyi2125</sub> | 5 | PPTX | MIT | Generates layered, fully editable PowerPoint files from a Claude Code or Codex agent skill. |
| **[Pitch Deck Iterator](https://github.com/MiraclePlus/pre-pp)**†<br><sub>MiraclePlus</sub> | 5 | PPTX | MIT | Iteratively refines pitch deck PPTX files through a Claude Code skill workflow. |
| **[Zhongguose PPT Skill](https://github.com/tanglele110-hash/zhongguose-ppt-skill)**†<br><sub>tanglele110-hash</sub> | 5 | PPTX | MIT | Creates presentation slides styled with traditional Chinese color palettes. |
| **[ZJ Lab Academic PPTX Skills](https://github.com/qianmo-qp/zjlab-academic-pptx-sklls)**†<br><sub>qianmo-qp</sub> | 5 | PPTX | Unspecified | Generates PPTX slides for laboratory technical or academic reports. |
| **[Consulting Diagnosis PPT Skill](https://github.com/Carl-Marks/consulting-diagnosis-ppt-skill)**†<br><sub>Carl-Marks</sub> | 5 | HTML | Unspecified | Runs a six-stage workflow from raw inputs through business analysis to a finished consulting diagnosis HTML deck. |
| **[Token Slides](https://github.com/pku-lemonade/TokenSlides)**†<br><sub>pku-lemonade</sub> | 5~ | Framework | Apache-2.0 | A Typst slide theme with Codex skills that converts academic papers into presentation slides. |
| **[Slide Weaver](https://github.com/RFYoung/slideweaver)**†<br><sub>RFYoung</sub> | 5 | PPTX | MIT | Generates academic report presentations end-to-end with minimal manual input. |
| **[PPT Template Fill](https://github.com/xiongwenhao112/ppt-template-fill)**†<br><sub>xiongwenhao112</sub> | 5 | PPTX | MIT | Fills a user-supplied PPTX template with AI-generated content while preserving the original layout. |
| **[SlideSage](https://github.com/vedraut/slidesage)**†<br><sub>vedraut</sub> | 5 | PPTX | MIT | Generates static .pptx decks from content using storytelling and instructional design principles. |
| **[KR Brand Decks](https://github.com/sylvanus4/kr-brand-decks)**<br><sub>sylvanus4</sub> | 5~ | Templates | NOASSERTION | 23 skills, one per Korean enterprise brand, each building an on-brand PPTX from scratch. |
| **[Web PPT](https://github.com/includewudi/web-ppt)**†<br><sub>includewudi</sub> | 4 | HTML | Unspecified | Generates self-contained HTML presentations that open directly in a browser and support video recording. |
| **[Codex XKPPT Skill](https://github.com/MURMURE11118586/codex-xkppt-skill)**†<br><sub>MURMURE11118586</sub> | 4 | PPTX | MIT | Generates editable presentations from topics, documents, PDFs, or Markdown, with template application and QA checks. |
| **[PPT Design Skill](https://github.com/billLiao/PPT-Design-Skill)**†<br><sub>billLiao</sub> | 4 | PPTX | Unspecified | Combines multiple design styles to generate .pptx files directly rather than HTML output. |
| **[PowerPoint Skill](https://github.com/Shimonimposed141/powerpoint-skill)**†<br><sub>Shimonimposed141</sub> | 4 | PPTX | MIT | Converts academic papers into PowerPoint presentations with native math rendering, diagrams, and multi-stage analysis. |
| **[HFUT Presentation Studio](https://github.com/linmohan00-rgb/hfut-presentation-studio)**†<br><sub>linmohan00-rgb</sub> | 4 | PPTX | Unspecified | Creates HFUT-styled red-and-white classroom slides from topics, screenshots, or existing materials, with layout and script review. |
| **[SJTU Beamer PPT](https://github.com/YarthsA/sjtu-beamer-ppt)**†<br><sub>YarthsA</sub> | 4 | HTML | Unspecified | Generates LaTeX Beamer presentations in the SJTU house style using the SJTUBeamer template. |
| **[Special Achievement Report](https://github.com/xxxd666/special-achievement-report)**†<br><sub>xxxd666</sub> | 4 | HTML | MIT | Generates consulting-grade achievement reports using 9 methodologies in a single Claude skill. |
| **[HTML PPT Academic Skill](https://github.com/w1ndys/html-ppt-academic-skill)**†<br><sub>w1ndys</sub> | 4 | HTML | MIT | Creates static HTML slides for academic contexts: thesis defenses, progress reports, and conference talks. |
| **[Frontend Slides](https://github.com/dreamid27/frontend-slides)**†<br><sub>dreamid27</sub> | 4 | HTML | MIT | Creates animation-rich HTML presentations from scratch or converts PowerPoint files, with 88 layout presets and 34 templates. |
| **[Economics Empirical PPT Skill](https://github.com/jialiruo-png/economics-empirical-ppt-skill)**†<br><sub>jialiruo-png</sub> | 4 | PPTX | Unspecified | Generates PPTX presentations for economics, finance, and empirical research papers, with interactive prompts for page count, word count, and style. |
| **[CUHK Slides Template (HTML)](https://github.com/HarlandZZC/cuhk-slides-template-html)**<br><sub>HarlandZZC</sub> | 4 | Templates | MIT | One self-contained HTML slide template in CUHK colours, plus a Markdown-to-slides skill. |
| **[HTML Report Generator](https://github.com/hpuhsp/html-report-generator)**†<br><sub>hpuhsp</sub> | 3 | HTML | Unspecified | Generates professional HTML presentations on any topic using live web research, with multiple style options and cited sources. |
| **[Demo Prep Skill](https://github.com/MohamedBIqbal/demo-prep-skill)**†<br><sub>MohamedBIqbal</sub> | 3 | Both | MIT | Produces McKinsey-style HTML presentations or PowerPoint files for product demos, with a built-in timer. |
| **[Avatar PPT Master](https://github.com/sadfrog71/avatar-ppt-master)**†<br><sub>sadfrog71</sub> | 3 | HTML | ⚠️ AGPL-3.0 | A fork of dashi-ppt with improved content generation and third-party images removed. |
| **[HTML PPT Video Skill](https://github.com/juguang/html-ppt-video-skill)**†<br><sub>juguang</sub> | 3 | HTML | MIT | Converts documents into HTML presentation videos with Chinese voiceover and subtitles. |
| **[AI PPT Skill](https://github.com/skychentian/ai-ppt-skill)**†<br><sub>skychentian</sub> | 3 | Both | Unspecified | Builds presentations end-to-end with 17 visual styles, outputting either HTML or an exported PPTX. |
| **[SVG to PPTX Skill](https://github.com/JamieJustTang/svg2pptx-skill)**†<br><sub>JamieJustTang</sub> | 3 | PPTX | NOASSERTION | Converts an AI-generated SVG into a fully editable native PowerPoint file, then optionally exports to PDF, Keynote, or Slides. |
| **[Doc to PPT Skill](https://github.com/reskfa/skill_doc2ppt)**†<br><sub>reskfa</sub> | 3 | Both | MIT | Converts Markdown or text documents into Claude-styled slides in HTML or PPTX format. |
| **[3D HTML Slide Skill](https://github.com/yoshifujidesign/3d-html-slide-skill)**† | 3 | HTML | MIT | Claude Code skill that generates a single-file HTML slide deck with Three.js wireframe backgrounds. |
| **[Image to Editable PPT Skill (zhoujie97)](https://github.com/zhoujie97/image-to-editable-ppt-skill)**†<br><sub>zhoujie97</sub> | 3 | PPTX | Unspecified | Rebuilds screenshots and infographics into editable PowerPoint shapes, text boxes and SVG icons. |
| **[TaoHtml](https://github.com/TaoGEO/TaoHtml)**†<br><sub>TaoGEO</sub> | 3 | HTML | MIT | Redesigns an existing Word, PDF or PPT into a 16:9 offline HTML deck with staged animation. |
| **[TikTok Slideshow Command Center](https://github.com/Meliwat/vyral-tiktok-slideshow-skill)**†<br><sub>Meliwat</sub> | 3 | Image | MIT | Plans TikTok photo carousels: content angle, slide design and posting cadence in one pass. |
| **[Ultimate PPT Master Skill](https://github.com/kdnsna/ultimate-ppt-master-skill)**†<br><sub>kdnsna</sub> | 2 | Both | MIT | Clarifies audience and style, then produces an editable PPTX or web deck from a one-line prompt. |
| **[PPTWork](https://github.com/JunfengRan/PPTWork)** | 2 | PPTX | MIT | Two Anthropic-style Skills that plan, author, and export PowerPoint decks from HTML. |
| **[Inspiration Deck Workshop](https://github.com/zjsthmjialin/inspiration-deck-workshop)**<br><sub>zjsthmjialin</sub> | 2 | Templates | MIT | 23 themes and 25 page layouts for animated static HTML decks, driven from a small CLI. |
| **[University PPT Skill](https://github.com/SiyuQiannn/university-ppt-skill)**<br><sub>SiyuQiannn</sub> | 1 | Templates | NOASSERTION | Editable university-branded PPTX built from school theme tokens and a reusable layout library. |
| **[Claude PPT Skills](https://github.com/sunxiaohui2025/claude-ppt-skills)**†<br><sub>sunxiaohui2025</sub> | 1 | HTML | Unspecified | Single-file HTML decks in six styles, with in-browser editing and a thumbnail overview grid. |
| **[Course HTML Slides Builder](https://github.com/HelenSong/course-html-slides-skill)**†<br><sub>HelenSong</sub> | 1 | HTML | MIT | Turns a course outline into multi-page HTML slides built for classroom projection. |
| **[Google Slides Deck Skill](https://github.com/eranw2000/google-slides-skill)**<br><sub>eranw2000</sub> | 1 | Framework | MIT | Rebuilds a Google Slides deck through the API, rendering each slide to PNG to check its work. |
| **[PPTX Deck Creation Kit](https://github.com/kimtth/agent-pptify-kit)**†<br><sub>kimtth</sub> | 1 | PPTX | MIT | Coordinate-explicit PPTX specs that stay native objects, shipped as a Copilot plugin. |
| **[PPT Deck Builder Skill](https://github.com/lk251066/ppt-deck-builder-skill)**†<br><sub>lk251066</sub> | 1 | Image | Unspecified | Renders each page as a finished image, repairs only the bad pages, then packs a PPTX. |
| **[Paper Deck Reveal](https://github.com/O0000-code/paper-deck-reveal)** | 0 | Framework | Apache-2.0 | Reveal.js skill that turns an academic paper into an offline deck with interactive demos. |
| **[GHB PPT Skill](https://github.com/NickyLam/GHB-PPT-Skill)**<br><sub>NickyLam</sub> | 0 | PPTX | MIT | Corporate-template PPTX where SVG becomes editable DrawingML, verified fully offline. |
| **[HTML Presentation Skill](https://github.com/defreitassl/html-presentation-skill)**†<br><sub>defreitassl</sub> | 0 | HTML | MIT | Turns documents, notes or briefs into a standalone HTML presentation, then validates it. |
| **[Slide Deck Skill](https://github.com/jayworker/slide-deck-skill)**<br><sub>jayworker</sub> | 0 | HTML | MIT | Single-file 16:9 HTML decks in a light dashboard style, one message per slide. |
| **[Marp Slides Studio](https://github.com/unsolublesugar/marp-slides-studio)**<br><sub>unsolublesugar</sub> | 0 | Templates | MIT | 50 Marp themes with a gallery, contrast checker and four agent skills for deck work. |

### Other curated lists

| Skill | ⭐ | Route | License | What it is |
|---|---:|---|---|---|
| **[awesome-html-slide-skills](https://github.com/ToseaAI/awesome-html-slide-skills)**†<br><sub>ToseaAI</sub> | 146 | List | Custom | Curated list of HTML slide skills and template libraries. A primary lead source for this registry. |
| **[Awesome-PPT-Design-Skills](https://github.com/software-ai-life/Awesome-PPT-Design-Skills)**†<br><sub>software-ai-life</sub> | 103 | List | Unspecified | Agent-agnostic PPT design skills for high-end editable presentation styles. |

<sub>`†` listed from the automated discovery sweep: the tagline and licence are read from the repository, but nobody has read its SKILL.md, so there is no install command or capability data for it yet. Rows without a dagger were researched by hand.<br>`*` monorepo star count — reflects the whole repo, not this one skill. `~` stale value, last refresh failed. `⚠️` copyleft license, check before commercial use.</sub>
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
| **Slidev** | ✅ | ✅ | · | ✅ | ✅ | ✅ | ✅ | ✅ | · | · |
| **Frontend Slides** | · | ✅ | · | · | · | ✅ | · | · | · | · |
| **Guizang PPT Skill** | — | · | · | · | ✅ | ✅ | · | · | — | · |
| **Baoyu Skills** | ✅ | ✅ | · | · | · | · | · | · | · | · |
| **Huashu Design** | ✅ | ✅ | · | · | · | ✅ | ✅ | · | · | · |
| **Quarkdown** | · | ✅ | · | · | ✅ | · | · | · | · | · |
| **Banana Slides** | ✅ | ✅ | · | · | · | · | · | · | · | n/a |
| **Visual Explainer** | · | · | · | · | ✅ | ✅ | · | · | · | ✅ |

<sub>✅ the docs claim it · — the docs say it does not · · the docs are silent, which is not the same as no · n/a the question does not apply to that route. Read from each project's own SKILL.md and README, never from running it; every ✅ carries the sentence it came from in [`data/capabilities.json`](data/capabilities.json).</sub>
<!-- END:CAPABILITIES -->

Read the middle column carefully: `·` means the docs never address it, which is not the
same as "no". Several of these projects do more than they write down. Where a capability
matters to you, the quote in [`data/capabilities.json`](data/capabilities.json) tells you
exactly which sentence to go and check.


---

## Motion: which ones animate, and how

The "Motion" column above only answers *whether* something animates. The question that
actually decides the choice is the next one: **what is moving, and what file do you hand
over at the end.** Because "a deck with some animation in it" means three mutually
incompatible things across these projects — and there is almost no converting between them.

Work out what you have to deliver first, then read down:

- **Someone must open it in PowerPoint and edit it** → the first group only, and it is short
- **A link or a single HTML file is fine** → the second group, where nearly everything is
- **A video file to post or send** → the third group

<!-- BEGIN:MOTION -->
#### Animation lives inside the .pptx

<sub>PowerPoint plays it with no browser involved, and the recipient can edit the timings. Also the hardest of the three to produce, which is why the list is this short.</sub>

| Skill | ⭐ | Route | Basis | What the motion actually is |
|---|---:|---|:-:|---|
| **[PPT Master](https://github.com/hugohe3/ppt-master)** | 53,817 | PPTX | ✅ | Entrance / emphasis / exit / motion-path animations and slide transitions written straight into the file by `pptx_animations.py`; speaker notes can also be rendered to narration audio. |
| **[Notrat PPT Studio](https://github.com/NestMold/notrat-ppt-studio-skill)** | 8 | Both | · | Claims animation across all three output modes — image, natively editable, and hybrid. |

#### Animation lives in the browser

<sub>Cheap, expressive, and gone the moment someone asks for the .pptx. This is where almost all the motion in this registry actually is.</sub>

| Skill | ⭐ | Route | Basis | What the motion actually is |
|---|---:|---|:-:|---|
| **[Slidev](https://github.com/slidevjs/slidev)** | 48,632 | Framework | ✅ | Click animations (step-by-step reveals), slide transitions and motion effects, all built into the framework. |
| **[Frontend Slides](https://github.com/zarazhangrui/frontend-slides)** | 29,166 | HTML | ✅ | "Animation-rich" zero-dependency single-file HTML; the motion ships with the 12 presets and 34 templates. |
| **[Guizang PPT Skill](https://github.com/op7418/guizang-ppt-skill)** | 26,155 | HTML | ✅ | Motion One entrance animations (bundled locally with a CDN fallback), plus WebGL motion that degrades to a static frame on low-power devices. |
| **[Visual Explainer](https://github.com/nicobailon/visual-explainer)** | 9,793 | HTML | ✅ | The restrained one: entrance and hover motion only where it clarifies hierarchy, `prefers-reduced-motion` respected, continuous glow / pulse / breathing banned outright. |
| **[HTML Anything](https://github.com/nexu-io/html-anything)** | 8,764 | Suite | ✅ | Staggered reveals specified to the millisecond: title at 0s, kicker at 200ms, a 1.2s stroke-dashoffset line draw from 400ms, then data labels every 100ms. |
| **[HTML PPT Studio](https://github.com/lewislulu/html-ppt-skill)** | 8,331 | HTML | ✅ | 47 animations — 27 CSS plus 20 canvas effects. The deepest motion library of any single skill here. |
| **[Dashi PPT Skill](https://github.com/chuspeeism/dashi-ppt-skill)** | 8,067 | Both | ✅ | Element entrances use each component's own built-in effect; the slide-transition style is switchable from the preview control panel. |
| **[Frontend Slides Editable](https://github.com/archlizheng/frontend-slides-editable)** | 497 | Both | ✅ | CSS-only by design — no React, no Motion library. Argues one well-orchestrated staggered load beats scattered micro-interactions. |
| **[Magic Slide](https://github.com/daniel-style/magic-slide)** | 171 | HTML | · | Magic Move-style transitions: a shared element glides from its position on one slide to the next instead of cutting. |
| **[Slide Deck Generator](https://github.com/code-on-sunday/slide-deck-generator)** | 145 | HTML | · | React + Vite + Framer Motion — the one that hands you a real animation library instead of hand-written CSS. |
| **[Visual Cognition Slides](https://github.com/edu-ai-builders/visual-cognition-slides)** | 83 | HTML | ✅ | An `ANIMATIONS.md` library of reusable code across 10 chapters, with motion justified by retention rather than looks. |
| **[HTML Slides](https://github.com/bluedusk/html-slides)** | 79 | HTML | ✅ | "Animation-rich" single-file HTML — same phrasing and lineage as frontend-slides. |
| **[KingDee PPT Skill](https://github.com/WayneZhon/KingDee-PPT-Skill)** | 56 | HTML | ✅ | Two tiers: Intersection Observer fades for the ordinary case, GSAP ScrollTrigger for Apple-style scroll narratives. |
| **[next-slide](https://github.com/codesstar/next-slide)** | 50 | HTML | ✅ | "Animation-rich" zero-dependency single file, bilingual out of the box. |
| **[Slide Creator](https://github.com/kaisersong/slide-creator)** | 49 | Both | ✅ | Animation is governed like colour and type — it must come from the chosen style file and nowhere else. |
| **[Slide Writer](https://github.com/FeeiCN/slide-writer)** | 41 | HTML | ✅ | Reveal animations are part of the design system: even a newly built component has to reuse the existing ones. |
| **[Slides AI Plugin](https://github.com/proyecto26/slides-ai-plugin)** | 38 | Both | · | One prompt out to either an animated HTML deck or an editable PowerPoint. |
| **[Skills Slides](https://github.com/nghiahsgs/skills-slides)** | 32 | HTML | ✅ | One `.html` with full animations, responsive sizing and keyboard navigation; 30+ effects feed the combinatorial style engine. |
| **[Interactive Slides](https://github.com/sylvial928/interactive-slides)** | 18 | HTML | · | Animated, interactive web decks with style presets and brand kits, plus one-click PowerPoint export. |
| **[AWS HTML Slides](https://github.com/lanceli93/aws-html-slides)** | 11 | HTML | · | Animation-rich HTML from scratch, or converted out of an existing .pptx. |
| **[Presentation Chef](https://github.com/sacredvoid/presentation-chef)** | 9 | HTML | · | Aims at Keynote-style "cinematic" animation inside one self-contained file. |
| **[Frontend Slides](https://github.com/dreamid27/frontend-slides)** | 4 | HTML | · | A frontend-slides derivative: animation-rich HTML with 88 layout presets and 34 templates. |
| **[CUHK Slides Template (HTML)](https://github.com/HarlandZZC/cuhk-slides-template-html)** | 4 | Templates | · | Animated stat counters and modal-backed feature grids, inside one hand-written template file. |
| **[3D HTML Slide Skill](https://github.com/yoshifujidesign/3d-html-slide-skill)** | 3 | HTML | · | Three.js wireframe backgrounds behind an otherwise single-file deck — the only 3D entry in the registry. |
| **[TaoHtml](https://github.com/TaoGEO/TaoHtml)** | 3 | HTML | · | Redesigns an existing Word / PDF / PPT into a 16:9 offline HTML deck with staged, build-up animation. |
| **[Inspiration Deck Workshop](https://github.com/zjsthmjialin/inspiration-deck-workshop)** | 2 | Templates | · | 23 themes and 25 layouts, all rendered as "animated static HTML" from a small CLI. |

#### The output is a video file

<sub>Not a deck you present but a file you send — MP4 / GIF, sometimes with voiceover. Different job, filed here because it is what people mean about half the time they ask for animation.</sub>

| Skill | ⭐ | Route | Basis | What the motion actually is |
|---|---:|---|:-:|---|
| **[Huashu Design](https://github.com/alchaincyf/huashu-design)** | 24,084 | Both | ✅ | The closest thing here to a real motion engine: a Stage + Sprite time-slice model behind `useTime` / `useSprite` / `interpolate` / `Easing`, exporting MP4 / GIF, 60fps interpolation and a scored soundtrack in one command. |
| **[NanoBanana PPT Skills](https://github.com/op7418/NanoBanana-PPT-Skills)** | 3,245 | Image | · | Generates slide images and video with transitions and interactive playback — an image pipeline, not a code one. |
| **[Presentation Skills](https://github.com/Sven-LI-sankyuu/presentation-skills)** | 171 | Both | · | A Codex CLI pack whose second half is an end-to-end web-demo video synthesis workflow. |
| **[Servasyy Skills](https://github.com/huangserva/servasyy_skills)** | 164 | Suite | · | A general AI suite bundling a video-generation skill alongside the deck one — that video is not slide motion. |
| **[NanoBanana PPT Skills](https://github.com/girish6055/NanoBanana-PPT-Skills)** | 14 | PPTX | · | A NanoBanana fork claiming smart transitions and interactive playback. |
| **[NanoBanana PPT Skills](https://github.com/xj-bear/NanoBanana-PPT-Skills)** | 13 | PPTX | · | A NanoBanana fork that adds Veo video content. |
| **[Web PPT](https://github.com/includewudi/web-ppt)** | 4 | HTML | · | Zero-dependency HTML that also records itself to video. |
| **[HTML PPT Video Skill](https://github.com/juguang/html-ppt-video-skill)** | 3 | HTML | · | Documents to an HTML presentation video with Chinese voiceover and subtitles. |

<sub>✅ the claim is backed by a quote from the project's own docs, recorded in [`data/capabilities.json`](data/capabilities.json) · · the claim is the project's own one-line description, which nobody has verified against its SKILL.md.<br>**The other 191 skills say nothing about motion anywhere this registry has read.** That is an absence of evidence, not evidence of absence — several of them almost certainly animate and simply never wrote it down.</sub>
<!-- END:MOTION -->

The one-line reading of this table: **motion is cheap in the browser and expensive in a
.pptx.** If your deliverable has to be a PowerPoint file the client can edit, the field
collapses from twenty-odd options to two — and that collapse tells you more about your
plan than any single row here.


---

## What they look like

The two tables above say what each project *is* and what it *claims*. Neither answers
the question you actually walked in with, which is whether you like what comes out. So
here are two pictures per project, published by the project itself.

**Two per skill, shown full size.** Two is enough for the decision this page serves,
which is which projects to keep — not which slide of one. They are content slides
rather than title slides, and two different styles where the project has them. Full
size rather than a contact sheet, because a slide shrunk to a thumbnail tells you the
palette and nothing else — not the type, not the hierarchy, not the whitespace, which
are the things you are choosing between. For every sample and style id of one project,
run `python scripts/pick.py styles <skill-id>`.

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
| `clone` | Clones into `~/.claude/skills/`, where Claude Code looks for personal skills. Restart the session and it is available. | 30 |
| `plugin` | Two commands typed **inside Claude Code**, not in a terminal. Adds the marketplace, then installs from it. | 3 |
| `skills-cli` | Agent-agnostic installer. Works outside Claude Code too. | 3 |
| `python` | Needs Python on your machine. Clone it, install the dependencies, then point your agent at the cloned directory. | 2 |
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
> not invoked a single one of these skills**, so each project's own SKILL.md is the authority on its trigger
> phrases and arguments. Step 4's description of previews was read out of
> frontend-slides' SKILL.md and holds for that skill only.

<!-- BEGIN:GALLERY -->
**Jump to:** [PPT Master](#gallery-ppt-master) · [Frontend Slides](#gallery-frontend-slides) · [Guizang PPT Skill](#gallery-guizang-ppt-skill) · [Huashu Design](#gallery-huashu-design) · [HTML PPT Studio](#gallery-html-ppt-skill) · [open-slide](#gallery-open-slide) · [Beautiful HTML Templates](#gallery-beautiful-html-templates) · [Codex Slides](#gallery-codex-slides) · [PPT Agent Workflow San](#gallery-ppt-agent-workflow-san) · [Frontend Slides Editable](#gallery-frontend-slides-editable) · [Mck PPT Design System](#gallery-mck-ppt-design-skill) · [PPT SVG Generator](#gallery-ppt-svg-generator) · [PPT Agent Skill](#gallery-ppt-agent-skill) · [HTML Slides](#gallery-html-slides-bluedusk) · [KingDee PPT Skill](#gallery-kingdee-ppt-skill) · [next-slide](#gallery-next-slide) · [Slide Creator](#gallery-slide-creator) · [Slide Writer](#gallery-slide-writer) · [PowerPoint Fancy Design](#gallery-powerpoint-fancy-design) · [Skills Slides](#gallery-skills-slides) · [PPTX from Layouts](#gallery-pptx-from-layouts) · [Excalidraw Slides Generator](#gallery-excalidraw-slides-skills) · [Econ Slides Skill](#gallery-econ-slides-skill) · [OpenCode PPT Studio](#gallery-oc-sdk-ppt) · [KR Brand Decks](#gallery-kr-brand-decks) · [CUHK Slides Template (HTML)](#gallery-cuhk-slides-template-html) · [3D HTML Slide Skill](#gallery-3d-html-slide-skill) · [Image to Editable PPT Skill (zhoujie97)](#gallery-image-to-editable-ppt-skill-zhoujie97) · [TaoHtml](#gallery-taohtml) · [TikTok Slideshow Command Center](#gallery-vyral-tiktok-slideshow-skill) · [PPTWork](#gallery-pptwork) · [Inspiration Deck Workshop](#gallery-inspiration-deck-workshop) · [University PPT Skill](#gallery-university-ppt-skill) · [Claude PPT Skills](#gallery-claude-ppt-skills) · [Course HTML Slides Builder](#gallery-course-html-slides-skill) · [Google Slides Deck Skill](#gallery-google-slides-skill) · [PPTX Deck Creation Kit](#gallery-agent-pptify-kit) · [PPT Deck Builder Skill](#gallery-ppt-deck-builder-skill) · [Paper Deck Reveal](#gallery-paper-deck-reveal) · [GHB PPT Skill](#gallery-ghb-ppt-skill) · [HTML Presentation Skill](#gallery-html-presentation-skill) · [Slide Deck Skill](#gallery-slide-deck-skill) · [Marp Slides Studio](#gallery-marp-slides-studio)

<a id="gallery-ppt-master"></a>

#### [PPT Master](https://github.com/hugohe3/ppt-master) · 53,817 ⭐ · PPTX

<sub>Documents or topics into genuinely native, editable PowerPoint decks.</sub>

<sub>2 of 46 images in [`hugohe3/ppt-master`](https://github.com/hugohe3/ppt-master) · both are the project's own README picks</sub>

```bash
git clone https://github.com/hugohe3/ppt-master && pip install -r requirements.txt
```

<sub><b>Style ids</b> `global-ai-capital` · `swiss-grid` · `glassmorphism-demo` · `sugar-rush-memphis` · `indie-bookstore-zine` · `pritzker-2026` · `academic-medical` · `dark-art-mv` · `launch-xiaomi` · `magazine-garden` · `nature-wildlife` · `tech-claude-plans` · 12 more via `python scripts/pick.py styles ppt-master` — name one when you ask for a deck. These are the project's own strings, read from its filenames and captions, not names this registry made up; each id's own sample image is listed by that command.</sub>

<img src="https://raw.githubusercontent.com/hugohe3/ppt-master/7ae3721c856fedb921d6acec52c7de69181f5194/docs/assets/screenshots/preview_global_ai_capital.png" width="100%" alt="Data journalism — Global AI Capital 2026">

<sub><b>Data journalism — Global AI Capital 2026</b> · <a href="https://github.com/hugohe3/ppt-master/blob/7ae3721c856fedb921d6acec52c7de69181f5194/docs/assets/screenshots/preview_global_ai_capital.png"><code>docs/assets/screenshots/preview_global_ai_capital.png</code></a></sub>

<img src="https://raw.githubusercontent.com/hugohe3/ppt-master/7ae3721c856fedb921d6acec52c7de69181f5194/docs/assets/screenshots/preview_swiss_grid.png" width="100%" alt="Swiss typographic grid — Grid Systems primer">

<sub><b>Swiss typographic grid — Grid Systems primer</b> · <code>swiss-grid</code> · <a href="https://github.com/hugohe3/ppt-master/blob/7ae3721c856fedb921d6acec52c7de69181f5194/docs/assets/screenshots/preview_swiss_grid.png"><code>docs/assets/screenshots/preview_swiss_grid.png</code></a></sub>

<a id="gallery-frontend-slides"></a>

#### [Frontend Slides](https://github.com/zarazhangrui/frontend-slides) · 29,166 ⭐ · HTML

<sub>Beautiful slides on the web using a coding agent's frontend skills.</sub>

<sub>2 of 102 images in [`zarazhangrui/frontend-slides`](https://github.com/zarazhangrui/frontend-slides) · both are the project's own README picks</sub>

```bash
/plugin marketplace add https://github.com/zarazhangrui/frontend-slides
/plugin install frontend-slides@frontend-slides
```

<sub><b>Style ids</b> `soft-editorial` · `editorial-forest` · `pin-and-paper` · `sakura-chroma` · `stencil-tablet` · `cobalt-grid` · `vellum` · `emerald-editorial` — name one when you ask for a deck. These are the project's own strings, read from its filenames and captions, not names this registry made up; each id's own sample image is listed by that command.</sub>

<img src="https://raw.githubusercontent.com/zarazhangrui/beautiful-html-templates/e5e204fb1f3b06290846e7dcd7aceddabeceec8c/screenshots/soft-editorial-4.png" width="100%" alt="Soft Editorial — slide 4">

<sub><b>Soft Editorial — slide 4</b> · <a href="https://github.com/zarazhangrui/beautiful-html-templates/blob/e5e204fb1f3b06290846e7dcd7aceddabeceec8c/screenshots/soft-editorial-4.png"><code>screenshots/soft-editorial-4.png</code></a></sub>

<img src="https://raw.githubusercontent.com/zarazhangrui/beautiful-html-templates/e5e204fb1f3b06290846e7dcd7aceddabeceec8c/screenshots/editorial-forest-2.png" width="100%" alt="Editorial Forest — slide 2">

<sub><b>Editorial Forest — slide 2</b> · <a href="https://github.com/zarazhangrui/beautiful-html-templates/blob/e5e204fb1f3b06290846e7dcd7aceddabeceec8c/screenshots/editorial-forest-2.png"><code>screenshots/editorial-forest-2.png</code></a></sub>

<a id="gallery-guizang-ppt-skill"></a>

#### [Guizang PPT Skill](https://github.com/op7418/guizang-ppt-skill) · 26,155 ⭐ · HTML

<sub>Editorial-magazine and Swiss-International HTML decks, with design locked down by constraint.</sub>

<sub>2 of 13 images in [`op7418/guizang-ppt-skill`](https://github.com/op7418/guizang-ppt-skill) · both are the project's own README picks</sub>

```bash
npx skills add https://github.com/op7418/guizang-ppt-skill --skill guizang-ppt-skill
```

<sub><b>Style ids</b> `ppt-skill-showcase` — name one when you ask for a deck. These are the project's own strings, read from its filenames and captions, not names this registry made up; each id's own sample image is listed by that command.</sub>

<img src="https://github.com/user-attachments/assets/5dc316a2-401c-4e37-9123-ea081b6ae470" width="100%" alt="Style A 电子杂志风效果展示">

<sub><b>Style A 电子杂志风效果展示</b> · GitHub attachment</sub>

<img src="https://github.com/user-attachments/assets/8960e78c-69bb-4b7e-aa95-6fad64b70314" width="100%" alt="Style B 瑞士国际主义效果展示">

<sub><b>Style B 瑞士国际主义效果展示</b> · GitHub attachment</sub>

<a id="gallery-huashu-design"></a>

#### [Huashu Design](https://github.com/alchaincyf/huashu-design) · 24,084 ⭐ · Both

<sub>HTML-native design skill — prototypes, decks, motion and design critique, not just slides.</sub>

<sub>2 of 24 images in [`alchaincyf/huashu-design`](https://github.com/alchaincyf/huashu-design)</sub>

```bash
npx skills add alchaincyf/huashu-design
```

<sub><b>Style ids</b> `ppt-build` · `ppt-pentagram` · `ppt-takram` · `ainav-build` · `ainav-pentagram` · `ainav-takram` · `aiwriting-build` · `aiwriting-pentagram` · `aiwriting-takram` · `devdocs-build` · `devdocs-pentagram` · `devdocs-takram` · 12 more via `python scripts/pick.py styles huashu-design` — name one when you ask for a deck. These are the project's own strings, read from its filenames and captions, not names this registry made up; each id's own sample image is listed by that command.</sub>

<img src="https://raw.githubusercontent.com/alchaincyf/huashu-design/1572d431f1411c82ec0baea94dea6a45f6063b26/assets/showcases/ppt/ppt-build.png" width="100%" alt="Huashu Design sample">

<sub><b>Ppt Build</b> · <a href="https://github.com/alchaincyf/huashu-design/blob/1572d431f1411c82ec0baea94dea6a45f6063b26/assets/showcases/ppt/ppt-build.png"><code>assets/showcases/ppt/ppt-build.png</code></a></sub>

<img src="https://raw.githubusercontent.com/alchaincyf/huashu-design/1572d431f1411c82ec0baea94dea6a45f6063b26/assets/showcases/ppt/ppt-pentagram.png" width="100%" alt="Huashu Design sample">

<sub><b>Ppt Pentagram</b> · <a href="https://github.com/alchaincyf/huashu-design/blob/1572d431f1411c82ec0baea94dea6a45f6063b26/assets/showcases/ppt/ppt-pentagram.png"><code>assets/showcases/ppt/ppt-pentagram.png</code></a></sub>

<a id="gallery-html-ppt-skill"></a>

#### [HTML PPT Studio](https://github.com/lewislulu/html-ppt-skill) · 8,331 ⭐ · HTML

<sub>24 themes, 31 layouts and 20+ animations for professional HTML presentations.</sub>

<sub>2 of 63 images in [`lewislulu/html-ppt-skill`](https://github.com/lewislulu/html-ppt-skill) · both are the project's own README picks</sub>

```bash
git clone https://github.com/lewislulu/html-ppt-skill ~/.claude/skills/html-ppt-skill
```

<sub><b>Style ids</b> `themes` · `templates` · `layouts` · `layouts-live` · `hero` · `presenter-mode` · `animations` · `animation-showcase` — name one when you ask for a deck. These are the project's own strings, read from its filenames and captions, not names this registry made up; each id's own sample image is listed by that command.</sub>

<img src="https://raw.githubusercontent.com/lewislulu/html-ppt-skill/f3a8435d3901697d5ac5e64d356c933637e43107/docs/readme/presenter-mode.png" width="100%" alt="Presenter mode with 4 magnetic cards">

<sub><b>Presenter mode with 4 magnetic cards</b> · <a href="https://github.com/lewislulu/html-ppt-skill/blob/f3a8435d3901697d5ac5e64d356c933637e43107/docs/readme/presenter-mode.png"><code>docs/readme/presenter-mode.png</code></a></sub>

<img src="https://raw.githubusercontent.com/lewislulu/html-ppt-skill/f3a8435d3901697d5ac5e64d356c933637e43107/docs/readme/themes.png" width="100%" alt="36 themes · 8 of them">

<sub><b>36 themes · 8 of them</b> · <a href="https://github.com/lewislulu/html-ppt-skill/blob/f3a8435d3901697d5ac5e64d356c933637e43107/docs/readme/themes.png"><code>docs/readme/themes.png</code></a></sub>

<a id="gallery-open-slide"></a>

#### [open-slide](https://github.com/1weiho/open-slide) · 7,561 ⭐ · Framework

<sub>A slide framework built for agents — React components on a fixed 1920x1080 canvas.</sub>

<sub>2 of 16 images in [`1weiho/open-slide`](https://github.com/1weiho/open-slide) · one of them is the project's own README pick</sub>

```bash
npx @open-slide/cli init my-slide
```

<sub><b>Style ids</b> `replit-features-result` · `create-slide-skill` · `openslide-home` · `replit-agent-home` · `assets-manager` · `inspector` · `presenter` · `theme` · `svgl` · `open-slide` · `replit-deploy` · `init-command` · 1 more via `python scripts/pick.py styles open-slide` — name one when you ask for a deck. These are the project's own strings, read from its filenames and captions, not names this registry made up; each id's own sample image is listed by that command.</sub>

<img src="https://github.com/user-attachments/assets/02f5e6d7-12a7-4a8e-88e7-ae8770a96584" width="100%" alt="open-slide github cover">

<sub><b>open-slide github cover</b> · GitHub attachment</sub>

<img src="https://raw.githubusercontent.com/1weiho/open-slide/35dc46ca27716ea86f8a76710bbd3640e9590628/apps/demo/slides/open-slide-on-replit/assets/replit-features-result.webp" width="100%" alt="open-slide sample">

<sub><b>Replit Features Result</b> · <a href="https://github.com/1weiho/open-slide/blob/35dc46ca27716ea86f8a76710bbd3640e9590628/apps/demo/slides/open-slide-on-replit/assets/replit-features-result.webp"><code>apps/demo/slides/open-slide-on-replit/assets/replit-features-result.webp</code></a></sub>

<a id="gallery-beautiful-html-templates"></a>

#### [Beautiful HTML Templates](https://github.com/zarazhangrui/beautiful-html-templates) · 4,545 ⭐ · Templates

<sub>34 HTML slide templates with index.json metadata so any agent can pick the right one.</sub>

<sub>2 of 102 images in [`zarazhangrui/beautiful-html-templates`](https://github.com/zarazhangrui/beautiful-html-templates) · both are the project's own README picks</sub>

```bash
git clone https://github.com/zarazhangrui/beautiful-html-templates
```

<sub><b>Style ids</b> `soft-editorial` · `editorial-forest` · `pin-and-paper` · `sakura-chroma` · `stencil-tablet` · `cobalt-grid` · `vellum` · `emerald-editorial` — name one when you ask for a deck. These are the project's own strings, read from its filenames and captions, not names this registry made up; each id's own sample image is listed by that command.</sub>

<img src="https://raw.githubusercontent.com/zarazhangrui/beautiful-html-templates/e5e204fb1f3b06290846e7dcd7aceddabeceec8c/screenshots/soft-editorial-4.png" width="100%" alt="Soft Editorial — slide 4">

<sub><b>Soft Editorial — slide 4</b> · <a href="https://github.com/zarazhangrui/beautiful-html-templates/blob/e5e204fb1f3b06290846e7dcd7aceddabeceec8c/screenshots/soft-editorial-4.png"><code>screenshots/soft-editorial-4.png</code></a></sub>

<img src="https://raw.githubusercontent.com/zarazhangrui/beautiful-html-templates/e5e204fb1f3b06290846e7dcd7aceddabeceec8c/screenshots/editorial-forest-2.png" width="100%" alt="Editorial Forest — slide 2">

<sub><b>Editorial Forest — slide 2</b> · <a href="https://github.com/zarazhangrui/beautiful-html-templates/blob/e5e204fb1f3b06290846e7dcd7aceddabeceec8c/screenshots/editorial-forest-2.png"><code>screenshots/editorial-forest-2.png</code></a></sub>

<a id="gallery-codex-slides"></a>

#### [Codex Slides](https://github.com/nexu-io/codex-slides) · 890 ⭐ · Framework

<sub>AI slide studio for Codex: image-native decks, parallel render, and PDF/PPTX export.</sub>

<sub>2 of 48 images in [`nexu-io/codex-slides`](https://github.com/nexu-io/codex-slides) · both are the project's own README picks</sub>

```bash
git clone https://github.com/nexu-io/codex-slides && cd codex-slides
```

<sub><b>Style ids</b> `hero` · `01-home-community` · `02-community-styles` · `04-project-questions` · `06-visual-style` · `07-parallel-generation` · `08-editor` · `09-presenter-mode` · `10-export` · `nb-vintage-patent` · `nb-visual-info-guide` · `market-report` · 12 more via `python scripts/pick.py styles codex-slides` — name one when you ask for a deck. These are the project's own strings, read from its filenames and captions, not names this registry made up; each id's own sample image is listed by that command.</sub>

<img src="https://raw.githubusercontent.com/nexu-io/codex-slides/dbc2a5992e937760e9ce8e587e11729f970881cb/docs/assets/readme/hero.png" width="100%" alt="Codex Slides — the open-source AI slide studio inside your coding agent, operated in the Codex in-app Browser">

<sub><b>Codex Slides — the open-source AI slide studio inside your coding agent, operated in the Codex in-app Browser</b> · <code>hero</code> · <a href="https://github.com/nexu-io/codex-slides/blob/dbc2a5992e937760e9ce8e587e11729f970881cb/docs/assets/readme/hero.png"><code>docs/assets/readme/hero.png</code></a></sub>

<img src="https://raw.githubusercontent.com/nexu-io/codex-slides/dbc2a5992e937760e9ce8e587e11729f970881cb/docs/assets/readme/01-home-community.png" width="100%" alt="Codex Slides home with the prompt composer, scenario shortcuts, and Community Styles">

<sub><b>Codex Slides home with the prompt composer, scenario shortcuts, and Community Styles</b> · <code>01-home-community</code> · <a href="https://github.com/nexu-io/codex-slides/blob/dbc2a5992e937760e9ce8e587e11729f970881cb/docs/assets/readme/01-home-community.png"><code>docs/assets/readme/01-home-community.png</code></a></sub>

<a id="gallery-ppt-agent-workflow-san"></a>

#### [PPT Agent Workflow San](https://github.com/mucsbr/ppt-agent-workflow-san) · 638 ⭐ · HTML

<sub>Progressive, interactive deck generation.</sub>

<sub>2 of 10 images in [`mucsbr/ppt-agent-workflow-san`](https://github.com/mucsbr/ppt-agent-workflow-san) · both are the project's own README picks</sub>

```bash
git clone https://github.com/mucsbr/ppt-agent-workflow-san
```

<sub><b>Style ids</b> `html-slide-to-pptx-preview` · `ppt-workflow-preview` · `ppt-workflow` · `02-core-conclusion` · `03-positioning` · `04-users-scenarios` · `05-growth-flywheel` · `06-competition` · `07-risks` · `08-conclusion` — name one when you ask for a deck. These are the project's own strings, read from its filenames and captions, not names this registry made up; each id's own sample image is listed by that command.</sub>

<img src="https://raw.githubusercontent.com/mucsbr/ppt-agent-workflow-san/801cd2bd46c3cc4ca2c846ff28da2d9284816cd9/2.png" width="100%" alt="html-slide-to-pptx-preview">

<sub><b>html-slide-to-pptx-preview</b> · <a href="https://github.com/mucsbr/ppt-agent-workflow-san/blob/801cd2bd46c3cc4ca2c846ff28da2d9284816cd9/2.png"><code>2.png</code></a></sub>

<img src="https://raw.githubusercontent.com/mucsbr/ppt-agent-workflow-san/801cd2bd46c3cc4ca2c846ff28da2d9284816cd9/1.png" width="100%" alt="ppt-workflow-preview">

<sub><b>ppt-workflow-preview</b> · <a href="https://github.com/mucsbr/ppt-agent-workflow-san/blob/801cd2bd46c3cc4ca2c846ff28da2d9284816cd9/1.png"><code>1.png</code></a></sub>

<a id="gallery-frontend-slides-editable"></a>

#### [Frontend Slides Editable](https://github.com/archlizheng/frontend-slides-editable) · 497 ⭐ · Both

<sub>Editable HTML decks with drag-resize, reordering, local save and PPTX conversion.</sub>

<sub>2 of 114 images in [`archlizheng/frontend-slides-editable`](https://github.com/archlizheng/frontend-slides-editable) · both are the project's own README picks</sub>

```bash
git clone https://github.com/archlizheng/frontend-slides-editable
```

<sub><b>Style ids</b> `cobalt-grid` · `studio-volt` · `soft-editorial` · `bold-signal` · `electric-studio` · `creative-voltage` · `dark-botanical` · `notebook-tabs` · `pastel-geometry` · `split-pastel` · `vintage-editorial` · `neon-cyber` · 12 more via `python scripts/pick.py styles frontend-slides-editable` — name one when you ask for a deck. These are the project's own strings, read from its filenames and captions, not names this registry made up; each id's own sample image is listed by that command.</sub>

<img src="https://raw.githubusercontent.com/archlizheng/frontend-slides-editable/e5663e6a0bdc2c2a673198bab3fb61036a7f20ee/docs/preset-previews/8-bit-orbit-mid.png" width="100%" alt="8-Bit Orbit — mid slide">

<sub><b>8-Bit Orbit — mid slide</b> · <code>8-bit-orbit-mid</code> · <a href="https://github.com/archlizheng/frontend-slides-editable/blob/e5663e6a0bdc2c2a673198bab3fb61036a7f20ee/docs/preset-previews/8-bit-orbit-mid.png"><code>docs/preset-previews/8-bit-orbit-mid.png</code></a></sub>

<img src="https://raw.githubusercontent.com/archlizheng/frontend-slides-editable/e5663e6a0bdc2c2a673198bab3fb61036a7f20ee/docs/preset-previews/8-bit-orbit-later.png" width="100%" alt="8-Bit Orbit — later slide">

<sub><b>8-Bit Orbit — later slide</b> · <code>8-bit-orbit-later</code> · <a href="https://github.com/archlizheng/frontend-slides-editable/blob/e5663e6a0bdc2c2a673198bab3fb61036a7f20ee/docs/preset-previews/8-bit-orbit-later.png"><code>docs/preset-previews/8-bit-orbit-later.png</code></a></sub>

<a id="gallery-mck-ppt-design-skill"></a>

#### [Mck PPT Design System](https://github.com/likaku/Mck-ppt-design-skill) · 274 ⭐ · PPTX

<sub>Consulting-firm-style design system: 70 layout patterns, flat design, python-pptx.</sub>

<sub>2 of 6 images in [`likaku/Mck-ppt-design-skill`](https://github.com/likaku/Mck-ppt-design-skill) · both are the project's own README picks</sub>

```bash
git clone https://github.com/likaku/Mck-ppt-design-skill
```

<img src="https://github.com/user-attachments/assets/075ec46d-dd73-4454-92d0-84184b78d276" width="100%" alt="Cover">

<sub><b>Cover</b> · GitHub attachment</sub>

<img src="https://github.com/user-attachments/assets/3b25f071-8a81-48e3-a62b-9d9be9026f2e" width="100%" alt="Content">

<sub><b>Content</b> · GitHub attachment</sub>

<a id="gallery-ppt-svg-generator"></a>

#### [PPT SVG Generator](https://github.com/vigorX777/ppt-svg-generator) · 258 ⭐ · PPTX

<sub>Markdown to PPT or PDF via SVG, with preset styles.</sub>

<sub>2 of 2 images in [`vigorX777/ppt-svg-generator`](https://github.com/vigorX777/ppt-svg-generator) · both are the project's own README picks</sub>

```bash
git clone https://github.com/vigorX777/ppt-svg-generator
```

<img src="https://github.com/user-attachments/assets/2454e688-d3b8-40a2-a3f8-893bbe5060ee" width="100%" alt="image">

<sub><b>image</b> · GitHub attachment</sub>

<img src="https://github.com/user-attachments/assets/97847c7f-5dc3-4a39-b4d8-ee3dc7d0396b" width="100%" alt="PixPin_2026-01-25_15-58-40">

<sub><b>PixPin_2026-01-25_15-58-40</b> · GitHub attachment</sub>

<a id="gallery-ppt-agent-skill"></a>

#### [PPT Agent Skill](https://github.com/Akxan/ppt-agent-skill) · 147 ⭐ · HTML

<sub>26 styles and 18 chart types benchmarked against Linear, Anthropic, Stripe, Apple and NYT.</sub>

<sub>2 of 32 images in [`Akxan/ppt-agent-skill`](https://github.com/Akxan/ppt-agent-skill) · both are the project's own README picks</sub>

```bash
git clone https://github.com/Akxan/ppt-agent-skill
```

<sub><b>Style ids</b> `all` · `vibrant` · `natural-retro` · `dark-professional` · `light-premium` · `cultural-oriental` · `bauhaus-block` · `blue-white` · `botanic-forest` · `candy-pastel` · `champagne-gold` · `chrome-y2k` · 12 more via `python scripts/pick.py styles ppt-agent-skill` — name one when you ask for a deck. These are the project's own strings, read from its filenames and captions, not names this registry made up; each id's own sample image is listed by that command.</sub>

<img src="https://raw.githubusercontent.com/Akxan/ppt-agent-skill/01825dee2ad40a8c719824252605396b9a570d57/assets/hero-all.png" width="100%" alt="26 风格预览">

<sub><b>26 风格预览</b> · <code>all</code> · <a href="https://github.com/Akxan/ppt-agent-skill/blob/01825dee2ad40a8c719824252605396b9a570d57/assets/hero-all.png"><code>assets/hero-all.png</code></a></sub>

<img src="https://raw.githubusercontent.com/Akxan/ppt-agent-skill/01825dee2ad40a8c719824252605396b9a570d57/assets/hero-vibrant.png" width="100%" alt="活力鲜明 4 风格">

<sub><b>活力鲜明 4 风格</b> · <code>vibrant</code> · <a href="https://github.com/Akxan/ppt-agent-skill/blob/01825dee2ad40a8c719824252605396b9a570d57/assets/hero-vibrant.png"><code>assets/hero-vibrant.png</code></a></sub>

<a id="gallery-html-slides-bluedusk"></a>

#### [HTML Slides](https://github.com/bluedusk/html-slides) · 79 ⭐ · HTML

<sub>HTML slides with speaker notes, plus a companion presentation app.</sub>

<sub>2 of 4 images in [`bluedusk/html-slides`](https://github.com/bluedusk/html-slides)</sub>

```bash
git clone https://github.com/bluedusk/html-slides
```

<sub><b>Style ids</b> `hero` — name one when you ask for a deck. These are the project's own strings, read from its filenames and captions, not names this registry made up; each id's own sample image is listed by that command.</sub>

<img src="https://raw.githubusercontent.com/bluedusk/html-slides/d8289f4c317905cc5d0ca265d32b791e6cb387b7/eval/content/assets/hero.jpg" width="100%" alt="HTML Slides sample">

<sub><b>Hero</b> · <a href="https://github.com/bluedusk/html-slides/blob/d8289f4c317905cc5d0ca265d32b791e6cb387b7/eval/content/assets/hero.jpg"><code>eval/content/assets/hero.jpg</code></a></sub>

<img src="https://raw.githubusercontent.com/bluedusk/html-slides/d8289f4c317905cc5d0ca265d32b791e6cb387b7/eval/content/assets/screenshot.jpg" width="100%" alt="HTML Slides sample">

<sub><b>Screenshot</b> · <a href="https://github.com/bluedusk/html-slides/blob/d8289f4c317905cc5d0ca265d32b791e6cb387b7/eval/content/assets/screenshot.jpg"><code>eval/content/assets/screenshot.jpg</code></a></sub>

<a id="gallery-kingdee-ppt-skill"></a>

#### [KingDee PPT Skill](https://github.com/WayneZhon/KingDee-PPT-Skill) · 56 ⭐ · HTML

<sub>KingDee corporate style decks.</sub>

<sub>1 of 1 images in [`WayneZhon/KingDee-PPT-Skill`](https://github.com/WayneZhon/KingDee-PPT-Skill)</sub>

```bash
git clone https://github.com/WayneZhon/KingDee-PPT-Skill
```

<sub><b>Style ids</b> `closing` — name one when you ask for a deck. These are the project's own strings, read from its filenames and captions, not names this registry made up; each id's own sample image is listed by that command.</sub>

<img src="https://raw.githubusercontent.com/WayneZhon/KingDee-PPT-Skill/28ca93aadeefc91fcc64152714ddeece15f13e1d/assets/closing_thanks.png" width="100%" alt="KingDee PPT Skill sample">

<sub><b>Closing</b> · closing · <a href="https://github.com/WayneZhon/KingDee-PPT-Skill/blob/28ca93aadeefc91fcc64152714ddeece15f13e1d/assets/closing_thanks.png"><code>assets/closing_thanks.png</code></a></sub>

<a id="gallery-next-slide"></a>

#### [next-slide](https://github.com/codesstar/next-slide) · 50 ⭐ · HTML

<sub>26+ styles, zero dependencies, bilingual.</sub>

<sub>1 of 1 images in [`codesstar/next-slide`](https://github.com/codesstar/next-slide)</sub>

```bash
git clone https://github.com/codesstar/next-slide
```

<sub><b>Style ids</b> `motion-brand-showcase` — name one when you ask for a deck. These are the project's own strings, read from its filenames and captions, not names this registry made up; each id's own sample image is listed by that command.</sub>

<img src="https://raw.githubusercontent.com/codesstar/next-slide/e92c1b2506e6cf5acff7d2b92339ba0c0ce2af22/scenarios/images/motion-brand-showcase.webp" width="100%" alt="next-slide sample">

<sub><b>Motion Brand Showcase</b> · <a href="https://github.com/codesstar/next-slide/blob/e92c1b2506e6cf5acff7d2b92339ba0c0ce2af22/scenarios/images/motion-brand-showcase.webp"><code>scenarios/images/motion-brand-showcase.webp</code></a></sub>

<a id="gallery-slide-creator"></a>

#### [Slide Creator](https://github.com/kaisersong/slide-creator) · 49 ⭐ · Both

<sub>AI planning, style discovery and PPTX export.</sub>

<sub>2 of 23 images in [`kaisersong/slide-creator`](https://github.com/kaisersong/slide-creator) · both are the project's own README picks</sub>

```bash
git clone https://github.com/kaisersong/slide-creator
```

<sub><b>Style ids</b> `strategy-consulting` · `blue-sky` · `bold-signal` · `electric-studio` · `creative-voltage` · `dark-botanical` · `notebook-tabs` · `pastel-geometry` · `split-pastel` · `vintage-editorial` · `neon-cyber` · `terminal-green` · 11 more via `python scripts/pick.py styles slide-creator` — name one when you ask for a deck. These are the project's own strings, read from its filenames and captions, not names this registry made up; each id's own sample image is listed by that command.</sub>

<img src="https://raw.githubusercontent.com/kaisersong/slide-creator/d0cf041e3a87db2ac75f8f583fc91a600e369e70/demos/screenshots/strategy-consulting.png" width="100%" alt="Strategy Consulting">

<sub><b>Strategy Consulting</b> · <a href="https://github.com/kaisersong/slide-creator/blob/d0cf041e3a87db2ac75f8f583fc91a600e369e70/demos/screenshots/strategy-consulting.png"><code>demos/screenshots/strategy-consulting.png</code></a></sub>

<img src="https://raw.githubusercontent.com/kaisersong/slide-creator/d0cf041e3a87db2ac75f8f583fc91a600e369e70/demos/screenshots/blue-sky.png" width="100%" alt="Blue Sky">

<sub><b>Blue Sky</b> · <a href="https://github.com/kaisersong/slide-creator/blob/d0cf041e3a87db2ac75f8f583fc91a600e369e70/demos/screenshots/blue-sky.png"><code>demos/screenshots/blue-sky.png</code></a></sub>

<a id="gallery-slide-writer"></a>

#### [Slide Writer](https://github.com/FeeiCN/slide-writer) · 41 ⭐ · HTML

<sub>Enterprise HTML decks from ideas, outlines, documents or speech drafts.</sub>

<sub>2 of 5 images in [`FeeiCN/slide-writer`](https://github.com/FeeiCN/slide-writer) · both are the project's own README picks</sub>

```bash
git clone https://github.com/FeeiCN/slide-writer
```

<sub><b>Style ids</b> `before-after` · `writer` · `test-antgroup-eric` · `test-tencent-pony-ma` · `test-alibaba-jack-ma` — name one when you ask for a deck. These are the project's own strings, read from its filenames and captions, not names this registry made up; each id's own sample image is listed by that command.</sub>

<img src="https://raw.githubusercontent.com/FeeiCN/slide-writer/3c4524c4abb3310fdee106282d0a64f156fd4ff6/examples/before-after.png" width="100%" alt="Slide-Writer Demo">

<sub><b>Slide-Writer Demo</b> · <code>before-after</code> · <a href="https://github.com/FeeiCN/slide-writer/blob/3c4524c4abb3310fdee106282d0a64f156fd4ff6/examples/before-after.png"><code>examples/before-after.png</code></a></sub>

<img src="https://raw.githubusercontent.com/FeeiCN/slide-writer/3c4524c4abb3310fdee106282d0a64f156fd4ff6/examples/slide-writer.png" width="100%" alt="Slide-Writer">

<sub><b>Slide-Writer</b> · <a href="https://github.com/FeeiCN/slide-writer/blob/3c4524c4abb3310fdee106282d0a64f156fd4ff6/examples/slide-writer.png"><code>examples/slide-writer.png</code></a></sub>

<a id="gallery-powerpoint-fancy-design"></a>

#### [PowerPoint Fancy Design](https://github.com/Phlegonlabs/Powerpoint-fancy-design) · 33 ⭐ · Both

<sub>Page-structured Markdown into styled 1600x900 HTML slides, PNG renders and exports.</sub>

<sub>2 of 30 images in [`Phlegonlabs/Powerpoint-fancy-design`](https://github.com/Phlegonlabs/Powerpoint-fancy-design) · both are the project's own README picks</sub>

```bash
git clone https://github.com/Phlegonlabs/Powerpoint-fancy-design
```

<sub><b>Style ids</b> `swiss-international` · `east-asian-minimalism` · `risograph-print` · `bauhaus-geometry` · `organic-handcrafted` · `art-deco-luxury` · `neo-brutalism` · `retro-futurism` · `dark-editorial` · `memphis-pop` — name one when you ask for a deck. These are the project's own strings, read from its filenames and captions, not names this registry made up; each id's own sample image is listed by that command.</sub>

<img src="https://raw.githubusercontent.com/Phlegonlabs/Powerpoint-fancy-design/d6167dbc5d1ee9a0f3b2b90b399156322e9178ae/assets/style-preview-a.png" width="100%" alt="Swiss International">

<sub><b>Swiss International</b> · <a href="https://github.com/Phlegonlabs/Powerpoint-fancy-design/blob/d6167dbc5d1ee9a0f3b2b90b399156322e9178ae/assets/style-preview-a.png"><code>assets/style-preview-a.png</code></a></sub>

<img src="https://raw.githubusercontent.com/Phlegonlabs/Powerpoint-fancy-design/d6167dbc5d1ee9a0f3b2b90b399156322e9178ae/assets/style-preview-b.png" width="100%" alt="East Asian Minimalism">

<sub><b>East Asian Minimalism</b> · <a href="https://github.com/Phlegonlabs/Powerpoint-fancy-design/blob/d6167dbc5d1ee9a0f3b2b90b399156322e9178ae/assets/style-preview-b.png"><code>assets/style-preview-b.png</code></a></sub>

<a id="gallery-skills-slides"></a>

#### [Skills Slides](https://github.com/nghiahsgs/skills-slides) · 32 ⭐ · HTML

<sub>50 aesthetics x 20 palettes x 10 fonts x 5 layouts x 30+ effects.</sub>

<sub>2 of 4 images in [`nghiahsgs/skills-slides`](https://github.com/nghiahsgs/skills-slides) · both are the project's own README picks</sub>

```bash
git clone https://github.com/nghiahsgs/skills-slides
```

<sub><b>Style ids</b> `06-features` · `07-checklist` · `03-50k` — name one when you ask for a deck. These are the project's own strings, read from its filenames and captions, not names this registry made up; each id's own sample image is listed by that command.</sub>

<img src="https://raw.githubusercontent.com/nghiahsgs/skills-slides/c271d3cda03bf79733cc91ba28e25716196638b7/examples/screenshots/slide-06-features.png" width="100%" alt="Feature grid — 6 cards with 3D tilt hover">

<sub><b>Feature grid — 6 cards with 3D tilt hover</b> · <code>06-features</code> · <a href="https://github.com/nghiahsgs/skills-slides/blob/c271d3cda03bf79733cc91ba28e25716196638b7/examples/screenshots/slide-06-features.png"><code>examples/screenshots/slide-06-features.png</code></a></sub>

<img src="https://raw.githubusercontent.com/nghiahsgs/skills-slides/c271d3cda03bf79733cc91ba28e25716196638b7/examples/screenshots/slide-07-checklist.png" width="100%" alt="Anti-slop checklist — 10-point quality gate">

<sub><b>Anti-slop checklist — 10-point quality gate</b> · <code>07-checklist</code> · <a href="https://github.com/nghiahsgs/skills-slides/blob/c271d3cda03bf79733cc91ba28e25716196638b7/examples/screenshots/slide-07-checklist.png"><code>examples/screenshots/slide-07-checklist.png</code></a></sub>

<a id="gallery-pptx-from-layouts"></a>

#### [PPTX from Layouts](https://github.com/tristan-mcinnis/pptx-from-layouts-skill) · 30 ⭐ · PPTX

<sub>Generate decks from markdown strictly through a template's slide master layouts.</sub>

<sub>1 of 1 images in [`tristan-mcinnis/pptx-from-layouts-skill`](https://github.com/tristan-mcinnis/pptx-from-layouts-skill)</sub>

```bash
git clone https://github.com/tristan-mcinnis/pptx-from-layouts-skill
```

<img src="https://raw.githubusercontent.com/tristan-mcinnis/pptx-from-layouts-skill/53b0e750694d807e3510c2017744197c3c5089b0/examples/q1-strategy/thumbnail.jpg" width="100%" alt="PPTX from Layouts sample">

<sub><b>Thumbnail</b> · <a href="https://github.com/tristan-mcinnis/pptx-from-layouts-skill/blob/53b0e750694d807e3510c2017744197c3c5089b0/examples/q1-strategy/thumbnail.jpg"><code>examples/q1-strategy/thumbnail.jpg</code></a></sub>

<a id="gallery-excalidraw-slides-skills"></a>

#### [Excalidraw Slides Generator](https://github.com/ZunbaRan/excalidraw-slides-skills) · 18 ⭐ · Framework

<sub>Two-phase workflow that turns text into 16:9 Excalidraw slides with generated SVG art.</sub>

<sub>2 of 5 images in [`ZunbaRan/excalidraw-slides-skills`](https://github.com/ZunbaRan/excalidraw-slides-skills) · both are the project's own README picks</sub>


<img src="https://github.com/user-attachments/assets/44db2400-3c6a-4de9-8c37-b26759b284c0" width="100%" alt="image">

<sub><b>image</b> · GitHub attachment</sub>

<img src="https://github.com/user-attachments/assets/89f3fc36-f0b7-45e7-b457-01e3b4f00e28" width="100%" alt="image">

<sub><b>image</b> · GitHub attachment</sub>

<a id="gallery-econ-slides-skill"></a>

#### [Econ Slides Skill](https://github.com/hanlulong/econ-slides-skill) · 14 ⭐ · Framework

<sub>Turns an economics paper into a Beamer seminar talk, with a timed speaker script.</sub>

<sub>2 of 5 images in [`hanlulong/econ-slides-skill`](https://github.com/hanlulong/econ-slides-skill) · both are the project's own README picks</sub>

```bash
git clone https://github.com/hanlulong/econ-slides-skill ~/.claude/skills/econ-slides
```

<sub><b>Style ids</b> `punchline` · `mainresult` · `fig2-event-study` · `fig1-rollout` · `fig3-cohorts` — name one when you ask for a deck. These are the project's own strings, read from its filenames and captions, not names this registry made up; each id's own sample image is listed by that command.</sub>

<img src="https://raw.githubusercontent.com/hanlulong/econ-slides-skill/4ac998bfa98bc0b59d4d1776b4ced565b34b802c/docs/images/sample-punchline.png" width="100%" alt="Punchline slide from an AI-built Beamer talk: the main result, one supporting heterogeneity pattern, and the implication">

<sub><b>Punchline slide from an AI-built Beamer talk: the main result, one supporting heterogeneity pattern, and the i</b> · <a href="https://github.com/hanlulong/econ-slides-skill/blob/4ac998bfa98bc0b59d4d1776b4ced565b34b802c/docs/images/sample-punchline.png"><code>docs/images/sample-punchline.png</code></a></sub>

<img src="https://raw.githubusercontent.com/hanlulong/econ-slides-skill/4ac998bfa98bc0b59d4d1776b4ced565b34b802c/docs/images/sample-mainresult.png" width="100%" alt="Main-result slide: four exact Table 2 estimates with one highlighted cell and a concise economic reading">

<sub><b>Main-result slide: four exact Table 2 estimates with one highlighted cell and a concise economic reading</b> · <code>mainresult</code> · <a href="https://github.com/hanlulong/econ-slides-skill/blob/4ac998bfa98bc0b59d4d1776b4ced565b34b802c/docs/images/sample-mainresult.png"><code>docs/images/sample-mainresult.png</code></a></sub>

<a id="gallery-oc-sdk-ppt"></a>

#### [OpenCode PPT Studio](https://github.com/Honghurumeng/oc_sdk_ppt) · 13 ⭐ · Both

<sub>Web app that drafts an outline, refines it in a second session, then builds HTML and PPTX.</sub>

<sub>2 of 3 images in [`Honghurumeng/oc_sdk_ppt`](https://github.com/Honghurumeng/oc_sdk_ppt) · both are the project's own README picks</sub>

<sub><b>Style ids</b> `html` · `llm` — name one when you ask for a deck. These are the project's own strings, read from its filenames and captions, not names this registry made up; each id's own sample image is listed by that command.</sub>

<img src="https://raw.githubusercontent.com/Honghurumeng/oc_sdk_ppt/3e2b8ba28d8c49f36c1bf1f98b14f4c3596dd9bd/images/3.png" width="100%" alt="HTML 预览与版本切换：支持按意见调整并激活某个版本">

<sub><b>HTML 预览与版本切换：支持按意见调整并激活某个版本</b> · <a href="https://github.com/Honghurumeng/oc_sdk_ppt/blob/3e2b8ba28d8c49f36c1bf1f98b14f4c3596dd9bd/images/3.png"><code>images/3.png</code></a></sub>

<img src="https://raw.githubusercontent.com/Honghurumeng/oc_sdk_ppt/3e2b8ba28d8c49f36c1bf1f98b14f4c3596dd9bd/images/2.png" width="100%" alt="构建日志：校验失败后自动修复并重试">

<sub><b>构建日志：校验失败后自动修复并重试</b> · <a href="https://github.com/Honghurumeng/oc_sdk_ppt/blob/3e2b8ba28d8c49f36c1bf1f98b14f4c3596dd9bd/images/2.png"><code>images/2.png</code></a></sub>

<a id="gallery-kr-brand-decks"></a>

#### [KR Brand Decks](https://github.com/sylvanus4/kr-brand-decks) · 5~ ⭐ · Templates

<sub>23 skills, one per Korean enterprise brand, each building an on-brand PPTX from scratch.</sub>

<sub>2 of 30 images in [`sylvanus4/kr-brand-decks`](https://github.com/sylvanus4/kr-brand-decks) · one of them is the project's own README pick</sub>

```bash
/plugin marketplace add sylvanus4/kr-brand-decks && /plugin install kr-brand-decks@kr-brand-decks
```

<sub><b>Style ids</b> `gallery` · `themes-gallery` · `celltrion` · `cj-cheiljedang` · `doosan` · `hanwha` · `hd-hyundai` · `hyundai-motor` · `kakao` · `kb-financial` · `kia` · `lg-electronics` · 11 more via `python scripts/pick.py styles kr-brand-decks` — name one when you ask for a deck. These are the project's own strings, read from its filenames and captions, not names this registry made up; each id's own sample image is listed by that command.</sub>

<img src="https://raw.githubusercontent.com/sylvanus4/kr-brand-decks/c6735ab91fb24afe31220358b419f87fb171d6d1/docs/gallery.png" width="100%" alt="Gallery of 23 brand cover slides">

<sub><b>Gallery of 23 brand cover slides</b> · <a href="https://github.com/sylvanus4/kr-brand-decks/blob/c6735ab91fb24afe31220358b419f87fb171d6d1/docs/gallery.png"><code>docs/gallery.png</code></a></sub>

<img src="https://raw.githubusercontent.com/sylvanus4/kr-brand-decks/c6735ab91fb24afe31220358b419f87fb171d6d1/docs/themes-gallery.png" width="100%" alt="KR Brand Decks sample">

<sub><b>Themes Gallery</b> · <a href="https://github.com/sylvanus4/kr-brand-decks/blob/c6735ab91fb24afe31220358b419f87fb171d6d1/docs/themes-gallery.png"><code>docs/themes-gallery.png</code></a></sub>

<a id="gallery-cuhk-slides-template-html"></a>

#### [CUHK Slides Template (HTML)](https://github.com/HarlandZZC/cuhk-slides-template-html) · 4 ⭐ · Templates

<sub>One self-contained HTML slide template in CUHK colours, plus a Markdown-to-slides skill.</sub>

<sub>2 of 2 images in [`HarlandZZC/cuhk-slides-template-html`](https://github.com/HarlandZZC/cuhk-slides-template-html) · one of them is the project's own README pick</sub>

```bash
git clone https://github.com/HarlandZZC/cuhk-slides-template-html && cp -r skills/md-to-cuhk-slides .claude/skills/
```

<sub><b>Style ids</b> `title` · `your-figure` — name one when you ask for a deck. These are the project's own strings, read from its filenames and captions, not names this registry made up; each id's own sample image is listed by that command.</sub>

<img src="https://raw.githubusercontent.com/HarlandZZC/cuhk-slides-template-html/ee6ed50a5136d98c1fb06d48ee7112e3a45714d5/docs/screenshots/title.png" width="100%" alt="Title slide preview">

<sub><b>Title slide preview</b> · <a href="https://github.com/HarlandZZC/cuhk-slides-template-html/blob/ee6ed50a5136d98c1fb06d48ee7112e3a45714d5/docs/screenshots/title.png"><code>docs/screenshots/title.png</code></a></sub>

<img src="https://raw.githubusercontent.com/HarlandZZC/cuhk-slides-template-html/ee6ed50a5136d98c1fb06d48ee7112e3a45714d5/your-figure.png" width="100%" alt="CUHK Slides Template (HTML) sample">

<sub><b>Your Figure</b> · <a href="https://github.com/HarlandZZC/cuhk-slides-template-html/blob/ee6ed50a5136d98c1fb06d48ee7112e3a45714d5/your-figure.png"><code>your-figure.png</code></a></sub>

<a id="gallery-3d-html-slide-skill"></a>

#### [3D HTML Slide Skill](https://github.com/yoshifujidesign/3d-html-slide-skill) · 3 ⭐ · HTML

<sub>Claude Code skill that generates a single-file HTML slide deck with Three.js wireframe backgrounds.</sub>

<sub>2 of 2 images in [`yoshifujidesign/3d-html-slide-skill`](https://github.com/yoshifujidesign/3d-html-slide-skill) · both are the project's own README picks</sub>


<img src="https://github.com/user-attachments/assets/7d150a1c-73ee-429a-8315-8be2650ebe11" width="100%" alt="WS002985">

<sub><b>WS002985</b> · GitHub attachment</sub>

<img src="https://github.com/user-attachments/assets/1e3be001-6598-40b8-bf9f-da10e7d77f5d" width="100%" alt="EP133-2_2">

<sub><b>EP133-2_2</b> · GitHub attachment</sub>

<a id="gallery-image-to-editable-ppt-skill-zhoujie97"></a>

#### [Image to Editable PPT Skill (zhoujie97)](https://github.com/zhoujie97/image-to-editable-ppt-skill) · 3 ⭐ · PPTX

<sub>Rebuilds screenshots and infographics into editable PowerPoint shapes, text boxes and SVG icons.</sub>

<sub>2 of 4 images in [`zhoujie97/image-to-editable-ppt-skill`](https://github.com/zhoujie97/image-to-editable-ppt-skill) · both are the project's own README picks</sub>

<sub><b>Style ids</b> `效果图1` · `效果图2` · `原图2` · `原图1` — name one when you ask for a deck. These are the project's own strings, read from its filenames and captions, not names this registry made up; each id's own sample image is listed by that command.</sub>

<img src="https://raw.githubusercontent.com/zhoujie97/image-to-editable-ppt-skill/e3c39d907ec6abf5266e4491c6aa001b663b9207/%E6%95%88%E6%9E%9C%E5%9B%BE/%E6%95%88%E6%9E%9C%E5%9B%BE2.png" width="100%" alt="alt text">

<sub><b>alt text</b> · <code>效果图2</code> · <a href="https://github.com/zhoujie97/image-to-editable-ppt-skill/blob/e3c39d907ec6abf5266e4491c6aa001b663b9207/效果图/效果图2.png"><code>效果图/效果图2.png</code></a></sub>

<img src="https://raw.githubusercontent.com/zhoujie97/image-to-editable-ppt-skill/e3c39d907ec6abf5266e4491c6aa001b663b9207/%E6%95%88%E6%9E%9C%E5%9B%BE/%E5%8E%9F%E5%9B%BE2.png" width="100%" alt="alt text">

<sub><b>alt text</b> · <code>原图2</code> · <a href="https://github.com/zhoujie97/image-to-editable-ppt-skill/blob/e3c39d907ec6abf5266e4491c6aa001b663b9207/效果图/原图2.png"><code>效果图/原图2.png</code></a></sub>

<a id="gallery-taohtml"></a>

#### [TaoHtml](https://github.com/TaoGEO/TaoHtml) · 3 ⭐ · HTML

<sub>Redesigns an existing Word, PDF or PPT into a 16:9 offline HTML deck with staged animation.</sub>

<sub>2 of 12 images in [`TaoGEO/TaoHtml`](https://github.com/TaoGEO/TaoHtml) · both are the project's own README picks</sub>

<sub><b>Style ids</b> `reference-style-reconstruction` · `corporate-template-fidelity` · `built-in-visual-systems` · `reference-vi-board` · `corporate-family` · `01-ai-search-mechanism` · `02-geo-four-keywords` · `03-recall-process` · `04-retest-report` · `corporate-template-reference` · `corporate-family-section` — name one when you ask for a deck. These are the project's own strings, read from its filenames and captions, not names this registry made up; each id's own sample image is listed by that command.</sub>

<img src="https://raw.githubusercontent.com/TaoGEO/TaoHtml/3f304ab6ea8d42dd99b5dee28d4bb81b84485d98/docs/assets/readme/v0.3.0/reference-style-reconstruction.png" width="100%" alt="参考风格重构 VI 设计标准图">

<sub><b>参考风格重构 VI 设计标准图</b> · <code>reference-style-reconstruction</code> · <a href="https://github.com/TaoGEO/TaoHtml/blob/3f304ab6ea8d42dd99b5dee28d4bb81b84485d98/docs/assets/readme/v0.3.0/reference-style-reconstruction.png"><code>docs/assets/readme/v0.3.0/reference-style-reconstruction.png</code></a></sub>

<img src="https://raw.githubusercontent.com/TaoGEO/TaoHtml/3f304ab6ea8d42dd99b5dee28d4bb81b84485d98/docs/assets/readme/v0.3.0/built-in-visual-systems.png" width="100%" alt="TaoHtml 四套内置视觉系统各五页总览">

<sub><b>TaoHtml 四套内置视觉系统各五页总览</b> · <code>built-in-visual-systems</code> · <a href="https://github.com/TaoGEO/TaoHtml/blob/3f304ab6ea8d42dd99b5dee28d4bb81b84485d98/docs/assets/readme/v0.3.0/built-in-visual-systems.png"><code>docs/assets/readme/v0.3.0/built-in-visual-systems.png</code></a></sub>

<a id="gallery-vyral-tiktok-slideshow-skill"></a>

#### [TikTok Slideshow Command Center](https://github.com/Meliwat/vyral-tiktok-slideshow-skill) · 3 ⭐ · Image

<sub>Plans TikTok photo carousels: content angle, slide design and posting cadence in one pass.</sub>

<sub>2 of 6 images in [`Meliwat/vyral-tiktok-slideshow-skill`](https://github.com/Meliwat/vyral-tiktok-slideshow-skill) · both are the project's own README picks</sub>

<sub><b>Style ids</b> `slide-1` · `slide-3` · `slide-5` · `command-center` · `renders` — name one when you ask for a deck. These are the project's own strings, read from its filenames and captions, not names this registry made up; each id's own sample image is listed by that command.</sub>

<img src="https://raw.githubusercontent.com/Meliwat/vyral-tiktok-slideshow-skill/f22e11a960c06d706cacbccccf5ff20985e70b9d/docs/command-center.png" width="100%" alt="The Command Center planning board">

<sub><b>The Command Center planning board</b> · <a href="https://github.com/Meliwat/vyral-tiktok-slideshow-skill/blob/f22e11a960c06d706cacbccccf5ff20985e70b9d/docs/command-center.png"><code>docs/command-center.png</code></a></sub>

<img src="https://raw.githubusercontent.com/Meliwat/vyral-tiktok-slideshow-skill/f22e11a960c06d706cacbccccf5ff20985e70b9d/skill/examples/renders/slide-03.jpg" width="100%" alt="Slide 3">

<sub><b>Slide 3</b> · <a href="https://github.com/Meliwat/vyral-tiktok-slideshow-skill/blob/f22e11a960c06d706cacbccccf5ff20985e70b9d/skill/examples/renders/slide-03.jpg"><code>skill/examples/renders/slide-03.jpg</code></a></sub>

<a id="gallery-pptwork"></a>

#### [PPTWork](https://github.com/JunfengRan/PPTWork) · 2 ⭐ · PPTX

<sub>Two Anthropic-style Skills that plan, author, and export PowerPoint decks from HTML.</sub>

<sub>2 of 28 images in [`JunfengRan/PPTWork`](https://github.com/JunfengRan/PPTWork) · both are the project's own README picks</sub>

```bash
git clone https://github.com/JunfengRan/PPTWork && cd PPTWork/ppt && npm install
```

<sub><b>Style ids</b> `showcase-bento` · `showcase-kpi` · `showcase-two-col` · `showcase-export` — name one when you ask for a deck. These are the project's own strings, read from its filenames and captions, not names this registry made up; each id's own sample image is listed by that command.</sub>

<img src="https://raw.githubusercontent.com/JunfengRan/PPTWork/c538d921935f96e4f7706af9370f61198b34c5da/examples/showcase/showcase-bento.png" width="100%" alt="Two skills bento layout">

<sub><b>Two skills bento layout</b> · <code>showcase-bento</code> · <a href="https://github.com/JunfengRan/PPTWork/blob/c538d921935f96e4f7706af9370f61198b34c5da/examples/showcase/showcase-bento.png"><code>examples/showcase/showcase-bento.png</code></a></sub>

<img src="https://raw.githubusercontent.com/JunfengRan/PPTWork/c538d921935f96e4f7706af9370f61198b34c5da/examples/showcase/showcase-kpi.png" width="100%" alt="AI agent market KPI row">

<sub><b>AI agent market KPI row</b> · <code>showcase-kpi</code> · <a href="https://github.com/JunfengRan/PPTWork/blob/c538d921935f96e4f7706af9370f61198b34c5da/examples/showcase/showcase-kpi.png"><code>examples/showcase/showcase-kpi.png</code></a></sub>

<a id="gallery-inspiration-deck-workshop"></a>

#### [Inspiration Deck Workshop](https://github.com/zjsthmjialin/inspiration-deck-workshop) · 2 ⭐ · Templates

<sub>23 themes and 25 page layouts for animated static HTML decks, driven from a small CLI.</sub>

<sub>2 of 23 images in [`zjsthmjialin/inspiration-deck-workshop`](https://github.com/zjsthmjialin/inspiration-deck-workshop) · both are the project's own README picks</sub>

```bash
git clone https://github.com/zjsthmjialin/inspiration-deck-workshop && node tools/cli.mjs new my-deck --template product-launch
```

<sub><b>Style ids</b> `18-black-gold-stage` · `19-platinum-launch` · `21-signal-dashboard` · `23-vivid-pop` · `00-all-themes-contact-sheet` · `01-clear-board` · `02-mist-blue` · `03-data-brief` · `04-deep-code` · `05-terminal-signal` · `06-blueprint-grid` · `07-soft-card` · 11 more via `python scripts/pick.py styles inspiration-deck-workshop` — name one when you ask for a deck. These are the project's own strings, read from its filenames and captions, not names this registry made up; each id's own sample image is listed by that command.</sub>

<img src="https://raw.githubusercontent.com/zjsthmjialin/inspiration-deck-workshop/2c13fdf624b35b11b657d41273ec1a7930786643/docs/assets/theme-showcase/18-black-gold-stage.png" width="100%" alt="Black Gold Stage">

<sub><b>Black Gold Stage</b> · <code>18-black-gold-stage</code> · <a href="https://github.com/zjsthmjialin/inspiration-deck-workshop/blob/2c13fdf624b35b11b657d41273ec1a7930786643/docs/assets/theme-showcase/18-black-gold-stage.png"><code>docs/assets/theme-showcase/18-black-gold-stage.png</code></a></sub>

<img src="https://raw.githubusercontent.com/zjsthmjialin/inspiration-deck-workshop/2c13fdf624b35b11b657d41273ec1a7930786643/docs/assets/theme-showcase/19-platinum-launch.png" width="100%" alt="Platinum Launch">

<sub><b>Platinum Launch</b> · <code>19-platinum-launch</code> · <a href="https://github.com/zjsthmjialin/inspiration-deck-workshop/blob/2c13fdf624b35b11b657d41273ec1a7930786643/docs/assets/theme-showcase/19-platinum-launch.png"><code>docs/assets/theme-showcase/19-platinum-launch.png</code></a></sub>

<a id="gallery-university-ppt-skill"></a>

#### [University PPT Skill](https://github.com/SiyuQiannn/university-ppt-skill) · 1 ⭐ · Templates

<sub>Editable university-branded PPTX built from school theme tokens and a reusable layout library.</sub>

<sub>2 of 10 images in [`SiyuQiannn/university-ppt-skill`](https://github.com/SiyuQiannn/university-ppt-skill) · one of them is the project's own README pick</sub>

```bash
git clone https://github.com/SiyuQiannn/university-ppt-skill
```

<sub><b>Style ids</b> `contact-sheet` · `02-图文案例证据-源模板复刻` · `05-对比分析框架-源模板复刻` · `03-流程时间线阶段-源模板复刻` · `01-综合卡片要点-源模板复刻` · `06-数据图表表格-源模板复刻` · `08-循环网络关系-源模板复刻` · `spec-driven-demo-contact-sheet` · `04-层级金字塔框架-源模板复刻` · `10-图标素材库-源模板复刻` — name one when you ask for a deck. These are the project's own strings, read from its filenames and captions, not names this registry made up; each id's own sample image is listed by that command.</sub>

<img src="https://raw.githubusercontent.com/SiyuQiannn/university-ppt-skill/0bcbaf2b4f332850ca929c990e00e03771a7349b/examples/preview_contact_sheet.png" width="100%" alt="Preview">

<sub><b>Preview</b> · <code>contact-sheet</code> · <a href="https://github.com/SiyuQiannn/university-ppt-skill/blob/0bcbaf2b4f332850ca929c990e00e03771a7349b/examples/preview_contact_sheet.png"><code>examples/preview_contact_sheet.png</code></a></sub>

<img src="https://raw.githubusercontent.com/SiyuQiannn/university-ppt-skill/0bcbaf2b4f332850ca929c990e00e03771a7349b/skill/university-ppt/assets/content-layouts/ruc_core/preview_02_%E5%9B%BE%E6%96%87%E6%A1%88%E4%BE%8B%E8%AF%81%E6%8D%AE_%E6%BA%90%E6%A8%A1%E6%9D%BF%E5%A4%8D%E5%88%BB.png" width="100%" alt="University PPT Skill sample">

<sub><b>02 图文案例证据 源模板复刻</b> · <a href="https://github.com/SiyuQiannn/university-ppt-skill/blob/0bcbaf2b4f332850ca929c990e00e03771a7349b/skill/university-ppt/assets/content-layouts/ruc_core/preview_02_图文案例证据_源模板复刻.png"><code>skill/university-ppt/assets/content-layouts/ruc_core/preview_02_图文案例证据_源模板复刻.png</code></a></sub>

<a id="gallery-claude-ppt-skills"></a>

#### [Claude PPT Skills](https://github.com/sunxiaohui2025/claude-ppt-skills) · 1 ⭐ · HTML

<sub>Single-file HTML decks in six styles, with in-browser editing and a thumbnail overview grid.</sub>

<sub>2 of 3 images in [`sunxiaohui2025/claude-ppt-skills`](https://github.com/sunxiaohui2025/claude-ppt-skills) · both are the project's own README picks</sub>


<img src="https://github.com/user-attachments/assets/d8742e1d-0fc1-4930-ac9a-6cc783fd47cd" width="100%" alt="截屏2026-05-28 15 23 36">

<sub><b>截屏2026-05-28 15 23 36</b> · GitHub attachment</sub>

<img src="https://github.com/user-attachments/assets/df1b2e93-14b7-49ac-b0e9-0d99e630d382" width="100%" alt="image">

<sub><b>image</b> · GitHub attachment</sub>

<a id="gallery-course-html-slides-skill"></a>

#### [Course HTML Slides Builder](https://github.com/HelenSong/course-html-slides-skill) · 1 ⭐ · HTML

<sub>Turns a course outline into multi-page HTML slides built for classroom projection.</sub>

<sub>2 of 9 images in [`HelenSong/course-html-slides-skill`](https://github.com/HelenSong/course-html-slides-skill) · one of them is the project's own README pick</sub>

<sub><b>Style ids</b> `collage` · `p01` · `p02-hook` · `p03-driving-question` · `p04-project-intro` · `p06-role-guide` · `p08-writing-guide` · `p11-practice` · `p12-share` — name one when you ask for a deck. These are the project's own strings, read from its filenames and captions, not names this registry made up; each id's own sample image is listed by that command.</sub>

<img src="https://raw.githubusercontent.com/HelenSong/course-html-slides-skill/6e2c36a1f8a934cbfa89ffc27a562b70206a777c/docs/collage.png" width="100%" alt="Slide Collage">

<sub><b>Slide Collage</b> · <a href="https://github.com/HelenSong/course-html-slides-skill/blob/6e2c36a1f8a934cbfa89ffc27a562b70206a777c/docs/collage.png"><code>docs/collage.png</code></a></sub>

<img src="https://raw.githubusercontent.com/HelenSong/course-html-slides-skill/6e2c36a1f8a934cbfa89ffc27a562b70206a777c/docs/screenshots/p02-hook.png" width="100%" alt="Course HTML Slides Builder sample">

<sub><b>P02 Hook</b> · <a href="https://github.com/HelenSong/course-html-slides-skill/blob/6e2c36a1f8a934cbfa89ffc27a562b70206a777c/docs/screenshots/p02-hook.png"><code>docs/screenshots/p02-hook.png</code></a></sub>

<a id="gallery-google-slides-skill"></a>

#### [Google Slides Deck Skill](https://github.com/eranw2000/google-slides-skill) · 1 ⭐ · Framework

<sub>Rebuilds a Google Slides deck through the API, rendering each slide to PNG to check its work.</sub>

<sub>1 of 1 images in [`eranw2000/google-slides-skill`](https://github.com/eranw2000/google-slides-skill) · one of them is the project's own README pick</sub>

```bash
cp -R google-slides-skill/enhance-slides ~/.claude/skills/
```

<sub><b>Style ids</b> `enhance-slides-flow` — name one when you ask for a deck. These are the project's own strings, read from its filenames and captions, not names this registry made up; each id's own sample image is listed by that command.</sub>

<img src="https://raw.githubusercontent.com/eranw2000/google-slides-skill/43127d4e79f963be2243e0369b779baf453eac28/docs/enhance-slides-flow.png" width="100%" alt="enhance-slides flow">

<sub><b>enhance-slides flow</b> · <a href="https://github.com/eranw2000/google-slides-skill/blob/43127d4e79f963be2243e0369b779baf453eac28/docs/enhance-slides-flow.png"><code>docs/enhance-slides-flow.png</code></a></sub>

<a id="gallery-agent-pptify-kit"></a>

#### [PPTX Deck Creation Kit](https://github.com/kimtth/agent-pptify-kit) · 1 ⭐ · PPTX

<sub>Coordinate-explicit PPTX specs that stay native objects, shipped as a Copilot plugin.</sub>

<sub>2 of 3 images in [`kimtth/agent-pptify-kit`](https://github.com/kimtth/agent-pptify-kit) · both are the project's own README picks</sub>

<sub><b>Style ids</b> `pptify-kit-stress-demo-contact-sheet` · `pptify-kit-stress-demo-v3-contact-sheet` · `pptify-kit-stress-demo-v2-contact-sheet` — name one when you ask for a deck. These are the project's own strings, read from its filenames and captions, not names this registry made up; each id's own sample image is listed by that command.</sub>

<img src="https://raw.githubusercontent.com/kimtth/agent-pptify-kit/831c9107b522baa8131e27c47d4cf04af5e54d93/docs/preview/pptify-kit-stress-demo-contact-sheet.png" width="100%" alt="Contact sheet of all 81 layouts in pptify-kit-stress-demo.pptx">

<sub><b>Contact sheet of all 81 layouts in pptify-kit-stress-demo.pptx</b> · <code>pptify-kit-stress-demo-contact-sheet</code> · <a href="https://github.com/kimtth/agent-pptify-kit/blob/831c9107b522baa8131e27c47d4cf04af5e54d93/docs/preview/pptify-kit-stress-demo-contact-sheet.png"><code>docs/preview/pptify-kit-stress-demo-contact-sheet.png</code></a></sub>

<img src="https://raw.githubusercontent.com/kimtth/agent-pptify-kit/831c9107b522baa8131e27c47d4cf04af5e54d93/docs/preview/pptify-kit-stress-demo-v3-contact-sheet.png" width="100%" alt="Contact sheet of all 60 layouts in pptify-kit-stress-demo-v3.pptx">

<sub><b>Contact sheet of all 60 layouts in pptify-kit-stress-demo-v3.pptx</b> · <code>pptify-kit-stress-demo-v3-contact-sheet</code> · <a href="https://github.com/kimtth/agent-pptify-kit/blob/831c9107b522baa8131e27c47d4cf04af5e54d93/docs/preview/pptify-kit-stress-demo-v3-contact-sheet.png"><code>docs/preview/pptify-kit-stress-demo-v3-contact-sheet.png</code></a></sub>

<a id="gallery-ppt-deck-builder-skill"></a>

#### [PPT Deck Builder Skill](https://github.com/lk251066/ppt-deck-builder-skill) · 1 ⭐ · Image

<sub>Renders each page as a finished image, repairs only the bad pages, then packs a PPTX.</sub>

<sub>2 of 4 images in [`lk251066/ppt-deck-builder-skill`](https://github.com/lk251066/ppt-deck-builder-skill) · both are the project's own README picks</sub>

<sub><b>Style ids</b> `slide-01` · `slide-04` · `slide-06` · `slide-08` — name one when you ask for a deck. These are the project's own strings, read from its filenames and captions, not names this registry made up; each id's own sample image is listed by that command.</sub>

<img src="https://raw.githubusercontent.com/lk251066/ppt-deck-builder-skill/aa3c9a23717aa836f6397407bfe7226969bd29bb/examples/grsai_ai_science_deck_micro_modules/slide-04.png" width="100%" alt="slide-04">

<sub><b>slide-04</b> · <a href="https://github.com/lk251066/ppt-deck-builder-skill/blob/aa3c9a23717aa836f6397407bfe7226969bd29bb/examples/grsai_ai_science_deck_micro_modules/slide-04.png"><code>examples/grsai_ai_science_deck_micro_modules/slide-04.png</code></a></sub>

<img src="https://raw.githubusercontent.com/lk251066/ppt-deck-builder-skill/aa3c9a23717aa836f6397407bfe7226969bd29bb/examples/grsai_ai_science_deck_micro_modules/slide-06.png" width="100%" alt="slide-06">

<sub><b>slide-06</b> · <a href="https://github.com/lk251066/ppt-deck-builder-skill/blob/aa3c9a23717aa836f6397407bfe7226969bd29bb/examples/grsai_ai_science_deck_micro_modules/slide-06.png"><code>examples/grsai_ai_science_deck_micro_modules/slide-06.png</code></a></sub>

<a id="gallery-paper-deck-reveal"></a>

#### [Paper Deck Reveal](https://github.com/O0000-code/paper-deck-reveal) · 0 ⭐ · Framework

<sub>Reveal.js skill that turns an academic paper into an offline deck with interactive demos.</sub>

<sub>2 of 22 images in [`O0000-code/paper-deck-reveal`](https://github.com/O0000-code/paper-deck-reveal) · both are the project's own README picks</sub>

```bash
git clone https://github.com/O0000-code/paper-deck-reveal && cd paper-deck-reveal
```

<sub><b>Style ids</b> `hero` · `funnel` · `forest` · `interactive` · `speaker` · `presets` · `rstb20200390f02` · `rstb20200390f03` · `rstb20200390f06` · `rstb20200390f04` — name one when you ask for a deck. These are the project's own strings, read from its filenames and captions, not names this registry made up; each id's own sample image is listed by that command.</sub>

<img src="https://raw.githubusercontent.com/O0000-code/paper-deck-reveal/9b1b779f0ffc31e5f5fb726ddc36b1c89a119a46/docs/screenshots/hero.png" width="100%" alt="Cover slide of a journal-club deck: a red hairline rule, a Chinese framing question set above the paper's English title ">

<sub><b>Cover slide of a journal-club deck: a red hairline rule, a Chinese framing question set above the paper's Engl</b> · <code>hero</code> · <a href="https://github.com/O0000-code/paper-deck-reveal/blob/9b1b779f0ffc31e5f5fb726ddc36b1c89a119a46/docs/screenshots/hero.png"><code>docs/screenshots/hero.png</code></a></sub>

<img src="https://raw.githubusercontent.com/O0000-code/paper-deck-reveal/9b1b779f0ffc31e5f5fb726ddc36b1c89a119a46/docs/screenshots/funnel.png" width="100%" alt="Participant funnel slide: recruited N = 976 → excluded −59 → analysed N = 917">

<sub><b>Participant funnel slide: recruited N = 976 → excluded −59 → analysed N = 917</b> · <a href="https://github.com/O0000-code/paper-deck-reveal/blob/9b1b779f0ffc31e5f5fb726ddc36b1c89a119a46/docs/screenshots/funnel.png"><code>docs/screenshots/funnel.png</code></a></sub>

<a id="gallery-ghb-ppt-skill"></a>

#### [GHB PPT Skill](https://github.com/NickyLam/GHB-PPT-Skill) · 0 ⭐ · PPTX

<sub>Corporate-template PPTX where SVG becomes editable DrawingML, verified fully offline.</sub>

<sub>1 of 1 images in [`NickyLam/GHB-PPT-Skill`](https://github.com/NickyLam/GHB-PPT-Skill)</sub>

```bash
python3 -m pip install -r requirements.txt && python3 scripts/ghb_ppt.py doctor
```

<img src="https://raw.githubusercontent.com/NickyLam/GHB-PPT-Skill/e7ae128cb7dd7380a27a7d4a1e852beeb6734091/assets/readme/showcase.png" width="100%" alt="GHB PPT Skill sample">

<sub><b>Showcase</b> · <a href="https://github.com/NickyLam/GHB-PPT-Skill/blob/e7ae128cb7dd7380a27a7d4a1e852beeb6734091/assets/readme/showcase.png"><code>assets/readme/showcase.png</code></a></sub>

<a id="gallery-html-presentation-skill"></a>

#### [HTML Presentation Skill](https://github.com/defreitassl/html-presentation-skill) · 0 ⭐ · HTML

<sub>Turns documents, notes or briefs into a standalone HTML presentation, then validates it.</sub>

<sub>2 of 5 images in [`defreitassl/html-presentation-skill`](https://github.com/defreitassl/html-presentation-skill) · both are the project's own README picks</sub>

<sub><b>Style ids</b> `artemis-program-overview` · `artemis-ii-executive-briefing` · `kubernetes-command-center` · `artemis-ii-mission-planner` · `who-air-pollution-dossier` — name one when you ask for a deck. These are the project's own strings, read from its filenames and captions, not names this registry made up; each id's own sample image is listed by that command.</sub>

<img src="https://raw.githubusercontent.com/defreitassl/html-presentation-skill/1e3b4d19d815d1d79b51a2faaf3197a6a272f10a/assets/previews/artemis-program-overview.png" width="100%" alt="Artemis Program Overview preview">

<sub><b>Artemis Program Overview preview</b> · <a href="https://github.com/defreitassl/html-presentation-skill/blob/1e3b4d19d815d1d79b51a2faaf3197a6a272f10a/assets/previews/artemis-program-overview.png"><code>assets/previews/artemis-program-overview.png</code></a></sub>

<img src="https://raw.githubusercontent.com/defreitassl/html-presentation-skill/1e3b4d19d815d1d79b51a2faaf3197a6a272f10a/assets/previews/artemis-ii-executive-briefing.png" width="100%" alt="Artemis II Executive Briefing preview">

<sub><b>Artemis II Executive Briefing preview</b> · <a href="https://github.com/defreitassl/html-presentation-skill/blob/1e3b4d19d815d1d79b51a2faaf3197a6a272f10a/assets/previews/artemis-ii-executive-briefing.png"><code>assets/previews/artemis-ii-executive-briefing.png</code></a></sub>

<a id="gallery-slide-deck-skill"></a>

#### [Slide Deck Skill](https://github.com/jayworker/slide-deck-skill) · 0 ⭐ · HTML

<sub>Single-file 16:9 HTML decks in a light dashboard style, one message per slide.</sub>

<sub>2 of 6 images in [`jayworker/slide-deck-skill`](https://github.com/jayworker/slide-deck-skill) · both are the project's own README picks</sub>

```bash
git clone https://github.com/jayworker/slide-deck-skill "$HOME/.claude/skills/slide-deck"
```

<sub><b>Style ids</b> `3` — name one when you ask for a deck. These are the project's own strings, read from its filenames and captions, not names this registry made up; each id's own sample image is listed by that command.</sub>

<img src="https://raw.githubusercontent.com/jayworker/slide-deck-skill/76ecc8e16804558d8f0d2eb3ff97eb4b29273306/docs/screenshots/slide-2.png" width="100%" alt="3층 구조">

<sub><b>3층 구조</b> · <a href="https://github.com/jayworker/slide-deck-skill/blob/76ecc8e16804558d8f0d2eb3ff97eb4b29273306/docs/screenshots/slide-2.png"><code>docs/screenshots/slide-2.png</code></a></sub>

<img src="https://raw.githubusercontent.com/jayworker/slide-deck-skill/76ecc8e16804558d8f0d2eb3ff97eb4b29273306/docs/screenshots/slide-3.png" width="100%" alt="아이콘 규칙">

<sub><b>아이콘 규칙</b> · <a href="https://github.com/jayworker/slide-deck-skill/blob/76ecc8e16804558d8f0d2eb3ff97eb4b29273306/docs/screenshots/slide-3.png"><code>docs/screenshots/slide-3.png</code></a></sub>

<a id="gallery-marp-slides-studio"></a>

#### [Marp Slides Studio](https://github.com/unsolublesugar/marp-slides-studio) · 0 ⭐ · Templates

<sub>50 Marp themes with a gallery, contrast checker and four agent skills for deck work.</sub>

<sub>2 of 9 images in [`unsolublesugar/marp-slides-studio`](https://github.com/unsolublesugar/marp-slides-studio) · both are the project's own README picks</sub>

```bash
gh repo create my-slides --template unsolublesugar/marp-slides-studio --private --clone && npm install
```

<sub><b>Style ids</b> `theme-preview` · `themes` · `gallery` · `layouts` · `code-block` · `code-block-diff` · `patterns` · `tones` · `themes-select` — name one when you ask for a deck. These are the project's own strings, read from its filenames and captions, not names this registry made up; each id's own sample image is listed by that command.</sub>

<img src="https://raw.githubusercontent.com/unsolublesugar/marp-slides-studio/2d761c1abc2004fd75c06d2c8d225ebff0c21b0a/docs/patterns.png" width="100%" alt="レイアウトパターン">

<sub><b>レイアウトパターン</b> · <code>patterns</code> · <a href="https://github.com/unsolublesugar/marp-slides-studio/blob/2d761c1abc2004fd75c06d2c8d225ebff0c21b0a/docs/patterns.png"><code>docs/patterns.png</code></a></sub>

<img src="https://raw.githubusercontent.com/unsolublesugar/marp-slides-studio/2d761c1abc2004fd75c06d2c8d225ebff0c21b0a/docs/theme-preview.png" width="100%" alt="テーマ切替プレビュー">

<sub><b>テーマ切替プレビュー</b> · <code>theme-preview</code> · <a href="https://github.com/unsolublesugar/marp-slides-studio/blob/2d761c1abc2004fd75c06d2c8d225ebff0c21b0a/docs/theme-preview.png"><code>docs/theme-preview.png</code></a></sub>

<sub>No imagery in the repositories of: Slidev, Quarkdown, Banana Slides, Visual Explainer, HTML Anything, Dashi PPT Skill, Codex PPT Skill, Baoyu Design, Codex Claude Academic Skills, NanoBanana PPT Skills, Gorden PPT Skill, Image to Editable PPT Skill, Oh My PPT, Gorden Super PPT Skills, CyberPPT, Ian Handdrawn PPT, GPT Image2 PPT Skills, PPT Image First, Humanize PPT, PPT Agent Skills, Academic PPTX, Claude Office Skills, Claude Skills, Power Design, Paper2Anything, RW Consulting PPT, Reveal.js Skill, Visual Style PPT Skill, DOM to PPTX, Beamer Skill, Marp Slides, Beamer Academic, Thesis Defense PPTX Skill, Planners PPT Hell, Apple Bento Grid, Hands on Deck, Codex PPT Skill, Skywork Skills, PPT Image2 Editable Rebuild, Claude Design Skill, Slide Image to Editable PPTX, Magic Slide, Presentation Skills, Servasyy Skills, Future Slide, Slide Deck Generator, Make Slide, HTML PPT Designer, PowerPoint Skill, Presentation Skills, Image to PPTX Skill, Literature Report PPT Builder, CN Academic Spark, Starry Slides, AI Paper to Slide Skill, Lieflat HTML Design, Knowledge Cat PPT Skill, Visual Cognition Slides, PPT Report Skills, SJTU PPT Template Skill, Space Multi Design PPT, Deck Factory, Awesome PPT Skills, HTML to Editable PPTX, Editable Image to PPT Skill, Huawei Style PPT Skill, Presentation, Presentation Skill, Baoyu Xuanyi Skills, Slide Wright, Jiarui SVG Skills, Paper PPT Skill, Slidev Skills, Codex Image to Editable PPT, 30x McKinsey Research Deck, Claude Code Codex Slide, Slides AI Plugin, PPT Skill, HTML to PPT PDF, Scholar PPT CN, Beautiful Hackathon Slides, BL Captain PPT Skill, Image PPT King, ImageGen PPTX Pipeline, Narrative Engine, PPT Design DNA, PPTX Template Skills, PPT Creator Skills, Presentation Skill, Econ Empirical Paper PPT Skill, Beamer Skill, Jingge Sense Deck, Keynote Slides Skill, PPT Agent, Slide Design Skill, Claude HTML Slide Builder, AI Draw Skill, HTML to PPTX, Neon Slides, Create HTML Deck, GZR NSFC PPT Skill, Interactive Slides, MBB Decks, KAI Presentation, Four-Up PPT Generator, Keynot, Competition PPT Template Skill, NanoBanana PPT Skills, PPT Image Share Builder, Japanese Corporate PPTX Skill, CyberBin PPT Skill, PPT Skill, NanoBanana PPT Skills, Fudan University PPT Skill, HalfAI Gufa PPT, Better PPT HTML Deck, McKinsey HTML Design Skill, TalkTrack, AWS HTML Slides, Prada Slides, Editable Leadership PPTX, Paper Figure PPTX Skill, Competition PPT Skill, SlideStage Pack, Deckset Claude Skill, IML PPTX, HTML to PPTX Skill, SlideSmith, Guizang PPT Skill, Aham PPT, High Quality Slides, Bento PPT Skill, Presentation Chef, Paper to LaTeX PPT, SOIL Deck Skills, Hand-Drawn PPT Skill, HTML PPT Skill, HTML to PPTX, PPT Expert Team, Modern PPT, Presentation Forge, Notrat PPT Studio, USTC PPT Template, AI Editable PPT Skill, Vela Slides, Bruce PPTX Generator, Tekion Slide Generator, PPT Master, PPT Image to Editable, PPT Skills, Research Group PPT Skill, Paper to Scholar Slides, Xidian Slides Skill, Paper to Slides Skill, Editable PPTX Skill, Pitch Deck Iterator, Zhongguose PPT Skill, ZJ Lab Academic PPTX Skills, Consulting Diagnosis PPT Skill, Token Slides, Slide Weaver, PPT Template Fill, SlideSage, Web PPT, Codex XKPPT Skill, PPT Design Skill, PowerPoint Skill, HFUT Presentation Studio, SJTU Beamer PPT, Special Achievement Report, HTML PPT Academic Skill, Frontend Slides, Economics Empirical PPT Skill, HTML Report Generator, Demo Prep Skill, Avatar PPT Master, HTML PPT Video Skill, AI PPT Skill, SVG to PPTX Skill, Doc to PPT Skill, Ultimate PPT Master Skill, Anthropic PPTX (official), Baoyu Skills, AI Skills (Cross-Platform).</sub>

<sub>**81 images, all of them the projects' own**, two per skill out of the 485 the harvest keeps in [`data/samples.json`](data/samples.json). The two are chosen for content, not order: a slide with something on it over a title slide, the project's own README picks over stray assets, and two different styles where the project has them. Each was read from its repository at a pinned commit, credited in the caption under it, and served from that repository rather than copied here. Nothing was produced by running a skill, so treat it as what each team chose to show off — not as a like-for-like comparison. Regenerate with `python scripts/fetch_samples.py`.</sub>
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
  each one. <!-- BEGIN:RESEARCHED -->39<!-- END:RESEARCHED --> entries were read by hand,
  SKILL.md included; the rest carry a `†` and rest on what the repository says about itself.
  Where I have run something, the dossier says so.
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
