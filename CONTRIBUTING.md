# Contributing

[English](#english) · [简体中文](#简体中文)

---

## English

### What is most valuable

In descending order of how much it helps:

1. **An independent benchmark score** on a pairing that has already been run. This directly
   tests scorer bias, which is the largest known weakness of this project. I did the
   research that built the registry, which makes me the wrong person to be the only scorer.
2. **A benchmark run on a skill with no runs yet** — especially PPTX-route skills, which
   are under-covered relative to how many people actually need editable output.
3. **A corpus that breaks skills in a way the current three do not.** Known gaps: RTL
   languages, dense CJK typography, accessibility requirements, decks over 40 slides.
4. **Chinese translations** of the eight principle files.
5. **A missing skill**, or a correction to how an existing one is described.

### Adding or correcting a skill

Edit **`data/skills.json` only**. Never edit a README table — it is generated, and the next
CI run overwrites it.

```bash
$EDITOR data/skills.json
python scripts/validate_registry.py    # required fields, valid route, no duplicates
python scripts/fetch_stats.py          # pull live GitHub numbers
python scripts/render.py               # regenerate both READMEs
python scripts/check_links.py          # nothing broken
```

Inclusion bar — a skill should meet most of these:

- Publicly available, with a real `SKILL.md` / `AGENTS.md` or equivalent
- Actually about producing slides or decks
- Documented well enough that a stranger could install and run it
- Not a fork of a listed skill with only cosmetic changes

Write `tagline_en` and `tagline_zh` as **what it is**, not as marketing. If you cannot say
what makes it different from the nearest listed alternative, it probably does not need its
own entry.

### Contributing a benchmark run

Read [`benchmark/README.md`](benchmark/README.md) first — the protocol matters more than
the result. Summary:

1. Install the skill. **Record its commit SHA**, the agent, and the model.
2. Paste a corpus file **unmodified**. No hints, no extra style steering.
3. Answer the skill's own interview questions as a reasonable user would, and log what you
   said. That is not a correction turn.
4. Every instruction after that **is** a correction turn. Log each verbatim. Cap at 20.
5. Save output under `benchmark/results/<run-id>/<skill-id>/<corpus-id>/`.
6. Run the fidelity checker **before** you look at the design:
   ```bash
   python benchmark/runner/check_fidelity.py --corpus <corpus> --deck <output-dir>
   ```
7. Screenshot it. Score dimensions 1–3 **from the images**, not from source.
8. Write `score.json` — shape is documented at the top of
   [`benchmark/runner/scorecard.py`](benchmark/runner/scorecard.py). **Every score needs a
   citation.** Uncited scores are stripped in review.
9. `python benchmark/runner/scorecard.py --validate`, then open the PR.

Commit the artifacts — decks, screenshots, transcripts. Anyone must be able to re-score
from your raw material and reach a different conclusion. That is the point.

### If you wrote one of these skills

Two things:

- **If this repo describes your project wrongly, open an issue.** It gets fixed. I would
  rather be corrected than accurate-looking.
- **If a benchmark run of your skill was flawed, say so.** It gets re-run, and the original
  stays visible in git history rather than being quietly deleted.

Authors are welcome to submit runs of their own skill. Mark them `"self_reported": true` in
`score.json` — they are still useful, they just carry a different weight.

### Style

- Prose in the READMEs and principles is hand-written. Tables are generated. Do not blur that line.
- Cite sources. "The author said X" needs a link.
- Say what is uncertain. This repo's credibility rests on being honest about limits, not on
  sounding authoritative.
- No superlatives without evidence. "Best" is a benchmark result, not an adjective.

---

## 简体中文

### 最有价值的贡献

按帮助程度降序：

1. **对已跑过的组合做一次独立打分。** 这直接检验评分人偏差 —— 本项目最大的已知弱点。
   登记册是我做的调研，这恰恰让我成为最不该当唯一评分人的那个人。
2. **对尚无实测的 skill 跑一次** —— 尤其是 PPTX 路线，相对于真正需要可编辑产出的人数而言
   覆盖严重不足。
3. **一份能以现有三份语料无法触及的方式击穿 skill 的新语料。** 已知空白：RTL 语言、高密度
   中日韩排版、无障碍要求、40 页以上的长 deck。
4. **八条原则正文的中文翻译。**
5. **补充遗漏的 skill**，或修正现有条目的描述。

### 新增或修正 skill

**只改 `data/skills.json`。** 永远不要手改 README 里的表格 —— 那是生成的，下次 CI 会覆盖。

```bash
$EDITOR data/skills.json
python scripts/validate_registry.py    # 必填字段、路线合法、无重复
python scripts/fetch_stats.py          # 拉取 GitHub 实时数据
python scripts/render.py               # 重新生成两个 README
python scripts/check_links.py          # 确认没有断链
```

收录门槛 —— 应满足其中大部分：

- 公开可获取，有真实的 `SKILL.md` / `AGENTS.md` 或等价物
- 确实是做幻灯片/演示的
- 文档足以让一个陌生人装上并跑起来
- 不是某个已收录 skill 的纯换皮 fork

`tagline_en` 和 `tagline_zh` 请写**它是什么**，不要写宣传语。如果你说不出它和最接近的那个
已收录项目有什么不同，那它大概不需要单独一条。

### 贡献一次实测

先读 [`benchmark/README.md`](benchmark/README.md) —— **协议比结果更重要**。摘要：

1. 装好 skill。**记录它的 commit SHA**、使用的 agent 和模型。
2. **原样粘贴**语料文件。不给提示，不额外引导风格。
3. skill 自己的问答环节按一个正常用户的方式回答，并记录你说了什么。**那不算修正轮次。**
4. 之后的每一条指令**都算**修正轮次。逐字记录。上限 20 轮。
5. 产物存到 `benchmark/results/<run-id>/<skill-id>/<corpus-id>/`。
6. **在看设计之前**先跑保真度检查：
   ```bash
   python benchmark/runner/check_fidelity.py --corpus <语料> --deck <产物目录>
   ```
7. 截图。维度 1–3 **看图打分**，不要看源码。
8. 写 `score.json` —— 格式见
   [`benchmark/runner/scorecard.py`](benchmark/runner/scorecard.py) 文件头。
   **每个分数都必须有引证。** 无引证的分数在复核时会被剔除。
9. 跑 `python benchmark/runner/scorecard.py --validate`，然后提 PR。

**把产物一起提交** —— deck、截图、对话记录。任何人都必须能基于你的原始材料重新打分并得出
不同结论。这正是重点。

### 如果你是这些 skill 的作者

两件事：

- **如果这里写错了你的项目，请开 issue。** 我会改。我宁可被纠正，也不要看起来准确。
- **如果对你 skill 的某次实测有问题，请直说。** 会重跑，并且原始记录留在 git 历史里，不会
  悄悄删掉。

欢迎作者提交自己 skill 的实测。请在 `score.json` 里标注 `"self_reported": true` ——
它们依然有用，只是权重不同。

### 写作风格

- README 和原则里的正文是手写的，表格是生成的。**不要模糊这条界线。**
- 给出处。「作者说过 X」需要附链接。
- **把不确定的地方说出来。** 这个仓库的可信度建立在诚实交代局限上，而不是听起来权威。
- 没有证据不要用最高级。「最好」是一个跑分结果，不是一个形容词。
