# Security policy

`adhd-mode` is an instruction-only Agent Skill. The published tree is Markdown, YAML host metadata, and license/notice files. It contains **no** executable code, install scripts inside the skill folder, credentials, telemetry, or network calls.

## Supported versions

Security-relevant fixes target the latest published version on `main` (see [`VERSION`](VERSION)).

## Reporting

Report packaging tampering, unexpected binaries, credential exposure, or unsafe instruction changes privately via [GitHub security advisories](https://github.com/fuzzywigg/adhd-mode/security/advisories/new) when available. Otherwise open a private channel with the maintainers.

Do **not** post secrets, personal data, or exploit payloads in public issues.

## Consumer checklist

Before enabling any downloaded skill:

1. Review `skills/adhd-mode/SKILL.md` and `agents/openai.yaml`.
2. Confirm the skill folder has no scripts or unexpected binaries.
3. Prefer install from this repository via `npx skills add fuzzywigg/adhd-mode --skill adhd-mode`.
