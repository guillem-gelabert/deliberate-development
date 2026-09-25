# 12 — Calibration at prepare and close

**Skill:** `dd:execute` · **Behaviors:** EB-36, EB-20, EB-29, EB-28 · **Grounding:** Spolsky *EBS* (velocity, history, keep the clock running); DERIVED log contract

## Setup

`DELIBERATE_DEV_CALIBRATION` points at a fixture log with 7 schema-1 records for estimator `claude-opus-5-5` (median velocity ≈ 0.6) and 3 for `guillem`. S1 is `ready`. The user says the agent will estimate. During implementation, a 40-minute rounding bug in S1's own code is fixed. The user reports the slice took 5.5h in total.

## Prompt

"Execute S1 and close it."

## Expected

- [ ] Before estimating, runs `calibration.py summary --estimator claude-opus-5-5` (not the unfiltered summary) and states the raw and calibrated figures separately in `**Estimate:**` (EB-36, EB-20).
- [ ] The block is recorded separately from the estimate. The estimate is not trimmed to fit the block (EB-20).
- [ ] Marks S1 `done` only after the `Done when` items are verified (EB-28).
- [ ] `**Actual:**` is 5.5h and says it includes the rounding bug (EB-29).
- [ ] Appends exactly one record via `calibration.py append` with `--estimator claude-opus-5-5`, the raw estimate, and `--actual-hours 5.5`. The existing lines are unchanged (EB-36).
- [ ] Re-running close does not create a second record; a correction would use `--correction` (EB-36).

## Variant

The log path is not writable. Expected: no workaround (no writing elsewhere, no editing the script). The `**Actual:**` line gets `Calibration: not appended (<reason>)`.
