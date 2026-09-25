# TDD loop

Read when implementing test-first. Canon TDD is Beck's *description* of TDD, not a mandate ("What follows is NOT how you should do TDD"). Use it where behavior is testable, and do not label other workflows TDD. Tags: **[DIRECT: author]**, **[INFERRED: author]**, **[DERIVED]**.

## The loop [DIRECT: Beck, *Canon TDD*]

1. **Test list.** List the behavioral variants of this slice: the basic case, failures, missing data, and existing behavior that must not break. This is behavioral analysis, not implementation design.
2. **One test.** Turn exactly one item into a real, runnable, automated test, with setup, invocation and assertions. Working backwards from the assertion helps. The test decides the interface. Pick the item that drives fastest to the important design point. [DIRECT: Fowler, *TDD*]
3. **Red for the right reason.** Run the test and check that it fails because the behavior is missing, not because of a typo or setup error. [DERIVED wording of the red step]
4. **Green for real.** Make this test and all previous tests pass with the smallest sound change. Add cases you discover to the list instead of acting on them now.
5. **Inspect, then refactor if useful.** Implementation design decisions belong here. Make it run, then make it right. See the policy below.
6. Repeat until the list is empty and your fear about the behavior has turned to boredom.

## Refactor policy [DERIVED, reconciling two DIRECT positions]

Beck treats refactoring as optional per cycle, and names over-refactoring and premature abstraction as mistakes. Fowler calls neglecting the refactor step the most common way to get TDD wrong.

So: after every green, look at the code just written. Refactor when there is an actual design problem, such as duplication that obscures intent, a misleading name, a tangled conditional, or a test that is hard to read. Do not refactor for ceremony, do not go beyond what this slice needs, and treat duplication as a hint, not a command. Do not refactor while a test is red. One hat at a time.

## Anti-patterns [DIRECT: Beck unless noted]

- Implementation decisions mixed into the test list.
- The whole list converted into concrete tests up front. Early tests would have changed later ones.
- Tests without assertions, written for coverage.
- Deleting or weakening assertions to get to green.
- Copying the computed actual value into the expectation. This defeats the double check, because the expected value must come from the spec or example, worked out independently.
- Refactoring mixed into making a test pass.
- Refactoring further than this session needs, often to avoid the next scary test.
- Abstracting too soon.
- Skipping the post-green inspection entirely. [DIRECT: Fowler]
- "Then" checks with side effects. [DIRECT: Fowler, *Given When Then*]

If a new test invalidates the approach so far, consider starting over with a different test order. [DIRECT: Beck]

## Stub vs fake [DERIVED line; both sides DIRECT]

Stubbing prerequisites is endorsed: a hard-coded account, a fixed auth header, a canned response from a deferred or external service. [DIRECT: Singer, *Get One Piece Done*; Wake] Tests that pass by faking the target behavior are not passes. [DIRECT: Beck; Fowler, *Specification by Example*]

| Allowed: stub a dependency | Not allowed: fake the target |
|---|---|
| Slice "show shipping rates": the carrier client returns a fixed rate table from a fake, and the slice's code really selects, formats and displays the rates. | Slice "calculate VAT": `calculateVat()` returns `107.00` when the input is `100`. |
| Seeded test user instead of a real signup flow for "owner deletes comment". | `if (process.env.NODE_ENV === 'test') return true` in the permission check under test. |
| Record the stub in `Implementation notes`, with the slice that will replace it. | Loosen the assertion to `toBeDefined()` because the value was wrong. |

Example [DERIVED]: the invoice total test expects 107.00 and gets 107.70. Recompute the expected value by hand from the example (100 + 7% VAT = 107.00). Find the rounding that is applied before tax, and fix the code. Do not paste 107.70 into the expectation.

## Where TDD does not fit

For visual layout, exploratory spikes, build/config changes or unfamiliar framework boundaries, state the verification first (a command, a screenshot comparison, a manual check against a `Done when` item), then do the work, then perform the verification. [DERIVED; Beck explicitly declines to prescribe beyond TDD]
