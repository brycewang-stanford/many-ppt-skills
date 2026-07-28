<div align="center">

# many-ppt-skills

**值得知道的 AI 幻灯片 Skill 全在这一页 —— 用横评代替 star 数排名。**

[English](README.md) · [简体中文](README.zh-CN.md)

<!-- BEGIN:COUNTS -->
**收录 26 个 skill** · **合计 143,031 star** · HTML 路线 13 个 · PPTX 路线 7 个 · 双路线 4 个 · 数据刷新于 **2026-07-28**
<!-- END:COUNTS -->

</div>

---

Coding Agent 把 CSS 写好了，半年之内冒出一整个新品类：把文档变成不像机器做的幻灯片的
Skill。现在有 30+ 个认真做的项目，其中四个 star 数都超过 2 万。

而所有关于它们的排名，都只是 star 数的重新排序。**star 衡量的是作者会不会发推，不能告诉你
这个 skill 会不会把你的营收数字编出来。**

所以这个仓库做两件事：

1. **一份登记册** —— 收录两条路线的全部 skill，带实时数据和「它到底适合干什么」的判断。
   由 [`data/skills.json`](data/skills.json) 自动生成，数字不会悄悄烂掉。
2. **一套横评** —— [同样三份材料跑遍所有 skill](benchmark/)，按
   [公开的评分卡](benchmark/rubric.md) 打分，附截图。七个维度里有两个是**一票否决**的：
   编造数字的 deck，无论多好看都不可能压过老实的那个。

外加从这些项目源码里提炼的 [**八条原则**](principles/) —— 30 个团队各自独立收敛到的同一批
做法，这是这个领域目前最接近「证据」的东西。

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

## 横评

<!-- BEGIN:SCORECARD -->
| 项目 | 总分 | 视觉 | 字体 | 密度 | 数据 | 内容 | 交付 | 代价 | 次数 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| **frontend-slides** | **28.0**/35 | 4.0 | 4.0 | 3.0 | 5.0 | 5.0 | 3.0 | 4.0 | 1 |

<sub>目前仅 1 次实测 —— 远不足以给任何东西排名。分数均为暂定值，每次实测都公开披露其利益冲突。⚠️ = 该次实测在数据或内容保真上被一票否决。</sub>
<!-- END:SCORECARD -->

→ [**协议、语料与评分卡**](benchmark/) · [run-01 详细记录](benchmark/results/run-01/README.md)

**第一次实测已完成** —— [frontend-slides × 季度经营回顾](benchmark/results/run-01/README.md)，
28/35。deck、全部 12 张截图、以及每一项打分的引证都已提交，**你可以自己重新打分**。

它查出两件值得知道的事：这个 skill 的第一原则是「零依赖」，但它自己的模板却规定要外链远程
字体；以及 Signal 模板的选择元数据写着 `density: high`，而它的设计文档却写着「不要让内容
填满超过半页」—— 于是**每一步都正确地遵循 skill，密度依然会做错**。

它还把我自己的工具链打穿了两次，这一点写在记录里，没有藏起来。

> **一次实测不构成排名。** 执行 skill 的人同时写了语料、写了评分卡、还做了打分。这个利益
> 冲突已在 score 文件中披露。请把它当作「工具链能跑通」的证据，而不是对该 skill 的判决。

**三份语料**，各自针对一类特定失败：

| 语料 | 压力测试 | 暴露什么 |
|---|---|---|
| [产品发布](benchmark/corpus/01-product-launch.md) | 高光时刻、低密度 | 模板感、怯懦配色、该放一个观点却堆满 bullet |
| [季度经营回顾](benchmark/corpus/02-quarterly-review.md) | 表格、图表、行动式标题 | **编造数字**、截断的表格 |
| [技术分享](benchmark/corpus/03-tech-talk.md) | 代码、架构图、渐进展开 | 代码变成图片、缩进被破坏 |

**七个维度**，各 0–5 分，满分 35。其中**数据保真**和**内容保真**是**一票否决**：任一项得 0，
总分直接封顶 17。编造了财务数字的漂亮 deck 不是好 deck，是负债。

而且保真度是**机器检查**，不靠肉眼：

```bash
python benchmark/runner/check_fidelity.py \
  --corpus benchmark/corpus/02-quarterly-review.md \
  --deck   benchmark/results/run-01/some-skill/02-quarterly-review/
```

它把两边的数字 token 全抽出来做 diff —— 既抓丢失的数字，更重要的是抓**被编造出来的**数字。
发现编造就返回非零退出码，可以直接卡 CI。

**你能贡献的最有价值的东西是一次独立打分。** 这份登记册是我做的调研，这恰恰让我成为最不该
当唯一评分人的那个人。虽然采用盲评，但那只能缓解偏差，不能消除。
→ [如何贡献一次实测](benchmark/README.md#contributing-a-run)

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
data/skills.json ──▶ 人工调研内容，唯一手写的文件
data/stats.json  ──▶ GitHub 实时数据，CI 每天刷新
        │
        └──▶ scripts/render.py ──▶ 生成两个 README 里的所有表格
```

```bash
python scripts/fetch_stats.py     # 刷新 star / fork / license / 活跃度
python scripts/render.py          # 重新生成两个 README 的全部表格
python scripts/render.py --check  # CI 卡口：README 过期就失败
```

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
