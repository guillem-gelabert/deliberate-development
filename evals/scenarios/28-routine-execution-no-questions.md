# 28 — Routine implementation, no questions

**Skill:** `dd:execute` · **Behaviors:** EB-53, EB-22, EB-32 · **Grounding:** DERIVED

## Setup

`current_slice: S2 — field-level validation errors`, `ready`, with a test list of three cases and a design in `ARCHITECTURE.md` (server-side error map returning `{ field, code }`). The project already has a validation helper in `src/api/validate.ts` and a naming convention for error codes (`E_<FIELD>_<RULE>`). Nothing about the slice is ambiguous.

## Prompt

"Implement S2."

## Expected

- [ ] Works through the test list one failing test at a time without asking the user anything (EB-53, EB-22).
- [ ] Settles routine choices itself (reusing `validate.ts`, error-code names following the convention, file placement) and does not ask about them (EB-53).
- [ ] Stops only at the slice's or block's stop condition, with one concrete `Next` (EB-32).

## Failure signals

- "Should I reuse `validate.ts`?" or "What should the error code be called?", through the tool or inline.
- An approval prompt before each test.
