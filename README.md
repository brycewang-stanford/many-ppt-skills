<div align="center">

# many-ppt-skills

**值得知道的 AI 幻灯片 Skill 全在这一页，并排对比 —— 让你挑对一个，然后接着干活。**

在[图库](#它们长什么样)里看中哪张，照 **[60 秒做出同款](#60-秒做出同款)** 三步走，就能做出你自己的那一份。

[简体中文](README.md) · [English](README.en.md)

<!-- BEGIN:COUNTS -->
**收录 227 个 skill**，其中 **39 个人工读过** · **合计 271,800 star** · HTML 路线 83 个 · PPTX 路线 79 个 · 双路线 25 个 · 数据刷新于 **2026-07-29**
<!-- END:COUNTS -->

</div>

---

Coding Agent 把 CSS 写好了，半年之内冒出一整个新品类：把文档变成不像机器做的幻灯片的
Skill。这一页收录了 <!-- BEGIN:TRACKED -->227<!-- END:TRACKED --> 个，其中四个 star 数都超过 2 万。

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

## 60 秒做出同款

先看[图库](#它们长什么样)，看中一张图之后照这三步走。下面用一个真实例子从头走一遍。

**第一步：从图注里抄下风格 ID。** 每张图下面都有一行说明，长这样：

> **Soft Editorial · 4** · `soft-editorial` · [`screenshots/soft-editorial-4.png`](https://github.com/zarazhangrui/beautiful-html-templates)

等宽字体的 `soft-editorial` 就是**风格 ID** —— 抄它。它属于哪个 skill，看这组图上方的标题
（这里是 **Frontend Slides**）。

**第二步：装这个 skill。** 命令就印在那组图上面，直接复制。这个例子里是 `plugin` 方式，
**两条命令都在 Claude Code 里面敲，不是终端**：

```text
/plugin marketplace add https://github.com/zarazhangrui/frontend-slides
/plugin install frontend-slides@frontend-slides
```

> 一共有五种安装方式，含义不同（`clone` 是克隆进 `~/.claude/skills/` 并需要重开会话，
> `python` 要本机装依赖，`npx` 是建项目而不是装 skill）。对照表在
> [看中一张图，怎么做出来](#看中一张图怎么做出来)。

**第三步：把风格 ID 写进你的话里。** 它不是命令行参数，就是提示词的一部分：

```text
用 soft-editorial 这个模板，把 docs/roadmap.md 做成一份 12 页的 deck，
面向投资人，我会现场讲，所以每页字少一点。
```

就这样。**点名风格 ID 等于跳过挑选环节** —— frontend-slides 默认会先生成 3 个预览让你选，
你直接点名就是告诉它别问了，照这个做。想看选项就别点名，直接说「帮我做一份关于 X 的 deck」。

不想自己翻这一页？[下一节](#让-agent-直接帮你挑)把这个仓库本身装成 skill，让 agent 替你选。

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

<details open>
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
| **[Slidev](https://github.com/slidevjs/slidev)**†<br><sub>slidevjs</sub> | 47,889 | 框架 | MIT | 面向开发者的演示文稿框架，使用 Markdown 和 Vue 制作幻灯片。 |
| **[PPT Master](https://github.com/hugohe3/ppt-master)**<br><sub>hugohe3</sub> | 41,774 | PPTX | MIT | 把文档或主题变成真正原生可编辑的 PPTX。 |
| **[Frontend Slides](https://github.com/zarazhangrui/frontend-slides)**<br><sub>Zara Zhang</sub> | 26,568 | HTML | MIT | 用 Coding Agent 的前端能力做好看的网页幻灯片。 |
| **[Guizang PPT Skill](https://github.com/op7418/guizang-ppt-skill)**<br><sub>op7418 (歸藏)</sub> | 22,694 | HTML | ⚠️ AGPL-3.0 | 杂志编辑风与瑞士国际风 HTML 幻灯片，以「锁死约束」保证一致性。 |
| **[Huashu Design](https://github.com/alchaincyf/huashu-design)**<br><sub>花生 (alchaincyf)</sub> | 22,190 | 双路线 | MIT | HTML 原生设计 skill —— 高保真原型、幻灯片、动效与设计评审，不止是 PPT。 |
| **[Quarkdown](https://github.com/iamgio/quarkdown)**†<br><sub>iamgio</sub> | 15,836 | 框架 | GPL-3.0 | 基于 Markdown 的框架，从单一源文件生成论文、演示文稿、网站和书籍。 |
| **[Banana Slides](https://github.com/Anionex/banana-slides)**†<br><sub>Anionex</sub> | 15,346 | PPTX | ⚠️ AGPL-3.0 | 原生 AI PPT 生成器，接受模板、文字提示或大纲，导出可编辑 PPTX 文件。 |
| **[Visual Explainer](https://github.com/nicobailon/visual-explainer)**<br><sub>nicobailon</sub> | 9,351 | HTML | MIT | 为图表、diff 评审、方案审计、数据表和项目复盘生成 HTML 页面或幻灯片。 |
| **[HTML Anything](https://github.com/nexu-io/html-anything)**†<br><sub>nexu-io</sub> | 7,996 | 套件 | Apache-2.0 | 具有 75 个技能的智能 HTML 编辑器，涵盖幻灯片、海报和原型等 9 种输出类型。 |
| **[HTML PPT Studio](https://github.com/lewislulu/html-ppt-skill)**<br><sub>lewislulu</sub> | 7,473 | HTML | MIT | 24 主题 × 31 布局 × 20+ 动效的专业 HTML 演示。 |
| **[open-slide](https://github.com/1weiho/open-slide)**<br><sub>1weiho</sub> | 6,042 | 框架 | MIT | 为 Agent 而生的幻灯片框架 —— React 组件渲染到固定 1920×1080 画布。 |
| **[Anthropic PPTX (official)](https://github.com/anthropics/skills/tree/main/skills/pptx)**<br><sub>Anthropic</sub> | 164,969* | PPTX | See repo | 官方基线方案 —— 创建、读取、编辑与合并 PowerPoint 文件。 |
| **[Baoyu Skills](https://github.com/JimLiu/baoyu-skills/tree/main/skills/baoyu-slide-deck)**†<br><sub>JimLiu (宝玉)</sub> | 24,310* | 套件 | MIT | 22 个技能的个人合集，其中 baoyu-slide-deck 把文章或大纲变成幻灯片。 |

### Tier A — 生产可用（100–5k star）

| 项目 | ⭐ | 路线 | License | 一句话 |
|---|---:|---|---|---|
| **[Dashi PPT Skill](https://github.com/chuspeeism/dashi-ppt-skill)**†<br><sub>chuspeeism</sub> | 4,388 | 双路线 | ⚠️ AGPL-3.0 | 从多种视觉主题生成可在浏览器编辑的演示文稿，支持导出为 HTML、PDF 和 PPTX。 |
| **[Codex PPT Skill](https://github.com/ningzimu/codex-ppt-skill)**†<br><sub>ningzimu</sub> | 4,295 | 图片 | MIT | 使用 GPT-Image-2 在 Codex 及兼容智能体中生成基于图像的 PowerPoint 幻灯片。 |
| **[Beautiful HTML Templates](https://github.com/zarazhangrui/beautiful-html-templates)**<br><sub>Zara Zhang</sub> | 3,940 | 模板库 | MIT | 34 套 HTML 幻灯片模板，配 index.json 元数据供任意 Agent 检索选用。 |
| **[NanoBanana PPT Skills](https://github.com/op7418/NanoBanana-PPT-Skills)**†<br><sub>op7418</sub> | 3,167 | 图片 | Unspecified | AI 技能，自动生成高质量 PPT 幻灯片图片和视频，支持智能转场与交互式播放。 |
| **[Baoyu Design](https://github.com/JimLiu/baoyu-design)**†<br><sub>JimLiu</sub> | 2,879 | HTML | MIT | 在本地运行 Claude 设计系统提示，生成 UI 原型、幻灯片和线框图，输出为独立 HTML 文件。 |
| **[Gorden PPT Skill](https://github.com/GordenSun/GordenPPTSkill)**†<br><sub>GordenSun</sub> | 2,822 | PPTX | NOASSERTION | 通过 JSON 文件对 17 个中文模板进行纯文字编辑，生成保留布局的 PPTX 文件。 |
| **[Codex Claude Academic Skills](https://github.com/zLanqing/codex-claude-academic-skills)**†<br><sub>zLanqing</sub> | 2,357 | 套件 | MIT | 面向科研人员的三技能套件，涵盖论文阅读、PPT/Word 生成、写作辅助及科学图表绘制。 |
| **[Oh My PPT](https://github.com/arcsin1/oh-my-ppt)**†<br><sub>arcsin1</sub> | 1,810 | HTML | Apache-2.0 | 输入文字描述，在本地生成简洁美观的 HTML 幻灯片，无需联网。 |
| **[Image to Editable PPT Skill](https://github.com/ningzimu/image-to-editable-ppt-skill)**†<br><sub>ningzimu</sub> | 1,676 | PPTX | MIT | 将幻灯片图像、PDF 及基于图像的 PPTX 文件转换为可编辑的 PowerPoint 演示文稿。 |
| **[Gorden Super PPT Skills](https://github.com/GordenSun/GordenSuperPPTSkills)**†<br><sub>GordenSun</sub> | 1,659 | PPTX | Unspecified | 使用 GPT 生成高质量 PPT 图像，再将其转换为完全可编辑的 PPTX 文件。 |
| **[CyberPPT](https://github.com/crazyykhllc-bit/CyberPPT)**†<br><sub>crazyykhllc-bit</sub> | 1,483 | PPTX | MIT | 用于生成高密度、可编辑咨询风格 PowerPoint 的 Codex 技能，支持 SCR 叙事与质量检查。 |
| **[Ian Handdrawn PPT](https://github.com/helloianneo/ian-handdrawn-ppt)**†<br><sub>helloianneo</sub> | 1,292 | 图片 | MIT | 生成手绘风格的中文技术 PPT 整页图像（PNG），包含 21:9 封面和 16:9 正文配图。 |
| **[PPT Image First](https://github.com/NyxTides/ppt-image-first)**†<br><sub>NyxTides</sub> | 1,175 | 图片 | Apache-2.0 | 面向 Codex、Claude Code 和 Opencode CLI 的以图像为优先的 PPT 生成技能。 |
| **[GPT Image2 PPT Skills](https://github.com/JuneYaooo/gpt-image2-ppt-skills)**†<br><sub>JuneYaooo</sub> | 1,118 | 图片 | Apache-2.0 | 使用 gpt-image-2 克隆 PPTX 布局，替换为您的内容；内置 10 套精选风格。 |
| **[PPT Agent Skills](https://github.com/sunbigfly/ppt-agent-skills)**†<br><sub>sunbigfly</sub> | 862 | HTML | NOASSERTION | 像构建软件工程一样，以代码驱动方式生成演示文稿的框架。 |
| **[Humanize PPT](https://github.com/LearnPrompt/humanize-ppt)**†<br><sub>LearnPrompt</sub> | 837 | HTML | NOASSERTION | 基于 AST 的大纲编排器，用于构建以人为中心的 AI 演示文稿工作流。 |
| **[Claude Office Skills](https://github.com/tfriedel/claude-office-skills)**<br><sub>tfriedel</sub> | 798 | PPTX | Unspecified | PPTX / DOCX / XLSX / PDF 全家桶，支持自动化。 |
| **[Academic PPTX](https://github.com/Gabberflast/academic-pptx-skill)**<br><sub>Gabberflast</sub> | 724 | PPTX | MIT | 会议报告、研讨会、论文答辩与基金汇报。 |
| **[Claude Skills](https://github.com/staruhub/ClaudeSkills)**†<br><sub>staruhub</sub> | 632 | 套件 | MIT | 精选 13 个 Claude Code 智能体技能，涵盖幻灯片、深度研究、PRD、文章和审计。 |
| **[PPT Agent Workflow San](https://github.com/mucsbr/ppt-agent-workflow-san)**<br><sub>mucsbr</sub> | 618 | HTML | Unspecified | 渐进交互式 PPT 生成 skill。 |
| **[Power Design](https://github.com/ItsssssJack/power-design)**†<br><sub>ItsssssJack</sub> | 575 | HTML | NOASSERTION | 结合品牌基因与 20 条设计原则的 Claude 技能，生成看起来非 AI 制作的幻灯片。 |
| **[Frontend Slides Editable](https://github.com/archlizheng/frontend-slides-editable)**<br><sub>archlizheng</sub> | 446 | 双路线 | MIT | 可编辑 HTML 幻灯片：拖拽缩放、页序调整、本地保存、PPTX 互转。 |
| **[Reveal.js Skill](https://github.com/ryanbbrown/revealjs-skill)**†<br><sub>ryanbbrown</sub> | 379 | HTML | MIT | 用于构建 reveal.js HTML 演示文稿的编码智能体技能。 |
| **[Visual Style PPT Skill](https://github.com/irenerachel/visual-style-ppt-skill)**†<br><sub>irenerachel</sub> | 359 | PPTX | Unspecified | 运行视觉风格 PPT 生成工作流的技能。 |
| **[Beamer Skill](https://github.com/Noi1r/beamer-skill)**†<br><sub>Noi1r</sub> | 319 | HTML | MIT | 管理学术 Beamer LaTeX 幻灯片的完整生命周期——创建、编译、审阅、质量评分与润色。 |
| **[RW Consulting PPT](https://github.com/Pikapika260214/rw-consulting-ppt)**†<br><sub>Pikapika260214</sub> | 317 | PPTX | MIT | 用于生成可编辑咨询风格 PowerPoint 演示文稿的 Codex 技能。 |
| **[Paper2Anything](https://github.com/QuZhan51496/paper2anything)**†<br><sub>QuZhan51496</sub> | 316 | 套件 | Apache-2.0 | 将学术论文 PDF 转换为幻灯片、海报、网页、小红书帖子或微信文章。 |
| **[DOM to PPTX](https://github.com/atharva9167j/dom-to-pptx)**†<br><sub>atharva9167j</sub> | 302 | PPTX | MIT | 客户端库，将任意 HTML 元素转换为像素精准、完全可编辑的 PowerPoint 幻灯片。 |
| **[Marp Slides](https://github.com/robonuggets/marp-slides)**†<br><sub>robonuggets</sub> | 271 | HTML | Unspecified | 适用于 Claude Code 的 MARP 演示文稿技能，含 22 个示例幻灯片、SVG 图表和深/浅主题。 |
| **[Beamer Academic](https://github.com/Faust-Donf/beamer-academic)**†<br><sub>Faust-Donf</sub> | 258 | HTML | MIT | 一键从论文生成高质量学术答辩 Beamer 幻灯片。 |
| **[PPT SVG Generator](https://github.com/vigorX777/ppt-svg-generator)**<br><sub>vigorX777</sub> | 248 | PPTX | MIT | Markdown → PPT / PDF，经 SVG 中转，多种预设风格。 |
| **[Mck PPT Design System](https://github.com/likaku/Mck-ppt-design-skill)**<br><sub>likaku</sub> | 230 | PPTX | Apache-2.0 | 咨询公司风设计系统：70 种布局，扁平设计，python-pptx。 |
| **[Planners PPT Hell](https://github.com/thePlannerIvan/planners-ppt-hell)**†<br><sub>thePlannerIvan</sub> | 216 | PPTX | ⚠️ AGPL-3.0 | 面向规划人员的 PPT 生成技能。 |
| **[Thesis Defense PPTX Skill](https://github.com/zouchenzhen/thesis-defense-pptx-skill)**†<br><sub>zouchenzhen</sub> | 209 | PPTX | Apache-2.0 | 从论文 PDF 或 LaTeX 源文件生成可编辑答辩 PPTX，同时保留指定 PPT 模板风格。 |
| **[Apple Bento Grid](https://github.com/hubeiqiao/apple-bento-grid)**†<br><sub>hubeiqiao</sub> | 204 | HTML | MIT | 生成苹果风格 Bento Grid 演示卡片，以 HTML 形式输出。 |
| **[Codex PPT Skill](https://github.com/Ronnie2025/codex-ppt-skill)**†<br><sub>Ronnie2025</sub> | 198 | 图片 | MIT | 面向中文 toB 商业汇报的 Codex PPT 生图、元素重组与 SVG 拆解工作流。 |
| **[Hands on Deck](https://github.com/EveryInc/hands-on-deck)**†<br><sub>EveryInc</sub> | 198 | PPTX | MIT | 让 AI 智能体通过原子 JSON 补丁检查、编辑、创建和验证 PPTX 文件的 CLI 工具。 |
| **[Skywork Skills](https://github.com/SkyworkAI/Skywork-Skills)**†<br><sub>SkyworkAI</sub> | 194 | 套件 | MIT | 智能体技能套件，涵盖 AI PPT、文档、Excel、图像、深度研究和音乐，适用于任何兼容智能体。 |
| **[PPT Image2 Editable Rebuild](https://github.com/wwe-dog/ppt-image2-editable-rebuild)**†<br><sub>wwe-dog</sub> | 186 | PPTX | Unlicense | 通过结合生成的视觉参考图与文本形状，将截图或参考图重建为可编辑的 PPTX 文件。 |
| **[Slide Image to Editable PPTX](https://github.com/w1163222589-coder/slide-image-to-editable-pptx)**†<br><sub>w1163222589-coder</sub> | 172 | PPTX | MIT | 将幻灯片截图转换为可编辑的 PowerPoint 演示文稿。 |
| **[Magic Slide](https://github.com/daniel-style/magic-slide)**†<br><sub>daniel-style</sub> | 170 | HTML | MIT | 生成带有流畅 Magic Move 风格转场动画的独立 HTML 演示文稿。 |
| **[Presentation Skills](https://github.com/Sven-LI-sankyuu/presentation-skills)**†<br><sub>Sven-LI-sankyuu</sub> | 162 | 双路线 | Unspecified | Codex CLI 技能集合，涵盖可编辑 PPT 图表协作与端到端网页演示视频合成工作流。 |
| **[Claude Design Skill](https://github.com/jiji262/claude-design-skill)**†<br><sub>jiji262</sub> | 162 | HTML | MIT | 在本地使用 Claude.ai 内部设计提示，生成 HTML 幻灯片、落地页、原型和海报。 |
| **[Servasyy Skills](https://github.com/huangserva/servasyy_skills)**†<br><sub>huangserva</sub> | 151 | 套件 | Unspecified | 一套覆盖写作、配图、PPT、播客、视频和漫画生成的AI技能集合。 |
| **[Ultimate PPT Master Skill](https://github.com/kdnsna/ultimate-ppt-master-skill)**†<br><sub>kdnsna</sub> | 147 | 双路线 | MIT | 通过明确受众、场景和风格后，将一句话需求转化为可编辑的PPTX或网页幻灯片。 |
| **[Future Slide](https://github.com/bytonylee/future-slide)**†<br><sub>bytonylee</sub> | 143 | 套件 | Apache-2.0 | 十个幻灯片技能，按规划 / 提示 / 渲染拆分，同时覆盖 HTML 与 GPT 生图两条路线。 |
| **[Slide Deck Generator](https://github.com/code-on-sunday/slide-deck-generator)**†<br><sub>code-on-sunday</sub> | 134 | HTML | MIT | 通过编程智能体提示，使用React、Vite和Framer Motion创建基于浏览器的幻灯片。 |
| **[PPT Agent Skill](https://github.com/Akxan/ppt-agent-skill)**<br><sub>Akxan</sub> | 116 | HTML | MIT | 26 种风格、18 种图表，对标 Linear / Anthropic / Stripe / Apple / NYT。 |
| **[HTML PPT Designer](https://github.com/andyhuo520/html-ppt-designer)**†<br><sub>andyhuo520</sub> | 114 | HTML | Unspecified | 将任意内容转化为精致的HTML演示文稿。 |
| **[Presentation Skills](https://github.com/pamelafox/presentation-skills)**†<br><sub>pamelafox</sub> | 105 | HTML | MIT | 面向教师和演讲者的AI智能体演示文稿处理技能集合。 |
| **[PowerPoint Skill](https://github.com/Noi1r/powerpoint-skill)**†<br><sub>Noi1r</sub> | 104 | PPTX | MIT | 生成包含原生数学公式、LaTeX和Graphviz/Mermaid/TikZ图表的PPTX演示文稿。 |
| **[Make Slide](https://github.com/Kuneosu/make-slide)**†<br><sub>Kuneosu</sub> | 104 | HTML | MIT | 根据提示生成独立的HTML幻灯片文件。 |
| **[AI Skills (Cross-Platform)](https://github.com/sanjay3290/ai-skills/tree/main/skills/google-slides)**†<br><sub>sanjay3290</sub> | 359* | 套件 | Apache-2.0 | 面向 Claude Code、Cursor 与 Codex 的 24 个跨平台技能，含 Google Slides。 |

### Tier B — 垂直与新兴（<100 star）

| 项目 | ⭐ | 路线 | License | 一句话 |
|---|---:|---|---|---|
| **[PPT Report Skills](https://github.com/myunwang/ppt-report-skills)**†<br><sub>myunwang</sub> | 96 | HTML | MIT | 构建带有ECharts图表、按幻灯片分文件存储、支持PDF/图片导出的网页汇报文稿。 |
| **[AI Paper to Slide Skill](https://github.com/Leo1998-Lu/ai-paper2slide-skill)**†<br><sub>Leo1998-Lu</sub> | 95 | PPTX | MIT | 将AI研究论文转换为会议级别的PowerPoint幻灯片。 |
| **[Literature Report PPT Builder](https://github.com/fangyuanopus/literature-report-ppt-builder)**†<br><sub>fangyuanopus</sub> | 91 | PPTX | MIT | 根据研究内容生成学术文献报告PowerPoint幻灯片。 |
| **[Image to PPTX Skill](https://github.com/knight6669/knight-imagetopptx-skill)**†<br><sub>knight6669</sub> | 84 | PPTX | MIT | 通过语义理解将幻灯片图片转换为可编辑的PowerPoint文件。 |
| **[Visual Cognition Slides](https://github.com/edu-ai-builders/visual-cognition-slides)**<br><sub>edu-ai-builders</sub> | 81 | HTML | MIT | 基于认知科学与教学设计的幻灯片，优化知识留存率。 |
| **[CN Academic Spark](https://github.com/wycmochi/cn-academic-spark)**†<br><sub>wycmochi</sub> | 78 | PPTX | MIT | 根据上传的论文材料，为论文答辩、组会汇报等场景生成带讲稿的可编辑学术PPTX。 |
| **[Knowledge Cat PPT Skill](https://github.com/gnipbao/knowledge-cat-ppt-skill)**†<br><sub>gnipbao</sub> | 77 | 双路线 | MIT | 采用故事优先的方式创建并质检PPT、HTML和图片型演示文稿。 |
| **[SJTU PPT Template Skill](https://github.com/ACTAshui/sjtu-ppt-template-skill)**†<br><sub>ACTAshui</sub> | 74 | PPTX | Unspecified | 生成上海交通大学风格的可编辑PowerPoint幻灯片。 |
| **[Deck Factory](https://github.com/gongnyang/deck-factory)**†<br><sub>gongnyang</sub> | 72 | HTML | MIT | 将一行提示词转化为暗色编辑风格的HTML演示文稿。 |
| **[HTML Slides](https://github.com/bluedusk/html-slides)**<br><sub>bluedusk</sub> | 70 | HTML | MIT | 带演讲者备注的 HTML 幻灯片，配套放映 app。 |
| **[Space Multi Design PPT](https://github.com/SpaceZephyr/space-multi-design-ppt)**†<br><sub>SpaceZephyr</sub> | 66 | PPTX | Unspecified | 通过Codex按照设计系统规范生成品牌化幻灯片。 |
| **[Lieflat HTML Design](https://github.com/larashero3-dotcom/lieflat-html-design)**†<br><sub>larashero3-dotcom</sub> | 63 | HTML | MIT | 通过智能体就绪的设计技能生成HTML幻灯片和小红书卡片。 |
| **[Jiarui SVG Skills](https://github.com/shenxiaofeng-pro/jiarui-svg-skills)**†<br><sub>shenxiaofeng-pro</sub> | 60 | 图片 | Unspecified | 生成带有公司Logo、主色调和逻辑结构的品牌SVG幻灯片图片，可拆分用于PPT。 |
| **[Awesome PPT Skills](https://github.com/stevenjinlong/awesome-ppt-skills)**†<br><sub>stevenjinlong</sub> | 57 | 图片 | Unspecified | 通过gpt-image-2将文字提示词转换为完整的全页式PPT幻灯片图片。 |
| **[Editable Image to PPT Skill](https://github.com/soulmujoco/EditableImage2PPTSkill)**†<br><sub>soulmujoco</sub> | 57 | PPTX | MIT | 将PPT幻灯片图片转换为可编辑的PowerPoint文件。 |
| **[KingDee PPT Skill](https://github.com/WayneZhon/KingDee-PPT-Skill)**<br><sub>WayneZhon</sub> | 56 | HTML | MIT | 将内容快速生成金蝶风格 PPT。 |
| **[Presentation](https://github.com/appautomaton/presentation)**†<br><sub>appautomaton</sub> | 53 | 双路线 | Unspecified | 通过四个可组合技能将业务问题转化为咨询级PDF和PPTX演示文稿。 |
| **[Huawei Style PPT Skill](https://github.com/zuiho-kai/huawei-style-ppt-skill)**<br><sub>zuiho-kai</sub> | 52 | HTML | Custom | 华为风格高密度信息 PPT 制作工作流。 |
| **[Slide Creator](https://github.com/kaisersong/slide-creator)**<br><sub>kaisersong</sub> | 46 | 双路线 | Unspecified | AI 规划 + 风格发现 + PPTX 导出。 |
| **[next-slide](https://github.com/codesstar/next-slide)**<br><sub>codesstar</sub> | 43 | HTML | MIT | 「你的下个 slide，何必是 PPT」—— 26+ 风格，零依赖，中英双语。 |
| **[HTML to Editable PPTX](https://github.com/Hasasasa/html-to-editable-pptx)**†<br><sub>Hasasasa</sub> | 43 | PPTX | MIT | 将HTML幻灯片转换为包含原生文字框（而非截图）的可编辑PPTX文件。 |
| **[Slide Writer](https://github.com/FeeiCN/slide-writer)**<br><sub>FeeiCN</sub> | 40 | HTML | MIT | 从想法、大纲、文档或演讲稿生成企业级 HTML 演示。 |
| **[Claude Code Codex Slide](https://github.com/phodal/claude-code-codex-slide)**†<br><sub>phodal</sub> | 39 | HTML | Unspecified | 通过Codex分析Claude Code源码，并以GPT生成的幻灯片呈现分析结果。 |
| **[Baoyu Xuanyi Skills](https://github.com/xuanxuan1983/baoyu-xuanyi-skills)**†<br><sub>xuanxuan1983</sub> | 39 | 模板库 | Unspecified | 将宝玉的智能体技能与七种PPT风格模板相结合。 |
| **[Beautiful Hackathon Slides](https://github.com/Esther2524/beautiful-hackathon-slides)**†<br><sub>Esther2524</sub> | 38 | HTML | MIT | 生成适合黑客松展示的大胆设计HTML宣传幻灯片。 |
| **[ImageGen PPTX Pipeline](https://github.com/eddyzzl/imagegen-pptx-pipeline)**†<br><sub>eddyzzl</sub> | 37 | PPTX | MIT | 使用图像生成技术生成可编辑PPTX幻灯片，并将幻灯片图片严格转换为PowerPoint。 |
| **[Paper PPT Skill](https://github.com/xiao634zhang/paper-ppt-skill)**†<br><sub>xiao634zhang</sub> | 35 | PPTX | Unspecified | 从PDF论文自动生成简洁的学术汇报幻灯片，支持模板定制、演讲稿导入和图片提取。 |
| **[Presentation Skill](https://github.com/siril9/presentation-skill)**†<br><sub>siril9</sub> | 34 | PPTX | MIT | 以源文件优先方式通过Codex生成可编辑PPTX幻灯片，含样式路由和质量审核。 |
| **[Codex Image to Editable PPT](https://github.com/wiltonesten-web/codeximage-to-editable-ppt-v1)**†<br><sub>wiltonesten-web</sub> | 34 | PPTX | MIT | 通过Codex将图片型PPT幻灯片重建为可编辑的PowerPoint文件。 |
| **[Slidev Skills](https://github.com/yoanbernabeu/slidev-skills)**†<br><sub>yoanbernabeu</sub> | 33 | 框架 | MIT | 二十个用于通过Slidev框架构建演示文稿的AI智能体技能。 |
| **[PPT Skill](https://github.com/AIPMAndy/PPTskill)**†<br><sub>AIPMAndy</sub> | 33 | PPTX | MIT | 无需设计技能，通过AI生成原生可编辑的PowerPoint文件。 |
| **[BL Captain PPT Skill](https://github.com/dososo/blcaptain-ppt-skill)**†<br><sub>dososo</sub> | 31 | HTML | NOASSERTION | 生成带有7种设计体系视觉风格、符合WCAG规范的单文件HTML演示文稿。 |
| **[HTML to PPT PDF](https://github.com/wangzan101/html-to-ppt-pdf)**†<br><sub>wangzan101</sub> | 31 | 双路线 | MIT | 将HTML幻灯片转换为PDF和图片型PPTX，供线下演讲使用。 |
| **[Skills Slides](https://github.com/nghiahsgs/skills-slides)**<br><sub>nghiahsgs</sub> | 29 | HTML | Unspecified | 50 美学 × 20 配色 × 10 字体 × 5 布局 × 30+ 特效 = 5 万种组合。 |
| **[Slides AI Plugin](https://github.com/proyecto26/slides-ai-plugin)**†<br><sub>proyecto26</sub> | 29 | 双路线 | MIT | 将单个提示词转化为动态HTML或可编辑PowerPoint演示文稿。 |
| **[Scholar PPT CN](https://github.com/deathcats4/scholar-ppt-cn)**†<br><sub>deathcats4</sub> | 28 | PPTX | MIT | 通过Codex将学术论文转换为带规划表和布局草图的可编辑PowerPoint幻灯片。 |
| **[PowerPoint Fancy Design](https://github.com/Phlegonlabs/Powerpoint-fancy-design)**<br><sub>Phlegonlabs</sub> | 27 | 双路线 | Unspecified | 结构化 Markdown → 1600×900 HTML 幻灯片 + PNG 渲染 + 可导出。 |
| **[Narrative Engine](https://github.com/nraford7/Narrative-Engine)**†<br><sub>nraford7</sub> | 27 | HTML | Unspecified | 将内容转化为基于叙事与沟通框架构建的HTML幻灯片。 |
| **[Image PPT King](https://github.com/TateZhouSiu/image-ppt-king)**†<br><sub>TateZhouSiu</sub> | 27 | PPTX | MIT | 将幻灯片截图和生成图片通过OCR识别和质检转换为可编辑的PPTX文件。 |
| **[PPT Design DNA](https://github.com/dakjdakd/PPT-Design-DNA)**†<br><sub>dakjdakd</sub> | 26 | HTML | Apache-2.0 | 从参考图片中提取视觉风格并保存为设计档案，再将其应用于HTML演示文稿。 |
| **[PPT Creator Skills](https://github.com/Yu-0312/ppt-creater-skills)**†<br><sub>Yu-0312</sub> | 25 | PPTX | NOASSERTION | 用于Claude Code的PowerPoint演示文稿创建技能。 |
| **[Beamer Skill](https://github.com/JaxonJP/beamer-skill)**†<br><sub>JaxonJP</sub> | 23 | HTML | MIT | 面向学术Beamer LaTeX演示文稿的全流程技能：编译、审阅、质检和TikZ审计。 |
| **[Jingge Sense Deck](https://github.com/jxshow/Jingge-PPT-sense-deck-skill)**†<br><sub>jxshow</sub> | 23 | HTML | Unspecified | 注重整套幻灯片视觉调性一致的 HTML deck 技能。 |
| **[Presentation Skill](https://github.com/OrangeViolin/presentation-skill)**†<br><sub>OrangeViolin</sub> | 22 | HTML | Unspecified | 输入主题，从62种品牌设计风格中生成可播放的HTML幻灯片。 |
| **[Econ Empirical Paper PPT Skill](https://github.com/1793065778/econ-empirical-paper-ppt-skill)**†<br><sub>1793065778</sub> | 22 | PPTX | Unspecified | 将实证经济学论文转换为适合PowerPoint使用的结构化演示文稿蓝图。 |
| **[HTML to PPTX](https://github.com/Emily27-alt/html-to-pptx)**†<br><sub>Emily27-alt</sub> | 20 | PPTX | MIT | 将HTML幻灯片转换为使用原生形状（而非截图）的可编辑.pptx文件。 |
| **[Neon Slides](https://github.com/lqshow/neon-slides)**†<br><sub>lqshow</sub> | 20 | HTML | MIT | 将文本大纲转换为适合技术演示的暗色霓虹主题HTML幻灯片。 |
| **[Claude HTML Slide Builder](https://github.com/mathruffian-dot/claude-html-slide-builder)**†<br><sub>mathruffian-dot</sub> | 20 | HTML | MIT | 将教材转换为AI互动式Reveal.js HTML演示文稿，并一键部署到GitHub Pages。 |
| **[30x McKinsey Research Deck](https://github.com/norahe0304-art/30x-mckinsey-research-deck)**†<br><sub>norahe0304-art</sub> | 20 | PPTX | MIT | 通过多智能体流水线，将研究提示词转化为经过对抗验证的麦肯锡风格市场研究幻灯片。 |
| **[Keynote Slides Skill](https://github.com/dbmcco/keynote-slides-skill)**†<br><sub>dbmcco</sub> | 19 | HTML | Unspecified | 生成 Keynote 风格的 HTML 演示幻灯片。 |
| **[PPT Agent](https://github.com/joker-sxj/ppt-agent)**†<br><sub>joker-sxj</sub> | 19 | 双路线 | MIT | 通过六阶段流水线，将主题转化为可逐元素编辑的 .pptx 文件及整页 SVG 网页预览。 |
| **[Interactive Slides](https://github.com/sylvial928/interactive-slides)**†<br><sub>sylvial928</sub> | 18 | HTML | MIT | 生成带有风格预设、品牌套件支持和一键导出 PowerPoint 功能的动画交互式网页演示文稿。 |
| **[PPTX Template Skills](https://github.com/CxyZyr/PPTX-Template-Skills)**†<br><sub>CxyZyr</sub> | 17 | PPTX | MIT | 将 PowerPoint 模板解析为机器可读的结构描述，再用新内容填充，生成完整的演示文稿。 |
| **[KAI Presentation](https://github.com/yevvonlim/kai-presentation)**†<br><sub>yevvonlim</sub> | 16 | HTML | Unspecified | 根据提示生成 KAI 品牌风格的 HTML 演示文稿。 |
| **[AI Draw Skill](https://github.com/stone-yu/ai-draw-skill)**†<br><sub>stone-yu</sub> | 15 | HTML | Unspecified | 将文字、链接、图片或 PDF 转换为 HTML 幻灯片或图表，提供 36 种 PPT 主题和 12 种图表主题。 |
| **[Keynot](https://github.com/shawnzam/keynot)**†<br><sub>shawnzam</sub> | 15 | HTML | MIT | 无需 Keynote 或 PowerPoint，将任意提示词转换为独立的 HTML 幻灯片。 |
| **[MBB Decks](https://github.com/floflo11/mbb-decks)**†<br><sub>floflo11</sub> | 15 | PPTX | MIT | 生成 MBB 风格的咨询 .pptx 文件，包含行动标题、MECE 要点和公司 Logo 项目符号。 |
| **[Slide Wright](https://github.com/arifszn/slide-wright)**†<br><sub>arifszn</sub> | 14 | HTML | MIT | 为每个提示生成具有独特设计的 reveal.js HTML 幻灯片。 |
| **[CyberBin PPT Skill](https://github.com/caikankan/cyberbin-ppt-skill)**†<br><sub>caikankan</sub> | 14 | HTML | ⚠️ AGPL-3.0 | 根据提示在本地生成 HTML 幻灯片。 |
| **[Competition PPT Template Skill](https://github.com/che626/competition-ppt-template-first-skill)**†<br><sub>che626</sub> | 13 | PPTX | MIT | 使用模板优先方式生成含真实证据的可编辑竞赛与答辩 PPTX 演示文稿。 |
| **[Four-Up PPT Generator](https://github.com/woniuniuniu/four-up-ppt-generator)**†<br><sub>woniuniuniu</sub> | 13 | PPTX | ⚠️ AGPL-3.0 | 基于 guizang-ppt-skill 生成每页四格布局的 PPTX 演示文稿。 |
| **[NanoBanana PPT Skills](https://github.com/xj-bear/NanoBanana-PPT-Skills)**†<br><sub>xj-bear</sub> | 13 | PPTX | Unspecified | 使用 AI 生成 PPT 文件，支持 Veo 视频内容。 |
| **[NanoBanana PPT Skills](https://github.com/girish6055/NanoBanana-PPT-Skills)**†<br><sub>girish6055</sub> | 13 | PPTX | Unspecified | 使用 AI 生成带有智能切换和交互式播放功能的 PPT 文件。 |
| **[PPT Image Share Builder](https://github.com/uuoov/ppt-image-share-builder)**†<br><sub>uuoov</sub> | 13 | 图片 | MIT | 从图片输入生成 PPT 页面图像、质检联系表、PPTX 封装文件和时序脚本。 |
| **[HalfAI Gufa PPT](https://github.com/HalfAI1102/HalfAI-gufappt)**†<br><sub>HalfAI1102</sub> | 12 | PPTX | MIT | 生成适合学校、职场和答辩场景的传统风格可编辑 PPTX 文件。 |
| **[Slide Design Skill](https://github.com/SlideSpeak/slide-design-skill)**†<br><sub>SlideSpeak</sub> | 12 | HTML | MIT | 根据演示文稿描述生成带有定制样式、真实图表、表格和图片的 1920x1080 HTML 幻灯片。 |
| **[Better PPT HTML Deck](https://github.com/ziguishian/better-ppt-html-deck)**†<br><sub>ziguishian</sub> | 12 | HTML | MIT | 先确认视觉方向，再生成可编辑、可预览、可导出的 HTML 演示文稿。 |
| **[Create HTML Deck](https://github.com/awesome-skills/create-html-deck)**†<br><sub>awesome-skills</sub> | 12 | HTML | MIT | 构建并验证适用于笔记本电脑和投影仪的原生浏览器 HTML 演示文稿。 |
| **[AWS HTML Slides](https://github.com/lanceli93/aws-html-slides)**†<br><sub>lanceli93</sub> | 11 | HTML | MIT | 从头创建富含动画效果的 HTML 演示文稿，或将现有 PowerPoint 文件转换为 HTML 格式。 |
| **[Prada Slides](https://github.com/prodigeproject/pradaslides)**†<br><sub>prodigeproject</sub> | 11 | 双路线 | MIT | 生成 PPTX、HTML 幻灯片和 PDF，并针对目标受众进行演示文稿规划。 |
| **[Japanese Corporate PPTX Skill](https://github.com/gonta223/japanese-corporate-pptx-skill)**†<br><sub>gonta223</sub> | 11 | PPTX | MIT | 生成日式企业风格的 PPTX 演示文稿。 |
| **[Editable Leadership PPTX](https://github.com/CamelKing1997/editable-leadership-pptx)**†<br><sub>CamelKing1997</sub> | 11 | PPTX | Apache-2.0 | 构建带有仓库证据支撑和截图质检的可编辑领导力、高管及项目汇报 PPTX 幻灯片。 |
| **[SlideStage Pack](https://github.com/SlideStage/slidestage-pack)**†<br><sub>SlideStage</sub> | 10 | HTML | Unspecified | 将 HTML 幻灯片打包为可分享或部署的发布包。 |
| **[Deckset Claude Skill](https://github.com/doudou1337/deckset-claude-skill)**†<br><sub>doudou1337</sub> | 10 | HTML | MIT | 接受 Markdown 输入，生成包含文档和示例的 Deckset 演示文稿文件。 |
| **[McKinsey HTML Design Skill](https://github.com/likaku/mck-html-design-skill)**†<br><sub>likaku</sub> | 10 | HTML | Apache-2.0 | 用 Python 生成麦肯锡风格的 HTML 演示文稿，内置 68 种布局，无需任何依赖。 |
| **[PPTX from Layouts](https://github.com/tristan-mcinnis/pptx-from-layouts-skill)**<br><sub>tristan-mcinnis</sub> | 9 | PPTX | MIT | 严格通过模板母版版式，从 Markdown 生成 PPTX。 |
| **[IML PPTX](https://github.com/tangonho/iml-pptx)**†<br><sub>tangonho</sub> | 9 | PPTX | Unspecified | 将文案和幻灯片图像重建为包含原生文本框与形状的可编辑 PowerPoint 文件。 |
| **[GZR NSFC PPT Skill](https://github.com/admithuman/gzr-nsfc-ppt-skill)**†<br><sub>admithuman</sub> | 9 | PPTX | MIT | 自动生成符合国家自然科学基金答辩风格的专业学术演示文稿。 |
| **[HTML to PPTX Skill](https://github.com/artifact-kit/html-to-pptx-skill)**†<br><sub>artifact-kit</sub> | 8 | PPTX | Unspecified | 将 HTML 页面转换为可下载、可编辑的 PowerPoint 演示文稿。 |
| **[Bento PPT Skill](https://github.com/YingYveltal/bento-ppt-skill)**†<br><sub>YingYveltal</sub> | 8 | 双路线 | MIT | 将主题转换为 16:9 Bento Grid 风格的 SVG 幻灯片，提供 HTML 预览和可编辑的 PowerPoint 导出。 |
| **[SlideSmith](https://github.com/aryankumawat/SlideSmith-Multi-Agent-AI-Slide-Maker-)**†<br><sub>aryankumawat</sub> | 8 | 双路线 | Unspecified | 多智能体系统，通过质量校验自动生成幻灯片并支持多格式导出。 |
| **[Fudan University PPT Skill](https://github.com/JZCreative/Fudan-University-PPT-skill)**†<br><sub>JZCreative</sub> | 8 | 双路线 | Unspecified | 生成带有复旦大学品牌标识的学术演示文稿，支持原生 PPTX 和离线 HTML 格式，内置校徽与配色资产。 |
| **[Presentation Chef](https://github.com/sacredvoid/presentation-chef)**†<br><sub>sacredvoid</sub> | 8 | HTML | MIT | 将任意内容转换为苹果 Keynote 风格的单文件 HTML 演示文稿，带有电影级动画效果。 |
| **[Paper Figure PPTX Skill](https://github.com/fengting124/paper-figure-pptx-skill)**†<br><sub>fengting124</sub> | 8 | PPTX | MIT | 将学术论文中的图表重建为可编辑且经 LibreOffice 验证的 PPTX 幻灯片。 |
| **[AI Editable PPT Skill](https://github.com/iwbaga724-Hinda/ai-editable-ppt-skill)**†<br><sub>iwbaga724-Hinda</sub> | 7 | PPTX | Unspecified | 根据报告、大纲、模板或 AI 生成的幻灯片图像创建可编辑的 PowerPoint 演示文稿。 |
| **[Hand-Drawn PPT Skill](https://github.com/danny0926/ppt-skills)**†<br><sub>danny0926</sub> | 7 | 双路线 | Unspecified | 将文本转换为手绘风格（rough.js）的 PPTX 幻灯片，采用视觉优先布局和双层可编辑结构。 |
| **[Guizang PPT Skill](https://github.com/alingowangxr/guizang-ppt-skill)**†<br><sub>alingowangxr</sub> | 7 | HTML | MIT | 生成网页版演示文稿、配图及常用社交平台封面，支持繁体中文和简体中文。 |
| **[TalkTrack](https://github.com/RuiqiWang-LGD/TalkTrack--)**†<br><sub>RuiqiWang-LGD</sub> | 7 | PPTX | Unspecified | 将 PDF、PPT 或图片方案转换为带可朗读稿和翻页提示的伴读幻灯片。 |
| **[HTML PPT Skill](https://github.com/chenyangji666/html-ppt-skill)**†<br><sub>chenyangji666</sub> | 7 | 框架 | MIT | 基于纯 HTML/CSS/JS 的演示文稿引擎，附带 AI 生成协议，用于创建幻灯片。 |
| **[HTML to PPTX](https://github.com/nlj626/html-to-pptx)**†<br><sub>nlj626</sub> | 7 | PPTX | MIT | 将 html-ppt 生成的 HTML 演示文稿一键转换为可下载的 PPTX 文件。 |
| **[PPT Expert Team](https://github.com/ThunderOne18/ppt-expert-team)**†<br><sub>ThunderOne18</sub> | 7 | 双路线 | NOASSERTION | 八步工作流技能，将文章或讲稿转换为可编辑的 HTML、图片或 PPTX 幻灯片，提供六种风格。 |
| **[Vela Slides](https://github.com/AgentiaPT/vela-slides)**†<br><sub>AgentiaPT</sub> | 7 | HTML | NOASSERTION | 一款 AI 驱动的应用与 Agent 技能，用于生成 HTML 幻灯片演示文稿。 |
| **[Paper to LaTeX PPT](https://github.com/moyoo0/paper-to-latex-ppt)**†<br><sub>moyoo0</sub> | 7 | HTML | MIT | 输入一篇论文，输出带讲稿的汇报幻灯片，适用于组会展示。 |
| **[SOIL Deck Skills](https://github.com/mathruffian-dot/soil-deck-skills)**†<br><sub>mathruffian-dot</sub> | 7 | 双路线 | MIT | 通过 Agent 技能生成教学幻灯片，支持全图 PPTX、可编辑 PPTX 和互动 HTML 三种格式。 |
| **[PPT Master](https://github.com/Categorytyy/ppt-master)**†<br><sub>Categorytyy</sub> | 6 | HTML | MIT | 用于生成 HTML 幻灯片演示文稿的 Agent 技能。 |
| **[PPT Image to Editable](https://github.com/L-Luke-L/ppt-image-to-editable)**†<br><sub>L-Luke-L</sub> | 6 | PPTX | Unspecified | 一个 Codex 技能，将 AI 生成的幻灯片图片拆分并重建为可编辑的 PPTX 文件。 |
| **[Modern PPT](https://github.com/lainshao/modern-ppt)**†<br><sub>lainshao</sub> | 6 | HTML | ⚠️ AGPL-3.0 | 生成包含 12 种布局、3 种主题和交互图表的单文件 HTML 演示文稿，兼容主流 AI 编程工具。 |
| **[Bruce PPTX Generator](https://github.com/bruc3van/bruce-pptx-generator)**†<br><sub>bruc3van</sub> | 5 | PPTX | Unspecified | 一个 Agent 技能，根据用户需求通过代码从零生成专业级 PowerPoint 演示文稿。 |
| **[PPT Skill](https://github.com/lgwanai/ppt-skill)**†<br><sub>lgwanai</sub> | 5 | HTML | Unspecified | 支持风格克隆、内置商用 SVG 素材和专家排版经验，生成高质量 HTML 幻灯片。 |
| **[Xidian Slides Skill](https://github.com/perper999/xidian-slides-skill)**†<br><sub>perper999</sub> | 5 | HTML | Unspecified | 按照西安电子科技大学官方视觉规范生成无依赖的 HTML 演示文稿。 |
| **[Presentation Forge](https://github.com/thmsgo18/presentation-forge)**†<br><sub>thmsgo18</sub> | 5 | HTML | MIT | 生成自包含的 HTML 幻灯片，并可从 PowerPoint 文件、图片或文字描述中导入品牌主题。 |
| **[Tekion Slide Generator](https://github.com/rsensui2/tekion-slide-generator)**†<br><sub>rsensui2</sub> | 5 | 双路线 | MIT | 使用 OpenAI 或 Gemini 图像生成，将 Markdown 转换为 16:9 2K 幻灯片并导出为 PPTX 或 PDF。 |
| **[Paper to Slides Skill](https://github.com/inhyeoklee/paper2slides-skill)**†<br><sub>inhyeoklee</sub> | 5 | HTML | MIT | 读取学术论文 PDF，生成对应的演示幻灯片。 |
| **[PPT Skills](https://github.com/CacinieP/ppt-skills)**†<br><sub>CacinieP</sub> | 5 | PPTX | MIT | 通过 PptxGenJS 生成支持中日韩字符的带主题可编辑 PPTX 文件。 |
| **[Editable PPTX Skill](https://github.com/Liuguanyi2125/editable-pptx-skill)**†<br><sub>Liuguanyi2125</sub> | 5 | PPTX | MIT | 通过 Claude Code 或 Codex 技能包生成分层、完全可编辑的 PowerPoint 文件。 |
| **[Pitch Deck Iterator](https://github.com/MiraclePlus/pre-pp)**†<br><sub>MiraclePlus</sub> | 5 | PPTX | Unspecified | 通过 Claude Code 技能工作流对路演 PPT 进行迭代优化。 |
| **[Zhongguose PPT Skill](https://github.com/tanglele110-hash/zhongguose-ppt-skill)**†<br><sub>tanglele110-hash</sub> | 5 | PPTX | MIT | 使用中国传统配色方案生成演示幻灯片。 |
| **[ZJ Lab Academic PPTX Skills](https://github.com/qianmo-qp/zjlab-academic-pptx-sklls)**†<br><sub>qianmo-qp</sub> | 5 | PPTX | Unspecified | 生成用于实验室技术或学术汇报的 PPTX 幻灯片。 |
| **[Research Group PPT Skill](https://github.com/lirouroud/research-group-ppt-skill)**†<br><sub>lirouroud</sub> | 5 | HTML | Unspecified | 读取科研进展素材，先输出逐页大纲供确认，再生成可翻页的 HTML 汇报。 |
| **[Paper to Scholar Slides](https://github.com/ficooooo/Paper2ScholarSlides)**†<br><sub>ficooooo</sub> | 5 | PPTX | MIT | 将综述初稿与论文素材转化为结构严谨、引用清晰、图表可解释的学术 PPTX 汇报。 |
| **[Consulting Diagnosis PPT Skill](https://github.com/Carl-Marks/consulting-diagnosis-ppt-skill)**†<br><sub>Carl-Marks</sub> | 5 | HTML | Unspecified | 经过六个阶段，从原始输入经业务分析最终生成咨询诊断报告的 HTML 幻灯片。 |
| **[Token Slides](https://github.com/pku-lemonade/TokenSlides)**†<br><sub>pku-lemonade</sub> | 5 | 框架 | Apache-2.0 | 基于 Typst 的幻灯片主题，配合 Codex 技能将学术论文转换为演示文稿。 |
| **[Aham PPT](https://github.com/Aham-AIAPP/aham-ppt)**†<br><sub>Aham-AIAPP</sub> | 4 | PPTX | MIT | 克制的 AI PPT 制作技能，通过参数化版式库生成规范、可编辑的 .pptx 文件。 |
| **[Notrat PPT Studio](https://github.com/NestMold/notrat-ppt-studio-skill)**†<br><sub>NestMold</sub> | 4 | 双路线 | MIT | 使用 Notrat 创建、改编和检查 PowerPoint 文件，支持图片型、原生可编辑型和混合型输出及动画效果。 |
| **[Web PPT](https://github.com/includewudi/web-ppt)**†<br><sub>includewudi</sub> | 4 | HTML | Unspecified | 生成零依赖的 HTML 演示文稿，可在浏览器直接打开，支持视频录制。 |
| **[Codex XKPPT Skill](https://github.com/MURMURE11118586/codex-xkppt-skill)**†<br><sub>MURMURE11118586</sub> | 4 | PPTX | MIT | 支持从主题、文档、PDF 或 Markdown 生成可编辑演示文稿，提供模板套用、单页修改和 QA 检查流程。 |
| **[High Quality Slides](https://github.com/andyqiu847-ai/high-quality-slides)**†<br><sub>andyqiu847-ai</sub> | 4 | HTML | MIT | 采用研究优先、叙事驱动的五阶段工作流，生成精致的 HTML 演示文稿。 |
| **[PPT Design Skill](https://github.com/billLiao/PPT-Design-Skill)**†<br><sub>billLiao</sub> | 4 | PPTX | Unspecified | 融合多种 PPT 设计风格，直接生成 .pptx 文件而非 HTML。 |
| **[PowerPoint Skill](https://github.com/Shimonimposed141/powerpoint-skill)**†<br><sub>Shimonimposed141</sub> | 4 | PPTX | MIT | 将学术论文转换为支持原生数学公式和图表的 PowerPoint 演示文稿，包含多阶段内容分析。 |
| **[Slide Weaver](https://github.com/RFYoung/slideweaver)**†<br><sub>RFYoung</sub> | 4 | PPTX | MIT | 经过多轮大模型调试打磨，可端到端半自动生成学术汇报 PPT。 |
| **[Competition PPT Skill](https://github.com/2750527986liu-maker/competition-ppt-skill)**†<br><sub>2750527986liu-maker</sub> | 4 | PPTX | Unspecified | 基于 python-pptx 与 PIL，自动生成中国国际大学生创新大赛路演 PPT。 |
| **[HFUT Presentation Studio](https://github.com/linmohan00-rgb/hfut-presentation-studio)**†<br><sub>linmohan00-rgb</sub> | 4 | PPTX | Unspecified | 根据课程主题、截图或原始素材制作合肥工业大学红白风格课堂汇报 PPT，并检查排版与演讲稿。 |
| **[SJTU Beamer PPT](https://github.com/YarthsA/sjtu-beamer-ppt)**†<br><sub>YarthsA</sub> | 4 | HTML | Unspecified | 使用 SJTUBeamer 模板生成符合上海交通大学风格的 LaTeX Beamer 演示文稿。 |
| **[Frontend Slides](https://github.com/dreamid27/frontend-slides)**†<br><sub>dreamid27</sub> | 4 | HTML | MIT | 提供 88 种布局预设和 34 套模板，从头生成或将 PowerPoint 转换为富含动画的独立 HTML 演示文稿。 |
| **[HTML Report Generator](https://github.com/hpuhsp/html-report-generator)**†<br><sub>hpuhsp</sub> | 3 | HTML | Unspecified | 通过实时网络研究生成多风格、有来源引用的专业 HTML 演示文稿，适用于任意主题。 |
| **[Demo Prep Skill](https://github.com/MohamedBIqbal/demo-prep-skill)**†<br><sub>MohamedBIqbal</sub> | 3 | 双路线 | MIT | 为产品演示生成麦肯锡风格的 HTML 或 PowerPoint 演示文稿，并内置计时功能。 |
| **[Avatar PPT Master](https://github.com/sadfrog71/avatar-ppt-master)**†<br><sub>sadfrog71</sub> | 3 | HTML | ⚠️ AGPL-3.0 | 基于 dashi-ppt 二次开发，优化了内容生成逻辑并移除了可能涉及版权问题的图片。 |
| **[Special Achievement Report](https://github.com/xxxd666/special-achievement-report)**†<br><sub>xxxd666</sub> | 3 | HTML | MIT | 通过一个 Claude 技能，运用 9 大方法论生成咨询公司级别的成果汇报。 |
| **[HTML PPT Academic Skill](https://github.com/w1ndys/html-ppt-academic-skill)**†<br><sub>w1ndys</sub> | 3 | HTML | MIT | 为大学生、研究生和教师生成静态 HTML 幻灯片，适用于论文答辩、开题报告和学术演讲等场景。 |
| **[HTML PPT Video Skill](https://github.com/juguang/html-ppt-video-skill)**†<br><sub>juguang</sub> | 3 | HTML | MIT | 将文档转换为带有中文配音和字幕的 HTML 演示视频。 |
| **[PPT Template Fill](https://github.com/xiongwenhao112/ppt-template-fill)**†<br><sub>xiongwenhao112</sub> | 3 | PPTX | MIT | 使用 AI 生成内容填充用户提供的 PPTX 模板，同时保留原有排版布局。 |
| **[AI PPT Skill](https://github.com/skychentian/ai-ppt-skill)**†<br><sub>skychentian</sub> | 3 | 双路线 | Unspecified | 提供 17 种视觉风格，全流程制作演示文稿，支持导出为 HTML 或 PPTX 格式。 |
| **[SVG to PPTX Skill](https://github.com/JamieJustTang/svg2pptx-skill)**†<br><sub>JamieJustTang</sub> | 3 | PPTX | NOASSERTION | 将 AI 生成的 SVG 转换为可完整编辑的原生 PowerPoint 文件，并支持导出为 PDF、Keynote 或 Google Slides。 |
| **[Doc to PPT Skill](https://github.com/reskfa/skill_doc2ppt)**†<br><sub>reskfa</sub> | 3 | 双路线 | MIT | 将 Markdown 或纯文本文档转换为 Claude 原生风格的 HTML 或 PPTX 幻灯片。 |
| **[Economics Empirical PPT Skill](https://github.com/jialiruo-png/economics-empirical-ppt-skill)**†<br><sub>jialiruo-png</sub> | 3 | PPTX | Unspecified | 为经管、金融和实证研究论文生成 PPTX 演示文稿，支持交互式选择页数、字数和风格。 |
| **[SlideSage](https://github.com/vedraut/slidesage)**†<br><sub>vedraut</sub> | 3 | PPTX | MIT | 基于故事叙述和教学设计原则，从内容生成静态 .pptx 演示文稿，兼容任何大语言模型。 |
| **[USTC PPT Template](https://github.com/zsc58/ustc-ppt-template)**†<br><sub>zsc58</sub> | 3 | 模板库 | NOASSERTION | 为中国科学技术大学提供15页蓝色学术PPT模板，含全套跳转导航与LaTeX公式管线。 |
| **[PPTWork](https://github.com/JunfengRan/PPTWork)** | — | PPTX | MIT | 两个 Anthropic 风格技能:从 HTML 规划、写作并导出 PowerPoint 演示文稿。 |
| **[Paper Deck Reveal](https://github.com/O0000-code/paper-deck-reveal)** | — | 框架 | Apache-2.0 | 基于 reveal.js 的技能:把学术论文转为带交互演示的离线可投影幻灯片。 |
| **[Codex Slides](https://github.com/nexu-io/codex-slides)** | — | 框架 | MIT | 面向 Codex 的 AI 幻灯片工作台:图像原生画布、并行渲染、支持 PDF/PPTX 导出。 |
| **[3D HTML Slide Skill](https://github.com/yoshifujidesign/3d-html-slide-skill)**† | — | HTML | MIT | Claude Code 技能:一键生成带 Three.js 线框背景的单文件 HTML 演示幻灯片。 |
| **[University PPT Skill](https://github.com/SiyuQiannn/university-ppt-skill)**<br><sub>SiyuQiannn</sub> | — | 模板库 | NOASSERTION | 以校色 token 与可复用版式库生成可编辑的高校主题 PPTX 演示文稿。 |
| **[Image to Editable PPT Skill (zhoujie97)](https://github.com/zhoujie97/image-to-editable-ppt-skill)**†<br><sub>zhoujie97</sub> | — | PPTX | Unspecified | 把截图与信息图重建为可编辑的 PowerPoint 文本框、原生形状与 SVG 图标。 |
| **[Claude PPT Skills](https://github.com/sunxiaohui2025/claude-ppt-skills)**†<br><sub>sunxiaohui2025</sub> | — | HTML | Unspecified | 生成六种风格的单文件 HTML 横向翻页 PPT,支持网页在线编辑与缩略图总览。 |
| **[Econ Slides Skill](https://github.com/hanlulong/econ-slides-skill)**<br><sub>hanlulong</sub> | — | 框架 | MIT | 把经济学论文转成 Beamer 研讨会报告,并附带按时长排布的逐字讲稿。 |
| **[GHB PPT Skill](https://github.com/NickyLam/GHB-PPT-Skill)**<br><sub>NickyLam</sub> | — | PPTX | MIT | 基于企业模板输出 PPTX,SVG 转为可编辑 DrawingML,默认全离线验证。 |
| **[OpenCode PPT Studio](https://github.com/Honghurumeng/oc_sdk_ppt)**†<br><sub>Honghurumeng</sub> | — | 双路线 | Unspecified | 网页应用:先出大纲初稿,再开新会话精修,然后生成 HTML slides 并本地构建 PPTX。 |
| **[Course HTML Slides Builder](https://github.com/HelenSong/course-html-slides-skill)**†<br><sub>HelenSong</sub> | — | HTML | MIT | 把课程大纲转成多页 HTML 幻灯片,面向课堂投影与互动工作坊设计。 |
| **[Excalidraw Slides Generator](https://github.com/ZunbaRan/excalidraw-slides-skills)**†<br><sub>ZunbaRan</sub> | — | 框架 | Unspecified | 两阶段工作流:把文本转成 16:9 Excalidraw 幻灯片,并自动生成配套 SVG 插图。 |
| **[CUHK Slides Template (HTML)](https://github.com/HarlandZZC/cuhk-slides-template-html)**<br><sub>HarlandZZC</sub> | — | 模板库 | MIT | 一份自包含的港中大配色 HTML 幻灯片模板,附带 Markdown 转幻灯片的 skill。 |
| **[TaoHtml](https://github.com/TaoGEO/TaoHtml)**†<br><sub>TaoGEO</sub> | — | HTML | MIT | 把已有的 Word、PDF 或 PPT 重新设计成带分步动效、可离线交付的 16:9 HTML 演示文稿。 |
| **[Google Slides Deck Skill](https://github.com/eranw2000/google-slides-skill)**<br><sub>eranw2000</sub> | — | 框架 | MIT | 通过 API 重建 Google Slides 演示文稿,并把每页渲染成 PNG 回看以自查结果。 |
| **[Inspiration Deck Workshop](https://github.com/zjsthmjialin/inspiration-deck-workshop)**<br><sub>zjsthmjialin</sub> | — | 模板库 | MIT | 23 套主题与 25 种页面版式,用一个小 CLI 生成带动效的静态 HTML 演示。 |
| **[HTML Presentation Skill](https://github.com/defreitassl/html-presentation-skill)**†<br><sub>defreitassl</sub> | — | HTML | MIT | 把文档、笔记或简报转成独立的 HTML 演示页面,并对结果做校验。 |
| **[PPTX Deck Creation Kit](https://github.com/kimtth/agent-pptify-kit)**†<br><sub>kimtth</sub> | — | PPTX | MIT | 以显式坐标规格生成 PPTX,输出保持原生对象,并以 Copilot 插件形式分发。 |
| **[TikTok Slideshow Command Center](https://github.com/Meliwat/vyral-tiktok-slideshow-skill)**†<br><sub>Meliwat</sub> | — | 图片 | MIT | 规划 TikTok 图文轮播:内容切角、单页设计与发布节奏一次成型。 |
| **[PPT Deck Builder Skill](https://github.com/lk251066/ppt-deck-builder-skill)**†<br><sub>lk251066</sub> | — | 图片 | Unspecified | 逐页生成成品图,只返修出问题的单页,最后统一打包成 PPTX。 |
| **[Starry Slides](https://github.com/StarryKit/starry-slides)**<br><sub>StarryKit</sub> | — | 框架 | Apache-2.0 | 以 HTML 为源文件的幻灯片编辑器,让 Agent 产出的整套 deck 保持完全可编辑。 |
| **[KR Brand Decks](https://github.com/sylvanus4/kr-brand-decks)**<br><sub>sylvanus4</sub> | — | 模板库 | NOASSERTION | 23 个 skill,每个对应一家韩国企业品牌,从零构建符合该品牌规范的 PPTX。 |
| **[Slide Deck Skill](https://github.com/jayworker/slide-deck-skill)**<br><sub>jayworker</sub> | — | HTML | MIT | 单文件 16:9 HTML 演示,浅色仪表盘风格,每页只讲一件事。 |
| **[Marp Slides Studio](https://github.com/unsolublesugar/marp-slides-studio)**<br><sub>unsolublesugar</sub> | — | 模板库 | MIT | 50 套 Marp 主题,配主题画廊、对比度检查与四个面向 Agent 的 deck 制作 skill。 |

### 其他精选列表

| 项目 | ⭐ | 路线 | License | 一句话 |
|---|---:|---|---|---|
| **[awesome-html-slide-skills](https://github.com/ToseaAI/awesome-html-slide-skills)**†<br><sub>ToseaAI</sub> | 104 | 列表 | Custom | HTML 演示 Skill 与模板库精选列表。本仓库的主要线索来源之一。 |
| **[Awesome-PPT-Design-Skills](https://github.com/software-ai-life/Awesome-PPT-Design-Skills)**†<br><sub>software-ai-life</sub> | 71 | 列表 | Unspecified | Agent 无关的高端可编辑 PPT 风格集。 |

<sub>`†` 来自自动发现，只核对了仓库自己写的一句话与协议，没人读过它的 SKILL.md，因此还没有安装命令和能力数据。没有剑标的是人工逐个读过的。<br>`*` monorepo star 数，反映整个仓库而非这一个 skill。`~` 上次刷新失败，为陈旧值。`⚠️` copyleft 协议，商用前请确认。</sub>
<!-- END:REGISTRY -->
---

## 每个到底能做什么

上面的登记册说的是每个项目**是什么**，这里说的是它的文档**声称它能做什么** —— 也就是通常
真正决定选择的那几列。

<!-- BEGIN:CAPABILITIES -->
| 项目 | → PPTX | → PDF | 数据图表 | 代码高亮 | 图示 | 动效 | 演讲备注 | 演讲者模式 | 自定义模板 | 离线可用 |
|---|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| **Anthropic PPTX (official)** | ✅ | ✅ | ✅ | · | · | · | ✅ | · | ✅ | n/a |
| **Slidev** | ✅ | ✅ | · | ✅ | ✅ | ✅ | ✅ | ✅ | · | · |
| **PPT Master** | ✅ | · | ✅ | · | ✅ | ✅ | ✅ | · | ✅ | n/a |
| **Frontend Slides** | · | ✅ | · | · | · | ✅ | · | · | · | · |
| **Baoyu Skills** | ✅ | ✅ | · | · | · | · | · | · | · | · |
| **Guizang PPT Skill** | — | · | · | · | ✅ | ✅ | · | · | — | · |
| **Huashu Design** | ✅ | ✅ | · | · | · | ✅ | ✅ | · | · | · |
| **Quarkdown** | · | ✅ | · | · | ✅ | · | · | · | · | · |
| **Banana Slides** | ✅ | ✅ | · | · | · | · | · | · | · | n/a |
| **Visual Explainer** | · | · | · | · | ✅ | ✅ | · | · | · | ✅ |

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
| `clone` | 克隆进 `~/.claude/skills/`，也就是 Claude Code 找个人 skill 的地方。重开一个会话就能用。 | 30 |
| `plugin` | 两条命令是在 **Claude Code 里面**敲的，不是终端。先加 marketplace，再从里面装。 | 3 |
| `skills-cli` | 跨 agent 的安装器，不止 Claude Code 能用。 | 3 |
| `python` | 需要本机有 Python。克隆下来、装依赖，然后让 agent 在这个目录里干活。 | 2 |
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
> `bold-template-pack/selection-index.json` 里的 slug（共 34 个）。但**本仓库一个 skill 的调用
> 都没有实跑过**，各项目的具体触发词和参数以它自己的 SKILL.md 为准。
> 第四步那句关于预览的描述，是从 frontend-slides 的 SKILL.md 里读到的，只对它成立。

<!-- BEGIN:GALLERY -->
**跳到：**[PPT Master](#gallery-ppt-master) <sub>24</sub> · [Frontend Slides](#gallery-frontend-slides) <sub>24</sub> · [Guizang PPT Skill](#gallery-guizang-ppt-skill) <sub>13</sub> · [Huashu Design](#gallery-huashu-design) <sub>24</sub> · [HTML PPT Studio](#gallery-html-ppt-skill) <sub>24</sub> · [open-slide](#gallery-open-slide) <sub>16</sub> · [Beautiful HTML Templates](#gallery-beautiful-html-templates) <sub>24</sub> · [PPT Agent Workflow San](#gallery-ppt-agent-workflow-san) <sub>10</sub> · [Frontend Slides Editable](#gallery-frontend-slides-editable) <sub>24</sub> · [PPT SVG Generator](#gallery-ppt-svg-generator) <sub>2</sub> · [Mck PPT Design System](#gallery-mck-ppt-design-skill) <sub>6</sub> · [PPT Agent Skill](#gallery-ppt-agent-skill) <sub>24</sub> · [HTML Slides](#gallery-html-slides-bluedusk) <sub>4</sub> · [KingDee PPT Skill](#gallery-kingdee-ppt-skill) <sub>1</sub> · [Slide Creator](#gallery-slide-creator) <sub>23</sub> · [next-slide](#gallery-next-slide) <sub>1</sub> · [Slide Writer](#gallery-slide-writer) <sub>5</sub> · [Skills Slides](#gallery-skills-slides) <sub>4</sub> · [PowerPoint Fancy Design](#gallery-powerpoint-fancy-design) <sub>24</sub> · [PPTX from Layouts](#gallery-pptx-from-layouts) <sub>1</sub> · [PPTWork](#gallery-pptwork) <sub>24</sub> · [Paper Deck Reveal](#gallery-paper-deck-reveal) <sub>22</sub> · [Codex Slides](#gallery-codex-slides) <sub>24</sub> · [3D HTML Slide Skill](#gallery-3d-html-slide-skill) <sub>2</sub> · [University PPT Skill](#gallery-university-ppt-skill) <sub>10</sub> · [Image to Editable PPT Skill (zhoujie97)](#gallery-image-to-editable-ppt-skill-zhoujie97) <sub>4</sub> · [Claude PPT Skills](#gallery-claude-ppt-skills) <sub>3</sub> · [Econ Slides Skill](#gallery-econ-slides-skill) <sub>5</sub> · [GHB PPT Skill](#gallery-ghb-ppt-skill) <sub>1</sub> · [OpenCode PPT Studio](#gallery-oc-sdk-ppt) <sub>3</sub> · [Course HTML Slides Builder](#gallery-course-html-slides-skill) <sub>9</sub> · [Excalidraw Slides Generator](#gallery-excalidraw-slides-skills) <sub>5</sub> · [CUHK Slides Template (HTML)](#gallery-cuhk-slides-template-html) <sub>2</sub> · [TaoHtml](#gallery-taohtml) <sub>12</sub> · [Google Slides Deck Skill](#gallery-google-slides-skill) <sub>1</sub> · [Inspiration Deck Workshop](#gallery-inspiration-deck-workshop) <sub>23</sub> · [HTML Presentation Skill](#gallery-html-presentation-skill) <sub>5</sub> · [PPTX Deck Creation Kit](#gallery-agent-pptify-kit) <sub>3</sub> · [TikTok Slideshow Command Center](#gallery-vyral-tiktok-slideshow-skill) <sub>6</sub> · [PPT Deck Builder Skill](#gallery-ppt-deck-builder-skill) <sub>4</sub> · [KR Brand Decks](#gallery-kr-brand-decks) <sub>24</sub> · [Slide Deck Skill](#gallery-slide-deck-skill) <sub>6</sub> · [Marp Slides Studio](#gallery-marp-slides-studio) <sub>9</sub>

<a id="gallery-ppt-master"></a>

#### [PPT Master](https://github.com/hugohe3/ppt-master) · 41,774 ⭐ · PPTX

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

#### [Frontend Slides](https://github.com/zarazhangrui/frontend-slides) · 26,568 ⭐ · HTML

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

#### [Guizang PPT Skill](https://github.com/op7418/guizang-ppt-skill) · 22,694 ⭐ · HTML

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

#### [Huashu Design](https://github.com/alchaincyf/huashu-design) · 22,190 ⭐ · 双路线

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

#### [HTML PPT Studio](https://github.com/lewislulu/html-ppt-skill) · 7,473 ⭐ · HTML

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

#### [open-slide](https://github.com/1weiho/open-slide) · 6,042 ⭐ · 框架

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

#### [Beautiful HTML Templates](https://github.com/zarazhangrui/beautiful-html-templates) · 3,940 ⭐ · 模板库

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

#### [PPT Agent Workflow San](https://github.com/mucsbr/ppt-agent-workflow-san) · 618 ⭐ · HTML

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

#### [Frontend Slides Editable](https://github.com/archlizheng/frontend-slides-editable) · 446 ⭐ · 双路线

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

#### [Mck PPT Design System](https://github.com/likaku/Mck-ppt-design-skill) · 230 ⭐ · PPTX

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

#### [PPT Agent Skill](https://github.com/Akxan/ppt-agent-skill) · 116 ⭐ · HTML

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

#### [Skills Slides](https://github.com/nghiahsgs/skills-slides) · 29 ⭐ · HTML

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

<a id="gallery-pptwork"></a>

#### [PPTWork](https://github.com/JunfengRan/PPTWork) · — ⭐ · PPTX

<sub>两个 Anthropic 风格技能:从 HTML 规划、写作并导出 PowerPoint 演示文稿。</sub>

<sub>取自 [`JunfengRan/PPTWork`](https://github.com/JunfengRan/PPTWork) 的 28 张图，此处 24 张，靠前的几张是项目自己放在 README 里的</sub>

```bash
git clone https://github.com/JunfengRan/PPTWork && cd PPTWork/ppt && npm install
```

<sub><b>下面出现的风格</b> `showcase` · `showcase-bento` · `showcase-kpi` · `showcase-two-col` · `showcase-export` · `thumbnail` —— 要哪个就在提示里点名。这些是<b>项目自己用的字符串</b>，取自每张图下面链接的文件名与说明，不是本仓库起的名字。</sub>

<img src="https://raw.githubusercontent.com/JunfengRan/PPTWork/c538d921935f96e4f7706af9370f61198b34c5da/examples/showcase/showcase-cover.png" width="100%" alt="PPTWork capabilities cover slide">

<sub><b>PPTWork capabilities cover slide</b> · <code>showcase</code> · 封面 · <a href="https://github.com/JunfengRan/PPTWork/blob/c538d921935f96e4f7706af9370f61198b34c5da/examples/showcase/showcase-cover.png"><code>examples/showcase/showcase-cover.png</code></a></sub>

<img src="https://raw.githubusercontent.com/JunfengRan/PPTWork/c538d921935f96e4f7706af9370f61198b34c5da/examples/showcase/showcase-bento.png" width="100%" alt="Two skills bento layout">

<sub><b>Two skills bento layout</b> · <code>showcase-bento</code> · <a href="https://github.com/JunfengRan/PPTWork/blob/c538d921935f96e4f7706af9370f61198b34c5da/examples/showcase/showcase-bento.png"><code>examples/showcase/showcase-bento.png</code></a></sub>

<img src="https://raw.githubusercontent.com/JunfengRan/PPTWork/c538d921935f96e4f7706af9370f61198b34c5da/examples/showcase/showcase-kpi.png" width="100%" alt="AI agent market KPI row">

<sub><b>AI agent market KPI row</b> · <code>showcase-kpi</code> · <a href="https://github.com/JunfengRan/PPTWork/blob/c538d921935f96e4f7706af9370f61198b34c5da/examples/showcase/showcase-kpi.png"><code>examples/showcase/showcase-kpi.png</code></a></sub>

<img src="https://raw.githubusercontent.com/JunfengRan/PPTWork/c538d921935f96e4f7706af9370f61198b34c5da/examples/showcase/showcase-two-col.png" width="100%" alt="Competitive landscape two-column slide">

<sub><b>Competitive landscape two-column slide</b> · <code>showcase-two-col</code> · <a href="https://github.com/JunfengRan/PPTWork/blob/c538d921935f96e4f7706af9370f61198b34c5da/examples/showcase/showcase-two-col.png"><code>examples/showcase/showcase-two-col.png</code></a></sub>

<img src="https://raw.githubusercontent.com/JunfengRan/PPTWork/c538d921935f96e4f7706af9370f61198b34c5da/examples/showcase/showcase-export.png" width="100%" alt="Four-step CLI workflow">

<sub><b>Four-step CLI workflow</b> · <code>showcase-export</code> · <a href="https://github.com/JunfengRan/PPTWork/blob/c538d921935f96e4f7706af9370f61198b34c5da/examples/showcase/showcase-export.png"><code>examples/showcase/showcase-export.png</code></a></sub>

<img src="https://raw.githubusercontent.com/JunfengRan/PPTWork/c538d921935f96e4f7706af9370f61198b34c5da/examples/ai-agent-landscape-2026/closing/thumbnail.png" width="100%" alt="PPTWork sample">

<sub><b>Thumbnail</b> · <a href="https://github.com/JunfengRan/PPTWork/blob/c538d921935f96e4f7706af9370f61198b34c5da/examples/ai-agent-landscape-2026/closing/thumbnail.png"><code>examples/ai-agent-landscape-2026/closing/thumbnail.png</code></a></sub>

<img src="https://raw.githubusercontent.com/JunfengRan/PPTWork/c538d921935f96e4f7706af9370f61198b34c5da/examples/ai-agent-landscape-2026/cover/thumbnail.png" width="100%" alt="PPTWork sample">

<sub><b>Thumbnail</b> · <a href="https://github.com/JunfengRan/PPTWork/blob/c538d921935f96e4f7706af9370f61198b34c5da/examples/ai-agent-landscape-2026/cover/thumbnail.png"><code>examples/ai-agent-landscape-2026/cover/thumbnail.png</code></a></sub>

<img src="https://raw.githubusercontent.com/JunfengRan/PPTWork/c538d921935f96e4f7706af9370f61198b34c5da/examples/ai-agent-landscape-2026/landscape/thumbnail.png" width="100%" alt="PPTWork sample">

<sub><b>Thumbnail</b> · <a href="https://github.com/JunfengRan/PPTWork/blob/c538d921935f96e4f7706af9370f61198b34c5da/examples/ai-agent-landscape-2026/landscape/thumbnail.png"><code>examples/ai-agent-landscape-2026/landscape/thumbnail.png</code></a></sub>

<img src="https://raw.githubusercontent.com/JunfengRan/PPTWork/c538d921935f96e4f7706af9370f61198b34c5da/examples/ai-agent-landscape-2026/market-size/thumbnail.png" width="100%" alt="PPTWork sample">

<sub><b>Thumbnail</b> · <a href="https://github.com/JunfengRan/PPTWork/blob/c538d921935f96e4f7706af9370f61198b34c5da/examples/ai-agent-landscape-2026/market-size/thumbnail.png"><code>examples/ai-agent-landscape-2026/market-size/thumbnail.png</code></a></sub>

<img src="https://raw.githubusercontent.com/JunfengRan/PPTWork/c538d921935f96e4f7706af9370f61198b34c5da/examples/ai-agent-landscape-2026/problem/thumbnail.png" width="100%" alt="PPTWork sample">

<sub><b>Thumbnail</b> · <a href="https://github.com/JunfengRan/PPTWork/blob/c538d921935f96e4f7706af9370f61198b34c5da/examples/ai-agent-landscape-2026/problem/thumbnail.png"><code>examples/ai-agent-landscape-2026/problem/thumbnail.png</code></a></sub>

<img src="https://raw.githubusercontent.com/JunfengRan/PPTWork/c538d921935f96e4f7706af9370f61198b34c5da/examples/ai-agent-landscape-2026/roadmap/thumbnail.png" width="100%" alt="PPTWork sample">

<sub><b>Thumbnail</b> · <a href="https://github.com/JunfengRan/PPTWork/blob/c538d921935f96e4f7706af9370f61198b34c5da/examples/ai-agent-landscape-2026/roadmap/thumbnail.png"><code>examples/ai-agent-landscape-2026/roadmap/thumbnail.png</code></a></sub>

<img src="https://raw.githubusercontent.com/JunfengRan/PPTWork/c538d921935f96e4f7706af9370f61198b34c5da/examples/ai-agent-landscape-2026/tech-trends/thumbnail.png" width="100%" alt="PPTWork sample">

<sub><b>Thumbnail</b> · <a href="https://github.com/JunfengRan/PPTWork/blob/c538d921935f96e4f7706af9370f61198b34c5da/examples/ai-agent-landscape-2026/tech-trends/thumbnail.png"><code>examples/ai-agent-landscape-2026/tech-trends/thumbnail.png</code></a></sub>

<img src="https://raw.githubusercontent.com/JunfengRan/PPTWork/c538d921935f96e4f7706af9370f61198b34c5da/examples/pptwork-capabilities/p01-cover/thumbnail.png" width="100%" alt="PPTWork sample">

<sub><b>Thumbnail</b> · <a href="https://github.com/JunfengRan/PPTWork/blob/c538d921935f96e4f7706af9370f61198b34c5da/examples/pptwork-capabilities/p01-cover/thumbnail.png"><code>examples/pptwork-capabilities/p01-cover/thumbnail.png</code></a></sub>

<img src="https://raw.githubusercontent.com/JunfengRan/PPTWork/c538d921935f96e4f7706af9370f61198b34c5da/examples/pptwork-capabilities/p03-bento/thumbnail.png" width="100%" alt="PPTWork sample">

<sub><b>Thumbnail</b> · <a href="https://github.com/JunfengRan/PPTWork/blob/c538d921935f96e4f7706af9370f61198b34c5da/examples/pptwork-capabilities/p03-bento/thumbnail.png"><code>examples/pptwork-capabilities/p03-bento/thumbnail.png</code></a></sub>

<img src="https://raw.githubusercontent.com/JunfengRan/PPTWork/c538d921935f96e4f7706af9370f61198b34c5da/examples/pptwork-capabilities/p04-metrics/thumbnail.png" width="100%" alt="PPTWork sample">

<sub><b>Thumbnail</b> · <a href="https://github.com/JunfengRan/PPTWork/blob/c538d921935f96e4f7706af9370f61198b34c5da/examples/pptwork-capabilities/p04-metrics/thumbnail.png"><code>examples/pptwork-capabilities/p04-metrics/thumbnail.png</code></a></sub>

<img src="https://raw.githubusercontent.com/JunfengRan/PPTWork/c538d921935f96e4f7706af9370f61198b34c5da/examples/pptwork-capabilities/p06-workflow/thumbnail.png" width="100%" alt="PPTWork sample">

<sub><b>Thumbnail</b> · <a href="https://github.com/JunfengRan/PPTWork/blob/c538d921935f96e4f7706af9370f61198b34c5da/examples/pptwork-capabilities/p06-workflow/thumbnail.png"><code>examples/pptwork-capabilities/p06-workflow/thumbnail.png</code></a></sub>

<img src="https://raw.githubusercontent.com/JunfengRan/PPTWork/c538d921935f96e4f7706af9370f61198b34c5da/examples/pptwork-capabilities/p07-philosophy/thumbnail.png" width="100%" alt="PPTWork sample">

<sub><b>Thumbnail</b> · <a href="https://github.com/JunfengRan/PPTWork/blob/c538d921935f96e4f7706af9370f61198b34c5da/examples/pptwork-capabilities/p07-philosophy/thumbnail.png"><code>examples/pptwork-capabilities/p07-philosophy/thumbnail.png</code></a></sub>

<img src="https://raw.githubusercontent.com/JunfengRan/PPTWork/c538d921935f96e4f7706af9370f61198b34c5da/examples/pptwork-capabilities/p08-closing/thumbnail.png" width="100%" alt="PPTWork sample">

<sub><b>Thumbnail</b> · <a href="https://github.com/JunfengRan/PPTWork/blob/c538d921935f96e4f7706af9370f61198b34c5da/examples/pptwork-capabilities/p08-closing/thumbnail.png"><code>examples/pptwork-capabilities/p08-closing/thumbnail.png</code></a></sub>

<img src="https://raw.githubusercontent.com/JunfengRan/PPTWork/c538d921935f96e4f7706af9370f61198b34c5da/ppt/assets/claude-warm/_preview/bento-asymmetric/thumbnail.png" width="100%" alt="PPTWork sample">

<sub><b>Thumbnail</b> · <a href="https://github.com/JunfengRan/PPTWork/blob/c538d921935f96e4f7706af9370f61198b34c5da/ppt/assets/claude-warm/_preview/bento-asymmetric/thumbnail.png"><code>ppt/assets/claude-warm/_preview/bento-asymmetric/thumbnail.png</code></a></sub>

<img src="https://raw.githubusercontent.com/JunfengRan/PPTWork/c538d921935f96e4f7706af9370f61198b34c5da/ppt/assets/claude-warm/_preview/cover-editorial/thumbnail.png" width="100%" alt="PPTWork sample">

<sub><b>Thumbnail</b> · <a href="https://github.com/JunfengRan/PPTWork/blob/c538d921935f96e4f7706af9370f61198b34c5da/ppt/assets/claude-warm/_preview/cover-editorial/thumbnail.png"><code>ppt/assets/claude-warm/_preview/cover-editorial/thumbnail.png</code></a></sub>

<img src="https://raw.githubusercontent.com/JunfengRan/PPTWork/c538d921935f96e4f7706af9370f61198b34c5da/ppt/assets/claude-warm/_preview/flow-timeline/thumbnail.png" width="100%" alt="PPTWork sample">

<sub><b>Thumbnail</b> · <a href="https://github.com/JunfengRan/PPTWork/blob/c538d921935f96e4f7706af9370f61198b34c5da/ppt/assets/claude-warm/_preview/flow-timeline/thumbnail.png"><code>ppt/assets/claude-warm/_preview/flow-timeline/thumbnail.png</code></a></sub>

<img src="https://raw.githubusercontent.com/JunfengRan/PPTWork/c538d921935f96e4f7706af9370f61198b34c5da/ppt/assets/claude-warm/_preview/quote-highlight/thumbnail.png" width="100%" alt="PPTWork sample">

<sub><b>Thumbnail</b> · <a href="https://github.com/JunfengRan/PPTWork/blob/c538d921935f96e4f7706af9370f61198b34c5da/ppt/assets/claude-warm/_preview/quote-highlight/thumbnail.png"><code>ppt/assets/claude-warm/_preview/quote-highlight/thumbnail.png</code></a></sub>

<img src="https://raw.githubusercontent.com/JunfengRan/PPTWork/c538d921935f96e4f7706af9370f61198b34c5da/ppt/assets/claude-warm/_preview/section-divider/thumbnail.png" width="100%" alt="PPTWork sample">

<sub><b>Thumbnail</b> · <a href="https://github.com/JunfengRan/PPTWork/blob/c538d921935f96e4f7706af9370f61198b34c5da/ppt/assets/claude-warm/_preview/section-divider/thumbnail.png"><code>ppt/assets/claude-warm/_preview/section-divider/thumbnail.png</code></a></sub>

<img src="https://raw.githubusercontent.com/JunfengRan/PPTWork/c538d921935f96e4f7706af9370f61198b34c5da/ppt/assets/corporate-light/_preview/agenda-grid/thumbnail.png" width="100%" alt="PPTWork sample">

<sub><b>Thumbnail</b> · <a href="https://github.com/JunfengRan/PPTWork/blob/c538d921935f96e4f7706af9370f61198b34c5da/ppt/assets/corporate-light/_preview/agenda-grid/thumbnail.png"><code>ppt/assets/corporate-light/_preview/agenda-grid/thumbnail.png</code></a></sub>

<a id="gallery-paper-deck-reveal"></a>

#### [Paper Deck Reveal](https://github.com/O0000-code/paper-deck-reveal) · — ⭐ · 框架

<sub>基于 reveal.js 的技能:把学术论文转为带交互演示的离线可投影幻灯片。</sub>

<sub>取自 [`O0000-code/paper-deck-reveal`](https://github.com/O0000-code/paper-deck-reveal) 的 22 张图，此处 22 张，靠前的几张是项目自己放在 README 里的</sub>

```bash
git clone https://github.com/O0000-code/paper-deck-reveal && cd paper-deck-reveal
```

<sub><b>下面出现的风格</b> `hero` · `funnel` · `forest` · `interactive` · `speaker` · `presets` · `rstb20200390f02` · `rstb20200390f03` · `rstb20200390f06` · `rstb20200390f04` —— 要哪个就在提示里点名。这些是<b>项目自己用的字符串</b>，取自每张图下面链接的文件名与说明，不是本仓库起的名字。</sub>

<img src="https://raw.githubusercontent.com/O0000-code/paper-deck-reveal/9b1b779f0ffc31e5f5fb726ddc36b1c89a119a46/docs/screenshots/hero.png" width="100%" alt="Cover slide of a journal-club deck: a red hairline rule, a Chinese framing question set above the paper's English title ">

<sub><b>Cover slide of a journal-club deck: a red hairline rule, a Chinese framing question set above the paper's Engl</b> · <code>hero</code> · <a href="https://github.com/O0000-code/paper-deck-reveal/blob/9b1b779f0ffc31e5f5fb726ddc36b1c89a119a46/docs/screenshots/hero.png"><code>docs/screenshots/hero.png</code></a></sub>

<img src="https://raw.githubusercontent.com/O0000-code/paper-deck-reveal/9b1b779f0ffc31e5f5fb726ddc36b1c89a119a46/docs/screenshots/funnel.png" width="100%" alt="Participant funnel slide: recruited N = 976 → excluded −59 → analysed N = 917">

<sub><b>Participant funnel slide: recruited N = 976 → excluded −59 → analysed N = 917</b> · <a href="https://github.com/O0000-code/paper-deck-reveal/blob/9b1b779f0ffc31e5f5fb726ddc36b1c89a119a46/docs/screenshots/funnel.png"><code>docs/screenshots/funnel.png</code></a></sub>

<img src="https://raw.githubusercontent.com/O0000-code/paper-deck-reveal/9b1b779f0ffc31e5f5fb726ddc36b1c89a119a46/docs/screenshots/forest.png" width="100%" alt="Per-language results slide: the paper">

<sub><b>Per-language results slide: the paper</b> · <code>forest</code> · <a href="https://github.com/O0000-code/paper-deck-reveal/blob/9b1b779f0ffc31e5f5fb726ddc36b1c89a119a46/docs/screenshots/forest.png"><code>docs/screenshots/forest.png</code></a></sub>

<img src="https://raw.githubusercontent.com/O0000-code/paper-deck-reveal/9b1b779f0ffc31e5f5fb726ddc36b1c89a119a46/docs/screenshots/interactive.png" width="100%" alt="Interactive slide: the participant">

<sub><b>Interactive slide: the participant</b> · <a href="https://github.com/O0000-code/paper-deck-reveal/blob/9b1b779f0ffc31e5f5fb726ddc36b1c89a119a46/docs/screenshots/interactive.png"><code>docs/screenshots/interactive.png</code></a></sub>

<img src="https://raw.githubusercontent.com/O0000-code/paper-deck-reveal/9b1b779f0ffc31e5f5fb726ddc36b1c89a119a46/docs/screenshots/speaker.png" width="100%" alt="Speaker view: current slide, next slide, timers, and nested speaker notes">

<sub><b>Speaker view: current slide, next slide, timers, and nested speaker notes</b> · <a href="https://github.com/O0000-code/paper-deck-reveal/blob/9b1b779f0ffc31e5f5fb726ddc36b1c89a119a46/docs/screenshots/speaker.png"><code>docs/screenshots/speaker.png</code></a></sub>

<img src="https://raw.githubusercontent.com/O0000-code/paper-deck-reveal/9b1b779f0ffc31e5f5fb726ddc36b1c89a119a46/docs/screenshots/presets.png" width="100%" alt="Eight accent presets applied to the same slide of the same deck">

<sub><b>Eight accent presets applied to the same slide of the same deck</b> · <a href="https://github.com/O0000-code/paper-deck-reveal/blob/9b1b779f0ffc31e5f5fb726ddc36b1c89a119a46/docs/screenshots/presets.png"><code>docs/screenshots/presets.png</code></a></sub>

<img src="https://raw.githubusercontent.com/O0000-code/paper-deck-reveal/9b1b779f0ffc31e5f5fb726ddc36b1c89a119a46/examples/cwiek-2022-bouba-kiki/figures/provenance/rstb20200390f02.jpg" width="100%" alt="Paper Deck Reveal sample">

<sub><b>Rstb20200390f02</b> · <a href="https://github.com/O0000-code/paper-deck-reveal/blob/9b1b779f0ffc31e5f5fb726ddc36b1c89a119a46/examples/cwiek-2022-bouba-kiki/figures/provenance/rstb20200390f02.jpg"><code>examples/cwiek-2022-bouba-kiki/figures/provenance/rstb20200390f02.jpg</code></a></sub>

<img src="https://raw.githubusercontent.com/O0000-code/paper-deck-reveal/9b1b779f0ffc31e5f5fb726ddc36b1c89a119a46/examples/cwiek-2022-bouba-kiki/figures/rstb20200390f02.jpg" width="100%" alt="Paper Deck Reveal sample">

<sub><b>Rstb20200390f02</b> · <a href="https://github.com/O0000-code/paper-deck-reveal/blob/9b1b779f0ffc31e5f5fb726ddc36b1c89a119a46/examples/cwiek-2022-bouba-kiki/figures/rstb20200390f02.jpg"><code>examples/cwiek-2022-bouba-kiki/figures/rstb20200390f02.jpg</code></a></sub>

<img src="https://raw.githubusercontent.com/O0000-code/paper-deck-reveal/9b1b779f0ffc31e5f5fb726ddc36b1c89a119a46/examples/cwiek-2022-bouba-kiki/figures/provenance/rstb20200390f03.jpg" width="100%" alt="Paper Deck Reveal sample">

<sub><b>Rstb20200390f03</b> · <a href="https://github.com/O0000-code/paper-deck-reveal/blob/9b1b779f0ffc31e5f5fb726ddc36b1c89a119a46/examples/cwiek-2022-bouba-kiki/figures/provenance/rstb20200390f03.jpg"><code>examples/cwiek-2022-bouba-kiki/figures/provenance/rstb20200390f03.jpg</code></a></sub>

<img src="https://raw.githubusercontent.com/O0000-code/paper-deck-reveal/9b1b779f0ffc31e5f5fb726ddc36b1c89a119a46/examples/cwiek-2022-bouba-kiki/figures/rstb20200390f03.jpg" width="100%" alt="Paper Deck Reveal sample">

<sub><b>Rstb20200390f03</b> · <a href="https://github.com/O0000-code/paper-deck-reveal/blob/9b1b779f0ffc31e5f5fb726ddc36b1c89a119a46/examples/cwiek-2022-bouba-kiki/figures/rstb20200390f03.jpg"><code>examples/cwiek-2022-bouba-kiki/figures/rstb20200390f03.jpg</code></a></sub>

<img src="https://raw.githubusercontent.com/O0000-code/paper-deck-reveal/9b1b779f0ffc31e5f5fb726ddc36b1c89a119a46/examples/cwiek-2022-bouba-kiki/figures/provenance/rstb20200390f06.jpg" width="100%" alt="Paper Deck Reveal sample">

<sub><b>Rstb20200390f06</b> · <a href="https://github.com/O0000-code/paper-deck-reveal/blob/9b1b779f0ffc31e5f5fb726ddc36b1c89a119a46/examples/cwiek-2022-bouba-kiki/figures/provenance/rstb20200390f06.jpg"><code>examples/cwiek-2022-bouba-kiki/figures/provenance/rstb20200390f06.jpg</code></a></sub>

<img src="https://raw.githubusercontent.com/O0000-code/paper-deck-reveal/9b1b779f0ffc31e5f5fb726ddc36b1c89a119a46/examples/cwiek-2022-bouba-kiki/figures/rstb20200390f06.jpg" width="100%" alt="Paper Deck Reveal sample">

<sub><b>Rstb20200390f06</b> · <a href="https://github.com/O0000-code/paper-deck-reveal/blob/9b1b779f0ffc31e5f5fb726ddc36b1c89a119a46/examples/cwiek-2022-bouba-kiki/figures/rstb20200390f06.jpg"><code>examples/cwiek-2022-bouba-kiki/figures/rstb20200390f06.jpg</code></a></sub>

<img src="https://raw.githubusercontent.com/O0000-code/paper-deck-reveal/9b1b779f0ffc31e5f5fb726ddc36b1c89a119a46/examples/cwiek-2022-bouba-kiki/figures/provenance/rstb20200390f04.jpg" width="100%" alt="Paper Deck Reveal sample">

<sub><b>Rstb20200390f04</b> · <a href="https://github.com/O0000-code/paper-deck-reveal/blob/9b1b779f0ffc31e5f5fb726ddc36b1c89a119a46/examples/cwiek-2022-bouba-kiki/figures/provenance/rstb20200390f04.jpg"><code>examples/cwiek-2022-bouba-kiki/figures/provenance/rstb20200390f04.jpg</code></a></sub>

<img src="https://raw.githubusercontent.com/O0000-code/paper-deck-reveal/9b1b779f0ffc31e5f5fb726ddc36b1c89a119a46/examples/cwiek-2022-bouba-kiki/figures/rstb20200390f04.jpg" width="100%" alt="Paper Deck Reveal sample">

<sub><b>Rstb20200390f04</b> · <a href="https://github.com/O0000-code/paper-deck-reveal/blob/9b1b779f0ffc31e5f5fb726ddc36b1c89a119a46/examples/cwiek-2022-bouba-kiki/figures/rstb20200390f04.jpg"><code>examples/cwiek-2022-bouba-kiki/figures/rstb20200390f04.jpg</code></a></sub>

<img src="https://raw.githubusercontent.com/O0000-code/paper-deck-reveal/9b1b779f0ffc31e5f5fb726ddc36b1c89a119a46/docs/figures/provenance/rstb20200390f02.jpg" width="100%" alt="Paper Deck Reveal sample">

<sub><b>Rstb20200390f02</b> · <a href="https://github.com/O0000-code/paper-deck-reveal/blob/9b1b779f0ffc31e5f5fb726ddc36b1c89a119a46/docs/figures/provenance/rstb20200390f02.jpg"><code>docs/figures/provenance/rstb20200390f02.jpg</code></a></sub>

<img src="https://raw.githubusercontent.com/O0000-code/paper-deck-reveal/9b1b779f0ffc31e5f5fb726ddc36b1c89a119a46/docs/figures/rstb20200390f02.jpg" width="100%" alt="Paper Deck Reveal sample">

<sub><b>Rstb20200390f02</b> · <a href="https://github.com/O0000-code/paper-deck-reveal/blob/9b1b779f0ffc31e5f5fb726ddc36b1c89a119a46/docs/figures/rstb20200390f02.jpg"><code>docs/figures/rstb20200390f02.jpg</code></a></sub>

<img src="https://raw.githubusercontent.com/O0000-code/paper-deck-reveal/9b1b779f0ffc31e5f5fb726ddc36b1c89a119a46/docs/figures/provenance/rstb20200390f03.jpg" width="100%" alt="Paper Deck Reveal sample">

<sub><b>Rstb20200390f03</b> · <a href="https://github.com/O0000-code/paper-deck-reveal/blob/9b1b779f0ffc31e5f5fb726ddc36b1c89a119a46/docs/figures/provenance/rstb20200390f03.jpg"><code>docs/figures/provenance/rstb20200390f03.jpg</code></a></sub>

<img src="https://raw.githubusercontent.com/O0000-code/paper-deck-reveal/9b1b779f0ffc31e5f5fb726ddc36b1c89a119a46/docs/figures/rstb20200390f03.jpg" width="100%" alt="Paper Deck Reveal sample">

<sub><b>Rstb20200390f03</b> · <a href="https://github.com/O0000-code/paper-deck-reveal/blob/9b1b779f0ffc31e5f5fb726ddc36b1c89a119a46/docs/figures/rstb20200390f03.jpg"><code>docs/figures/rstb20200390f03.jpg</code></a></sub>

<img src="https://raw.githubusercontent.com/O0000-code/paper-deck-reveal/9b1b779f0ffc31e5f5fb726ddc36b1c89a119a46/docs/figures/provenance/rstb20200390f06.jpg" width="100%" alt="Paper Deck Reveal sample">

<sub><b>Rstb20200390f06</b> · <a href="https://github.com/O0000-code/paper-deck-reveal/blob/9b1b779f0ffc31e5f5fb726ddc36b1c89a119a46/docs/figures/provenance/rstb20200390f06.jpg"><code>docs/figures/provenance/rstb20200390f06.jpg</code></a></sub>

<img src="https://raw.githubusercontent.com/O0000-code/paper-deck-reveal/9b1b779f0ffc31e5f5fb726ddc36b1c89a119a46/docs/figures/rstb20200390f06.jpg" width="100%" alt="Paper Deck Reveal sample">

<sub><b>Rstb20200390f06</b> · <a href="https://github.com/O0000-code/paper-deck-reveal/blob/9b1b779f0ffc31e5f5fb726ddc36b1c89a119a46/docs/figures/rstb20200390f06.jpg"><code>docs/figures/rstb20200390f06.jpg</code></a></sub>

<img src="https://raw.githubusercontent.com/O0000-code/paper-deck-reveal/9b1b779f0ffc31e5f5fb726ddc36b1c89a119a46/docs/figures/provenance/rstb20200390f04.jpg" width="100%" alt="Paper Deck Reveal sample">

<sub><b>Rstb20200390f04</b> · <a href="https://github.com/O0000-code/paper-deck-reveal/blob/9b1b779f0ffc31e5f5fb726ddc36b1c89a119a46/docs/figures/provenance/rstb20200390f04.jpg"><code>docs/figures/provenance/rstb20200390f04.jpg</code></a></sub>

<img src="https://raw.githubusercontent.com/O0000-code/paper-deck-reveal/9b1b779f0ffc31e5f5fb726ddc36b1c89a119a46/docs/figures/rstb20200390f04.jpg" width="100%" alt="Paper Deck Reveal sample">

<sub><b>Rstb20200390f04</b> · <a href="https://github.com/O0000-code/paper-deck-reveal/blob/9b1b779f0ffc31e5f5fb726ddc36b1c89a119a46/docs/figures/rstb20200390f04.jpg"><code>docs/figures/rstb20200390f04.jpg</code></a></sub>

<a id="gallery-codex-slides"></a>

#### [Codex Slides](https://github.com/nexu-io/codex-slides) · — ⭐ · 框架

<sub>面向 Codex 的 AI 幻灯片工作台:图像原生画布、并行渲染、支持 PDF/PPTX 导出。</sub>

<sub>取自 [`nexu-io/codex-slides`](https://github.com/nexu-io/codex-slides) 的 48 张图，此处 24 张，靠前的几张是项目自己放在 README 里的</sub>

```bash
git clone https://github.com/nexu-io/codex-slides && cd codex-slides
```

<sub><b>下面出现的风格</b> `hero` · `01-home-community` · `02-community-styles` · `04-project-questions` · `06-visual-style` · `07-parallel-generation` · `08-editor` · `09-presenter-mode` · `10-export` · `nb-vintage-patent` · `nb-visual-info-guide` · `market-report` —— 要哪个就在提示里点名。这些是<b>项目自己用的字符串</b>，取自每张图下面链接的文件名与说明，不是本仓库起的名字。</sub>

<img src="https://raw.githubusercontent.com/nexu-io/codex-slides/dbc2a5992e937760e9ce8e587e11729f970881cb/docs/assets/readme/hero.png" width="100%" alt="Codex Slides — the open-source AI slide studio inside your coding agent, operated in the Codex in-app Browser">

<sub><b>Codex Slides — the open-source AI slide studio inside your coding agent, operated in the Codex in-app Browser</b> · <code>hero</code> · <a href="https://github.com/nexu-io/codex-slides/blob/dbc2a5992e937760e9ce8e587e11729f970881cb/docs/assets/readme/hero.png"><code>docs/assets/readme/hero.png</code></a></sub>

<img src="https://raw.githubusercontent.com/nexu-io/codex-slides/dbc2a5992e937760e9ce8e587e11729f970881cb/docs/assets/readme/01-home-community.png" width="100%" alt="Codex Slides home with the prompt composer, scenario shortcuts, and Community Styles">

<sub><b>Codex Slides home with the prompt composer, scenario shortcuts, and Community Styles</b> · <code>01-home-community</code> · <a href="https://github.com/nexu-io/codex-slides/blob/dbc2a5992e937760e9ce8e587e11729f970881cb/docs/assets/readme/01-home-community.png"><code>docs/assets/readme/01-home-community.png</code></a></sub>

<img src="https://raw.githubusercontent.com/nexu-io/codex-slides/dbc2a5992e937760e9ce8e587e11729f970881cb/docs/assets/readme/02-community-styles.png" width="100%" alt="Community Styles gallery with 73 visual directions">

<sub><b>Community Styles gallery with 73 visual directions</b> · <code>02-community-styles</code> · <a href="https://github.com/nexu-io/codex-slides/blob/dbc2a5992e937760e9ce8e587e11729f970881cb/docs/assets/readme/02-community-styles.png"><code>docs/assets/readme/02-community-styles.png</code></a></sub>

<img src="https://raw.githubusercontent.com/nexu-io/codex-slides/dbc2a5992e937760e9ce8e587e11729f970881cb/docs/assets/readme/04-project-questions.png" width="100%" alt="English clarification form inside a Codex Slides project">

<sub><b>English clarification form inside a Codex Slides project</b> · <code>04-project-questions</code> · <a href="https://github.com/nexu-io/codex-slides/blob/dbc2a5992e937760e9ce8e587e11729f970881cb/docs/assets/readme/04-project-questions.png"><code>docs/assets/readme/04-project-questions.png</code></a></sub>

<img src="https://raw.githubusercontent.com/nexu-io/codex-slides/dbc2a5992e937760e9ce8e587e11729f970881cb/docs/assets/readme/06-visual-style.png" width="100%" alt="Ranked visual direction picker inside a Codex Slides project">

<sub><b>Ranked visual direction picker inside a Codex Slides project</b> · <code>06-visual-style</code> · <a href="https://github.com/nexu-io/codex-slides/blob/dbc2a5992e937760e9ce8e587e11729f970881cb/docs/assets/readme/06-visual-style.png"><code>docs/assets/readme/06-visual-style.png</code></a></sub>

<img src="https://raw.githubusercontent.com/nexu-io/codex-slides/dbc2a5992e937760e9ce8e587e11729f970881cb/docs/assets/readme/07-parallel-generation.png" width="100%" alt="English slide generation with completed and pending pages visible">

<sub><b>English slide generation with completed and pending pages visible</b> · <code>07-parallel-generation</code> · <a href="https://github.com/nexu-io/codex-slides/blob/dbc2a5992e937760e9ce8e587e11729f970881cb/docs/assets/readme/07-parallel-generation.png"><code>docs/assets/readme/07-parallel-generation.png</code></a></sub>

<img src="https://raw.githubusercontent.com/nexu-io/codex-slides/dbc2a5992e937760e9ce8e587e11729f970881cb/docs/assets/readme/08-editor.png" width="100%" alt="English slide editor with the complete 16:9 canvas contained in view, editing toolbar, speaker notes, and thumbnails">

<sub><b>English slide editor with the complete 16:9 canvas contained in view, editing toolbar, speaker notes, and thum</b> · <code>08-editor</code> · <a href="https://github.com/nexu-io/codex-slides/blob/dbc2a5992e937760e9ce8e587e11729f970881cb/docs/assets/readme/08-editor.png"><code>docs/assets/readme/08-editor.png</code></a></sub>

<img src="https://raw.githubusercontent.com/nexu-io/codex-slides/dbc2a5992e937760e9ce8e587e11729f970881cb/docs/assets/readme/09-presenter-mode.png" width="100%" alt="Audience playback and Presenter Mode menu with the complete slide visible behind it">

<sub><b>Audience playback and Presenter Mode menu with the complete slide visible behind it</b> · <code>09-presenter-mode</code> · <a href="https://github.com/nexu-io/codex-slides/blob/dbc2a5992e937760e9ce8e587e11729f970881cb/docs/assets/readme/09-presenter-mode.png"><code>docs/assets/readme/09-presenter-mode.png</code></a></sub>

<img src="https://raw.githubusercontent.com/nexu-io/codex-slides/dbc2a5992e937760e9ce8e587e11729f970881cb/docs/assets/readme/10-export.png" width="100%" alt="English PDF and PowerPoint export menu above a fully contained 16:9 slide">

<sub><b>English PDF and PowerPoint export menu above a fully contained 16:9 slide</b> · <code>10-export</code> · <a href="https://github.com/nexu-io/codex-slides/blob/dbc2a5992e937760e9ce8e587e11729f970881cb/docs/assets/readme/10-export.png"><code>docs/assets/readme/10-export.png</code></a></sub>

<img src="https://raw.githubusercontent.com/nexu-io/codex-slides/dbc2a5992e937760e9ce8e587e11729f970881cb/public/community/nb-vintage-patent.jpg" width="100%" alt="Vintage patent filing style technical page">

<sub><b>Vintage patent filing style technical page</b> · <code>nb-vintage-patent</code> · <a href="https://github.com/nexu-io/codex-slides/blob/dbc2a5992e937760e9ce8e587e11729f970881cb/public/community/nb-vintage-patent.jpg"><code>public/community/nb-vintage-patent.jpg</code></a></sub>

<img src="https://raw.githubusercontent.com/nexu-io/codex-slides/dbc2a5992e937760e9ce8e587e11729f970881cb/public/community/nb-visual-info-guide.jpg" width="100%" alt="Clean visual information guide layout">

<sub><b>Clean visual information guide layout</b> · <code>nb-visual-info-guide</code> · <a href="https://github.com/nexu-io/codex-slides/blob/dbc2a5992e937760e9ce8e587e11729f970881cb/public/community/nb-visual-info-guide.jpg"><code>public/community/nb-visual-info-guide.jpg</code></a></sub>

<img src="https://raw.githubusercontent.com/nexu-io/codex-slides/dbc2a5992e937760e9ce8e587e11729f970881cb/docs/assets/readme/case-market-report.png" width="100%" alt="Business and market report deck">

<sub><b>Business and market report deck</b> · <a href="https://github.com/nexu-io/codex-slides/blob/dbc2a5992e937760e9ce8e587e11729f970881cb/docs/assets/readme/case-market-report.png"><code>docs/assets/readme/case-market-report.png</code></a></sub>

<img src="https://raw.githubusercontent.com/nexu-io/codex-slides/dbc2a5992e937760e9ce8e587e11729f970881cb/docs/assets/readme/case-data.png" width="100%" alt="Data visualization dashboard deck">

<sub><b>Data visualization dashboard deck</b> · <a href="https://github.com/nexu-io/codex-slides/blob/dbc2a5992e937760e9ce8e587e11729f970881cb/docs/assets/readme/case-data.png"><code>docs/assets/readme/case-data.png</code></a></sub>

<img src="https://raw.githubusercontent.com/nexu-io/codex-slides/dbc2a5992e937760e9ce8e587e11729f970881cb/docs/assets/readme/case-keynote.png" width="100%" alt="Product keynote deck">

<sub><b>Product keynote deck</b> · <a href="https://github.com/nexu-io/codex-slides/blob/dbc2a5992e937760e9ce8e587e11729f970881cb/docs/assets/readme/case-keynote.png"><code>docs/assets/readme/case-keynote.png</code></a></sub>

<img src="https://raw.githubusercontent.com/nexu-io/codex-slides/dbc2a5992e937760e9ce8e587e11729f970881cb/docs/assets/readme/case-editorial.png" width="100%" alt="Editorial magazine-style deck">

<sub><b>Editorial magazine-style deck</b> · <a href="https://github.com/nexu-io/codex-slides/blob/dbc2a5992e937760e9ce8e587e11729f970881cb/docs/assets/readme/case-editorial.png"><code>docs/assets/readme/case-editorial.png</code></a></sub>

<img src="https://raw.githubusercontent.com/nexu-io/codex-slides/dbc2a5992e937760e9ce8e587e11729f970881cb/public/community/nb-bold-product-ad.jpg" width="100%" alt="Bold high-contrast product ad slide">

<sub><b>Bold high-contrast product ad slide</b> · <code>nb-bold-product-ad</code> · <a href="https://github.com/nexu-io/codex-slides/blob/dbc2a5992e937760e9ce8e587e11729f970881cb/public/community/nb-bold-product-ad.jpg"><code>public/community/nb-bold-product-ad.jpg</code></a></sub>

<img src="https://raw.githubusercontent.com/nexu-io/codex-slides/dbc2a5992e937760e9ce8e587e11729f970881cb/public/community/nb-golden-serif-quote.jpg" width="100%" alt="Warm golden serif quote slide">

<sub><b>Warm golden serif quote slide</b> · <code>nb-golden-serif-quote</code> · <a href="https://github.com/nexu-io/codex-slides/blob/dbc2a5992e937760e9ce8e587e11729f970881cb/public/community/nb-golden-serif-quote.jpg"><code>public/community/nb-golden-serif-quote.jpg</code></a></sub>

<img src="https://raw.githubusercontent.com/nexu-io/codex-slides/dbc2a5992e937760e9ce8e587e11729f970881cb/public/community/foryou-pitch-midnight-traction.jpg" width="100%" alt="Midnight investor pitch title slide">

<sub><b>Midnight investor pitch title slide</b> · <code>foryou-pitch-midnight-traction</code> · <a href="https://github.com/nexu-io/codex-slides/blob/dbc2a5992e937760e9ce8e587e11729f970881cb/public/community/foryou-pitch-midnight-traction.jpg"><code>public/community/foryou-pitch-midnight-traction.jpg</code></a></sub>

<img src="https://raw.githubusercontent.com/nexu-io/codex-slides/dbc2a5992e937760e9ce8e587e11729f970881cb/public/community/foryou-data-answer-first.jpg" width="100%" alt="Answer-first data slide with a national map and KPI callouts">

<sub><b>Answer-first data slide with a national map and KPI callouts</b> · <code>foryou-data-answer-first</code> · <a href="https://github.com/nexu-io/codex-slides/blob/dbc2a5992e937760e9ce8e587e11729f970881cb/public/community/foryou-data-answer-first.jpg"><code>public/community/foryou-data-answer-first.jpg</code></a></sub>

<img src="https://raw.githubusercontent.com/nexu-io/codex-slides/dbc2a5992e937760e9ce8e587e11729f970881cb/public/community/foryou-craft-editorial-ink.jpg" width="100%" alt="Editorial ink-and-paper report title slide">

<sub><b>Editorial ink-and-paper report title slide</b> · <code>foryou-craft-editorial-ink</code> · <a href="https://github.com/nexu-io/codex-slides/blob/dbc2a5992e937760e9ce8e587e11729f970881cb/public/community/foryou-craft-editorial-ink.jpg"><code>public/community/foryou-craft-editorial-ink.jpg</code></a></sub>

<img src="https://raw.githubusercontent.com/nexu-io/codex-slides/dbc2a5992e937760e9ce8e587e11729f970881cb/public/community/nb-chalkboard-lesson.jpg" width="100%" alt="Warm chalkboard lesson layout with hand-drawn diagrams">

<sub><b>Warm chalkboard lesson layout with hand-drawn diagrams</b> · <code>nb-chalkboard-lesson</code> · <a href="https://github.com/nexu-io/codex-slides/blob/dbc2a5992e937760e9ce8e587e11729f970881cb/public/community/nb-chalkboard-lesson.jpg"><code>public/community/nb-chalkboard-lesson.jpg</code></a></sub>

<img src="https://raw.githubusercontent.com/nexu-io/codex-slides/dbc2a5992e937760e9ce8e587e11729f970881cb/docs/assets/readme/03-scenarios.png" width="100%" alt="Scenario library with 24 presentation workflows">

<sub><b>Scenario library with 24 presentation workflows</b> · <code>03-scenarios</code> · <a href="https://github.com/nexu-io/codex-slides/blob/dbc2a5992e937760e9ce8e587e11729f970881cb/docs/assets/readme/03-scenarios.png"><code>docs/assets/readme/03-scenarios.png</code></a></sub>

<img src="https://raw.githubusercontent.com/nexu-io/codex-slides/dbc2a5992e937760e9ce8e587e11729f970881cb/docs/assets/readme/05-research-brief.png" width="100%" alt="Source-backed English research brief in Design Files">

<sub><b>Source-backed English research brief in Design Files</b> · <code>05-research-brief</code> · <a href="https://github.com/nexu-io/codex-slides/blob/dbc2a5992e937760e9ce8e587e11729f970881cb/docs/assets/readme/05-research-brief.png"><code>docs/assets/readme/05-research-brief.png</code></a></sub>

<img src="https://raw.githubusercontent.com/nexu-io/codex-slides/dbc2a5992e937760e9ce8e587e11729f970881cb/docs/assets/readme/05-research-outline.png" width="100%" alt="Editable English presentation outline">

<sub><b>Editable English presentation outline</b> · <code>05-research-outline</code> · <a href="https://github.com/nexu-io/codex-slides/blob/dbc2a5992e937760e9ce8e587e11729f970881cb/docs/assets/readme/05-research-outline.png"><code>docs/assets/readme/05-research-outline.png</code></a></sub>

<a id="gallery-3d-html-slide-skill"></a>

#### [3D HTML Slide Skill](https://github.com/yoshifujidesign/3d-html-slide-skill) · — ⭐ · HTML

<sub>Claude Code 技能:一键生成带 Three.js 线框背景的单文件 HTML 演示幻灯片。</sub>

<sub>取自 [`yoshifujidesign/3d-html-slide-skill`](https://github.com/yoshifujidesign/3d-html-slide-skill) 的 2 张图，此处 2 张，靠前的几张是项目自己放在 README 里的</sub>


<img src="https://github.com/user-attachments/assets/7d150a1c-73ee-429a-8315-8be2650ebe11" width="100%" alt="WS002985">

<sub><b>WS002985</b> · GitHub 附件图</sub>

<img src="https://github.com/user-attachments/assets/1e3be001-6598-40b8-bf9f-da10e7d77f5d" width="100%" alt="EP133-2_2">

<sub><b>EP133-2_2</b> · GitHub 附件图</sub>

<a id="gallery-university-ppt-skill"></a>

#### [University PPT Skill](https://github.com/SiyuQiannn/university-ppt-skill) · — ⭐ · 模板库

<sub>以校色 token 与可复用版式库生成可编辑的高校主题 PPTX 演示文稿。</sub>

<sub>取自 [`SiyuQiannn/university-ppt-skill`](https://github.com/SiyuQiannn/university-ppt-skill) 的 10 张图，此处 10 张，靠前的几张是项目自己放在 README 里的</sub>

```bash
git clone https://github.com/SiyuQiannn/university-ppt-skill
```

<sub><b>下面出现的风格</b> `contact-sheet` · `02-图文案例证据-源模板复刻` · `05-对比分析框架-源模板复刻` · `03-流程时间线阶段-源模板复刻` · `01-综合卡片要点-源模板复刻` · `06-数据图表表格-源模板复刻` · `08-循环网络关系-源模板复刻` · `spec-driven-demo-contact-sheet` · `04-层级金字塔框架-源模板复刻` · `10-图标素材库-源模板复刻` —— 要哪个就在提示里点名。这些是<b>项目自己用的字符串</b>，取自每张图下面链接的文件名与说明，不是本仓库起的名字。</sub>

<img src="https://raw.githubusercontent.com/SiyuQiannn/university-ppt-skill/0bcbaf2b4f332850ca929c990e00e03771a7349b/examples/preview_contact_sheet.png" width="100%" alt="Preview">

<sub><b>Preview</b> · <code>contact-sheet</code> · <a href="https://github.com/SiyuQiannn/university-ppt-skill/blob/0bcbaf2b4f332850ca929c990e00e03771a7349b/examples/preview_contact_sheet.png"><code>examples/preview_contact_sheet.png</code></a></sub>

<img src="https://raw.githubusercontent.com/SiyuQiannn/university-ppt-skill/0bcbaf2b4f332850ca929c990e00e03771a7349b/skill/university-ppt/assets/content-layouts/ruc_core/preview_02_%E5%9B%BE%E6%96%87%E6%A1%88%E4%BE%8B%E8%AF%81%E6%8D%AE_%E6%BA%90%E6%A8%A1%E6%9D%BF%E5%A4%8D%E5%88%BB.png" width="100%" alt="University PPT Skill sample">

<sub><b>02 图文案例证据 源模板复刻</b> · <a href="https://github.com/SiyuQiannn/university-ppt-skill/blob/0bcbaf2b4f332850ca929c990e00e03771a7349b/skill/university-ppt/assets/content-layouts/ruc_core/preview_02_图文案例证据_源模板复刻.png"><code>skill/university-ppt/assets/content-layouts/ruc_core/preview_02_图文案例证据_源模板复刻.png</code></a></sub>

<img src="https://raw.githubusercontent.com/SiyuQiannn/university-ppt-skill/0bcbaf2b4f332850ca929c990e00e03771a7349b/skill/university-ppt/assets/content-layouts/ruc_core/preview_05_%E5%AF%B9%E6%AF%94%E5%88%86%E6%9E%90%E6%A1%86%E6%9E%B6_%E6%BA%90%E6%A8%A1%E6%9D%BF%E5%A4%8D%E5%88%BB.png" width="100%" alt="University PPT Skill sample">

<sub><b>05 对比分析框架 源模板复刻</b> · <a href="https://github.com/SiyuQiannn/university-ppt-skill/blob/0bcbaf2b4f332850ca929c990e00e03771a7349b/skill/university-ppt/assets/content-layouts/ruc_core/preview_05_对比分析框架_源模板复刻.png"><code>skill/university-ppt/assets/content-layouts/ruc_core/preview_05_对比分析框架_源模板复刻.png</code></a></sub>

<img src="https://raw.githubusercontent.com/SiyuQiannn/university-ppt-skill/0bcbaf2b4f332850ca929c990e00e03771a7349b/skill/university-ppt/assets/content-layouts/ruc_core/preview_03_%E6%B5%81%E7%A8%8B%E6%97%B6%E9%97%B4%E7%BA%BF%E9%98%B6%E6%AE%B5_%E6%BA%90%E6%A8%A1%E6%9D%BF%E5%A4%8D%E5%88%BB.png" width="100%" alt="University PPT Skill sample">

<sub><b>03 流程时间线阶段 源模板复刻</b> · <a href="https://github.com/SiyuQiannn/university-ppt-skill/blob/0bcbaf2b4f332850ca929c990e00e03771a7349b/skill/university-ppt/assets/content-layouts/ruc_core/preview_03_流程时间线阶段_源模板复刻.png"><code>skill/university-ppt/assets/content-layouts/ruc_core/preview_03_流程时间线阶段_源模板复刻.png</code></a></sub>

<img src="https://raw.githubusercontent.com/SiyuQiannn/university-ppt-skill/0bcbaf2b4f332850ca929c990e00e03771a7349b/skill/university-ppt/assets/content-layouts/ruc_core/preview_01_%E7%BB%BC%E5%90%88%E5%8D%A1%E7%89%87%E8%A6%81%E7%82%B9_%E6%BA%90%E6%A8%A1%E6%9D%BF%E5%A4%8D%E5%88%BB.png" width="100%" alt="University PPT Skill sample">

<sub><b>01 综合卡片要点 源模板复刻</b> · <a href="https://github.com/SiyuQiannn/university-ppt-skill/blob/0bcbaf2b4f332850ca929c990e00e03771a7349b/skill/university-ppt/assets/content-layouts/ruc_core/preview_01_综合卡片要点_源模板复刻.png"><code>skill/university-ppt/assets/content-layouts/ruc_core/preview_01_综合卡片要点_源模板复刻.png</code></a></sub>

<img src="https://raw.githubusercontent.com/SiyuQiannn/university-ppt-skill/0bcbaf2b4f332850ca929c990e00e03771a7349b/skill/university-ppt/assets/content-layouts/ruc_core/preview_06_%E6%95%B0%E6%8D%AE%E5%9B%BE%E8%A1%A8%E8%A1%A8%E6%A0%BC_%E6%BA%90%E6%A8%A1%E6%9D%BF%E5%A4%8D%E5%88%BB.png" width="100%" alt="University PPT Skill sample">

<sub><b>06 数据图表表格 源模板复刻</b> · <a href="https://github.com/SiyuQiannn/university-ppt-skill/blob/0bcbaf2b4f332850ca929c990e00e03771a7349b/skill/university-ppt/assets/content-layouts/ruc_core/preview_06_数据图表表格_源模板复刻.png"><code>skill/university-ppt/assets/content-layouts/ruc_core/preview_06_数据图表表格_源模板复刻.png</code></a></sub>

<img src="https://raw.githubusercontent.com/SiyuQiannn/university-ppt-skill/0bcbaf2b4f332850ca929c990e00e03771a7349b/skill/university-ppt/assets/content-layouts/ruc_core/preview_08_%E5%BE%AA%E7%8E%AF%E7%BD%91%E7%BB%9C%E5%85%B3%E7%B3%BB_%E6%BA%90%E6%A8%A1%E6%9D%BF%E5%A4%8D%E5%88%BB.png" width="100%" alt="University PPT Skill sample">

<sub><b>08 循环网络关系 源模板复刻</b> · <a href="https://github.com/SiyuQiannn/university-ppt-skill/blob/0bcbaf2b4f332850ca929c990e00e03771a7349b/skill/university-ppt/assets/content-layouts/ruc_core/preview_08_循环网络关系_源模板复刻.png"><code>skill/university-ppt/assets/content-layouts/ruc_core/preview_08_循环网络关系_源模板复刻.png</code></a></sub>

<img src="https://raw.githubusercontent.com/SiyuQiannn/university-ppt-skill/0bcbaf2b4f332850ca929c990e00e03771a7349b/examples/spec_driven_demo_contact_sheet.png" width="100%" alt="University PPT Skill sample">

<sub><b>Spec Driven Demo Contact Sheet</b> · <a href="https://github.com/SiyuQiannn/university-ppt-skill/blob/0bcbaf2b4f332850ca929c990e00e03771a7349b/examples/spec_driven_demo_contact_sheet.png"><code>examples/spec_driven_demo_contact_sheet.png</code></a></sub>

<img src="https://raw.githubusercontent.com/SiyuQiannn/university-ppt-skill/0bcbaf2b4f332850ca929c990e00e03771a7349b/skill/university-ppt/assets/content-layouts/ruc_core/preview_04_%E5%B1%82%E7%BA%A7%E9%87%91%E5%AD%97%E5%A1%94%E6%A1%86%E6%9E%B6_%E6%BA%90%E6%A8%A1%E6%9D%BF%E5%A4%8D%E5%88%BB.png" width="100%" alt="University PPT Skill sample">

<sub><b>04 层级金字塔框架 源模板复刻</b> · <a href="https://github.com/SiyuQiannn/university-ppt-skill/blob/0bcbaf2b4f332850ca929c990e00e03771a7349b/skill/university-ppt/assets/content-layouts/ruc_core/preview_04_层级金字塔框架_源模板复刻.png"><code>skill/university-ppt/assets/content-layouts/ruc_core/preview_04_层级金字塔框架_源模板复刻.png</code></a></sub>

<img src="https://raw.githubusercontent.com/SiyuQiannn/university-ppt-skill/0bcbaf2b4f332850ca929c990e00e03771a7349b/skill/university-ppt/assets/content-layouts/ruc_core/preview_10_%E5%9B%BE%E6%A0%87%E7%B4%A0%E6%9D%90%E5%BA%93_%E6%BA%90%E6%A8%A1%E6%9D%BF%E5%A4%8D%E5%88%BB.png" width="100%" alt="University PPT Skill sample">

<sub><b>10 图标素材库 源模板复刻</b> · <a href="https://github.com/SiyuQiannn/university-ppt-skill/blob/0bcbaf2b4f332850ca929c990e00e03771a7349b/skill/university-ppt/assets/content-layouts/ruc_core/preview_10_图标素材库_源模板复刻.png"><code>skill/university-ppt/assets/content-layouts/ruc_core/preview_10_图标素材库_源模板复刻.png</code></a></sub>

<a id="gallery-image-to-editable-ppt-skill-zhoujie97"></a>

#### [Image to Editable PPT Skill (zhoujie97)](https://github.com/zhoujie97/image-to-editable-ppt-skill) · — ⭐ · PPTX

<sub>把截图与信息图重建为可编辑的 PowerPoint 文本框、原生形状与 SVG 图标。</sub>

<sub>取自 [`zhoujie97/image-to-editable-ppt-skill`](https://github.com/zhoujie97/image-to-editable-ppt-skill) 的 4 张图，此处 4 张，靠前的几张是项目自己放在 README 里的</sub>

<sub><b>下面出现的风格</b> `效果图1` · `效果图2` · `原图2` · `原图1` —— 要哪个就在提示里点名。这些是<b>项目自己用的字符串</b>，取自每张图下面链接的文件名与说明，不是本仓库起的名字。</sub>

<img src="https://raw.githubusercontent.com/zhoujie97/image-to-editable-ppt-skill/e3c39d907ec6abf5266e4491c6aa001b663b9207/%E6%95%88%E6%9E%9C%E5%9B%BE/%E6%95%88%E6%9E%9C%E5%9B%BE1.png" width="100%" alt="alt text">

<sub><b>alt text</b> · <code>效果图1</code> · <a href="https://github.com/zhoujie97/image-to-editable-ppt-skill/blob/e3c39d907ec6abf5266e4491c6aa001b663b9207/效果图/效果图1.png"><code>效果图/效果图1.png</code></a></sub>

<img src="https://raw.githubusercontent.com/zhoujie97/image-to-editable-ppt-skill/e3c39d907ec6abf5266e4491c6aa001b663b9207/%E6%95%88%E6%9E%9C%E5%9B%BE/%E6%95%88%E6%9E%9C%E5%9B%BE2.png" width="100%" alt="alt text">

<sub><b>alt text</b> · <code>效果图2</code> · <a href="https://github.com/zhoujie97/image-to-editable-ppt-skill/blob/e3c39d907ec6abf5266e4491c6aa001b663b9207/效果图/效果图2.png"><code>效果图/效果图2.png</code></a></sub>

<img src="https://raw.githubusercontent.com/zhoujie97/image-to-editable-ppt-skill/e3c39d907ec6abf5266e4491c6aa001b663b9207/%E6%95%88%E6%9E%9C%E5%9B%BE/%E5%8E%9F%E5%9B%BE2.png" width="100%" alt="alt text">

<sub><b>alt text</b> · <code>原图2</code> · <a href="https://github.com/zhoujie97/image-to-editable-ppt-skill/blob/e3c39d907ec6abf5266e4491c6aa001b663b9207/效果图/原图2.png"><code>效果图/原图2.png</code></a></sub>

<img src="https://raw.githubusercontent.com/zhoujie97/image-to-editable-ppt-skill/e3c39d907ec6abf5266e4491c6aa001b663b9207/%E6%95%88%E6%9E%9C%E5%9B%BE/%E5%8E%9F%E5%9B%BE1.jpg" width="100%" alt="alt text">

<sub><b>alt text</b> · <code>原图1</code> · <a href="https://github.com/zhoujie97/image-to-editable-ppt-skill/blob/e3c39d907ec6abf5266e4491c6aa001b663b9207/效果图/原图1.jpg"><code>效果图/原图1.jpg</code></a></sub>

<a id="gallery-claude-ppt-skills"></a>

#### [Claude PPT Skills](https://github.com/sunxiaohui2025/claude-ppt-skills) · — ⭐ · HTML

<sub>生成六种风格的单文件 HTML 横向翻页 PPT,支持网页在线编辑与缩略图总览。</sub>

<sub>取自 [`sunxiaohui2025/claude-ppt-skills`](https://github.com/sunxiaohui2025/claude-ppt-skills) 的 3 张图，此处 3 张，靠前的几张是项目自己放在 README 里的</sub>


<img src="https://github.com/user-attachments/assets/d8742e1d-0fc1-4930-ac9a-6cc783fd47cd" width="100%" alt="截屏2026-05-28 15 23 36">

<sub><b>截屏2026-05-28 15 23 36</b> · GitHub 附件图</sub>

<img src="https://github.com/user-attachments/assets/df1b2e93-14b7-49ac-b0e9-0d99e630d382" width="100%" alt="image">

<sub><b>image</b> · GitHub 附件图</sub>

<img src="https://github.com/user-attachments/assets/da11e54a-f568-4204-9146-35f7acc57f5a" width="100%" alt="image">

<sub><b>image</b> · GitHub 附件图</sub>

<a id="gallery-econ-slides-skill"></a>

#### [Econ Slides Skill](https://github.com/hanlulong/econ-slides-skill) · — ⭐ · 框架

<sub>把经济学论文转成 Beamer 研讨会报告,并附带按时长排布的逐字讲稿。</sub>

<sub>取自 [`hanlulong/econ-slides-skill`](https://github.com/hanlulong/econ-slides-skill) 的 5 张图，此处 5 张，靠前的几张是项目自己放在 README 里的</sub>

```bash
git clone https://github.com/hanlulong/econ-slides-skill ~/.claude/skills/econ-slides
```

<sub><b>下面出现的风格</b> `punchline` · `mainresult` · `fig2-event-study` · `fig1-rollout` · `fig3-cohorts` —— 要哪个就在提示里点名。这些是<b>项目自己用的字符串</b>，取自每张图下面链接的文件名与说明，不是本仓库起的名字。</sub>

<img src="https://raw.githubusercontent.com/hanlulong/econ-slides-skill/4ac998bfa98bc0b59d4d1776b4ced565b34b802c/docs/images/sample-punchline.png" width="100%" alt="Punchline slide from an AI-built Beamer talk: the main result, one supporting heterogeneity pattern, and the implication">

<sub><b>Punchline slide from an AI-built Beamer talk: the main result, one supporting heterogeneity pattern, and the i</b> · <a href="https://github.com/hanlulong/econ-slides-skill/blob/4ac998bfa98bc0b59d4d1776b4ced565b34b802c/docs/images/sample-punchline.png"><code>docs/images/sample-punchline.png</code></a></sub>

<img src="https://raw.githubusercontent.com/hanlulong/econ-slides-skill/4ac998bfa98bc0b59d4d1776b4ced565b34b802c/docs/images/sample-mainresult.png" width="100%" alt="Main-result slide: four exact Table 2 estimates with one highlighted cell and a concise economic reading">

<sub><b>Main-result slide: four exact Table 2 estimates with one highlighted cell and a concise economic reading</b> · <code>mainresult</code> · <a href="https://github.com/hanlulong/econ-slides-skill/blob/4ac998bfa98bc0b59d4d1776b4ced565b34b802c/docs/images/sample-mainresult.png"><code>docs/images/sample-mainresult.png</code></a></sub>

<img src="https://raw.githubusercontent.com/hanlulong/econ-slides-skill/4ac998bfa98bc0b59d4d1776b4ced565b34b802c/docs/sample-talk/figures-slides/fig2_event_study.png" width="100%" alt="Econ Slides Skill sample">

<sub><b>Fig2 Event Study</b> · <a href="https://github.com/hanlulong/econ-slides-skill/blob/4ac998bfa98bc0b59d4d1776b4ced565b34b802c/docs/sample-talk/figures-slides/fig2_event_study.png"><code>docs/sample-talk/figures-slides/fig2_event_study.png</code></a></sub>

<img src="https://raw.githubusercontent.com/hanlulong/econ-slides-skill/4ac998bfa98bc0b59d4d1776b4ced565b34b802c/docs/sample-talk/figures-slides/fig1_rollout.png" width="100%" alt="Econ Slides Skill sample">

<sub><b>Fig1 Rollout</b> · <a href="https://github.com/hanlulong/econ-slides-skill/blob/4ac998bfa98bc0b59d4d1776b4ced565b34b802c/docs/sample-talk/figures-slides/fig1_rollout.png"><code>docs/sample-talk/figures-slides/fig1_rollout.png</code></a></sub>

<img src="https://raw.githubusercontent.com/hanlulong/econ-slides-skill/4ac998bfa98bc0b59d4d1776b4ced565b34b802c/docs/sample-talk/figures-slides/fig3_cohorts.png" width="100%" alt="Econ Slides Skill sample">

<sub><b>Fig3 Cohorts</b> · <a href="https://github.com/hanlulong/econ-slides-skill/blob/4ac998bfa98bc0b59d4d1776b4ced565b34b802c/docs/sample-talk/figures-slides/fig3_cohorts.png"><code>docs/sample-talk/figures-slides/fig3_cohorts.png</code></a></sub>

<a id="gallery-ghb-ppt-skill"></a>

#### [GHB PPT Skill](https://github.com/NickyLam/GHB-PPT-Skill) · — ⭐ · PPTX

<sub>基于企业模板输出 PPTX,SVG 转为可编辑 DrawingML,默认全离线验证。</sub>

<sub>取自 [`NickyLam/GHB-PPT-Skill`](https://github.com/NickyLam/GHB-PPT-Skill) 的 1 张图，此处 1 张</sub>

```bash
python3 -m pip install -r requirements.txt && python3 scripts/ghb_ppt.py doctor
```

<sub><b>下面出现的风格</b> `showcase` —— 要哪个就在提示里点名。这些是<b>项目自己用的字符串</b>，取自每张图下面链接的文件名与说明，不是本仓库起的名字。</sub>

<img src="https://raw.githubusercontent.com/NickyLam/GHB-PPT-Skill/e7ae128cb7dd7380a27a7d4a1e852beeb6734091/assets/readme/showcase.png" width="100%" alt="GHB PPT Skill sample">

<sub><b>Showcase</b> · <a href="https://github.com/NickyLam/GHB-PPT-Skill/blob/e7ae128cb7dd7380a27a7d4a1e852beeb6734091/assets/readme/showcase.png"><code>assets/readme/showcase.png</code></a></sub>

<a id="gallery-oc-sdk-ppt"></a>

#### [OpenCode PPT Studio](https://github.com/Honghurumeng/oc_sdk_ppt) · — ⭐ · 双路线

<sub>网页应用:先出大纲初稿,再开新会话精修,然后生成 HTML slides 并本地构建 PPTX。</sub>

<sub>取自 [`Honghurumeng/oc_sdk_ppt`](https://github.com/Honghurumeng/oc_sdk_ppt) 的 3 张图，此处 3 张，靠前的几张是项目自己放在 README 里的</sub>

<sub><b>下面出现的风格</b> `html` · `llm` —— 要哪个就在提示里点名。这些是<b>项目自己用的字符串</b>，取自每张图下面链接的文件名与说明，不是本仓库起的名字。</sub>

<img src="https://raw.githubusercontent.com/Honghurumeng/oc_sdk_ppt/3e2b8ba28d8c49f36c1bf1f98b14f4c3596dd9bd/images/3.png" width="100%" alt="HTML 预览与版本切换：支持按意见调整并激活某个版本">

<sub><b>HTML 预览与版本切换：支持按意见调整并激活某个版本</b> · <a href="https://github.com/Honghurumeng/oc_sdk_ppt/blob/3e2b8ba28d8c49f36c1bf1f98b14f4c3596dd9bd/images/3.png"><code>images/3.png</code></a></sub>

<img src="https://raw.githubusercontent.com/Honghurumeng/oc_sdk_ppt/3e2b8ba28d8c49f36c1bf1f98b14f4c3596dd9bd/images/1.png" width="100%" alt="主页：创建/恢复任务与 LLM 配置入口">

<sub><b>主页：创建/恢复任务与 LLM 配置入口</b> · <a href="https://github.com/Honghurumeng/oc_sdk_ppt/blob/3e2b8ba28d8c49f36c1bf1f98b14f4c3596dd9bd/images/1.png"><code>images/1.png</code></a></sub>

<img src="https://raw.githubusercontent.com/Honghurumeng/oc_sdk_ppt/3e2b8ba28d8c49f36c1bf1f98b14f4c3596dd9bd/images/2.png" width="100%" alt="构建日志：校验失败后自动修复并重试">

<sub><b>构建日志：校验失败后自动修复并重试</b> · <a href="https://github.com/Honghurumeng/oc_sdk_ppt/blob/3e2b8ba28d8c49f36c1bf1f98b14f4c3596dd9bd/images/2.png"><code>images/2.png</code></a></sub>

<a id="gallery-course-html-slides-skill"></a>

#### [Course HTML Slides Builder](https://github.com/HelenSong/course-html-slides-skill) · — ⭐ · HTML

<sub>把课程大纲转成多页 HTML 幻灯片,面向课堂投影与互动工作坊设计。</sub>

<sub>取自 [`HelenSong/course-html-slides-skill`](https://github.com/HelenSong/course-html-slides-skill) 的 9 张图，此处 9 张，靠前的几张是项目自己放在 README 里的</sub>

<sub><b>下面出现的风格</b> `collage` · `p01` · `p02-hook` · `p03-driving-question` · `p04-project-intro` · `p06-role-guide` · `p08-writing-guide` · `p11-practice` · `p12-share` —— 要哪个就在提示里点名。这些是<b>项目自己用的字符串</b>，取自每张图下面链接的文件名与说明，不是本仓库起的名字。</sub>

<img src="https://raw.githubusercontent.com/HelenSong/course-html-slides-skill/6e2c36a1f8a934cbfa89ffc27a562b70206a777c/docs/collage.png" width="100%" alt="Slide Collage">

<sub><b>Slide Collage</b> · <a href="https://github.com/HelenSong/course-html-slides-skill/blob/6e2c36a1f8a934cbfa89ffc27a562b70206a777c/docs/collage.png"><code>docs/collage.png</code></a></sub>

<img src="https://raw.githubusercontent.com/HelenSong/course-html-slides-skill/6e2c36a1f8a934cbfa89ffc27a562b70206a777c/docs/screenshots/p01-cover.png" width="100%" alt="Course HTML Slides Builder sample">

<sub><b>P01</b> · 封面 · <a href="https://github.com/HelenSong/course-html-slides-skill/blob/6e2c36a1f8a934cbfa89ffc27a562b70206a777c/docs/screenshots/p01-cover.png"><code>docs/screenshots/p01-cover.png</code></a></sub>

<img src="https://raw.githubusercontent.com/HelenSong/course-html-slides-skill/6e2c36a1f8a934cbfa89ffc27a562b70206a777c/docs/screenshots/p02-hook.png" width="100%" alt="Course HTML Slides Builder sample">

<sub><b>P02 Hook</b> · <a href="https://github.com/HelenSong/course-html-slides-skill/blob/6e2c36a1f8a934cbfa89ffc27a562b70206a777c/docs/screenshots/p02-hook.png"><code>docs/screenshots/p02-hook.png</code></a></sub>

<img src="https://raw.githubusercontent.com/HelenSong/course-html-slides-skill/6e2c36a1f8a934cbfa89ffc27a562b70206a777c/docs/screenshots/p03-driving-question.png" width="100%" alt="Course HTML Slides Builder sample">

<sub><b>P03 Driving Question</b> · <a href="https://github.com/HelenSong/course-html-slides-skill/blob/6e2c36a1f8a934cbfa89ffc27a562b70206a777c/docs/screenshots/p03-driving-question.png"><code>docs/screenshots/p03-driving-question.png</code></a></sub>

<img src="https://raw.githubusercontent.com/HelenSong/course-html-slides-skill/6e2c36a1f8a934cbfa89ffc27a562b70206a777c/docs/screenshots/p04-project-intro.png" width="100%" alt="Course HTML Slides Builder sample">

<sub><b>P04 Project Intro</b> · <a href="https://github.com/HelenSong/course-html-slides-skill/blob/6e2c36a1f8a934cbfa89ffc27a562b70206a777c/docs/screenshots/p04-project-intro.png"><code>docs/screenshots/p04-project-intro.png</code></a></sub>

<img src="https://raw.githubusercontent.com/HelenSong/course-html-slides-skill/6e2c36a1f8a934cbfa89ffc27a562b70206a777c/docs/screenshots/p06-role-guide.png" width="100%" alt="Course HTML Slides Builder sample">

<sub><b>P06 Role Guide</b> · <a href="https://github.com/HelenSong/course-html-slides-skill/blob/6e2c36a1f8a934cbfa89ffc27a562b70206a777c/docs/screenshots/p06-role-guide.png"><code>docs/screenshots/p06-role-guide.png</code></a></sub>

<img src="https://raw.githubusercontent.com/HelenSong/course-html-slides-skill/6e2c36a1f8a934cbfa89ffc27a562b70206a777c/docs/screenshots/p08-writing-guide.png" width="100%" alt="Course HTML Slides Builder sample">

<sub><b>P08 Writing Guide</b> · <a href="https://github.com/HelenSong/course-html-slides-skill/blob/6e2c36a1f8a934cbfa89ffc27a562b70206a777c/docs/screenshots/p08-writing-guide.png"><code>docs/screenshots/p08-writing-guide.png</code></a></sub>

<img src="https://raw.githubusercontent.com/HelenSong/course-html-slides-skill/6e2c36a1f8a934cbfa89ffc27a562b70206a777c/docs/screenshots/p11-practice.png" width="100%" alt="Course HTML Slides Builder sample">

<sub><b>P11 Practice</b> · <a href="https://github.com/HelenSong/course-html-slides-skill/blob/6e2c36a1f8a934cbfa89ffc27a562b70206a777c/docs/screenshots/p11-practice.png"><code>docs/screenshots/p11-practice.png</code></a></sub>

<img src="https://raw.githubusercontent.com/HelenSong/course-html-slides-skill/6e2c36a1f8a934cbfa89ffc27a562b70206a777c/docs/screenshots/p12-share.png" width="100%" alt="Course HTML Slides Builder sample">

<sub><b>P12 Share</b> · <a href="https://github.com/HelenSong/course-html-slides-skill/blob/6e2c36a1f8a934cbfa89ffc27a562b70206a777c/docs/screenshots/p12-share.png"><code>docs/screenshots/p12-share.png</code></a></sub>

<a id="gallery-excalidraw-slides-skills"></a>

#### [Excalidraw Slides Generator](https://github.com/ZunbaRan/excalidraw-slides-skills) · — ⭐ · 框架

<sub>两阶段工作流:把文本转成 16:9 Excalidraw 幻灯片,并自动生成配套 SVG 插图。</sub>

<sub>取自 [`ZunbaRan/excalidraw-slides-skills`](https://github.com/ZunbaRan/excalidraw-slides-skills) 的 5 张图，此处 5 张，靠前的几张是项目自己放在 README 里的</sub>


<img src="https://github.com/user-attachments/assets/44db2400-3c6a-4de9-8c37-b26759b284c0" width="100%" alt="image">

<sub><b>image</b> · GitHub 附件图</sub>

<img src="https://github.com/user-attachments/assets/89f3fc36-f0b7-45e7-b457-01e3b4f00e28" width="100%" alt="image">

<sub><b>image</b> · GitHub 附件图</sub>

<img src="https://github.com/user-attachments/assets/5ab31d78-49af-499f-801b-5ec374aa70d1" width="100%" alt="image">

<sub><b>image</b> · GitHub 附件图</sub>

<img src="https://github.com/user-attachments/assets/68470fc6-6fdf-49aa-a7b1-c97ca93c8c23" width="100%" alt="image">

<sub><b>image</b> · GitHub 附件图</sub>

<img src="https://github.com/user-attachments/assets/a1167d48-1bc1-4f5b-940b-145f235249bd" width="100%" alt="image">

<sub><b>image</b> · GitHub 附件图</sub>

<a id="gallery-cuhk-slides-template-html"></a>

#### [CUHK Slides Template (HTML)](https://github.com/HarlandZZC/cuhk-slides-template-html) · — ⭐ · 模板库

<sub>一份自包含的港中大配色 HTML 幻灯片模板,附带 Markdown 转幻灯片的 skill。</sub>

<sub>取自 [`HarlandZZC/cuhk-slides-template-html`](https://github.com/HarlandZZC/cuhk-slides-template-html) 的 2 张图，此处 2 张，靠前的几张是项目自己放在 README 里的</sub>

```bash
git clone https://github.com/HarlandZZC/cuhk-slides-template-html && cp -r skills/md-to-cuhk-slides .claude/skills/
```

<sub><b>下面出现的风格</b> `title` · `your-figure` —— 要哪个就在提示里点名。这些是<b>项目自己用的字符串</b>，取自每张图下面链接的文件名与说明，不是本仓库起的名字。</sub>

<img src="https://raw.githubusercontent.com/HarlandZZC/cuhk-slides-template-html/ee6ed50a5136d98c1fb06d48ee7112e3a45714d5/docs/screenshots/title.png" width="100%" alt="Title slide preview">

<sub><b>Title slide preview</b> · <a href="https://github.com/HarlandZZC/cuhk-slides-template-html/blob/ee6ed50a5136d98c1fb06d48ee7112e3a45714d5/docs/screenshots/title.png"><code>docs/screenshots/title.png</code></a></sub>

<img src="https://raw.githubusercontent.com/HarlandZZC/cuhk-slides-template-html/ee6ed50a5136d98c1fb06d48ee7112e3a45714d5/your-figure.png" width="100%" alt="CUHK Slides Template (HTML) sample">

<sub><b>Your Figure</b> · <a href="https://github.com/HarlandZZC/cuhk-slides-template-html/blob/ee6ed50a5136d98c1fb06d48ee7112e3a45714d5/your-figure.png"><code>your-figure.png</code></a></sub>

<a id="gallery-taohtml"></a>

#### [TaoHtml](https://github.com/TaoGEO/TaoHtml) · — ⭐ · HTML

<sub>把已有的 Word、PDF 或 PPT 重新设计成带分步动效、可离线交付的 16:9 HTML 演示文稿。</sub>

<sub>取自 [`TaoGEO/TaoHtml`](https://github.com/TaoGEO/TaoHtml) 的 12 张图，此处 12 张，靠前的几张是项目自己放在 README 里的</sub>

<sub><b>下面出现的风格</b> `reference-style-reconstruction` · `corporate-template-fidelity` · `built-in-visual-systems` · `reference-vi-board` · `corporate-family` · `01-ai-search-mechanism` · `02-geo-four-keywords` · `03-recall-process` · `04-retest-report` · `corporate-template-reference` · `corporate-family-section` —— 要哪个就在提示里点名。这些是<b>项目自己用的字符串</b>，取自每张图下面链接的文件名与说明，不是本仓库起的名字。</sub>

<img src="https://raw.githubusercontent.com/TaoGEO/TaoHtml/3f304ab6ea8d42dd99b5dee28d4bb81b84485d98/docs/assets/readme/v0.3.0/reference-style-reconstruction.png" width="100%" alt="参考风格重构 VI 设计标准图">

<sub><b>参考风格重构 VI 设计标准图</b> · <code>reference-style-reconstruction</code> · <a href="https://github.com/TaoGEO/TaoHtml/blob/3f304ab6ea8d42dd99b5dee28d4bb81b84485d98/docs/assets/readme/v0.3.0/reference-style-reconstruction.png"><code>docs/assets/readme/v0.3.0/reference-style-reconstruction.png</code></a></sub>

<img src="https://raw.githubusercontent.com/TaoGEO/TaoHtml/3f304ab6ea8d42dd99b5dee28d4bb81b84485d98/docs/assets/readme/v0.3.0/corporate-template-fidelity.png" width="100%" alt="企业模板保真五页合成样例">

<sub><b>企业模板保真五页合成样例</b> · <code>corporate-template-fidelity</code> · <a href="https://github.com/TaoGEO/TaoHtml/blob/3f304ab6ea8d42dd99b5dee28d4bb81b84485d98/docs/assets/readme/v0.3.0/corporate-template-fidelity.png"><code>docs/assets/readme/v0.3.0/corporate-template-fidelity.png</code></a></sub>

<img src="https://raw.githubusercontent.com/TaoGEO/TaoHtml/3f304ab6ea8d42dd99b5dee28d4bb81b84485d98/docs/assets/readme/v0.3.0/built-in-visual-systems.png" width="100%" alt="TaoHtml 四套内置视觉系统各五页总览">

<sub><b>TaoHtml 四套内置视觉系统各五页总览</b> · <code>built-in-visual-systems</code> · <a href="https://github.com/TaoGEO/TaoHtml/blob/3f304ab6ea8d42dd99b5dee28d4bb81b84485d98/docs/assets/readme/v0.3.0/built-in-visual-systems.png"><code>docs/assets/readme/v0.3.0/built-in-visual-systems.png</code></a></sub>

<img src="https://raw.githubusercontent.com/TaoGEO/TaoHtml/3f304ab6ea8d42dd99b5dee28d4bb81b84485d98/examples/corporate-template-fidelity/reference-vi-board.png" width="100%" alt="TaoHtml sample">

<sub><b>Reference Vi Board</b> · <a href="https://github.com/TaoGEO/TaoHtml/blob/3f304ab6ea8d42dd99b5dee28d4bb81b84485d98/examples/corporate-template-fidelity/reference-vi-board.png"><code>examples/corporate-template-fidelity/reference-vi-board.png</code></a></sub>

<img src="https://raw.githubusercontent.com/TaoGEO/TaoHtml/3f304ab6ea8d42dd99b5dee28d4bb81b84485d98/tests/fixtures/corporate-family-cover.png" width="100%" alt="TaoHtml sample">

<sub><b>Corporate Family</b> · 封面 · <a href="https://github.com/TaoGEO/TaoHtml/blob/3f304ab6ea8d42dd99b5dee28d4bb81b84485d98/tests/fixtures/corporate-family-cover.png"><code>tests/fixtures/corporate-family-cover.png</code></a></sub>

<img src="https://raw.githubusercontent.com/TaoGEO/TaoHtml/3f304ab6ea8d42dd99b5dee28d4bb81b84485d98/docs/assets/cases/geo-salon/01-ai-search-mechanism.png" width="100%" alt="TaoHtml sample">

<sub><b>01 Ai Search Mechanism</b> · <a href="https://github.com/TaoGEO/TaoHtml/blob/3f304ab6ea8d42dd99b5dee28d4bb81b84485d98/docs/assets/cases/geo-salon/01-ai-search-mechanism.png"><code>docs/assets/cases/geo-salon/01-ai-search-mechanism.png</code></a></sub>

<img src="https://raw.githubusercontent.com/TaoGEO/TaoHtml/3f304ab6ea8d42dd99b5dee28d4bb81b84485d98/docs/assets/cases/geo-salon/02-geo-four-keywords.png" width="100%" alt="TaoHtml sample">

<sub><b>02 Geo Four Keywords</b> · <a href="https://github.com/TaoGEO/TaoHtml/blob/3f304ab6ea8d42dd99b5dee28d4bb81b84485d98/docs/assets/cases/geo-salon/02-geo-four-keywords.png"><code>docs/assets/cases/geo-salon/02-geo-four-keywords.png</code></a></sub>

<img src="https://raw.githubusercontent.com/TaoGEO/TaoHtml/3f304ab6ea8d42dd99b5dee28d4bb81b84485d98/docs/assets/cases/geo-salon/03-recall-process.png" width="100%" alt="TaoHtml sample">

<sub><b>03 Recall Process</b> · <a href="https://github.com/TaoGEO/TaoHtml/blob/3f304ab6ea8d42dd99b5dee28d4bb81b84485d98/docs/assets/cases/geo-salon/03-recall-process.png"><code>docs/assets/cases/geo-salon/03-recall-process.png</code></a></sub>

<img src="https://raw.githubusercontent.com/TaoGEO/TaoHtml/3f304ab6ea8d42dd99b5dee28d4bb81b84485d98/docs/assets/cases/geo-salon/04-retest-report.png" width="100%" alt="TaoHtml sample">

<sub><b>04 Retest Report</b> · <a href="https://github.com/TaoGEO/TaoHtml/blob/3f304ab6ea8d42dd99b5dee28d4bb81b84485d98/docs/assets/cases/geo-salon/04-retest-report.png"><code>docs/assets/cases/geo-salon/04-retest-report.png</code></a></sub>

<img src="https://raw.githubusercontent.com/TaoGEO/TaoHtml/3f304ab6ea8d42dd99b5dee28d4bb81b84485d98/tests/fixtures/corporate-template-reference.png" width="100%" alt="TaoHtml sample">

<sub><b>Corporate Template Reference</b> · <a href="https://github.com/TaoGEO/TaoHtml/blob/3f304ab6ea8d42dd99b5dee28d4bb81b84485d98/tests/fixtures/corporate-template-reference.png"><code>tests/fixtures/corporate-template-reference.png</code></a></sub>

<img src="https://raw.githubusercontent.com/TaoGEO/TaoHtml/3f304ab6ea8d42dd99b5dee28d4bb81b84485d98/tests/fixtures/corporate-family-section.png" width="100%" alt="TaoHtml sample">

<sub><b>Corporate Family Section</b> · <a href="https://github.com/TaoGEO/TaoHtml/blob/3f304ab6ea8d42dd99b5dee28d4bb81b84485d98/tests/fixtures/corporate-family-section.png"><code>tests/fixtures/corporate-family-section.png</code></a></sub>

<img src="https://raw.githubusercontent.com/TaoGEO/TaoHtml/3f304ab6ea8d42dd99b5dee28d4bb81b84485d98/tests/fixtures/corporate-family-toc.png" width="100%" alt="TaoHtml sample">

<sub><b>Corporate Family</b> · 目录页 · <a href="https://github.com/TaoGEO/TaoHtml/blob/3f304ab6ea8d42dd99b5dee28d4bb81b84485d98/tests/fixtures/corporate-family-toc.png"><code>tests/fixtures/corporate-family-toc.png</code></a></sub>

<a id="gallery-google-slides-skill"></a>

#### [Google Slides Deck Skill](https://github.com/eranw2000/google-slides-skill) · — ⭐ · 框架

<sub>通过 API 重建 Google Slides 演示文稿,并把每页渲染成 PNG 回看以自查结果。</sub>

<sub>取自 [`eranw2000/google-slides-skill`](https://github.com/eranw2000/google-slides-skill) 的 1 张图，此处 1 张，靠前的几张是项目自己放在 README 里的</sub>

```bash
cp -R google-slides-skill/enhance-slides ~/.claude/skills/
```

<sub><b>下面出现的风格</b> `enhance-slides-flow` —— 要哪个就在提示里点名。这些是<b>项目自己用的字符串</b>，取自每张图下面链接的文件名与说明，不是本仓库起的名字。</sub>

<img src="https://raw.githubusercontent.com/eranw2000/google-slides-skill/43127d4e79f963be2243e0369b779baf453eac28/docs/enhance-slides-flow.png" width="100%" alt="enhance-slides flow">

<sub><b>enhance-slides flow</b> · <a href="https://github.com/eranw2000/google-slides-skill/blob/43127d4e79f963be2243e0369b779baf453eac28/docs/enhance-slides-flow.png"><code>docs/enhance-slides-flow.png</code></a></sub>

<a id="gallery-inspiration-deck-workshop"></a>

#### [Inspiration Deck Workshop](https://github.com/zjsthmjialin/inspiration-deck-workshop) · — ⭐ · 模板库

<sub>23 套主题与 25 种页面版式,用一个小 CLI 生成带动效的静态 HTML 演示。</sub>

<sub>取自 [`zjsthmjialin/inspiration-deck-workshop`](https://github.com/zjsthmjialin/inspiration-deck-workshop) 的 23 张图，此处 23 张，靠前的几张是项目自己放在 README 里的</sub>

```bash
git clone https://github.com/zjsthmjialin/inspiration-deck-workshop && node tools/cli.mjs new my-deck --template product-launch
```

<sub><b>下面出现的风格</b> `18-black-gold-stage` · `19-platinum-launch` · `21-signal-dashboard` · `23-vivid-pop` · `00-all-themes-contact-sheet` · `01-clear-board` · `02-mist-blue` · `03-data-brief` · `04-deep-code` · `05-terminal-signal` · `06-blueprint-grid` · `07-soft-card` —— 要哪个就在提示里点名。这些是<b>项目自己用的字符串</b>，取自每张图下面链接的文件名与说明，不是本仓库起的名字。</sub>

<img src="https://raw.githubusercontent.com/zjsthmjialin/inspiration-deck-workshop/2c13fdf624b35b11b657d41273ec1a7930786643/docs/assets/theme-showcase/18-black-gold-stage.png" width="100%" alt="Black Gold Stage">

<sub><b>Black Gold Stage</b> · <code>18-black-gold-stage</code> · <a href="https://github.com/zjsthmjialin/inspiration-deck-workshop/blob/2c13fdf624b35b11b657d41273ec1a7930786643/docs/assets/theme-showcase/18-black-gold-stage.png"><code>docs/assets/theme-showcase/18-black-gold-stage.png</code></a></sub>

<img src="https://raw.githubusercontent.com/zjsthmjialin/inspiration-deck-workshop/2c13fdf624b35b11b657d41273ec1a7930786643/docs/assets/theme-showcase/19-platinum-launch.png" width="100%" alt="Platinum Launch">

<sub><b>Platinum Launch</b> · <code>19-platinum-launch</code> · <a href="https://github.com/zjsthmjialin/inspiration-deck-workshop/blob/2c13fdf624b35b11b657d41273ec1a7930786643/docs/assets/theme-showcase/19-platinum-launch.png"><code>docs/assets/theme-showcase/19-platinum-launch.png</code></a></sub>

<img src="https://raw.githubusercontent.com/zjsthmjialin/inspiration-deck-workshop/2c13fdf624b35b11b657d41273ec1a7930786643/docs/assets/theme-showcase/21-signal-dashboard.png" width="100%" alt="Signal Dashboard">

<sub><b>Signal Dashboard</b> · <code>21-signal-dashboard</code> · <a href="https://github.com/zjsthmjialin/inspiration-deck-workshop/blob/2c13fdf624b35b11b657d41273ec1a7930786643/docs/assets/theme-showcase/21-signal-dashboard.png"><code>docs/assets/theme-showcase/21-signal-dashboard.png</code></a></sub>

<img src="https://raw.githubusercontent.com/zjsthmjialin/inspiration-deck-workshop/2c13fdf624b35b11b657d41273ec1a7930786643/docs/assets/theme-showcase/23-vivid-pop.png" width="100%" alt="Vivid Pop">

<sub><b>Vivid Pop</b> · <code>23-vivid-pop</code> · <a href="https://github.com/zjsthmjialin/inspiration-deck-workshop/blob/2c13fdf624b35b11b657d41273ec1a7930786643/docs/assets/theme-showcase/23-vivid-pop.png"><code>docs/assets/theme-showcase/23-vivid-pop.png</code></a></sub>

<img src="https://raw.githubusercontent.com/zjsthmjialin/inspiration-deck-workshop/2c13fdf624b35b11b657d41273ec1a7930786643/docs/assets/theme-showcase/00-all-themes-contact-sheet.png" width="100%" alt="All theme preview">

<sub><b>All theme preview</b> · <code>00-all-themes-contact-sheet</code> · <a href="https://github.com/zjsthmjialin/inspiration-deck-workshop/blob/2c13fdf624b35b11b657d41273ec1a7930786643/docs/assets/theme-showcase/00-all-themes-contact-sheet.png"><code>docs/assets/theme-showcase/00-all-themes-contact-sheet.png</code></a></sub>

<img src="https://raw.githubusercontent.com/zjsthmjialin/inspiration-deck-workshop/2c13fdf624b35b11b657d41273ec1a7930786643/docs/assets/theme-showcase/01-clear-board.png" width="100%" alt="Inspiration Deck Workshop sample">

<sub><b>01 Clear Board</b> · <a href="https://github.com/zjsthmjialin/inspiration-deck-workshop/blob/2c13fdf624b35b11b657d41273ec1a7930786643/docs/assets/theme-showcase/01-clear-board.png"><code>docs/assets/theme-showcase/01-clear-board.png</code></a></sub>

<img src="https://raw.githubusercontent.com/zjsthmjialin/inspiration-deck-workshop/2c13fdf624b35b11b657d41273ec1a7930786643/docs/assets/theme-showcase/02-mist-blue.png" width="100%" alt="Inspiration Deck Workshop sample">

<sub><b>02 Mist Blue</b> · <a href="https://github.com/zjsthmjialin/inspiration-deck-workshop/blob/2c13fdf624b35b11b657d41273ec1a7930786643/docs/assets/theme-showcase/02-mist-blue.png"><code>docs/assets/theme-showcase/02-mist-blue.png</code></a></sub>

<img src="https://raw.githubusercontent.com/zjsthmjialin/inspiration-deck-workshop/2c13fdf624b35b11b657d41273ec1a7930786643/docs/assets/theme-showcase/03-data-brief.png" width="100%" alt="Inspiration Deck Workshop sample">

<sub><b>03 Data Brief</b> · <a href="https://github.com/zjsthmjialin/inspiration-deck-workshop/blob/2c13fdf624b35b11b657d41273ec1a7930786643/docs/assets/theme-showcase/03-data-brief.png"><code>docs/assets/theme-showcase/03-data-brief.png</code></a></sub>

<img src="https://raw.githubusercontent.com/zjsthmjialin/inspiration-deck-workshop/2c13fdf624b35b11b657d41273ec1a7930786643/docs/assets/theme-showcase/04-deep-code.png" width="100%" alt="Inspiration Deck Workshop sample">

<sub><b>04 Deep Code</b> · <a href="https://github.com/zjsthmjialin/inspiration-deck-workshop/blob/2c13fdf624b35b11b657d41273ec1a7930786643/docs/assets/theme-showcase/04-deep-code.png"><code>docs/assets/theme-showcase/04-deep-code.png</code></a></sub>

<img src="https://raw.githubusercontent.com/zjsthmjialin/inspiration-deck-workshop/2c13fdf624b35b11b657d41273ec1a7930786643/docs/assets/theme-showcase/05-terminal-signal.png" width="100%" alt="Inspiration Deck Workshop sample">

<sub><b>05 Terminal Signal</b> · <a href="https://github.com/zjsthmjialin/inspiration-deck-workshop/blob/2c13fdf624b35b11b657d41273ec1a7930786643/docs/assets/theme-showcase/05-terminal-signal.png"><code>docs/assets/theme-showcase/05-terminal-signal.png</code></a></sub>

<img src="https://raw.githubusercontent.com/zjsthmjialin/inspiration-deck-workshop/2c13fdf624b35b11b657d41273ec1a7930786643/docs/assets/theme-showcase/06-blueprint-grid.png" width="100%" alt="Inspiration Deck Workshop sample">

<sub><b>06 Blueprint Grid</b> · <a href="https://github.com/zjsthmjialin/inspiration-deck-workshop/blob/2c13fdf624b35b11b657d41273ec1a7930786643/docs/assets/theme-showcase/06-blueprint-grid.png"><code>docs/assets/theme-showcase/06-blueprint-grid.png</code></a></sub>

<img src="https://raw.githubusercontent.com/zjsthmjialin/inspiration-deck-workshop/2c13fdf624b35b11b657d41273ec1a7930786643/docs/assets/theme-showcase/07-soft-card.png" width="100%" alt="Inspiration Deck Workshop sample">

<sub><b>07 Soft Card</b> · <a href="https://github.com/zjsthmjialin/inspiration-deck-workshop/blob/2c13fdf624b35b11b657d41273ec1a7930786643/docs/assets/theme-showcase/07-soft-card.png"><code>docs/assets/theme-showcase/07-soft-card.png</code></a></sub>

<img src="https://raw.githubusercontent.com/zjsthmjialin/inspiration-deck-workshop/2c13fdf624b35b11b657d41273ec1a7930786643/docs/assets/theme-showcase/08-editorial-space.png" width="100%" alt="Inspiration Deck Workshop sample">

<sub><b>08 Editorial Space</b> · <a href="https://github.com/zjsthmjialin/inspiration-deck-workshop/blob/2c13fdf624b35b11b657d41273ec1a7930786643/docs/assets/theme-showcase/08-editorial-space.png"><code>docs/assets/theme-showcase/08-editorial-space.png</code></a></sub>

<img src="https://raw.githubusercontent.com/zjsthmjialin/inspiration-deck-workshop/2c13fdf624b35b11b657d41273ec1a7930786643/docs/assets/theme-showcase/09-journal-spark.png" width="100%" alt="Inspiration Deck Workshop sample">

<sub><b>09 Journal Spark</b> · <a href="https://github.com/zjsthmjialin/inspiration-deck-workshop/blob/2c13fdf624b35b11b657d41273ec1a7930786643/docs/assets/theme-showcase/09-journal-spark.png"><code>docs/assets/theme-showcase/09-journal-spark.png</code></a></sub>

<img src="https://raw.githubusercontent.com/zjsthmjialin/inspiration-deck-workshop/2c13fdf624b35b11b657d41273ec1a7930786643/docs/assets/theme-showcase/11-glass-light.png" width="100%" alt="Inspiration Deck Workshop sample">

<sub><b>11 Glass Light</b> · <a href="https://github.com/zjsthmjialin/inspiration-deck-workshop/blob/2c13fdf624b35b11b657d41273ec1a7930786643/docs/assets/theme-showcase/11-glass-light.png"><code>docs/assets/theme-showcase/11-glass-light.png</code></a></sub>

<img src="https://raw.githubusercontent.com/zjsthmjialin/inspiration-deck-workshop/2c13fdf624b35b11b657d41273ec1a7930786643/docs/assets/theme-showcase/12-brand-pop.png" width="100%" alt="Inspiration Deck Workshop sample">

<sub><b>12 Brand Pop</b> · <a href="https://github.com/zjsthmjialin/inspiration-deck-workshop/blob/2c13fdf624b35b11b657d41273ec1a7930786643/docs/assets/theme-showcase/12-brand-pop.png"><code>docs/assets/theme-showcase/12-brand-pop.png</code></a></sub>

<img src="https://raw.githubusercontent.com/zjsthmjialin/inspiration-deck-workshop/2c13fdf624b35b11b657d41273ec1a7930786643/docs/assets/theme-showcase/13-paper-research.png" width="100%" alt="Inspiration Deck Workshop sample">

<sub><b>13 Paper Research</b> · <a href="https://github.com/zjsthmjialin/inspiration-deck-workshop/blob/2c13fdf624b35b11b657d41273ec1a7930786643/docs/assets/theme-showcase/13-paper-research.png"><code>docs/assets/theme-showcase/13-paper-research.png</code></a></sub>

<img src="https://raw.githubusercontent.com/zjsthmjialin/inspiration-deck-workshop/2c13fdf624b35b11b657d41273ec1a7930786643/docs/assets/theme-showcase/14-consulting-pro.png" width="100%" alt="Inspiration Deck Workshop sample">

<sub><b>14 Consulting Pro</b> · <a href="https://github.com/zjsthmjialin/inspiration-deck-workshop/blob/2c13fdf624b35b11b657d41273ec1a7930786643/docs/assets/theme-showcase/14-consulting-pro.png"><code>docs/assets/theme-showcase/14-consulting-pro.png</code></a></sub>

<img src="https://raw.githubusercontent.com/zjsthmjialin/inspiration-deck-workshop/2c13fdf624b35b11b657d41273ec1a7930786643/docs/assets/theme-showcase/15-minimal-stage.png" width="100%" alt="Inspiration Deck Workshop sample">

<sub><b>15 Minimal Stage</b> · <a href="https://github.com/zjsthmjialin/inspiration-deck-workshop/blob/2c13fdf624b35b11b657d41273ec1a7930786643/docs/assets/theme-showcase/15-minimal-stage.png"><code>docs/assets/theme-showcase/15-minimal-stage.png</code></a></sub>

<img src="https://raw.githubusercontent.com/zjsthmjialin/inspiration-deck-workshop/2c13fdf624b35b11b657d41273ec1a7930786643/docs/assets/theme-showcase/16-neon-orbit.png" width="100%" alt="Inspiration Deck Workshop sample">

<sub><b>16 Neon Orbit</b> · <a href="https://github.com/zjsthmjialin/inspiration-deck-workshop/blob/2c13fdf624b35b11b657d41273ec1a7930786643/docs/assets/theme-showcase/16-neon-orbit.png"><code>docs/assets/theme-showcase/16-neon-orbit.png</code></a></sub>

<img src="https://raw.githubusercontent.com/zjsthmjialin/inspiration-deck-workshop/2c13fdf624b35b11b657d41273ec1a7930786643/docs/assets/theme-showcase/17-quantum-grid.png" width="100%" alt="Inspiration Deck Workshop sample">

<sub><b>17 Quantum Grid</b> · <a href="https://github.com/zjsthmjialin/inspiration-deck-workshop/blob/2c13fdf624b35b11b657d41273ec1a7930786643/docs/assets/theme-showcase/17-quantum-grid.png"><code>docs/assets/theme-showcase/17-quantum-grid.png</code></a></sub>

<img src="https://raw.githubusercontent.com/zjsthmjialin/inspiration-deck-workshop/2c13fdf624b35b11b657d41273ec1a7930786643/docs/assets/theme-showcase/20-executive-ink.png" width="100%" alt="Inspiration Deck Workshop sample">

<sub><b>20 Executive Ink</b> · <a href="https://github.com/zjsthmjialin/inspiration-deck-workshop/blob/2c13fdf624b35b11b657d41273ec1a7930786643/docs/assets/theme-showcase/20-executive-ink.png"><code>docs/assets/theme-showcase/20-executive-ink.png</code></a></sub>

<img src="https://raw.githubusercontent.com/zjsthmjialin/inspiration-deck-workshop/2c13fdf624b35b11b657d41273ec1a7930786643/docs/assets/theme-showcase/22-editorial-luxe.png" width="100%" alt="Inspiration Deck Workshop sample">

<sub><b>22 Editorial Luxe</b> · <a href="https://github.com/zjsthmjialin/inspiration-deck-workshop/blob/2c13fdf624b35b11b657d41273ec1a7930786643/docs/assets/theme-showcase/22-editorial-luxe.png"><code>docs/assets/theme-showcase/22-editorial-luxe.png</code></a></sub>

<a id="gallery-html-presentation-skill"></a>

#### [HTML Presentation Skill](https://github.com/defreitassl/html-presentation-skill) · — ⭐ · HTML

<sub>把文档、笔记或简报转成独立的 HTML 演示页面,并对结果做校验。</sub>

<sub>取自 [`defreitassl/html-presentation-skill`](https://github.com/defreitassl/html-presentation-skill) 的 5 张图，此处 5 张，靠前的几张是项目自己放在 README 里的</sub>

<sub><b>下面出现的风格</b> `artemis-program-overview` · `artemis-ii-executive-briefing` · `kubernetes-command-center` · `artemis-ii-mission-planner` · `who-air-pollution-dossier` —— 要哪个就在提示里点名。这些是<b>项目自己用的字符串</b>，取自每张图下面链接的文件名与说明，不是本仓库起的名字。</sub>

<img src="https://raw.githubusercontent.com/defreitassl/html-presentation-skill/1e3b4d19d815d1d79b51a2faaf3197a6a272f10a/assets/previews/artemis-program-overview.png" width="100%" alt="Artemis Program Overview preview">

<sub><b>Artemis Program Overview preview</b> · <a href="https://github.com/defreitassl/html-presentation-skill/blob/1e3b4d19d815d1d79b51a2faaf3197a6a272f10a/assets/previews/artemis-program-overview.png"><code>assets/previews/artemis-program-overview.png</code></a></sub>

<img src="https://raw.githubusercontent.com/defreitassl/html-presentation-skill/1e3b4d19d815d1d79b51a2faaf3197a6a272f10a/assets/previews/artemis-ii-executive-briefing.png" width="100%" alt="Artemis II Executive Briefing preview">

<sub><b>Artemis II Executive Briefing preview</b> · <a href="https://github.com/defreitassl/html-presentation-skill/blob/1e3b4d19d815d1d79b51a2faaf3197a6a272f10a/assets/previews/artemis-ii-executive-briefing.png"><code>assets/previews/artemis-ii-executive-briefing.png</code></a></sub>

<img src="https://raw.githubusercontent.com/defreitassl/html-presentation-skill/1e3b4d19d815d1d79b51a2faaf3197a6a272f10a/assets/previews/kubernetes-command-center.png" width="100%" alt="Kubernetes Command Center preview">

<sub><b>Kubernetes Command Center preview</b> · <a href="https://github.com/defreitassl/html-presentation-skill/blob/1e3b4d19d815d1d79b51a2faaf3197a6a272f10a/assets/previews/kubernetes-command-center.png"><code>assets/previews/kubernetes-command-center.png</code></a></sub>

<img src="https://raw.githubusercontent.com/defreitassl/html-presentation-skill/1e3b4d19d815d1d79b51a2faaf3197a6a272f10a/assets/previews/artemis-ii-mission-planner.png" width="100%" alt="Artemis II Mission Planner preview">

<sub><b>Artemis II Mission Planner preview</b> · <a href="https://github.com/defreitassl/html-presentation-skill/blob/1e3b4d19d815d1d79b51a2faaf3197a6a272f10a/assets/previews/artemis-ii-mission-planner.png"><code>assets/previews/artemis-ii-mission-planner.png</code></a></sub>

<img src="https://raw.githubusercontent.com/defreitassl/html-presentation-skill/1e3b4d19d815d1d79b51a2faaf3197a6a272f10a/assets/previews/who-air-pollution-dossier.png" width="100%" alt="WHO Ambient Air Pollution Dossier preview">

<sub><b>WHO Ambient Air Pollution Dossier preview</b> · <code>who-air-pollution-dossier</code> · <a href="https://github.com/defreitassl/html-presentation-skill/blob/1e3b4d19d815d1d79b51a2faaf3197a6a272f10a/assets/previews/who-air-pollution-dossier.png"><code>assets/previews/who-air-pollution-dossier.png</code></a></sub>

<a id="gallery-agent-pptify-kit"></a>

#### [PPTX Deck Creation Kit](https://github.com/kimtth/agent-pptify-kit) · — ⭐ · PPTX

<sub>以显式坐标规格生成 PPTX,输出保持原生对象,并以 Copilot 插件形式分发。</sub>

<sub>取自 [`kimtth/agent-pptify-kit`](https://github.com/kimtth/agent-pptify-kit) 的 3 张图，此处 3 张，靠前的几张是项目自己放在 README 里的</sub>

<sub><b>下面出现的风格</b> `pptify-kit-stress-demo-contact-sheet` · `pptify-kit-stress-demo-v3-contact-sheet` · `pptify-kit-stress-demo-v2-contact-sheet` —— 要哪个就在提示里点名。这些是<b>项目自己用的字符串</b>，取自每张图下面链接的文件名与说明，不是本仓库起的名字。</sub>

<img src="https://raw.githubusercontent.com/kimtth/agent-pptify-kit/831c9107b522baa8131e27c47d4cf04af5e54d93/docs/preview/pptify-kit-stress-demo-contact-sheet.png" width="100%" alt="Contact sheet of all 81 layouts in pptify-kit-stress-demo.pptx">

<sub><b>Contact sheet of all 81 layouts in pptify-kit-stress-demo.pptx</b> · <code>pptify-kit-stress-demo-contact-sheet</code> · <a href="https://github.com/kimtth/agent-pptify-kit/blob/831c9107b522baa8131e27c47d4cf04af5e54d93/docs/preview/pptify-kit-stress-demo-contact-sheet.png"><code>docs/preview/pptify-kit-stress-demo-contact-sheet.png</code></a></sub>

<img src="https://raw.githubusercontent.com/kimtth/agent-pptify-kit/831c9107b522baa8131e27c47d4cf04af5e54d93/docs/preview/pptify-kit-stress-demo-v3-contact-sheet.png" width="100%" alt="Contact sheet of all 60 layouts in pptify-kit-stress-demo-v3.pptx">

<sub><b>Contact sheet of all 60 layouts in pptify-kit-stress-demo-v3.pptx</b> · <code>pptify-kit-stress-demo-v3-contact-sheet</code> · <a href="https://github.com/kimtth/agent-pptify-kit/blob/831c9107b522baa8131e27c47d4cf04af5e54d93/docs/preview/pptify-kit-stress-demo-v3-contact-sheet.png"><code>docs/preview/pptify-kit-stress-demo-v3-contact-sheet.png</code></a></sub>

<img src="https://raw.githubusercontent.com/kimtth/agent-pptify-kit/831c9107b522baa8131e27c47d4cf04af5e54d93/docs/preview/pptify-kit-stress-demo-v2-contact-sheet.png" width="100%" alt="Contact sheet of all 50 layouts in pptify-kit-stress-demo-v2.pptx">

<sub><b>Contact sheet of all 50 layouts in pptify-kit-stress-demo-v2.pptx</b> · <code>pptify-kit-stress-demo-v2-contact-sheet</code> · <a href="https://github.com/kimtth/agent-pptify-kit/blob/831c9107b522baa8131e27c47d4cf04af5e54d93/docs/preview/pptify-kit-stress-demo-v2-contact-sheet.png"><code>docs/preview/pptify-kit-stress-demo-v2-contact-sheet.png</code></a></sub>

<a id="gallery-vyral-tiktok-slideshow-skill"></a>

#### [TikTok Slideshow Command Center](https://github.com/Meliwat/vyral-tiktok-slideshow-skill) · — ⭐ · 图片

<sub>规划 TikTok 图文轮播:内容切角、单页设计与发布节奏一次成型。</sub>

<sub>取自 [`Meliwat/vyral-tiktok-slideshow-skill`](https://github.com/Meliwat/vyral-tiktok-slideshow-skill) 的 6 张图，此处 6 张，靠前的几张是项目自己放在 README 里的</sub>

<sub><b>下面出现的风格</b> `slide-1` · `slide-3` · `slide-5` · `command-center` · `renders` —— 要哪个就在提示里点名。这些是<b>项目自己用的字符串</b>，取自每张图下面链接的文件名与说明，不是本仓库起的名字。</sub>

<img src="https://raw.githubusercontent.com/Meliwat/vyral-tiktok-slideshow-skill/f22e11a960c06d706cacbccccf5ff20985e70b9d/skill/examples/renders/slide-01.jpg" width="100%" alt="Slide 1">

<sub><b>Slide 1</b> · <a href="https://github.com/Meliwat/vyral-tiktok-slideshow-skill/blob/f22e11a960c06d706cacbccccf5ff20985e70b9d/skill/examples/renders/slide-01.jpg"><code>skill/examples/renders/slide-01.jpg</code></a></sub>

<img src="https://raw.githubusercontent.com/Meliwat/vyral-tiktok-slideshow-skill/f22e11a960c06d706cacbccccf5ff20985e70b9d/skill/examples/renders/slide-03.jpg" width="100%" alt="Slide 3">

<sub><b>Slide 3</b> · <a href="https://github.com/Meliwat/vyral-tiktok-slideshow-skill/blob/f22e11a960c06d706cacbccccf5ff20985e70b9d/skill/examples/renders/slide-03.jpg"><code>skill/examples/renders/slide-03.jpg</code></a></sub>

<img src="https://raw.githubusercontent.com/Meliwat/vyral-tiktok-slideshow-skill/f22e11a960c06d706cacbccccf5ff20985e70b9d/skill/examples/renders/slide-05.jpg" width="100%" alt="Slide 5">

<sub><b>Slide 5</b> · <a href="https://github.com/Meliwat/vyral-tiktok-slideshow-skill/blob/f22e11a960c06d706cacbccccf5ff20985e70b9d/skill/examples/renders/slide-05.jpg"><code>skill/examples/renders/slide-05.jpg</code></a></sub>

<img src="https://raw.githubusercontent.com/Meliwat/vyral-tiktok-slideshow-skill/f22e11a960c06d706cacbccccf5ff20985e70b9d/docs/command-center.png" width="100%" alt="The Command Center planning board">

<sub><b>The Command Center planning board</b> · <a href="https://github.com/Meliwat/vyral-tiktok-slideshow-skill/blob/f22e11a960c06d706cacbccccf5ff20985e70b9d/docs/command-center.png"><code>docs/command-center.png</code></a></sub>

<img src="https://raw.githubusercontent.com/Meliwat/vyral-tiktok-slideshow-skill/f22e11a960c06d706cacbccccf5ff20985e70b9d/skill/examples/renders/slide-02.jpg" width="100%" alt="TikTok Slideshow Command Center sample">

<sub><b>Renders</b> · <a href="https://github.com/Meliwat/vyral-tiktok-slideshow-skill/blob/f22e11a960c06d706cacbccccf5ff20985e70b9d/skill/examples/renders/slide-02.jpg"><code>skill/examples/renders/slide-02.jpg</code></a></sub>

<img src="https://raw.githubusercontent.com/Meliwat/vyral-tiktok-slideshow-skill/f22e11a960c06d706cacbccccf5ff20985e70b9d/skill/examples/renders/slide-04.jpg" width="100%" alt="TikTok Slideshow Command Center sample">

<sub><b>Renders</b> · <a href="https://github.com/Meliwat/vyral-tiktok-slideshow-skill/blob/f22e11a960c06d706cacbccccf5ff20985e70b9d/skill/examples/renders/slide-04.jpg"><code>skill/examples/renders/slide-04.jpg</code></a></sub>

<a id="gallery-ppt-deck-builder-skill"></a>

#### [PPT Deck Builder Skill](https://github.com/lk251066/ppt-deck-builder-skill) · — ⭐ · 图片

<sub>逐页生成成品图,只返修出问题的单页,最后统一打包成 PPTX。</sub>

<sub>取自 [`lk251066/ppt-deck-builder-skill`](https://github.com/lk251066/ppt-deck-builder-skill) 的 4 张图，此处 4 张，靠前的几张是项目自己放在 README 里的</sub>

<sub><b>下面出现的风格</b> `slide-01` · `slide-04` · `slide-06` · `slide-08` —— 要哪个就在提示里点名。这些是<b>项目自己用的字符串</b>，取自每张图下面链接的文件名与说明，不是本仓库起的名字。</sub>

<img src="https://raw.githubusercontent.com/lk251066/ppt-deck-builder-skill/aa3c9a23717aa836f6397407bfe7226969bd29bb/examples/grsai_ai_science_deck_micro_modules/slide-01.png" width="100%" alt="slide-01">

<sub><b>slide-01</b> · <a href="https://github.com/lk251066/ppt-deck-builder-skill/blob/aa3c9a23717aa836f6397407bfe7226969bd29bb/examples/grsai_ai_science_deck_micro_modules/slide-01.png"><code>examples/grsai_ai_science_deck_micro_modules/slide-01.png</code></a></sub>

<img src="https://raw.githubusercontent.com/lk251066/ppt-deck-builder-skill/aa3c9a23717aa836f6397407bfe7226969bd29bb/examples/grsai_ai_science_deck_micro_modules/slide-04.png" width="100%" alt="slide-04">

<sub><b>slide-04</b> · <a href="https://github.com/lk251066/ppt-deck-builder-skill/blob/aa3c9a23717aa836f6397407bfe7226969bd29bb/examples/grsai_ai_science_deck_micro_modules/slide-04.png"><code>examples/grsai_ai_science_deck_micro_modules/slide-04.png</code></a></sub>

<img src="https://raw.githubusercontent.com/lk251066/ppt-deck-builder-skill/aa3c9a23717aa836f6397407bfe7226969bd29bb/examples/grsai_ai_science_deck_micro_modules/slide-06.png" width="100%" alt="slide-06">

<sub><b>slide-06</b> · <a href="https://github.com/lk251066/ppt-deck-builder-skill/blob/aa3c9a23717aa836f6397407bfe7226969bd29bb/examples/grsai_ai_science_deck_micro_modules/slide-06.png"><code>examples/grsai_ai_science_deck_micro_modules/slide-06.png</code></a></sub>

<img src="https://raw.githubusercontent.com/lk251066/ppt-deck-builder-skill/aa3c9a23717aa836f6397407bfe7226969bd29bb/examples/grsai_ai_science_deck_micro_modules/slide-08.png" width="100%" alt="slide-08">

<sub><b>slide-08</b> · <a href="https://github.com/lk251066/ppt-deck-builder-skill/blob/aa3c9a23717aa836f6397407bfe7226969bd29bb/examples/grsai_ai_science_deck_micro_modules/slide-08.png"><code>examples/grsai_ai_science_deck_micro_modules/slide-08.png</code></a></sub>

<a id="gallery-kr-brand-decks"></a>

#### [KR Brand Decks](https://github.com/sylvanus4/kr-brand-decks) · — ⭐ · 模板库

<sub>23 个 skill,每个对应一家韩国企业品牌,从零构建符合该品牌规范的 PPTX。</sub>

<sub>取自 [`sylvanus4/kr-brand-decks`](https://github.com/sylvanus4/kr-brand-decks) 的 30 张图，此处 24 张，靠前的几张是项目自己放在 README 里的</sub>

```bash
/plugin marketplace add sylvanus4/kr-brand-decks && /plugin install kr-brand-decks@kr-brand-decks
```

<sub><b>下面出现的风格</b> `gallery` · `themes-gallery` · `celltrion` · `cj-cheiljedang` · `doosan` · `hanwha` · `hd-hyundai` · `hyundai-motor` · `kakao` · `kb-financial` · `kia` · `lg-electronics` —— 要哪个就在提示里点名。这些是<b>项目自己用的字符串</b>，取自每张图下面链接的文件名与说明，不是本仓库起的名字。</sub>

<img src="https://raw.githubusercontent.com/sylvanus4/kr-brand-decks/c6735ab91fb24afe31220358b419f87fb171d6d1/docs/gallery.png" width="100%" alt="Gallery of 23 brand cover slides">

<sub><b>Gallery of 23 brand cover slides</b> · <a href="https://github.com/sylvanus4/kr-brand-decks/blob/c6735ab91fb24afe31220358b419f87fb171d6d1/docs/gallery.png"><code>docs/gallery.png</code></a></sub>

<img src="https://raw.githubusercontent.com/sylvanus4/kr-brand-decks/c6735ab91fb24afe31220358b419f87fb171d6d1/docs/themes-gallery.png" width="100%" alt="KR Brand Decks sample">

<sub><b>Themes Gallery</b> · <a href="https://github.com/sylvanus4/kr-brand-decks/blob/c6735ab91fb24afe31220358b419f87fb171d6d1/docs/themes-gallery.png"><code>docs/themes-gallery.png</code></a></sub>

<img src="https://raw.githubusercontent.com/sylvanus4/kr-brand-decks/c6735ab91fb24afe31220358b419f87fb171d6d1/skills/deck-celltrion/examples/celltrion-cover.png" width="100%" alt="KR Brand Decks sample">

<sub><b>Celltrion</b> · 封面 · <a href="https://github.com/sylvanus4/kr-brand-decks/blob/c6735ab91fb24afe31220358b419f87fb171d6d1/skills/deck-celltrion/examples/celltrion-cover.png"><code>skills/deck-celltrion/examples/celltrion-cover.png</code></a></sub>

<img src="https://raw.githubusercontent.com/sylvanus4/kr-brand-decks/c6735ab91fb24afe31220358b419f87fb171d6d1/skills/deck-cj-cheiljedang/examples/cj-cheiljedang-cover.png" width="100%" alt="KR Brand Decks sample">

<sub><b>Cj Cheiljedang</b> · 封面 · <a href="https://github.com/sylvanus4/kr-brand-decks/blob/c6735ab91fb24afe31220358b419f87fb171d6d1/skills/deck-cj-cheiljedang/examples/cj-cheiljedang-cover.png"><code>skills/deck-cj-cheiljedang/examples/cj-cheiljedang-cover.png</code></a></sub>

<img src="https://raw.githubusercontent.com/sylvanus4/kr-brand-decks/c6735ab91fb24afe31220358b419f87fb171d6d1/skills/deck-doosan/examples/doosan-cover.png" width="100%" alt="KR Brand Decks sample">

<sub><b>Doosan</b> · 封面 · <a href="https://github.com/sylvanus4/kr-brand-decks/blob/c6735ab91fb24afe31220358b419f87fb171d6d1/skills/deck-doosan/examples/doosan-cover.png"><code>skills/deck-doosan/examples/doosan-cover.png</code></a></sub>

<img src="https://raw.githubusercontent.com/sylvanus4/kr-brand-decks/c6735ab91fb24afe31220358b419f87fb171d6d1/skills/deck-hanwha/examples/hanwha-cover.png" width="100%" alt="KR Brand Decks sample">

<sub><b>Hanwha</b> · 封面 · <a href="https://github.com/sylvanus4/kr-brand-decks/blob/c6735ab91fb24afe31220358b419f87fb171d6d1/skills/deck-hanwha/examples/hanwha-cover.png"><code>skills/deck-hanwha/examples/hanwha-cover.png</code></a></sub>

<img src="https://raw.githubusercontent.com/sylvanus4/kr-brand-decks/c6735ab91fb24afe31220358b419f87fb171d6d1/skills/deck-hd-hyundai/examples/hd-hyundai-cover.png" width="100%" alt="KR Brand Decks sample">

<sub><b>Hd Hyundai</b> · 封面 · <a href="https://github.com/sylvanus4/kr-brand-decks/blob/c6735ab91fb24afe31220358b419f87fb171d6d1/skills/deck-hd-hyundai/examples/hd-hyundai-cover.png"><code>skills/deck-hd-hyundai/examples/hd-hyundai-cover.png</code></a></sub>

<img src="https://raw.githubusercontent.com/sylvanus4/kr-brand-decks/c6735ab91fb24afe31220358b419f87fb171d6d1/skills/deck-hyundai-motor/examples/hyundai-motor-cover.png" width="100%" alt="KR Brand Decks sample">

<sub><b>Hyundai Motor</b> · 封面 · <a href="https://github.com/sylvanus4/kr-brand-decks/blob/c6735ab91fb24afe31220358b419f87fb171d6d1/skills/deck-hyundai-motor/examples/hyundai-motor-cover.png"><code>skills/deck-hyundai-motor/examples/hyundai-motor-cover.png</code></a></sub>

<img src="https://raw.githubusercontent.com/sylvanus4/kr-brand-decks/c6735ab91fb24afe31220358b419f87fb171d6d1/skills/deck-kakao/examples/kakao-cover.png" width="100%" alt="KR Brand Decks sample">

<sub><b>Kakao</b> · 封面 · <a href="https://github.com/sylvanus4/kr-brand-decks/blob/c6735ab91fb24afe31220358b419f87fb171d6d1/skills/deck-kakao/examples/kakao-cover.png"><code>skills/deck-kakao/examples/kakao-cover.png</code></a></sub>

<img src="https://raw.githubusercontent.com/sylvanus4/kr-brand-decks/c6735ab91fb24afe31220358b419f87fb171d6d1/skills/deck-kb-financial/examples/kb-financial-cover.png" width="100%" alt="KR Brand Decks sample">

<sub><b>Kb Financial</b> · 封面 · <a href="https://github.com/sylvanus4/kr-brand-decks/blob/c6735ab91fb24afe31220358b419f87fb171d6d1/skills/deck-kb-financial/examples/kb-financial-cover.png"><code>skills/deck-kb-financial/examples/kb-financial-cover.png</code></a></sub>

<img src="https://raw.githubusercontent.com/sylvanus4/kr-brand-decks/c6735ab91fb24afe31220358b419f87fb171d6d1/skills/deck-kia/examples/kia-cover.png" width="100%" alt="KR Brand Decks sample">

<sub><b>Kia</b> · 封面 · <a href="https://github.com/sylvanus4/kr-brand-decks/blob/c6735ab91fb24afe31220358b419f87fb171d6d1/skills/deck-kia/examples/kia-cover.png"><code>skills/deck-kia/examples/kia-cover.png</code></a></sub>

<img src="https://raw.githubusercontent.com/sylvanus4/kr-brand-decks/c6735ab91fb24afe31220358b419f87fb171d6d1/skills/deck-lg-electronics/examples/lg-electronics-cover.png" width="100%" alt="KR Brand Decks sample">

<sub><b>Lg Electronics</b> · 封面 · <a href="https://github.com/sylvanus4/kr-brand-decks/blob/c6735ab91fb24afe31220358b419f87fb171d6d1/skills/deck-lg-electronics/examples/lg-electronics-cover.png"><code>skills/deck-lg-electronics/examples/lg-electronics-cover.png</code></a></sub>

<img src="https://raw.githubusercontent.com/sylvanus4/kr-brand-decks/c6735ab91fb24afe31220358b419f87fb171d6d1/skills/deck-lg-energy/examples/lg-energy-cover.png" width="100%" alt="KR Brand Decks sample">

<sub><b>Lg Energy</b> · 封面 · <a href="https://github.com/sylvanus4/kr-brand-decks/blob/c6735ab91fb24afe31220358b419f87fb171d6d1/skills/deck-lg-energy/examples/lg-energy-cover.png"><code>skills/deck-lg-energy/examples/lg-energy-cover.png</code></a></sub>

<img src="https://raw.githubusercontent.com/sylvanus4/kr-brand-decks/c6735ab91fb24afe31220358b419f87fb171d6d1/skills/deck-naver/examples/naver-cover.png" width="100%" alt="KR Brand Decks sample">

<sub><b>Naver</b> · 封面 · <a href="https://github.com/sylvanus4/kr-brand-decks/blob/c6735ab91fb24afe31220358b419f87fb171d6d1/skills/deck-naver/examples/naver-cover.png"><code>skills/deck-naver/examples/naver-cover.png</code></a></sub>

<img src="https://raw.githubusercontent.com/sylvanus4/kr-brand-decks/c6735ab91fb24afe31220358b419f87fb171d6d1/skills/deck-ncsoft/examples/ncsoft-cover.png" width="100%" alt="KR Brand Decks sample">

<sub><b>Ncsoft</b> · 封面 · <a href="https://github.com/sylvanus4/kr-brand-decks/blob/c6735ab91fb24afe31220358b419f87fb171d6d1/skills/deck-ncsoft/examples/ncsoft-cover.png"><code>skills/deck-ncsoft/examples/ncsoft-cover.png</code></a></sub>

<img src="https://raw.githubusercontent.com/sylvanus4/kr-brand-decks/c6735ab91fb24afe31220358b419f87fb171d6d1/skills/deck-ncsoft/examples/tmpc-01.png" width="100%" alt="KR Brand Decks sample">

<sub><b>Tmpc · 01</b> · <a href="https://github.com/sylvanus4/kr-brand-decks/blob/c6735ab91fb24afe31220358b419f87fb171d6d1/skills/deck-ncsoft/examples/tmpc-01.png"><code>skills/deck-ncsoft/examples/tmpc-01.png</code></a></sub>

<img src="https://raw.githubusercontent.com/sylvanus4/kr-brand-decks/c6735ab91fb24afe31220358b419f87fb171d6d1/skills/deck-nongshim/examples/nongshim-cover.png" width="100%" alt="KR Brand Decks sample">

<sub><b>Nongshim</b> · 封面 · <a href="https://github.com/sylvanus4/kr-brand-decks/blob/c6735ab91fb24afe31220358b419f87fb171d6d1/skills/deck-nongshim/examples/nongshim-cover.png"><code>skills/deck-nongshim/examples/nongshim-cover.png</code></a></sub>

<img src="https://raw.githubusercontent.com/sylvanus4/kr-brand-decks/c6735ab91fb24afe31220358b419f87fb171d6d1/skills/deck-posco/examples/posco-cover.png" width="100%" alt="KR Brand Decks sample">

<sub><b>Posco</b> · 封面 · <a href="https://github.com/sylvanus4/kr-brand-decks/blob/c6735ab91fb24afe31220358b419f87fb171d6d1/skills/deck-posco/examples/posco-cover.png"><code>skills/deck-posco/examples/posco-cover.png</code></a></sub>

<img src="https://raw.githubusercontent.com/sylvanus4/kr-brand-decks/c6735ab91fb24afe31220358b419f87fb171d6d1/skills/deck-samsung-mobile/examples/samsung-mobile-cover.png" width="100%" alt="KR Brand Decks sample">

<sub><b>Samsung Mobile</b> · 封面 · <a href="https://github.com/sylvanus4/kr-brand-decks/blob/c6735ab91fb24afe31220358b419f87fb171d6d1/skills/deck-samsung-mobile/examples/samsung-mobile-cover.png"><code>skills/deck-samsung-mobile/examples/samsung-mobile-cover.png</code></a></sub>

<img src="https://raw.githubusercontent.com/sylvanus4/kr-brand-decks/c6735ab91fb24afe31220358b419f87fb171d6d1/skills/deck-samsung-sdi/examples/samsung-sdi-cover.png" width="100%" alt="KR Brand Decks sample">

<sub><b>Samsung Sdi</b> · 封面 · <a href="https://github.com/sylvanus4/kr-brand-decks/blob/c6735ab91fb24afe31220358b419f87fb171d6d1/skills/deck-samsung-sdi/examples/samsung-sdi-cover.png"><code>skills/deck-samsung-sdi/examples/samsung-sdi-cover.png</code></a></sub>

<img src="https://raw.githubusercontent.com/sylvanus4/kr-brand-decks/c6735ab91fb24afe31220358b419f87fb171d6d1/skills/deck-samsung-semi/examples/samsung-semi-cover.png" width="100%" alt="KR Brand Decks sample">

<sub><b>Samsung Semi</b> · 封面 · <a href="https://github.com/sylvanus4/kr-brand-decks/blob/c6735ab91fb24afe31220358b419f87fb171d6d1/skills/deck-samsung-semi/examples/samsung-semi-cover.png"><code>skills/deck-samsung-semi/examples/samsung-semi-cover.png</code></a></sub>

<img src="https://raw.githubusercontent.com/sylvanus4/kr-brand-decks/c6735ab91fb24afe31220358b419f87fb171d6d1/skills/deck-samsung-semi/examples/tmpc-01.png" width="100%" alt="KR Brand Decks sample">

<sub><b>Tmpc · 01</b> · <a href="https://github.com/sylvanus4/kr-brand-decks/blob/c6735ab91fb24afe31220358b419f87fb171d6d1/skills/deck-samsung-semi/examples/tmpc-01.png"><code>skills/deck-samsung-semi/examples/tmpc-01.png</code></a></sub>

<img src="https://raw.githubusercontent.com/sylvanus4/kr-brand-decks/c6735ab91fb24afe31220358b419f87fb171d6d1/skills/deck-shinhan/examples/shinhan-cover.png" width="100%" alt="KR Brand Decks sample">

<sub><b>Shinhan</b> · 封面 · <a href="https://github.com/sylvanus4/kr-brand-decks/blob/c6735ab91fb24afe31220358b419f87fb171d6d1/skills/deck-shinhan/examples/shinhan-cover.png"><code>skills/deck-shinhan/examples/shinhan-cover.png</code></a></sub>

<img src="https://raw.githubusercontent.com/sylvanus4/kr-brand-decks/c6735ab91fb24afe31220358b419f87fb171d6d1/skills/deck-sk-hynix/examples/sk-hynix-cover.png" width="100%" alt="KR Brand Decks sample">

<sub><b>Sk Hynix</b> · 封面 · <a href="https://github.com/sylvanus4/kr-brand-decks/blob/c6735ab91fb24afe31220358b419f87fb171d6d1/skills/deck-sk-hynix/examples/sk-hynix-cover.png"><code>skills/deck-sk-hynix/examples/sk-hynix-cover.png</code></a></sub>

<a id="gallery-slide-deck-skill"></a>

#### [Slide Deck Skill](https://github.com/jayworker/slide-deck-skill) · — ⭐ · HTML

<sub>单文件 16:9 HTML 演示,浅色仪表盘风格,每页只讲一件事。</sub>

<sub>取自 [`jayworker/slide-deck-skill`](https://github.com/jayworker/slide-deck-skill) 的 6 张图，此处 6 张，靠前的几张是项目自己放在 README 里的</sub>

```bash
git clone https://github.com/jayworker/slide-deck-skill "$HOME/.claude/skills/slide-deck"
```

<sub><b>下面出现的风格</b> `3` —— 要哪个就在提示里点名。这些是<b>项目自己用的字符串</b>，取自每张图下面链接的文件名与说明，不是本仓库起的名字。</sub>

<img src="https://raw.githubusercontent.com/jayworker/slide-deck-skill/76ecc8e16804558d8f0d2eb3ff97eb4b29273306/docs/screenshots/slide-1.png" width="100%" alt="표지">

<sub><b>표지</b> · <a href="https://github.com/jayworker/slide-deck-skill/blob/76ecc8e16804558d8f0d2eb3ff97eb4b29273306/docs/screenshots/slide-1.png"><code>docs/screenshots/slide-1.png</code></a></sub>

<img src="https://raw.githubusercontent.com/jayworker/slide-deck-skill/76ecc8e16804558d8f0d2eb3ff97eb4b29273306/docs/screenshots/slide-2.png" width="100%" alt="3층 구조">

<sub><b>3층 구조</b> · <a href="https://github.com/jayworker/slide-deck-skill/blob/76ecc8e16804558d8f0d2eb3ff97eb4b29273306/docs/screenshots/slide-2.png"><code>docs/screenshots/slide-2.png</code></a></sub>

<img src="https://raw.githubusercontent.com/jayworker/slide-deck-skill/76ecc8e16804558d8f0d2eb3ff97eb4b29273306/docs/screenshots/slide-3.png" width="100%" alt="아이콘 규칙">

<sub><b>아이콘 규칙</b> · <a href="https://github.com/jayworker/slide-deck-skill/blob/76ecc8e16804558d8f0d2eb3ff97eb4b29273306/docs/screenshots/slide-3.png"><code>docs/screenshots/slide-3.png</code></a></sub>

<img src="https://raw.githubusercontent.com/jayworker/slide-deck-skill/76ecc8e16804558d8f0d2eb3ff97eb4b29273306/docs/screenshots/slide-4.png" width="100%" alt="데이터 슬라이드">

<sub><b>데이터 슬라이드</b> · <a href="https://github.com/jayworker/slide-deck-skill/blob/76ecc8e16804558d8f0d2eb3ff97eb4b29273306/docs/screenshots/slide-4.png"><code>docs/screenshots/slide-4.png</code></a></sub>

<img src="https://raw.githubusercontent.com/jayworker/slide-deck-skill/76ecc8e16804558d8f0d2eb3ff97eb4b29273306/docs/screenshots/slide-5.png" width="100%" alt="데이터 색 규칙">

<sub><b>데이터 색 규칙</b> · <a href="https://github.com/jayworker/slide-deck-skill/blob/76ecc8e16804558d8f0d2eb3ff97eb4b29273306/docs/screenshots/slide-5.png"><code>docs/screenshots/slide-5.png</code></a></sub>

<img src="https://raw.githubusercontent.com/jayworker/slide-deck-skill/76ecc8e16804558d8f0d2eb3ff97eb4b29273306/docs/screenshots/slide-6.png" width="100%" alt="액션 아이템">

<sub><b>액션 아이템</b> · <a href="https://github.com/jayworker/slide-deck-skill/blob/76ecc8e16804558d8f0d2eb3ff97eb4b29273306/docs/screenshots/slide-6.png"><code>docs/screenshots/slide-6.png</code></a></sub>

<a id="gallery-marp-slides-studio"></a>

#### [Marp Slides Studio](https://github.com/unsolublesugar/marp-slides-studio) · — ⭐ · 模板库

<sub>50 套 Marp 主题,配主题画廊、对比度检查与四个面向 Agent 的 deck 制作 skill。</sub>

<sub>取自 [`unsolublesugar/marp-slides-studio`](https://github.com/unsolublesugar/marp-slides-studio) 的 9 张图，此处 9 张，靠前的几张是项目自己放在 README 里的</sub>

```bash
gh repo create my-slides --template unsolublesugar/marp-slides-studio --private --clone && npm install
```

<sub><b>下面出现的风格</b> `theme-preview` · `themes` · `gallery` · `layouts` · `code-block` · `code-block-diff` · `patterns` · `tones` · `themes-select` —— 要哪个就在提示里点名。这些是<b>项目自己用的字符串</b>，取自每张图下面链接的文件名与说明，不是本仓库起的名字。</sub>

<img src="https://raw.githubusercontent.com/unsolublesugar/marp-slides-studio/2d761c1abc2004fd75c06d2c8d225ebff0c21b0a/docs/theme-preview.png" width="100%" alt="テーマ切替プレビュー">

<sub><b>テーマ切替プレビュー</b> · <code>theme-preview</code> · <a href="https://github.com/unsolublesugar/marp-slides-studio/blob/2d761c1abc2004fd75c06d2c8d225ebff0c21b0a/docs/theme-preview.png"><code>docs/theme-preview.png</code></a></sub>

<img src="https://raw.githubusercontent.com/unsolublesugar/marp-slides-studio/2d761c1abc2004fd75c06d2c8d225ebff0c21b0a/docs/themes.png" width="100%" alt="テーマの例（レイアウト×配色×トーンの組み合わせ）">

<sub><b>テーマの例（レイアウト×配色×トーンの組み合わせ）</b> · <code>themes</code> · <a href="https://github.com/unsolublesugar/marp-slides-studio/blob/2d761c1abc2004fd75c06d2c8d225ebff0c21b0a/docs/themes.png"><code>docs/themes.png</code></a></sub>

<img src="https://raw.githubusercontent.com/unsolublesugar/marp-slides-studio/2d761c1abc2004fd75c06d2c8d225ebff0c21b0a/docs/gallery.png" width="100%" alt="テーマギャラリー">

<sub><b>テーマギャラリー</b> · <code>gallery</code> · <a href="https://github.com/unsolublesugar/marp-slides-studio/blob/2d761c1abc2004fd75c06d2c8d225ebff0c21b0a/docs/gallery.png"><code>docs/gallery.png</code></a></sub>

<img src="https://raw.githubusercontent.com/unsolublesugar/marp-slides-studio/2d761c1abc2004fd75c06d2c8d225ebff0c21b0a/docs/layouts.png" width="100%" alt="レイアウトバリエーション">

<sub><b>レイアウトバリエーション</b> · <code>layouts</code> · <a href="https://github.com/unsolublesugar/marp-slides-studio/blob/2d761c1abc2004fd75c06d2c8d225ebff0c21b0a/docs/layouts.png"><code>docs/layouts.png</code></a></sub>

<img src="https://raw.githubusercontent.com/unsolublesugar/marp-slides-studio/2d761c1abc2004fd75c06d2c8d225ebff0c21b0a/docs/code-block.png" width="100%" alt="コードブロックの表示例">

<sub><b>コードブロックの表示例</b> · <code>code-block</code> · <a href="https://github.com/unsolublesugar/marp-slides-studio/blob/2d761c1abc2004fd75c06d2c8d225ebff0c21b0a/docs/code-block.png"><code>docs/code-block.png</code></a></sub>

<img src="https://raw.githubusercontent.com/unsolublesugar/marp-slides-studio/2d761c1abc2004fd75c06d2c8d225ebff0c21b0a/docs/code-block-diff.png" width="100%" alt="diffの表示例">

<sub><b>diffの表示例</b> · <code>code-block-diff</code> · <a href="https://github.com/unsolublesugar/marp-slides-studio/blob/2d761c1abc2004fd75c06d2c8d225ebff0c21b0a/docs/code-block-diff.png"><code>docs/code-block-diff.png</code></a></sub>

<img src="https://raw.githubusercontent.com/unsolublesugar/marp-slides-studio/2d761c1abc2004fd75c06d2c8d225ebff0c21b0a/docs/patterns.png" width="100%" alt="レイアウトパターン">

<sub><b>レイアウトパターン</b> · <code>patterns</code> · <a href="https://github.com/unsolublesugar/marp-slides-studio/blob/2d761c1abc2004fd75c06d2c8d225ebff0c21b0a/docs/patterns.png"><code>docs/patterns.png</code></a></sub>

<img src="https://raw.githubusercontent.com/unsolublesugar/marp-slides-studio/2d761c1abc2004fd75c06d2c8d225ebff0c21b0a/docs/tones.png" width="100%" alt="トーンの違い">

<sub><b>トーンの違い</b> · <code>tones</code> · <a href="https://github.com/unsolublesugar/marp-slides-studio/blob/2d761c1abc2004fd75c06d2c8d225ebff0c21b0a/docs/tones.png"><code>docs/tones.png</code></a></sub>

<img src="https://raw.githubusercontent.com/unsolublesugar/marp-slides-studio/2d761c1abc2004fd75c06d2c8d225ebff0c21b0a/docs/themes-select.png" width="100%" alt="Marp Slides Studio sample">

<sub><b>Themes Select</b> · <a href="https://github.com/unsolublesugar/marp-slides-studio/blob/2d761c1abc2004fd75c06d2c8d225ebff0c21b0a/docs/themes-select.png"><code>docs/themes-select.png</code></a></sub>

<sub>以下项目的仓库里没有可用图片：Slidev、Quarkdown、Banana Slides、Visual Explainer、HTML Anything、Dashi PPT Skill、Codex PPT Skill、NanoBanana PPT Skills、Baoyu Design、Gorden PPT Skill、Codex Claude Academic Skills、Oh My PPT、Image to Editable PPT Skill、Gorden Super PPT Skills、CyberPPT、Ian Handdrawn PPT、PPT Image First、GPT Image2 PPT Skills、PPT Agent Skills、Humanize PPT、Claude Office Skills、Academic PPTX、Claude Skills、Power Design、Reveal.js Skill、Visual Style PPT Skill、Beamer Skill、RW Consulting PPT、Paper2Anything、DOM to PPTX、Marp Slides、Beamer Academic、Planners PPT Hell、Thesis Defense PPTX Skill、Apple Bento Grid、Codex PPT Skill、Hands on Deck、Skywork Skills、PPT Image2 Editable Rebuild、Slide Image to Editable PPTX、Magic Slide、Presentation Skills、Claude Design Skill、Servasyy Skills、Ultimate PPT Master Skill、Future Slide、Slide Deck Generator、HTML PPT Designer、Presentation Skills、PowerPoint Skill、Make Slide、PPT Report Skills、AI Paper to Slide Skill、Literature Report PPT Builder、Image to PPTX Skill、Visual Cognition Slides、CN Academic Spark、Knowledge Cat PPT Skill、SJTU PPT Template Skill、Deck Factory、Space Multi Design PPT、Lieflat HTML Design、Jiarui SVG Skills、Awesome PPT Skills、Editable Image to PPT Skill、Presentation、Huawei Style PPT Skill、HTML to Editable PPTX、Claude Code Codex Slide、Baoyu Xuanyi Skills、Beautiful Hackathon Slides、ImageGen PPTX Pipeline、Paper PPT Skill、Presentation Skill、Codex Image to Editable PPT、Slidev Skills、PPT Skill、BL Captain PPT Skill、HTML to PPT PDF、Slides AI Plugin、Scholar PPT CN、Narrative Engine、Image PPT King、PPT Design DNA、PPT Creator Skills、Beamer Skill、Jingge Sense Deck、Presentation Skill、Econ Empirical Paper PPT Skill、HTML to PPTX、Neon Slides、Claude HTML Slide Builder、30x McKinsey Research Deck、Keynote Slides Skill、PPT Agent、Interactive Slides、PPTX Template Skills、KAI Presentation、AI Draw Skill、Keynot、MBB Decks、Slide Wright、CyberBin PPT Skill、Competition PPT Template Skill、Four-Up PPT Generator、NanoBanana PPT Skills、NanoBanana PPT Skills、PPT Image Share Builder、HalfAI Gufa PPT、Slide Design Skill、Better PPT HTML Deck、Create HTML Deck、AWS HTML Slides、Prada Slides、Japanese Corporate PPTX Skill、Editable Leadership PPTX、SlideStage Pack、Deckset Claude Skill、McKinsey HTML Design Skill、IML PPTX、GZR NSFC PPT Skill、HTML to PPTX Skill、Bento PPT Skill、SlideSmith、Fudan University PPT Skill、Presentation Chef、Paper Figure PPTX Skill、AI Editable PPT Skill、Hand-Drawn PPT Skill、Guizang PPT Skill、TalkTrack、HTML PPT Skill、HTML to PPTX、PPT Expert Team、Vela Slides、Paper to LaTeX PPT、SOIL Deck Skills、PPT Master、PPT Image to Editable、Modern PPT、Bruce PPTX Generator、PPT Skill、Xidian Slides Skill、Presentation Forge、Tekion Slide Generator、Paper to Slides Skill、PPT Skills、Editable PPTX Skill、Pitch Deck Iterator、Zhongguose PPT Skill、ZJ Lab Academic PPTX Skills、Research Group PPT Skill、Paper to Scholar Slides、Consulting Diagnosis PPT Skill、Token Slides、Aham PPT、Notrat PPT Studio、Web PPT、Codex XKPPT Skill、High Quality Slides、PPT Design Skill、PowerPoint Skill、Slide Weaver、Competition PPT Skill、HFUT Presentation Studio、SJTU Beamer PPT、Frontend Slides、HTML Report Generator、Demo Prep Skill、Avatar PPT Master、Special Achievement Report、HTML PPT Academic Skill、HTML PPT Video Skill、PPT Template Fill、AI PPT Skill、SVG to PPTX Skill、Doc to PPT Skill、Economics Empirical PPT Skill、SlideSage、USTC PPT Template、Starry Slides、Anthropic PPTX (official)、Baoyu Skills、AI Skills (Cross-Platform)。</sub>

<sub>**共 485 张，全部来自各项目自己的仓库**，按原尺寸完整展示、不做缩略图 —— 幻灯片信息密度高，缩到 300px 根本看不清字体和层次。每张都读自锁定的 commit，出处写在它上方的说明里，并且直接由原仓库提供、没有复制到本仓库。**没有任何一张是本仓库跑出来的**，所以它反映的是每个团队愿意拿出来展示的样子，不是同题横评。用 `python scripts/fetch_samples.py` 重新生成。</sub>
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
- **描述基于文档**，不是基于「我亲手都做过 deck」。登记册里
  <!-- BEGIN:RESEARCHED -->39<!-- END:RESEARCHED --> 个是人工逐个读过 SKILL.md 的，
  其余带 `†` 的只核对了仓库自己写的一句话。我实际跑过的，档案里会写明。
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
