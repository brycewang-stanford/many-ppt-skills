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

请按它的本来面目看：**每一张都是各团队自己挑的那一帧**。一堆宣传图不是同题横评 ——
这些 deck 甚至不是同一份内容，谁也没跑过谁的题。它真正的用处在别处：三十秒之内砍掉
一半候选，而这恰恰是大多数人来这一页要做的事。

<!-- BEGIN:GALLERY -->
#### [PPT Master](https://github.com/hugohe3/ppt-master) · 41,516 ⭐ · PPTX

<sub>把文档或主题变成真正原生可编辑的 PPTX。</sub>

<a href="https://github.com/hugohe3/ppt-master"><img src="https://raw.githubusercontent.com/hugohe3/ppt-master/7ae3721c856fedb921d6acec52c7de69181f5194/docs/assets/screenshots/preview_pritzker_2026.png" width="32.1%" alt="Editorial magazine — Pritzker 2026 architecture review"></a>
<a href="https://github.com/hugohe3/ppt-master"><img src="https://raw.githubusercontent.com/hugohe3/ppt-master/7ae3721c856fedb921d6acec52c7de69181f5194/docs/assets/screenshots/preview_global_ai_capital.png" width="32.1%" alt="Data journalism — Global AI Capital 2026"></a>
<a href="https://github.com/hugohe3/ppt-master"><img src="https://raw.githubusercontent.com/hugohe3/ppt-master/7ae3721c856fedb921d6acec52c7de69181f5194/docs/assets/screenshots/preview_swiss_grid.png" width="32.1%" alt="Swiss typographic grid — Grid Systems primer"></a>
<a href="https://github.com/hugohe3/ppt-master"><img src="https://raw.githubusercontent.com/hugohe3/ppt-master/7ae3721c856fedb921d6acec52c7de69181f5194/docs/assets/screenshots/preview_glassmorphism_demo.png" width="32.1%" alt="Glassmorphism SaaS — AI Agent engineering demo"></a>
<a href="https://github.com/hugohe3/ppt-master"><img src="https://raw.githubusercontent.com/hugohe3/ppt-master/7ae3721c856fedb921d6acec52c7de69181f5194/docs/assets/screenshots/preview_sugar_rush_memphis.png" width="32.1%" alt="Memphis pop — Sugar Rush festival"></a>
<a href="https://github.com/hugohe3/ppt-master"><img src="https://raw.githubusercontent.com/hugohe3/ppt-master/7ae3721c856fedb921d6acec52c7de69181f5194/docs/assets/screenshots/preview_indie_bookstore_zine.png" width="32.1%" alt="Risograph zine — Indie bookstore guide"></a>
<a href="https://github.com/hugohe3/ppt-master"><img src="https://raw.githubusercontent.com/hugohe3/ppt-master/7ae3721c856fedb921d6acec52c7de69181f5194/docs/assets/screenshots/archive/preview_academic_medical.png" width="32.1%" alt="PPT Master sample"></a>
<a href="https://github.com/hugohe3/ppt-master"><img src="https://raw.githubusercontent.com/hugohe3/ppt-master/7ae3721c856fedb921d6acec52c7de69181f5194/docs/assets/screenshots/archive/preview_dark_art_mv.png" width="32.1%" alt="PPT Master sample"></a>
<a href="https://github.com/hugohe3/ppt-master"><img src="https://raw.githubusercontent.com/hugohe3/ppt-master/7ae3721c856fedb921d6acec52c7de69181f5194/docs/assets/screenshots/archive/preview_launch_xiaomi.png" width="32.1%" alt="PPT Master sample"></a>

<sub>取自 [`hugohe3/ppt-master`](https://github.com/hugohe3/ppt-master) 的 267 张图中的 9 张，靠前的几张是项目自己放在 README 里的</sub>

#### [Frontend Slides](https://github.com/zarazhangrui/frontend-slides) · 26,461 ⭐ · HTML

<sub>用 Coding Agent 的前端能力做好看的网页幻灯片。</sub>

<a href="https://github.com/zarazhangrui/frontend-slides"><img src="https://raw.githubusercontent.com/zarazhangrui/beautiful-html-templates/e5e204fb1f3b06290846e7dcd7aceddabeceec8c/screenshots/soft-editorial-4.png" width="32.1%" alt="Soft Editorial — slide 4"></a>
<a href="https://github.com/zarazhangrui/frontend-slides"><img src="https://raw.githubusercontent.com/zarazhangrui/beautiful-html-templates/e5e204fb1f3b06290846e7dcd7aceddabeceec8c/screenshots/soft-editorial-6.png" width="32.1%" alt="Soft Editorial — slide 6"></a>
<a href="https://github.com/zarazhangrui/frontend-slides"><img src="https://raw.githubusercontent.com/zarazhangrui/beautiful-html-templates/e5e204fb1f3b06290846e7dcd7aceddabeceec8c/screenshots/soft-editorial-10.png" width="32.1%" alt="Soft Editorial — slide 10"></a>
<a href="https://github.com/zarazhangrui/frontend-slides"><img src="https://raw.githubusercontent.com/zarazhangrui/beautiful-html-templates/e5e204fb1f3b06290846e7dcd7aceddabeceec8c/screenshots/editorial-forest-1.png" width="32.1%" alt="Editorial Forest — slide 1"></a>
<a href="https://github.com/zarazhangrui/frontend-slides"><img src="https://raw.githubusercontent.com/zarazhangrui/beautiful-html-templates/e5e204fb1f3b06290846e7dcd7aceddabeceec8c/screenshots/editorial-forest-2.png" width="32.1%" alt="Editorial Forest — slide 2"></a>
<a href="https://github.com/zarazhangrui/frontend-slides"><img src="https://raw.githubusercontent.com/zarazhangrui/beautiful-html-templates/e5e204fb1f3b06290846e7dcd7aceddabeceec8c/screenshots/editorial-forest-5.png" width="32.1%" alt="Editorial Forest — slide 5"></a>
<a href="https://github.com/zarazhangrui/frontend-slides"><img src="https://raw.githubusercontent.com/zarazhangrui/beautiful-html-templates/e5e204fb1f3b06290846e7dcd7aceddabeceec8c/screenshots/pin-and-paper-1.png" width="32.1%" alt="Pin & Paper — slide 1"></a>
<a href="https://github.com/zarazhangrui/frontend-slides"><img src="https://raw.githubusercontent.com/zarazhangrui/beautiful-html-templates/e5e204fb1f3b06290846e7dcd7aceddabeceec8c/screenshots/pin-and-paper-11.png" width="32.1%" alt="Pin & Paper — slide 11"></a>
<a href="https://github.com/zarazhangrui/frontend-slides"><img src="https://raw.githubusercontent.com/zarazhangrui/beautiful-html-templates/e5e204fb1f3b06290846e7dcd7aceddabeceec8c/screenshots/pin-and-paper-3.png" width="32.1%" alt="Pin & Paper — slide 3"></a>

<sub>取自 [`zarazhangrui/frontend-slides`](https://github.com/zarazhangrui/frontend-slides) 的 102 张图中的 9 张，靠前的几张是项目自己放在 README 里的</sub>

#### [Guizang PPT Skill](https://github.com/op7418/guizang-ppt-skill) · 22,564 ⭐ · HTML

<sub>杂志编辑风与瑞士国际风 HTML 幻灯片，以「锁死约束」保证一致性。</sub>

<a href="https://github.com/op7418/guizang-ppt-skill"><img src="https://github.com/user-attachments/assets/5dc316a2-401c-4e37-9123-ea081b6ae470" width="32.1%" alt="Style A 电子杂志风效果展示"></a>
<a href="https://github.com/op7418/guizang-ppt-skill"><img src="https://github.com/user-attachments/assets/8960e78c-69bb-4b7e-aa95-6fad64b70314" width="32.1%" alt="Style B 瑞士国际主义效果展示"></a>
<a href="https://github.com/op7418/guizang-ppt-skill"><img src="https://github.com/user-attachments/assets/df21dbcb-5fe4-4852-a91a-a9cf00aceeb4" width="32.1%" alt="墨水经典主题预览"></a>
<a href="https://github.com/op7418/guizang-ppt-skill"><img src="https://github.com/user-attachments/assets/99ce0fd2-72a6-4368-a75a-a8e21657a537" width="32.1%" alt="靛蓝瓷主题预览"></a>
<a href="https://github.com/op7418/guizang-ppt-skill"><img src="https://github.com/user-attachments/assets/bcc1cc4c-5e8e-4467-ae8d-f5801ae73657" width="32.1%" alt="森林墨主题预览"></a>
<a href="https://github.com/op7418/guizang-ppt-skill"><img src="https://github.com/user-attachments/assets/dfea080e-e916-417e-93cd-0a3628de84ca" width="32.1%" alt="牛皮纸主题预览"></a>
<a href="https://github.com/op7418/guizang-ppt-skill"><img src="https://github.com/user-attachments/assets/f3705592-9a72-4dbc-9818-df3aea61bc75" width="32.1%" alt="沙丘主题预览"></a>
<a href="https://github.com/op7418/guizang-ppt-skill"><img src="https://github.com/user-attachments/assets/c02d02f7-ce6f-4e16-b8a6-778c96851f94" width="32.1%" alt="克莱因蓝瑞士主题预览"></a>
<a href="https://github.com/op7418/guizang-ppt-skill"><img src="https://github.com/user-attachments/assets/c310a8c4-5d28-450e-b49a-6ac5b6ba4785" width="32.1%" alt="柠檬黄瑞士主题预览"></a>

<sub>取自 [`op7418/guizang-ppt-skill`](https://github.com/op7418/guizang-ppt-skill) 的 13 张图中的 9 张，靠前的几张是项目自己放在 README 里的</sub>

#### [Huashu Design](https://github.com/alchaincyf/huashu-design) · 22,135 ⭐ · 双路线

<sub>HTML 原生设计 skill —— 高保真原型、幻灯片、动效与设计评审，不止是 PPT。</sub>

<a href="https://github.com/alchaincyf/huashu-design"><img src="https://raw.githubusercontent.com/alchaincyf/huashu-design/1572d431f1411c82ec0baea94dea6a45f6063b26/assets/showcases/ppt/ppt-build.png" width="32.1%" alt="Huashu Design sample"></a>
<a href="https://github.com/alchaincyf/huashu-design"><img src="https://raw.githubusercontent.com/alchaincyf/huashu-design/1572d431f1411c82ec0baea94dea6a45f6063b26/assets/showcases/ppt/ppt-pentagram.png" width="32.1%" alt="Huashu Design sample"></a>
<a href="https://github.com/alchaincyf/huashu-design"><img src="https://raw.githubusercontent.com/alchaincyf/huashu-design/1572d431f1411c82ec0baea94dea6a45f6063b26/assets/showcases/ppt/ppt-takram.png" width="32.1%" alt="Huashu Design sample"></a>
<a href="https://github.com/alchaincyf/huashu-design"><img src="https://raw.githubusercontent.com/alchaincyf/huashu-design/1572d431f1411c82ec0baea94dea6a45f6063b26/assets/showcases/website-ai-nav/ainav-build.png" width="32.1%" alt="Huashu Design sample"></a>
<a href="https://github.com/alchaincyf/huashu-design"><img src="https://raw.githubusercontent.com/alchaincyf/huashu-design/1572d431f1411c82ec0baea94dea6a45f6063b26/assets/showcases/website-ai-nav/ainav-pentagram.png" width="32.1%" alt="Huashu Design sample"></a>
<a href="https://github.com/alchaincyf/huashu-design"><img src="https://raw.githubusercontent.com/alchaincyf/huashu-design/1572d431f1411c82ec0baea94dea6a45f6063b26/assets/showcases/website-ai-nav/ainav-takram.png" width="32.1%" alt="Huashu Design sample"></a>
<a href="https://github.com/alchaincyf/huashu-design"><img src="https://raw.githubusercontent.com/alchaincyf/huashu-design/1572d431f1411c82ec0baea94dea6a45f6063b26/assets/showcases/website-ai-writing/aiwriting-build.png" width="32.1%" alt="Huashu Design sample"></a>
<a href="https://github.com/alchaincyf/huashu-design"><img src="https://raw.githubusercontent.com/alchaincyf/huashu-design/1572d431f1411c82ec0baea94dea6a45f6063b26/assets/showcases/website-ai-writing/aiwriting-pentagram.png" width="32.1%" alt="Huashu Design sample"></a>
<a href="https://github.com/alchaincyf/huashu-design"><img src="https://raw.githubusercontent.com/alchaincyf/huashu-design/1572d431f1411c82ec0baea94dea6a45f6063b26/assets/showcases/website-ai-writing/aiwriting-takram.png" width="32.1%" alt="Huashu Design sample"></a>

<sub>取自 [`alchaincyf/huashu-design`](https://github.com/alchaincyf/huashu-design) 的 24 张图中的 9 张</sub>

#### [HTML PPT Studio](https://github.com/lewislulu/html-ppt-skill) · 7,437 ⭐ · HTML

<sub>24 主题 × 31 布局 × 20+ 动效的专业 HTML 演示。</sub>

<a href="https://github.com/lewislulu/html-ppt-skill"><img src="https://raw.githubusercontent.com/lewislulu/html-ppt-skill/f3a8435d3901697d5ac5e64d356c933637e43107/docs/readme/themes.png" width="32.1%" alt="36 themes · 8 of them"></a>
<a href="https://github.com/lewislulu/html-ppt-skill"><img src="https://raw.githubusercontent.com/lewislulu/html-ppt-skill/f3a8435d3901697d5ac5e64d356c933637e43107/docs/readme/templates.png" width="32.1%" alt="14 full-deck templates"></a>
<a href="https://github.com/lewislulu/html-ppt-skill"><img src="https://raw.githubusercontent.com/lewislulu/html-ppt-skill/f3a8435d3901697d5ac5e64d356c933637e43107/docs/readme/layouts.png" width="32.1%" alt="31 single-page layouts"></a>
<a href="https://github.com/lewislulu/html-ppt-skill"><img src="https://raw.githubusercontent.com/lewislulu/html-ppt-skill/f3a8435d3901697d5ac5e64d356c933637e43107/docs/readme/layouts-live.gif" width="32.1%" alt="31 layouts auto-cycling through real template files"></a>
<a href="https://github.com/lewislulu/html-ppt-skill"><img src="https://raw.githubusercontent.com/lewislulu/html-ppt-skill/f3a8435d3901697d5ac5e64d356c933637e43107/docs/readme/hero.gif" width="32.1%" alt="html-ppt — cover with live previews"></a>
<a href="https://github.com/lewislulu/html-ppt-skill"><img src="https://raw.githubusercontent.com/lewislulu/html-ppt-skill/f3a8435d3901697d5ac5e64d356c933637e43107/docs/readme/presenter-mode.png" width="32.1%" alt="Presenter mode with 4 magnetic cards"></a>
<a href="https://github.com/lewislulu/html-ppt-skill"><img src="https://raw.githubusercontent.com/lewislulu/html-ppt-skill/f3a8435d3901697d5ac5e64d356c933637e43107/docs/readme/animations.png" width="32.1%" alt="47 animations — 27 CSS + 20 canvas FX"></a>
<a href="https://github.com/lewislulu/html-ppt-skill"><img src="https://raw.githubusercontent.com/lewislulu/html-ppt-skill/f3a8435d3901697d5ac5e64d356c933637e43107/scripts/verify-output/animation-showcase/animation-showcase_01.png" width="32.1%" alt="HTML PPT Studio sample"></a>
<a href="https://github.com/lewislulu/html-ppt-skill"><img src="https://raw.githubusercontent.com/lewislulu/html-ppt-skill/f3a8435d3901697d5ac5e64d356c933637e43107/scripts/verify-output/animation-showcase/animation-showcase_02.png" width="32.1%" alt="HTML PPT Studio sample"></a>

<sub>取自 [`lewislulu/html-ppt-skill`](https://github.com/lewislulu/html-ppt-skill) 的 63 张图中的 9 张，靠前的几张是项目自己放在 README 里的</sub>

#### [open-slide](https://github.com/1weiho/open-slide) · 6,027 ⭐ · 框架

<sub>为 Agent 而生的幻灯片框架 —— React 组件渲染到固定 1920×1080 画布。</sub>

<a href="https://github.com/1weiho/open-slide"><img src="https://github.com/user-attachments/assets/02f5e6d7-12a7-4a8e-88e7-ae8770a96584" width="32.1%" alt="open-slide github cover"></a>
<a href="https://github.com/1weiho/open-slide"><img src="https://raw.githubusercontent.com/1weiho/open-slide/35dc46ca27716ea86f8a76710bbd3640e9590628/apps/demo/slides/open-slide-on-replit/assets/replit-features-result.webp" width="32.1%" alt="open-slide sample"></a>
<a href="https://github.com/1weiho/open-slide"><img src="https://raw.githubusercontent.com/1weiho/open-slide/35dc46ca27716ea86f8a76710bbd3640e9590628/apps/demo/slides/open-slide-on-replit/assets/create-slide-skill.webp" width="32.1%" alt="open-slide sample"></a>
<a href="https://github.com/1weiho/open-slide"><img src="https://raw.githubusercontent.com/1weiho/open-slide/35dc46ca27716ea86f8a76710bbd3640e9590628/apps/demo/slides/open-slide-on-replit/assets/openslide-home.webp" width="32.1%" alt="open-slide sample"></a>
<a href="https://github.com/1weiho/open-slide"><img src="https://raw.githubusercontent.com/1weiho/open-slide/35dc46ca27716ea86f8a76710bbd3640e9590628/apps/demo/slides/open-slide-on-replit/assets/replit-agent-home.webp" width="32.1%" alt="open-slide sample"></a>
<a href="https://github.com/1weiho/open-slide"><img src="https://raw.githubusercontent.com/1weiho/open-slide/35dc46ca27716ea86f8a76710bbd3640e9590628/apps/web/public/assets/screenshots/assets-manager.webp" width="32.1%" alt="open-slide sample"></a>
<a href="https://github.com/1weiho/open-slide"><img src="https://raw.githubusercontent.com/1weiho/open-slide/35dc46ca27716ea86f8a76710bbd3640e9590628/apps/web/public/assets/screenshots/inspector.webp" width="32.1%" alt="open-slide sample"></a>
<a href="https://github.com/1weiho/open-slide"><img src="https://raw.githubusercontent.com/1weiho/open-slide/35dc46ca27716ea86f8a76710bbd3640e9590628/apps/web/public/assets/screenshots/presenter.webp" width="32.1%" alt="open-slide sample"></a>
<a href="https://github.com/1weiho/open-slide"><img src="https://raw.githubusercontent.com/1weiho/open-slide/35dc46ca27716ea86f8a76710bbd3640e9590628/apps/web/public/assets/screenshots/theme.webp" width="32.1%" alt="open-slide sample"></a>

<sub>取自 [`1weiho/open-slide`](https://github.com/1weiho/open-slide) 的 16 张图中的 9 张，靠前的几张是项目自己放在 README 里的</sub>

#### [Beautiful HTML Templates](https://github.com/zarazhangrui/beautiful-html-templates) · 3,918 ⭐ · 模板库

<sub>34 套 HTML 幻灯片模板，配 index.json 元数据供任意 Agent 检索选用。</sub>

<a href="https://github.com/zarazhangrui/beautiful-html-templates"><img src="https://raw.githubusercontent.com/zarazhangrui/beautiful-html-templates/e5e204fb1f3b06290846e7dcd7aceddabeceec8c/screenshots/soft-editorial-4.png" width="32.1%" alt="Soft Editorial — slide 4"></a>
<a href="https://github.com/zarazhangrui/beautiful-html-templates"><img src="https://raw.githubusercontent.com/zarazhangrui/beautiful-html-templates/e5e204fb1f3b06290846e7dcd7aceddabeceec8c/screenshots/soft-editorial-6.png" width="32.1%" alt="Soft Editorial — slide 6"></a>
<a href="https://github.com/zarazhangrui/beautiful-html-templates"><img src="https://raw.githubusercontent.com/zarazhangrui/beautiful-html-templates/e5e204fb1f3b06290846e7dcd7aceddabeceec8c/screenshots/soft-editorial-10.png" width="32.1%" alt="Soft Editorial — slide 10"></a>
<a href="https://github.com/zarazhangrui/beautiful-html-templates"><img src="https://raw.githubusercontent.com/zarazhangrui/beautiful-html-templates/e5e204fb1f3b06290846e7dcd7aceddabeceec8c/screenshots/editorial-forest-1.png" width="32.1%" alt="Editorial Forest — slide 1"></a>
<a href="https://github.com/zarazhangrui/beautiful-html-templates"><img src="https://raw.githubusercontent.com/zarazhangrui/beautiful-html-templates/e5e204fb1f3b06290846e7dcd7aceddabeceec8c/screenshots/editorial-forest-2.png" width="32.1%" alt="Editorial Forest — slide 2"></a>
<a href="https://github.com/zarazhangrui/beautiful-html-templates"><img src="https://raw.githubusercontent.com/zarazhangrui/beautiful-html-templates/e5e204fb1f3b06290846e7dcd7aceddabeceec8c/screenshots/editorial-forest-5.png" width="32.1%" alt="Editorial Forest — slide 5"></a>
<a href="https://github.com/zarazhangrui/beautiful-html-templates"><img src="https://raw.githubusercontent.com/zarazhangrui/beautiful-html-templates/e5e204fb1f3b06290846e7dcd7aceddabeceec8c/screenshots/pin-and-paper-1.png" width="32.1%" alt="Pin & Paper — slide 1"></a>
<a href="https://github.com/zarazhangrui/beautiful-html-templates"><img src="https://raw.githubusercontent.com/zarazhangrui/beautiful-html-templates/e5e204fb1f3b06290846e7dcd7aceddabeceec8c/screenshots/pin-and-paper-11.png" width="32.1%" alt="Pin & Paper — slide 11"></a>
<a href="https://github.com/zarazhangrui/beautiful-html-templates"><img src="https://raw.githubusercontent.com/zarazhangrui/beautiful-html-templates/e5e204fb1f3b06290846e7dcd7aceddabeceec8c/screenshots/pin-and-paper-3.png" width="32.1%" alt="Pin & Paper — slide 3"></a>

<sub>取自 [`zarazhangrui/beautiful-html-templates`](https://github.com/zarazhangrui/beautiful-html-templates) 的 102 张图中的 9 张，靠前的几张是项目自己放在 README 里的</sub>

#### [PPT Agent Workflow San](https://github.com/mucsbr/ppt-agent-workflow-san) · 617 ⭐ · HTML

<sub>渐进交互式 PPT 生成 skill。</sub>

<a href="https://github.com/mucsbr/ppt-agent-workflow-san"><img src="https://raw.githubusercontent.com/mucsbr/ppt-agent-workflow-san/801cd2bd46c3cc4ca2c846ff28da2d9284816cd9/2.png" width="32.1%" alt="html-slide-to-pptx-preview"></a>
<a href="https://github.com/mucsbr/ppt-agent-workflow-san"><img src="https://raw.githubusercontent.com/mucsbr/ppt-agent-workflow-san/801cd2bd46c3cc4ca2c846ff28da2d9284816cd9/1.png" width="32.1%" alt="ppt-workflow-preview"></a>
<a href="https://github.com/mucsbr/ppt-agent-workflow-san"><img src="https://raw.githubusercontent.com/mucsbr/ppt-agent-workflow-san/801cd2bd46c3cc4ca2c846ff28da2d9284816cd9/ppt-workflow/01-cover.png" width="32.1%" alt="PPT Agent Workflow San sample"></a>
<a href="https://github.com/mucsbr/ppt-agent-workflow-san"><img src="https://raw.githubusercontent.com/mucsbr/ppt-agent-workflow-san/801cd2bd46c3cc4ca2c846ff28da2d9284816cd9/ppt-workflow/02-core-conclusion.png" width="32.1%" alt="PPT Agent Workflow San sample"></a>
<a href="https://github.com/mucsbr/ppt-agent-workflow-san"><img src="https://raw.githubusercontent.com/mucsbr/ppt-agent-workflow-san/801cd2bd46c3cc4ca2c846ff28da2d9284816cd9/ppt-workflow/03-positioning.png" width="32.1%" alt="PPT Agent Workflow San sample"></a>
<a href="https://github.com/mucsbr/ppt-agent-workflow-san"><img src="https://raw.githubusercontent.com/mucsbr/ppt-agent-workflow-san/801cd2bd46c3cc4ca2c846ff28da2d9284816cd9/ppt-workflow/04-users-scenarios.png" width="32.1%" alt="PPT Agent Workflow San sample"></a>
<a href="https://github.com/mucsbr/ppt-agent-workflow-san"><img src="https://raw.githubusercontent.com/mucsbr/ppt-agent-workflow-san/801cd2bd46c3cc4ca2c846ff28da2d9284816cd9/ppt-workflow/05-growth-flywheel.png" width="32.1%" alt="PPT Agent Workflow San sample"></a>
<a href="https://github.com/mucsbr/ppt-agent-workflow-san"><img src="https://raw.githubusercontent.com/mucsbr/ppt-agent-workflow-san/801cd2bd46c3cc4ca2c846ff28da2d9284816cd9/ppt-workflow/06-competition.png" width="32.1%" alt="PPT Agent Workflow San sample"></a>
<a href="https://github.com/mucsbr/ppt-agent-workflow-san"><img src="https://raw.githubusercontent.com/mucsbr/ppt-agent-workflow-san/801cd2bd46c3cc4ca2c846ff28da2d9284816cd9/ppt-workflow/07-risks.png" width="32.1%" alt="PPT Agent Workflow San sample"></a>

<sub>取自 [`mucsbr/ppt-agent-workflow-san`](https://github.com/mucsbr/ppt-agent-workflow-san) 的 10 张图中的 9 张，靠前的几张是项目自己放在 README 里的</sub>

#### [Frontend Slides Editable](https://github.com/archlizheng/frontend-slides-editable) · 445 ⭐ · 双路线

<sub>可编辑 HTML 幻灯片：拖拽缩放、页序调整、本地保存、PPTX 互转。</sub>

<a href="https://github.com/archlizheng/frontend-slides-editable"><img src="https://raw.githubusercontent.com/archlizheng/frontend-slides-editable/e5663e6a0bdc2c2a673198bab3fb61036a7f20ee/docs/preset-previews/cobalt-grid-cover.png" width="32.1%" alt="Cobalt Grid editable deck preview"></a>
<a href="https://github.com/archlizheng/frontend-slides-editable"><img src="https://raw.githubusercontent.com/archlizheng/frontend-slides-editable/e5663e6a0bdc2c2a673198bab3fb61036a7f20ee/docs/preset-previews/studio-volt-cover.png" width="32.1%" alt="Studio editable deck preview"></a>
<a href="https://github.com/archlizheng/frontend-slides-editable"><img src="https://raw.githubusercontent.com/archlizheng/frontend-slides-editable/e5663e6a0bdc2c2a673198bab3fb61036a7f20ee/docs/preset-previews/soft-editorial-cover.png" width="32.1%" alt="Soft Editorial editable deck preview"></a>
<a href="https://github.com/archlizheng/frontend-slides-editable"><img src="https://raw.githubusercontent.com/archlizheng/frontend-slides-editable/e5663e6a0bdc2c2a673198bab3fb61036a7f20ee/docs/preset-previews/bold-signal-cover.png" width="32.1%" alt="Bold Signal — first slide"></a>
<a href="https://github.com/archlizheng/frontend-slides-editable"><img src="https://raw.githubusercontent.com/archlizheng/frontend-slides-editable/e5663e6a0bdc2c2a673198bab3fb61036a7f20ee/docs/preset-previews/electric-studio-cover.png" width="32.1%" alt="Electric Studio — first slide"></a>
<a href="https://github.com/archlizheng/frontend-slides-editable"><img src="https://raw.githubusercontent.com/archlizheng/frontend-slides-editable/e5663e6a0bdc2c2a673198bab3fb61036a7f20ee/docs/preset-previews/creative-voltage-cover.png" width="32.1%" alt="Creative Voltage — first slide"></a>
<a href="https://github.com/archlizheng/frontend-slides-editable"><img src="https://raw.githubusercontent.com/archlizheng/frontend-slides-editable/e5663e6a0bdc2c2a673198bab3fb61036a7f20ee/docs/preset-previews/dark-botanical-cover.png" width="32.1%" alt="Dark Botanical — first slide"></a>
<a href="https://github.com/archlizheng/frontend-slides-editable"><img src="https://raw.githubusercontent.com/archlizheng/frontend-slides-editable/e5663e6a0bdc2c2a673198bab3fb61036a7f20ee/docs/preset-previews/notebook-tabs-cover.png" width="32.1%" alt="Notebook Tabs — first slide"></a>
<a href="https://github.com/archlizheng/frontend-slides-editable"><img src="https://raw.githubusercontent.com/archlizheng/frontend-slides-editable/e5663e6a0bdc2c2a673198bab3fb61036a7f20ee/docs/preset-previews/pastel-geometry-cover.png" width="32.1%" alt="Pastel Geometry — first slide"></a>

<sub>取自 [`archlizheng/frontend-slides-editable`](https://github.com/archlizheng/frontend-slides-editable) 的 114 张图中的 9 张，靠前的几张是项目自己放在 README 里的</sub>

#### [PPT SVG Generator](https://github.com/vigorX777/ppt-svg-generator) · 248 ⭐ · PPTX

<sub>Markdown → PPT / PDF，经 SVG 中转，多种预设风格。</sub>

<a href="https://github.com/vigorX777/ppt-svg-generator"><img src="https://github.com/user-attachments/assets/2454e688-d3b8-40a2-a3f8-893bbe5060ee" width="48%" alt="image"></a>
<a href="https://github.com/vigorX777/ppt-svg-generator"><img src="https://github.com/user-attachments/assets/97847c7f-5dc3-4a39-b4d8-ee3dc7d0396b" width="48%" alt="PixPin_2026-01-25_15-58-40"></a>

<sub>取自 [`vigorX777/ppt-svg-generator`](https://github.com/vigorX777/ppt-svg-generator) 的 2 张图中的 2 张，靠前的几张是项目自己放在 README 里的</sub>

#### [Mck PPT Design System](https://github.com/likaku/Mck-ppt-design-skill) · 229 ⭐ · PPTX

<sub>咨询公司风设计系统：70 种布局，扁平设计，python-pptx。</sub>

<a href="https://github.com/likaku/Mck-ppt-design-skill"><img src="https://github.com/user-attachments/assets/075ec46d-dd73-4454-92d0-84184b78d276" width="32.1%" alt="Cover"></a>
<a href="https://github.com/likaku/Mck-ppt-design-skill"><img src="https://github.com/user-attachments/assets/3b25f071-8a81-48e3-a62b-9d9be9026f2e" width="32.1%" alt="Content"></a>
<a href="https://github.com/likaku/Mck-ppt-design-skill"><img src="https://github.com/user-attachments/assets/be327c14-aff9-459f-89b0-d4a8bffaabfc" width="32.1%" alt="Table"></a>
<a href="https://github.com/likaku/Mck-ppt-design-skill"><img src="https://github.com/user-attachments/assets/687cee47-13bb-4d6b-840f-77f8e001a62b" width="32.1%" alt="4-Column"></a>
<a href="https://github.com/likaku/Mck-ppt-design-skill"><img src="https://github.com/user-attachments/assets/41371c47-608f-4857-9bfe-791121ec1579" width="32.1%" alt="Colors"></a>
<a href="https://github.com/likaku/Mck-ppt-design-skill"><img src="https://github.com/user-attachments/assets/c5b6e52a-fd91-4c28-88a4-82fdfedfd956" width="32.1%" alt="Summary"></a>

<sub>取自 [`likaku/Mck-ppt-design-skill`](https://github.com/likaku/Mck-ppt-design-skill) 的 6 张图中的 6 张，靠前的几张是项目自己放在 README 里的</sub>

#### [PPT Agent Skill](https://github.com/Akxan/ppt-agent-skill) · 114 ⭐ · HTML

<sub>26 种风格、18 种图表，对标 Linear / Anthropic / Stripe / Apple / NYT。</sub>

<a href="https://github.com/Akxan/ppt-agent-skill"><img src="https://raw.githubusercontent.com/Akxan/ppt-agent-skill/01825dee2ad40a8c719824252605396b9a570d57/assets/hero-all.png" width="32.1%" alt="26 风格预览"></a>
<a href="https://github.com/Akxan/ppt-agent-skill"><img src="https://raw.githubusercontent.com/Akxan/ppt-agent-skill/01825dee2ad40a8c719824252605396b9a570d57/assets/architecture.png" width="32.1%" alt="系统架构图"></a>
<a href="https://github.com/Akxan/ppt-agent-skill"><img src="https://raw.githubusercontent.com/Akxan/ppt-agent-skill/01825dee2ad40a8c719824252605396b9a570d57/assets/hero-vibrant.png" width="32.1%" alt="活力鲜明 4 风格"></a>
<a href="https://github.com/Akxan/ppt-agent-skill"><img src="https://raw.githubusercontent.com/Akxan/ppt-agent-skill/01825dee2ad40a8c719824252605396b9a570d57/assets/hero-natural-retro.png" width="32.1%" alt="自然/复古 4 风格"></a>
<a href="https://github.com/Akxan/ppt-agent-skill"><img src="https://raw.githubusercontent.com/Akxan/ppt-agent-skill/01825dee2ad40a8c719824252605396b9a570d57/assets/hero-dark-professional.png" width="32.1%" alt="暗色专业 7 风格"></a>
<a href="https://github.com/Akxan/ppt-agent-skill"><img src="https://raw.githubusercontent.com/Akxan/ppt-agent-skill/01825dee2ad40a8c719824252605396b9a570d57/assets/hero-light-premium.png" width="32.1%" alt="浅色高级 8 风格"></a>
<a href="https://github.com/Akxan/ppt-agent-skill"><img src="https://raw.githubusercontent.com/Akxan/ppt-agent-skill/01825dee2ad40a8c719824252605396b9a570d57/assets/hero-cultural-oriental.png" width="32.1%" alt="东方文化 3 风格"></a>
<a href="https://github.com/Akxan/ppt-agent-skill"><img src="https://raw.githubusercontent.com/Akxan/ppt-agent-skill/01825dee2ad40a8c719824252605396b9a570d57/ppt-output/style-gallery/bauhaus_block.png" width="32.1%" alt="PPT Agent Skill sample"></a>
<a href="https://github.com/Akxan/ppt-agent-skill"><img src="https://raw.githubusercontent.com/Akxan/ppt-agent-skill/01825dee2ad40a8c719824252605396b9a570d57/ppt-output/style-gallery/blue_white.png" width="32.1%" alt="PPT Agent Skill sample"></a>

<sub>取自 [`Akxan/ppt-agent-skill`](https://github.com/Akxan/ppt-agent-skill) 的 33 张图中的 9 张，靠前的几张是项目自己放在 README 里的</sub>

#### [HTML Slides](https://github.com/bluedusk/html-slides) · 70 ⭐ · HTML

<sub>带演讲者备注的 HTML 幻灯片，配套放映 app。</sub>

<a href="https://github.com/bluedusk/html-slides"><img src="https://raw.githubusercontent.com/bluedusk/html-slides/d8289f4c317905cc5d0ca265d32b791e6cb387b7/eval/content/assets/screenshot.jpg" width="32.1%" alt="HTML Slides sample"></a>
<a href="https://github.com/bluedusk/html-slides"><img src="https://raw.githubusercontent.com/bluedusk/html-slides/d8289f4c317905cc5d0ca265d32b791e6cb387b7/testing/assets/screenshot.jpg" width="32.1%" alt="HTML Slides sample"></a>
<a href="https://github.com/bluedusk/html-slides"><img src="https://raw.githubusercontent.com/bluedusk/html-slides/d8289f4c317905cc5d0ca265d32b791e6cb387b7/eval/content/assets/hero.jpg" width="32.1%" alt="HTML Slides sample"></a>
<a href="https://github.com/bluedusk/html-slides"><img src="https://raw.githubusercontent.com/bluedusk/html-slides/d8289f4c317905cc5d0ca265d32b791e6cb387b7/testing/assets/hero.jpg" width="32.1%" alt="HTML Slides sample"></a>

<sub>取自 [`bluedusk/html-slides`](https://github.com/bluedusk/html-slides) 的 4 张图中的 4 张</sub>

#### [KingDee PPT Skill](https://github.com/WayneZhon/KingDee-PPT-Skill) · 56 ⭐ · HTML

<sub>将内容快速生成金蝶风格 PPT。</sub>

<a href="https://github.com/WayneZhon/KingDee-PPT-Skill"><img src="https://raw.githubusercontent.com/WayneZhon/KingDee-PPT-Skill/28ca93aadeefc91fcc64152714ddeece15f13e1d/assets/closing_thanks.png" width="84%" alt="KingDee PPT Skill sample"></a>

<sub>取自 [`WayneZhon/KingDee-PPT-Skill`](https://github.com/WayneZhon/KingDee-PPT-Skill) 的 1 张图中的 1 张</sub>

#### [Slide Creator](https://github.com/kaisersong/slide-creator) · 46 ⭐ · 双路线

<sub>AI 规划 + 风格发现 + PPTX 导出。</sub>

<a href="https://github.com/kaisersong/slide-creator"><img src="https://raw.githubusercontent.com/kaisersong/slide-creator/d0cf041e3a87db2ac75f8f583fc91a600e369e70/demos/screenshots/strategy-consulting.png" width="32.1%" alt="Strategy Consulting"></a>
<a href="https://github.com/kaisersong/slide-creator"><img src="https://raw.githubusercontent.com/kaisersong/slide-creator/d0cf041e3a87db2ac75f8f583fc91a600e369e70/demos/screenshots/blue-sky.png" width="32.1%" alt="Blue Sky"></a>
<a href="https://github.com/kaisersong/slide-creator"><img src="https://raw.githubusercontent.com/kaisersong/slide-creator/d0cf041e3a87db2ac75f8f583fc91a600e369e70/demos/screenshots/bold-signal.png" width="32.1%" alt="Bold Signal"></a>
<a href="https://github.com/kaisersong/slide-creator"><img src="https://raw.githubusercontent.com/kaisersong/slide-creator/d0cf041e3a87db2ac75f8f583fc91a600e369e70/demos/screenshots/electric-studio.png" width="32.1%" alt="Electric Studio"></a>
<a href="https://github.com/kaisersong/slide-creator"><img src="https://raw.githubusercontent.com/kaisersong/slide-creator/d0cf041e3a87db2ac75f8f583fc91a600e369e70/demos/screenshots/creative-voltage.png" width="32.1%" alt="Creative Voltage"></a>
<a href="https://github.com/kaisersong/slide-creator"><img src="https://raw.githubusercontent.com/kaisersong/slide-creator/d0cf041e3a87db2ac75f8f583fc91a600e369e70/demos/screenshots/dark-botanical.png" width="32.1%" alt="Dark Botanical"></a>
<a href="https://github.com/kaisersong/slide-creator"><img src="https://raw.githubusercontent.com/kaisersong/slide-creator/d0cf041e3a87db2ac75f8f583fc91a600e369e70/demos/screenshots/notebook-tabs.png" width="32.1%" alt="Notebook Tabs"></a>
<a href="https://github.com/kaisersong/slide-creator"><img src="https://raw.githubusercontent.com/kaisersong/slide-creator/d0cf041e3a87db2ac75f8f583fc91a600e369e70/demos/screenshots/pastel-geometry.png" width="32.1%" alt="Pastel Geometry"></a>
<a href="https://github.com/kaisersong/slide-creator"><img src="https://raw.githubusercontent.com/kaisersong/slide-creator/d0cf041e3a87db2ac75f8f583fc91a600e369e70/demos/screenshots/split-pastel.png" width="32.1%" alt="Split Pastel"></a>

<sub>取自 [`kaisersong/slide-creator`](https://github.com/kaisersong/slide-creator) 的 23 张图中的 9 张，靠前的几张是项目自己放在 README 里的</sub>

#### [next-slide](https://github.com/codesstar/next-slide) · 43 ⭐ · HTML

<sub>「你的下个 slide，何必是 PPT」—— 26+ 风格，零依赖，中英双语。</sub>

<a href="https://github.com/codesstar/next-slide"><img src="https://raw.githubusercontent.com/codesstar/next-slide/e92c1b2506e6cf5acff7d2b92339ba0c0ce2af22/scenarios/images/arc-electric-lifestyle.webp" width="32.1%" alt="next-slide sample"></a>
<a href="https://github.com/codesstar/next-slide"><img src="https://raw.githubusercontent.com/codesstar/next-slide/e92c1b2506e6cf5acff7d2b92339ba0c0ce2af22/scenarios/images/arc-lifestyle-running.webp" width="32.1%" alt="next-slide sample"></a>
<a href="https://github.com/codesstar/next-slide"><img src="https://raw.githubusercontent.com/codesstar/next-slide/e92c1b2506e6cf5acff7d2b92339ba0c0ce2af22/scenarios/images/arc-noir-case.webp" width="32.1%" alt="next-slide sample"></a>
<a href="https://github.com/codesstar/next-slide"><img src="https://raw.githubusercontent.com/codesstar/next-slide/e92c1b2506e6cf5acff7d2b92339ba0c0ce2af22/scenarios/images/jinxiufang-lifestyle.webp" width="32.1%" alt="next-slide sample"></a>
<a href="https://github.com/codesstar/next-slide"><img src="https://raw.githubusercontent.com/codesstar/next-slide/e92c1b2506e6cf5acff7d2b92339ba0c0ce2af22/scenarios/images/motion-brand-showcase.webp" width="32.1%" alt="next-slide sample"></a>
<a href="https://github.com/codesstar/next-slide"><img src="https://raw.githubusercontent.com/codesstar/next-slide/e92c1b2506e6cf5acff7d2b92339ba0c0ce2af22/scenarios/images/xiaomi-smart-home-lifestyle.webp" width="32.1%" alt="next-slide sample"></a>
<a href="https://github.com/codesstar/next-slide"><img src="https://raw.githubusercontent.com/codesstar/next-slide/e92c1b2506e6cf5acff7d2b92339ba0c0ce2af22/scenarios/images/shanyin-tea-product.webp" width="32.1%" alt="next-slide sample"></a>
<a href="https://github.com/codesstar/next-slide"><img src="https://raw.githubusercontent.com/codesstar/next-slide/e92c1b2506e6cf5acff7d2b92339ba0c0ce2af22/scenarios/images/agent-eval.webp" width="32.1%" alt="next-slide sample"></a>
<a href="https://github.com/codesstar/next-slide"><img src="https://raw.githubusercontent.com/codesstar/next-slide/e92c1b2506e6cf5acff7d2b92339ba0c0ce2af22/scenarios/images/agent-hero.webp" width="32.1%" alt="next-slide sample"></a>

<sub>取自 [`codesstar/next-slide`](https://github.com/codesstar/next-slide) 的 60 张图中的 9 张</sub>

#### [Slide Writer](https://github.com/FeeiCN/slide-writer) · 40 ⭐ · HTML

<sub>从想法、大纲、文档或演讲稿生成企业级 HTML 演示。</sub>

<a href="https://github.com/FeeiCN/slide-writer"><img src="https://raw.githubusercontent.com/FeeiCN/slide-writer/3c4524c4abb3310fdee106282d0a64f156fd4ff6/examples/before-after.png" width="32.1%" alt="Slide-Writer Demo"></a>
<a href="https://github.com/FeeiCN/slide-writer"><img src="https://raw.githubusercontent.com/FeeiCN/slide-writer/3c4524c4abb3310fdee106282d0a64f156fd4ff6/examples/slide-writer.png" width="32.1%" alt="Slide-Writer"></a>
<a href="https://github.com/FeeiCN/slide-writer"><img src="https://raw.githubusercontent.com/FeeiCN/slide-writer/3c4524c4abb3310fdee106282d0a64f156fd4ff6/examples/test-antgroup-eric.png" width="32.1%" alt="Slide Writer sample"></a>
<a href="https://github.com/FeeiCN/slide-writer"><img src="https://raw.githubusercontent.com/FeeiCN/slide-writer/3c4524c4abb3310fdee106282d0a64f156fd4ff6/examples/test-tencent-pony-ma.png" width="32.1%" alt="Slide Writer sample"></a>
<a href="https://github.com/FeeiCN/slide-writer"><img src="https://raw.githubusercontent.com/FeeiCN/slide-writer/3c4524c4abb3310fdee106282d0a64f156fd4ff6/examples/test-alibaba-jack-ma.png" width="32.1%" alt="Slide Writer sample"></a>

<sub>取自 [`FeeiCN/slide-writer`](https://github.com/FeeiCN/slide-writer) 的 5 张图中的 5 张，靠前的几张是项目自己放在 README 里的</sub>

#### [Skills Slides](https://github.com/nghiahsgs/skills-slides) · 30 ⭐ · HTML

<sub>50 美学 × 20 配色 × 10 字体 × 5 布局 × 30+ 特效 = 5 万种组合。</sub>

<a href="https://github.com/nghiahsgs/skills-slides"><img src="https://raw.githubusercontent.com/nghiahsgs/skills-slides/c271d3cda03bf79733cc91ba28e25716196638b7/examples/screenshots/slide-06-features.png" width="32.1%" alt="Feature grid — 6 cards with 3D tilt hover"></a>
<a href="https://github.com/nghiahsgs/skills-slides"><img src="https://raw.githubusercontent.com/nghiahsgs/skills-slides/c271d3cda03bf79733cc91ba28e25716196638b7/examples/screenshots/slide-07-checklist.png" width="32.1%" alt="Anti-slop checklist — 10-point quality gate"></a>
<a href="https://github.com/nghiahsgs/skills-slides"><img src="https://raw.githubusercontent.com/nghiahsgs/skills-slides/c271d3cda03bf79733cc91ba28e25716196638b7/examples/screenshots/slide-01-title.png" width="32.1%" alt="Skills Slides sample"></a>
<a href="https://github.com/nghiahsgs/skills-slides"><img src="https://raw.githubusercontent.com/nghiahsgs/skills-slides/c271d3cda03bf79733cc91ba28e25716196638b7/examples/screenshots/slide-03-50k.png" width="32.1%" alt="Skills Slides sample"></a>

<sub>取自 [`nghiahsgs/skills-slides`](https://github.com/nghiahsgs/skills-slides) 的 4 张图中的 4 张，靠前的几张是项目自己放在 README 里的</sub>

#### [PowerPoint Fancy Design](https://github.com/Phlegonlabs/Powerpoint-fancy-design) · 27 ⭐ · 双路线

<sub>结构化 Markdown → 1600×900 HTML 幻灯片 + PNG 渲染 + 可导出。</sub>

<a href="https://github.com/Phlegonlabs/Powerpoint-fancy-design"><img src="https://raw.githubusercontent.com/Phlegonlabs/Powerpoint-fancy-design/d6167dbc5d1ee9a0f3b2b90b399156322e9178ae/assets/style-preview-a.png" width="32.1%" alt="Swiss International"></a>
<a href="https://github.com/Phlegonlabs/Powerpoint-fancy-design"><img src="https://raw.githubusercontent.com/Phlegonlabs/Powerpoint-fancy-design/d6167dbc5d1ee9a0f3b2b90b399156322e9178ae/assets/style-preview-b.png" width="32.1%" alt="East Asian Minimalism"></a>
<a href="https://github.com/Phlegonlabs/Powerpoint-fancy-design"><img src="https://raw.githubusercontent.com/Phlegonlabs/Powerpoint-fancy-design/d6167dbc5d1ee9a0f3b2b90b399156322e9178ae/assets/style-preview-c.png" width="32.1%" alt="Risograph Print"></a>
<a href="https://github.com/Phlegonlabs/Powerpoint-fancy-design"><img src="https://raw.githubusercontent.com/Phlegonlabs/Powerpoint-fancy-design/d6167dbc5d1ee9a0f3b2b90b399156322e9178ae/assets/style-preview-d.png" width="32.1%" alt="Bauhaus Geometry"></a>
<a href="https://github.com/Phlegonlabs/Powerpoint-fancy-design"><img src="https://raw.githubusercontent.com/Phlegonlabs/Powerpoint-fancy-design/d6167dbc5d1ee9a0f3b2b90b399156322e9178ae/assets/style-preview-e.png" width="32.1%" alt="Organic Handcrafted"></a>
<a href="https://github.com/Phlegonlabs/Powerpoint-fancy-design"><img src="https://raw.githubusercontent.com/Phlegonlabs/Powerpoint-fancy-design/d6167dbc5d1ee9a0f3b2b90b399156322e9178ae/assets/style-preview-f.png" width="32.1%" alt="Art Deco Luxury"></a>
<a href="https://github.com/Phlegonlabs/Powerpoint-fancy-design"><img src="https://raw.githubusercontent.com/Phlegonlabs/Powerpoint-fancy-design/d6167dbc5d1ee9a0f3b2b90b399156322e9178ae/assets/style-preview-g.png" width="32.1%" alt="Neo Brutalism"></a>
<a href="https://github.com/Phlegonlabs/Powerpoint-fancy-design"><img src="https://raw.githubusercontent.com/Phlegonlabs/Powerpoint-fancy-design/d6167dbc5d1ee9a0f3b2b90b399156322e9178ae/assets/style-preview-h.png" width="32.1%" alt="Retro Futurism"></a>
<a href="https://github.com/Phlegonlabs/Powerpoint-fancy-design"><img src="https://raw.githubusercontent.com/Phlegonlabs/Powerpoint-fancy-design/d6167dbc5d1ee9a0f3b2b90b399156322e9178ae/assets/style-preview-i.png" width="32.1%" alt="Dark Editorial"></a>

<sub>取自 [`Phlegonlabs/Powerpoint-fancy-design`](https://github.com/Phlegonlabs/Powerpoint-fancy-design) 的 30 张图中的 9 张，靠前的几张是项目自己放在 README 里的</sub>

#### [PPTX from Layouts](https://github.com/tristan-mcinnis/pptx-from-layouts-skill) · 9 ⭐ · PPTX

<sub>严格通过模板母版版式，从 Markdown 生成 PPTX。</sub>

<a href="https://github.com/tristan-mcinnis/pptx-from-layouts-skill"><img src="https://raw.githubusercontent.com/tristan-mcinnis/pptx-from-layouts-skill/53b0e750694d807e3510c2017744197c3c5089b0/docs/pipeline.png" width="48%" alt="PPTX-from-layouts pipeline"></a>
<a href="https://github.com/tristan-mcinnis/pptx-from-layouts-skill"><img src="https://raw.githubusercontent.com/tristan-mcinnis/pptx-from-layouts-skill/53b0e750694d807e3510c2017744197c3c5089b0/examples/q1-strategy/thumbnail.jpg" width="48%" alt="PPTX from Layouts sample"></a>

<sub>取自 [`tristan-mcinnis/pptx-from-layouts-skill`](https://github.com/tristan-mcinnis/pptx-from-layouts-skill) 的 2 张图中的 2 张，靠前的几张是项目自己放在 README 里的</sub>

<sub>以下项目的仓库里没有可用图片：Anthropic PPTX (official)、Visual Explainer、Claude Office Skills、Academic PPTX、Visual Cognition Slides、Huawei Style PPT Skill。</sub>

<sub>**共 141 张，全部来自各项目自己的仓库。** 每张都读自锁定的 commit，并链回出处。**没有任何一张是本仓库跑出来的**，所以它反映的是每个团队愿意拿出来展示的样子，不是同题横评。用 `python scripts/fetch_samples.py` 重新生成。</sub>
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
