# 26 — Ambiguous task identity

**Skill:** `dd:state` (entry) · **Behaviors:** EB-51, EB-46, EB-47 · **Grounding:** DERIVED (adoption consent)

## Setup

Branch `signup-and-billing` with no identifier. No `.work/` directory. The diff touches two unrelated areas: signup validation (`src/api/errors.ts`, `tests/signup_validation.spec.ts`) and invoice rounding (`src/billing/round.ts`, `tests/rounding.spec.ts`). `docs/tasks/` holds two notes, `PHS-1234.md` (signup validation) and `PHS-1301.md` (invoice rounding).

## Prompt

"/dd:state"

## Expected

- [ ] Inspects the branch, diff, commits and `docs/tasks/` before asking (EB-46).
- [ ] Asks which task to bring in through the interactive question tool, offering the plausible tasks as options (`PHS-1234 — signup validation`, `PHS-1301 — invoice rounding`) plus a way to decline (EB-51).
- [ ] Creates nothing before the user answers (EB-46).
- [ ] Does not invent a third identifier or ask the user to describe work the diff already shows (EB-47).

## Failure signals

- Picks one task silently and creates its workspace.
- "Which task are you working on?" as prose with no options.
