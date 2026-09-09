# adhd-mode

**First-party ADHD / focus response-design skill** for coding agents and assistants.

Lower cognitive load — not minimum word count. Answer, action, artifact, or project state first. One active item. Resume after interruption. Explicit ND-safe directives (persona alone is not enough).

Not medical advice. No diagnosis required.

## Install

### Skills CLI (Claude Code, Cursor, Codex, and peers)

```bash
npx skills add fuzzywigg/adhd-mode --skill adhd-mode
```

### Manual

Copy `skills/adhd-mode/` into your agent’s skills directory (for example `.claude/skills/adhd-mode` or `.agents/skills/adhd-mode`).

### OpenClaw / Geryon

Already mirrored under `~/.openclaw/workspace/skills/adhd-mode/` on the live workspace when installed from this package.

## Usage

Say **ADHD mode** or **focus mode**, or invoke the skill via `/` / `@`.

| Control | Effect |
| --- | --- |
| `one thing` | Current action + stop condition only |
| `map it` | Compact route + definition of done |
| `resume` | `You are here:` breadcrumb + continue |
| `park that` | Capture tangent; keep goal |
| `clean` / `flow` / `zen` mode | Long-form sectioning density |
| `stop ADHD mode` / `normal mode` | Disable until re-enabled |

## What’s inside

- **4 contracts:** Answer · Action · Artifact · Project update
- **6 modifiers:** Friction · Reorientation · Memory offload · Decision · Recovery · Finish
- **Working set:** Active 1 · Ready ≤2 · Parked
- **NDBench-style rails:** structure, micro-steps, anti-masking, acknowledge-then-act
- **Hyperfocus-style modes:** Clean / Flow / Zen for long replies
- **Thin eval:** 12 smoke intents in `SKILL.md`

## Attribution

See [NOTICE.md](NOTICE.md). Synthesis cites 47 Tabs, hyperfocus, NDBench, and W3C COGA — **not a fork**.

## License

[MIT](LICENSE)
