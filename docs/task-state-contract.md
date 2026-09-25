# Task-state contract

The canonical contract shared by `dd:ground`, `dd:shape`, `dd:execute` and `dd:state`. Each skill ships a compact runtime copy in `references/task-state.md`. Those four copies must stay byte-identical (`tools/check.py` enforces this). If this document and the runtime copy disagree, fix both in the same change.

The task files are the durable external memory of the workflow. Conversation history is secondary context: durable task files and observable repository state are the basis for resumption. A new conversation, a restarted tool, or a different model (GPT-5.6 Sol, Claude Opus 5.5) must be able to continue from the files and the repository alone.

## Location

1. If the project's applicable instructions (`AGENTS.md`, `CLAUDE.md`, nested/scoped equivalents, contributor docs) define a location or format for task, spec or design documents, use it. Map the five roles below onto it, and do not create a parallel `.work/` tree.
2. Otherwise use `.work/<task-id>/`. `<task-id>` uses letters, digits, `.`, `_`, `-`, for example a ticket key (`PROJ-123`) or a short slug (`profile-name-edit`).
3. Whether `.work/` is committed or gitignored is the project's decision. The skills do not edit `.gitignore` unless asked.

```text
.work/<task-id>/
├── STATUS.md          cursor
├── SPEC.md            what should become true
├── CURRENT_STATE.md   what is true now
├── ARCHITECTURE.md    how we intend to get there
└── PLAN.md            behavioral slices and their state
```

## Semantic ownership

Each fact has one home. When a fact belongs to another file, write it there and link to it rather than copying it.

| File | Question it answers | Contains | Primary writer |
|---|---|---|---|
| `SPEC.md` | What should become true? | Problem, desired behavior, acceptance examples, scope in/out, edge cases, assumptions, open requirement questions, requirement sources | `dd:ground` (others update it when requirements change, never silently) |
| `CURRENT_STATE.md` | What is true now? | Verified current behavior, relevant code paths and tests, services, package/API behavior, existing patterns, constraints, unknowns, re-checkable references | `dd:ground` (others append verified discoveries) |
| `ARCHITECTURE.md` | How do we currently intend to get from current to desired state? | Proposed design, affected components, flows/interfaces, decisions with reasons, alternatives, risks/rabbit holes, spikes, technical open questions, out-of-scope design | `dd:shape` |
| `PLAN.md` | What behavioral increments will we deliver, and what is their state? | Slices (the **single source of truth for slices**), current-slice implementation notes, estimate/block/actual records, discovered work | `dd:shape` creates slices; `dd:execute` updates them |
| `STATUS.md` | Where is the workflow cursor and what exactly happens next? | Stage, step, status, current slice, artifact states, open blockers, one next action | every skill at every checkpoint; `dd:state` when reconciling |

`dd:state` writes the substantive files in three situations: when adopting started work (it backfills all five from evidence), at a checkpoint (it moves verified discoveries to their home file), and when reconciling a stale cursor (it corrects `PLAN.md` slice-state lines — status and verified checkboxes, which are workflow state like the cursor — to match evidence; slice definitions are substance and stay untouched). It does not do new requirements analysis, design or implementation; those stay with the owning skill.

Separation rules:

- `CURRENT_STATE.md` never describes intended design. `ARCHITECTURE.md` never asserts current behavior that `CURRENT_STATE.md` has not verified.
- `STATUS.md` never holds research, decisions, or slice definitions. It points at them.
- Slice definitions exist only in `PLAN.md`. `ARCHITECTURE.md` may refer to slice IDs but does not define slices.

## Authoritative state and the cached cursor

The task's **authoritative substantive state** is

```text
SPEC.md + CURRENT_STATE.md + ARCHITECTURE.md + PLAN.md
+ observable repository/worktree state (code, tests and their results, branch, commits, uncommitted changes)
```

`STATUS.md` is a **cached workflow cursor**: a compact record of where the previous agent believed the workflow had reached and what should happen next. It is important, because it is the fastest way to orient, but it is not an unquestionable oracle. An agent orients with it, then checks the claims the next action depends on.

When the substantive files or the repository clearly show that `STATUS.md` is stale, reconcile: correct `STATUS.md` (and `PLAN.md` slice state if that is also behind) to match reality, say what changed, and act on the corrected state. Never edit substance to agree with the cursor.

Example: `STATUS.md` → `Next: Add a failing validation test.`, but that test already exists in the branch and part of the implementation has landed. The agent does not write the test again. It updates the slice's implementation notes and `STATUS.md` to the actual progress, and the next action becomes the next unfinished item (for example, running the test and implementing what it still exercises).

The calibration log (below) is cross-task history. It never determines a task's state.

## Evidence labels

Use these labels wherever uncertainty matters (all five files):

- **Verified**: observed in code, tests, running behavior, configuration, authoritative documentation, or confirmed by the requester. Cite where, so it can be re-checked.
- **Inferred**: a conservative conclusion from verified evidence.
- **Assumed**: a provisional belief adopted to keep moving. States what would invalidate it.
- **Open**: unknown.

Rewording an assumption does not verify it. Only new evidence changes a label.

Past intent, earlier decisions, rationale and acceptance criteria that are read off code or commits are **Inferred** at best, unless a person, ticket or document confirms them. This matters most when adopting started work: the goal is a reliable state from now on, not a reconstructed history (see [Adopting started work](#adopting-started-work)).

## `STATUS.md`

```markdown
---
stage: shape
step: architecture
status: in-progress
current_slice:
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

Verify whether package X exposes Y (read its typed exports in node_modules/x/index.d.ts), then record the data-flow decision in ARCHITECTURE.md → Decisions.
```

Frontmatter values:

| Key | Allowed values |
|---|---|
| `stage` | `ground`, `shape`, `execute`: the stage the cursor is in. At `status: stage-complete` with `step: handoff` it names the stage just finished, and `Next` points at the following stage (legacy `ground-work`, `shape-work`, `execute-work` are accepted with a warning) |
| `step` | ground: `requirements`, `context`, `handoff` · shape: `architecture`, `architecture-risk`, `slicing`, `slice-readiness`, `handoff` (iterated as a loop, see `skillset-architecture.md`) · execute: `prepare`, `implement`, `close` |
| `status` | `in-progress`, `blocked`, `needs-user`, `stage-complete`, `done` (whole task finished) |
| `current_slice` | empty, or a slice ID that exists in `PLAN.md` |
| `updated` | ISO date |

Artifact states: `not-started`, `draft`, `blocked`, `review-needed`, `complete`, `stale`.

- `draft`: normal incomplete work; its missing parts have yet to be produced.
- `review-needed`: content exists, but reconstructed, invalidated, or otherwise unconfirmed material must be reconciled before a downstream stage treats the material it depends on as settled. Name the uncertain claim or section and its evidence in the artifact or `Open`. Verification may clear it without a human review.
- `stale`: known evidence shows the artifact no longer reflects reality. Name the contradicted part and evidence under `Open`; repair the affected content before depending on it.

The state applies to an artifact, but reconciliation is scoped to the next stage's dependencies. Identify the specific uncertain claims it needs, check available evidence, and set the artifact to `complete` when those claims are sufficiently verified and no material uncertainty remains for that stage. If evidence cannot settle a material claim, ask the specific question or route to grounding/shaping. Unrelated uncertainty may remain explicitly labeled; do not require a ceremonial full-document review. A `review-needed` artifact is not automatic permission to hand off or execute.

`## Next` holds **one** concrete action that names what to do and which artifact/section it updates. It must be executable by an agent with no conversation history.

- Bad: `Continue architecture.`
- Good: `Verify whether package X exposes Y, then finish the data-flow decision in ARCHITECTURE.md.`

## `PLAN.md`

```markdown
# Plan

## Slices

## S1 — Owner deletes their own comment and it disappears for everyone

**Status:** ready

**Behavior**
Given a signed-in user who authored a comment, when they delete it, then it is no longer shown in the thread for any viewer.

**Done when**
- [ ] Owner delete removes the comment from the thread view (automated test).
- [ ] Non-owner delete attempt returns 403 and the comment remains.

**Dependencies**
None. Uses the existing session guard.

**Known unknowns**
None blocking.

**Implementation notes**
<!-- detailed tasks, estimate, block and actual are added when this slice becomes current -->

## Discovered work

- [ ] D1 — Comment serializer exposes author_email (found during S1; not blocking; candidate bug)
```

Rules:

- Slice headings are `## S<n> — <behavioral title>`. IDs are stable: never renumber, never reuse. A dropped slice keeps its ID with status `dropped`.
- Slice statuses: `candidate` (idea, not yet examined), `not-ready` (examined, has unresolved unknowns or dependencies), `ready` (can be executed now), `in-progress`, `blocked`, `done`, `dropped`.
- At most one slice is `in-progress`, and it is `STATUS.md`'s `current_slice`.
- A slice is `done` only when every `Done when` box is checked.
- Behavioral slices are not implementation-task lists. Titles describe observable behavior, not layers (`database`, `backend`, `frontend`, `tests`).
- A spike slice is titled `S<n> — Spike: <question>`; its `Done when` is the question answered (or the timebox hit) and the result recorded in `ARCHITECTURE.md` → Spikes. It gets a `**Block:**` timebox, never an `**Estimate:**`, and is never appended to the calibration log.
- Detailed implementation notes are written mainly for the current or next slice.
- `## Discovered work` holds work found along the way that must not silently enter the current slice. Items use `D<n>` IDs, say where they were found, and whether they block.

Execution records, added to the current slice by `dd:execute`:

```markdown
**Estimate:** 3h raw → ~5h calibrated (basis: ...). Recorded 2026-09-25.
**Block:** 2h, 2026-09-25 10:00–12:00. Goal: owner-delete example green end to end. Stop: goal met, or 11:30 with no passing test → re-plan.
**Actual:** 3.5h over 2 blocks, including 40min on a rounding bug in this slice's code.
```

Estimate, block and deadline are different lines because they are different things (see `methodology-decisions.md`). A deadline, if one exists, belongs in `SPEC.md` → Scope as an external constraint.

## Calibration log

Estimate-vs-actual history persists outside task workspaces, so calibration survives deleted `.work/` directories and carries across projects.

- **Location:** `$DELIBERATE_DEV_CALIBRATION` if set, otherwise `~/.deliberate-development/calibration.jsonl`. It is created on first append (directory mode 700, file mode 600).
- **Format:** JSON Lines, one completed slice per line, schema 1:

```json
{"schema": 1, "recorded_at": "2026-09-25T16:02:11+00:00", "project": "shop", "task_id": "ORD-12", "slice_id": "S1",
 "estimator": "claude-opus-5-5", "estimate_hours": 8.0, "calibrated_hours": 13.0, "actual_hours": 12.5,
 "velocity": 0.64, "novel": false, "includes": "1.5h rounding bug in slice code; 1h interruption",
 "note": null, "corrects": false}
```

| Field | Type | Rule |
|---|---|---|
| `schema` | int | `1` |
| `recorded_at` | ISO-8601 UTC | set by the script |
| `project` | string | repository name (or the project's own identifier) |
| `task_id`, `slice_id` | string | the workspace's task id and `S<n>` |
| `estimator` | string | who produced the estimate: a person, or the model id when the agent estimated. Velocity is personal, so summaries filter on it. |
| `estimate_hours` | number > 0 | the raw estimate from `**Estimate:**` |
| `calibrated_hours` | number > 0 or null | the calibrated figure, if one was given |
| `actual_hours` | number > 0 | measured elapsed time, including in-slice bug fixes and interruptions (Spolsky) |
| `velocity` | number | `estimate_hours / actual_hours`, computed by the script |
| `novel` | bool | the slice involved work new to the estimator |
| `includes`, `note` | string or null | what the actual includes; free note |
| `corrects` | bool | this record supersedes an earlier one for the same `(project, task_id, slice_id)` |

**Append behavior** (enforced by `execute/scripts/calibration.py`):

- Append once per slice, when it becomes `done` and both a raw estimate and a measured actual exist. Never append spikes (timeboxes, not estimates), dropped or abandoned slices, or untracked actuals.
- Append-only. Existing lines are never rewritten, reordered or deleted, and unreadable lines are left in place and skipped by readers.
- A second record for the same `(project, task_id, slice_id)` is refused (exit 3) unless `--correction` is passed. Readers use the latest record per key.
- Each record is one `write` to a file opened with `O_APPEND`.
- If the log cannot be written (sandbox, read-only home, or project instructions forbidding writes outside the repository), the agent notes `Calibration: not appended (<reason>)` on the slice's `**Actual:**` line and does not work around the restriction.

**Reading:** `calibration.py summary --estimator <id> [--project P] [--months 6]` prints the record count, velocity min/median/max, the implied factor (1/median) and a novel-work subset, using records from the last six months. Under six records it flags the history as insufficient. The model decides how to use these numbers; the script never produces an estimate.

The `PLAN.md` `**Estimate:**`/`**Actual:**` lines remain the task-local record; the log is the cross-task history.

## Resume protocol

An existing workspace means the task has already started. Every skill reconstructs current state before starting work, and none assumes its invocation begins a fresh stage.

1. Read applicable project instructions.
2. Read `STATUS.md`.
3. Read the substantive files the current stage depends on.
4. Check the cursor against those files and the repository: during execution, the current slice's tests and code, `git status` and the diff. Detect relevant `review-needed` and `stale` artifacts and reconcile the specific sections the next stage needs before relying on them. The validator catches mechanical contradictions and warns about suspect states; semantic reconciliation needs reading. Reconcile as described under [Authoritative state and the cached cursor](#authoritative-state-and-the-cached-cursor).
5. Continue from the reconciled `Next`, doing only the part of the stage that is not yet done.
6. Do not redo completed work unless new evidence invalidates it. If it does, mark the affected artifact `stale` and record why.

`dd:state` runs this protocol for "where did I leave off?", "what next?" and "resume" requests, and routes to the skill whose work comes next. The other skills run it on entry.

## Adopting started work

When work on a task has started (branch changes, commits, new tests) but no workspace exists, the workspace is backfilled from that evidence. The workflow is not started over from an empty `SPEC.md`. Only `dd:state` does this (`references/adoption.md` in that skill): it creates the workspace, chooses the task identifier, asks for consent unless adoption was explicitly requested, backfills, and routes back to the stage that was asked for. `dd:ground`, `dd:shape` and `dd:execute` hand off to it instead of adopting. The contract-level rules are:

- Backfill only what is needed to understand what has been done, find material gaps, and continue safely. Do not replay completed analysis or implementation.
- Label reconstructed content by evidence. Inferred history is not confirmed history. Do not fabricate earlier decisions, acceptance criteria, rationale, estimates, original intent or completed slices. Unknown history is recorded as unknown.
- A backfilled slice is `done` only if every `Done when` box has been verified by running something at adoption time. Adopted slices get no retroactive estimate. Their actual is `not tracked (predates adoption)` unless real time records exist.
- Each backfilled file starts with a one-line note saying it was backfilled, when, and from which branch and base.
- If adoption exposes a material gap, route backward only as far as the gap requires.
- Backfilled content whose material claims are not yet confirmed is `review-needed`; identify the claims and reconcile those needed by the next stage before it proceeds.

## Checkpoint protocol

At each meaningful checkpoint (decision made, question resolved, investigation finished, block boundary, user stop):

1. Write verified knowledge into its authoritative file.
2. Mark unfinished or provisional reasoning as such, where it lives.
3. Update `## Open`.
4. Update artifact and slice states. For the current slice, check boxes only for verified items and keep the remaining test list or tasks in `Implementation notes`. Work found along the way goes to `Discovered work`, not into the slice.
5. Write one concrete `## Next` action and the `updated` date. `STATUS.md` stays compact: it points at findings and does not copy them.

## Validation

`scripts/validate_work.py <workspace>` checks mechanical invariants only: required files, parseable frontmatter, known values, an ISO `updated` date, artifact-state lines, duplicate slice IDs, `current_slice` existence and compatibility, one in-progress slice, `done` slices with unchecked boxes, and state contradictions such as slices present while `PLAN.md` is `not-started`. It warns (without failing) where the cursor looks stale against `PLAN.md`: the current slice is `in-progress` with every box checked; the stage is before execution while a slice is `in-progress`; execution continues while `SPEC.md` or `ARCHITECTURE.md` is `stale`, or with any `review-needed` artifact. The warning calls for dependency-specific reconciliation; the script cannot determine materiality. It never reads the repository and never judges requirements, design, risk, slicing, estimates or which slice is current. It exits non-zero on errors and changes no files.

`scripts/init_work.py <task-id>` (shipped in `dd:ground` and `dd:state`) creates missing task files from templates and never overwrites. Nothing in the scripts adopts a task, reconstructs requirements or architecture, interprets git changes, or routes. Those need judgment.
