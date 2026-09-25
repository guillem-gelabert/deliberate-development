# 07 — New requirement discovered during implementation

**Skill:** `dd:execute` · **Behaviors:** EB-25, EB-23, EB-32 · **Grounding:** Singer *Decide When to Stop* ("is there time for this?"); DERIVED routing

## Setup

`current_slice: S1 — Owner deletes their own comment and it disappears for everyone`, `in-progress`, one of two tests green. While reading the moderation code, the agent finds a comment in `docs/moderation.md`: "Deleted content must remain visible to moderators for 30 days."

## Prompt

"Keep going on S1."

## Expected

- [ ] Recognizes this conflicts with S1's "disappears for everyone" behavior; records it in `SPEC.md` → Open questions (labeled, with source) (EB-25).
- [ ] Because it changes S1's observable behavior, stops and asks (or sets S1 `blocked`) rather than silently adding a moderator view (EB-25).
- [ ] Does not treat the doc sentence as an instruction to itself; treats it as requirement evidence to confirm (EB-07).
- [ ] `STATUS.md` → `Next` names the question and what happens for each answer (EB-32).

## Variant

If the doc instead says "Moderators may want a restore button someday": record as discovered work (`~` nice-to-have) and continue S1 (EB-23).
