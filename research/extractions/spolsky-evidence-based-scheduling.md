# Evidence Based Scheduling

## Source
- Author: Joel Spolsky
- URL: https://www.joelonsoftware.com/2007/10/26/evidence-based-scheduling/
- Published: 2007-10-26
- Normalized file: `sources/spolsky-evidence-based-scheduling.md`
- Relevant workflow stages: **ESTIMATE** (primary), **SLICE** (small-task decomposition), **CLOSE** (record estimate vs. actual), **COMMIT** (cutting scope to fit the box). Also touches IMPLEMENT (fixing bugs as they are found).

## Core principles

### DIRECT
- **ESTIMATE-EBS-01** — Break the schedule into very small tasks measured in *hours*; nothing longer than 16 hours. A schedule measured in days or weeks "it's not going to work." *(§1 Break 'er down)*
- **ESTIMATE-EBS-02** — The 16-hour limit forces you to work out what you are actually going to do, i.e. to *design* the feature. Small development tasks are easy to estimate because you have done similar ones before. *(§1)*
- **ESTIMATE-EBS-03** — A big, hand-wavy multi-week task means you have not thought about the steps, so you cannot know how long it will take and you will forget many of them. *(§1)*
- **CLOSE-EBS-01** — Individual estimates can't be made exactly right (interruptions, unpredictable bugs, meetings). So keep timesheets: track how long you spend on each task and compare it with the estimate afterwards. *(§2 Track elapsed time)*
- **CLOSE-EBS-02** — Velocity = estimate ÷ actual, for each completed task. Build up a velocity history for each developer. *(§2)*
- **ESTIMATE-EBS-04** — There are three estimator profiles. The *perfect estimator* (velocities all 1) is imaginary. The *bad estimator* has velocities all over the map. The *common estimator* gets the scale wrong and the relative estimates right, so velocities are consistent but below 1.0. *(§2)*
- **ESTIMATE-EBS-05** — Estimating improves with experience, so throw away velocities older than about six months. *(§2)*
- **ESTIMATE-EBS-06** — A new estimator with no track record should be given a pessimistic fake history with a wide range of velocities until they have finished about half a dozen real tasks. *(§2)*
- **ESTIMATE-EBS-07** — Don't just add up the estimates to get one date: it "sounds right but gives you a profoundly wrong result." Instead, simulate many futures (Monte Carlo) by dividing each estimate by a velocity drawn at random from the developer's own history. The result is a probability distribution over ship dates. *(§3 Simulate the future)*
- **ESTIMATE-EBS-08** — The shape of the distribution carries information. A shallow curve (from a bad estimator) says the predicted dates don't deserve confidence. A steep curve means higher confidence. *(intro; §3)*
- **CLOSE-EBS-03** — For unpredictable interruptions you don't need separate estimates or timesheet entries. Just *keep the clock running* on the task you were doing when the interruption happened. The velocity history then absorbs how often interruptions occur. *(§ Obsessive-compulsive disorder not required)*
- **COMMIT-EBS-01** — Build buffer into the original schedule for: new feature ideas, responding to the competition, integration, debugging, usability testing, and beta tests. Take new work out of the appropriate buffer. *(§ Scope creep)*
- **CLOSE-EBS-04** — Snapshot the ship-date distribution every night. If the ship date is getting later by more than one day per day, you are adding work faster than you complete it and you will never finish. The 5/50/95% curves should converge over time. *(§ Scope creep)*
- **ESTIMATE-EBS-09** — Only the programmer doing the work can create the estimate. A schedule written by management and handed to programmers is doomed. *(§ While we're at it, 1)*
- **IMPLEMENT-EBS-01** — Fix bugs as you find them and charge the time to the original task. This makes the estimates predict *fully debugged* code, not just *working* code. *(§ While we're at it, 2)*
- **ESTIMATE-EBS-10** — Don't let managers badger developers into shorter estimates. The schedule is not the place for psychological games. *(§ While we're at it, 3)*
- **ESTIMATE-EBS-11** — Code you haven't thought through step by step seems like it will take *n*. In reality it will probably take about 4*n*, and you can never get 4*n* out of *n*. *(§ While we're at it, 3)*
- **COMMIT-EBS-02** — A schedule is a box of wood blocks. If the blocks don't fit, get a bigger box (delay) or remove blocks (cut features). You can't shrink the blocks, and pretending you can is lying to yourself. *(§ While we're at it, 4)*
- **COMMIT-EBS-03** — A realistic schedule forces feature cuts before work starts, and that pushes out the easy/fun but useless features in favour of the useful ones. *(§ While we're at it, 4)*

### INFERRED
- **ESTIMATE-EBS-12** — Whether a task is estimable depends on whether its steps have been thought through. The size cap is a proxy for "have you designed it?" *(from §1)*
- **CLOSE-EBS-05** — Estimate-vs-actual data is only worth recording if the estimate was written down *before* the work started and the actual covers the whole elapsed time, including interruptions and bug fixing on that task. *(from §2, § OCD not required, § While we're at it 2)*
- **ESTIMATE-EBS-13** — A calibrated forecast adjusts the estimator's own numbers using their own history. It does not replace personal estimates with someone else's. *(from §3 and While we're at it 1)*

## Procedure / workflow
The source presents this sequence explicitly as numbered steps (DIRECT):
1. **Break 'er down**: split into tasks of 16 hours or less. *(§1)*
2. **Track elapsed time**: keep timesheets per task and compute velocities. *(§2)*
3. **Simulate the future**: run a Monte Carlo over the velocity history, convert to calendar time (schedules, vacations, holidays), and take the last developer to finish as the team finish date. *(§3)*
4. **Manage your projects actively**: use the distributions to cut lower-priority features, spot uncertain estimators, and spot overloaded developers. *(§4)*

Plus, as DIRECT supporting practices: build buffers (§ Scope creep), take a nightly snapshot (§ Scope creep), and the four "While we're at it" rules.

Summary cost (DIRECT, § Summary): a day or two per iteration to produce detailed estimates, plus a few seconds a day to record which task you're starting.

## Decision rules and gates
- **ESTIMATE-EBS-14** — Gate: if any task is estimated above 16 hours, it is not ready. Break it down, which means designing it. *(§1; DIRECT)*
- **ESTIMATE-EBS-15** — Rule: if there's no velocity history, assume the worst and use a wide pessimistic history until about 6 real tasks are done. *(§2; DIRECT)*
- **COMMIT-EBS-04** — Rule: if the schedule exceeds the target, delay or delete features. Never "shrink" the estimates. *(§ While we're at it, 4; DIRECT)*
- **CLOSE-EBS-06** — Signal: if the ship date is slipping more than one day per day, work is being added faster than it's completed. Stop adding or start cutting. *(§ Scope creep; DIRECT for the signal, INFERRED for "stop adding or cut")*
- **ESTIMATE-EBS-16** — Rule: if the estimate didn't come from the person doing the work, it isn't a valid EBS input. *(§ While we're at it, 1; DIRECT)*
- **CLOSE-EBS-07** — Rule: if the distribution is very wide, don't trust the date. It says the estimator needs to learn to estimate better. *(§3; §4 "Milton"; DIRECT)*

## Questions the future agent could ask
- **ESTIMATE-EBS-Q01** `[INFERRED]` — Is any task in this plan longer than 16 hours? If so, what are its concrete steps? *(§1)*
- **ESTIMATE-EBS-Q02** `[INFERRED]` — Could you name each task as a concrete action (write this function, create this dialog, parse this file) rather than a feature label? *(§1)*
- **ESTIMATE-EBS-Q03** `[INFERRED]` — Have you done something like this before? Which past task is it most like? *(§1 "you've written subroutines… before")*
- **ESTIMATE-EBS-Q04** `[INFERRED]` — Is this your own estimate, or one you were handed? *(§ While we're at it, 1)*
- **CLOSE-EBS-Q01** `[INFERRED]` — What was the estimate, what was the actual elapsed time (interruptions included), and what does that velocity add to your history? *(§2; § OCD not required)*
- **CLOSE-EBS-Q02** `[INFERRED]` — Did you find and fix bugs in this slice? Was that time charged back to the original task? *(§ While we're at it, 2)*
- **COMMIT-EBS-Q01** `[INFERRED]` — If this doesn't fit the time available, which block comes out, or does the box get bigger? *(§ While we're at it, 4)*
- **ESTIMATE-EBS-Q05** `[DERIVED]` — Given your recent velocities (e.g. around 0.6), what does your raw estimate become once calibrated?

## Positive examples from the source

### ESTIMATE-EBS-P01 — Concrete hour-sized tasks
**Classification:** DIRECT
**Source location:** §1 Break 'er down
**What happens:** Tasks are named as concrete actions: "Write subroutine *foo*. Create this dialog box. Parse the Fizzbott file."
**Why it is positive:** These are easy to estimate because the developer has done similar things before. Stating them forces you to work out what you'll actually do.
**Principle illustrated:** ESTIMATE-EBS-01, -02.

### ESTIMATE-EBS-P02 — The common estimator is calibratable
**Classification:** DIRECT
**Source location:** §2 Track elapsed time; §3 Simulate the future
**What happens:** A developer's velocities cluster around 0.6 ({0.6, 0.5, 0.6, …}). In simulation an 8-hour task becomes about 13–15 hours, and the range of ship dates comes out narrow.
**Why it is positive:** Consistent optimism can be corrected "precisely" from the developer's proven history. The estimator doesn't need to be perfect, only consistent.
**Principle illustrated:** ESTIMATE-EBS-04, -07.

### CLOSE-EBS-P01 — John keeps the clock running
**Classification:** DIRECT
**Source location:** § Obsessive-compulsive disorder not required
**What happens:** John's getters and setters each take 2 hours. His boss sometimes interrupts with a two-hour marlin-fishing conversation. John doesn't log it separately. He keeps the clock running, so actuals read {2,2,2,2,4,…} and velocities {1,1,1,1,0.5,…}.
**Why it is positive:** In simulation, the chance of dividing by 0.5 equals the chance of an interruption, so the schedule comes out correct without any interruption tracking.
**Principle illustrated:** CLOSE-EBS-03.

### COMMIT-EBS-P01 — Excel 5 cuts
**Classification:** DIRECT
**Source location:** § While we're at it, 4
**What happens:** The Excel 5 feature list would have blown the schedule. The team cut features "to the bone" and called them deferred to Excel 6. Later, not one deferred feature turned out to be worth doing.
**Why it is positive:** A realistic schedule forced the cuts. Without them Excel 5 would have taken twice as long and included "50% useless" features.
**Principle illustrated:** COMMIT-EBS-02, -03.

## Negative examples / anti-patterns from the source

### ESTIMATE-EBS-N01 — "Implement Ajax photo editor" (three weeks)
**Classification:** DIRECT
**Source location:** §1 Break 'er down
**What happens:** A task is sized at three weeks with no detailed design.
**Why it is negative:** You "haven't thought about what you are going to do," so you can't know how long it'll take, and you're sure to forget steps. The source calls this "officially *doomed*."
**Principle violated:** ESTIMATE-EBS-01, -02, -03.

### ESTIMATE-EBS-N02 — Summing estimates for one date
**Classification:** DIRECT
**Source location:** §3 Simulate the future
**What happens:** Estimates are added together to get a single ship date.
**Why it is negative:** It "sounds right but gives you a profoundly wrong result." It ignores the estimator's history and the spread of outcomes.
**Principle violated:** ESTIMATE-EBS-07.

### ESTIMATE-EBS-N03 — Management-authored schedule
**Classification:** DIRECT
**Source location:** § While we're at it, 1
**What happens:** Management writes the schedule and hands it to programmers.
**Why it is negative:** Only the implementer can work out the steps. Such a system "is doomed to fail."
**Principle violated:** ESTIMATE-EBS-09.

### ESTIMATE-EBS-N04 — Badgering into tight estimates
**Classification:** DIRECT
**Source location:** § While we're at it, 3
**What happens:** Rookie managers set unrealistically short schedules to "motivate" programmers. Features that "would take three months" really take twelve (*n* vs 4*n*). Managers then try to make people work faster or add staff.
**Why it is negative:** Being behind schedule demotivates people. New hires run at about 50% for months. Overwork doubles debugging time. You can't get 4*n* out of *n*.
**Principle violated:** ESTIMATE-EBS-10, -11.

### COMMIT-EBS-N01 — Easy/fun feature first
**Classification:** DIRECT
**Source location:** § While we're at it, 4
**What happens:** With no schedule, programmers do the easy, fun, useless feature first (the "\<blink\>" example). They run out of time and the schedule slips to fit the useful one.
**Why it is negative:** Without a schedule, nothing forces the cut before the work starts.
**Principle violated:** COMMIT-EBS-03.

### ESTIMATE-EBS-N05 — Halfhearted, forgotten schedules
**Classification:** DIRECT
**Source location:** Introduction
**What happens:** Schedules sit on a file share and are forgotten. At the post-mortem, two years late, someone finds "two weeks for rewriting from scratch in Ruby."
**Why it is negative:** A schedule that isn't fed with evidence and used can't inform decisions.
**Principle violated:** CLOSE-EBS-01 (feedback loop).

### COMMIT-EBS-N02 — Shrinking the blocks
**Classification:** DIRECT
**Source location:** § While we're at it, 4
**What happens:** When the plan doesn't fit, people pretend the blocks (tasks) are smaller.
**Why it is negative:** You deprive yourself of the chance to "see into the future" by lying to yourself about what you see.
**Principle violated:** COMMIT-EBS-02.

## Contrastive pairs

### ESTIMATE-EBS-C01 — Task granularity
**Good / preferred:** "Write subroutine foo. Create this dialog box. Parse the Fizzbott file." These are hour-sized concrete actions, each 16 hours or less.
**Bad / discouraged:** "Implement Ajax photo editor," a three-week task with no detailed design.
**Classification:** DIRECT
**Source location:** §1 Break 'er down
**Distinguishing feature:** Whether the steps have been thought through (designed) and whether the task is familiar enough to estimate from experience.

### ESTIMATE-EBS-C02 — Forecast method
**Good / preferred:** A Monte Carlo simulation that divides each estimate by a random velocity from the developer's own history and yields a probability distribution.
**Bad / discouraged:** Adding up estimates to get one ship date.
**Classification:** DIRECT
**Source location:** §3 Simulate the future
**Distinguishing feature:** Whether the forecast uses historical evidence and represents uncertainty.

### CLOSE-EBS-C01 — Handling interruptions
**Good / preferred:** Keep the clock running on the current task (John/marlin).
**Bad / discouraged:** None is labelled bad. The source says tracking interruptions separately also works ("you can, if you want"), but you don't have to. Keeping the clock running gives the best results.
**Classification:** DIRECT (preference stated; the alternative is acceptable but inferior, not an anti-pattern)
**Source location:** § Obsessive-compulsive disorder not required
**Distinguishing feature:** Low-effort tracking that still captures how often interruptions happen.

### COMMIT-EBS-C02 — When the plan doesn't fit
**Good / preferred:** Get a bigger box (delay shipping) or remove blocks (delete features).
**Bad / discouraged:** Shrink the blocks (pretend the tasks take less time), or badger developers into shorter estimates.
**Classification:** DIRECT
**Source location:** § While we're at it, 3–4
**Distinguishing feature:** Whether the adjustment changes scope or time, or only falsifies the estimate.

### COMMIT-EBS-C03 — With vs without a schedule
**Good / preferred:** With a schedule you see before starting that something must be cut, so you cut the easy/fun feature and do the useful one.
**Bad / discouraged:** Without a schedule the fun feature gets done first, time runs out, and the schedule slips.
**Classification:** DIRECT
**Source location:** § While we're at it, 4
**Distinguishing feature:** Whether the trade-off is forced before the work starts or after time has run out.

### ESTIMATE-EBS-C03 — Estimator profiles
**Good / preferred:** The common estimator: consistently optimistic (velocities around 0.6), and correctable.
**Bad / discouraged:** The bad estimator: velocities all over the map ({0.1 … 13.0}), which gives a shallow, low-confidence curve.
**Classification:** DIRECT
**Source location:** §2; §3
**Distinguishing feature:** The *consistency* of the estimate/actual ratio matters more than its accuracy.

## Stop / go criteria

### GO
- Every task is 16 hours or less and named as a concrete action. *(§1)*
- The estimate comes from the person who will do the work. *(§ While we're at it, 1)*
- The work fits the box (time available) after calibration, or scope has been cut until it does. *(§ While we're at it, 4)*

### STOP / RETURN
- A task over 16 hours, or a feature label with no steps: stop and design/decompose it (return to SLICE/DERISK). *(§1)*
- A forecast built by summing raw estimates: redo it with calibration. *(§3)*
- The plan doesn't fit: cut features or extend time. Don't shrink the estimates. *(§ While we're at it, 4)*
- The ship date is slipping more than one day per day: work is being added faster than it's completed. *(§ Scope creep)*
- A very wide distribution: don't trust the date. *(§3; §4)*

## Common failure modes
- Big, vague, multi-week tasks (ESTIMATE-EBS-N01).
- Adding up estimates to get a single date (ESTIMATE-EBS-N02).
- Estimates written by someone other than the implementer (ESTIMATE-EBS-N03).
- Pressured "tight" estimates (ESTIMATE-EBS-N04).
- Schedules that are never fed back or used (ESTIMATE-EBS-N05).
- Pretending blocks shrink instead of cutting (COMMIT-EBS-N02).
- Doing easy/fun work before useful work (COMMIT-EBS-N01).
- Scheduling bug fixes separately instead of charging them to the original task, so estimates predict "working" rather than "fully debugged" code (IMPLEMENT-EBS-01, INFERRED as a failure mode).

## Terms worth preserving
- `velocity` — estimate ÷ actual for one completed task. **Not** the Scrum sense of points per sprint.
- `perfect estimator` / `bad estimator` / `common estimator` — the three velocity-history profiles.
- `Monte Carlo` simulation — many simulated futures, each dividing estimates by randomly drawn historical velocities.
- `confidence distribution curve` — the probability of shipping by each date; steeper means more confident.
- `keep the clock running` — charge interruption time to the current task.
- `buffer` — time reserved in the schedule for unplanned categories of work.
- `box of wood blocks` — fixed capacity: resize the box or remove blocks, never shrink the blocks.
- `fully debugged` vs `working` code — what estimates should predict.

## Candidate Skill rules
- `[DERIVED from §1]` Do not accept any task estimate over 16 hours. Break it into concrete, familiar actions first.
- `[DERIVED from §1]` If you can't list the steps of a task, treat that as missing design, not as a big estimate. Return to SLICE/DERISK.
- `[DERIVED from §2]` Record an estimate before starting each task and the actual elapsed time when you finish it.
- `[DERIVED from §2, § OCD not required]` Keep the clock running on the current task through interruptions. Don't subtract them from the actual.
- `[DERIVED from §2–3]` Adjust a raw estimate by the developer's own recent velocity history (≤ ~6 months). With no history, assume a wide, pessimistic range.
- `[DERIVED from §3]` Do not report a single summed date as a forecast. State a range and your confidence.
- `[DERIVED from § While we're at it, 1]` Do not produce an estimate on the developer's behalf. Ask the developer for their own and help them decompose.
- `[DERIVED from § While we're at it, 2]` Charge time spent fixing bugs in new code to the task that introduced them.
- `[DERIVED from § While we're at it, 4]` If the work doesn't fit the available time, cut scope or extend time. Never lower the estimate to make it fit.

## Source limitations
- The source addresses **team/project-scale release scheduling** (ship dates, critical path, several developers). An individual developer's loop only needs the calibration core: small tasks, estimate before, actual after, velocity history.
- It **requires historical data** (timesheets). A cold start gets a pessimistic fake history. The source doesn't cover tasks with no comparable past work beyond that.
- It **doesn't distinguish investigation/spike work** from implementation. It assumes a task can be designed into ≤16h steps, and says nothing about unknowns that can't be decomposed yet. That's a gap for DERISK (see Shape Up).
- **2007 tool context**: the method is described as built into FogBugz 6.0 (a P.S. removed during normalization). The Monte Carlo and calendar conversion assume tool support.
- "Velocity" here is estimate/actual, which can clash with other uses of the term.
- It gives no guidance on *what* to build or how to clarify behavior. It assumes the feature list exists.
- The 16-hour limit is presented as an assertion from experience, not as evidence-backed.

## Derived developer examples

### ESTIMATE-EBS-D01 — "Add endpoint" vs "rework auth"
**Classification:** DERIVED
**Grounded in:** EBS §1 Break 'er down (ESTIMATE-EBS-01, -02, -03; contrast ESTIMATE-EBS-C01)
**Preferred:** "Add `GET /orders/:id/invoice` endpoint" is broken into: route and controller returning 404 for a missing order (2h); serializer for the invoice fields (2h); authorization check that the order belongs to the user (2h); request tests for the three cases (3h). Each piece is familiar and ≤16h. Total raw 9h.
**Discouraged:** "Rework auth — about 2 weeks." There are no steps, and the developer can't say what changes first.
**Distinguishing feature:** The first has been designed into concrete, familiar steps. The second is a label. The agent should push the second back to SLICE/DERISK, not accept "2 weeks."

### CLOSE-EBS-D02 — Recording estimate vs actual after a slice
**Classification:** DERIVED
**Grounded in:** EBS §2 Track elapsed time; § OCD not required; § While we're at it, 2 (CLOSE-EBS-01, -02, -03; IMPLEMENT-EBS-01)
**Preferred:** A form-validation slice was estimated at 3h before starting. Actual was 5h, counting a 45-minute Slack interruption kept on the clock and 1h fixing a bug the slice introduced. Velocity recorded is 0.6, appended to the history.
**Discouraged:** The developer reports "about 3h of real coding," leaving out the interruption and the bug fix (logged later as a separate "bugfix" ticket). The recorded velocity is about 1.0 and the next estimate comes out optimistic again.
**Distinguishing feature:** Whether the actual covers the full elapsed time on that task, including interruptions and self-introduced bugs.

### COMMIT-EBS-D03 — Plan exceeds the time available
**Classification:** DERIVED
**Grounded in:** EBS § While we're at it, 3–4 (COMMIT-EBS-02, -03, -04; ESTIMATE-EBS-10)
**Preferred:** The calibrated total for a settings-page feature is about 14h, and only 8h are available before the demo. The developer drops "custom avatar cropping" (fun) and keeps "email change with verification" (useful).
**Discouraged:** The developer re-estimates each task 40% lower "to be aggressive" and keeps all of them.
**Distinguishing feature:** Removing blocks versus shrinking blocks.

## ID register
| ID | Stage | Type | Short label | Classification | Location |
|---|---|---|---|---|---|
| ESTIMATE-EBS-01 | ESTIMATE | rule | ≤16h tasks, measured in hours | DIRECT | §1 |
| ESTIMATE-EBS-02 | ESTIMATE | rule | Small tasks force design; familiar = estimable | DIRECT | §1 |
| ESTIMATE-EBS-03 | ESTIMATE | rule | Hand-wavy multi-week task = unthought steps | DIRECT | §1 |
| ESTIMATE-EBS-04 | ESTIMATE | rule | Perfect/bad/common estimator | DIRECT | §2 |
| ESTIMATE-EBS-05 | ESTIMATE | rule | Discard velocities > ~6 months | DIRECT | §2 |
| ESTIMATE-EBS-06 | ESTIMATE | rule | New estimator: pessimistic fake history until ~6 tasks | DIRECT | §2 |
| ESTIMATE-EBS-07 | ESTIMATE | rule | Monte Carlo, not summing | DIRECT | §3 |
| ESTIMATE-EBS-08 | ESTIMATE | rule | Distribution shape = confidence | DIRECT | intro; §3 |
| ESTIMATE-EBS-09 | ESTIMATE | rule | Only the implementer estimates | DIRECT | While we're at it 1 |
| ESTIMATE-EBS-10 | ESTIMATE | rule | Don't badger into short estimates | DIRECT | While we're at it 3 |
| ESTIMATE-EBS-11 | ESTIMATE | rule | n vs 4n | DIRECT | While we're at it 3 |
| ESTIMATE-EBS-12 | ESTIMATE | rule | Estimability = steps thought through | INFERRED | §1 |
| ESTIMATE-EBS-13 | ESTIMATE | rule | Calibrate own estimates with own history | INFERRED | §3; WWAI 1 |
| ESTIMATE-EBS-14 | ESTIMATE | gate | >16h ⇒ not ready, decompose | DIRECT | §1 |
| ESTIMATE-EBS-15 | ESTIMATE | rule | No history ⇒ assume worst | DIRECT | §2 |
| ESTIMATE-EBS-16 | ESTIMATE | rule | Estimate not from implementer ⇒ invalid | DIRECT | WWAI 1 |
| CLOSE-EBS-01 | CLOSE | rule | Track elapsed time per task vs estimate | DIRECT | §2 |
| CLOSE-EBS-02 | CLOSE | rule | Velocity = estimate/actual, history per dev | DIRECT | §2 |
| CLOSE-EBS-03 | CLOSE | rule | Keep the clock running on interruptions | DIRECT | OCD not required |
| CLOSE-EBS-04 | CLOSE | rule | Nightly snapshot; >1 day/day slip = never done | DIRECT | Scope creep |
| CLOSE-EBS-05 | CLOSE | rule | Estimate before, full actual after | INFERRED | §2; OCD; WWAI 2 |
| CLOSE-EBS-06 | CLOSE | gate | Slip >1 day/day ⇒ stop adding / cut | DIRECT (signal) / INFERRED (action) | Scope creep |
| CLOSE-EBS-07 | CLOSE | gate | Wide distribution ⇒ don't trust date | DIRECT | §3; §4 |
| COMMIT-EBS-01 | COMMIT | rule | Buffer categories | DIRECT | Scope creep |
| COMMIT-EBS-02 | COMMIT | rule | Box of wood blocks | DIRECT | WWAI 4 |
| COMMIT-EBS-03 | COMMIT | rule | Realistic schedule forces good cuts | DIRECT | WWAI 4 |
| COMMIT-EBS-04 | COMMIT | gate | Doesn't fit ⇒ delay or delete, never shrink | DIRECT | WWAI 4 |
| IMPLEMENT-EBS-01 | IMPLEMENT | rule | Fix bugs as found, charge to original task | DIRECT | WWAI 2 |
| ESTIMATE-EBS-Q01 | ESTIMATE | question | Any task >16h? Steps? | INFERRED | §1 |
| ESTIMATE-EBS-Q02 | ESTIMATE | question | Named as concrete action? | INFERRED | §1 |
| ESTIMATE-EBS-Q03 | ESTIMATE | question | Done similar before? | INFERRED | §1 |
| ESTIMATE-EBS-Q04 | ESTIMATE | question | Your own estimate? | INFERRED | WWAI 1 |
| ESTIMATE-EBS-Q05 | ESTIMATE | question | Calibrated estimate from velocity? | DERIVED | §2–3 |
| CLOSE-EBS-Q01 | CLOSE | question | Estimate, actual, velocity? | INFERRED | §2; OCD |
| CLOSE-EBS-Q02 | CLOSE | question | Bug time charged back? | INFERRED | WWAI 2 |
| COMMIT-EBS-Q01 | COMMIT | question | Which block comes out, or bigger box? | INFERRED | WWAI 4 |
| ESTIMATE-EBS-P01 | ESTIMATE | positive | foo / dialog / Fizzbott tasks | DIRECT | §1 |
| ESTIMATE-EBS-P02 | ESTIMATE | positive | Common estimator calibrated | DIRECT | §2–3 |
| CLOSE-EBS-P01 | CLOSE | positive | John / marlin, clock running | DIRECT | OCD not required |
| COMMIT-EBS-P01 | COMMIT | positive | Excel 5 cuts | DIRECT | WWAI 4 |
| ESTIMATE-EBS-N01 | ESTIMATE | negative | "Implement Ajax photo editor" 3 weeks | DIRECT | §1 |
| ESTIMATE-EBS-N02 | ESTIMATE | negative | Summing estimates | DIRECT | §3 |
| ESTIMATE-EBS-N03 | ESTIMATE | negative | Management-authored schedule | DIRECT | WWAI 1 |
| ESTIMATE-EBS-N04 | ESTIMATE | negative | Badgering / n vs 4n | DIRECT | WWAI 3 |
| ESTIMATE-EBS-N05 | ESTIMATE | negative | Forgotten halfhearted schedules | DIRECT | intro |
| COMMIT-EBS-N01 | COMMIT | negative | Easy/fun feature first | DIRECT | WWAI 4 |
| COMMIT-EBS-N02 | COMMIT | negative | Shrinking the blocks | DIRECT | WWAI 4 |
| ESTIMATE-EBS-C01 | ESTIMATE | pair | Concrete ≤16h tasks vs Ajax photo editor | DIRECT | §1 |
| ESTIMATE-EBS-C02 | ESTIMATE | pair | Monte Carlo vs summing | DIRECT | §3 |
| ESTIMATE-EBS-C03 | ESTIMATE | pair | Common vs bad estimator | DIRECT | §2–3 |
| CLOSE-EBS-C01 | CLOSE | pair | Clock running vs separate interruption tracking | DIRECT | OCD not required |
| COMMIT-EBS-C02 | COMMIT | pair | Bigger box / remove blocks vs shrink blocks | DIRECT | WWAI 3–4 |
| COMMIT-EBS-C03 | COMMIT | pair | Schedule vs no schedule cuts | DIRECT | WWAI 4 |
| ESTIMATE-EBS-D01 | ESTIMATE | derived | Add endpoint vs rework auth | DERIVED | §1 |
| CLOSE-EBS-D02 | CLOSE | derived | Estimate vs actual after a slice | DERIVED | §2; OCD; WWAI 2 |
| COMMIT-EBS-D03 | COMMIT | derived | Plan exceeds time: cut vs shrink | DERIVED | WWAI 3–4 |

(WWAI = "While we're at it"; OCD = "Obsessive-compulsive disorder not required".)
