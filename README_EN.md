<div align="center">

# 🧠 CEO Skill

**Help AI think like a strong CEO chief of staff: structure decisions, detect bias, predict competition, and manage stakeholders.**

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](./LICENSE)
[![Skill](https://img.shields.io/badge/Type-Agent%20Skill-blue)](./SKILL.md)
[![Language](https://img.shields.io/badge/Python-helpers-3776AB?logo=python&logoColor=white)](./scripts/analysis_tools.py)
[![Evals](https://img.shields.io/badge/Evals-Examples-orange)](./evals/evals.json)

[简体中文](./README.md) | **English**

</div>

---

## What is this?

`ceo-skill` is a **CEO decision-support skill for AI agents**.

It is not just a “sound-smart business prompt,” and it is not a generic strategy consultant template. Its goal is much more specific:

> Turn messy, high-stakes executive decisions into structured decision workflows.

It focuses on:

- strategic trade-offs
- prioritization and resource allocation
- crisis response
- board / investor / org communication
- competitive war gaming
- cognitive debiasing
- financial and scenario analysis

---

## What problem does it solve?

Many “CEO advisor” prompts have the same weaknesses:

- they sound polished but stay vague
- they list frameworks but do not choose the right one
- they give advice without surfacing trade-offs
- they ignore cognitive bias
- they ignore competitor response
- they ignore stakeholder dynamics

The core value of `ceo-skill` is this:

**It turns executive advice from loose conversation into a structured decision process.**

---

## Why this is different from a generic strategy prompt

| Capability | Generic strategy prompt | Consultant-style answer | **CEO Skill** |
|---|---|---|---|
| Decision classification (one-way / two-way / crisis) | ❌ | ⚠️ Sometimes | ✅ |
| At least 3 options + do-nothing baseline | ❌ | ⚠️ Inconsistent | ✅ |
| Stakeholder mapping | ❌ | ⚠️ | ✅ |
| Cognitive debiasing | ❌ | ❌ | ✅ |
| Competitive response prediction | ❌ | ⚠️ | ✅ |
| Quantitative helper scripts | ❌ | ❌ | ✅ |
| Crisis / prioritization / war game modes | ❌ | ❌ | ✅ |

In one sentence:

**This is not a CEO prompt that talks better. It is a CEO skill that decomposes decisions better.**

---

## Repository structure

```text
.
├── SKILL.md                            # Main skill definition
├── references/
│   ├── frameworks.md                   # Decision framework library
│   ├── cognitive-debiasing.md          # Bias detection and debiasing
│   ├── stakeholder-playbook.md         # Stakeholder management
│   └── war-gaming.md                   # Competitive simulation
├── scripts/analysis_tools.py           # Monte Carlo / ICE / EV / NPV / IRR helpers
└── evals/evals.json                    # Example evaluation cases
```

---

## Use cases

This skill is especially useful for questions like:

### 1) Strategic decisions
- Should we enter a new market?
- Should we acquire this company?
- Should we continue investing or cut losses?

### 2) Resource allocation
- We have 5 initiatives but can only fund 2. Which ones first?
- Should budget go to growth, product, or org?

### 3) Crisis response
- What should we do if a key executive suddenly resigns?
- How should we handle an outage or PR crisis?

### 4) Stakeholder and political dynamics
- How do we align board, investors, and leadership?
- How do we manage stakeholders during a reorg?

### 5) Competitive war gaming
- If we cut price / launch a feature / enter a market, how will competitors respond?

---

## Quick start

### 1) Ask it like you would ask a strong chief of staff

Examples:

- Should we enter Japan this year?
- We can only fund 2 of 5 initiatives. How should we prioritize?
- Our CTO may leave for a competitor. What do we do in the next 2 hours?
- Should we acquire this smaller competitor now or wait?

### 2) What you should expect back

Not generic business advice, but:

- decision classification first
- explicit constraints, stakeholders, and deadline
- at least 3 options plus a do-nothing baseline
- framework-based reasoning, not just opinions
- recommendation, risks, and next steps

### 3) The fastest way to understand it: examples

- [examples/mna-acquisition-decision.md](./examples/mna-acquisition-decision.md)
- [examples/cto-departure-crisis.md](./examples/cto-departure-crisis.md)
- [examples/prioritization-five-initiatives.md](./examples/prioritization-five-initiatives.md)

## How it works

Instead of jumping straight to a conclusion, it typically goes through this flow:

1. classify the decision type
2. clarify the real question, constraints, stakeholders, deadline, and do-nothing cost
3. generate at least 3 options plus a do-nothing baseline
4. choose the right decision framework
5. run debiasing checks
6. produce a recommendation, risks, and next steps

The focus is not just “having an opinion,” but **improving decision quality**.

---

## Built-in analysis helpers

The repository includes `scripts/analysis_tools.py` with lightweight but practical tools for:

- Monte Carlo simulation
- Decision matrix
- ICE scoring
- Expected value
- NPV
- IRR

Their value is not to become a full finance stack, but to make the skill **less purely verbal** when high-stakes decisions need numbers.

### You can now run them from the CLI

```bash
# ICE scoring
python scripts/analysis_tools.py ice --json '[
  {"name":"AI features","impact":9,"confidence":7,"ease":6},
  {"name":"Customer success","impact":8,"confidence":8,"ease":7}
]'

# Decision matrix
python scripts/analysis_tools.py decision-matrix --file examples/decision-matrix.json

# NPV
python scripts/analysis_tools.py npv --rate 0.12 --json '[-3000000, 1200000, 1500000, 1800000]'
```

That makes this repo feel more like an **executable decision toolkit**, not only a prompt artifact.

---

## Best places to start

If this is your first time here, begin with:

1. [SKILL.md](./SKILL.md) — main workflow and decision modes
2. [references/frameworks.md](./references/frameworks.md) — framework library
3. [references/cognitive-debiasing.md](./references/cognitive-debiasing.md) — bias checks
4. [references/stakeholder-playbook.md](./references/stakeholder-playbook.md) — stakeholder dynamics
5. [scripts/analysis_tools.py](./scripts/analysis_tools.py) — quantitative helpers

---

## Roadmap

- [x] Main skill definition
- [x] Decision framework references
- [x] Debiasing references
- [x] Stakeholder playbook
- [x] War gaming references
- [x] Analysis helpers
- [ ] Add realistic case examples (M&A / layoffs / fundraising / reorg)
- [ ] Add full Chinese + English usage examples
- [ ] Add benchmark / eval result presentation
- [ ] Add clearer runtime compatibility notes

---

## What still limits growth

The biggest limitations are not content quality, but packaging:

1. **front-page clarity** — weak README means weak conversion
2. **positioning** — no memorable one-line pitch
3. **proof** — not enough concrete examples yet
4. **English coverage** — without it, the audience stays narrow

That is why repository packaging matters so much here.

---

## Contributing

Contributions are welcome, especially:

- new decision modes
- stronger eval cases
- realistic business case templates
- more analysis helpers
- runtime compatibility guidance

Please read [CONTRIBUTING.md](./CONTRIBUTING.md) first.

---

## License

MIT License.

---

## If this repo helps you

Please do two simple things:

1. give it a **⭐ Star**
2. contribute a real decision case or PR

That is the fastest way to turn this from a personal artifact into a reusable decision tool.
