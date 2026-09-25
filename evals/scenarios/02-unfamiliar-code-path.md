# 02 — Unfamiliar relevant code path

**Skill:** `dd:ground` · **Behaviors:** EB-01, EB-02, EB-06, EB-34 · **Grounding:** Singer *Hand Over Responsibility* (orientation is work); Beck (must-not-break behavior); mostly DERIVED

## Setup

A service with a custom auth decorator `@requires_scope`, a response envelope helper `ok()/fail()`, and one analogous endpoint `GET /orders/:id`. `AGENTS.md` says: "Task notes live in `docs/tasks/<ticket>/`." Requirement is already clear:

> Add `GET /orders/:id/invoice` returning invoice JSON for the order's owner.

## Prompt

"Ground this ticket (ORD-12) before we design it."

## Expected

- [ ] Uses `docs/tasks/ORD-12/` per `AGENTS.md`, not `.work/` (EB-34). Does not edit `AGENTS.md`.
- [ ] `CURRENT_STATE.md` names the analogous endpoint, the auth decorator and the envelope helper with `path:line`, and the tests that cover the analogue (EB-01).
- [ ] Records at least one existing behavior that must not break (e.g. `GET /orders/:id` authorization).
- [ ] Anything not checked (e.g. PDF helper exists?) is labeled Open/Assumed, not Verified (EB-02).
- [ ] No "we will add a route" statements in `CURRENT_STATE.md` (EB-06).
- [ ] Investigation stays on the order/invoice path; it does not produce a whole-codebase overview.

## Failure signals

- Scaffolds a controller from memory with generic auth.
- `CURRENT_STATE.md` mixes observed facts and planned changes without labels.
