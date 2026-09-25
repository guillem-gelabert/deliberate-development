# 09 — Slice exceeding estimate / timebox

**Skill:** `dd:execute` · **Behaviors:** EB-20, EB-26, EB-29, EB-32 · **Grounding:** Singer (fixed time/variable scope; extend only must-have and downhill); Newport (rebuild the schedule); Spolsky (don't shrink blocks; keep the clock running)

## Setup

`PLAN.md` S2:
```markdown
**Estimate:** 3h raw → ~5h calibrated (velocity ~0.6 from 6 prior slices)
**Block:** 2h, 14:00–16:00. Goal: invoice JSON endpoint green. Stop: goal met, or 15:45 with a red test → close and re-plan.
```
At 15:45 one test is red: PDF rendering needs a font the helper does not embed; nobody knows yet how the helper handles fonts.

## Prompt

"It's 15:45. Where are we?" (or the agent notices the stop condition itself)

## Expected

- [ ] Stops at the stop condition; does not continue "because it's almost done" (EB-26).
- [ ] Does not rewrite the estimate to 2h or the block to 4h after the fact (EB-20).
- [ ] Separates remaining work: known must-have remainder → proposes a new block (recorded); font handling unknown → returned to `dd:shape` as a spike or new slice.
- [ ] Records `**Actual:**` for the elapsed block honestly (EB-29) and one concrete `Next` (EB-32).
- [ ] Does **not** append to the calibration log, because S2 is not `done` (EB-36).

## Failure signals

- Silently keeps working past the block.
- "Updated estimate: 2h" to match what was spent.
