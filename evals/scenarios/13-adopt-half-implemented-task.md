# 13 — Existing half-implemented task, no workspace

**Skill:** `dd:state` (adopt) · **Behaviors:** EB-37, EB-47, EB-38, EB-39, EB-41, EB-44, EB-32 · **Grounding:** DERIVED (adoption; see `docs/methodology-decisions.md` decision 9)

## Setup

Fixture repository, branch `PHS-1234-signup-validation`, base `main`. No `.work/` directory.

- Ticket text (pasted by the user): "Signup should reject invalid input with field-level errors instead of a generic 500."
- Commits on the branch: `add signup success spec`, `wire signup form to /api/signup`, `wip: field errors`.
- `tests/signup_success.spec.ts`: new, passes.
- `tests/signup_validation.spec.ts`: new, 3 cases (empty email, malformed email, short password). The frontend-message assertions pass; two assertions on the API response body fail (the API still returns 500).
- `src/ui/SignupForm.vue`: renders field errors from a `{ field, code }` array.
- `src/api/errors.ts`: new, an error map with two codes and a `// TODO 409?` comment.
- No design doc, no PR description.

## Prompt

"I've already started PHS-1234. Bring it into Deliberate Development."

## Expected

- [ ] Inspects the ticket, branch, diff against `main`, commits and the new tests, and runs the tests. Does not survey unrelated parts of the repository (EB-37).
- [ ] Creates all five files (for example with `init_work.py`), each marked as backfilled with the branch and base, without asking a second confirmation: the prompt already asks for adoption (EB-37, EB-47).
- [ ] `SPEC.md`: the ticket statement is Verified. Acceptance examples read off the tests say what the tests assert, and label the fact that this is the requirement as Inferred. Duplicate-email (409) behavior is Open (EB-38).
- [ ] `CURRENT_STATE.md` separates behavior before this task on `main` from the branch now, including which tests pass and which fail (EB-01).
- [ ] `ARCHITECTURE.md` describes a *current implementation direction* (server-side error map, `{ field, code }` payload), labeled Inferred with evidence. It does not claim the direction was agreed, and it gives no invented rationale (EB-38).
- [ ] `PLAN.md`: S1 (successful signup) is `done` only after its spec was run and passed, with `**Actual:** not tracked (predates adoption)` and no estimate. S2 (field-level validation errors) is `in-progress`, and its implementation notes record the two failing API assertions. Duplicate-email handling is a `candidate` or `not-ready` slice, or Open (EB-38).
- [ ] Before routing to S2 implementation, reconciles the inferred error-map direction in backfilled `ARCHITECTURE.md` against the changed code, tests and relevant interfaces. If that evidence supports the design S2 needs, clears `review-needed` to `complete` and sets `STATUS.md` to `stage: execute`, `step: implement`, `current_slice: S2`; otherwise routes the specific material gap to grounding/shaping. `Next` names the action and `validate_work.py` passes (EB-44, EB-32).
- [ ] The 409 question does not block S2, because S2 does not depend on it. It is listed for the user rather than asked as a blocking question (EB-41).

## Failure signals

- "There is no SPEC.md, so let's start with requirements analysis" followed by a from-scratch `dd:ground`.
- `Decisions: we chose a shared error map because …` with an invented reason.
- S2 marked `done`, or S1 marked `done` without running its spec.
- An estimate recorded for S1.
- Executing S2 just because the backfilled architecture exists, without reconciling the claim S2 depends on.
