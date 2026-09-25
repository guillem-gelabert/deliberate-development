# Task-state contract

Shared by `dd:ground`, `dd:shape`, `dd:execute`, `dd:state`. This file is identical in all four workflow skills (not `dd:help`).

## Location

Use the project's own convention for task/spec/design documents if its applicable instructions define one; map the roles below onto it. Otherwise use `.work/<task-id>/` (`<task-id>`: letters, digits, `.`, `_`, `-`). Do not edit `.gitignore` or project instruction files to accommodate the workspace unless asked.

## Files and ownership

One home per fact. Link instead of copying.

- `SPEC.md` — what should become true: problem, desired behavior, acceptance examples, scope in/out, edge cases, assumptions, open requirement questions, sources. A deadline, if any, goes under scope as an external constraint.
- `CURRENT_STATE.md` — what is true now: verified behavior, code paths, tests, services, package/API behavior, patterns, constraints, unknowns, re-checkable references. Never intended design.
- `ARCHITECTURE.md` — how we intend to get from current to desired state: design, affected components, flows/interfaces, decisions and reasons, alternatives, risks, spikes, technical open questions, out-of-scope design. Refers to slice IDs; does not define slices.
- `PLAN.md` — the single source of truth for slices, their states, current-slice implementation notes, estimate/block/actual records, and `Discovered work`.
- `STATUS.md` — the cursor only: stage, step, status, current slice, artifact states, open blockers, one next action. No research, decisions, or slice definitions.

## Authority

- The task's actual state is `SPEC.md` + `CURRENT_STATE.md` + `ARCHITECTURE.md` + `PLAN.md` + the observable repository/worktree (code, tests, branch, uncommitted changes, test results).
- `STATUS.md` is a cached workflow cursor: where the previous agent believed the workflow had reached and what it expected next. Orient with it, then check it. When the substantive files or the repository clearly contradict it, they win: correct `STATUS.md` (and `PLAN.md` slice state if that is also behind), say what changed, and act on the corrected state.
- Conversation history is secondary context. Resume from the files and the repository, not from memory of an earlier chat.
- The personal calibration log (outside the workspace) is cross-task estimation history. It never determines a task's state.

## Evidence labels

**Verified** (observed or confirmed; cite where) · **Inferred** (conservative conclusion from verified evidence) · **Assumed** (provisional; say what would invalidate it) · **Open** (unknown). Rewording never upgrades a label; only evidence does. Past intent, decisions, rationale and acceptance criteria read off code or commits are **Inferred** at best, unless a person, ticket or document confirms them.

## STATUS.md

```markdown
---
stage: shape          # ground | shape | execute
step: architecture         # see below
status: in-progress        # in-progress | blocked | needs-user | stage-complete | done
current_slice:             # empty or a slice ID from PLAN.md
updated: 2026-09-25
---

# Status

## Artifact state

- SPEC.md: complete
- CURRENT_STATE.md: complete
- ARCHITECTURE.md: draft
- PLAN.md: not-started

## Open

- Does package X expose Y? Blocks the data-flow decision.

## Next

Verify whether package X exposes Y, then finish the data-flow decision in ARCHITECTURE.md → Decisions.
```

Steps — ground: `requirements`, `context`, `handoff` · shape: `architecture`, `architecture-risk`, `slicing`, `slice-readiness`, `handoff` (a loop; see dd:shape) · execute: `prepare`, `implement`, `close`. `stage` names the stage the cursor is in; at `status: stage-complete` with `step: handoff` it is the stage just finished, and `Next` names the following stage.

Artifact states: `not-started`, `draft`, `blocked`, `review-needed`, `complete`, `stale`.

- `draft`: normal incomplete work.
- `review-needed`: content exists, but reconstructed, invalidated, or otherwise unconfirmed material cannot be treated as settled by a downstream stage until the material it needs is reconciled. Identify the uncertain claims/sections and their evidence. This does not automatically require a human review.
- `stale`: known evidence shows the artifact no longer reflects reality. Name the contradicted part and evidence under `Open`; repair it before depending on it.

On entry or resume, identify `review-needed`/`stale` artifacts relevant to the next stage. Check the specific claims that stage needs against available evidence. When the needed claims are sufficiently verified and no material uncertainty remains for that stage, update them and clear `review-needed` to `complete`. If evidence cannot settle a material claim, ask the specific question or route to grounding/shaping. Explicitly label unrelated uncertainty; do not force a full-document review. A `review-needed` artifact is not automatic clearance to execute.

`Next` is one action naming what to do and which file/section it updates, executable by an agent with no chat history. Not "Continue architecture."

## PLAN.md

```markdown
# Plan

## Slices

## S1 — <observable behavior, not a layer>

**Status:** ready

**Behavior**
Given ..., when ..., then ...

**Done when**
- [ ] ...

**Dependencies**
...

**Known unknowns**
...

**Implementation notes**
<!-- detailed tasks mainly once this slice is current -->

## Discovered work

- [ ] D1 — <item> (found during S1; blocking: no)
```

- IDs `S<n>` are stable: never renumber or reuse. Dropped slices stay, marked `dropped`.
- Slice states: `candidate` (unexamined idea), `not-ready` (unknowns or dependencies unresolved), `ready`, `in-progress`, `blocked`, `done`, `dropped`.
- At most one slice is `in-progress`; it is `current_slice`.
- `done` requires every `Done when` box checked.
- Execution records on the current slice, each its own line:
  `**Estimate:** <raw> → <calibrated> (basis)` · `**Block:** <duration, when>. Goal: ... Stop: ...` · `**Actual:** <time, what it includes>`.
- A spike slice is titled `S<n> — Spike: <question>`; its `Done when` is the question answered (or the timebox hit) and the result recorded in `ARCHITECTURE.md` → Spikes. It gets a `**Block:**` timebox, never an `**Estimate:**`.

## Resume

An existing workspace means the task has already started. Reconstruct its state before starting work; do not assume this invocation begins a fresh stage.

1. Read applicable project instructions.
2. Read `STATUS.md`, then the files the current stage depends on.
3. Check the cursor against those files and the repository (during execution: the current slice's tests and code, `git status` and diff). Check relevant `review-needed`/`stale` claims before relying on them. Run `scripts/validate_work.py <workspace>`; its warnings require judgment about materiality. Reconcile as described under Authority.
4. Continue from the reconciled `Next`, doing only the part of the stage that is not yet done. Do not redo completed work unless new evidence invalidates it; then mark the artifact `stale` and record why.

Work already started with no workspace (branch changes, commits, new tests): only `dd:state` adopts it, by backfilling the files from that evidence after the user's consent. Other skills hand off to `dd:state` and write nothing. Do not start the workflow over from an empty `SPEC.md`.

## Checkpoint

1. Write verified knowledge to its authoritative file.
2. Mark provisional reasoning as provisional where it lives.
3. Update `Open`, artifact states, slice states.
4. Write one concrete `Next` and the `updated` date.
