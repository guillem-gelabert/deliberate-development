# Skillset architecture

Four skills that share one task workspace, plus `dd:help`, which explains the commands and only lists which task workspaces exist. Three are stages, and one is the control and re-entry point.

```text
            ┌── dd:ground
            │
dd:state ───┼── dd:shape
            │
            └── dd:execute
```

A new task normally runs the stages in order, and `dd:execute` repeats per slice:

```text
dd:ground ──► dd:shape ──► dd:execute ──┐
    ▲             ▲                     │ next slice
    │             └─────────────────────┤
    └─── requirement/context invalid ───┘
```

`dd:state` is not a stage and does not sit between stages. It is the entry point for a task that has already started, the re-entry point after an interruption, the task-state inspector ("where are we?"), the "what next?" interface, the checkpoint helper, and the router to whichever stage's work comes next. Each stage skill can still be invoked directly and resumes on its own.

| Skill | Question | Reads | Writes (owns) | Hands off when |
|---|---|---|---|---|
| `dd:ground` | What is wanted, and what is true now? | request, linked docs, code, tests, config, package/API docs | `SPEC.md`, `CURRENT_STATE.md`, `STATUS.md` | desired behavior is designable and relevant current state is verified; material ambiguities resolved or explicitly blocking |
| `dd:shape` | How will we get there, in what behavioral increments? | `SPEC.md`, `CURRENT_STATE.md` | `ARCHITECTURE.md`, `PLAN.md` (slices), `STATUS.md` | architecture sufficient for current scope; material unknowns resolved or spiked; ≥1 `ready` slice with `Done when` |
| `dd:execute` | Deliver one ready slice inside an explicit block | all five, calibration log | `PLAN.md` (slice state, notes, estimate/block/actual, discovered work), code, tests, `STATUS.md`, calibration log (append); appends verified discoveries to `SPEC.md`/`CURRENT_STATE.md`/`ARCHITECTURE.md` | slice `done`, or block stop condition reached and state checkpointed |
| `dd:state` | Where is this task really, and what happens next? | all five, repository/worktree state (branch, diff, tests), ticket | `STATUS.md` and `PLAN.md` slice state (reconciliation); all five when adopting (backfill) or checkpointing (verified discoveries to their home) | question answered; adoption or checkpoint exit met; or, on resume, at the routed skill's stop conditions |
| `dd:help` | Which command fits my situation? | user question; task-doc root listing | nothing | the question is answered |

## `dd:ground`

Establishes enough verified knowledge about the requirement and the technical context to support design.

- **Requirements** → `SPEC.md`: read the request; find explicit and hidden ambiguities (undefined terms, missing states, boundary cases, permissions, error behavior, migration/back-compat, assumptions that change implementation); test alternate interpretations; resolve from evidence; ask the user only when evidence cannot settle a material question; write concrete Given/When/Then examples including behavior that must not change.
- **Context** → `CURRENT_STATE.md`: only what the task touches: integrations, library/service contracts, relevant code/tests/config/data flow, analogous implementations and conventions, where authoritative docs live. Every fact is labeled and re-checkable.
- Does not design. This is the weakest-grounded area of the methodology. Codebase reconnaissance is mostly DERIVED (see `methodology-decisions.md`).

## `dd:shape`

Turns desired + current state into a bounded design and a behavioral plan, as a loop:

```text
architecture ──► architecture risk check ──► slice ──► slice readiness/risk check ──► exit
     ▲                                                        │
     └──────────────── design-level finding ◄─────────────────┤
                             slice-local finding ─► re-slice / spike slice ─► check again
```

1. **Architecture** (`step: architecture`): evaluate the design against `SPEC.md` and `CURRENT_STATE.md`. Record the design and decisions in `ARCHITECTURE.md`.
2. **Architecture risk check** (`step: architecture-risk`): test the whole design for risks, unknowns, dependencies and rabbit holes that could change it. Patch, fence, cut or spike each one. An unresolved dependency the design rests on blocks slicing.
3. **Slice** (`step: slicing`): write behavioral slices into `PLAN.md`. **Slices describe independently observable, verifiable behavior, not technical layers.**
4. **Slice readiness/risk check** (`step: slice-readiness`): check each near-term slice (observable, end to end, independent, downhill, small, consistent with the architecture) and mark it `ready` or `not-ready`. Design-level findings go back to step 1. Slice-local ones are re-sliced or spiked.

Future slices stay behavioral. Only the current or near-term slice gets implementation detail.

## `dd:execute`

Executes one understood slice inside an explicit work block.

1. **Prepare:** select the current ready slice; inspect its existing test and verification setup; break it into concrete tasks; estimate it (only if it is downhill), calibrated from the persistent log; decide the block (duration, goal, stop condition). Keep estimate ≠ block ≠ deadline.
2. **Implement:** incrementally, TDD where it fits: test list → one concrete behavior → failing test → minimal real implementation → inspect/refactor when useful → next. Discovered work is classified immediately (see below).
3. **Close:** reconcile task documents, record estimate vs actual in `PLAN.md` and append one record to the calibration log, update slice state, checkpoint an exact `Next`.

## `dd:state`

Reconstructs, explains, initializes/adopts, checkpoints and routes the state of a task. Five operations (conceptual, not subcommands):

- **State**: a compact operational summary (stage, current slice, done, current, open, next), verified against the files and repository rather than echoed from `STATUS.md`.
- **Next**: one concrete executable action.
- **Resume**: reconstruct → reconcile a stale cursor → route → continue under the routed skill (invoked when available).
- **Adopt**: for started work with no workspace. It backfills the five files conservatively from evidence (ticket, branch, diff, tests, commits, existing docs), identifies the current slice and stage, and records the next action. It does not replay completed stages, and it does not present inferred history as confirmed.
- **Checkpoint**: persists verified discoveries in their authoritative files, brings the current slice in `PLAN.md` up to date, keeps `STATUS.md` compact, and records one exact next action.

Routing, first match wins; a gap routes backward only if it is material to the current/next slice or the architecture they rest on:

| Observed state | Route |
|---|---|
| Material requirement ambiguity | `dd:ground` (requirements) |
| Relevant current-system behavior insufficiently understood | `dd:ground` (context) |
| Desired/current state known, architecture unresolved | `dd:shape` (architecture) |
| Existing architecture materially invalidated | `dd:shape` (architecture; artifact `stale`) |
| Current slice too large / risky / not ready | `dd:shape` (slice readiness) |
| Ready slice, none in progress | `dd:execute` (prepare) |
| Current slice in progress and still valid | `dd:execute` (implement) |
| All slices done/dropped | verify acceptance examples; close and report completion |

`dd:state` does not copy the stage skills' methodology. After routing, the stage's rules apply.

Before a downstream stage uses a `review-needed` artifact, it reconciles the specific uncertain claims that stage needs. Evidence may clear it to `complete`; an unresolved material claim routes to grounding or shaping. `draft` is ordinary unfinished work, while `stale` means known evidence contradicts the artifact. Generic re-entry language selects `dd:state`; explicit implementation language selects `dd:execute`, which still reconstructs state when entered directly.

## `dd:help`

Orientation only. A bare invocation returns the five-command cheat sheet, the normal flow and a situation → command list; a specific question gets a short answer naming one command. It lists the task-doc root to see which task workspaces exist and names them, but reads no task files, creates no workspace and starts no other skill. "Which dd command should I use?" belongs here; "what should I do next on this task?" belongs to `dd:state`.

## Cross-skill invariants

Encoded once per skill where they apply at runtime:

| Invariant | Where it is enforced at runtime |
|---|---|
| Evidence labels: verified / inferred / assumed / open; inferred history ≠ confirmed history | `references/task-state.md` (all four workflow skills) |
| Current state ≠ intended architecture | `task-state.md`; `dd:shape` SKILL.md |
| Scope: unrelated discoveries → `PLAN.md` → Discovered work; blockers re-planned explicitly | `dd:execute` SKILL.md + `references/scope-and-close.md` |
| Estimate ≠ timebox/appetite ≠ deadline | `dd:execute` SKILL.md + `references/estimate-and-block.md` |
| No precise estimates for uncertainty-dominated work; de-risk first | `dd:shape` SKILL.md; `dd:execute` SKILL.md |
| Stub dependencies, never fake the behavior under test | `dd:execute` `references/tdd-loop.md`; `dd:shape` `references/slicing.md` |
| Mid-work bugs: blocking → now; non-blocking → capture | `dd:execute` SKILL.md |
| Schedule revisable; current block not silently extended | `dd:execute` SKILL.md |
| Calibration history persists across tasks, append-only | `execute/scripts/calibration.py` + `references/estimate-and-block.md` |
| Substantive files + repository are authoritative; `STATUS.md` is a cached cursor, reconciled when stale | `task-state.md` → Authority, Resume; `dd:state` SKILL.md → Reconcile |
| An existing workspace is reconstructed before work starts; no invocation assumes a fresh stage | `task-state.md` → Resume + one line in each stage skill's "Enter or resume" |
| Started work is adopted by backfill, not replayed, and only by `dd:state` after consent | `task-state.md` → Resume; `dd:state` `references/adoption.md`; one hand-off line in each stage skill's "Enter or resume" |
| Needed user choices and confirmations go through the interactive question tool (inline fallback); routine judgment is not a question | one line in each SKILL.md where the skill asks; `dd:state` `references/adoption.md` → Before writing |
| Workflow vocabulary is identical across skills | shared `validate_work.py` + `tools/check.py` vocabulary check |

## Independence and resumability

- **Invoked directly.** Each workflow skill (`dd:help` only lists workspaces) starts by reading project instructions, then reconstructs state from an existing workspace (it does not assume it begins a fresh stage). For example, `dd:execute` invoked while S2 is `in-progress` resumes S2 from its tests and diff; it does not prepare a new plan. If there is no workspace and nothing has started: `dd:ground` initializes one. `dd:shape` and `dd:execute` point the user to `dd:ground`, or, if the user explicitly wants to skip it, create the missing files from the contract and record the skipped grounding as `Open`. If there is no workspace but work has started, any skill hands off to `dd:state`, the only skill that adopts: it proposes adoption (or proceeds, if the user asked for it), backfills, and routes back to the requested stage.
- **Out-of-order entry.** If the reconciled state names another stage, the invoked skill says so and either continues that stage's recorded `Next` (if it is within its remit) or returns.
- **Re-entry without knowing the stage.** `dd:state` answers "where did I leave off?" and routes, so the user does not need to know which stage skill to invoke.
- **Model switching.** Nothing lives only in the conversation. The contract, labels and vocabulary are identical across skills and models.

## Project instructions

The skills never require `AGENTS.md`/`CLAUDE.md` and never edit them. When such files exist, including nested/scoped ones, the applicable ones are obeyed. A project-defined location/format for specs or design docs replaces `.work/<task-id>/`. Project test, lint and commit conventions override skill defaults.

## Packaging

Each skill is self-contained: its references, scripts and templates travel in its own ZIP. The only duplication across packages is deliberate, so that each skill installs standalone: `references/task-state.md` and `scripts/validate_work.py` (all four workflow skills), and `scripts/init_work.py` with `assets/templates/` (`dd:ground` and `dd:state`). `tools/check.py` keeps the copies byte-identical, and the `skills/ground/` copy is the one to edit. The skills never read from this repository at runtime.
