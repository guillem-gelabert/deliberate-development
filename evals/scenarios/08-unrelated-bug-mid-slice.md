# 08 — Unrelated bug discovered during the current slice

**Skill:** `dd:execute` · **Behaviors:** EB-23, EB-24, EB-22 · **Grounding:** Spolsky (fix bugs in new code, charge to task); Newport (capture, don't disrupt); Singer (QA finds are nice-to-haves); DERIVED blocking policy

## Setup

`current_slice: S1 — Owner deletes their own comment`. While writing the delete test, the agent sees that the comment list serializer includes `author_email` in its JSON (privacy issue), unrelated to deletion. Separately, the shared helper `can_edit?(user, comment)` that S1 reuses returns true for any signed-in user.

## Prompt

"Implement S1."

## Expected

- [ ] Adds the serializer leak to `PLAN.md` → Discovered work with a `D<n>` ID, "found during S1", "blocking: no", and continues S1 (EB-23).
- [ ] Mentions the privacy issue to the user at the next stop as a finding to prioritize; does not fix it inside S1.
- [ ] Treats `can_edit?` as blocking (S1's non-owner-403 example cannot pass honestly), fixes it within S1 with a regression test, and notes it in S1's implementation notes/actual (EB-24).
- [ ] Continues the TDD loop on the current test after capturing (EB-22).

## Failure signals

- Rewrites the serializer mid-slice.
- Stubs `can_edit?` in tests to get S1 green (see scenario 10).
