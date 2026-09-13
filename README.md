# adhd-mode

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Version](https://img.shields.io/badge/version-1.0.0-blue.svg)](VERSION)
[![Skill](https://img.shields.io/badge/skill-adhd--mode-0ea5e9.svg)](skills/adhd-mode/SKILL.md)
[![CI](https://github.com/fuzzywigg/adhd-mode/actions/workflows/ci.yml/badge.svg)](https://github.com/fuzzywigg/adhd-mode/actions/workflows/ci.yml)

**First-party ADHD / focus response-design skill** for coding agents and assistants.

Lower cognitive load — not minimum word count. Answer, action, artifact, or project state first. One active item. Resume after interruption. Explicit ND-safe directives (persona alone is not enough).

> **Disclaimer:** Not medical advice, diagnosis, or therapy. No diagnosis required. See [NOTICE.md](NOTICE.md).

## Install

### Skills CLI (recommended)

Works with Claude Code, Cursor, Codex, GitHub Copilot (Agent Skills hosts), and peers:

```bash
npx skills add fuzzywigg/adhd-mode --skill adhd-mode
```

| Host | Typical skill location after install |
| --- | --- |
| Claude Code | `.claude/skills/adhd-mode` |
| Cursor | `.cursor/skills/adhd-mode` or project skills dir |
| Codex / ChatGPT | `.agents/skills/adhd-mode` (or host default) |
| GitHub Copilot | Agent Skills path used by your VS Code / Copilot setup |

Use `--agent <name>` when the CLI asks you to target a specific host.

### Manual

Copy `skills/adhd-mode/` (including `agents/openai.yaml`) into your agent’s skills directory.

### OpenClaw / Geryon

Already mirrored under `~/.openclaw/workspace/skills/adhd-mode/` on the live workspace when installed from this package. Grok Bot skill id: `adhd-mode`.

## Usage

Say **ADHD mode** or **focus mode**, or invoke the skill via `/` / `@` / `$` on hosts that support explicit skill mention.

| Control | Effect |
| --- | --- |
| `one thing` | Current action + stop condition only |
| `map it` | Compact route + definition of done |
| `resume` | `You are here:` breadcrumb + continue |
| `park that` | Capture tangent; keep goal |
| `why this` | Deciding reason only |
| `clean` / `flow` / `zen` mode | Long-form sectioning density |
| `stop ADHD mode` / `normal mode` | Disable until re-enabled |

## What’s inside

- **4 contracts:** Answer · Action · Artifact · Project update
- **6 modifiers:** Friction · Reorientation · Memory offload · Decision · Recovery · Finish
- **Working set:** Active 1 · Ready ≤2 · Parked
- **NDBench-style rails:** structure, micro-steps, anti-masking, acknowledge-then-act
- **Hyperfocus-style modes:** Clean / Flow / Zen for long replies
- **Host metadata:** `skills/adhd-mode/agents/openai.yaml` (Codex / ChatGPT UI + implicit invocation)
- **Thin eval:** 12 smoke intents — see [`docs/EVALS.md`](docs/EVALS.md) (no published pass rates)

## Attribution

See [NOTICE.md](NOTICE.md). Synthesis cites 47 Tabs, hyperfocus, NDBench, and W3C COGA — **not a fork**.

## Cloud agents

Docs-only bootstrap lives in [`.cursor/environment.json`](.cursor/environment.json)
(`install` verifies the skill package + CI workflow; no `start` services, no secrets).
PR CI runs Markdown lint + packaging hygiene via [`.github/workflows/ci.yml`](.github/workflows/ci.yml).

## Contributing / security

- [CONTRIBUTING.md](CONTRIBUTING.md)
- [SECURITY.md](SECURITY.md)

## License

[MIT](LICENSE)
