# 20 — Generic re-entry and explicit implementation triggers

**Skill:** `dd:state` for generic re-entry; `dd:execute` for implementation · **Behaviors:** EB-45, EB-30, EB-39 · **Grounding:** DERIVED skill routing

## Setup

An existing task workspace has S1 done and S2 in progress. `STATUS.md` names an S2 test as the next action. The repository shows that test and a partial implementation already exist. Run each prompt separately in a fresh conversation with the same fixture.

## Prompts

1. "Continue where I left off."
2. "Continue coding S2."

## Expected

- [ ] Prompt 1 selects `dd:state` for generic re-entry, reconciles the cursor, then routes to the appropriate stage (EB-45, EB-39).
- [ ] Prompt 2 selects `dd:execute` for implementation, reconstructs existing task state on entry, and continues S2 from the actual test/code progress (EB-45, EB-30).
- [ ] Neither path repeats S1 or rewrites the existing S2 test (EB-31).

## Failure signals

- Prompt 1 selects `dd:execute` immediately solely because a slice is in progress.
- Prompt 2 treats implementation as a state-summary request only.
