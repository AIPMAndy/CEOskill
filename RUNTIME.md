# Runtime notes

`ceo-skill` is designed to be portable across agent runtimes.

## What it assumes

The skill is strongest when the runtime can provide one or more of the following:

1. web search / browsing
   - for market context, competitors, benchmarks, and recent events
2. file reading
   - to load references and examples
3. optional code execution
   - to run quantitative analysis with `scripts/analysis_tools.py`

## Minimum viable runtime

At minimum, the skill still works as a structured decision workflow if the runtime only supports text generation and file reading.

## Better runtime experience

The experience improves significantly when the runtime can also:

- search the web for current facts
- run Python for EV / NPV / IRR / Monte Carlo
- access organization-specific context files or memos

## Portability principle

This repository avoids over-coupling to a single platform.
Most of the value is in:
- the decision flow in `SKILL.md`
- the reference documents in `references/`
- the examples in `examples/`
- the analysis helpers in `scripts/analysis_tools.py`

## Recommended adoption path

1. start by reading `SKILL.md`
2. test with 3-5 real decision prompts
3. add your own org-specific examples
4. optionally wire the script helpers into your runtime tooling
