# 06 — Session interrupted halfway through dd:shape

**Skill:** `dd:shape` (fresh conversation, possibly a different model) · **Behaviors:** EB-30, EB-31, EB-32, EB-33 · **Grounding:** DERIVED (task-state contract)

## Setup

Fixture workspace `.work/CMT-7/`:

`STATUS.md`
```markdown
---
stage: shape
step: architecture-risk
status: in-progress
current_slice:
updated: 2026-09-24
---

# Status

## Artifact state

- SPEC.md: complete
- CURRENT_STATE.md: complete
- ARCHITECTURE.md: draft
- PLAN.md: not-started

## Open

- Does the ORM's soft-delete scope apply to comment counts? Affects whether counts need a separate query.

## Next

Check whether `Comment.default_scope` in app/models/comment.rb excludes soft-deleted rows from `comments_count`, then record the counting decision in ARCHITECTURE.md → Decisions.
```

`ARCHITECTURE.md` has Goal, Proposed design, Components affected filled in; Decisions has one entry; Risks lists the counting question.

## Prompt

New conversation: "Continue CMT-7."

## Expected

- [ ] Reads `STATUS.md` and the artifacts before acting; states where it is resuming (EB-30).
- [ ] Performs the recorded `Next` (inspects `comment.rb` / counter cache) first; does not rewrite Goal/Proposed design or re-run grounding (EB-31).
- [ ] Records the counting decision in `ARCHITECTURE.md` → Decisions, then proceeds to slicing in the same session if nothing blocks (EB-35).
- [ ] `STATUS.md` stays a cursor: no research copied into it (EB-33); `validate_work.py` passes at the end (EB-32).

## Failure signals

- "Let's start by understanding the requirements" and re-derives `SPEC.md`.
- Asks the user what was decided previously.
