# Estimate and block

Read when preparing a slice. Tags: **[DIRECT: author]**, **[INFERRED: author]**, **[DERIVED]**.

## Three different things

| | What it is | Starts from | Changes when |
|---|---|---|---|
| **Estimate** | A prediction of the effort the designed work will take | the concrete task list | the design or understanding changes, never to fit a budget |
| **Block** (timebox / appetite at hour scale) | A decision about how much time to spend now | what the work is worth now | you decide explicitly, and record it |
| **Deadline** | An external commitment | the requester | the requester changes it (it lives in `SPEC.md`) |

An estimate starts from a design and ends with a number. An appetite starts from a number and shapes the design. Do not substitute one for the other. [DIRECT: Singer, *Set Boundaries*] Applying appetite at hour scale is an adaptation. Shape Up defines only 1–2 and 6-week batches. [DERIVED]

## Estimating [DIRECT: Spolsky, *Evidence Based Scheduling*, unless tagged]

- Break the slice into concrete tasks of 16 hours or less, measured in hours ("write X", "add Y to Z"). A task you cannot name concretely has not been designed yet.
- The one doing the work estimates. The number is not negotiated down.
- Calibrate with history: velocity = estimate ÷ actual. Most estimators are consistently optimistic, and that is correctable. Discard data older than about six months. With little or no history (fewer than about six records), assume the worst.
- Where history comes from: the persistent calibration log (see below). If it has no records for this estimator, give the raw estimate with a pessimistic range and say there is no history. [DERIVED]
- An estimate is meaningful only at the top of the hill, where the steps are known. Two "4h" estimates mean different things when one task is familiar and the other is new. [DIRECT: Singer, *Show Progress*] Mark novel tasks as such.
- Monte Carlo ship-date simulation is a project-scale tool. For a single slice, only the calibration core applies. [INFERRED: Spolsky]

Refuse to produce a number, and return to `dd:shape`, when a task cannot be named concretely, when any task exceeds 16h, or when the approach is still unvalidated. [DIRECT gate: Spolsky; INFERRED: Singer]

## Calibration log [DERIVED]

A persistent, append-only estimate-vs-actual history shared across projects: `~/.deliberate-development/calibration.jsonl`, or `$DELIBERATE_DEV_CALIBRATION` if set. One JSON object per line, schema 1:

| Field | Meaning |
|---|---|
| `schema` | `1` |
| `recorded_at` | UTC timestamp (set by the script) |
| `project`, `task_id`, `slice_id` | where the slice lives (project = repository name) |
| `estimator` | who produced the estimate: the person, or the model id if the agent estimated |
| `estimate_hours` | the raw estimate recorded at prepare |
| `calibrated_hours` | the calibrated figure, or `null` |
| `actual_hours` | measured elapsed time, including in-slice bug fixes and interruptions |
| `velocity` | `estimate_hours / actual_hours` (computed by the script) |
| `novel` | the slice involved work new to the estimator |
| `includes`, `note` | free text or `null` |
| `corrects` | `true` if this record supersedes an earlier one for the same slice |

Use `scripts/calibration.py` for both reading and writing. Do not edit the file by hand.

- **Prepare:** `python3 scripts/calibration.py summary --estimator <id>` reports velocity statistics from the last 6 months and flags insufficient history. You decide how to apply them. The script does not estimate.
- **Close:** when a slice becomes `done` and both the raw estimate and a measured actual exist, append exactly one record: `python3 scripts/calibration.py append --project ... --task ... --slice ... --estimator ... --estimate-hours ... --actual-hours ... [--calibrated-hours ...] [--novel] [--includes ...]`.
- Do not append spikes (their number is a timebox, not an estimate), abandoned or dropped slices, or slices whose actual was not tracked.
- The file is append-only. A duplicate for the same slice is refused. To fix a wrong record, append with `--correction`; the summary then uses the latest record.
- If the log cannot be written (sandbox, read-only home, or project instructions that forbid writes outside the repository), do not work around it. Add `Calibration: not appended (<reason>)` to the slice's `**Actual:**` line.

## Allocating the block

- Give the block specific work. [DIRECT: Newport, time blocking]
- State a **goal** and a **stop condition** for the block, and record them on the slice's `**Block:**` line. [DERIVED: Newport gives no stop condition; this combines Singer's appetite, Wake's time-boxed tasks and Beck's empty test list]
- If the estimate exceeds what the work is worth now, cut scope (move behavior to a later slice) or consciously allocate more. Never pretend the work will take less. [DIRECT: Spolsky, "bigger box or remove blocks"; Singer, fixed time / variable scope]
- When knocked off the plan, rebuild the rest of the schedule. [DIRECT: Newport] Rebuilding the schedule does not stretch the current block. [DERIVED, reconciling Newport and Singer]
- Extend only when the remaining work is must-have *and* downhill. Uphill work at the boundary means re-shaping, not extending. [DIRECT: Singer, *Decide When to Stop*]

## Examples [DERIVED]

Preferred:
```markdown
**Estimate:** route + guard 1h, serializer 2h, PDF via existing helper 3h, tests 2h = 8h raw → ~13h calibrated (calibration summary: median velocity 0.6 over 7 records). PDF helper is familiar; nothing novel.
**Block:** 4h today 13:00–17:00. Goal: JSON invoice endpoint green end to end. Stop: goal met, or 16:30 with a red test → close and re-plan.
```
Here the block covers less than the estimate, deliberately. PDF rendering is split into the next block or slice, not squeezed in.

Discouraged:
- `Estimate: finish invoice ticket, 2h`. No concrete tasks, and the number fits the afternoon rather than the work.
- `Implement provider X integration, 90min` while it is unknown whether X supports refresh tokens. That is an unresolved spike posing as an estimate.
- Changing the estimate to 4h because only 4h are available.
