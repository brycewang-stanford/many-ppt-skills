# Eight Principles

**What 30+ teams converged on independently — the closest thing this field has to evidence.**

[English](#english) · [简体中文](#简体中文)

---

## English

These are not opinions about slide design. They are patterns extracted by reading the
`SKILL.md`, `AGENTS.md` and source of every project in [the registry](../README.md), and
keeping only what showed up in multiple projects that had no reason to copy each other.

Convergence is the filter. When a Chinese indie developer, a Silicon Valley tinkerer and
Anthropic's own document team all arrive at the same oddly specific rule, that rule is
probably about how the models actually behave — not about taste.

| | Principle | One line | Strength of evidence |
|---|---|---|---|
| 1 | [Show, don't tell](01-show-dont-tell.md) | Never ask about taste. Generate options and let people point. | ★★★★★ |
| 2 | [Anti-slop is a banned list](02-anti-ai-slop.md) | "Make it beautiful" does nothing. "Never use Inter" does. | ★★★★★ |
| 3 | [Slides are print, not web](03-fixed-stage.md) | Fixed 1920×1080, scale to fit, letterbox. Give up responsive. | ★★★★★ |
| 4 | [Constraint beats freedom](04-constraint-beats-freedom.md) | Lock the palette. Agents get more consistent, not less capable. | ★★★★☆ |
| 5 | [SKILL.md is a table of contents](05-progressive-disclosure.md) | 1,625 lines → 183. Same features, 89% less context. | ★★★★☆ |
| 6 | [Single file outlasts frameworks](06-single-file.md) | Dependencies are debt. Inline everything. | ★★★★☆ |
| 7 | [Render it and look at it](07-render-and-look.md) | Visual output needs visual QA. Let the model see its own work. | ★★★☆☆ |
| 8 | [Distill, don't design](08-distill-dont-design.md) | Do it by hand 30 times, *then* write the skill. | ★★★☆☆ |

**Strength of evidence** reflects how many independent projects encode the rule, and
whether any of them state it as non-negotiable. Five stars means it is near-universal and
at least one project calls it mandatory. Three means it is well-attested but not yet
settled.

### The most transferable ones

If you are writing any agent skill — not just a slide skill — principles
**1**, **5**, **7** and **8** apply unchanged. They are about how to structure instructions
for a model and how to verify its output, and nothing about them is specific to slides.

Principles **2**, **3**, **4** and **6** are about generated design artifacts specifically,
though 2 and 4 generalize to any task where the model's default output trends toward the
bland average of its training data — which is most of them.

### How to read these

Each file follows the same shape:

- **The principle**, stated as plainly as possible
- **The evidence** — who encodes it, with citations
- **Why it works** — the mechanism, not just the observation
- **How to apply it** — concretely, in your own skill
- **Where it breaks** — because a principle with no failure mode is a slogan

---

## 简体中文

这八条不是关于幻灯片设计的观点，而是通读[登记册](../README.zh-CN.md)里每个项目的
`SKILL.md`、`AGENTS.md` 和源码后提取出来的模式 —— 并且只保留了那些**在多个彼此没有抄袭
关系的项目里反复出现**的做法。

**收敛本身就是筛选器。** 当一个中国独立开发者、一个硅谷 tinkerer 和 Anthropic 自家的文档团队
各自抵达同一条如此具体的规则时，那条规则大概率是关于模型的真实行为，而不是关于品味。

| | 原则 | 一句话 | 证据强度 |
|---|---|---|---|
| 1 | [Show, don't tell](01-show-dont-tell.md) | 永远不要问审美。生成选项让人指。 | ★★★★★ |
| 2 | [反 slop 靠禁用清单](02-anti-ai-slop.md) | 「做好看点」没用，「禁用 Inter」有用。 | ★★★★★ |
| 3 | [幻灯片是印刷品](03-fixed-stage.md) | 固定 1920×1080，等比缩放，加黑边。放弃响应式。 | ★★★★★ |
| 4 | [约束胜过自由](04-constraint-beats-freedom.md) | 锁死配色。Agent 会更稳定，而不是更无能。 | ★★★★☆ |
| 5 | [SKILL.md 是目录](05-progressive-disclosure.md) | 1,625 行 → 183 行，功能不变，context 省 89%。 | ★★★★☆ |
| 6 | [单文件比框架活得久](06-single-file.md) | 依赖就是债。全部内联。 | ★★★★☆ |
| 7 | [渲染出来，然后看一眼](07-render-and-look.md) | 视觉产物需要视觉验收。让模型看见自己的作品。 | ★★★☆☆ |
| 8 | [蒸馏，而非设计](08-distill-dont-design.md) | 先手工做三十遍，**再**写 skill。 | ★★★☆☆ |

**证据强度**反映有多少个独立项目编码了这条规则，以及是否有项目把它列为不可协商。五星表示
接近普遍共识且至少有一个项目标为强制；三星表示证据充分但尚未定论。

### 最可迁移的几条

如果你在写**任何** agent skill（不限于幻灯片），第 **1**、**5**、**7**、**8** 条可以原样套用。
它们讲的是「如何为模型组织指令」和「如何验证模型产出」，和幻灯片没有任何绑定关系。

第 **2**、**3**、**4**、**6** 条针对生成式设计产物，但其中 2 和 4 可以推广到任何「模型默认
产出会滑向训练数据平庸均值」的任务 —— 也就是大多数任务。

> **翻译说明：** 八篇正文目前为英文。中文版正在补，欢迎认领 ——
> 见 [CONTRIBUTING.md](../CONTRIBUTING.md)。上表的一句话摘要已包含每条的核心结论。
