# Many PPT Skills — AI 幻灯片 Skill 生态调研

> 一份关于「用 Coding Agent 做 PPT」这件事的全景调研：主流 Skill 清单、技术路线对比、选型建议，以及从这些项目里提炼出的设计方法论。
>
> **数据快照：2026-07-28**（Star 数为当日 GitHub API 实时抓取，非二手榜单转载）

---

## TL;DR

1. **2026 年上半年，「PPT Skill」是 Agent Skill 生态里最卷的一个赛道。** 短短半年冒出 30+ 个认真做的项目，头部四个项目合计超过 11 万 star。
2. **赛道分裂成两条技术路线**：**HTML-native**（产出浏览器里放映的单文件 HTML）和 **Native PPTX**（产出真正可编辑的 .pptx）。两条路线解决的是不同的问题，不是互相替代关系。
3. **Zara Zhang（[@zarazhangrui](https://github.com/zarazhangrui)）是 HTML-native 路线的定义者**。她的 [frontend-slides](https://github.com/zarazhangrui/frontend-slides)（26.5k ⭐）不是第一个做 HTML 幻灯片的，但它把 **"show, don't tell" 的审美发现流程**和**反 AI slop 的设计约束**变成了这个品类的事实标准 —— 后来者几乎都在抄它的交互范式。
4. **单看 star，最大的是 [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master)（41.5k ⭐）**，走的是 Native PPTX 路线。它在中文 HTML-slide 榜单里常被漏掉，因为不算「HTML slide skill」。
5. **官方兜底方案是 Anthropic 的 [pptx skill](https://github.com/anthropics/skills/tree/main/skills/pptx)**，基于 `pptxgenjs` + OOXML 直改，能力全但不管审美。

---

## 目录

- [一、这个赛道为什么会存在](#一这个赛道为什么会存在)
- [二、两条技术路线](#二两条技术路线)
- [三、Zara Zhang 与 frontend-slides](#三zara-zhang-与-frontend-slides)
- [四、主流 Skill 全表](#四主流-skill-全表)
- [五、头部项目逐个拆解](#五头部项目逐个拆解)
- [六、选型指南](#六选型指南)
- [七、从这些项目里提炼的方法论](#七从这些项目里提炼的方法论)
- [八、安装方式速查](#八安装方式速查)
- [九、参考来源](#九参考来源)

---

## 一、这个赛道为什么会存在

传统 AI PPT 工具（Gamma、Beautiful.ai 之类）的问题是：模板池是固定的，你能做出来的东西上限就是模板的上限，而且做出来一眼就是「AI 做的」。

Coding Agent 的出现改变了约束条件 —— 如果 Agent 会写 CSS，那它的设计自由度就是 CSS 的自由度，而不是某个模板库的自由度。Zara Zhang 那条引爆这个赛道的推文说得最直白：

> "The world hasn't woken up to the fact that **code can create much better slides than most PPT tools**."
> — [@zarazhangrui, 2026-01](https://x.com/zarazhangrui/status/2016337615843434646)

配合上 Anthropic 在 2025 年底推出的 **Agent Skills** 规范（`SKILL.md` + 渐进式披露 + 脚本），把「做好 PPT 的工作流和最佳实践」打包成可分发资产这件事，第一次有了标准格式。于是 2026 年 1—7 月，这个赛道爆炸了。

---

## 二、两条技术路线

| | **HTML-native 路线** | **Native PPTX 路线** |
|---|---|---|
| **产出** | 单文件 `.html`，浏览器全屏放映 | 真正的 `.pptx`，PowerPoint/Keynote 打开 |
| **代表** | frontend-slides、guizang-ppt-skill、huashu-design、html-ppt-skill | ppt-master、Anthropic 官方 pptx、Mck-ppt-design-skill |
| **技术栈** | 手写 HTML/CSS/JS，固定 1920×1080 舞台 + `transform: scale()` 自适应 | `python-pptx` / `pptxgenjs` / 直改 OOXML / SVG→DrawingML |
| **设计自由度** | ★★★★★ 任何 Chrome 能渲染的效果都能用 | ★★★☆☆ 受 OOXML 表达能力限制 |
| **动效** | ★★★★★ CSS/WebGL 全开 | ★★☆☆☆ PPT 原生转场与动画 |
| **可交付性** | 需要浏览器；客户不能用 PPT 改 | 甲方/领导可以直接改，能进公司模板体系 |
| **版本控制** | ★★★★★ 纯文本 diff | ★☆☆☆☆ 二进制 |
| **典型场景** | 技术分享、路演、发布会、个人品牌 | 咨询报告、投标、汇报、需要交付给非技术方 |

**关键判断：这不是「新旧之争」。** 决定你选哪条的不是审美偏好，而是一个很现实的问题 —— **交付物之后还要不要被别人用 PowerPoint 二次编辑？** 要，就走 PPTX；不要，就走 HTML，能好看很多。

也有项目在做**融合**：[huashu-design](https://github.com/alchaincyf/huashu-design) 同时输出 HTML 和「保留文本框的可编辑 PPTX」；[archlizheng/frontend-slides-editable](https://github.com/archlizheng/frontend-slides-editable) 给 HTML 加了拖拽编辑和 PPTX 互转。

---

## 三、Zara Zhang 与 frontend-slides

### 3.1 人物背景

**Zara Zhang（张睿）**，GitHub [@zarazhangrui](https://github.com/zarazhangrui)，X [@zarazhangrui](https://x.com/zarazhangrui)，个人站 [zarazhang.com](http://www.zarazhang.com/)。GitHub 自我介绍是 "AI tinkerer"，12k+ followers，18 个公开仓库但总 star 数超过 4 万 —— 是那种**产出密度极高的独立开发者/内容创作者**类型，不是团队。

她的仓库有个非常一致的模式：**每个都是一个 Agent Skill，每个都解决一个「把 A 格式的内容变成 B 格式的漂亮东西」的问题**。

| 仓库 | ⭐ | 做什么 |
|---|---:|---|
| **[frontend-slides](https://github.com/zarazhangrui/frontend-slides)** | **26,459** | **用前端能力做 HTML 幻灯片（本文主角）** |
| [follow-builders](https://github.com/zarazhangrui/follow-builders) | 5,998 | 监控 X/YouTube 上的 AI builder，做成摘要 |
| [codebase-to-course](https://github.com/zarazhangrui/codebase-to-course) | 5,290 | 把任意代码库变成交互式单页 HTML 课程 |
| **[beautiful-html-templates](https://github.com/zarazhangrui/beautiful-html-templates)** | **3,918** | **34 个 HTML 幻灯片模板库，给 Agent 选用** |
| [lark-coding-agent-bridge](https://github.com/zarazhangrui/lark-coding-agent-bridge) | 2,021 | 飞书 ↔ Claude Code/Codex 的桥接 bot |
| [tab-out](https://github.com/zarazhangrui/tab-out) | 1,704 | 标签页管理 Chrome 扩展 |
| [beautiful-feishu-whiteboard](https://github.com/zarazhangrui/beautiful-feishu-whiteboard) | 597 | 35 套配色，做飞书白板 |
| [youtube-to-ebook](https://github.com/zarazhangrui/youtube-to-ebook) | 521 | YouTube 字幕 → EPUB 电子书 |
| [personalized-podcast](https://github.com/zarazhangrui/personalized-podcast) | 407 | 任意内容 → 个性化 AI 播客 |

### 3.2 frontend-slides 是什么

> Create beautiful slides on the web using a coding agent's frontend skills

- **26,459 ⭐ / 2,148 fork / MIT**
- 创建于 **2026-01-28**，半年做到 2.6 万 star —— 平均每天 ~145 star
- 语言：JavaScript，Topics：`ai-slides` `claude-skill` `generative-ui` `vibe-coding`

**核心能力：**
- 产出**零依赖单文件 HTML**，固定 16:9（1920×1080）
- **12 个 curated 预设风格** + **34 个 bold 设计模板**
- **PPT → Web 转换**（用 `python-pptx` 抽取原稿内容和图片，再重新设计）
- 一键部署 Vercel 拿分享链接；Playwright 导出 PDF

### 3.3 最重要的创新：Phase 2「show, don't tell」

这是 frontend-slides 对整个赛道影响最大的东西，值得单独讲。

**问题**：Agent 问你「你想要什么风格？」是个糟糕的问题。大部分人**说不出**自己要什么风格，但**看到了就知道**喜不喜欢。

**frontend-slides 的解法**：不问，直接生成 **3 个真实预览**让你选 ——

1. 一个 **safe preset**（12 个预设里挑最匹配的）
2. 一个 **bold template**（34 个模板包里挑）
3. 一个 **wildcard**（第二个 bold 模板，或者完全自定义设计）

而且 SKILL.md 里明确规定了 **preview authenticity**：每个预览必须看起来像是**你这份 deck 的真实首页**，不能是抽象色卡或者占位符。

Zara 自己的表述：

> "You don't need to be a designer to make beautiful things. **You just need to react to what you see.**"

这个范式后来被 huashu-design（"Fallback Advisor：生成 3 个平行视觉方向"）、kaisersong/slide-creator（"style discovery"）等一堆项目直接沿用。

### 3.4 第二个创新：把「反 AI slop」写成硬约束

SKILL.md 里有一整套**明确禁止**的东西，目标是让产出不像 AI 做的：

- **字体**：禁用 Inter / Roboto / Arial，必须从 Fontshare 或 Google Fonts 里挑有性格的
- **配色**：必须有**主导色 + 尖锐强调色**，禁止「怯懦的均匀分布」
- **背景**：必须有氛围（渐变、纹理），禁止纯色平铺
- **动效**：要**入场时的 staggered reveal 大效果**，而不是散落各处的微交互
- **元数据泄漏**：绝不能把 "Option A/B/C"、模板名、内部注释渲染到幻灯片上

有意思的是 **Anthropic 官方 pptx skill 里也有同款条款**：明确禁止「标题下的装饰线」和「装饰色条」，理由是 *"these signal AI generation"*。两边独立收敛到同一个结论，说明这确实是 AI 生成物的通用指纹。

### 3.5 第三个值得学的：固定舞台（Fixed 16:9 Stage）

SKILL.md 把这条标为 **Non-Negotiable**：

- 每页活在固定 **1920×1080** 画布里，整体等比 `scale` 到视口
- **内容永不为移动端重排** —— 视口比例不对就加黑边（letterbox/pillarbox）
- 切页用 `.active` / `.visible` class 控制，**不用 `display: none`**（保住 CSS 过渡动画）
- 禁止任何会重排幻灯片内容的响应式断点

这条看着「反 Web 直觉」，但它是对的：**幻灯片是印刷品，不是网页**。放弃响应式换来的是「所见即所得，投影仪上不会崩」。这个约定后来被 open-slide、guizang 等基本原样继承，已经是这个品类的通用规范。

### 3.6 工程上的一课：渐进式披露（Progressive Disclosure）

在 7.8k star 的时候，Zara 重构了 SKILL.md：

> "I just restructured it following the 'progressive disclosure' pattern: went from **1,625 lines loaded every time to 183**. Same functionality, **89% less context bloat**. Treat your instruction file like a table of contents."
> — [@zarazhangrui](https://x.com/zarazhangrui/status/2029092514435932647)

现在的文件结构就是这个思路的体现 —— `SKILL.md` 是**地图**，其余按需加载：

```
SKILL.md              (28KB)  流程地图，永远加载
STYLE_PRESETS.md      (8KB)   12 个预设，只在选风格时加载
bold-template-pack/           34 套设计系统 + 精简元数据
html-template.md      (11KB)  HTML 结构
viewport-base.css     (2.7KB) 必须整份内联进产物的基础 CSS
animation-patterns.md (4KB)   动效参考
scripts/                      PPT 抽取 / 部署 / PDF 导出
```

**这是写任何 Skill 都该学的模式**，不限于 PPT。

### 3.7 她是怎么做出来的（方法论本身很有价值）

> 1. 让 Claude Code 做一个看起来像幻灯片的网站
> 2. **迭代几十次**，直到它满足我对「好幻灯片」的标准
> 3. 让 Claude 把我们刚走过的**工作流和最佳实践变成一个 skill**
>
> — [@zarazhangrui](https://x.com/zarazhangrui/status/2028152141072994717)

即：**Skill 不是设计出来的，是从大量真实迭代里蒸馏出来的。** 先自己把一件事做到满意，再让 Agent 把过程固化。这可能是整份调研里最可迁移的一条经验。

### 3.8 增长轨迹

| 时间点 | Star | 来源 |
|---|---:|---|
| 2026-01-28 | 仓库创建 | GitHub API |
| ~2026-02 | 1k | [X](https://x.com/zarazhangrui/status/2025798415154921961) |
| ~2026-03 | 7.8k（重构为渐进式披露） | [X](https://x.com/zarazhangrui/status/2029092514435932647) |
| ~2026-03 | 10k | [X](https://x.com/zarazhangrui/status/2034331675363279338) |
| ~2026-06 | 20k（加入模板、网页发布、内联编辑） | [X](https://x.com/zarazhangrui/status/2061889286585405790) |
| **2026-07-28** | **26,459** | GitHub API |

---

## 四、主流 Skill 全表

> Star 数为 2026-07-28 GitHub API 实时数据，按 star 降序。

### Tier S — 头部（5k+ ⭐）

| 项目 | ⭐ | 路线 | License | 一句话 |
|---|---:|---|---|---|
| [hugohe3/**ppt-master**](https://github.com/hugohe3/ppt-master) | 41,513 | PPTX | MIT | 文档/主题 → 原生可编辑 PPTX，含原生形状/图表/转场/旁白音频 |
| [zarazhangrui/**frontend-slides**](https://github.com/zarazhangrui/frontend-slides) | 26,459 | HTML | MIT | HTML-native 路线的定义者，"show don't tell" 风格发现 |
| [op7418/**guizang-ppt-skill**](https://github.com/op7418/guizang-ppt-skill) | 22,561 | HTML | AGPL-3.0 | 歸藏出品，杂志编辑风 + 瑞士国际风，锁定式设计约束 |
| [alchaincyf/**huashu-design**](https://github.com/alchaincyf/huashu-design) | 22,133 | HTML+PPTX | MIT | 花生出品，20 设计哲学 + 5 维评审 + MP4 导出，泛设计 skill |
| [nicobailon/visual-explainer](https://github.com/nicobailon/visual-explainer) | 9,346 | HTML | MIT | 面向工程场景：图表、diff 评审、方案审计、项目复盘 |
| [lewislulu/html-ppt-skill](https://github.com/lewislulu/html-ppt-skill) | 7,436 | HTML | MIT | HTML PPT Studio，24 主题 × 31 布局 × 20+ 动效 |
| [1weiho/open-slide](https://github.com/1weiho/open-slide) | 6,027 | HTML/React | MIT | 不是 skill 是**框架**：React 组件 + 演讲者模式 + 浏览器内批注 |

### Tier A — 生产可用（100—5000 ⭐）

| 项目 | ⭐ | 路线 | License | 一句话 |
|---|---:|---|---|---|
| [zarazhangrui/beautiful-html-templates](https://github.com/zarazhangrui/beautiful-html-templates) | 3,918 | 模板库 | MIT | 34 套模板 + `index.json` 元数据，供 Agent 检索选用 |
| [tfriedel/claude-office-skills](https://github.com/tfriedel/claude-office-skills) | 798 | PPTX | — | PPTX/DOCX/XLSX/PDF 全家桶，Office 自动化 |
| [Gabberflast/academic-pptx-skill](https://github.com/Gabberflast/academic-pptx-skill) | 722 | PPTX | MIT | 学术演讲专用：行动式标题、论证结构、引用规范 |
| [mucsbr/ppt-agent-workflow-san](https://github.com/mucsbr/ppt-agent-workflow-san) | 617 | HTML | — | 渐进交互式 PPT 生成 |
| [archlizheng/frontend-slides-editable](https://github.com/archlizheng/frontend-slides-editable) | 445 | HTML+PPTX | MIT | frontend-slides 的可编辑分支：拖拽调整、重排、PPTX 互转 |
| [vigorX777/ppt-svg-generator](https://github.com/vigorX777/ppt-svg-generator) | 248 | SVG→PPT/PDF | MIT | Markdown → PPT/PDF，5 种预设风格 |
| [likaku/Mck-ppt-design-skill](https://github.com/likaku/Mck-ppt-design-skill) | 229 | PPTX | Apache-2.0 | 麦肯锡咨询风设计系统，70 种布局，`python-pptx` |
| [bytonylee/future-slide-skill](https://github.com/bytonylee/future-slide-skill) | ~135 | HTML | — | （仓库已迁移） |
| [Akxan/ppt-agent-skill](https://github.com/Akxan/ppt-agent-skill) | 114 | HTML | MIT | 26 风格 18 图表，对标 Linear/Stripe/Apple/NYT |

### Tier B — 垂直/新兴（<100 ⭐）

| 项目 | ⭐ | 一句话 |
|---|---:|---|
| [ToseaAI/awesome-html-slide-skills](https://github.com/ToseaAI/awesome-html-slide-skills) | 104 | **本调研的主要线索来源**，HTML slide skill 精选列表 |
| [edu-ai-builders/visual-cognition-slides](https://github.com/edu-ai-builders/visual-cognition-slides) | 81 | 基于认知科学与教学设计，优化知识留存率 |
| [software-ai-life/Awesome-PPT-Design-Skills](https://github.com/software-ai-life/Awesome-PPT-Design-Skills) | 71 | Agent 无关的高端可编辑 PPT 风格集 |
| [bluedusk/html-slides](https://github.com/bluedusk/html-slides) | 70 | 带演讲者备注，配套 HTMLSlides 放映 app |
| [WayneZhon/KingDee-PPT-Skill](https://github.com/WayneZhon/KingDee-PPT-Skill) | 56 | 金蝶企业风 |
| [zuiho-kai/huawei-style-ppt-skill](https://github.com/zuiho-kai/huawei-style-ppt-skill) | 52 | 华为高密度信息风 |
| [kaisersong/slide-creator](https://github.com/kaisersong/slide-creator) | 46 | AI 规划 + 风格发现 + PPTX 导出 |
| [codesstar/next-slide](https://github.com/codesstar/next-slide) | 43 | 「你的下个 slide，何必是 PPT」，26+ 风格，中英双语 |
| [FeeiCN/slide-writer](https://github.com/FeeiCN/slide-writer) | 40 | 企业级 HTML 演示，支持从演讲稿生成 |
| [nghiahsgs/skills-slides](https://github.com/nghiahsgs/skills-slides) | 30 | 50 美学 × 20 配色 × 10 字体 × 5 布局 = 5 万种组合 |
| [Phlegonlabs/Powerpoint-fancy-design](https://github.com/Phlegonlabs/Powerpoint-fancy-design) | 27 | Markdown → 1600×900 HTML + PNG + 可导出 |
| [tristan-mcinnis/pptx-from-layouts-skill](https://github.com/tristan-mcinnis/pptx-from-layouts-skill) | 9 | 严格走模板母版版式生成，企业模板合规场景 |

### 官方基线

| 项目 | ⭐ | 说明 |
|---|---:|---|
| [anthropics/skills](https://github.com/anthropics/skills) → `skills/pptx` | 164,681（整仓） | Anthropic 官方，`pptxgenjs` 建新 + OOXML 直改旧 + `markitdown` 抽文本 |

---

## 五、头部项目逐个拆解

### 🥇 ppt-master — 41.5k ⭐ · Native PPTX 的天花板

**为什么它 star 最高却常在 HTML slide 榜单里缺席**：因为它压根不是 HTML slide skill。它解决的是另一个更「刚需」的问题 —— **甲方要的是能改的 .pptx**。

**技术路线很聪明**：内容 → AI 设计 → **生成 SVG** → `finalize_svg.py` 转成 PowerPoint 原生 **DrawingML**。这样既拿到了 SVG 的设计表达力，产出又是真正的原生对象（形状、连接线、可拖的调整手柄），不是把图片贴进 PPT。

- 原生形状/连接线/调整手柄、数据驱动的原生图表与表格（`--native-charts-and-tables`）
- 转场与动画（进入/强调/退出/路径动画）
- **演讲者备注可转旁白音频**
- 支持自定义 `.pptx` 模板与母版；多画布尺寸（16:9 / 社交媒体）
- 仅需 Python 3.10+，`pip install -r requirements.txt`
- Agent 无关：Cursor / Windsurf / Zed / Claude Code / Copilot / Cline / Codex CLI 都能跑
- **维护极活跃**：v4.2.0 发布于 2026-07-25，1357 commits，3 个 open issue

### 🥈 frontend-slides — 26.5k ⭐ · 见[第三章](#三zara-zhang-与-frontend-slides)

### 🥉 guizang-ppt-skill — 22.6k ⭐ · 「设计即约束」

作者 **op7418（歸藏）**，中文 AI 圈知名的设计/AI 内容创作者。

它的理念和 frontend-slides 恰好相反 —— **frontend-slides 给自由，guizang 给约束**：

- 两套视觉系统：**Style A**（10 布局，叙事导向）/ **Style B**（22 个**锁死的**布局，网格化，事实导向）
- 主题色只有预设（A 五套、B 四套），**不允许自定义 hex**
- 内置自动校验
- 可选接 GPT-Image 2.0 生成配图/示意图
- 多平台封面（21:9 / 1:1 / 3:4 / 16:9）
- WebGL 动效 + 低功耗静态降级
- **AGPL-3.0** —— 这是全表里唯一的强 copyleft，商用前请注意

> 「锁死配色和布局」听起来是缺点，实际是对 Agent 最友好的设计：**约束越强，Agent 出错的空间越小，一致性越高**。

### huashu-design — 22.1k ⭐ · 不只是 PPT

作者**花生（alchaincyf）**。严格说它是**泛 HTML 设计 skill**，幻灯片只是它七种交付物之一（还有 App/Web 高保真原型、MP4/GIF 动效、信息图、设计对比等）。

三个值得单独学的设计：

1. **Brand Asset Protocol** —— 五步流程防止 AI 幻觉品牌色：*询问 → 搜索 → 下载 → grep 提取颜色 → 写入 spec*。这是个很实在的反幻觉工程实践。
2. **Fallback Advisor** —— 需求模糊时，用**不同逻辑体系**生成 3 个平行视觉方向（和 Zara 的 show-don't-tell 同源）。
3. **5 维专家评审** —— 哲学一致性 / 视觉层级 / 执行细节 / 功能性 / 创新性，各 0–10 分，出雷达图 + Keep/Fix/Quick Wins 清单。

产出**同时支持 HTML 和保留文本框的可编辑 PPTX**，是少数真正打通两条路线的项目。

### open-slide — 6k ⭐ · 唯一的「框架」而非「Skill」

其他都是**指导层**（告诉 Agent 该怎么写），open-slide 是**运行时**（提供基础设施让 Agent 写的东西能跑好）。

```bash
npx @open-slide/cli init my-slide
```

- 任意 React 组件渲染到固定 1920×1080 画布
- 内置 skill：`/create-slide`（问 4 个问题后生成结构）、`/slide-authoring`（技术参考）、`/apply-comments`
- **浏览器内 inspector**：点某个元素写「把这个改成红色」，Agent 自动应用 —— 这是全表里最好的人机协作回路
- 演讲者模式（备注 + 计时器）、热重载、静态 HTML/PDF 导出、svgl logo 资产管理

**代价**：有 npm 依赖和构建步骤，丢掉了「单文件零依赖」这个 HTML 路线的核心优势。适合**长期反复做 deck 的团队**，不适合一次性交付。

### Anthropic 官方 pptx skill — 基线方案

能力全面但**不管审美**（审美归 `frontend-design` / `theme-factory` 等其他官方 skill 管）。

三条工作流：

| 场景 | 做法 |
|---|---|
| **新建** | 写 `pptxgenjs` 脚本（预装，别 npm install）。注意：先设 layout 再加 slide、hex 不带 `#`、**绝不跨 `add*` 调用复用 options 对象** |
| **改现有/套模板** | 解压 → 改 `ppt/slides/slideN.xml` → 重压。复制页必须用 `scripts/add_slide.py`，删完跑 `scripts/clean.py` 清孤儿资源 |
| **抽文本** | `markitdown deck.pptx`，或 `scripts/thumbnail.py` 出带标注的版式缩略图网格 |

**QA 流水线值得抄**：`markitdown` 查内容 → `validate.py` 查 schema/关系/内容 → `soffice --convert-to pdf` + `pdftoppm` 转图**让模型自己看一眼**。「渲染成图再自检」这一步是保证质量的关键，很多社区 skill 缺这一环。

---

## 六、选型指南

### 决策树

```
交付物需要别人用 PowerPoint 二次编辑吗？
├─ 需要 ──→ Native PPTX 路线
│   ├─ 要最好的视觉 + 原生对象 ──→ ppt-master (41.5k)
│   ├─ 必须套公司现成模板母版 ──→ Anthropic 官方 pptx / pptx-from-layouts-skill
│   ├─ 咨询/投行汇报风 ─────────→ Mck-ppt-design-skill
│   └─ 学术会议/答辩 ───────────→ academic-pptx-skill
│
└─ 不需要 ──→ HTML-native 路线
    ├─ 想要最强设计自由度 + 不知道自己要什么风格
    │                        ──→ frontend-slides ⭐ 首选
    ├─ 要杂志/瑞士风的强一致性，能接受 AGPL
    │                        ──→ guizang-ppt-skill
    ├─ 不止要 PPT，还要原型/动效/信息图
    │                        ──→ huashu-design
    ├─ 团队长期反复做 deck，想要工程化 + 演讲者模式
    │                        ──→ open-slide
    ├─ 做技术图解、代码评审、项目复盘
    │                        ──→ visual-explainer
    └─ 想两头都要（HTML + 可编辑 PPTX）
                             ──→ huashu-design / frontend-slides-editable
```

### 一句话建议

- **只装一个**：`frontend-slides`。它是这个品类的参考实现，交互范式最成熟，社区最大，出问题最容易搜到答案。
- **装两个**：`frontend-slides` + `ppt-master`。覆盖两条路线，基本没有做不了的场景。
- **中文语境高频汇报**：加 `guizang-ppt-skill` 或 `huashu-design`，中文排版和审美更对味。
- **注意 License**：`guizang-ppt-skill` 是 **AGPL-3.0**，其余头部项目基本都是 MIT。商业场景务必先看清楚。

---

## 七、从这些项目里提炼的方法论

这一节是本调研最有价值的部分 —— 抛开具体项目，**这些 30+ 个项目独立收敛出的共识**，就是「让 Agent 做出好设计」的通用规律。

### 1. Show, don't tell —— 不要问审美，要给选项

人**说不出**自己的审美，但**看得出**。任何需要用户表达审美偏好的环节，都应该转化成「生成 2–4 个真实预览让用户挑」。frontend-slides 的 Phase 2、huashu-design 的 Fallback Advisor 都是这个模式。

**推广**：这不只适用于 PPT。任何 Agent 任务里涉及主观品味的决策点，都适用。

### 2. 反 AI slop 要写成**否定式硬约束**

「做得好看点」是无效指令。有效的是明确禁止清单：

| 禁止 | 因为 |
|---|---|
| Inter / Roboto / Arial | 默认字体 = 没做选择 |
| 纯色平铺背景 | 缺乏氛围，一眼模板 |
| 均匀分布的配色 | 「怯懦」，没有视觉焦点 |
| 标题下的装饰线、装饰色条 | **Anthropic 官方点名**：AI 生成的指纹 |
| 散落各处的微交互 | 不如一次有力的入场动效 |

**规律**：模型的默认输出会滑向训练数据的**均值**，而均值就是「AI 味」。所以好的 Skill 主要靠**减法**（禁止什么）而非加法（要求什么）。

### 3. 幻灯片是印刷品，不是网页

固定 1920×1080 舞台 + 等比缩放 + 黑边，**放弃响应式**。这条被几乎所有 HTML 路线项目采纳，已成事实标准。

### 4. 强约束反而出好结果

guizang 锁死配色和布局、Mck-skill 固定 70 种版式、Anthropic 官方一堆 "never do X" 的规则 —— **给 Agent 的自由度越小，一致性和成功率越高**。设计系统的价值在 Agent 时代被放大了。

### 5. 渐进式披露：`SKILL.md` 是目录，不是全文

Zara 的实测数据：**1,625 行 → 183 行，功能不变，context 减少 89%**。主文件只留「什么时候该读哪个文件」的地图，细节全部下沉到按需加载的附属文件。

### 6. 单文件零依赖 = 长期可用

> "Dependencies represent technical debt; **single HTML files outlast frameworks**."

一个内联了所有 CSS/JS 的 HTML 文件，十年后还能打开。一个 npm 项目，两年后 `npm install` 就挂了。open-slide 是唯一的例外，它用工程化换了协作能力。

### 7. 渲染成图，让模型自己看

Anthropic 官方 QA 流水线的最后一步：`soffice --convert-to pdf` → `pdftoppm` → **把图给模型看**。视觉产物必须视觉验收，光看代码是查不出排版问题的。这一步很多社区 skill 缺失，是质量差距的主要来源之一。

### 8. Skill 是蒸馏出来的，不是设计出来的

Zara 的三步法：**自己迭代几十次做到满意 → 让 Agent 把这个过程写成 Skill**。先有好结果，再有 Skill；反过来做基本都失败。

---

## 八、安装方式速查

生态里目前有四种分发方式并存：

```bash
# 1. Claude Code Plugin Marketplace（frontend-slides 推荐方式，分两条消息发）
/plugin marketplace add https://github.com/zarazhangrui/frontend-slides
/plugin install frontend-slides@frontend-slides
# 调用：/frontend-slides:frontend-slides

# 2. 官方 skills marketplace
/plugin install pptx@anthropic-skills

# 3. skills CLI（社区通用，需 v1.5.19+）
npx skills add alchaincyf/huashu-design
npx skills add https://github.com/op7418/guizang-ppt-skill --skill guizang-ppt-skill

# 4. 手动克隆（最通用，任何 Agent 都能用）
git clone https://github.com/zarazhangrui/frontend-slides ~/.claude/skills/frontend-slides
# 调用：/frontend-slides

# 5. 独立 CLI / Python 项目
npx @open-slide/cli init my-slide          # open-slide
pip install -r requirements.txt            # ppt-master（需 Python 3.10+）
```

**给非 Claude Agent 用**（Codex / Cursor / Copilot / Gemini CLI）：绝大多数项目都是 Agent 无关的，直接把 `SKILL.md` 或 `AGENTS.md` 的路径丢给 Agent 让它读就行。

---

## 九、参考来源

### 一手来源（GitHub）
- [zarazhangrui/frontend-slides](https://github.com/zarazhangrui/frontend-slides) · [SKILL.md](https://raw.githubusercontent.com/zarazhangrui/frontend-slides/main/SKILL.md)
- [zarazhangrui/beautiful-html-templates](https://github.com/zarazhangrui/beautiful-html-templates)
- [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master)
- [op7418/guizang-ppt-skill](https://github.com/op7418/guizang-ppt-skill)
- [alchaincyf/huashu-design](https://github.com/alchaincyf/huashu-design)
- [1weiho/open-slide](https://github.com/1weiho/open-slide)
- [anthropics/skills](https://github.com/anthropics/skills) · [skills/pptx/SKILL.md](https://raw.githubusercontent.com/anthropics/skills/main/skills/pptx/SKILL.md)
- 全表 Star / License / 更新时间数据均由 GitHub REST API 于 2026-07-28 实时抓取

### Zara Zhang 本人的表述（X）
- [「代码能做出比大多数 PPT 工具更好的幻灯片」（首发）](https://x.com/zarazhangrui/status/2016337615843434646)
- [「我是怎么做出 frontend-slides 的」三步法](https://x.com/zarazhangrui/status/2028152141072994717)
- [渐进式披露重构：1625 行 → 183 行](https://x.com/zarazhangrui/status/2029092514435932647)
- [10k star](https://x.com/zarazhangrui/status/2034331675363279338) · [20k star + 新功能](https://x.com/zarazhangrui/status/2061889286585405790)
- [个人网站 zarazhang.com](http://www.zarazhang.com/) · [LobeHub · Zara Zhang Top 5 AI Agent Skills](https://lobehub.com/skills/collection/zarazhang)

### 榜单与评测
- [ToseaAI/awesome-html-slide-skills](https://github.com/ToseaAI/awesome-html-slide-skills) —— 本调研的主要线索来源
- [Tosea.ai · 30+ Best HTML Slide Skills 2026](https://tosea.ai/blog/best-html-slide-skills-library-2026) —— S/A/B 三档分级法
- [Claude Directory · Best PowerPoint (PPTX) Skill](https://www.claudedirectory.org/skills/pptx)
- [Claude Skills Hub · Best PowerPoint Skills 2026](https://claudeskills.info/best/ppt-skills/)
- [Felo · 10 Best AI PPT Skills for Claude Code CLI 2026](https://felo.ai/blog/10-best-ai-ppt-skills-claude-code-cli-2026/)
- [Open Design · Claude PPT Skills](https://open-design.ai/blog/claude-ppt-skills/)
- [Firecrawl · Best Claude Code Skills 2026](https://www.firecrawl.dev/blog/best-claude-code-skills)
- [Medium · 30+ Best HTML Slide Skill（Sylvia Chen）](https://medium.com/@2315610426/30-best-html-slide-skill-the-complete-curated-library-for-claude-code-codex-cursor-and-52769bf248ee)

---

## 附：本调研的已知局限

- **Star 数是热度不是质量**。头部几个项目的传播很大程度依赖作者的社交影响力（Zara 在 X、歸藏和花生在中文圈），排名不完全等于实际效果。
- **未做实测对比**。本文基于文档、README、SKILL.md 和公开评测，**没有对每个 skill 跑同一份内容做横向出图对比**。如果要做严肃选型，建议自己拿一份真实材料跑 top 3。
- **`bytonylee/future-slide-skill` 仓库已迁移**，star 数取自二手榜单（~135），未能实时校验。
- 二手榜单（Tosea、Felo、Claude Directory 等）的 star 数普遍滞后，本文表格一律以 API 实时数据为准，两者不一致时以本文为准。
