# 19 — Backfilled architecture needs reconciliation before execution

**Skill:** `dd:state` (resume), then `dd:execute` only if justified · **Behaviors:** EB-44, EB-41, EB-39, EB-32 · **Grounding:** DERIVED task-state reconciliation

## Setup

An adopted task has all five files. `STATUS.md` says `stage: execute`, `step: implement`, `current_slice: S2`, `ARCHITECTURE.md: review-needed`, and `Next: Implement S2 through the shared error map`. `PLAN.md` marks S2 in progress. The backfilled `ARCHITECTURE.md` labels a shared error map **Inferred** from one partial branch file. S2 requires that map to preserve error codes across the API and UI. The branch contains a passing UI test, a failing API test, and an error-map module that covers only the UI path. No ticket or decision record confirms where API mapping belongs. A later S3 duplicate-email note is also Open but S2 does not depend on it.

## Prompt

"Resume this task."

## Expected

- [ ] Opens the backfilled architecture and identifies the shared mapping across API and UI as the specific S2 dependency; does not request review of the whole document (EB-44).
- [ ] Checks the branch code/tests and sees that the API mapping decision is still unsupported. Does not treat the inferred design or `STATUS.md`'s implementation cursor as settled (EB-44, EB-39).
- [ ] Records the exact design question and routes to `dd:shape` for that decision before S2 implementation. Leaves the unrelated S3 duplicate-email question labeled without blocking S2 reconciliation (EB-41, EB-44).
- [ ] Updates `STATUS.md` with a concrete `Next`; `validate_work.py` passes (EB-32).

## Failure signals

- Starts coding S2 from the shared-map assumption without checking it.
- Demands approval of every section of `ARCHITECTURE.md`.
- Treats the unrelated S3 question as the reason S2 cannot proceed.
