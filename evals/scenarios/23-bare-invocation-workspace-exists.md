# 23 — Bare invocation, workspace exists

**Skill:** `dd:state` (state) · **Behaviors:** EB-48, EB-39, EB-44, EB-42 · **Grounding:** DERIVED (task-state contract: `STATUS.md` is a cached cursor)

## Setup

Branch `PHS-1234-signup-validation` with a valid workspace `.work/PHS-1234/`. `PLAN.md` has S1 `done` and S2 `in-progress`. `STATUS.md` says `stage: execute`, `step: implement`, `current_slice: S2`, and its `Next` is "Make the malformed-email API assertion pass." Since `updated`, a commit has made that assertion pass, so the cursor is stale. `ARCHITECTURE.md` is `review-needed`.

## Prompt

"/dd:state"

## Expected

- [ ] Does not ask whether to initialize or adopt anything, and does not create a second workspace or run `init_work.py` (EB-48).
- [ ] Runs the S2 tests, sees the malformed-email assertion now passes, and corrects `PLAN.md` and `STATUS.md` to the observed state, saying what changed (EB-39).
- [ ] Notices `ARCHITECTURE.md` is `review-needed` and reconciles only the claims S2 needs next (EB-44).
- [ ] Reports the stage, the current slice and one concrete `Next` (EB-48, EB-42).

## Failure signals

- "I don't see a workspace; should I create one?"
- A new `.work/signup-validation/` beside `.work/PHS-1234/`.
- Repeats the `Next` from the stale cursor.
