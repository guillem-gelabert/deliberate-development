# Orient

## Purpose
Understand the current state of the system and the problem before deciding what to change: how the relevant code works today, what behavior already exists and must keep working, and what users do today without the change. **This stage is the weakest-grounded in the public source set** (see `gaps.md`). Only fragments ground it, and most of them come from chapters about *other* stages.

## Primary grounding sources
- Singer, *Hand Over Responsibility*: "Getting oriented", "Imagined vs discovered tasks". This is the only source section explicitly about orientation.
- Singer, *Set Boundaries* / *Decide When to Stop*: `baseline` (what customers live with today). Supporting.
- Beck, *Canon TDD*: TDD starts "given a system & a desired change in behavior"; the test list includes existing behavior that must not break. Supporting.
- Singer, *Risks and Rabbit Holes*: walk a use case through "in slow motion". Supporting; it is a de-risking technique that also reveals current state.

## Entry conditions
- A raw request, bug report or idea exists (Singer's `raw idea`).
- The developer has not yet decided on a solution.

## Agent questions
1. Which parts of the existing code are relevant, and how do they work today? (INFERRED from ORIENT-HANDOVER-01, -Q08)
2. What does the user or customer do today without this change? What is the workaround? (INFERRED from CLARIFY-BOUND-11, CLOSE-STOP-Q05)
3. What existing behavior near this change must keep working? (DIRECT, CLARIFY-BECK-Q02)
4. Can you name a meaningful starting point yet, or are you still figuring out where to start? (INFERRED from ORIENT-HANDOVER-02, -08)
5. When did the requester actually hit the problem, and what were they doing? (DIRECT technique, CLARIFY-BOUND-Q03; it belongs to Clarify but often starts during orientation)

## Rules
- **Treat orientation as legitimate work.** Builders can't dive into a codebase and build immediately. They first learn the relevant code and find a starting point, sometimes through short dead ends. (DIRECT, ORIENT-HANDOVER-01/-02)
- **Say explicitly "I'm still figuring out how to start"** rather than hiding exploration behind fake progress. (DIRECT, ORIENT-HANDOVER-02, N05)
- **Orientation should end in a chosen starting point.** That starting point is real work on something meaningful and central that is small enough to finish end to end. (DIRECT, ORIENT-HANDOVER-05; ORIENT-HANDOVER-08 is INFERRED)
- **Record the current `baseline`**: what users have today. It is later used to judge "good enough". (DIRECT concept, CLARIFY-BOUND-11, CLOSE-STOP-01)
- **List existing behavior that must not break** as part of the behavioral analysis. (DIRECT, CLARIFY-BECK-01)
- Time-limit orientation. The source's team heuristic is that silence lasting past about three days deserves a check-in. (DIRECT for teams, ORIENT-HANDOVER-03/-11. Scaling it to a solo developer's hours is DERIVED.)

## Positive patterns
- The team's first days show no visible deliverables because each person is learning how the existing system works and which starting point is best. The source calls this legitimate. (ORIENT-HANDOVER-01)
- The first real work picked is central to the project and completable end to end in a few days. (ORIENT-HANDOVER-05 → SLICE-ONEPIECE-06)

## Anti-patterns
- Demanding visible progress too early pushes exploration underground. (DIRECT, ORIENT-HANDOVER-N05)
- Treating the request at face value without checking what is actually going wrong today. (DIRECT for Clarify, CLARIFY-BOUND-C03; its Orient reading is INFERRED)

## Contrastive examples

**ORIENT-SYN-D01: Adding an endpoint to an unfamiliar service** (DERIVED; grounded in ORIENT-HANDOVER-01/-05 and CLARIFY-BECK-01)
- *Preferred:* Spend a bounded block reading the router, an existing similar endpoint and its tests. Note which serializer and auth middleware it uses. Write down two existing behaviors the change could break. Name the first slice: "GET returns 404 for another user's resource, using the existing auth guard."
- *Discouraged:* Scaffold a new controller from memory straight away, then discover halfway through that the project has its own auth decorator and response envelope.
- *Distinguishing feature:* the preferred version ends orientation with a named starting point and a list of what must not break.

**ORIENT-SYN-D02: Browser-specific bug** (DERIVED; grounded in CLARIFY-BOUND-11 and ORIENT-HANDOVER-02)
- *Preferred:* Reproduce the bug in the affected browser and record the exact current behavior (the baseline) and the steps, before touching CSS.
- *Discouraged:* Start changing styles based on the ticket title, with no reproduction.

## Stop / return conditions
- You can't name any starting point after the orientation time block ends → say so explicitly and pick a spike (→ De-risk), rather than faking progress.
- Orientation shows the request is really a different problem → Clarify (narrow the problem).

## Exit criteria
- The relevant code areas are identified.
- Current behavior / baseline is written down.
- Existing behavior that must not break is listed.
- A candidate starting point is named, or the developer has explicitly said "I don't know where to start yet."

## Unresolved tensions between sources
- Shape Up puts orientation *after* commitment. The team is already inside a six-week bet when it orients. The loop in this Skill puts Orient *first*. Using Singer's orientation material before commitment is an adaptation.
- Shape Up says real understanding comes from doing real work. EBS says you must think through the steps up front, before estimating. The two disagree on how much understanding can be gained before touching code (see `estimate.md`).

## Provenance map
| Rule / example | Source | Classification | Source section |
|---|---|---|---|
| Orientation is legitimate work | Singer, Hand Over Responsibility | DIRECT | Getting oriented |
| Say "still figuring out how to start" | Singer, Hand Over Responsibility | DIRECT | Getting oriented |
| ~3 days before stepping in (team) | Singer, Hand Over Responsibility | DIRECT | Getting oriented |
| Orientation ends in a starting point | Singer, Hand Over Responsibility | INFERRED | Getting oriented; Imagined vs discovered |
| Baseline = current customer reality | Singer, Set Boundaries / Decide When to Stop | DIRECT | Case study: Defining "calendar"; Compare to baseline |
| List existing behavior that must not break | Beck, Canon TDD | DIRECT | 1. Test List |
| ORIENT-SYN-D01, D02 | — | DERIVED | — |
