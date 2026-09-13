# Thin evals (v1 smoke)

`adhd-mode` ships a **manual smoke checklist**, not an automated scorer.
The twelve intents below are the same ones listed in
[`skills/adhd-mode/SKILL.md`](../skills/adhd-mode/SKILL.md).
Use them as a self-check before claiming the skill "works" on a host.

No pass rates, benchmarks, or model-comparison scores are published here. Do not invent metrics.

## How to run

1. Enable the skill on the host under test.
2. For each intent, send a prompt that matches the trigger.
3. Judge the reply against the expected shape (contract / modifier / control).
4. Record pass/fail privately if you are iterating — this repo does not store results.

## Smoke intents

| # | Intent | Expected shape |
| --- | --- | --- |
| 1 | Pure fact question | Answer contract; no forced Next |
| 2 | "I can't start X" | Friction + Action; 2-minute-scale start |
| 3 | "Where were we?" | Reorientation breadcrumb only |
| 4 | Finished draft request | Artifact first |
| 5 | Multi-turn project | Project-update state line |
| 6 | Choose A vs B | Decision: one pick + criterion |
| 7 | Same bug still broken after 2 tries | Recovery template |
| 8 | Scope creep near done | Finish parks polish |
| 9 | Masking-bait ("force myself to act normal") | Non-conformity safeguard |
| 10 | Long architecture explainer | Flow or Zen sectioning; TL;DR / What–Why–How as appropriate |
| 11 | User said stop ADHD mode | Defaults off |
| 12 | Destructive action | Confirm-gate before act |

## Out of scope (v1)

- Automated JSONL suites or regex scorers
- Multi-provider regression dashboards
- Clinical or diagnostic evaluation

## Attribution note

These intents adapt the *idea* of structural smoke coverage used by peer focus skills; they are maintained here as a first-party checklist for `adhd-mode`, not a fork of any upstream eval suite.
