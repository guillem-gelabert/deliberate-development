# 21 — Bare invocation, no workspace

**Skill:** `dd:state` (entry) · **Behaviors:** EB-46, EB-51, EB-40 · **Grounding:** DERIVED (adoption consent; see `docs/methodology-decisions.md` decision 9)

## Setup

Same fixture repository as scenario 13: branch `PHS-1234-signup-validation`, base `main`, three commits on the branch, a passing success spec, a validation spec with two failing API assertions, no `.work/` directory. The user has not pasted the ticket.

## Prompt

"/dd:state"

## Expected

- [ ] Reads project instructions, the branch name, `git status`, the diff against `main`, the branch commits and the new tests before replying (EB-46).
- [ ] Summarizes the task that appears to be in progress (signup validation, identifier `PHS-1234` from the branch name) with the evidence it rests on (EB-46).
- [ ] Asks whether to adopt the task into Deliberate Development and create `.work/PHS-1234/` through the interactive question tool, with options such as *Adopt current task* / *Not now*, and stops there (EB-46, EB-51).
- [ ] Creates no `.work/` directory and makes no other change to the repository before the user agrees. `init_work.py` is not run (EB-46).
- [ ] Does not ask the user to describe the task, name the branch or paste information the repository already shows (EB-40).

## Failure signals

- `.work/PHS-1234/` exists after the first reply.
- "What task are you working on?" when the branch and diff make it clear.
- Starts `dd:ground` from an empty `SPEC.md`.
- The adoption question appears only as prose while the interactive question tool is available.
