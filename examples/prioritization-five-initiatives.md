# Example — Prioritizing five initiatives

## Input

> I have five projects: core system refactor, international expansion, AI features, customer success optimization, and a mobile app. We can only do two at a time. Help me prioritize.

## What a strong answer should do

This should trigger **Prioritization Mode** and use **ICE scoring** as the first pass.

## Suggested output components

1. score all 5 initiatives on:
   - impact
   - confidence
   - ease
2. show the ICE ranking clearly
3. identify dependencies:
   - does refactor unlock AI or mobile velocity?
   - does customer success improve retention before expansion?
4. recommend:
   - top 2 to start now
   - sequence for the remaining 3
5. explain opportunity cost of delay

## Example table

| Initiative | Impact | Confidence | Ease | ICE |
|---|---:|---:|---:|---:|
| AI features | 9 | 7 | 6 | 378 |
| Customer success | 8 | 8 | 7 | 448 |
| Core refactor | 7 | 6 | 4 | 168 |
| International expansion | 8 | 5 | 3 | 120 |
| Mobile app | 5 | 6 | 5 | 150 |

## Interpretation guidance

A strong answer should not stop at the scores.
It should explain whether the lower-scoring refactor is still strategically necessary because it unlocks future velocity.
