<div align="center">

# 🧠 CEO Skill

**让 AI 像优秀 CEO 幕僚一样思考：结构化决策、识别偏差、预判竞争、管理利益相关者。**

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](./LICENSE)
[![Skill](https://img.shields.io/badge/Type-Agent%20Skill-blue)](./SKILL.md)
[![Language](https://img.shields.io/badge/Python-helpers-3776AB?logo=python&logoColor=white)](./scripts/analysis_tools.py)
[![Evals](https://img.shields.io/badge/Evals-Examples-orange)](./evals/evals.json)

**简体中文** | [English](./README_EN.md)

</div>

---

## 这是什么

`ceo-skill` 是一个给 AI agent 用的 **CEO 决策辅助 Skill**。

它不是“帮 CEO 输出几句鸡汤”的 prompt，也不是泛泛而谈的商业顾问模板。它的目标更具体：

> 把高风险、高不确定性的管理决策，拆成可以执行的分析流程。

它重点覆盖：

- 战略取舍
- 资源分配与优先级
- 危机响应
- 董事会 / 投资人 / 组织沟通
- 竞争预判（war gaming）
- 认知偏差检查（debiasing）
- 财务与情景分析

---

## 它解决什么问题

很多“CEO 顾问型 AI 提示词”都有同一个问题：

- 会说漂亮话，但不落地
- 会列框架，但不会选框架
- 会给建议，但不展示 trade-off
- 不检查认知偏差
- 不考虑竞争反应
- 不处理 stakeholder dynamics

`ceo-skill` 的核心价值是：

**把“高层决策建议”从模糊对话，变成结构化决策流程。**

---

## 为什么它和普通 strategy prompt 不一样

| 能力 | 普通战略 Prompt | 商业顾问式回答 | **CEO Skill** |
|---|---|---|---|
| 决策分类（one-way / two-way / crisis） | ❌ | ⚠️ 偶尔 | ✅ |
| 至少 3 个可比选项 + do nothing | ❌ | ⚠️ 不稳定 | ✅ |
| 利益相关者映射 | ❌ | ⚠️ | ✅ |
| 认知偏差检查 | ❌ | ❌ | ✅ |
| 竞争响应预判 | ❌ | ⚠️ | ✅ |
| 数据分析辅助脚本 | ❌ | ❌ | ✅ |
| crisis / prioritization / war game 模式 | ❌ | ❌ | ✅ |

一句话：

**这不是“更会说”的 CEO prompt，而是“更会拆决策”的 CEO skill。**

---

## 核心组成

```text
.
├── SKILL.md                            # 主 skill 定义
├── references/
│   ├── frameworks.md                   # 各类决策框架
│   ├── cognitive-debiasing.md          # 偏差识别与纠偏
│   ├── stakeholder-playbook.md         # 利益相关者管理
│   └── war-gaming.md                   # 竞争推演
├── scripts/analysis_tools.py           # Monte Carlo / ICE / EV / NPV / IRR 等工具
└── evals/evals.json                    # 示例评测用例
```

---

## 适用场景

这个 skill 特别适合下面这些问题：

### 1) 战略决策
- 我该不该进入新市场？
- 我们要不要收购这家公司？
- 这个业务该继续投还是止损？

### 2) 资源分配
- 多个项目只能做 2 个，先做哪个？
- 预算应该投增长、产品还是组织？

### 3) 危机响应
- 核心高管离职怎么办？
- 线上事故 / 公关危机怎么处理？

### 4) 组织与政治
- 董事会、投资人、管理层怎么对齐？
- 组织调整时怎么管 stakeholder？

### 5) 竞争推演
- 如果我们降价 / 上新功能 / 进入对方市场，竞对会怎么反应？

---

## 快速上手

### 1) 直接把它当成 CEO 幕僚来问

示例：

- 我们该不该进入日本市场？
- 这次组织重组先动销售还是先动产品？
- CTO 要离职去竞对，我现在 2 小时内先做什么？
- 5 个项目只能做 2 个，怎么排优先级？

### 2) 你应该期待的输出

不是泛泛建议，而是：

- 先判断决策类型
- 明确约束、stakeholder、deadline
- 给至少 3 个选项 + do nothing
- 跑框架，而不是只喊观点
- 输出 recommendation / risks / next steps

### 3) 看例子最快

如果你想 3 分钟理解它到底有什么用，直接看：

- [examples/mna-acquisition-decision.md](./examples/mna-acquisition-decision.md)
- [examples/cto-departure-crisis.md](./examples/cto-departure-crisis.md)
- [examples/prioritization-five-initiatives.md](./examples/prioritization-five-initiatives.md)

## 快速理解它的工作方式

它不是直接给结论，而是按这种结构推进：

1. 先判断这是什么类型的决策
2. 明确真实问题、约束、利益相关者、deadline、do nothing 后果
3. 至少生成 3 个选项 + do nothing
4. 选择最合适的决策框架
5. 跑一轮 debiasing
6. 输出 recommendation + risk + next steps

也就是说，它的重点不是“观点”，而是 **决策质量**。

---

## 自带分析能力

仓库里的 `scripts/analysis_tools.py` 提供了几个轻量但实用的分析工具：

- Monte Carlo simulation
- Decision matrix
- ICE scoring
- Expected value
- NPV
- IRR

这些脚本的价值不是“金融建模有多高级”，而是让 skill 在处理高层决策时，**不只停留在语言层面**。

### 现在可以直接命令行运行

例如：

```bash
# ICE 评分
python scripts/analysis_tools.py ice --json '[
  {"name":"AI 功能","impact":9,"confidence":7,"ease":6},
  {"name":"客户成功","impact":8,"confidence":8,"ease":7}
]'

# 决策矩阵
python scripts/analysis_tools.py decision-matrix --file examples/decision-matrix.json

# NPV
python scripts/analysis_tools.py npv --rate 0.12 --json '[-3000000, 1200000, 1500000, 1800000]'
```

这让它更像一个**可执行的 decision toolkit**，而不只是一个 prompt 包。

---

## 当前最有价值的地方

如果你第一次看这个项目，建议重点看：

1. [SKILL.md](./SKILL.md) — 主流程和决策模式
2. [references/frameworks.md](./references/frameworks.md) — 决策框架库
3. [references/cognitive-debiasing.md](./references/cognitive-debiasing.md) — 偏差检查
4. [references/stakeholder-playbook.md](./references/stakeholder-playbook.md) — 组织政治与沟通
5. [scripts/analysis_tools.py](./scripts/analysis_tools.py) — 定量分析辅助

---

## Roadmap

- [x] 主 skill 定义
- [x] 决策框架参考库
- [x] debiasing 参考库
- [x] stakeholder playbook
- [x] war gaming 参考库
- [x] 分析脚本
- [ ] 增加真实案例示例（M&A / 裁员 / 融资 / 组织重组）
- [ ] 增加中英文完整使用示例
- [ ] 增加 benchmark / eval 结果展示
- [ ] 增加更强的 runtime 兼容说明

---

## 当前阻碍它火的地方

如果认真看，这个项目现在最缺的不是内容，而是：

1. **门面**：原 README 太弱，无法 5 秒打动人
2. **传播语言**：没有一句让人记住的定位
3. **案例证据**：缺真实场景演示
4. **英文覆盖**：没有英文 README 就很难出圈

所以我现在优先把这些基础设施补起来。

---

## 贡献方式

欢迎补充：

- 新的决策模式
- 更强的 eval case
- 真实业务案例模板
- 更多分析脚本
- 不同 agent runtime 的适配方式

请先阅读：[CONTRIBUTING.md](./CONTRIBUTING.md)

---

## License

MIT License.

---

## 如果这个项目对你有帮助

请直接：

1. 给仓库一个 **⭐ Star**
2. 提一个真实决策案例或 PR

这会让这个 skill 更快从“个人项目”变成“可复用的决策工具”。
