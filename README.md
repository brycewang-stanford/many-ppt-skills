<div align="center">

# many-ppt-skills

**值得知道的 AI 幻灯片 Skill 全在这一页，并排对比 —— 让你挑对一个，然后接着干活。**

[简体中文](README.md) · [English](README.en.md)

<!-- BEGIN:COUNTS -->
**收录 26 个 skill** · **合计 143,031 star** · HTML 路线 13 个 · PPTX 路线 7 个 · 双路线 4 个 · 数据刷新于 **2026-07-28**
<!-- END:COUNTS -->

</div>

---

Coding Agent 把 CSS 写好了，半年之内冒出一整个新品类：把文档变成不像机器做的幻灯片的
Skill。现在有 30+ 个认真做的项目，其中四个 star 数都超过 2 万。

而所有关于它们的排名，都只是 star 数的重新排序。**star 衡量的是作者会不会发推，不能告诉你
哪一个能处理好你的代码块，也不能告诉你财务总监能不能编辑第 12 页。**

这个仓库就是用一页纸回答这件事：

1. **全部收齐** —— 两条路线值得知道的 skill 都在，带实时数据。由
   [`data/skills.json`](data/skills.json) 自动生成，数字不会悄悄烂掉。
2. **按真正决定选择的点来对比** —— 先回答[路线问题](#从这里开始你走哪条路线)，再看每个到底
   适合干什么。都是你能自己核对的事实，不是我编的分数。
3. **[八条原则](principles/)** —— 从这些项目源码里提炼，30 个团队各自独立收敛到的同一批做法，
   这是这个领域目前最接近「证据」的东西。

挑一个、装上、继续干活。这就是全部意图。

---

## 让 agent 直接帮你挑

这个仓库本身也是一个 skill。装上之后，你不用自己翻这一页 —— 直接说「我要做一份给投资人的
deck」，它会先问路线问题，再给出具体的 skill、安装命令和风格 ID。

```bash
# 作为 Claude Code 插件
/plugin marketplace add https://github.com/brycewang-stanford/many-ppt-skills
/plugin install many-ppt-skills@many-ppt-skills

# 或者直接克隆成个人 skill
git clone https://github.com/brycewang-stanford/many-ppt-skills ~/.claude/skills/many-ppt-skills
```

背后是一个命令行查询层，你也可以自己用：

```bash
python scripts/pick.py route                  # 路线问题 + 各路线数量
python scripts/pick.py list --route pptx      # 某条路线下的 skill
python scripts/pick.py show ppt-master        # 安装命令、风格 ID、能力
python scripts/pick.py styles frontend-slides # 全部风格 ID 及对应样例图
python scripts/pick.py find editorial         # 搜风格 ID 和描述
```

**它只做选型，不生成 deck**，也不会替你编造别人项目的调用语法 —— 那以各项目自己的
`SKILL.md` 为准。详见 [`SKILL.md`](SKILL.md)。

---

## 从这里开始：你走哪条路线？

这是唯一真正重要的决策，而且它和审美无关。

> **有人需要用 PowerPoint 打开你的交付物并编辑它吗？**

| | **HTML 路线** | **原生 PPTX 路线** |
|---|---|---|
| **产出** | 单个 `.html`，浏览器放映 | 真正的 `.pptx` |
| **设计天花板** | ★★★★★ Chrome 能渲染的都行 | ★★★☆☆ 受 OOXML 限制 |
| **动效** | ★★★★★ CSS、WebGL | ★★☆☆☆ 原生转场 |
| **交接** | 对方无法用 Office 编辑 | 对方正常编辑 |
| **版本控制** | ★★★★★ 纯文本 diff | ★☆☆☆☆ 二进制 |
| **套企业模板** | ✗ | ✓ |
| **从这个开始** | [Frontend Slides](https://github.com/zarazhangrui/frontend-slides) | [PPT Master](https://github.com/hugohe3/ppt-master) |

**不需要 → 走 HTML。** 天花板高得多，而且不是一点点。零依赖单文件十年后照样能打开。
**需要 → 走 PPTX。** 如果财务总监改不了第 12 页，其他都白搭。

这不是新旧之争，是两种不同的活。

<details>
<summary><b>完整决策树</b></summary>

```
交付物需要对方用 PowerPoint 编辑吗？
├─ 需要 ──▶ 原生 PPTX
│   ├─ 要最好的视觉 + 真原生对象 ········ ppt-master
│   ├─ 必须严格套企业模板母版 ·········· pptx-from-layouts-skill
│   ├─ 对已有 deck 做程序化改造 ········ Anthropic pptx（官方）
│   ├─ 咨询 / 董事会 / 投资备忘录 ······· Mck-ppt-design-skill
│   └─ 会议报告 / 答辩 / 基金汇报 ······· academic-pptx-skill
│
└─ 不需要 ──▶ HTML 路线
    ├─ 不知道自己想要什么风格 ·········· frontend-slides
    ├─ 中文编辑风强一致性（注意 AGPL）·· guizang-ppt-skill
    ├─ 还要原型 / 动效 / 信息图 ········· huashu-design
    ├─ 团队长期做 deck，要演讲者模式 ···· open-slide
    ├─ 技术图解 / diff 评审 / 项目复盘 ·· visual-explainer
    ├─ 教学培训，在意知识留存 ·········· visual-cognition-slides
    └─ HTML 和可编辑 PPTX 都要 ········· huashu-design · frontend-slides-editable
```

</details>

### 如果只装一个

[**Frontend Slides**](https://github.com/zarazhangrui/frontend-slides)，作者
[Zara Zhang](https://github.com/zarazhangrui)。它定义了这个品类的交互范式 ——
**不问你想要什么风格，而是直接生成三个「你这份 deck」的真实预览让你指**。社区最大，遇到问题
最容易搜到答案。

再加 [**PPT Master**](https://github.com/hugohe3/ppt-master) 作为第二个，基本覆盖所有场景。

---

## 登记册

<!-- BEGIN:REGISTRY -->
### Tier S — 大规模验证（5k+ star）

| 项目 | ⭐ | 路线 | License | 一句话 |
|---|---:|---|---|---|
| **[PPT Master](https://github.com/hugohe3/ppt-master)**<br><sub>hugohe3</sub> | 41,516 | PPTX | MIT | 把文档或主题变成真正原生可编辑的 PPTX。 |
| **[Frontend Slides](https://github.com/zarazhangrui/frontend-slides)**<br><sub>Zara Zhang</sub> | 26,461 | HTML | MIT | 用 Coding Agent 的前端能力做好看的网页幻灯片。 |
| **[Guizang PPT Skill](https://github.com/op7418/guizang-ppt-skill)**<br><sub>op7418 (歸藏)</sub> | 22,564 | HTML | ⚠️ AGPL-3.0 | 杂志编辑风与瑞士国际风 HTML 幻灯片，以「锁死约束」保证一致性。 |
| **[Huashu Design](https://github.com/alchaincyf/huashu-design)**<br><sub>花生 (alchaincyf)</sub> | 22,135 | 双路线 | MIT | HTML 原生设计 skill —— 高保真原型、幻灯片、动效与设计评审，不止是 PPT。 |
| **[Visual Explainer](https://github.com/nicobailon/visual-explainer)**<br><sub>nicobailon</sub> | 9,346 | HTML | MIT | 为图表、diff 评审、方案审计、数据表和项目复盘生成 HTML 页面或幻灯片。 |
| **[HTML PPT Studio](https://github.com/lewislulu/html-ppt-skill)**<br><sub>lewislulu</sub> | 7,437 | HTML | MIT | 24 主题 × 31 布局 × 20+ 动效的专业 HTML 演示。 |
| **[open-slide](https://github.com/1weiho/open-slide)**<br><sub>1weiho</sub> | 6,027 | 框架 | MIT | 为 Agent 而生的幻灯片框架 —— React 组件渲染到固定 1920×1080 画布。 |
| **[Anthropic PPTX (official)](https://github.com/anthropics/skills/tree/main/skills/pptx)**<br><sub>Anthropic</sub> | 164,681* | PPTX | See repo | 官方基线方案 —— 创建、读取、编辑与合并 PowerPoint 文件。 |

### Tier A — 生产可用（100–5k star）

| 项目 | ⭐ | 路线 | License | 一句话 |
|---|---:|---|---|---|
| **[Beautiful HTML Templates](https://github.com/zarazhangrui/beautiful-html-templates)**<br><sub>Zara Zhang</sub> | 3,918 | 模板库 | MIT | 34 套 HTML 幻灯片模板，配 index.json 元数据供任意 Agent 检索选用。 |
| **[Claude Office Skills](https://github.com/tfriedel/claude-office-skills)**<br><sub>tfriedel</sub> | 798 | PPTX | Unspecified | PPTX / DOCX / XLSX / PDF 全家桶，支持自动化。 |
| **[Academic PPTX](https://github.com/Gabberflast/academic-pptx-skill)**<br><sub>Gabberflast</sub> | 722 | PPTX | MIT | 会议报告、研讨会、论文答辩与基金汇报。 |
| **[PPT Agent Workflow San](https://github.com/mucsbr/ppt-agent-workflow-san)**<br><sub>mucsbr</sub> | 617 | HTML | Unspecified | 渐进交互式 PPT 生成 skill。 |
| **[Frontend Slides Editable](https://github.com/archlizheng/frontend-slides-editable)**<br><sub>archlizheng</sub> | 445 | 双路线 | MIT | 可编辑 HTML 幻灯片：拖拽缩放、页序调整、本地保存、PPTX 互转。 |
| **[PPT SVG Generator](https://github.com/vigorX777/ppt-svg-generator)**<br><sub>vigorX777</sub> | 248 | PPTX | MIT | Markdown → PPT / PDF，经 SVG 中转，多种预设风格。 |
| **[Mck PPT Design System](https://github.com/likaku/Mck-ppt-design-skill)**<br><sub>likaku</sub> | 229 | PPTX | Apache-2.0 | 咨询公司风设计系统：70 种布局，扁平设计，python-pptx。 |
| **[PPT Agent Skill](https://github.com/Akxan/ppt-agent-skill)**<br><sub>Akxan</sub> | 114 | HTML | MIT | 26 种风格、18 种图表，对标 Linear / Anthropic / Stripe / Apple / NYT。 |

### Tier B — 垂直与新兴（<100 star）

| 项目 | ⭐ | 路线 | License | 一句话 |
|---|---:|---|---|---|
| **[Visual Cognition Slides](https://github.com/edu-ai-builders/visual-cognition-slides)**<br><sub>edu-ai-builders</sub> | 81 | HTML | MIT | 基于认知科学与教学设计的幻灯片，优化知识留存率。 |
| **[HTML Slides](https://github.com/bluedusk/html-slides)**<br><sub>bluedusk</sub> | 70 | HTML | MIT | 带演讲者备注的 HTML 幻灯片，配套放映 app。 |
| **[KingDee PPT Skill](https://github.com/WayneZhon/KingDee-PPT-Skill)**<br><sub>WayneZhon</sub> | 56 | HTML | MIT | 将内容快速生成金蝶风格 PPT。 |
| **[Huawei Style PPT Skill](https://github.com/zuiho-kai/huawei-style-ppt-skill)**<br><sub>zuiho-kai</sub> | 52 | HTML | Custom | 华为风格高密度信息 PPT 制作工作流。 |
| **[Slide Creator](https://github.com/kaisersong/slide-creator)**<br><sub>kaisersong</sub> | 46 | 双路线 | Unspecified | AI 规划 + 风格发现 + PPTX 导出。 |
| **[next-slide](https://github.com/codesstar/next-slide)**<br><sub>codesstar</sub> | 43 | HTML | MIT | 「你的下个 slide，何必是 PPT」—— 26+ 风格，零依赖，中英双语。 |
| **[Slide Writer](https://github.com/FeeiCN/slide-writer)**<br><sub>FeeiCN</sub> | 40 | HTML | MIT | 从想法、大纲、文档或演讲稿生成企业级 HTML 演示。 |
| **[Skills Slides](https://github.com/nghiahsgs/skills-slides)**<br><sub>nghiahsgs</sub> | 30 | HTML | Unspecified | 50 美学 × 20 配色 × 10 字体 × 5 布局 × 30+ 特效 = 5 万种组合。 |
| **[PowerPoint Fancy Design](https://github.com/Phlegonlabs/Powerpoint-fancy-design)**<br><sub>Phlegonlabs</sub> | 27 | 双路线 | Unspecified | 结构化 Markdown → 1600×900 HTML 幻灯片 + PNG 渲染 + 可导出。 |
| **[PPTX from Layouts](https://github.com/tristan-mcinnis/pptx-from-layouts-skill)**<br><sub>tristan-mcinnis</sub> | 9 | PPTX | MIT | 严格通过模板母版版式，从 Markdown 生成 PPTX。 |

### 其他精选列表

| 项目 | ⭐ | 路线 | License | 一句话 |
|---|---:|---|---|---|
| **[awesome-html-slide-skills](https://github.com/ToseaAI/awesome-html-slide-skills)**<br><sub>ToseaAI</sub> | 104 | 列表 | Custom | HTML 演示 Skill 与模板库精选列表。本仓库的主要线索来源之一。 |
| **[Awesome-PPT-Design-Skills](https://github.com/software-ai-life/Awesome-PPT-Design-Skills)**<br><sub>software-ai-life</sub> | 71 | 列表 | Unspecified | Agent 无关的高端可编辑 PPT 风格集。 |

<sub>`*` monorepo star 数，反映整个仓库而非这一个 skill。`~` 上次刷新失败，为陈旧值。`⚠️` copyleft 协议，商用前请确认。</sub>
<!-- END:REGISTRY -->
---

## 每个到底能做什么

上面的登记册说的是每个项目**是什么**，这里说的是它的文档**声称它能做什么** —— 也就是通常
真正决定选择的那几列。

<!-- BEGIN:CAPABILITIES -->
| 项目 | → PPTX | → PDF | 数据图表 | 代码高亮 | 图示 | 动效 | 演讲备注 | 演讲者模式 | 自定义模板 | 离线可用 |
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

<sub>✅ 文档声明支持 · — 文档明确说明不支持 · · 文档未提及，这不等于不支持 · n/a 该问题对这条路线不适用。全部读自各项目自己的 SKILL.md 与 README，不是实跑验证；每个 ✅ 的出处引文都在 [`data/capabilities.json`](data/capabilities.json)。</sub>
<!-- END:CAPABILITIES -->

中间那个值要看仔细：`·` 表示文档从未提及，**这不等于「不支持」**。这些项目里有好几个做的比
写下来的多。如果某项能力对你重要，[`data/capabilities.json`](data/capabilities.json) 里的
引文会告诉你该去核对哪一句话。


---

## 它们长什么样

上面两张表说的是每个项目**是什么**、**声称能做什么**。但都没回答你真正的问题：
**你喜不喜欢它出的东西。** 所以这里把这些项目自己公开的成品图，能收的都收进来了。

**全部按原尺寸铺开，不做缩略图。** 幻灯片是高密度的东西，缩成一排小图只能看出配色，
看不出字体、层次和留白 —— 而要挑的恰恰是后面这些。页面因此很长，用下面的目录直接跳。

风格名和说明全部**读自项目自己的文件名与图注**，不是本仓库起的。每张图下面都标着出处路径
并链回原文件，所以标错了也是看得出来的。

请按它的本来面目看：**每一张都是各团队自己挑的那一帧**。一堆宣传图不是同题横评 ——
这些 deck 甚至不是同一份内容，谁也没跑过谁的题。它真正的用处在别处：三十秒之内砍掉
一半候选，而这恰恰是大多数人来这一页要做的事。

### 看中一张图，怎么做出来

**一、记下图下面那两样东西。** 每张图的说明行长这样：

> **Soft Editorial · 4** · `soft-editorial` · [`screenshots/soft-editorial-4.png`](https://github.com/zarazhangrui/beautiful-html-templates)

粗体是人话名字，`等宽` 的那个是**风格 ID** —— 这是你等下要点名的字符串。最后是出处文件，
点进去能看到原件。

**二、装它所属的 skill。** 命令就在这一节每个 skill 的标题下面，直接复制。
但**五种安装方式的含义不一样**，别装错地方：

<!-- BEGIN:INSTALLMETHODS -->
| 安装方式 | 实际发生了什么 | 数量 |
|---|---|---:|
| `clone` | 克隆进 `~/.claude/skills/`，也就是 Claude Code 找个人 skill 的地方。重开一个会话就能用。 | 20 |
| `plugin` | 两条命令是在 **Claude Code 里面**敲的，不是终端。先加 marketplace，再从里面装。 | 2 |
| `skills-cli` | 跨 agent 的安装器，不止 Claude Code 能用。 | 2 |
| `python` | 需要本机有 Python。克隆下来、装依赖，然后让 agent 在这个目录里干活。 | 1 |
| `npx` | 它是**建项目**，不是装 skill —— 跑完你得到一个可以直接开工的目录。 | 1 |
<!-- END:INSTALLMETHODS -->

**三、跟 agent 说人话，并点名风格 ID。** 风格名不是命令行参数，是给 agent 的指令内容：

```text
用 soft-editorial 这个模板，把 docs/roadmap.md 做成一份 12 页的 deck，
面向投资人，讲的时候我会展开，所以每页字少一点。
```

**四、知道你在跳过什么。** 有些 skill 默认会先生成几个预览让你挑 —— 比如 frontend-slides
的 SKILL.md 写着默认生成 3 个预览（1 个稳妥预设 + 1 个 bold 模板 + 1 个 wildcard）。
**你直接点名模板 ID，就是跳过这一步**，它会去读那个模板的 `design.md` 然后照着做。
想让它给你几个选项，就别点名，直接说「帮我做一份关于 X 的 deck」。

> **两点实话。** 安装命令来自人工维护的 [`data/skills.json`](data/skills.json)，风格 ID 来自
> 项目自己的文件 —— 我核对过 `soft-editorial` 等确实是 frontend-slides 自带
> `bold-template-pack/selection-index.json` 里的 slug（共 34 个）。但**本仓库没有实跑过
> 这 26 个 skill 的调用**，各项目的具体触发词和参数以它自己的 SKILL.md 为准。
> 第四步那句关于预览的描述，是从 frontend-slides 的 SKILL.md 里读到的，只对它成立。

<!-- BEGIN:GALLERY -->
**跳到：**[PPT Master](#gallery-ppt-master) <sub>24</sub> · [Frontend Slides](#gallery-frontend-slides) <sub>24</sub> · [Guizang PPT Skill](#gallery-guizang-ppt-skill) <sub>13</sub> · [Huashu Design](#gallery-huashu-design) <sub>24</sub> · [HTML PPT Studio](#gallery-html-ppt-skill) <sub>24</sub> · [open-slide](#gallery-open-slide) <sub>16</sub> · [Beautiful HTML Templates](#gallery-beautiful-html-templates) <sub>24</sub> · [PPT Agent Workflow San](#gallery-ppt-agent-workflow-san) <sub>10</sub> · [Frontend Slides Editable](#gallery-frontend-slides-editable) <sub>24</sub> · [PPT SVG Generator](#gallery-ppt-svg-generator) <sub>2</sub> · [Mck PPT Design System](#gallery-mck-ppt-design-skill) <sub>6</sub> · [PPT Agent Skill](#gallery-ppt-agent-skill) <sub>24</sub> · [HTML Slides](#gallery-html-slides-bluedusk) <sub>4</sub> · [KingDee PPT Skill](#gallery-kingdee-ppt-skill) <sub>1</sub> · [Slide Creator](#gallery-slide-creator) <sub>23</sub> · [next-slide](#gallery-next-slide) <sub>1</sub> · [Slide Writer](#gallery-slide-writer) <sub>5</sub> · [Skills Slides](#gallery-skills-slides) <sub>4</sub> · [PowerPoint Fancy Design](#gallery-powerpoint-fancy-design) <sub>24</sub> · [PPTX from Layouts](#gallery-pptx-from-layouts) <sub>1</sub>

<a id="gallery-ppt-master"></a>

#### [PPT Master](https://github.com/hugohe3/ppt-master) · 41,516 ⭐ · PPTX

<sub>把文档或主题变成真正原生可编辑的 PPTX。</sub>

<sub>取自 [`hugohe3/ppt-master`](https://github.com/hugohe3/ppt-master) 的 46 张图，此处 24 张，靠前的几张是项目自己放在 README 里的</sub>

```bash
git clone https://github.com/hugohe3/ppt-master && pip install -r requirements.txt
```

<sub><b>下面出现的风格</b> `global-ai-capital` · `swiss-grid` · `glassmorphism-demo` · `sugar-rush-memphis` · `indie-bookstore-zine` · `pritzker-2026` · `academic-medical` · `dark-art-mv` · `launch-xiaomi` · `magazine-garden` · `nature-wildlife` · `tech-claude-plans` —— 要哪个就在提示里点名。这些是<b>项目自己用的字符串</b>，取自每张图下面链接的文件名与说明，不是本仓库起的名字。</sub>

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

<sub>用 Coding Agent 的前端能力做好看的网页幻灯片。</sub>

<sub>取自 [`zarazhangrui/frontend-slides`](https://github.com/zarazhangrui/frontend-slides) 的 102 张图，此处 24 张，靠前的几张是项目自己放在 README 里的</sub>

```bash
/plugin marketplace add https://github.com/zarazhangrui/frontend-slides
/plugin install frontend-slides@frontend-slides
```

<sub><b>下面出现的风格</b> `soft-editorial` · `editorial-forest` · `pin-and-paper` · `sakura-chroma` · `stencil-tablet` · `cobalt-grid` · `vellum` · `emerald-editorial` —— 要哪个就在提示里点名。这些是<b>项目自己用的字符串</b>，取自每张图下面链接的文件名与说明，不是本仓库起的名字。</sub>

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

<sub>杂志编辑风与瑞士国际风 HTML 幻灯片，以「锁死约束」保证一致性。</sub>

<sub>取自 [`op7418/guizang-ppt-skill`](https://github.com/op7418/guizang-ppt-skill) 的 13 张图，此处 13 张，靠前的几张是项目自己放在 README 里的</sub>

```bash
npx skills add https://github.com/op7418/guizang-ppt-skill --skill guizang-ppt-skill
```

<sub><b>下面出现的风格</b> `ppt-skill-showcase` —— 要哪个就在提示里点名。这些是<b>项目自己用的字符串</b>，取自每张图下面链接的文件名与说明，不是本仓库起的名字。</sub>

<img src="https://github.com/user-attachments/assets/5dc316a2-401c-4e37-9123-ea081b6ae470" width="100%" alt="Style A 电子杂志风效果展示">

<sub><b>Style A 电子杂志风效果展示</b> · GitHub 附件图</sub>

<img src="https://github.com/user-attachments/assets/8960e78c-69bb-4b7e-aa95-6fad64b70314" width="100%" alt="Style B 瑞士国际主义效果展示">

<sub><b>Style B 瑞士国际主义效果展示</b> · GitHub 附件图</sub>

<img src="https://github.com/user-attachments/assets/df21dbcb-5fe4-4852-a91a-a9cf00aceeb4" width="100%" alt="墨水经典主题预览">

<sub><b>墨水经典主题预览</b> · GitHub 附件图</sub>

<img src="https://github.com/user-attachments/assets/99ce0fd2-72a6-4368-a75a-a8e21657a537" width="100%" alt="靛蓝瓷主题预览">

<sub><b>靛蓝瓷主题预览</b> · GitHub 附件图</sub>

<img src="https://github.com/user-attachments/assets/bcc1cc4c-5e8e-4467-ae8d-f5801ae73657" width="100%" alt="森林墨主题预览">

<sub><b>森林墨主题预览</b> · GitHub 附件图</sub>

<img src="https://github.com/user-attachments/assets/dfea080e-e916-417e-93cd-0a3628de84ca" width="100%" alt="牛皮纸主题预览">

<sub><b>牛皮纸主题预览</b> · GitHub 附件图</sub>

<img src="https://github.com/user-attachments/assets/f3705592-9a72-4dbc-9818-df3aea61bc75" width="100%" alt="沙丘主题预览">

<sub><b>沙丘主题预览</b> · GitHub 附件图</sub>

<img src="https://github.com/user-attachments/assets/c02d02f7-ce6f-4e16-b8a6-778c96851f94" width="100%" alt="克莱因蓝瑞士主题预览">

<sub><b>克莱因蓝瑞士主题预览</b> · GitHub 附件图</sub>

<img src="https://github.com/user-attachments/assets/c310a8c4-5d28-450e-b49a-6ac5b6ba4785" width="100%" alt="柠檬黄瑞士主题预览">

<sub><b>柠檬黄瑞士主题预览</b> · GitHub 附件图</sub>

<img src="https://github.com/user-attachments/assets/65f7b3f9-3358-419e-b513-f7f2cc24ec76" width="100%" alt="柠檬绿瑞士主题预览">

<sub><b>柠檬绿瑞士主题预览</b> · GitHub 附件图</sub>

<img src="https://github.com/user-attachments/assets/9c3319c9-a134-4657-9a56-211c23411f7f" width="100%" alt="安全橙瑞士主题预览">

<sub><b>安全橙瑞士主题预览</b> · GitHub 附件图</sub>

<img src="https://github.com/user-attachments/assets/81138fad-31b9-49ab-8e38-23b2bc48edc4" width="100%" alt="360 安全龙虾 / Kimi work / Cola Skill 金牌赞助">

<sub><b>360 安全龙虾 / Kimi work / Cola Skill 金牌赞助</b> · GitHub 附件图</sub>

<img src="https://raw.githubusercontent.com/op7418/guizang-ppt-skill/929c2ecb63a22b54d400c4911ed70bf96c2b355d/assets/ppt-skill-showcase.png" width="100%" alt="Guizang PPT Skill sample">

<sub><b>Ppt Skill Showcase</b> · <a href="https://github.com/op7418/guizang-ppt-skill/blob/929c2ecb63a22b54d400c4911ed70bf96c2b355d/assets/ppt-skill-showcase.png"><code>assets/ppt-skill-showcase.png</code></a></sub>

<a id="gallery-huashu-design"></a>

#### [Huashu Design](https://github.com/alchaincyf/huashu-design) · 22,135 ⭐ · 双路线

<sub>HTML 原生设计 skill —— 高保真原型、幻灯片、动效与设计评审，不止是 PPT。</sub>

<sub>取自 [`alchaincyf/huashu-design`](https://github.com/alchaincyf/huashu-design) 的 24 张图，此处 24 张</sub>

```bash
npx skills add alchaincyf/huashu-design
```

<sub><b>下面出现的风格</b> `ppt-build` · `ppt-pentagram` · `ppt-takram` · `ainav-build` · `ainav-pentagram` · `ainav-takram` · `aiwriting-build` · `aiwriting-pentagram` · `aiwriting-takram` · `devdocs-build` · `devdocs-pentagram` · `devdocs-takram` —— 要哪个就在提示里点名。这些是<b>项目自己用的字符串</b>，取自每张图下面链接的文件名与说明，不是本仓库起的名字。</sub>

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

<sub>24 主题 × 31 布局 × 20+ 动效的专业 HTML 演示。</sub>

<sub>取自 [`lewislulu/html-ppt-skill`](https://github.com/lewislulu/html-ppt-skill) 的 63 张图，此处 24 张，靠前的几张是项目自己放在 README 里的</sub>

```bash
git clone https://github.com/lewislulu/html-ppt-skill ~/.claude/skills/html-ppt-skill
```

<sub><b>下面出现的风格</b> `themes` · `templates` · `layouts` · `layouts-live` · `hero` · `presenter-mode` · `animations` · `animation-showcase` —— 要哪个就在提示里点名。这些是<b>项目自己用的字符串</b>，取自每张图下面链接的文件名与说明，不是本仓库起的名字。</sub>

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

#### [open-slide](https://github.com/1weiho/open-slide) · 6,027 ⭐ · 框架

<sub>为 Agent 而生的幻灯片框架 —— React 组件渲染到固定 1920×1080 画布。</sub>

<sub>取自 [`1weiho/open-slide`](https://github.com/1weiho/open-slide) 的 16 张图，此处 16 张，靠前的几张是项目自己放在 README 里的</sub>

```bash
npx @open-slide/cli init my-slide
```

<sub><b>下面出现的风格</b> `replit-features-result` · `create-slide-skill` · `openslide-home` · `replit-agent-home` · `assets-manager` · `inspector` · `presenter` · `theme` · `svgl` · `open-slide` · `replit-deploy` · `init-command` —— 要哪个就在提示里点名。这些是<b>项目自己用的字符串</b>，取自每张图下面链接的文件名与说明，不是本仓库起的名字。</sub>

<img src="https://github.com/user-attachments/assets/02f5e6d7-12a7-4a8e-88e7-ae8770a96584" width="100%" alt="open-slide github cover">

<sub><b>open-slide github cover</b> · GitHub 附件图</sub>

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

<sub><b>Open Slide</b> · 封面 · <a href="https://github.com/1weiho/open-slide/blob/35dc46ca27716ea86f8a76710bbd3640e9590628/apps/web/public/assets/screenshots/open-slide-cover.webp"><code>apps/web/public/assets/screenshots/open-slide-cover.webp</code></a></sub>

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

#### [Beautiful HTML Templates](https://github.com/zarazhangrui/beautiful-html-templates) · 3,918 ⭐ · 模板库

<sub>34 套 HTML 幻灯片模板，配 index.json 元数据供任意 Agent 检索选用。</sub>

<sub>取自 [`zarazhangrui/beautiful-html-templates`](https://github.com/zarazhangrui/beautiful-html-templates) 的 102 张图，此处 24 张，靠前的几张是项目自己放在 README 里的</sub>

```bash
git clone https://github.com/zarazhangrui/beautiful-html-templates
```

<sub><b>下面出现的风格</b> `soft-editorial` · `editorial-forest` · `pin-and-paper` · `sakura-chroma` · `stencil-tablet` · `cobalt-grid` · `vellum` · `emerald-editorial` —— 要哪个就在提示里点名。这些是<b>项目自己用的字符串</b>，取自每张图下面链接的文件名与说明，不是本仓库起的名字。</sub>

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

<sub>渐进交互式 PPT 生成 skill。</sub>

<sub>取自 [`mucsbr/ppt-agent-workflow-san`](https://github.com/mucsbr/ppt-agent-workflow-san) 的 10 张图，此处 10 张，靠前的几张是项目自己放在 README 里的</sub>

```bash
git clone https://github.com/mucsbr/ppt-agent-workflow-san
```

<sub><b>下面出现的风格</b> `html-slide-to-pptx-preview` · `ppt-workflow-preview` · `ppt-workflow` · `02-core-conclusion` · `03-positioning` · `04-users-scenarios` · `05-growth-flywheel` · `06-competition` · `07-risks` · `08-conclusion` —— 要哪个就在提示里点名。这些是<b>项目自己用的字符串</b>，取自每张图下面链接的文件名与说明，不是本仓库起的名字。</sub>

<img src="https://raw.githubusercontent.com/mucsbr/ppt-agent-workflow-san/801cd2bd46c3cc4ca2c846ff28da2d9284816cd9/2.png" width="100%" alt="html-slide-to-pptx-preview">

<sub><b>html-slide-to-pptx-preview</b> · <a href="https://github.com/mucsbr/ppt-agent-workflow-san/blob/801cd2bd46c3cc4ca2c846ff28da2d9284816cd9/2.png"><code>2.png</code></a></sub>

<img src="https://raw.githubusercontent.com/mucsbr/ppt-agent-workflow-san/801cd2bd46c3cc4ca2c846ff28da2d9284816cd9/1.png" width="100%" alt="ppt-workflow-preview">

<sub><b>ppt-workflow-preview</b> · <a href="https://github.com/mucsbr/ppt-agent-workflow-san/blob/801cd2bd46c3cc4ca2c846ff28da2d9284816cd9/1.png"><code>1.png</code></a></sub>

<img src="https://raw.githubusercontent.com/mucsbr/ppt-agent-workflow-san/801cd2bd46c3cc4ca2c846ff28da2d9284816cd9/ppt-workflow/01-cover.png" width="100%" alt="PPT Agent Workflow San sample">

<sub><b>Ppt Workflow</b> · 封面 · <a href="https://github.com/mucsbr/ppt-agent-workflow-san/blob/801cd2bd46c3cc4ca2c846ff28da2d9284816cd9/ppt-workflow/01-cover.png"><code>ppt-workflow/01-cover.png</code></a></sub>

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

#### [Frontend Slides Editable](https://github.com/archlizheng/frontend-slides-editable) · 445 ⭐ · 双路线

<sub>可编辑 HTML 幻灯片：拖拽缩放、页序调整、本地保存、PPTX 互转。</sub>

<sub>取自 [`archlizheng/frontend-slides-editable`](https://github.com/archlizheng/frontend-slides-editable) 的 114 张图，此处 24 张，靠前的几张是项目自己放在 README 里的</sub>

```bash
git clone https://github.com/archlizheng/frontend-slides-editable
```

<sub><b>下面出现的风格</b> `cobalt-grid` · `studio-volt` · `soft-editorial` · `bold-signal` · `electric-studio` · `creative-voltage` · `dark-botanical` · `notebook-tabs` · `pastel-geometry` · `split-pastel` · `vintage-editorial` · `neon-cyber` —— 要哪个就在提示里点名。这些是<b>项目自己用的字符串</b>，取自每张图下面链接的文件名与说明，不是本仓库起的名字。</sub>

<img src="https://raw.githubusercontent.com/archlizheng/frontend-slides-editable/e5663e6a0bdc2c2a673198bab3fb61036a7f20ee/docs/preset-previews/cobalt-grid-cover.png" width="100%" alt="Cobalt Grid editable deck preview">

<sub><b>Cobalt Grid editable deck preview</b> · 封面 · <a href="https://github.com/archlizheng/frontend-slides-editable/blob/e5663e6a0bdc2c2a673198bab3fb61036a7f20ee/docs/preset-previews/cobalt-grid-cover.png"><code>docs/preset-previews/cobalt-grid-cover.png</code></a></sub>

<img src="https://raw.githubusercontent.com/archlizheng/frontend-slides-editable/e5663e6a0bdc2c2a673198bab3fb61036a7f20ee/docs/preset-previews/studio-volt-cover.png" width="100%" alt="Studio editable deck preview">

<sub><b>Studio editable deck preview</b> · <code>studio-volt</code> · 封面 · <a href="https://github.com/archlizheng/frontend-slides-editable/blob/e5663e6a0bdc2c2a673198bab3fb61036a7f20ee/docs/preset-previews/studio-volt-cover.png"><code>docs/preset-previews/studio-volt-cover.png</code></a></sub>

<img src="https://raw.githubusercontent.com/archlizheng/frontend-slides-editable/e5663e6a0bdc2c2a673198bab3fb61036a7f20ee/docs/preset-previews/soft-editorial-cover.png" width="100%" alt="Soft Editorial editable deck preview">

<sub><b>Soft Editorial editable deck preview</b> · 封面 · <a href="https://github.com/archlizheng/frontend-slides-editable/blob/e5663e6a0bdc2c2a673198bab3fb61036a7f20ee/docs/preset-previews/soft-editorial-cover.png"><code>docs/preset-previews/soft-editorial-cover.png</code></a></sub>

<img src="https://raw.githubusercontent.com/archlizheng/frontend-slides-editable/e5663e6a0bdc2c2a673198bab3fb61036a7f20ee/docs/preset-previews/bold-signal-cover.png" width="100%" alt="Bold Signal — first slide">

<sub><b>Bold Signal — first slide</b> · 封面 · <a href="https://github.com/archlizheng/frontend-slides-editable/blob/e5663e6a0bdc2c2a673198bab3fb61036a7f20ee/docs/preset-previews/bold-signal-cover.png"><code>docs/preset-previews/bold-signal-cover.png</code></a></sub>

<img src="https://raw.githubusercontent.com/archlizheng/frontend-slides-editable/e5663e6a0bdc2c2a673198bab3fb61036a7f20ee/docs/preset-previews/electric-studio-cover.png" width="100%" alt="Electric Studio — first slide">

<sub><b>Electric Studio — first slide</b> · 封面 · <a href="https://github.com/archlizheng/frontend-slides-editable/blob/e5663e6a0bdc2c2a673198bab3fb61036a7f20ee/docs/preset-previews/electric-studio-cover.png"><code>docs/preset-previews/electric-studio-cover.png</code></a></sub>

<img src="https://raw.githubusercontent.com/archlizheng/frontend-slides-editable/e5663e6a0bdc2c2a673198bab3fb61036a7f20ee/docs/preset-previews/creative-voltage-cover.png" width="100%" alt="Creative Voltage — first slide">

<sub><b>Creative Voltage — first slide</b> · 封面 · <a href="https://github.com/archlizheng/frontend-slides-editable/blob/e5663e6a0bdc2c2a673198bab3fb61036a7f20ee/docs/preset-previews/creative-voltage-cover.png"><code>docs/preset-previews/creative-voltage-cover.png</code></a></sub>

<img src="https://raw.githubusercontent.com/archlizheng/frontend-slides-editable/e5663e6a0bdc2c2a673198bab3fb61036a7f20ee/docs/preset-previews/dark-botanical-cover.png" width="100%" alt="Dark Botanical — first slide">

<sub><b>Dark Botanical — first slide</b> · 封面 · <a href="https://github.com/archlizheng/frontend-slides-editable/blob/e5663e6a0bdc2c2a673198bab3fb61036a7f20ee/docs/preset-previews/dark-botanical-cover.png"><code>docs/preset-previews/dark-botanical-cover.png</code></a></sub>

<img src="https://raw.githubusercontent.com/archlizheng/frontend-slides-editable/e5663e6a0bdc2c2a673198bab3fb61036a7f20ee/docs/preset-previews/notebook-tabs-cover.png" width="100%" alt="Notebook Tabs — first slide">

<sub><b>Notebook Tabs — first slide</b> · 封面 · <a href="https://github.com/archlizheng/frontend-slides-editable/blob/e5663e6a0bdc2c2a673198bab3fb61036a7f20ee/docs/preset-previews/notebook-tabs-cover.png"><code>docs/preset-previews/notebook-tabs-cover.png</code></a></sub>

<img src="https://raw.githubusercontent.com/archlizheng/frontend-slides-editable/e5663e6a0bdc2c2a673198bab3fb61036a7f20ee/docs/preset-previews/pastel-geometry-cover.png" width="100%" alt="Pastel Geometry — first slide">

<sub><b>Pastel Geometry — first slide</b> · 封面 · <a href="https://github.com/archlizheng/frontend-slides-editable/blob/e5663e6a0bdc2c2a673198bab3fb61036a7f20ee/docs/preset-previews/pastel-geometry-cover.png"><code>docs/preset-previews/pastel-geometry-cover.png</code></a></sub>

<img src="https://raw.githubusercontent.com/archlizheng/frontend-slides-editable/e5663e6a0bdc2c2a673198bab3fb61036a7f20ee/docs/preset-previews/split-pastel-cover.png" width="100%" alt="Split Pastel — first slide">

<sub><b>Split Pastel — first slide</b> · 封面 · <a href="https://github.com/archlizheng/frontend-slides-editable/blob/e5663e6a0bdc2c2a673198bab3fb61036a7f20ee/docs/preset-previews/split-pastel-cover.png"><code>docs/preset-previews/split-pastel-cover.png</code></a></sub>

<img src="https://raw.githubusercontent.com/archlizheng/frontend-slides-editable/e5663e6a0bdc2c2a673198bab3fb61036a7f20ee/docs/preset-previews/vintage-editorial-cover.png" width="100%" alt="Vintage Editorial — first slide">

<sub><b>Vintage Editorial — first slide</b> · 封面 · <a href="https://github.com/archlizheng/frontend-slides-editable/blob/e5663e6a0bdc2c2a673198bab3fb61036a7f20ee/docs/preset-previews/vintage-editorial-cover.png"><code>docs/preset-previews/vintage-editorial-cover.png</code></a></sub>

<img src="https://raw.githubusercontent.com/archlizheng/frontend-slides-editable/e5663e6a0bdc2c2a673198bab3fb61036a7f20ee/docs/preset-previews/neon-cyber-cover.png" width="100%" alt="Neon Cyber — first slide">

<sub><b>Neon Cyber — first slide</b> · 封面 · <a href="https://github.com/archlizheng/frontend-slides-editable/blob/e5663e6a0bdc2c2a673198bab3fb61036a7f20ee/docs/preset-previews/neon-cyber-cover.png"><code>docs/preset-previews/neon-cyber-cover.png</code></a></sub>

<img src="https://raw.githubusercontent.com/archlizheng/frontend-slides-editable/e5663e6a0bdc2c2a673198bab3fb61036a7f20ee/docs/preset-previews/terminal-green-cover.png" width="100%" alt="Terminal Green — first slide">

<sub><b>Terminal Green — first slide</b> · 封面 · <a href="https://github.com/archlizheng/frontend-slides-editable/blob/e5663e6a0bdc2c2a673198bab3fb61036a7f20ee/docs/preset-previews/terminal-green-cover.png"><code>docs/preset-previews/terminal-green-cover.png</code></a></sub>

<img src="https://raw.githubusercontent.com/archlizheng/frontend-slides-editable/e5663e6a0bdc2c2a673198bab3fb61036a7f20ee/docs/preset-previews/swiss-modern-cover.png" width="100%" alt="Swiss Modern — first slide">

<sub><b>Swiss Modern — first slide</b> · 封面 · <a href="https://github.com/archlizheng/frontend-slides-editable/blob/e5663e6a0bdc2c2a673198bab3fb61036a7f20ee/docs/preset-previews/swiss-modern-cover.png"><code>docs/preset-previews/swiss-modern-cover.png</code></a></sub>

<img src="https://raw.githubusercontent.com/archlizheng/frontend-slides-editable/e5663e6a0bdc2c2a673198bab3fb61036a7f20ee/docs/preset-previews/paper-ink-cover.png" width="100%" alt="Paper and Ink — first slide">

<sub><b>Paper and Ink — first slide</b> · <code>paper-ink</code> · 封面 · <a href="https://github.com/archlizheng/frontend-slides-editable/blob/e5663e6a0bdc2c2a673198bab3fb61036a7f20ee/docs/preset-previews/paper-ink-cover.png"><code>docs/preset-previews/paper-ink-cover.png</code></a></sub>

<img src="https://raw.githubusercontent.com/archlizheng/frontend-slides-editable/e5663e6a0bdc2c2a673198bab3fb61036a7f20ee/docs/preset-previews/8-bit-orbit-cover.png" width="100%" alt="8-Bit Orbit — cover slide">

<sub><b>8-Bit Orbit — cover slide</b> · 封面 · <a href="https://github.com/archlizheng/frontend-slides-editable/blob/e5663e6a0bdc2c2a673198bab3fb61036a7f20ee/docs/preset-previews/8-bit-orbit-cover.png"><code>docs/preset-previews/8-bit-orbit-cover.png</code></a></sub>

<img src="https://raw.githubusercontent.com/archlizheng/frontend-slides-editable/e5663e6a0bdc2c2a673198bab3fb61036a7f20ee/docs/preset-previews/8-bit-orbit-mid.png" width="100%" alt="8-Bit Orbit — mid slide">

<sub><b>8-Bit Orbit — mid slide</b> · <code>8-bit-orbit-mid</code> · <a href="https://github.com/archlizheng/frontend-slides-editable/blob/e5663e6a0bdc2c2a673198bab3fb61036a7f20ee/docs/preset-previews/8-bit-orbit-mid.png"><code>docs/preset-previews/8-bit-orbit-mid.png</code></a></sub>

<img src="https://raw.githubusercontent.com/archlizheng/frontend-slides-editable/e5663e6a0bdc2c2a673198bab3fb61036a7f20ee/docs/preset-previews/8-bit-orbit-later.png" width="100%" alt="8-Bit Orbit — later slide">

<sub><b>8-Bit Orbit — later slide</b> · <code>8-bit-orbit-later</code> · <a href="https://github.com/archlizheng/frontend-slides-editable/blob/e5663e6a0bdc2c2a673198bab3fb61036a7f20ee/docs/preset-previews/8-bit-orbit-later.png"><code>docs/preset-previews/8-bit-orbit-later.png</code></a></sub>

<img src="https://raw.githubusercontent.com/archlizheng/frontend-slides-editable/e5663e6a0bdc2c2a673198bab3fb61036a7f20ee/docs/preset-previews/biennale-yellow-cover.png" width="100%" alt="Biennale Yellow — cover slide">

<sub><b>Biennale Yellow — cover slide</b> · 封面 · <a href="https://github.com/archlizheng/frontend-slides-editable/blob/e5663e6a0bdc2c2a673198bab3fb61036a7f20ee/docs/preset-previews/biennale-yellow-cover.png"><code>docs/preset-previews/biennale-yellow-cover.png</code></a></sub>

<img src="https://raw.githubusercontent.com/archlizheng/frontend-slides-editable/e5663e6a0bdc2c2a673198bab3fb61036a7f20ee/docs/preset-previews/biennale-yellow-mid.png" width="100%" alt="Biennale Yellow — mid slide">

<sub><b>Biennale Yellow — mid slide</b> · <code>biennale-yellow-mid</code> · <a href="https://github.com/archlizheng/frontend-slides-editable/blob/e5663e6a0bdc2c2a673198bab3fb61036a7f20ee/docs/preset-previews/biennale-yellow-mid.png"><code>docs/preset-previews/biennale-yellow-mid.png</code></a></sub>

<img src="https://raw.githubusercontent.com/archlizheng/frontend-slides-editable/e5663e6a0bdc2c2a673198bab3fb61036a7f20ee/docs/preset-previews/biennale-yellow-later.png" width="100%" alt="Biennale Yellow — later slide">

<sub><b>Biennale Yellow — later slide</b> · <code>biennale-yellow-later</code> · <a href="https://github.com/archlizheng/frontend-slides-editable/blob/e5663e6a0bdc2c2a673198bab3fb61036a7f20ee/docs/preset-previews/biennale-yellow-later.png"><code>docs/preset-previews/biennale-yellow-later.png</code></a></sub>

<img src="https://raw.githubusercontent.com/archlizheng/frontend-slides-editable/e5663e6a0bdc2c2a673198bab3fb61036a7f20ee/docs/preset-previews/block-frame-cover.png" width="100%" alt="BlockFrame — cover slide">

<sub><b>BlockFrame — cover slide</b> · <code>block-frame</code> · 封面 · <a href="https://github.com/archlizheng/frontend-slides-editable/blob/e5663e6a0bdc2c2a673198bab3fb61036a7f20ee/docs/preset-previews/block-frame-cover.png"><code>docs/preset-previews/block-frame-cover.png</code></a></sub>

<img src="https://raw.githubusercontent.com/archlizheng/frontend-slides-editable/e5663e6a0bdc2c2a673198bab3fb61036a7f20ee/docs/preset-previews/block-frame-mid.png" width="100%" alt="BlockFrame — mid slide">

<sub><b>BlockFrame — mid slide</b> · <code>block-frame-mid</code> · <a href="https://github.com/archlizheng/frontend-slides-editable/blob/e5663e6a0bdc2c2a673198bab3fb61036a7f20ee/docs/preset-previews/block-frame-mid.png"><code>docs/preset-previews/block-frame-mid.png</code></a></sub>

<img src="https://raw.githubusercontent.com/archlizheng/frontend-slides-editable/e5663e6a0bdc2c2a673198bab3fb61036a7f20ee/docs/preset-previews/block-frame-later.png" width="100%" alt="BlockFrame — later slide">

<sub><b>BlockFrame — later slide</b> · <code>block-frame-later</code> · <a href="https://github.com/archlizheng/frontend-slides-editable/blob/e5663e6a0bdc2c2a673198bab3fb61036a7f20ee/docs/preset-previews/block-frame-later.png"><code>docs/preset-previews/block-frame-later.png</code></a></sub>

<a id="gallery-ppt-svg-generator"></a>

#### [PPT SVG Generator](https://github.com/vigorX777/ppt-svg-generator) · 248 ⭐ · PPTX

<sub>Markdown → PPT / PDF，经 SVG 中转，多种预设风格。</sub>

<sub>取自 [`vigorX777/ppt-svg-generator`](https://github.com/vigorX777/ppt-svg-generator) 的 2 张图，此处 2 张，靠前的几张是项目自己放在 README 里的</sub>

```bash
git clone https://github.com/vigorX777/ppt-svg-generator
```

<img src="https://github.com/user-attachments/assets/2454e688-d3b8-40a2-a3f8-893bbe5060ee" width="100%" alt="image">

<sub><b>image</b> · GitHub 附件图</sub>

<img src="https://github.com/user-attachments/assets/97847c7f-5dc3-4a39-b4d8-ee3dc7d0396b" width="100%" alt="PixPin_2026-01-25_15-58-40">

<sub><b>PixPin_2026-01-25_15-58-40</b> · GitHub 附件图</sub>

<a id="gallery-mck-ppt-design-skill"></a>

#### [Mck PPT Design System](https://github.com/likaku/Mck-ppt-design-skill) · 229 ⭐ · PPTX

<sub>咨询公司风设计系统：70 种布局，扁平设计，python-pptx。</sub>

<sub>取自 [`likaku/Mck-ppt-design-skill`](https://github.com/likaku/Mck-ppt-design-skill) 的 6 张图，此处 6 张，靠前的几张是项目自己放在 README 里的</sub>

```bash
git clone https://github.com/likaku/Mck-ppt-design-skill
```

<img src="https://github.com/user-attachments/assets/075ec46d-dd73-4454-92d0-84184b78d276" width="100%" alt="Cover">

<sub><b>Cover</b> · GitHub 附件图</sub>

<img src="https://github.com/user-attachments/assets/3b25f071-8a81-48e3-a62b-9d9be9026f2e" width="100%" alt="Content">

<sub><b>Content</b> · GitHub 附件图</sub>

<img src="https://github.com/user-attachments/assets/be327c14-aff9-459f-89b0-d4a8bffaabfc" width="100%" alt="Table">

<sub><b>Table</b> · GitHub 附件图</sub>

<img src="https://github.com/user-attachments/assets/687cee47-13bb-4d6b-840f-77f8e001a62b" width="100%" alt="4-Column">

<sub><b>4-Column</b> · GitHub 附件图</sub>

<img src="https://github.com/user-attachments/assets/41371c47-608f-4857-9bfe-791121ec1579" width="100%" alt="Colors">

<sub><b>Colors</b> · GitHub 附件图</sub>

<img src="https://github.com/user-attachments/assets/c5b6e52a-fd91-4c28-88a4-82fdfedfd956" width="100%" alt="Summary">

<sub><b>Summary</b> · GitHub 附件图</sub>

<a id="gallery-ppt-agent-skill"></a>

#### [PPT Agent Skill](https://github.com/Akxan/ppt-agent-skill) · 114 ⭐ · HTML

<sub>26 种风格、18 种图表，对标 Linear / Anthropic / Stripe / Apple / NYT。</sub>

<sub>取自 [`Akxan/ppt-agent-skill`](https://github.com/Akxan/ppt-agent-skill) 的 32 张图，此处 24 张，靠前的几张是项目自己放在 README 里的</sub>

```bash
git clone https://github.com/Akxan/ppt-agent-skill
```

<sub><b>下面出现的风格</b> `all` · `vibrant` · `natural-retro` · `dark-professional` · `light-premium` · `cultural-oriental` · `bauhaus-block` · `blue-white` · `botanic-forest` · `candy-pastel` · `champagne-gold` · `chrome-y2k` —— 要哪个就在提示里点名。这些是<b>项目自己用的字符串</b>，取自每张图下面链接的文件名与说明，不是本仓库起的名字。</sub>

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

<sub>带演讲者备注的 HTML 幻灯片，配套放映 app。</sub>

<sub>取自 [`bluedusk/html-slides`](https://github.com/bluedusk/html-slides) 的 4 张图，此处 4 张</sub>

```bash
git clone https://github.com/bluedusk/html-slides
```

<sub><b>下面出现的风格</b> `screenshot` · `hero` —— 要哪个就在提示里点名。这些是<b>项目自己用的字符串</b>，取自每张图下面链接的文件名与说明，不是本仓库起的名字。</sub>

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

<sub>将内容快速生成金蝶风格 PPT。</sub>

<sub>取自 [`WayneZhon/KingDee-PPT-Skill`](https://github.com/WayneZhon/KingDee-PPT-Skill) 的 1 张图，此处 1 张</sub>

```bash
git clone https://github.com/WayneZhon/KingDee-PPT-Skill
```

<sub><b>下面出现的风格</b> `closing` —— 要哪个就在提示里点名。这些是<b>项目自己用的字符串</b>，取自每张图下面链接的文件名与说明，不是本仓库起的名字。</sub>

<img src="https://raw.githubusercontent.com/WayneZhon/KingDee-PPT-Skill/28ca93aadeefc91fcc64152714ddeece15f13e1d/assets/closing_thanks.png" width="100%" alt="KingDee PPT Skill sample">

<sub><b>Closing</b> · 结尾页 · <a href="https://github.com/WayneZhon/KingDee-PPT-Skill/blob/28ca93aadeefc91fcc64152714ddeece15f13e1d/assets/closing_thanks.png"><code>assets/closing_thanks.png</code></a></sub>

<a id="gallery-slide-creator"></a>

#### [Slide Creator](https://github.com/kaisersong/slide-creator) · 46 ⭐ · 双路线

<sub>AI 规划 + 风格发现 + PPTX 导出。</sub>

<sub>取自 [`kaisersong/slide-creator`](https://github.com/kaisersong/slide-creator) 的 23 张图，此处 23 张，靠前的几张是项目自己放在 README 里的</sub>

```bash
git clone https://github.com/kaisersong/slide-creator
```

<sub><b>下面出现的风格</b> `strategy-consulting` · `blue-sky` · `bold-signal` · `electric-studio` · `creative-voltage` · `dark-botanical` · `notebook-tabs` · `pastel-geometry` · `split-pastel` · `vintage-editorial` · `neon-cyber` · `terminal-green` —— 要哪个就在提示里点名。这些是<b>项目自己用的字符串</b>，取自每张图下面链接的文件名与说明，不是本仓库起的名字。</sub>

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

<sub>「你的下个 slide，何必是 PPT」—— 26+ 风格，零依赖，中英双语。</sub>

<sub>取自 [`codesstar/next-slide`](https://github.com/codesstar/next-slide) 的 1 张图，此处 1 张</sub>

```bash
git clone https://github.com/codesstar/next-slide
```

<sub><b>下面出现的风格</b> `motion-brand-showcase` —— 要哪个就在提示里点名。这些是<b>项目自己用的字符串</b>，取自每张图下面链接的文件名与说明，不是本仓库起的名字。</sub>

<img src="https://raw.githubusercontent.com/codesstar/next-slide/e92c1b2506e6cf5acff7d2b92339ba0c0ce2af22/scenarios/images/motion-brand-showcase.webp" width="100%" alt="next-slide sample">

<sub><b>Motion Brand Showcase</b> · <a href="https://github.com/codesstar/next-slide/blob/e92c1b2506e6cf5acff7d2b92339ba0c0ce2af22/scenarios/images/motion-brand-showcase.webp"><code>scenarios/images/motion-brand-showcase.webp</code></a></sub>

<a id="gallery-slide-writer"></a>

#### [Slide Writer](https://github.com/FeeiCN/slide-writer) · 40 ⭐ · HTML

<sub>从想法、大纲、文档或演讲稿生成企业级 HTML 演示。</sub>

<sub>取自 [`FeeiCN/slide-writer`](https://github.com/FeeiCN/slide-writer) 的 5 张图，此处 5 张，靠前的几张是项目自己放在 README 里的</sub>

```bash
git clone https://github.com/FeeiCN/slide-writer
```

<sub><b>下面出现的风格</b> `before-after` · `writer` · `test-antgroup-eric` · `test-tencent-pony-ma` · `test-alibaba-jack-ma` —— 要哪个就在提示里点名。这些是<b>项目自己用的字符串</b>，取自每张图下面链接的文件名与说明，不是本仓库起的名字。</sub>

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

<sub>50 美学 × 20 配色 × 10 字体 × 5 布局 × 30+ 特效 = 5 万种组合。</sub>

<sub>取自 [`nghiahsgs/skills-slides`](https://github.com/nghiahsgs/skills-slides) 的 4 张图，此处 4 张，靠前的几张是项目自己放在 README 里的</sub>

```bash
git clone https://github.com/nghiahsgs/skills-slides
```

<sub><b>下面出现的风格</b> `06-features` · `07-checklist` · `03-50k` —— 要哪个就在提示里点名。这些是<b>项目自己用的字符串</b>，取自每张图下面链接的文件名与说明，不是本仓库起的名字。</sub>

<img src="https://raw.githubusercontent.com/nghiahsgs/skills-slides/c271d3cda03bf79733cc91ba28e25716196638b7/examples/screenshots/slide-06-features.png" width="100%" alt="Feature grid — 6 cards with 3D tilt hover">

<sub><b>Feature grid — 6 cards with 3D tilt hover</b> · <code>06-features</code> · <a href="https://github.com/nghiahsgs/skills-slides/blob/c271d3cda03bf79733cc91ba28e25716196638b7/examples/screenshots/slide-06-features.png"><code>examples/screenshots/slide-06-features.png</code></a></sub>

<img src="https://raw.githubusercontent.com/nghiahsgs/skills-slides/c271d3cda03bf79733cc91ba28e25716196638b7/examples/screenshots/slide-07-checklist.png" width="100%" alt="Anti-slop checklist — 10-point quality gate">

<sub><b>Anti-slop checklist — 10-point quality gate</b> · <code>07-checklist</code> · <a href="https://github.com/nghiahsgs/skills-slides/blob/c271d3cda03bf79733cc91ba28e25716196638b7/examples/screenshots/slide-07-checklist.png"><code>examples/screenshots/slide-07-checklist.png</code></a></sub>

<img src="https://raw.githubusercontent.com/nghiahsgs/skills-slides/c271d3cda03bf79733cc91ba28e25716196638b7/examples/screenshots/slide-01-title.png" width="100%" alt="Skills Slides sample">

<sub><b>Title</b> · 标题页 · <a href="https://github.com/nghiahsgs/skills-slides/blob/c271d3cda03bf79733cc91ba28e25716196638b7/examples/screenshots/slide-01-title.png"><code>examples/screenshots/slide-01-title.png</code></a></sub>

<img src="https://raw.githubusercontent.com/nghiahsgs/skills-slides/c271d3cda03bf79733cc91ba28e25716196638b7/examples/screenshots/slide-03-50k.png" width="100%" alt="Skills Slides sample">

<sub><b>03 50k</b> · <a href="https://github.com/nghiahsgs/skills-slides/blob/c271d3cda03bf79733cc91ba28e25716196638b7/examples/screenshots/slide-03-50k.png"><code>examples/screenshots/slide-03-50k.png</code></a></sub>

<a id="gallery-powerpoint-fancy-design"></a>

#### [PowerPoint Fancy Design](https://github.com/Phlegonlabs/Powerpoint-fancy-design) · 27 ⭐ · 双路线

<sub>结构化 Markdown → 1600×900 HTML 幻灯片 + PNG 渲染 + 可导出。</sub>

<sub>取自 [`Phlegonlabs/Powerpoint-fancy-design`](https://github.com/Phlegonlabs/Powerpoint-fancy-design) 的 30 张图，此处 24 张，靠前的几张是项目自己放在 README 里的</sub>

```bash
git clone https://github.com/Phlegonlabs/Powerpoint-fancy-design
```

<sub><b>下面出现的风格</b> `swiss-international` · `east-asian-minimalism` · `risograph-print` · `bauhaus-geometry` · `organic-handcrafted` · `art-deco-luxury` · `neo-brutalism` · `retro-futurism` · `dark-editorial` · `memphis-pop` —— 要哪个就在提示里点名。这些是<b>项目自己用的字符串</b>，取自每张图下面链接的文件名与说明，不是本仓库起的名字。</sub>

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

<sub>严格通过模板母版版式，从 Markdown 生成 PPTX。</sub>

<sub>取自 [`tristan-mcinnis/pptx-from-layouts-skill`](https://github.com/tristan-mcinnis/pptx-from-layouts-skill) 的 1 张图，此处 1 张</sub>

```bash
git clone https://github.com/tristan-mcinnis/pptx-from-layouts-skill
```

<sub><b>下面出现的风格</b> `thumbnail` —— 要哪个就在提示里点名。这些是<b>项目自己用的字符串</b>，取自每张图下面链接的文件名与说明，不是本仓库起的名字。</sub>

<img src="https://raw.githubusercontent.com/tristan-mcinnis/pptx-from-layouts-skill/53b0e750694d807e3510c2017744197c3c5089b0/examples/q1-strategy/thumbnail.jpg" width="100%" alt="PPTX from Layouts sample">

<sub><b>Thumbnail</b> · <a href="https://github.com/tristan-mcinnis/pptx-from-layouts-skill/blob/53b0e750694d807e3510c2017744197c3c5089b0/examples/q1-strategy/thumbnail.jpg"><code>examples/q1-strategy/thumbnail.jpg</code></a></sub>

<sub>以下项目的仓库里没有可用图片：Anthropic PPTX (official)、Visual Explainer、Claude Office Skills、Academic PPTX、Visual Cognition Slides、Huawei Style PPT Skill。</sub>

<sub>**共 278 张，全部来自各项目自己的仓库**，按原尺寸完整展示、不做缩略图 —— 幻灯片信息密度高，缩到 300px 根本看不清字体和层次。每张都读自锁定的 commit，出处写在它上方的说明里，并且直接由原仓库提供、没有复制到本仓库。**没有任何一张是本仓库跑出来的**，所以它反映的是每个团队愿意拿出来展示的样子，不是同题横评。用 `python scripts/fetch_samples.py` 重新生成。</sub>
<!-- END:GALLERY -->

---

## 横评 —— 已搁置

原本的计划是拿一份公开评分卡给每个 skill 打分。工具链是真的建好了并且能跑：三份
[语料](benchmark/corpus/)、[七维度评分卡](benchmark/rubric.md)、机械化的数据保真与图表校验、
双盲评审。

**但它被搁置了，原因是算术。** PPTX 路线生成一份 deck 约需 $10 的 agent 成本，而且这个价还没
跑完；Tier S 全覆盖跑一遍要几百美元 —— 而评分卡自己写着，实测次数不到两位数时分数没有意义。
也就是说，要花几个月和真金白银才能得到第一个站得住的排名，这不该是这个仓库把自己耗进去的地方。
**用上面的表来选，那是事实，不是分数。**

这次尝试真正留下的东西比分数更值钱 —— 那些测量工具，以及一个现在成了
[原则 7 实证](principles/07-render-and-look.md)的发现。

<details>
<summary>唯一跑完的那一次</summary>

<!-- BEGIN:SCORECARD -->
| 项目 | 总分 | 视觉 | 字体 | 密度 | 数据 | 内容 | 交付 | 代价 | 次数 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| **frontend-slides** | **25.0**/35 | 3.0 | 4.0 | 3.0 | 3.0 | 5.0 | 3.0 | 4.0 | 1 |

<sub>目前仅 1 次实测 —— 远不足以给任何东西排名。分数均为暂定值，每次实测都公开披露其利益冲突。⚠️ = 该次实测在数据或内容保真上被一票否决。</sub>
<!-- END:SCORECARD -->

n=1，原本还是非盲评的，认真测过之后
[两个维度被下调](benchmark/results/run-01/README.md#corrections)。这不是排名。
→ [工具链、语料与评分卡](benchmark/)

</details>

---

## 八条原则

三十来个团队并行解决了同一个问题。**他们各自独立收敛到的地方，是这个领域最可靠的信号。**
[**阅读全部原则 →**](principles/)

| | 原则 | 一句话版本 |
|---|---|---|
| 1 | [Show, don't tell](principles/01-show-dont-tell.md) | 永远不要问审美。生成选项让人指。 |
| 2 | [反 slop 靠禁用清单](principles/02-anti-ai-slop.md) | 「做好看点」没用，「禁用 Inter」有用。 |
| 3 | [幻灯片是印刷品](principles/03-fixed-stage.md) | 固定 1920×1080，等比缩放，加黑边。放弃响应式。 |
| 4 | [约束胜过自由](principles/04-constraint-beats-freedom.md) | 锁死配色。Agent 会更稳定，而不是更无能。 |
| 5 | [SKILL.md 是目录](principles/05-progressive-disclosure.md) | Zara 把 1,625 行砍到 183 行，功能不变，context 省 89%。 |
| 6 | [单文件比框架活得久](principles/06-single-file.md) | 依赖就是债。全部内联。 |
| 7 | [渲染出来，然后看一眼](principles/07-render-and-look.md) | 视觉产物需要视觉验收。截图，让模型自己看。 |
| 8 | [蒸馏，而非设计](principles/08-distill-dont-design.md) | 先手工做三十遍，**再**写 skill。 |

第 2 条的证据最硬：`frontend-slides` 和 Anthropic 官方 `pptx` skill **各自独立地**、用几乎
一样的措辞，禁止了「标题下方的装饰线」。当一个社区和一个模型厂商收敛到同一条如此具体的禁令
时，那就是机器生成设计的真实指纹。

---

## 这份数据怎么保持准确

手工维护的列表一定会烂。这份是生成的：

```
data/skills.json       ──▶ 人工调研内容，唯一手写的文件
data/stats.json        ──▶ GitHub 实时数据，CI 每天刷新
data/capabilities.json ──▶ 文档声称的能力，每条都带出处引文
data/samples.json      ──▶ 样例图，锁定到读取时的那个 commit
        │
        └──▶ scripts/render.py ──▶ 生成两个 README 里的所有表格和图库
```

```bash
python scripts/fetch_stats.py       # 刷新 star / fork / license / 活跃度
python scripts/fetch_samples.py     # 重新抓取各仓库的样例图
python scripts/fetch_samples.py --verify   # 校验每张锁定的图仍然存在
python scripts/render.py            # 重新生成两个 README 的全部表格
python scripts/render.py --check    # CI 卡口：README 过期就失败
```

图库里的图**一张都没有复制进本仓库**，全部是指向原项目文件、且锁死 commit 的链接 ——
这样图不会在说明文字底下悄悄变掉，署名也丢不了。

GitHub Action 每天跑一次，数字变化时自动开 PR。**手工改表格是无效操作** —— 下次生成会覆盖。
要改请改 `data/skills.json`。

---

## 参与贡献

新 skill、勘误，尤其是**实测跑分** —— 见 [CONTRIBUTING.md](CONTRIBUTING.md)。

如果你是这些 skill 的作者，而这里写错了，请开 issue。我会改；如果是某次实测有问题，会重跑，
并把原始记录留在 git 历史里。

---

## 诚实的局限

- **star 数衡量的是关注度，不是质量。** 这里好几个项目的增长很大程度来自作者可观的社交影响
  力。那是关于社区规模的真实信号，仅此而已。这正是横评存在的理由。
- **目前还没有实测数据。** 本页的排序**不是**质量排名，而是一份按热度排序、并明确标注了这一
  点的登记册 —— 在真实分数出现之前都是如此。
- **生成式的方差是真实存在的。** 同一个 skill、同一个 prompt，两次产出就是不一样。在样本量
  进入两位数之前，小的分差不说明任何问题。
- **描述基于文档**，不是基于「我亲手用全部 26 个都做过 deck」。我实际跑过的，档案里会写明。
- **这是个快速变化的领域。** 所有内容都带日期，请看清楚。

---

## 来源与前人工作

有两份精选列表走在这个仓库之前，也是本仓库的线索来源 ——
[ToseaAI/awesome-html-slide-skills](https://github.com/ToseaAI/awesome-html-slide-skills)
和 [software-ai-life/Awesome-PPT-Design-Skills](https://github.com/software-ai-life/Awesome-PPT-Design-Skills)。
两者都聚焦 HTML 路线；本登记册同时覆盖 PPTX 路线 —— 而这个领域 star 数最高的那个项目，恰恰
就在那条路线上。

更长的调研笔记（含支撑八条原则的一手材料阅读）：
[`docs/research-notes-2026-07.md`](docs/research-notes-2026-07.md)。

所有 star、fork、license 和活跃度数据均由 GitHub REST API 实时抓取，**从不转载其他列表**。

---

<div align="center">
<sub>

登记册内容采用 [CC BY 4.0](LICENSE) · 代码采用 [MIT](LICENSE-CODE)
被收录的项目各有其协议 —— **请自行确认**，其中有一个是 AGPL-3.0。

</sub>
</div>
