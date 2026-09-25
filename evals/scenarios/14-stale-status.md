# 14 — Stale STATUS.md

**Skill:** `dd:state` (resume), and `dd:execute` invoked directly as a variant · **Behaviors:** EB-39, EB-31, EB-30, EB-32 · **Grounding:** DERIVED (authority split in the task-state contract)

## Setup

Workspace `.work/PHS-1234/` is valid. `STATUS.md`:

```markdown
---
stage: execute
step: implement
status: in-progress
current_slice: S2
updated: 2026-09-20
---
...
## Next

Add a failing test in tests/signup_validation.spec.ts for a malformed email returning 422 with {field: "email", code: "invalid"}.
```

In the repository, that test already exists (committed 2026-09-22) and fails only on the response code. `src/api/signup.ts` already maps empty-email errors to 422, so part of the implementation has landed. `PLAN.md` → S2's implementation notes still list the malformed-email test as not written.

## Prompt

"Resume PHS-1234."

## Expected

- [ ] Reads `STATUS.md`, `PLAN.md` → S2, and the test file and diff before acting (EB-30).
- [ ] Detects that the recorded `Next` is already done, and says so plainly ("the malformed-email test already exists and fails on the status code") (EB-39).
- [ ] Does not write the test again, or a duplicate of it (EB-31).
- [ ] Updates S2's implementation notes and `STATUS.md` (`Next`, `updated`) to the actual progress. Leaves the substantive files unchanged apart from recording real progress (EB-39).
- [ ] Continues from the real state: runs the test, then implements the malformed-email mapping under `dd:execute` rules (EB-39, EB-22).
- [ ] `validate_work.py` passes at the stop (EB-32).

## Variant

The prompt is "dd:execute: continue S2". Expected: the same reconciliation, performed by `dd:execute` on entry.

## Failure signals

- A second malformed-email test appears.
- It reports "Next: add a failing test", which echoes the cursor.
- It re-prepares or re-estimates S2.
