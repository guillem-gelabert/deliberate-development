# Estimate

## Purpose
Produce the developer's own estimate for the concrete, de-risked slice, broken into small familiar tasks and calibrated against the developer's history of estimate vs actual. An estimate is **not** an appetite. An estimate starts from a design and ends with a number. An appetite starts from a number and shapes the design (see `commit.md`).

## Primary grounding sources
- Spolsky, *Evidence Based Scheduling*: primary.
- Singer, *Show Progress*: primary counterweight. Estimates don't show uncertainty and are only meaningful at the top of the hill.
- Singer, *Set Boundaries*: supporting. Appetite ≠ estimate.
- Wake, *INVEST*: supporting. What makes a story estimable.

## Entry conditions
- The slice has passed De-risk: no open rabbit holes, and the work is downhill or close to it.

## Agent questions
1. Is every task 16 hours or less, named as a concrete action (write X, create Y, parse Z)? (INFERRED, ESTIMATE-EBS-Q01/Q02)
2. Have you done tasks like these before? (INFERRED, ESTIMATE-EBS-Q03)
3. Is this your own estimate as the person doing the work? (INFERRED, ESTIMATE-EBS-Q04)
4. What does your recent estimate/actual history say? Adjust the raw estimate by your typical ratio. (DERIVED, ESTIMATE-EBS-Q05)
5. Is this still uphill? If you can't list the steps yet, the number is not meaningful. (INFERRED, ESTIMATE-HILL-04/-09)
6. If it can't be estimated, why: not understood, too big, or unfamiliar to you? (INFERRED, ESTIMATE-INVEST-Q04)

## Rules
- **Break the work into tasks of 16 hours or less, measured in hours.** (DIRECT, ESTIMATE-EBS-01/-14)
- **Small tasks force you to design the feature.** A hand-wavy multi-week task means the steps haven't been thought through and some are being forgotten. (DIRECT, ESTIMATE-EBS-02/-03)
- **Only the programmer doing the work creates the estimate.** (DIRECT, ESTIMATE-EBS-09)
- **Calibrate with history.** Velocity = estimate ÷ actual. Most estimators are consistently optimistic, which can be corrected. Erratic estimators produce low-confidence dates. (DIRECT, ESTIMATE-EBS-04; CLOSE-EBS-02)
- **Discard velocity data older than about six months. With no history, assume the worst** until about six real tasks are recorded. (DIRECT, ESTIMATE-EBS-05/-06)
- **Don't sum point estimates into one date.** Simulate many possible futures, e.g. with Monte Carlo, to get a probability distribution. (DIRECT, ESTIMATE-EBS-07; relevant mostly at project scale)
- **Don't negotiate estimates down.** Work that seems like *n* often takes about 4*n* when the steps are counted. (DIRECT, ESTIMATE-EBS-10/-11)
- **An estimate is only meaningful where the work is understood.** Two 4-hour estimates mean very different things if one task is familiar and the other is novel. (DIRECT, ESTIMATE-HILL-02/N04; ESTIMATE-HILL-04 "top of the hill")
- **Do not substitute appetite for estimate, or estimate for appetite.** (DIRECT, ESTIMATE-BOUND-05; INFERRED, ESTIMATE-BOUND-15)

## Positive patterns
- "Write subroutine foo. Create this dialog box. Parse the Fizzbott file." These are small, familiar and easy to estimate. (DIRECT, ESTIMATE-EBS-P01)
- The common estimator: consistent velocities around 0.6. The simulation corrects for this optimism precisely. (DIRECT, ESTIMATE-EBS-P02)
- Dinner party: estimating shopping and prep only became fair once a recipe was chosen, at the top of the hill. (DIRECT, ESTIMATE-HILL-P05)

## Anti-patterns
- "Implement Ajax photo editor": three weeks, no detailed design, officially "doomed". (DIRECT, ESTIMATE-EBS-N01)
- Adding up estimates to get a single ship date. (DIRECT, ESTIMATE-EBS-N02)
- A manager writing the schedule for programmers. (DIRECT, ESTIMATE-EBS-N03)
- Badgering programmers into "tight" estimates. (DIRECT, ESTIMATE-EBS-N04)
- Two identical "4 hours" estimates hiding very different uncertainty. (DIRECT, ESTIMATE-HILL-N04)

## Contrastive examples

**ESTIMATE-EBS-C01 (DIRECT pair):** concrete ≤16h tasks (foo / dialog / Fizzbott) vs "Implement Ajax photo editor" (3 weeks). The distinguishing feature is whether the steps have been designed.

**ESTIMATE-SYN-D01: Adding an endpoint vs "rework auth"** (DERIVED; grounded in ESTIMATE-EBS-01/-03)
- *Preferred:* `GET /orders/:id/invoice` → route + auth guard (1h), serializer (2h), PDF render using the existing helper (3h), tests (2h). Raw total 8h. With a personal velocity of about 0.6, plan for about 13h.
- *Discouraged:* "Rework auth: about 2 weeks." There are no steps, so no number is meaningful. Return to Slice and De-risk.

**ESTIMATE-SYN-D02: Novel vs familiar task with the same raw number** (DERIVED; grounded in ESTIMATE-HILL-02)
- *Preferred:* "4h (done this 10 times)" and "4h, but uphill: websocket reconnection is new to me, spike first".
- *Discouraged:* Two bare "4h" entries.

## Stop / return conditions
- Any task is over 16h or can't be named as a concrete action → return to Slice or De-risk. (DIRECT gate, ESTIMATE-EBS-14)
- The work is still uphill → return to De-risk (spike). (INFERRED, ESTIMATE-HILL-09)
- The estimate came from someone other than the implementer → re-estimate. (DIRECT, ESTIMATE-EBS-16)

## Exit criteria
- A task list of ≤16h items with raw estimates, a calibrated total using personal history (or a pessimistic default when there is none), and any tasks still uncertain flagged as such.

## Unresolved tensions between sources
- **Up-front task breakdown vs discovered tasks. This is a genuine conflict.** Spolsky: break everything into ≤16h tasks up front, which forces design. Singer: teams begin with *imagined* tasks, and *discovered* tasks make up "the true bulk of the project". Estimates don't show uncertainty, and status should be read from uphill/downhill, not task counts. The Skill should not average these. A defensible reading (INFERRED) is that EBS-style estimates apply to the *downhill* part of a de-risked slice, and discovered tasks are expected and recorded at Close.
- **Probabilistic scheduling scale.** EBS's Monte Carlo and ship-date distributions are team/project tools that need timesheet history. For a single slice, only the calibration core (estimate, actual, velocity) transfers directly.
- **Appetite ≠ estimate.** Shape Up explicitly contrasts them. EBS never mentions appetite. EBS's "box of wood blocks" (cut features or get a bigger box) is compatible with fixed-time/variable-scope but comes from the other direction.

## Provenance map
| Rule / example | Source | Classification | Source section |
|---|---|---|---|
| ≤16h tasks; small tasks force design | Spolsky, EBS | DIRECT | 1) Break 'er down |
| Velocity; perfect/bad/common estimator | Spolsky, EBS | DIRECT | 2) Track elapsed time |
| Discard old velocities; pessimistic default | Spolsky, EBS | DIRECT | 2) Track elapsed time |
| Monte Carlo, not sums | Spolsky, EBS | DIRECT | 3) Simulate the future |
| Only implementer estimates; don't badger | Spolsky, EBS | DIRECT | While we're at it 1, 3 |
| Estimates don't show uncertainty | Singer, Show Progress | DIRECT | Estimates don't show uncertainty |
| Estimate at top of hill | Singer, Show Progress | DIRECT | Work is like a hill |
| Appetite ≠ estimate | Singer, Set Boundaries | DIRECT | Fixed time, variable scope |
| Estimable = negotiated + size + team | Wake, INVEST | DIRECT | Estimable |
| Trust estimates only downhill | Singer, Show Progress | INFERRED | — |
| ESTIMATE-SYN-D01, D02 | — | DERIVED | — |
