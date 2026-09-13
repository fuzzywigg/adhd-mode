# Contributing

Thanks for helping keep `adhd-mode` small, honest, and portable.

## Scope

This package is an **instruction-only** Agent Skill (`skills/adhd-mode/`). Prefer focused PRs that improve clarity, installability, or host metadata — not sprawling companion apps or medical framing.

## Before you change behavior

1. Read [`skills/adhd-mode/SKILL.md`](skills/adhd-mode/SKILL.md) and [`NOTICE.md`](NOTICE.md).
2. Name which **contract** or **modifier** owns the change.
3. Preserve safety, accuracy, warmth, and requested depth (lower cognitive load ≠ minimum word count).
4. Update the matching smoke intent in [`docs/EVALS.md`](docs/EVALS.md) / `SKILL.md` when behavior shifts.
5. Do **not** invent eval pass rates, medical claims, or secrets.

## Branch / PR

- Default branch is `main`. Prefer `cursor/<task>` (or equivalent) for agent PRs.
- Keep PRs thin: docs/CI/hygiene or one contract/modifier change at a time.
- CI on PRs to `main`: Markdown lint + packaging hygiene (required files,
  instruction-only skill tree, no committed secret material).

## Local checks

No build step. Sanity-check:

```bash
# Same checks Cloud Agents run via .cursor/environment.json
test -f skills/adhd-mode/SKILL.md
test -f skills/adhd-mode/agents/openai.yaml
test -f LICENSE && test -f NOTICE.md && test -f VERSION
test -f .github/workflows/ci.yml && test -f docs/EVALS.md
head -n 20 skills/adhd-mode/SKILL.md
npx --yes markdownlint-cli2 "**/*.md"
```

Install path consumers expect:

```bash
npx skills add fuzzywigg/adhd-mode --skill adhd-mode
```

## Attribution

Keep [`NOTICE.md`](NOTICE.md) accurate. This is a first-party synthesis, **not** a fork. Credit peer sources for adapted principles; do not copy their prose wholesale.
