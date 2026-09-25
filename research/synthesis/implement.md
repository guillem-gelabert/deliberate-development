# Implement

## Purpose
Build the committed slice incrementally. Where TDD fits, use Canon TDD's inner loop: test list → one concrete test → make it pass → optionally refactor → repeat. Capture anything newly discovered without derailing the current step. TDD governs the inner loop only. It does not replace Clarify or Slice.

## Primary grounding sources
- Beck, *Canon TDD*: primary.
- Fowler, *Test Driven Development*: supporting.
- Fowler, *Given When Then*: supporting. Test structure; side-effect-free "then" checks.
- Singer, *Get One Piece Done*: supporting. Affordances before pixels; program just enough; hard-code what doesn't teach you anything.
- Newport, *Time-Block Planner*: supporting. Capture tasks without disrupting the current block.
- Spolsky, *EBS*: supporting. Fix bugs as found and charge them to the original task.

## Entry conditions
- Commit exit: goal, time block and stop condition stated.

## Agent questions
1. Does the test list contain behaviors only, with no implementation decisions? (INFERRED, IMPLEMENT-BECK-Q01)
2. Which single item becomes the next concrete, runnable test, and which one drives fastest to the important design point? (DIRECT, IMPLEMENT-BECK-03; INFERRED, IMPLEMENT-FTDD-Q01)
3. Does the test have a real assertion, with the expected value worked out independently of the code? (INFERRED, IMPLEMENT-BECK-Q02/Q03)
4. Are you making it pass, or refactoring? (Pick one.) (INFERRED, IMPLEMENT-BECK-Q04)
5. Did a new case come up? Add it to the list. Does it invalidate the work so far? If so, push on or start over. (DIRECT, IMPLEMENT-BECK-06/Q05)
6. Is this refactor needed for this session, or is it avoidance of the next hard test? (INFERRED, IMPLEMENT-BECK-Q06)
7. Does this new thing need doing now, or should it be captured for later? (INFERRED, IMPLEMENT-TBP-Q01)

## Rules
- **Start from a test list of behavioral variants, including existing behavior that must not break.** (DIRECT, CLARIFY-BECK-01; IMPLEMENT-FTDD-02)
- **Turn exactly one item into a real automated test** with setup, invocation and assertions. Try working backwards from the assertions. (DIRECT, IMPLEMENT-BECK-03/-14; IMPLEMENT-BECK-P03)
- **Decide the interface in the test. Decide implementation design in the refactor step.** (DIRECT, IMPLEMENT-BECK-02/-04; IMPLEMENT-FTDD-05)
- **Make it pass for real.** The new test and all previous tests must pass. (DIRECT, IMPLEMENT-BECK-05)
- **Add discovered cases to the list and cross off passing ones.** If a discovery invalidates earlier work, decide whether to push on or start over. Beck's tip: start over with a different test order. (DIRECT, IMPLEMENT-BECK-06/-15; IMPLEMENT-BECK-P02)
- **Keep refactoring as a separate step after green**, and only as far as needed for this session. Duplication is a hint, not a command. (DIRECT, IMPLEMENT-BECK-07/-16/-17)
- **Wire affordances before polish, and program just enough for the next step.** Hard-code anything that won't teach you something, e.g. HTTPAuth instead of full login. (DIRECT, IMPLEMENT-ONEPIECE-03/-04/-P02)
- **Capture new tasks or notes mid-block instead of switching to them.** (DIRECT, IMPLEMENT-TBP-01/-02)
- **Fix bugs in new code as you find them, and count the time against the original task.** (DIRECT, IMPLEMENT-EBS-01)

## Positive patterns
- A test list that begins "basic case, what if this service times out, what if the key isn't in the database yet…" (DIRECT, IMPLEMENT-BECK-P01)
- Starting over with a different test order after a test invalidates the approach. (DIRECT, IMPLEMENT-BECK-P02)
- A hard-coded HTTPAuth password let real interview data flow early. (DIRECT, IMPLEMENT-ONEPIECE-P02)

## Anti-patterns (Beck's explicit mistakes, all DIRECT)
- IMPLEMENT-BECK-N01: mixing implementation design decisions into the test list.
- IMPLEMENT-BECK-N02: the misreading "TDD just launches into coding", which misses the test list.
- IMPLEMENT-BECK-N03: writing tests without assertions just for coverage.
- IMPLEMENT-BECK-N04: converting the whole test list into concrete tests up front. This causes rework when the first test changes a decision, plus "depression and/or boredom".
- IMPLEMENT-BECK-N05: deleting assertions so a test pretends to pass.
- IMPLEMENT-BECK-N06: copying computed values into expected values. This defeats the double check.
- IMPLEMENT-BECK-N07: mixing refactoring into making the test pass ("two hats").
- IMPLEMENT-BECK-N08: refactoring further than this session needs, often to avoid the next scary test.
- IMPLEMENT-BECK-N09: abstracting too soon.
- IMPLEMENT-FTDD-N01 (Fowler): neglecting the refactor step, which ends in "a messy aggregation of code fragments".
- IMPLEMENT-GWT-N01 (Fowler): "then" checks with side effects.

## Contrastive examples

**IMPLEMENT-BECK-C01 (DIRECT pair):** one test at a time vs all tests written up front. The distinguishing feature is whether feedback from the first passing test can reshape later tests.

**IMPLEMENT-BECK-C02 (DIRECT pair):** making the test pass for real vs deleting assertions or pasting computed values.

**IMPLEMENT-SYN-D01: Handling a failing test** (DERIVED; grounded in IMPLEMENT-BECK-N05/N06, SBE double check IMPLEMENT-SBE-01)
- *Preferred:* The invoice total test fails, expecting 107.00 and getting 107.70. Recompute the expected value by hand from the example (100 + 7% VAT = 107.00). Find the rounding applied before tax, and fix the code.
- *Discouraged:* Paste 107.70 into the expectation "because that's what it returns".

**IMPLEMENT-SYN-D02: Discovered work mid-block** (DERIVED; grounded in IMPLEMENT-TBP-02, IMPLEMENT-BECK-06)
- *Preferred:* While making "owner deletes comment" pass, you notice the comment serializer leaks `author_email`. Write it on the capture list as a separate item, and add "non-owner gets 403" to the test list. Continue the current test.
- *Discouraged:* Drop the red test and start rewriting the serializer.

## Stop / return conditions
- A new test invalidates the approach → consider starting over with a different order. (DIRECT, IMPLEMENT-BECK-15)
- The time box's stop condition is hit with the test still red → stop and go to Close to re-plan. (DERIVED from Commit)
- A discovered item is outside this slice → capture it, don't implement it. (DIRECT, IMPLEMENT-TBP-02)

## Exit criteria
- The test list is empty, and your fear for the behavior has been "transmuted into boredom". (DIRECT, CLOSE-BECK-01/-02)
- Or the time box ended, and the state is recorded for Close.

## Unresolved tensions between sources
- **Refactoring emphasis. Recorded, not resolved.** Beck: refactoring is *optional*, and "refactoring further than necessary" is a named mistake. Fowler: neglecting the refactor step is "the most common way" to screw up TDD. Both warn about the same step from opposite sides.
- **Fix now vs capture for later.** EBS says fix bugs as you find them and charge the time to the original task. The Time-Block Planner says capture new tasks to avoid disrupting the block. Shape Up makes QA-found issues nice-to-haves by default. A defensible split (INFERRED) is that a bug *in the code of the current slice* gets fixed now, while anything else is captured.
- **Hard-coding.** Singer and Wake endorse hard-coding *prerequisites* (accounts, auth). Fowler notes that a supplier could satisfy example-based specs with hard-coded *responses*, and Beck forbids faking a pass. The difference is stubbing a dependency vs faking the behavior under test.
- **Beck's preface.** Canon TDD describes TDD. It does not prescribe it ("What follows is NOT how you should do TDD"). The Skill should apply it "where appropriate" and never label other workflows as TDD.

## Provenance map
| Rule / example | Source | Classification | Source section |
|---|---|---|---|
| Five-step loop | Beck, Canon TDD | DIRECT | summary; The Steps |
| One test at a time; mistakes N01–N09 | Beck, Canon TDD | DIRECT | 1–4 |
| Interface in test, implementation in refactor | Beck, Canon TDD | DIRECT | Interface/Implementation Split; 2; 4 |
| Test list first; sequencing; refactor neglect | Fowler, TDD | DIRECT | paras 2, 4 |
| Then checks side-effect free | Fowler, GWT | DIRECT | pre-condition para |
| Affordances first; program just enough | Singer, Get One Piece Done | DIRECT | Affordances…; Program just enough… |
| Capture without disrupting block | Newport, Time-Block Planner | DIRECT | A Closer Look |
| Fix bugs as found, charge to task | Spolsky, EBS | DIRECT | While we're at it 2 |
| IMPLEMENT-SYN-D01, D02 | — | DERIVED | — |
