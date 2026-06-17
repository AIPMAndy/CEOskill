<div align="center">

# 🧠 CEO Skill

**AI 决策助手，专为高管设计。不只给建议，更会拆解 trade-off、识别认知偏差、预判竞争反应。**

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](./LICENSE)
[![GitHub Stars](https://img.shields.io/github/stars/AIPMAndy/ceo-skill?style=social)](https://github.com/AIPMAndy/ceo-skill)
[![Agent Skill](https://img.shields.io/badge/Type-Agent%20Skill-blue)](./SKILL.md)

[English](./README_EN.md) | **简体中文**

</div>

---

## 👤 关于作者

**我是 Andy**，前腾讯/百度 AI 产品专家 → 大模型独角兽 VP → 持续创业者。

过去 18 个月，我用 AI 做了 100+ 个重大决策：
- ✅ [是否 All-in AI Agent 生态？](./examples/real-andy-case-ai-agent-pivot.md)（结果：建立了中文 AI Skill 第一入口，116 stars）
- ✅ 63 个项目如何砍到 15 个？（优先级排序）
- ✅ CEOskill 如何定价？（$0 vs $99 vs $999）

**这个工具是我提炼的决策方法论**：不是让 AI 给建议，而是让 AI 拆 trade-off、查偏差、推演竞争。

📖 延伸阅读：[为什么 CEOskill 只有 15 stars？](./examples/meta-why-only-15-stars.md)（以及如何改变）

---

## 💡 一句话价值

**普通 AI 会说"建议你做市场调研"，CEO Skill 会说"这是 One-Way Door 决策，你有确认偏差，这里有 4 个选项的 trade-off，竞对可能这样反击，董事会里 2 票支持 1 票反对"。**

---

## 🎯 5 秒自测：你需要它吗？

如果你经常面对这些场景，它就是为你设计的：

| 场景 | 典型问题 |
|------|---------|
| 🎯 **战略决策** | 该不该进新市场？收购还是自建？业务止损还是继续投？ |
| 💰 **资源分配** | 5 个项目只能做 2 个，先做哪个？预算投增长还是产品？ |
| 🔥 **危机响应** | CTO 要去竞对，2 小时内先做什么？线上事故怎么处理？ |
| 🤝 **利益相关者** | 董事会、投资人、管理层怎么对齐？组织调整怎么管政治？ |
| ⚔️ **竞争推演** | 如果我们降价/上新功能，竞对会怎么反应？ |

---

## ❌ 问题：为什么普通 AI 不够用？

大部分"CEO 顾问型 AI"的通病：

```
用户："我们该不该进入日本市场？"

普通 AI：
"进入日本市场是一个重要的战略决策。您需要考虑市场规模、
竞争格局、本地化成本等因素。建议先做市场调研，评估风险，
制定详细计划。如果您需要，我可以帮您列出一些关键问题..."

❌ 会说漂亮话，但不落地
❌ 会列框架，但不会选框架
❌ 会给建议，但不展示 trade-off
❌ 不检查认知偏差（你是不是因为竞对进了所以想进？）
❌ 不预判竞争反应（本地玩家会怎么反击？）
❌ 不处理利益相关者（董事会、投资人、管理层谁支持谁反对？）
```

---

## ✅ 解决：CEO Skill 怎么做？

```
用户："我们该不该进入日本市场？"

CEO Skill：

【决策分类】Type 1 (One-Way Door) - 进入成本高，退出代价大

【偏差检查】
- 你是否因为竞对刚进入而产生 FOMO？
- 是否高估了"先发优势"？（日本市场更看重本地化深度）
- 是否低估了监管/文化壁垒？

【4 个选项 + Trade-off】
A. 全资子公司进入（投入 $5M，18 个月回本，风险：本地化失败）
B. 合资/收购本地玩家（投入 $8M，6 个月落地，风险：整合冲突）
C. 先做轻量试点（投入 $500K，验证 PMF，风险：错过窗口期）
D. 不进入（省 $5M+，专注现有市场，风险：竞对建立壁垒）

【竞争推演】
- 本地 Top 3 玩家会如何反应？（价格战/渠道封锁/监管游说）
- 你的竞对进入后 6 个月表现如何？（数据：用户增长 vs 烧钱速度）

【利益相关者】
- 董事会：2 人支持（看好国际化），1 人反对（担心分散资源）
- 投资人：关注 18 个月内 ARR 增长，不关注地域
- 管理层：销售 VP 支持，CFO 中立偏反对

【推荐】
Option C（试点）+ 6 个月决策点。
原因：日本市场 PMF 不确定性高，全押风险大。
Next Step：
1. 找 1-2 个本地 design partner（2 周）
2. 跑 MVP 验证付费意愿（3 个月）
3. 根据数据决定 A/B/D（第 6 个月）

✅ 结构化决策流程
✅ 至少 3 个可比选项 + do nothing
✅ 明确 trade-off
✅ 检查认知偏差
✅ 预判竞争与利益相关者反应
✅ 给 next steps + 决策点
```

---

## 📊 对比：CEO Skill vs 普通 AI

| 能力 | 普通 AI | 商业顾问 Prompt | **CEO Skill** |
|------|---------|----------------|--------------|
| 决策分类（one-way / two-way / crisis） | ❌ | ⚠️ 偶尔 | ✅ 强制 |
| 至少 3 个可比选项 + do nothing | ❌ | ⚠️ 不稳定 | ✅ 强制 |
| 明确 trade-off（不只给结论） | ❌ | ⚠️ | ✅ |
| 认知偏差检查（FOMO/沉没成本/锚定） | ❌ | ❌ | ✅ |
| 竞争响应预判（war gaming） | ❌ | ⚠️ | ✅ |
| 利益相关者映射（董事会/投资人/管理层） | ❌ | ⚠️ | ✅ |
| 贝叶斯决策分析（概率更新/敏感性分析） | ❌ | ❌ | ✅ |
| 数据分析辅助（Monte Carlo/ICE/NPV） | ❌ | ❌ | ✅ |

---

## 🚀 核心能力

### 1️⃣ 结构化决策流程

不是"给建议"，而是"拆决策"：

- **决策分类**：One-Way Door / Two-Way Door / Crisis / Strategic Bet
- **框架选择**：根据场景自动选择最佳框架（Decision Matrix / ICE / Porter's Five Forces / OODA Loop 等）
- **选项生成**：强制至少 3 个可比选项 + do nothing
- **Trade-off 分析**：明确每个选项的代价、风险、资源需求

### 2️⃣ 认知偏差检查（Debiasing）

CEO 决策最大的敌人不是信息不足，而是认知偏差：

- **锚定效应**：你是不是被竞对/投资人/顾问的数字锚定了？
- **沉没成本**：你是不是因为"已经投了 $X"而不愿止损？
- **确认偏差**：你是不是只找支持自己观点的数据？
- **FOMO**：你是不是因为"别人都在做"而跟风？
- **可得性偏差**：你是不是因为最近一个案例而高估概率？

📖 参考：[`references/cognitive-debiasing.md`](./references/cognitive-debiasing.md)

### 3️⃣ 竞争推演（War Gaming）

不只看自己，还要预判对手：

- **如果我们降价，竞对会跟进还是打差异化？**
- **如果我们进入他们的市场，他们会反击还是防守？**
- **如果我们收购这家公司，竞对会怎么反应？**

📖 参考：[`references/war-gaming.md`](./references/war-gaming.md)

### 4️⃣ 利益相关者管理（Stakeholder Playbook）

高层决策不只是"对不对"，还要考虑"谁支持谁反对"：

- **董事会**：谁是盟友？谁是反对者？谁是摇摆票？
- **投资人**：他们关注什么指标？容忍度多高？
- **管理层**：谁会因为这个决策受益/受损？
- **关键员工**：谁可能因此离职？

📖 参考：[`references/stakeholder-playbook.md`](./references/stakeholder-playbook.md)

### 5️⃣ 贝叶斯决策分析（Bayesian Decision Analysis）

在不确定性下系统化更新信念：

- **先验概率设定**：基于行业基准/历史数据建立初始信念
- **证据质量分级**：A/B/C/D/E 五级证据评估体系
- **似然比更新**：根据新证据系统化调整概率
- **敏感性分析**：测试假设变化对结论的影响
- **期望值决策**：结合概率与收益做最优选择

**适用场景**：
- 产品成功率预测（市场进入/新功能上线）
- 投资决策（收购/融资/资源分配）
- 风险评估（技术可行性/竞争威胁）
- 持续更新信念（随新数据动态调整策略）

📖 参考：[`references/bayesian-decision-analysis.md`](./references/bayesian-decision-analysis.md) | [`scripts/bayesian_calculator.py`](./scripts/bayesian_calculator.py)

### 6️⃣ 数据分析工具

不只是定性分析，还有定量支持：

- **Monte Carlo 模拟**：不确定性下的概率分布
- **ICE 评分**：Impact / Confidence / Ease 快速排优先级
- **NPV / IRR**：投资回报分析
- **Expected Value**：期望值计算
- **Scenario Planning**：最好/基准/最坏情况

📖 参考：[`scripts/analysis_tools.py`](./scripts/analysis_tools.py)

---

## 🎬 真实案例

### 🔥 Andy 的真实决策（NEW）
- **[是否 All-in AI Agent 生态？](./examples/real-andy-case-ai-agent-pivot.md)**
  - 背景：2024年1月，手上有10+个SaaS项目，OpenClaw刚开源
  - 决策：Barbell Strategy（90% AI Agent + 10% 保险）
  - 结果：18个月后，awesome系列116 stars，建立了中文AI Skill生态位
  - **完整展示：决策分类 → 偏差检查 → 选项对比 → 竞争推演 → 贝叶斯分析 → 复盘**

- **[为什么 CEOskill 只有 15 stars？](./examples/meta-why-only-15-stars.md)**
  - 问题：产品价值最高，但star最少
  - 根因：目标用户不在GitHub + 缺少个人品牌 + 缺少社交证明
  - 行动：内容营销 + 真实案例 + 商业化路径
  - **Meta案例：用CEOskill分析CEOskill本身**

### 战略决策
- 进入新市场？收购还是自建？业务止损还是继续投？
- 📄 示例：[M&A 收购决策](./examples/mna-acquisition-decision.md)（待补充）

### 资源分配
- 多个项目争资源，先做哪个？预算怎么分配？
- 📄 示例：[5 个项目优先级排序](./examples/prioritization-five-initiatives.md)（待补充）

### 危机响应
- 核心高管离职、线上事故、PR 危机怎么处理？
- 📄 示例：[CTO 离职危机](./examples/cto-departure-crisis.md)（待补充）

### 组织与政治
- 董事会、投资人、管理层怎么对齐？组织调整怎么管？
- 📄 示例：待补充

### 竞争推演
- 如果我们做 X，竞对会怎么反应？
- 📄 示例：待补充

📂 更多示例：[`examples/`](./examples/)

---

## ⚡ 快速开始

### 直接问

把它当成你的 CEO 幕僚：

```
"我们该不该进入日本市场？"
"5 个项目只能做 2 个，怎么排优先级？"
"CTO 要去竞对，我现在 2 小时内先做什么？"
"如果我们降价 20%，竞对会怎么反应？"
```

### 期待的输出

不是泛泛建议，而是：

1. **决策分类** - 这是什么类型的决策？为什么重要？
2. **偏差检查** - 你的思考有哪些盲点？
3. **选项对比** - 至少 3 个选项 + do nothing，每个的 trade-off 是什么？
4. **竞争/利益相关者分析** - 别人会怎么反应？
5. **推荐 + Next Steps** - 建议做什么？下一步是什么？

---

## 📦 安装

### OpenClaw / Claude Code / Cursor

```bash
# OpenClaw
openclaw skill install https://github.com/AIPMAndy/ceo-skill

# Claude Code / Cursor
# 将 SKILL.md 添加到项目上下文
```

### 其他 Agent Runtime

📖 参考：[RUNTIME.md](./RUNTIME.md)

**核心原则**：
- 文本能力就能跑基本版
- 有 web search 会更强
- 有 Python / code execution 时，定量分析价值明显上升

---

## 🔥 为什么它能火？

### 1. 痛点真实且高频

CEO / 创始人 / 高管每天都在做高风险决策，但：
- 顾问太贵（$500-2000/小时）
- 内部团队有利益冲突
- 普通 AI 太泛泛

### 2. 效果可量化

不是"感觉更好"，而是：
- 决策质量提升（有结构 vs 无结构）
- 时间节省（2 小时 → 30 分钟）
- 盲点减少（偏差检查 + 竞争推演）

### 3. 传播性强

- **一句话定位**："让 AI 像顶级 CEO 幕僚一样拆解决策"
- **对比表格**：CEO Skill vs 普通 AI 一目了然
- **真实案例**：M&A / 危机 / 优先级排序
- **开源免费**：MIT License，任何人可用

### 4. 社区驱动

- 欢迎补充真实案例
- 欢迎贡献新的决策框架
- 欢迎适配更多 Agent Runtime

---

## 📁 核心文件

```text
.
├── SKILL.md                            # 主 skill 定义（核心）
├── references/
│   ├── frameworks.md                   # 决策框架库
│   ├── bayesian-decision-analysis.md   # 贝叶斯决策分析
│   ├── cognitive-debiasing.md          # 认知偏差检查
│   ├── stakeholder-playbook.md         # 利益相关者管理
│   └── war-gaming.md                   # 竞争推演
├── scripts/
│   ├── analysis_tools.py               # 数据分析工具
│   └── bayesian_calculator.py          # 贝叶斯计算器
├── examples/                           # 真实案例
│   ├── mna-acquisition-decision.md
│   ├── cto-departure-crisis.md
│   └── prioritization-five-initiatives.md
└── evals/evals.json                    # 评测用例
```

---

## 🗺️ Roadmap

- [x] 主 skill 定义
- [x] 决策框架参考库
- [x] 认知偏差检查
- [x] 利益相关者管理
- [x] 竞争推演
- [x] 数据分析工具
- [x] **贝叶斯决策分析框架**
- [ ] 增加 10+ 真实案例（M&A / 裁员 / 融资 / 组织重组）
- [ ] 增加 benchmark / eval 结果展示
- [ ] 增加视频演示
- [ ] 增加更多 Agent Runtime 适配

---

## 🤝 贡献

欢迎补充：

- 真实决策案例（匿名化）
- 新的决策框架
- 更强的 eval case
- 不同 Agent Runtime 的适配

📖 请先阅读：[CONTRIBUTING.md](./CONTRIBUTING.md)

---

## 📄 License

MIT License.

---

## 💖 如果这个项目对你有帮助

1. 给仓库一个 **⭐ Star**
2. 提一个真实决策案例或 PR
3. 分享给需要的人

**让 AI 决策辅助从"个人项目"变成"可复用的决策工具"。**

---

<div align="center">

Made with 🧠 by [Andy](https://github.com/AIPMAndy)

[⭐ Star on GitHub](https://github.com/AIPMAndy/ceo-skill) | [📖 Documentation](./SKILL.md) | [💬 Discussions](https://github.com/AIPMAndy/ceo-skill/discussions)

</div>
