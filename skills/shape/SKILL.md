---
name: shape
description: Turn grounded requirements and verified current state into a bounded architecture, explicit risks and spikes, and independently verifiable behavioral slices, iterating between architecture and slice-level risk checks. Use after dd:ground, or when asked to design, de-risk, break down, or plan a non-trivial software task. Reads SPEC.md and CURRENT_STATE.md; maintains ARCHITECTURE.md, PLAN.md and STATUS.md in a resumable task workspace.
---

# Shape

## Role in the workflow

- **Purpose:** Turn grounded understanding into an implementable design and behavioral slices.
- **Position:** Between `dd:ground` and implementation; returns here when design or slice readiness needs revision.
- **Consumes:** `SPEC.md`, `CURRENT_STATE.md`, and existing task state when resuming.
- **Produces:** `ARCHITECTURE.md` and `PLAN.md`, with `STATUS.md` pointing to a ready slice or a blocker.
- **Handoff:** Move to `dd:execute` when the needed architecture is decided, material risks are resolved or scheduled as spikes, and at least one slice has verifiable `Done when` conditions and is ready. Return material requirement gaps to `dd:ground`.

Outcome: `ARCHITECTURE.md` records a design sufficient for the current scope, with material unknowns resolved or fenced off. `PLAN.md` holds behavioral slices, at least one of them `ready`, with observable done conditions.

## Hard rules

- Slices describe independently observable, verifiable behavior, never technical layers. `database / backend / frontend / tests` is not a slice structure.
- `PLAN.md` is the only place slices are defined. Future slices stay behavioral. Write implementation detail only for the current or next slice.
- `ARCHITECTURE.md` is intended design. Do not restate it as current fact, and do not edit `CURRENT_STATE.md` to fit the design. New verified facts go to `CURRENT_STATE.md`; changed requirements go to `SPEC.md`, stated explicitly, never slipped in to suit an architecture.
- Before finalizing a decision, verify every material assumption that can be checked from available evidence: read the code, the types, the installed package, the docs for the installed version, or run a probe.
- Do not add future-facing abstractions, configuration or extension points unless the current scope requires them.
- Size and uncertainty are separate problems: slice what is large; spike what is unknown. Do not attach a precise effort number to work whose feasibility or approach is still unknown.
- Ask the user only for decisions that are theirs: scope trade-offs, accepting a risk, choosing between options with different observable behavior or cost. Technical facts you can establish yourself are not questions for the user. If requirements or constraints favor one option, take it and record why; do not turn design into a series of approvals. When a user decision is needed, ask through the environment's native interactive question tool (in Claude Code, `AskUserQuestion`) with short, mutually exclusive options; without one, ask one concise inline question.

## Enter or resume

1. Read applicable project instructions and obey them, including where design docs live.
2. Existing workspace: reconstruct current state before starting work (Resume in `references/task-state.md`), reading `SPEC.md`, `CURRENT_STATE.md`, then `ARCHITECTURE.md` and `PLAN.md` if they have content. Reconcile the specific `review-needed` claims the design or next slice depends on before treating them as settled. Do not assume this invocation begins a fresh stage. Keep decisions and slices that still hold, revise only what the evidence invalidates, and leave `done` slices alone.
3. No workspace, but the work has already started: hand off to `dd:state`, which owns adoption: invoke it if available (say whether the user explicitly asked to adopt, and that this stage was requested), otherwise stop and tell the user to run `/dd:state`. Do not create `.work/` yourself or design from scratch.
4. No workspace, or `SPEC.md`/`CURRENT_STATE.md` not started: run `dd:ground` first. If the user explicitly wants to skip it, create the missing files per `references/task-state.md`, record the skipped grounding under `Open`, and verify each fact you rely on as you go.
5. If `SPEC.md` has an unresolved material question, stop and return it to the user. Do not design around it.

Read `references/task-state.md` before writing task files.

## Loop

```text
architecture → architecture risk check → slice → slice readiness/risk check
      ▲                  │                                   │
      └──── design-level problem found ◄─────────────────────┤
                                     slice-local problem ─► re-slice / spike slice
```

Iterate until the exit criteria hold. Each pass updates the files; `STATUS.md` → `step` shows where the loop is.

### Architecture (`step: architecture`)

Record in `ARCHITECTURE.md`: the goal, the proposed design, affected components, data/control flows and interfaces, decisions with their reasons, and out-of-scope design. List alternatives only where a real choice existed, and say why they lost. Follow existing project patterns recorded in `CURRENT_STATE.md` unless `SPEC.md` requires otherwise.

### Architecture risk check (`step: architecture-risk`)

Test the design as a whole. Walk the main use case through it step by step, and list every point where it rests on something not yet verified. Resolve now any unknown that could change the architecture, feasibility, data migration or permissions. For each risk choose one response and record it under Risks: **patch** (a simpler decided solution), **fence** (declare it out of scope), **cut**, or **spike** (a time-boxed question with the decision it unlocks). Read `references/architecture-and-risk.md` for the viability questions and the spike format.

An unresolved dependency that the whole design rests on keeps `ARCHITECTURE.md` `blocked` or `review-needed`. It does not become a slice note, and slicing does not start on top of it.

### Slice (`step: slicing`)

Write slices into `PLAN.md` in the contract format: stable `S<n>` IDs, a behavioral title, status, Given/When/Then behavior, `Done when` checkboxes, dependencies, and known unknowns. Choose the first slice as the smallest end-to-end behavior that is core to the problem and exercises the riskiest part. Stub peripheral prerequisites to reach it. Read `references/slicing.md` for split patterns, first-slice choice and contrastive examples.

### Slice readiness/risk check (`step: slice-readiness`)

Check the first slice and any near-term ones individually, using the readiness checklist in `references/slicing.md`. Mark each one `ready` or `not-ready`, and write the reason for `not-ready` in the slice. Later slices may stay `candidate`.

Route what the check finds:

- **Slice-local problem** (too large, overlapping, unknown confined to this slice, missing prerequisite): re-slice, add a spike slice, or stub the prerequisite. Then check again.
- **Design-level problem** (the slice reveals that a component, flow or interface in `ARCHITECTURE.md` is wrong or unverified): set `ARCHITECTURE.md` to `draft` and record the finding under Risks or Open technical questions. Return to `step: architecture`.
- **Requirement problem**: record it in `SPEC.md` → Open questions and return to `dd:ground` if it is material.

## Checkpoint

Write decisions to `ARCHITECTURE.md` and slices to `PLAN.md` before updating `STATUS.md`. When stopping mid-stage, `Next` names the exact decision or question and the section it updates. For example: "Verify whether package X exposes Y, then finish the data-flow decision in ARCHITECTURE.md → Decisions." Not "Continue architecture."

## Exit → `dd:execute`

Set `step: handoff`, `status: stage-complete`, `current_slice` to the first ready slice, and point `Next` at preparing that slice, when all of these hold:

- the architecture needed by the first ready slice is decided and verified; `ARCHITECTURE.md` is `complete`, or remaining `review-needed` material is explicitly unrelated to that slice;
- the architecture risk check has no open design-level risk (each is patched, fenced, cut, or a completed/scheduled spike);
- the first slice passed the readiness check, or it is itself a spike slice (slice form in `references/architecture-and-risk.md`);
- `PLAN.md` has at least one `ready` slice with `Done when` conditions;
- `python3 scripts/validate_work.py <workspace>` reports no errors.

If these do not hold, stay in `dd:shape` or record the blocker. Do not pass ambiguity downstream. Stop at the handoff unless the user asked for the whole workflow.

Return here from `dd:execute` when a slice's architecture is invalidated, a slice proves too large, or discovered work needs to become new slices.
