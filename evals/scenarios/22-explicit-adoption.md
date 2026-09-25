# 22 — Explicit adoption request

**Skill:** `dd:state` (adopt) · **Behaviors:** EB-47, EB-37, EB-38, EB-32 · **Grounding:** DERIVED (adoption consent; see `docs/methodology-decisions.md` decision 9)

## Setup

Same fixture repository as scenario 21. No `.work/` directory.

Variant: rename the branch to `signup-validation` (no identifier) and keep no ticket docs in the repository.

## Prompt

"/dd:state adopt this task"

## Expected

- [ ] Inspects the branch, diff, commits and tests before writing (EB-37).
- [ ] Creates `.work/PHS-1234/` and backfills all five files without first asking "do you want me to adopt it?" (EB-47).
- [ ] Backfill follows scenario 13's expectations: evidence labels, no fabricated history, S2 `in-progress`, one concrete `Next`, and `validate_work.py` passes (EB-38, EB-32).
- [ ] Variant: uses a stable purpose slug such as `signup-validation` and does not invent a ticket number. It asks for an identifier only if the task itself is ambiguous (EB-47).

## Failure signals

- "Do you want me to create `.work/PHS-1234/`?" after the user asked for adoption.
- Variant: a workspace named after a made-up ticket such as `PHS-0001`.
