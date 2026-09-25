# Close

## Purpose
Compare intent with outcome. Record estimate vs actual, capture discovered work, decide whether the slice is good enough by comparing it to the baseline, and choose the next slice.

## Primary grounding sources
- Spolsky, *EBS*: primary for estimate vs actual, velocity and interruptions.
- Singer, *Decide When to Stop*: primary for baseline, scope hammering and must-have vs nice-to-have.
- Singer, *Hand Over Responsibility* / *Show Progress*: supporting. Discovered tasks are expected; lists grow as work progresses.
- Wake, *INVEST (SMART Measurable)*: supporting. "Can we mark it as done?"
- Beck, *Canon TDD*: supporting. The fear → boredom stop condition.
- Newport: supporting. Time blocks give hard evidence of how long things take; captured items are processed later.

## Entry conditions
- Implement exit (list empty) or a time-box stop.

## Agent questions
1. Can you mark it done? Does it do what it was meant to, are tests included, and is the code refactored? (DIRECT, CLOSE-INVEST-Q05 / CLOSE-INVEST-03)
2. What did you estimate, what did it actually take, and what velocity does that give (estimate ÷ actual)? (INFERRED, CLOSE-EBS-Q01)
3. Did bug-fix and interruption time count against this task? (INFERRED, CLOSE-EBS-Q02; CLOSE-EBS-03)
4. Is it better than what users have today (the baseline), even if it isn't ideal? (DIRECT, CLOSE-STOP-Q05)
5. For each remaining or discovered item: is it a must-have? Could you ship without it? What happens if you don't do it? Is it new or pre-existing? How likely is it, and who does it affect? (DIRECT, CLOSE-STOP-Q07)
6. What goes on the list next? Which remaining item is most core, most novel, or scariest? (INFERRED, SLICE-ONEPIECE-06 + DERISK-HILL-06)

## Rules
- **Record time actually spent against the estimate for each task.** (DIRECT, CLOSE-EBS-01/-02)
- **Keep the clock running through interruptions.** Don't separate them out. The velocity history then accounts for them. (DIRECT, CLOSE-EBS-03)
- **Count bug-fix time against the original task**, so estimates predict *fully debugged* code. (DIRECT, IMPLEMENT-EBS-01)
- **"Done" means it does what was intended, includes tests, and has been refactored.** (DIRECT, CLOSE-INVEST-03). Shape Up's team version is "done means deployed". (DIRECT, CLOSE-HANDOVER-07)
- **Compare down to the baseline, not up to the ideal.** (DIRECT, CLOSE-STOP-01/-C04)
- **Expect discovered tasks.** Lists grow as work progresses, and scope grows like grass. Sort new items into must-have vs nice-to-have (Shape Up marks nice-to-haves with `~`). (DIRECT, CLOSE-HANDOVER-04, CLOSE-STOP-03/-06; ESTIMATE-HILL-01)
- **Cutting scope isn't lowering quality.** (DIRECT, CLOSE-STOP-04)
- **Process captured items later.** They become slices, bugs or discarded notes. (INFERRED, CLOSE-TBP-01)
- **If the ship date slips by more than a day per day, work is being added faster than it's finished.** (DIRECT signal at project scale, CLOSE-EBS-04/-06)

## Positive patterns
- John and the marlin conversations: keeping the clock running makes interruption probability show up exactly in the velocities. (DIRECT, CLOSE-EBS-P01)
- A finished scope with one `~` nice-to-have that was never built. (DIRECT, Decide When to Stop, Scope hammering; see CLOSE-STOP-06)
- QA findings are nice-to-haves by default, and the team promotes the must-haves. (DIRECT, CLOSE-STOP-07)

## Anti-patterns
- Aiming for the ideal, so the work is never good enough. (DIRECT, CLOSE-STOP-C04)
- A to-do list with nothing left open, read as "done" when tasks simply haven't been discovered yet. (DIRECT, ESTIMATE-HILL-01 / Show Progress, The tasks that aren't there)
- Forgotten, halfhearted schedules that are never compared with reality. (DIRECT, ESTIMATE-EBS-N05)

## Contrastive examples

**CLOSE-STOP-C04 (DIRECT pair):** compare down to the baseline ("better than what they have now") vs compare up to the ideal ("never good enough").

**CLOSE-SYN-D01: Recording estimate vs actual after a slice** (DERIVED; grounded in CLOSE-EBS-01/-03, IMPLEMENT-EBS-01)
- *Preferred:* "Invoice endpoint: estimated 8h, actual 12.5h, including 1.5h for a rounding bug found during the slice and 1h of a support call I didn't stop the clock for. Velocity 0.64. Discovered: PDF font embedding (must-have, next slice); admin re-send (~ nice-to-have)."
- *Discouraged:* "Done, took a bit longer," with no numbers, the bug logged as a separate unplanned task, and discovered items left in your head.

**CLOSE-SYN-D02: Time box ended before the test list was empty** (DERIVED; grounded in COMMIT-STOP-08/-09, CLOSE-STOP-05)
- *Preferred:* Two items remain. One is downhill and must-have, so re-block it tomorrow. The other still has an unknown (uphill), so turn it into a spike rather than extending.
- *Discouraged:* Keep going into the evening "because it's almost done".

## Stop / return conditions
- The remaining work is uphill → return to De-risk. Do not extend. (DIRECT, COMMIT-STOP-09)
- A discovered must-have changes the problem → Clarify.
- Otherwise → Slice (next slice) or stop.

## Exit criteria
- The estimate/actual/velocity record is appended to the developer's history.
- Discovered items are sorted into must-have, nice-to-have and captured-for-later.
- The next slice is named, or the work is explicitly stopped.

## Unresolved tensions between sources
- **What "done" requires.** Wake: done = intended behavior + tests + refactored. Shape Up: done = deployed, with docs/marketing optional. Beck: done = list empty and fear gone. These are different thresholds, and the Skill should say which one applies.
- **Interruptions.** EBS wants them left inside the task's actual time. Newport wants the *plan* rebuilt after a disruption. Both can hold, since one is measurement and the other is scheduling, but the Skill must not "correct" actuals for interruptions.
- **Retrospection is thin.** No source gives a structured intent-vs-outcome review beyond estimate vs actual and scope triage (see `gaps.md`).

## Provenance map
| Rule / example | Source | Classification | Source section |
|---|---|---|---|
| Track elapsed time; velocity | Spolsky, EBS | DIRECT | 2) Track elapsed time |
| Keep the clock running | Spolsky, EBS | DIRECT | Obsessive-compulsive disorder not required |
| Charge bug time to original task | Spolsky, EBS | DIRECT | While we're at it 2 |
| Can we mark it done | Wake, INVEST | DIRECT | Measurable |
| Compare to baseline | Singer, Decide When to Stop | DIRECT | Compare to baseline |
| Scope hammering questions; ~ nice-to-have | Singer, Decide When to Stop | DIRECT | Scope hammering |
| Discovered tasks; lists grow | Singer, Hand Over Responsibility; Show Progress | DIRECT | Imagined vs discovered tasks; The tasks that aren't there |
| Fear → boredom | Beck, Canon TDD | DIRECT | 5 |
| Captured items processed later | Newport, Time-Block Planner | INFERRED | A Closer Look |
| CLOSE-SYN-D01, D02 | — | DERIVED | — |
