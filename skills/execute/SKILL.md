---
name: execute
description: Use for explicit implementation intent on a prepared behavioral slice, including implement the current or ready slice, continue coding S2, execute this work block, finish or fix the current implementation, test it, or work on a prepared slice. Generic task re-entry such as "continue where I left off" belongs to dd:state.
---

# Execute

## Role in the workflow

- **Purpose:** Implement and verify the current ready behavioral slice.
- **Position:** Implementation stage after `dd:shape`; repeats for each ready slice.
- **Consumes:** The ready or in-progress slice in `PLAN.md`, supporting task files, and relevant code and tests.
- **Produces:** Verified behavior and updated code, tests, `PLAN.md`, and `STATUS.md`, including a checkpoint or close record.
- **Handoff:** Stop when the slice is verified done or the block's stop condition is reached and state is checkpointed. Continue with another `dd:execute` slice when requested; return to `dd:shape` if design or slice assumptions break, or to `dd:ground` for a material requirement gap. Complete the task when all slices and acceptance examples pass.

Outcome: the current slice is either `done`, meaning every `Done when` box is checked and verified by running something, or stopped at an explicit block boundary. Either way the task files record estimate vs actual, discoveries, and an exact next action.

## Hard rules

- Work on `current_slice` only. Discovered work that does not block it goes to `PLAN.md` → `Discovered work`, with a `D<n>` ID and where it was found. Do not silently absorb it.
- **Estimate ≠ block ≠ deadline.** The estimate predicts effort. The block is a decision about how much time to spend now. The deadline is an external commitment recorded in `SPEC.md`. Record each separately, and never adjust one to match another.
- Do not estimate, or start implementing, a slice whose approach or feasibility is still unknown. Return it to `dd:shape` for a spike or re-slice.
- Do not implement against a material requirement ambiguity or an invalidated design. Record it, and return to `dd:ground` or `dd:shape`.
- You may stub a dependency or deferred prerequisite. Never fake the behavior under test: no returning the expected literal, special-casing test inputs, weakening or deleting assertions, or copying computed output into expectations.
- Do not extend the current block because the work grew. At its stop condition: finish, cut scope, or explicitly allocate another block and record it. The wider schedule may be rebuilt freely.
- Do not ask about routine implementation judgment. Ask only when a material unresolved choice blocks the slice, continuing would change scope or observable behavior, or the user must pick between valid paths; use the environment's native interactive question tool (in Claude Code, `AskUserQuestion`) with short, mutually exclusive options; without one, ask one concise inline question.
- Follow the project's test, lint, commit and branch conventions. Do not commit, push or deploy unless the user or the project instructions say to.

## Enter or resume

1. Read applicable project instructions. Reconstruct current state before starting work (Resume in `references/task-state.md`): `STATUS.md`, then `PLAN.md`, and `SPEC.md`, `CURRENT_STATE.md` and `ARCHITECTURE.md` as they bear on the current slice. Resolve any `review-needed` claim the slice depends on before implementation; verify from evidence and clear it to `complete`, or route the material question to its owner. Do not assume this invocation begins a fresh slice.
2. If `current_slice` is `in-progress`, resume it. Compare its test list and `Done when` with the tests and the diff, and continue from what is actually done. Do not prepare or estimate it again, and do not rewrite tests that already exist. A change of conversation or model is not a reason to restart.
3. `current_slice` must exist and be `ready` or `in-progress`. If none is set, pick the first `ready` slice and set it. If no slice is ready, return to `dd:shape`.
4. No workspace: if the work has already started, hand off to `dd:state`, which owns adoption: invoke it if available (say whether the user explicitly asked to adopt, and that this stage was requested), otherwise stop and tell the user to run `/dd:state`. Do not create `.work/` yourself. Otherwise start with `dd:ground`.
5. Before changing implementation, inspect the verification setup for this slice: the test framework, nearby tests, relevant scripts and CI checks, and project testing conventions. On resume, reuse a recorded preflight only after checking it still applies. Record the chosen test path or other verification in the slice's `Implementation notes`. If a suitable test path exists, start each new testable behavior with a failing test; on resume, continue from tests already present. If no suitable path exists, record the gap and define proportionate verification before changing code; do not silently add a test framework. Ask only if the choice materially changes scope or needs the user's decision.

Read `references/task-state.md` before writing task files.

## Prepare (`step: prepare`)

In the slice's `Implementation notes`: restate its observable outcome, list the concrete tasks for this slice only, and add the test list. Then record, as separate lines:

- `**Estimate:**` the raw estimate from the concrete tasks, then a calibrated figure with its basis (`python3 scripts/calibration.py summary --estimator <id>`);
- `**Block:**` the duration and time, a goal, and a stop condition.

A spike slice (`S<n> — Spike: <question>`) gets no `**Estimate:**`: its `**Block:**` is the spike's timebox, and its `Done when` is met when the question is answered (or the timebox hit) and the result is recorded in `ARCHITECTURE.md` → Spikes.

Read `references/estimate-and-block.md` for calibration, what to do when the estimate exceeds the block, and examples. If a task cannot be named as a concrete action, or the work is still uphill, the slice is not ready. Say so and return it to `dd:shape`.

Set the slice `in-progress` and `step: implement`.

## Implement (`step: implement`)

Where behavior can be tested, run the TDD loop: test list → pick one concrete behavior → write a failing test and watch it fail for the intended reason → make it and all earlier tests pass with the minimal real implementation → inspect the new code for an actual design problem and refactor if there is one → next behavior. Add newly discovered cases to the test list instead of chasing them. Read `references/tdd-loop.md` for the loop's rules, its anti-patterns, and the stub-vs-fake line.

Where test-first does not fit (layout, exploratory spikes, configuration), define the verification before changing things, then perform it.

Keep going while the next step is clear and inside the slice. A finished substep or an available progress update is not a reason to stop.

Classify each discovery as it happens:

| Discovery | Action |
|---|---|
| Needed to meet this slice's `Done when` | Do it now, inside the block. |
| Bug that blocks or invalidates this slice, including bugs in this slice's new code | Fix it now. Its time counts in the slice's actual. |
| Bug or improvement that does not block this slice | Record it in `Discovered work` and continue. |
| New or changed requirement | Record it in `SPEC.md` (labeled). If it changes this slice's behavior or is material, stop and ask. Otherwise add it as discovered work. |
| Current-state fact was wrong | Correct `CURRENT_STATE.md`. If the design depends on it, mark `ARCHITECTURE.md` `stale` and return to `dd:shape`. |
| Slice is larger than planned | Stop at the block boundary and return to `dd:shape` to re-slice. Do not extend. |

Read `references/scope-and-close.md` for examples of each.

## Close (`step: close`)

At the slice's completion, the block's stop condition, or a user stop:

1. Run the verification: tests, lint/type checks where the project uses them, and each `Done when` item. Check a box only after it has been verified.
2. Write verified discoveries to their authoritative file. Mark an artifact `stale` when implementation proves it wrong; use `review-needed` when changed or reconstructed content still needs a reliability check before a dependent stage can use it.
3. Record `**Actual:**` (the real elapsed time, including bug fixes and interruptions; never invented), and compare it with the estimate. When the slice is `done` and both numbers exist, append one record with `scripts/calibration.py append` (see `references/estimate-and-block.md`).
4. Set the slice to `done`, leave it `in-progress` with the remaining test list, or mark it `blocked` with the reason.
5. `python3 scripts/validate_work.py <workspace>`, then set `STATUS.md` → `Next` to one concrete action.

After a slice is `done`: continue to the next `ready` slice only if the user asked for more than one slice. Otherwise stop with `Next` pointing at preparing it, or at `dd:shape` if none is ready. When every slice is `done` or `dropped` and `SPEC.md`'s acceptance examples pass, set `status: done`.
