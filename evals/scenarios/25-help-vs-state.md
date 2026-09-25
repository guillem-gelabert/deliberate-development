# 25 — Task next step goes to dd:state, not dd:help

**Skill:** `dd:state` (next) · **Behaviors:** EB-50, EB-42, EB-39 · **Grounding:** DERIVED (skill routing)

## Setup

Scenario 17's fixture, with the workspace at `.work/PHS-1234/`: S3 is `in-progress` with "rates sorted by price" as its next unchecked test, and later slices are `candidate`/`ready`. The files agree with the repository.

## Prompt

"What should I do next on PHS-1234?"

## Expected

- [ ] Selects `dd:state`, not `dd:help` (EB-50).
- [ ] Reconciles the cursor against the files and repository and gives one concrete next action for PHS-1234: write the failing "rates sorted by price" test for S3 (EB-39, EB-42).

## Failure signals

- Replies with the generic command cheat sheet.
- "Run `dd:state` to find out" without doing it.
