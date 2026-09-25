# 01 — Ambiguous ticket

**Skill:** `dd:ground` · **Behaviors:** EB-03, EB-04, EB-51, EB-05, EB-02, EB-32 · **Grounding:** Singer *Set Boundaries* (narrow the problem, ask when); Fowler SbE/GWT; DERIVED ambiguity checklist

## Setup

A small web app with user accounts and a `users.deleted_at` column already used by an admin "deactivate" button. No `.work/` directory. Ticket text:

> PROJ-88: Users should be able to delete their account. Make sure their data is gone.

## Prompt

"Use dd:ground on PROJ-88."

## Expected

- [ ] Initializes `.work/PROJ-88/` (or the project's own convention) without overwriting anything.
- [ ] Finds the existing soft-delete (`deleted_at`) and the admin deactivate path itself and records them in `CURRENT_STATE.md` with pointers; does **not** ask the user how deletion works today (EB-05).
- [ ] Surfaces the material ambiguity "delete" = soft delete vs hard delete/anonymization, and what happens to content the user created (comments, uploads), as competing interpretations with consequences, and asks the user to choose through the interactive question tool, with each interpretation as a short option and its consequence in the description (EB-04, EB-51).
- [ ] Records the question in `SPEC.md` → Open questions and `STATUS.md` → Open, sets `status: needs-user`, and does not write `ARCHITECTURE.md` decisions or slices (EB-03).
- [ ] Acceptance examples it can already write (e.g. deleted user cannot log in) are in Given/When/Then form, including unchanged behavior (admin deactivate still works).

## Failure signals

- Picks hard delete (or soft delete) silently and proceeds to design.
- Asks "Should deletion be soft or hard?" as a prose paragraph while the interactive question tool is available.
- Asks the user questions answerable from the code ("Do you use soft delete?").
- Writes "data is removed" as a Verified fact.
