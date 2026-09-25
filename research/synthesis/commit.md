# Commit

## Purpose
Decide how much time the slice is worth (appetite), put that time on the calendar (time block), and state the goal and the stop condition before starting. Three things are committed here and must be kept apart:
- **Appetite**: how much the work *deserves*. It sets scope (Shape Up).
- **Time block**: *when* the work happens. It is a plan for attention and can be revised (Newport).
- **Estimate**: how long the designed work is *expected* to take (EBS; see `estimate.md`).

A personal time block is not a delivery commitment.

## Primary grounding sources
- Singer, *Set Boundaries*: primary for appetite and fixed time / variable scope.
- Newport, *Focus Week*: primary for time blocking.
- Newport, *Time-Block Planner*: supporting, limited to the one method paragraph.
- Spolsky, *EBS*: supporting. Box of wood blocks, buffer.
- Singer, *Decide When to Stop*: supporting. "Is there time for this?", when to extend.
- Wake, *INVEST (SMART)*: supporting. A time-boxed task tells you when to seek help or split.

## Entry conditions
- The slice has an estimate, or is an explicitly time-boxed spike.

## Agent questions
1. How much of your time is this slice worth: a quick fix, half a day, more? (DIRECT idea, COMMIT-BOUND-Q01; scaling it to hours is DERIVED)
2. Does the estimate fit the appetite? If not, which part comes out, or does the box get bigger? (INFERRED, COMMIT-EBS-Q01)
3. What specific work is this block for, and what counts as done at the end of it? (INFERRED, COMMIT-TBLOCK-Q01; the stop condition is DERIVED)
4. At what point will you stop and ask for help, split, or re-plan? (INFERRED, COMMIT-INVEST-Q06)
5. Is this the important work, or are you reacting? (INFERRED, COMMIT-TBLOCK-Q02)

## Rules
- **Set an appetite explicitly before designing further.** The appetite is a time budget that constrains the solution. (DIRECT, COMMIT-BOUND-02/-03)
- **Fixed time, variable scope.** When time runs short, cut scope and keep quality. (DIRECT, COMMIT-BOUND-06; COMMIT-BOUND-P04 typos vs extra section)
- **"Good" is relative to the time you're willing to spend.** (DIRECT, COMMIT-BOUND-07)
- **If it doesn't fit, get a bigger box or remove blocks. Never pretend to shrink the blocks.** (DIRECT, COMMIT-EBS-02/-04)
- **Give every minute a job.** Partition the working day into blocks with specific work assigned. (DIRECT, COMMIT-TBLOCK-01/-02; COMMIT-TBP-01)
- **When knocked off the plan, rebuild the schedule for the rest of the day.** Intention, not perfection. (DIRECT, COMMIT-TBLOCK-03/-09; COMMIT-TBP-02/-04)
- **A task should be time-boxed so you know when to seek help, split it, or change approach.** (DIRECT, COMMIT-INVEST-02/-04)
- **Before accepting new work mid-slice, ask "Is there time for this?"** (DIRECT, COMMIT-STOP-02)
- **Only extend when the remaining work is must-have *and* downhill.** Uphill work at the deadline means reshaping, not extending. (DIRECT, COMMIT-STOP-08/-09)
- **Don't extend time blocking to life outside work.** (DIRECT, COMMIT-TBLOCK-06/-10)

## Positive patterns
- The book deadline: with a week left, the author chose fixing typos over adding a section. (DIRECT, COMMIT-BOUND-P04)
- Newport's example day: strategy memo 9–10, meeting, 30 minutes of email, 90 minutes on a project report. (DIRECT, COMMIT-TBLOCK-P01)
- Excel 5 features cut to fit the schedule turned out to be the least valuable. (DIRECT, COMMIT-EBS-P01)

## Anti-patterns
- The list/reactive day: filling the time between meetings by reacting to email. (DIRECT, COMMIT-TBLOCK-N01)
- With no schedule, programmers do the easy/fun feature first and run out of time for the useful one. (DIRECT, COMMIT-EBS-N01)
- Shrinking the blocks, i.e. pretending the work will take less. (DIRECT, COMMIT-EBS-N02)
- Accepting every "wouldn't it be better if…" without asking whether there's time. (DIRECT, COMMIT-STOP-N06)

## Contrastive examples

**COMMIT-TBLOCK-C01 (DIRECT pair):** time blocking vs list/reactive. The distinguishing feature is whether work is assigned to specific time in advance.

**COMMIT-SYN-D01: Appetite vs estimate for an endpoint** (DERIVED; grounded in ESTIMATE-BOUND-05, COMMIT-EBS-04)
- *Preferred:* "This invoice endpoint is worth about half a day (appetite). My calibrated estimate is about 13h, so it doesn't fit. Cut PDF rendering (return JSON only, PDF as the next slice), or decide it's worth two days."
- *Discouraged:* "I'll squeeze the 13h into this afternoon," which shrinks the blocks.

**COMMIT-SYN-D02: Block with a goal and stop condition** (DERIVED; grounded in COMMIT-TBLOCK-02, COMMIT-INVEST-02)
- *Preferred:* "10:00–12:00: make the owner-delete scenario pass end to end. Stop condition: both Given/When/Then examples green, or at 11:30 with no passing test → stop and re-plan."
- *Discouraged:* "Morning: work on comments."

## Stop / return conditions
- The estimate exceeds the appetite and nothing can be cut → return to Slice (smaller slice) or Clarify (narrower problem). Do not commit anyway.
- The block has no specific goal → it isn't a time block in Newport's sense. (INFERRED, COMMIT-TBLOCK-08)

## Exit criteria
- A written statement giving the slice goal, the appetite, the calibrated estimate, the time block(s), and the stop condition. The stop condition is either "done" (examples pass) or "time box hit → re-plan".

## Unresolved tensions between sources
- **Re-planning freedom vs a fixed time box.** Newport: when disrupted, simply rebuild the rest of the day. Shape Up: the fixed time box is a circuit breaker and extensions are rare. These operate at different levels (attention scheduling vs delivery commitment). The Skill should let blocks move while holding the appetite fixed.
- **Newport gives no stop condition** for the task inside a block. The block ends when time ends. The "goal + stop condition" rule is DERIVED from Shape Up (appetite), Wake (time-boxed tasks) and Beck (list empty).
- **Appetite at hours/days scale is an adaptation.** Shape Up defines appetite only as Small Batch (1–2 weeks) or Big Batch (6 weeks) for a team.
- **Buffer vs fixed scope.** EBS builds buffer for new features, integration, debugging and so on. Shape Up handles overrun by hammering scope and using cool-down, not by buffering.

## Provenance map
| Rule / example | Source | Classification | Source section |
|---|---|---|---|
| Appetite; Small/Big Batch | Singer, Set Boundaries | DIRECT | Setting the appetite |
| Fixed time, variable scope | Singer, Set Boundaries | DIRECT | Fixed time, variable scope |
| Good is relative | Singer, Set Boundaries | DIRECT | "Good" is relative |
| Bigger box or remove blocks | Spolsky, EBS | DIRECT | While we're at it 4 |
| Every minute a job; rebuild when knocked off | Newport, Focus Week; Time-Block Planner | DIRECT | basic idea; A Closer Look |
| Time-boxed task → seek help/split | Wake, INVEST | DIRECT | Time-Boxed |
| Is there time for this? / when to extend | Singer, Decide When to Stop | DIRECT | Limits motivate trade-offs; When to extend |
| Goal + stop condition per block | — | DERIVED | — |
| COMMIT-SYN-D01, D02 | — | DERIVED | — |
