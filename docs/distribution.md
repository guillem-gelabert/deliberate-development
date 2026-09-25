# Distribution

`skills/{ground,shape,execute,state,help}/` is the only maintained behavioral source. Each skill owns its `SKILL.md`, references, scripts and assets. The per-skill `agents/openai.yaml` files provide optional OpenAI presentation metadata; runtime instructions do not depend on them.

```text
canonical skills/
  ├── root plugin.json + .agents/plugins/marketplace.json → Codex
  ├── .claude-plugin/plugin.json + marketplace.json      → Claude Code
  └── tools/check.py --package                           → standalone ZIPs
```

Codex uses the portable Agent Plugins root manifest and discovers the five root `skills/` children. Its local marketplace entry points to this repository root. No `.codex-plugin/` fallback is needed. Claude Code uses its own thin manifest and marketplace catalog, also pointing at this root; its default plugin layout scans the same `skills/`. The Claude marketplace source is relative to the repository, so a checkout at another path works without editing it. Installed clients may cache a copy of the plugin, but that copy is an installation artifact, not a separately maintained method.

The standalone ZIPs are built on demand into the gitignored `dist/`; each contains one skill folder generated from `skills/`. Shared runtime contract and validator copies inside those folders are deliberate so each ZIP works alone; `tools/check.py` requires them to stay byte-identical.

The task state is portable across clients: Codex can create `.work/PHS-1234/` through `dd:ground`; Claude Code can resume it with `dd:state`; Codex can continue its current slice with `dd:execute`. Both read and update the same `STATUS.md`, `SPEC.md`, `CURRENT_STATE.md`, `ARCHITECTURE.md`, and `PLAN.md` contract, or the project's configured equivalent. Neither integration creates platform-specific task state.
