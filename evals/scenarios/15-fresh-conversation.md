# 15 — Fresh conversation, workspace exists

**Skill:** `dd:state` (resume) · **Behaviors:** EB-40, EB-30, EB-39, EB-42 · **Grounding:** DERIVED (task-state contract: conversation history is secondary)

## Setup

Workspace `.work/ORD-12/` from earlier sessions, possibly produced by a different model. `STATUS.md` says `stage: shape`, `step: slice-readiness`, and `Next` is "Run the readiness check on S2 (partial refunds) against ARCHITECTURE.md → Refund flow and mark it ready or not-ready in PLAN.md." S1 is `ready`. S2 and S3 are `candidate`. The files agree with each other and with the repository, which has no changes since `updated`. The conversation has no history.

## Prompt

"Where did I leave off on ORD-12? Continue."

## Expected

- [ ] Gives a short state summary built from the files (stage, what is ready, what is being checked) without asking the user what happened before (EB-40, EB-42).
- [ ] Confirms the cursor is current (the repository has no changes after `updated`) instead of simply trusting it (EB-39).
- [ ] Continues with the recorded `Next` under `dd:shape` rules. It does not re-derive `SPEC.md` or rewrite the architecture (EB-30, EB-31).
- [ ] Stops at `dd:shape`'s own stop conditions with one concrete `Next` (EB-32).

## Failure signals

- "Can you remind me what we decided about refunds?"
- Starts `dd:ground` because "this is a new conversation".
