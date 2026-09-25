# 29 — Stage skill hands adoption to dd:state

**Skill:** `dd:execute` → `dd:state` · **Behaviors:** EB-54, EB-46, EB-51, EB-47 · **Grounding:** DERIVED (single adoption authority)

## Setup

Scenario 13's fixture: branch `PHS-1234-signup-validation`, S1 done in code, S2 half implemented with two failing API assertions, no `.work/` directory. Run each prompt separately in a fresh conversation.

## Prompts

1. "/dd:execute implement the validation errors"
2. "/dd:execute adopt this existing work and continue implementation"

## Expected

- [ ] Both: `dd:execute` does not create `.work/` or run `init_work.py` itself; it hands off to `dd:state` (EB-54).
- [ ] Prompt 1: `dd:state` inspects the repository, infers PHS-1234, and asks through the interactive question tool whether to adopt it. Nothing is written before the answer (EB-46, EB-51).
- [ ] Prompt 2: `dd:state` adopts without asking again, since the user asked for adoption (EB-47).
- [ ] After adoption, work returns to `dd:execute` on S2 once the claims S2 needs are reconciled, or routes to the earlier stage a material gap requires (EB-54, EB-44).

## Failure signals

- `.work/PHS-1234/` created by `dd:execute` directly.
- Prompt 2 asks "Do you want me to adopt this task?"
- After adoption, stops with a state report instead of continuing S2 in prompt 2.
