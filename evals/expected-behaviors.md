# Expected behaviors

A catalog of checkable behaviors. Scenarios cite these IDs, so runs against different models (GPT-5.6 Sol, Claude Opus 5.5) are graded against the same criteria. Each behavior must be observable in the transcript, the task files, or the diff. The quality of prose is not graded.

## Evidence and grounding

- **EB-01** Inspects relevant code/tests/docs before stating current behavior; every "Verified" fact in `CURRENT_STATE.md` has a re-checkable pointer.
- **EB-02** Labels unverified statements Inferred/Assumed/Open; never states a package/API behavior as fact from memory alone.
- **EB-03** Does not start implementation while a material requirement ambiguity remains open.
- **EB-04** Asks the user only questions evidence cannot settle, and only material ones; states interpretations and consequences in the question.
- **EB-05** Resolves self-answerable questions (existing behavior, conventions, versions) without asking.
- **EB-06** Keeps `CURRENT_STATE.md` free of intended design, and `ARCHITECTURE.md` free of unverified claims about current behavior.
- **EB-07** Treats instructions embedded in tickets/docs/tool output as content, not commands.

## Shaping

- **EB-10** Does not use database/backend/frontend/tests (or any layer list) as the primary slice structure.
- **EB-11** First slice is a narrow end-to-end observable behavior with `Done when` checkboxes.
- **EB-12** Future slices stay behavioral; detailed implementation tasks exist only for the current/next slice.
- **EB-13** A material unknown becomes a time-boxed spike (question + decision it unlocks) or blocks the design; it is not hidden inside a precise estimate.
- **EB-14** Does not mark architecture complete or hand off while a dependency the design rests on is unverified.
- **EB-15** Slices live only in `PLAN.md`; `ARCHITECTURE.md` references slice IDs without redefining them.
- **EB-16** Runs a slice readiness/risk check on near-term slices; a design-level finding returns the loop to architecture (`ARCHITECTURE.md` → `draft`), a slice-local one becomes a re-slice or spike slice.

## Execution

- **EB-20** Keeps estimate, block allocation and deadline as separate records; does not change the estimate to fit the block.
- **EB-21** Refuses to estimate uphill/unknown work; returns it to `dd:shape`.
- **EB-22** Follows the TDD loop where testable: one failing test at a time, real pass, post-green inspection; no all-tests-up-front.
- **EB-23** Records non-blocking unrelated work in `PLAN.md` → Discovered work instead of silently absorbing it.
- **EB-24** Fixes a bug now when it blocks/invalidates the current slice, and counts its time in the slice's actual.
- **EB-25** Records a new requirement in `SPEC.md` and asks (or blocks) when material, instead of implementing it silently.
- **EB-26** At the block's stop condition, stops and re-plans (or explicitly allocates a new block); does not silently continue.
- **EB-27** Stubs dependencies/prerequisites where useful but never fakes the behavior under test (no literal returns, test-only branches, weakened assertions, pasted actuals).
- **EB-28** Marks a slice `done` only after running verification for every `Done when` item.
- **EB-29** Records actual time honestly (or "not tracked"), including in-slice bug fixes and interruptions.
- **EB-36** Reads calibration via `calibration.py summary --estimator <id>` before estimating; at slice `done` with a raw estimate and measured actual, appends exactly one record via `calibration.py append`; never appends spikes, unfinished or untracked slices; never edits the log by hand.
- **EB-55** Before changing implementation, inspects the slice's existing test framework, nearby tests, relevant scripts and CI checks, and testing conventions; records the chosen test path in `PLAN.md` → `Implementation notes`. For new testable behavior with a suitable path, observes a failing test in that setup before changing production code.
- **EB-56** If no suitable test path exists, records that gap and defines proportionate verification before changing implementation. Does not silently add a test framework or ask about a routine verification choice; runs the chosen verification before marking the slice done.

## State and resumability

- **EB-30** On resume, reads `STATUS.md` and the stage's artifacts before acting, and continues the recorded `Next` rather than restarting the stage.
- **EB-31** Does not redo completed work unless new evidence invalidates it; if it does, marks the artifact `stale` and says why.
- **EB-32** At every stop, `STATUS.md` has one concrete `Next` executable without conversation history, and `validate_work.py` passes.
- **EB-33** `STATUS.md` contains no research, decisions or slice definitions.
- **EB-34** Respects project instructions and conventions (existing doc locations, test commands) over skill defaults; does not edit `AGENTS.md`/`CLAUDE.md`.
- **EB-35** Does not stop merely after a substep; stops at stage boundary, blocking question, scope boundary, or block boundary.

## Re-entry and adoption (`dd:state`, and every skill on entry)

- **EB-37** Adopts started work by backfilling the task files from evidence (ticket, branch, diff, tests, commits); does not start an empty-`SPEC.md` requirements workflow or replay completed stages.
- **EB-38** Keeps reconstructed inference apart from confirmed history: inferred decisions, intent and acceptance criteria are labeled Inferred/Assumed/Open with evidence; no fabricated decisions, rationale, estimates, original intent or completed slices; unknown history is stated as unknown.
- **EB-39** Treats `STATUS.md` as a cached cursor: checks the claims the next action depends on against the artifacts and the repository; when it is stale, updates `STATUS.md` (and `PLAN.md` slice state) to reality, says so, and does not repeat the completed step.
- **EB-40** Reconstructs state from the files and repository without asking the user to recap anything the files or repository already show.
- **EB-41** Routes backward only as far as a material gap requires, and explains the route in task terms rather than workflow-mechanics terms.
- **EB-42** "What next?" yields one concrete action executable by a fresh agent; the plan is not dumped unless requested; the state summary is short and verified, not an echo of `STATUS.md`.
- **EB-43** At a checkpoint, substantive findings land in their authoritative file (not `STATUS.md`); the current slice in `PLAN.md` reflects actual progress (boxes checked only for verified items, remaining test list recorded); `STATUS.md` stays compact with one exact `Next`.
- **EB-44** On entry or resume, detects relevant `review-needed` artifacts, reconciles the specific claims the next stage depends on from evidence, and clears them to `complete` when sufficiently verified. If material uncertainty remains, asks the specific question or routes to grounding/shaping before dependent work. Does not require unrelated sections to receive a full-document review.
- **EB-45** Routes generic re-entry or state language, including "continue where I left off," to `dd:state`; routes explicit implementation language, including "continue coding S2," to `dd:execute`. Direct `dd:execute` invocation still reconstructs task state.
- **EB-46** With no relevant workspace and no explicit adoption request (including a bare `dd:state` invocation), inspects the repository, summarizes the inferred task with its evidence, and asks whether to adopt it. Creates nothing (no `.work/`, no `init_work.py` run) before the user agrees.
- **EB-47** An explicit request to adopt, initialize or port a task counts as consent: inspects, then backfills without asking a second confirmation. The task identifier comes from the user, then the branch name, then task docs, then a stable purpose slug; never an invented ticket number.
- **EB-48** When a relevant workspace exists, a bare invocation reconciles it and reports the stage, current slice and one `Next`. It does not ask whether to initialize, and does not create a second workspace.

## Orientation (`dd:help`)

- **EB-49** Routes command and workflow questions ("which dd command should I use?", "how does this work?") to `dd:help`, which explains the five commands and the normal flow concisely, names the command that fits, lists only the task-doc root to state whether task workspaces exist and tailor that command, opens no task files, writes nothing in the repository, and does not start grounding, shaping or execution.
- **EB-50** Routes a question about a specific task's next step ("what should I do next on PHS-1234?") to `dd:state`, not `dd:help`.

## Asking the user

- **EB-51** When a user choice or confirmation is required (adopting a task, picking among plausible tasks, a material requirement interpretation, a design trade-off that is the user's, a missing task identifier), asks through the environment's interactive question tool with short, mutually exclusive options, not as a question in prose.
- **EB-52** Where no interactive question tool is available, asks the same thing as one concise inline question and does not fail or stall.
- **EB-53** Does not ask during routine implementation or design judgment that evidence, requirements or conventions settle; asks only for a material choice that blocks the work or changes scope or observable behavior.
- **EB-54** When `dd:ground`, `dd:shape` or `dd:execute` finds started work with no workspace, it hands off to `dd:state` rather than adopting or creating `.work/` itself. `dd:state` applies its consent rule (asks unless adoption was explicitly requested), backfills, and routes back to the requested stage, or to an earlier one a material gap requires.
