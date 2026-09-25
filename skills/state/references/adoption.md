# Adopting started work

Read when a task already has implementation, tests or design work but no workspace, or only a partial one. Everything here is **[DERIVED]**. The research corpus does not discuss bringing work that is already under way into a workflow.

The aim is a reliable state from now on. It is not a complete history. Backfill only as much requirement and current-state knowledge as you need to understand what has been done, find the material gaps, and continue safely.

Use **Verified** for observed or confirmed claims with a re-checkable pointer, **Inferred** for a conservative conclusion from them, **Assumed** for a provisional claim with its invalidation condition, and **Open** for what remains unknown. Code can verify its current behavior without proving why it was written or that its behavior is the agreed requirement.

## Before writing

Adoption writes to the repository, so it needs the user's consent. First inspect the evidence below (branch, `git status`, diff, recent commits, project instructions, task docs, changed tests) and infer which task is in progress. Then:

- **Explicit request** ("adopt this task", "initialize PHS-1234", "port the current task into Deliberate Development"): the request is the consent. Backfill without asking again, unless inspection turns up a new material ambiguity, such as two plausible tasks.
- **Anything else**, including a bare invocation: write nothing. State the inferred task and its evidence, then ask with the interactive question tool, for example: "No Deliberate Development workspace exists for the current task. From the branch and changes it appears to be PHS-1234 (signup validation). Adopt it into `.work/PHS-1234/`?" with the options *Adopt current task* and *Not now*. If the task itself is ambiguous, offer the plausible tasks as the options instead. Without the tool, ask the same question inline in one or two sentences.

If a relevant workspace already exists, this section does not apply: reconcile it instead.

### Task identifier

Use the first that applies: an identifier the user gave; a clear identifier in the branch name; a clear identifier in the relevant task documentation; a short stable slug describing the task's purpose. Never invent a ticket number. If several tasks remain plausible, ask only which one, or only for the missing identifier; do not ask for anything the repository already shows.

## Backfill, do not replay

- Discouraged: "There is no `SPEC.md`, so begin a complete requirements analysis."
- Preferred: "The branch already implements the success path and has failing tests for two validation cases. Record the requirement those tests and the ticket establish, the current state of the branch, the design direction the code shows, and the slices that follow. Then continue with the validation slice."

## Evidence

Read what is available and relevant, roughly from most to least useful:

1. Project instructions, and their conventions for task documents and base branches.
2. The request: the ticket or issue, linked documents, the user's notes, what the user says in this conversation.
3. The branch: its name, `git status` (uncommitted work), the diff against the likely base (the merge-base with the project's default branch; say which base you used), and the commits on the branch.
4. New and changed tests. These are the strongest evidence of intended behavior. Run them and record which pass and which fail.
5. Changed source files and their immediate collaborators.
6. Existing specs, design notes, ADRs, PR descriptions, and connected tracker or domain sources.

Stop reading a thread once more detail would not change the stage, the current slice, or the next action.

## What each file gets

Start with `python3 scripts/init_work.py <task-id>`, or `--fill-missing` for a partial workspace. Then replace the template content. The template `STATUS.md` always describes a fresh task, so rewrite it completely.

Put this line at the top of every file you backfill:

`> Backfilled <date> from existing work on <branch> (base <ref>). Earlier history is reconstructed; labels mark what was observed.`

- **`SPEC.md`**: the problem and desired behavior, from the ticket or the user (**Verified**, with source). Acceptance examples come from the ticket (**Verified**) or are read off tests. For a test, what it asserts is **Verified**, but that the assertion *is the requirement* is **Inferred** unless something confirms it. Behavior nobody has specified is **Open**. If material examples are only Inferred, set the file to `review-needed`.
- **`CURRENT_STATE.md`**: two parts. *Before this task* is the relevant behavior on the base. *On the branch now* covers what is implemented, what tests exist, which pass and which fail, and any uncommitted changes. Each fact gets a pointer.
- **`ARCHITECTURE.md`**: the design the changes embody, under a heading such as `Current implementation direction`, labeled **Inferred** and listing its evidence. Record a decision as agreed only when a person or document confirms it. Where rationale and alternatives are unknown, write that they are unknown; do not invent them. Use `draft` for ordinary unfinished design; use `review-needed` when existing reconstructed design needs reliability checks before a dependent stage can rely on it.
- **`PLAN.md`**: behavioral slices covering what exists and what remains, in the contract format.
  - Mark a slice `done` only if every `Done when` box has been verified by running something now. Otherwise it is `in-progress`, or earlier.
  - Work that finished a layer but no behavior (an endpoint with no caller) is progress inside the slice it serves, not a `done` slice.
  - Adopted slices get no estimate. Record `**Actual:** not tracked (predates adoption)` unless real time records exist.
  - Remaining slices are `candidate` until a readiness check. The in-progress slice keeps its remaining test list or tasks in `Implementation notes`.
- **`STATUS.md`**: the routed `stage`/`step`, `current_slice`, artifact states, `Open`, and one `Next`.

## Inferred history is not confirmed history

- Discouraged: `Decisions: Architecture B (server-side validation with a shared error map) was agreed.`
- Preferred:
  ```markdown
  ## Current implementation direction
  Inferred: validation errors are mapped server-side through a shared error map.
  Evidence: src/api/errors.ts (new on branch), SignupController#create uses it, tests/signup_errors.spec.ts.
  Whether this was agreed, and why, is Open.
  ```
- Discouraged: `S1 — done` because a file named `signup_success.spec.ts` exists.
- Preferred: `S1 — done`, after running the spec and seeing it pass, with each box checked against that run.

## When adoption exposes a gap

Route backward only as far as the gap requires. Everything else carries on.

- The expected behavior for HTTP 409 cannot be established, and S2 needs it → requirement clarification in `dd:ground`. Batch it with any other questions the user must answer.
- The code assumes package X retries automatically, which is unverified and would change the design → current-state investigation in `dd:ground`.
- New evidence contradicts an assumption the design rests on → mark `ARCHITECTURE.md` `stale`, then `dd:shape`.
- Requirements and design are still valid and the slice is simply unfinished → `dd:execute`, continuing the slice.

Before routing to execution, reconcile the specific `review-needed` claims that the current slice needs, following `references/state-reconciliation.md`. Ask the user only what evidence cannot settle and what matters to the current or next slice, for example "Is the retry in `client.ts` intended, or left over?" Leave unrelated uncertainty labeled in its artifact without blocking that slice.
