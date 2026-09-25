# Deliberate Development

Five agent skills for non-trivial software work. Three are stages: understand what is wanted and what exists, shape it into a bounded design with behavioral slices, then execute one slice at a time inside explicit work blocks. The fourth, `dd:state`, tells you where a task stands, what comes next, and brings already-started work into the workflow. The fifth, `dd:help`, explains the commands. The workflow's state lives in plain Markdown files, so any agent can stop and another can resume. That includes switching between GPT-5.6 Sol and Claude Opus 5.5, or opening a new conversation.

The method is distilled from a small public research corpus (Fowler, Wake, Singer/Shape Up, Spolsky, Newport, Beck). Research claims and the main runtime rules are labeled by how directly their sources support them, with project decisions marked DERIVED.

## The skills

| Skill | Produces | Stops when |
|---|---|---|
| `dd:ground` | `SPEC.md` (what should become true) and `CURRENT_STATE.md` (what is true now) | requirements are designable, the relevant context is verified, and material ambiguities are resolved or blocking |
| `dd:shape` | `ARCHITECTURE.md` (intended design, risks, spikes) and `PLAN.md` (behavioral slices), iterating architecture → architecture risk check → slice → slice readiness check | the design is sufficient, unknowns are resolved or spiked, and at least one slice is `ready` |
| `dd:execute` | code, tests, `PLAN.md` slice state with estimate/block/actual records, and calibration-log entries | the slice is `done`, or the block's stop condition is reached and checkpointed |
| `dd:state` | a verified state summary, one concrete next action, a reconciled `STATUS.md`; on adoption, backfilled task files | the question is answered, the adoption or checkpoint is recorded, or (on resume) the routed stage stops |
| `dd:help` | a short cheat sheet and the command that fits your situation; lists existing task workspaces, writes nothing | the question is answered |

Normal flow for a new task: `dd:ground → dd:shape → dd:execute`, then `dd:execute` again for the next slice. Each stage skill can also be invoked directly ("use dd:shape on PROJ-12", "dd:execute: continue"). If the workspace already exists, it reconstructs the current state first and continues only the part of its stage that is not done.

`dd:state` is the entry and re-entry point: "where did I leave off?", "what's next on PHS-1234?", "resume PHS-1234", "adopt this task", "checkpoint here, I'm stopping". It checks the recorded state against the files and the repository, corrects it if it is stale, and routes to the stage whose work comes next. You do not need to know which stage skill to call. Invoked bare on a repository with no workspace, it infers the task in progress and asks before creating `.work/`.

Not sure which command to use? Run `/dd:help`. It answers "which dd command should I use?"; "what should I do next on this task?" belongs to `dd:state`.

## Install and use

Codex and Claude Code use the same canonical skill definitions from `skills/`. No platform-specific task files or workflow copies are required. See [distribution details](docs/distribution.md).

### Codex

From a checkout, add this repository's local marketplace and install the bundle:

```bash
codex plugin marketplace add /absolute/path/to/deliberate-development
codex plugin add dd@deliberate-development-local
```

Start a new Codex session after installation. The portable root `plugin.json` exposes all five skills from `skills/`; the `.agents/plugins/marketplace.json` entry makes the bundle installable locally. Codex can also add a hosted Git repository as a marketplace source when this repository is published there.

### Claude Code

For a session using the checkout directly:

```bash
claude --plugin-dir /absolute/path/to/deliberate-development
```

For an installed plugin, run `claude plugin marketplace add /absolute/path/to/deliberate-development` and then `claude plugin install dd@guillem-local`. If it was installed earlier but disabled, run `claude plugin enable dd@guillem-local`. Its skills are available as `/dd:ground`, `/dd:shape`, `/dd:execute`, `/dd:state`, and `/dd:help`.

Upgrading from 0.4.x: the skills were previously `ground-work`, `shape-work`, `execute-work` and `work-state`. Existing `STATUS.md` files with `stage: ground-work`, `shape-work` or `execute-work` still validate, with a warning to rename the stage to `ground`, `shape` or `execute`.

### Individual skills

Run `python3 tools/check.py --package` to build five standalone skill packages as `dist/dd-<skill>.zip` (gitignored, not committed). Install the desired ZIP through the individual-skill installer supported by your OpenAI/ChatGPT surface, or unpack its one skill folder into a local skills directory. The ZIPs are generated from the same `skills/` source.

## Task workspace

```text
.work/<task-id>/
├── STATUS.md          cursor: stage, step, artifact states, blockers, one next action
├── SPEC.md
├── CURRENT_STATE.md
├── ARCHITECTURE.md
└── PLAN.md            single source of truth for slices
```

If the project's `AGENTS.md`/`CLAUDE.md` (or equivalent) defines where task or design docs live, the skills use that location instead. The skills do not need those files and never edit them. The full contract is in [`docs/task-state-contract.md`](docs/task-state-contract.md).

Resuming: the substantive files plus the repository are the task's real state, and `STATUS.md` is a cached cursor over them. A new session reads `STATUS.md`, checks it against the artifacts and the code/tests, reconciles it if it is stale (for example, when the recorded next step is to write a test that already exists), and continues from there. It does not restart the stage.

## Bringing an existing task into the framework

If you have already started a task without these skills, invoke `dd:state` with something like:

```text
Bring the task on my current branch into Deliberate Development.
```

```text
Adopt PHS-1234. I've already started implementing it.
```

The agent inspects the existing evidence: the ticket, the branch, the diff against the base, commits, and the new and changed tests (which it runs). It backfills the five task files conservatively. What it observed is labeled Verified. What it reconstructs, such as the design direction the code shows, is labeled Inferred, and anything unknown is Open. It does not invent earlier decisions, estimates or finished slices. It then identifies the current slice and stage and records one next action. It does not replay stages that are already done. It routes backward only when adoption exposes a gap that matters, such as an unresolved requirement the current slice depends on.

Calibration history lives outside task workspaces in `~/.deliberate-development/calibration.jsonl` (override with `$DELIBERATE_DEV_CALIBRATION`). It is an append-only JSON Lines log, with one record per completed slice (estimate, actual, velocity, estimator), written and summarized by `execute/scripts/calibration.py`. Schema and append rules: [`docs/task-state-contract.md`](docs/task-state-contract.md#calibration-log).

## Repository layout

```text
skills/     the five installable skills (edit these)
docs/       architecture, task-state contract, prompting principles, methodology decisions
research/   sources/ (normalized articles), extractions/ (per-source, ID-tagged), synthesis/ (per-stage, provenance index, gaps)
evals/      Markdown scenarios and the expected-behavior catalog
tools/      check.py (validate + package), test_scripts.py (smoke tests)
archive/    original-skill-zips/ (the first downloaded packages, kept for reference)
dist/       built ZIPs, one skill each (gitignored; built by check.py --package)
plugin.json portable plugin identity for Codex
.agents/plugins/ Codex local marketplace entry
.claude-plugin/ Claude Code manifest and local marketplace entry
```

## Research and runtime

`research/` is the evidence base, and it never ships. Runtime skills carry only compact references distilled from `research/synthesis/`, with each rule tagged:

- **DIRECT**: explicitly stated by the source.
- **INFERRED**: a conservative restatement or implication.
- **DERIVED**: created for this skillset. Never attributed to an author.

The runtime rule map at the top of `research/synthesis/provenance-index.md` links the five skills' main operational rules to source IDs or explicit DERIVED decisions. Stable IDs (for example `IMPLEMENT-BECK-N05`) link synthesis rules to extractions in that index. Source conflicts, and how the skillset resolves them, are in [`docs/methodology-decisions.md`](docs/methodology-decisions.md). The weakest-grounded area is unfamiliar-codebase reconnaissance in `dd:ground`, which is mostly DERIVED. `dd:state` (re-entry, adoption, reconciliation, routing, checkpointing) is a DERIVED workflow extension: the corpus does not cover it.

To change a methodological rule: find it in `research/synthesis/`, check its extraction (and the source if needed), update the runtime reference, and record any new adaptation in `methodology-decisions.md`. Normalized sources in `research/sources/` are not edited.

## Validate and package

```bash
python3 tools/check.py             # structure, references, shared-file sync, vocabulary, dist freshness, official validator if found, smoke tests
python3 tools/check.py --package   # also writes dist/dd-{ground,shape,execute,state,help}.zip
```

`tools/check.py` uses the skill-creator `quick_validate.py` / `package_skill.py` when installed (set `SKILL_CREATOR_DIR` to point at it), and falls back to its own checks and zip. Each ZIP contains exactly one skill folder. Some files are deliberately duplicated so that each skill installs standalone: `references/task-state.md` and `scripts/validate_work.py` in the four workflow skills (not `dd:help`), and `scripts/init_work.py` with `assets/templates/` in `dd:ground` and `dd:state`. The check fails if the copies drift, or if any skill uses a stage, step, status or state value that the validator does not know. Edit the `skills/ground/` copy and copy it across.

The root portable plugin and Claude Code manifest both expose `skills/` directly. Platform metadata never supplies workflow instructions.

## Evals

`evals/` holds thirty-one Markdown scenarios, including adoption with `review-needed` architecture and generic resume versus explicit implementation routing, graded against `evals/expected-behaviors.md`. See [`evals/README.md`](evals/README.md).
