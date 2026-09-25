# Canon TDD

## Source
- Author: Kent Beck
- URL: https://newsletter.kentbeck.com/p/canon-tdd (published 2023-12-11)
- Normalized file: `sources/beck-canon-tdd.md`
- Relevant workflow stages: IMPLEMENT (primary), CLARIFY (test list as behavioral analysis), CLOSE (stop condition: list empty / fear → boredom)

## Core principles

### DIRECT
- **IMPLEMENT-BECK-01** — TDD is a *programming workflow* for changing the behavior of a system (which may be empty). Its intended result: everything that used to work still works; the new behavior works as expected; the system is ready for the next change; the programmer and colleagues feel confident in these points. *(Overview)*
- **IMPLEMENT-BECK-02** — Design has two flavors that should not be lumped together: how a behavior is *invoked* (interface) and how the system *implements* it. *(Interface/Implementation Split)*
- **CLARIFY-BECK-01** — The first step, given a system and a desired behavior change, is to list all expected variants of the new behavior — including cases where the change should not break existing behavior. This is "behavioral analysis", not implementation design. *(1. Test List)*
- **IMPLEMENT-BECK-03** — Write exactly one test at a time: "a really truly automated test, with setup & invocation & assertions". *(2. Write a Test)*
- **IMPLEMENT-BECK-04** — Interface decisions are made while writing the test; implementation decisions belong to the refactor step ("*Now* you get to make implementation design decisions"). *(2. Write a Test; 4. Optionally Refactor)*
- **IMPLEMENT-BECK-05** — Make the test (and all previous tests) pass *for real*. *(3. Make it Pass; summary step 3)*
- **IMPLEMENT-BECK-06** — Discovered cases go onto the Test List during red→green; they are not acted on immediately. When a test passes, mark it off the list. *(3. Make it Pass)*
- **IMPLEMENT-BECK-07** — Refactoring is *optional* per cycle and is its own step, after green. "Make it run, *then* make it right." *(3. Make it Pass; 4. Optionally Refactor)*
- **IMPLEMENT-BECK-08** — The order in which tests are picked is an important skill that comes with experience and significantly affects both the experience and the final result. *(2. Write a Test)*
- **CLOSE-BECK-01** — Loop until the Test List is empty; keep going "until your fear for the behavior of the code has been transmuted into boredom." *(5. Until the Test List is Empty)*
- **IMPLEMENT-BECK-09** — The post is descriptive, not prescriptive: "What follows is NOT how *you* should *do* TDD." Other workflows that work are fine; they just aren't Canon TDD. Critiques should target the actual workflow, not a strawman. *(Author's preface; Intro)*

### INFERRED
- **IMPLEMENT-BECK-10** — The test list is also the "done" criterion for the implementation loop: without it, you cannot tell when you are finished (inferred from Beck's rebuttal "You'll never know when you're done. Nope."). *(1. Test List)*
- **IMPLEMENT-BECK-11** — The value of TDD's validation depends on the expected value being produced independently of the code under test (the "double checking" Beck says copy-pasting defeats). *(3. Make it Pass)*
- **IMPLEMENT-BECK-12** — Speculative tests written ahead of feedback are a liability: early passing tests can invalidate assumptions baked into later ones. *(2. Write a Test)*

## Procedure / workflow

DIRECT — Beck presents this as the canonical workflow (summary at top of post):

1. Write a list of the test scenarios you want to cover.
2. Turn exactly one item on the list into an actual, concrete, runnable test.
3. Change the code to make the test (and all previous tests) pass, adding items to the list as you discover them.
4. Optionally refactor to improve the implementation design.
5. Until the list is empty, go back to #2.

Beck explicitly notes this "looks like a computer program but it's not" — it is written that way to communicate with programmers. *(The Steps)*

## Decision rules and gates
- **IMPLEMENT-BECK-13** — While listing tests, think only in behavior; defer internals. An implementation sketch "in Sharpie on a napkin" is allowed if needed, but "you might not really need it. Experiment." *(1. Test List)* — DIRECT
- **IMPLEMENT-BECK-14** — A test counts only if it is automated and has setup, invocation and assertions. Protip: try working backwards from the assertions. *(2. Write a Test)* — DIRECT
- **IMPLEMENT-BECK-15** — If a newly discovered test invalidates work already done (example: "there's no way to handle the case of an empty folder"), decide whether to push on or start over. Beck's protip: start over, but pick a different order to implement the tests. *(3. Make it Pass)* — DIRECT
- **IMPLEMENT-BECK-16** — Refactor only as far as necessary for this session. *(4. Optionally Refactor)* — DIRECT
- **IMPLEMENT-BECK-17** — Treat duplication as "a hint, not a command" when deciding whether to abstract. *(4. Optionally Refactor)* — DIRECT
- **CLOSE-BECK-02** — Stop gate: list empty *and* fear has turned into boredom. *(5.)* — DIRECT

## Questions the future agent could ask
- **CLARIFY-BECK-Q01** — What are all the expected variants of the new behavior (basic case, timeouts, missing data, …)? `[DIRECT]` *(1. Test List — Beck's own example variants)*
- **CLARIFY-BECK-Q02** — In what ways could this change break existing behavior, and are those on the list? `[DIRECT]` *(1. Test List)*
- **IMPLEMENT-BECK-Q01** — Is this list item about behavior, or have I slipped an implementation decision into it? `[INFERRED]` *(1. Test List — Mistake)*
- **IMPLEMENT-BECK-Q02** — Does this test have real assertions? What would the assertion be if I wrote it first? `[INFERRED]` *(2. Write a Test — protip + Mistake)*
- **IMPLEMENT-BECK-Q03** — Where did the expected value come from — independent reasoning, or copied from the code's output? `[INFERRED]` *(3. Make it Pass — Mistake)*
- **IMPLEMENT-BECK-Q04** — Am I making it pass, or am I refactoring? (Only one hat at a time.) `[INFERRED]` *(3. Make it Pass — Mistake)*
- **IMPLEMENT-BECK-Q05** — Does this newly discovered case invalidate what's done? If so, push on or start over with a different test order? `[DIRECT]` *(3. Make it Pass)*
- **CLOSE-BECK-Q01** — Is the list empty, and is there anything about this behavior I'm still afraid of? `[INFERRED]` *(5.)*
- **IMPLEMENT-BECK-Q06** — Is this refactor needed for this session, or am I avoiding the next scary test? `[INFERRED]` *(4. Optionally Refactor — Mistake)*

## Positive examples from the source

### IMPLEMENT-BECK-P01 — Test list as enumerated behavioral variants
**Classification:** DIRECT
**Source location:** 1. Test List
**What happens:** Beck illustrates the list: the basic case, then what if a service times out, what if the key isn't in the database yet, etc.
**Why it is positive:** It is behavioral analysis covering variants and edge conditions before coding starts.
**Principle illustrated:** CLARIFY-BECK-01, IMPLEMENT-BECK-10.

### IMPLEMENT-BECK-P02 — Start over with a different order
**Classification:** DIRECT
**Source location:** 3. Make it Pass
**What happens:** A discovered case ("no way to handle the case of an empty folder") invalidates prior work; Beck recommends starting over and choosing a different test order.
**Why it is positive:** Treats test order as a design lever and accepts rework rather than patching around a broken foundation.
**Principle illustrated:** IMPLEMENT-BECK-08, IMPLEMENT-BECK-15.

### IMPLEMENT-BECK-P03 — Work backwards from the assertions
**Classification:** DIRECT
**Source location:** 2. Write a Test (protip)
**What happens:** Beck suggests writing the assertion first and working backwards to setup and invocation.
**Why it is positive:** Keeps the test anchored on observable behavior.
**Principle illustrated:** IMPLEMENT-BECK-14.

## Negative examples / anti-patterns from the source

### IMPLEMENT-BECK-N01 — Mixing implementation design into the test list
**Classification:** DIRECT
**Source location:** 1. Test List — "Mistake"
**What happens:** While listing tests, the programmer also decides how internals will look.
**Why it is negative:** Beck says you list tests better when that's all you concentrate on; internals come later ("Chill.").
**Principle violated:** CLARIFY-BECK-01, IMPLEMENT-BECK-02.

### IMPLEMENT-BECK-N02 — "TDD just launches into coding"
**Classification:** DIRECT
**Source location:** 1. Test List
**What happens:** Critics (and practitioners) skip the list step, claiming TDD starts by coding and never knows when it's done.
**Why it is negative:** Beck says people "missed this step in the book"; the list is the initial step.
**Principle violated:** CLARIFY-BECK-01, IMPLEMENT-BECK-10.

### IMPLEMENT-BECK-N03 — Tests without assertions for coverage
**Classification:** DIRECT
**Source location:** 2. Write a Test — "Mistake"
**What happens:** Tests are written without assertions just to raise code coverage.
**Why it is negative:** A test needs setup, invocation *and* assertions.
**Principle violated:** IMPLEMENT-BECK-03, IMPLEMENT-BECK-14.

### IMPLEMENT-BECK-N04 — Converting the whole list into tests up front
**Classification:** DIRECT
**Source location:** 2. Write a Test — "Mistake"
**What happens:** All list items become concrete tests first, then are made to pass one at a time.
**Why it is negative:** If passing the first test changes a decision, all speculative tests need rework; and by test #6 with nothing passing, "Depression and/or boredom."
**Principle violated:** IMPLEMENT-BECK-03, IMPLEMENT-BECK-12.

### IMPLEMENT-BECK-N05 — Deleting assertions so the test pretends to pass
**Classification:** DIRECT
**Source location:** 3. Make it Pass — "Mistake"
**What happens:** Assertions are removed to get green.
**Why it is negative:** "Make it pass for real."
**Principle violated:** IMPLEMENT-BECK-05.

### IMPLEMENT-BECK-N06 — Copying computed values into expected values
**Classification:** DIRECT
**Source location:** 3. Make it Pass — "Mistake"
**What happens:** The actual output of the code is pasted into the test as the expected value.
**Why it is negative:** It "defeats double checking, which creates much of the validation value of TDD."
**Principle violated:** IMPLEMENT-BECK-11.

### IMPLEMENT-BECK-N07 — Mixing refactoring into making the test pass
**Classification:** DIRECT
**Source location:** 3. Make it Pass — "Mistake"
**What happens:** The programmer restructures code while trying to reach green.
**Why it is negative:** The "wearing two hats" problem; make it run, *then* make it right.
**Principle violated:** IMPLEMENT-BECK-07.

### IMPLEMENT-BECK-N08 — Refactoring further than necessary for this session
**Classification:** DIRECT
**Source location:** 4. Optionally Refactor — "Mistake"
**What happens:** Tidying continues past what's needed, partly because tidying feels good and facing the next (possibly unknown) test feels scary.
**Why it is negative:** It avoids the next test; Beck admits being stuck like this himself on a side project.
**Principle violated:** IMPLEMENT-BECK-16.

### IMPLEMENT-BECK-N09 — Abstracting too soon
**Classification:** DIRECT
**Source location:** 4. Optionally Refactor — "Mistake"
**What happens:** Duplication triggers immediate abstraction.
**Why it is negative:** "Duplication is a hint, not a command."
**Principle violated:** IMPLEMENT-BECK-17.

### IMPLEMENT-BECK-N10 — Critiquing a strawman
**Classification:** DIRECT
**Source location:** Author's preface; Intro
**What happens:** People say "TDD suckz" because of something that isn't TDD, e.g., "I hate writing all the tests before I write any code."
**Why it is negative:** That is not the canonical workflow (see N04); critique the actual thing.
**Principle violated:** IMPLEMENT-BECK-09.

## Contrastive pairs

### IMPLEMENT-BECK-C01 — One test at a time vs. all tests up front
**Good / preferred:** Turn exactly one list item into a runnable test, make it pass, then pick the next.
**Bad / discouraged:** Convert every list item into concrete tests, then make them pass one by one.
**Classification:** DIRECT
**Source location:** Steps summary #2; 2. Write a Test — Mistake
**Distinguishing feature:** Whether tests get written *after* feedback from earlier passes, or speculatively before any feedback.

### IMPLEMENT-BECK-C02 — Pass for real vs. fake pass
**Good / preferred:** Change the system so the test (and all previous tests) passes.
**Bad / discouraged:** Delete assertions, or paste computed values into expected values.
**Classification:** DIRECT
**Source location:** 3. Make it Pass
**Distinguishing feature:** Whether the test still independently checks the behavior.

### IMPLEMENT-BECK-C03 — Separate hats vs. two hats
**Good / preferred:** Get to green first, then (optionally) refactor.
**Bad / discouraged:** Refactor while making the test pass.
**Classification:** DIRECT
**Source location:** 3. Make it Pass — Mistake; 4. Optionally Refactor
**Distinguishing feature:** Whether behavior change and structure change happen in the same step.

### IMPLEMENT-BECK-C04 — Behavioral test list vs. design-laden list
**Good / preferred:** List behavior variants only (basic case, timeouts, missing key…) plus "don't break existing" cases.
**Bad / discouraged:** Decide internals while listing.
**Classification:** DIRECT
**Source location:** 1. Test List
**Distinguishing feature:** Whether list items describe observable behavior or internal structure.

### IMPLEMENT-BECK-C05 — Refactor enough vs. refactor to avoid the next test
**Good / preferred:** Refactor as needed for this session, then face the next test.
**Bad / discouraged:** Keep tidying, because the next test is scary; or abstract on first duplication.
**Classification:** DIRECT
**Source location:** 4. Optionally Refactor
**Distinguishing feature:** Whether the refactor serves the current design or postpones the next test.

## Stop / go criteria

### GO
- A system and a desired behavior change exist, and there is a test list (DIRECT, 1.).
- The next item has been chosen and can be expressed as one automated test with setup, invocation and assertions (DIRECT, 2.).
- After green: optionally refactor, then return to #2 (DIRECT, summary).

### STOP / RETURN
- A discovered case invalidates completed work → decide push on vs. start over; the protip is start over with a different order (DIRECT, 3.).
- New case discovered mid-step → add to list, don't chase it now (DIRECT, 3.).
- Refactoring going beyond this session's needs → stop and move on to the next test (DIRECT, 4.).
- List empty and fear turned to boredom → done (DIRECT, 5.).

## Common failure modes
All DIRECT; see N01–N10: design-laden test list; skipping the list; assertion-free tests; writing all tests up front; deleting assertions; copying computed values; refactoring during green; over-refactoring; premature abstraction; critiquing non-TDD as TDD.

## Terms worth preserving
- `Test List` — the list of expected behavioral variants of the change, including non-regression cases; edited throughout.
- `Canon TDD` — Beck's five-step workflow; other workflows may work but aren't Canon TDD.
- `interface vs implementation` (logical vs physical design) — invocation vs internals; tests drive the former, refactoring the latter.
- `double checking` — independent expected value vs. computed actual; the source of much of TDD's validation value.
- `wearing two hats` — mixing make-it-pass with refactoring.
- `fear → boredom` — Beck's subjective stopping condition.

## Candidate Skill rules
- `[DERIVED from 1. Test List]` Before writing code for a behavior change, write a test list of behavior variants and non-regression cases. Do not put implementation decisions on it.
- `[DERIVED from 2. Write a Test]` Write exactly one automated test with a real assertion at a time. Do not pre-write the rest of the list as tests.
- `[DERIVED from 3. Make it Pass]` Make the test pass by changing the system. Do not delete assertions or paste computed output into expected values.
- `[DERIVED from 3. Make it Pass]` If you discover a new case, add it to the list and keep going. If it invalidates completed work, stop and choose between pushing on and restarting with a different test order (prefer restarting).
- `[DERIVED from 3./4.]` Do not refactor while red. After green, refactor only as far as this session needs; treat duplication as a hint.
- `[DERIVED from 5.]` If the list is empty but uncertainty about the behavior remains, return to the list and add the cases you are afraid of.
- `[DERIVED from preface]` Present TDD as the default inner loop where it fits, not a mandate; do not describe "write all tests first" as TDD.

## Derived developer examples

### IMPLEMENT-BECK-D01 — Adding email validation to a signup form
**Classification:** DERIVED
**Grounded in:** Beck — Test List (behavior only), one test at a time (C01, C04)
**Preferred:** Test list: valid email accepted; empty field shows "required"; malformed address shows format error; whitespace trimmed; existing password-field validation still works. Write only the "empty field" test, make it pass, tick it, pick the next.
**Discouraged:** List reads "add a `validators/email.ts` with regex, wire into Formik schema"; five failing tests written up front; halfway through, the team switches validation libraries and all five need rewriting.

### IMPLEMENT-BECK-D02 — Changing an API response shape
**Classification:** DERIVED
**Grounded in:** Beck — double checking (N06), make it pass for real (N05)
**Preferred:** Expected JSON for `GET /orders/42` is written from the agreed contract (e.g. `total` in cents as integer) before running the code.
**Discouraged:** Run the endpoint, copy its output into the snapshot/expected value, and call the test green. That test only proves the code returns what it returns.

### IMPLEMENT-BECK-D03 — Handling a failing test mid-change
**Classification:** DERIVED
**Grounded in:** Beck — discovered cases go on the list; start over with different order (IMPLEMENT-BECK-15)
**Preferred:** While making "archive order" pass, you notice orders with pending refunds can't be archived. Add it to the list. If that breaks the archive model you built, revert and start with the refund case first.
**Discouraged:** Immediately branch off to build refund handling while the current test is still red, or comment out the failing assertion to get back to green.

## Source limitations
- Governs only the inner implementation loop; says nothing about how to arrive at the desired behavior change, slicing, estimation or time commitment.
- "Picking the next test" is declared a skill that comes with experience; no sequencing heuristics are given (open question: "is code sensitive to initial conditions?").
- The stop condition (fear → boredom) is subjective.
- Explicitly non-prescriptive ("NOT how *you* should *do* TDD"). A Skill that mandates it goes beyond the source's own framing.
- **Tension with Fowler (FTDD):** Beck makes refactoring *optional* per cycle and lists over-refactoring as a mistake; Fowler calls *neglecting* refactoring the most common way to screw up TDD. They can both hold (don't skip it; don't overdo it), but the sources stress opposite risks. Record both; do not merge them.
- No guidance on legacy code without tests, UI/browser-specific behavior, or where the test list lives relative to a story's acceptance criteria.

## ID register
| ID | Stage | Type | Short label | Classification | Location |
|---|---|---|---|---|---|
| IMPLEMENT-BECK-01 | IMPLEMENT | rule | TDD goals: old works, new works, ready for next, confidence | DIRECT | Overview |
| IMPLEMENT-BECK-02 | IMPLEMENT | rule | Interface vs implementation split | DIRECT | Interface/Implementation Split |
| CLARIFY-BECK-01 | CLARIFY | rule | Test list = behavioral analysis incl. non-regression | DIRECT | 1. Test List |
| IMPLEMENT-BECK-03 | IMPLEMENT | rule | One real automated test at a time | DIRECT | 2. Write a Test |
| IMPLEMENT-BECK-04 | IMPLEMENT | rule | Interface decisions in test; implementation in refactor | DIRECT | 2.; 4. |
| IMPLEMENT-BECK-05 | IMPLEMENT | rule | Make it pass for real (all prior tests too) | DIRECT | 3. Make it Pass |
| IMPLEMENT-BECK-06 | IMPLEMENT | rule | Add discovered cases to list; mark off passed | DIRECT | 3. Make it Pass |
| IMPLEMENT-BECK-07 | IMPLEMENT | rule | Refactor optional, separate step after green | DIRECT | 3.; 4. |
| IMPLEMENT-BECK-08 | IMPLEMENT | rule | Test order matters; skill from experience | DIRECT | 2. Write a Test |
| CLOSE-BECK-01 | CLOSE | rule | Loop until list empty; fear → boredom | DIRECT | 5. |
| IMPLEMENT-BECK-09 | IMPLEMENT | rule | Descriptive not prescriptive; critique actual thing | DIRECT | Preface; Intro |
| IMPLEMENT-BECK-10 | IMPLEMENT | rule | Test list defines "done" for the loop | INFERRED | 1. Test List |
| IMPLEMENT-BECK-11 | IMPLEMENT | rule | Validation needs independent expected values | INFERRED | 3. Make it Pass |
| IMPLEMENT-BECK-12 | IMPLEMENT | rule | Speculative tests are a rework liability | INFERRED | 2. Write a Test |
| IMPLEMENT-BECK-13 | IMPLEMENT | gate | Behavior only in list; napkin sketch optional | DIRECT | 1. Test List |
| IMPLEMENT-BECK-14 | IMPLEMENT | gate | Test needs setup/invocation/assertions; work back from asserts | DIRECT | 2. Write a Test |
| IMPLEMENT-BECK-15 | IMPLEMENT | gate | Invalidating discovery → push on or start over (prefer restart, new order) | DIRECT | 3. Make it Pass |
| IMPLEMENT-BECK-16 | IMPLEMENT | gate | Refactor only as far as needed this session | DIRECT | 4. |
| IMPLEMENT-BECK-17 | IMPLEMENT | gate | Duplication is a hint, not a command | DIRECT | 4. |
| CLOSE-BECK-02 | CLOSE | gate | Stop: list empty and fear is boredom | DIRECT | 5. |
| CLARIFY-BECK-Q01 | CLARIFY | question | All expected variants? | DIRECT | 1. |
| CLARIFY-BECK-Q02 | CLARIFY | question | What existing behavior could break? | DIRECT | 1. |
| IMPLEMENT-BECK-Q01 | IMPLEMENT | question | Behavior or implementation in list item? | INFERRED | 1. |
| IMPLEMENT-BECK-Q02 | IMPLEMENT | question | Real assertion? | INFERRED | 2. |
| IMPLEMENT-BECK-Q03 | IMPLEMENT | question | Expected value independent? | INFERRED | 3. |
| IMPLEMENT-BECK-Q04 | IMPLEMENT | question | Passing or refactoring? | INFERRED | 3. |
| IMPLEMENT-BECK-Q05 | IMPLEMENT | question | Discovery invalidates work → push on / restart? | DIRECT | 3. |
| CLOSE-BECK-Q01 | CLOSE | question | List empty and no fear left? | INFERRED | 5. |
| IMPLEMENT-BECK-Q06 | IMPLEMENT | question | Refactor needed or avoidance? | INFERRED | 4. |
| IMPLEMENT-BECK-P01 | IMPLEMENT | positive | Enumerated behavioral variants | DIRECT | 1. |
| IMPLEMENT-BECK-P02 | IMPLEMENT | positive | Start over, different order | DIRECT | 3. |
| IMPLEMENT-BECK-P03 | IMPLEMENT | positive | Work backwards from assertions | DIRECT | 2. |
| IMPLEMENT-BECK-N01 | IMPLEMENT | negative | Implementation design in test list | DIRECT | 1. Mistake |
| IMPLEMENT-BECK-N02 | IMPLEMENT | negative | "TDD just launches into coding" | DIRECT | 1. |
| IMPLEMENT-BECK-N03 | IMPLEMENT | negative | Assertion-free tests for coverage | DIRECT | 2. Mistake |
| IMPLEMENT-BECK-N04 | IMPLEMENT | negative | All list items to tests up front | DIRECT | 2. Mistake |
| IMPLEMENT-BECK-N05 | IMPLEMENT | negative | Delete assertions to pass | DIRECT | 3. Mistake |
| IMPLEMENT-BECK-N06 | IMPLEMENT | negative | Paste computed values as expected | DIRECT | 3. Mistake |
| IMPLEMENT-BECK-N07 | IMPLEMENT | negative | Refactor while making it pass | DIRECT | 3. Mistake |
| IMPLEMENT-BECK-N08 | IMPLEMENT | negative | Over-refactoring this session | DIRECT | 4. Mistake |
| IMPLEMENT-BECK-N09 | IMPLEMENT | negative | Abstracting too soon | DIRECT | 4. Mistake |
| IMPLEMENT-BECK-N10 | IMPLEMENT | negative | Strawman critique | DIRECT | Preface |
| IMPLEMENT-BECK-C01 | IMPLEMENT | pair | One at a time vs all up front | DIRECT | 2. |
| IMPLEMENT-BECK-C02 | IMPLEMENT | pair | Pass for real vs fake pass | DIRECT | 3. |
| IMPLEMENT-BECK-C03 | IMPLEMENT | pair | Separate hats vs two hats | DIRECT | 3.; 4. |
| IMPLEMENT-BECK-C04 | IMPLEMENT | pair | Behavioral vs design-laden list | DIRECT | 1. |
| IMPLEMENT-BECK-C05 | IMPLEMENT | pair | Enough refactor vs avoidance refactor | DIRECT | 4. |
| IMPLEMENT-BECK-D01 | IMPLEMENT | derived | Email validation test list | DERIVED | — |
| IMPLEMENT-BECK-D02 | IMPLEMENT | derived | API response expected values | DERIVED | — |
| IMPLEMENT-BECK-D03 | IMPLEMENT | derived | Discovered case mid-change | DERIVED | — |
