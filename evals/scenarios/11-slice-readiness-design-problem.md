# 11 — Slice readiness check exposes a design-level problem

**Skill:** `dd:shape` · **Behaviors:** EB-16, EB-14, EB-10 · **Grounding:** Wake *INVEST*/*Independent Stories*; Singer *Show Progress*; DERIVED loop

## Setup

Workspace at `stage: shape`, `step: slicing`. `ARCHITECTURE.md` (`draft`) decides: "Comment deletion is a soft delete; the thread view filters `deleted_at IS NULL`." `PLAN.md` has `S1 — Owner deletes their own comment and it disappears for everyone` (`candidate`). `CURRENT_STATE.md` records: "Verified: thread view is served from a denormalized `thread_cache` table rebuilt nightly (jobs/rebuild_thread_cache.rb:12)."

## Prompt

"Finish slicing and hand off."

## Expected

- [ ] Runs the readiness check on S1 and finds that "disappears for everyone" cannot hold with a nightly cache, so the check fails *architecture-consistent* (EB-16).
- [ ] Treats this as design-level: sets `ARCHITECTURE.md` to `draft`, records the cache conflict under Risks / Open technical questions, sets `step: architecture`, and revises the design (e.g. invalidate the cache entry on delete) before re-checking S1 (EB-16).
- [ ] Does not mark S1 `ready` with "handle cache" in its implementation notes, and does not hand off (EB-14).
- [ ] After the design change, S1 is re-checked and marked `ready` with `Done when`. Slices remain behavioral (EB-10).

## Failure signals

- `S1 ready` plus `S2 — Cache invalidation` as a technical slice.
- Handoff with the conflict unrecorded.
