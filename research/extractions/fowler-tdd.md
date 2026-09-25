# Test Driven Development

## Source
- Author: Martin Fowler
- URL: https://martinfowler.com/bliki/TestDrivenDevelopment.html (original 2005-03-05; updated 2023-12-11)
- Normalized file: `sources/fowler-tdd.md`
- Relevant workflow stages: IMPLEMENT (primary); CLARIFY (weakly: interface-first thinking)

## Core principles

### DIRECT
- **IMPLEMENT-FTDD-01** — TDD guides development by writing tests, repeating three steps: write a test for the next bit of functionality; write functional code until it passes; refactor new *and old* code so it is well structured. *(opening)*
- **IMPLEMENT-FTDD-02** — Before red-green-refactor there is "a vital initial step": write out a list of test cases, pick one, apply red-green-refactor, then pick the next. *(para 2)*
- **IMPLEMENT-FTDD-03** — Sequencing tests is a skill: pick tests that drive quickly to the salient points in the design. *(para 2)*
- **IMPLEMENT-FTDD-04** — Add tests to the list as they occur to you during the process. *(para 2)*
- **IMPLEMENT-FTDD-05** — Test-first gives two benefits: self-testing code (functional code is only written in response to a test), and thinking about the interface first, which helps separate interface from implementation. *(para 3)*
- **IMPLEMENT-FTDD-06** — The most common way to screw up TDD is neglecting refactoring; without it you get "a messy aggregation of code fragments" (though tested). *(para 4)*
- **IMPLEMENT-FTDD-07** — Fowler points to Beck's Canon TDD as "the key online summary". *(Further Reading)*

### INFERRED
- **IMPLEMENT-FTDD-08** — Refactoring scope includes pre-existing code touched by the change, not only the new code ("both new and old code"). *(opening)*

## Procedure / workflow
DIRECT (presented as the process):
1. Write out a list of test cases.
2. Pick one.
3. Red: write a test for the next bit of functionality.
4. Green: write functional code until the test passes.
5. Refactor new and old code.
6. Pick the next; add new tests to the list as they occur.

## Decision rules and gates
- **IMPLEMENT-FTDD-09** — Write functional code only in response to making a test pass. *(para 3)* — DIRECT
- **IMPLEMENT-FTDD-10** — Choose the next test by how quickly it drives to salient design points. *(para 2)* — DIRECT
- **IMPLEMENT-FTDD-11** — Do not skip the refactor step. *(para 4)* — INFERRED (from "most common way to screw up")

## Questions the future agent could ask
- **IMPLEMENT-FTDD-Q01** — Which test on the list would drive us fastest to the salient point in the design? `[INFERRED]` *(para 2)*
- **IMPLEMENT-FTDD-Q02** — How will a caller use this? What is the interface? `[INFERRED]` *(para 3)*
- **IMPLEMENT-FTDD-Q03** — Now that it's green, is the new and old code well structured, or did we just add a fragment? `[INFERRED]` *(para 4)*

## Positive examples from the source
The source has no worked examples. It describes the process abstractly.

## Negative examples / anti-patterns from the source

### IMPLEMENT-FTDD-N01 — Neglecting the refactor step
**Classification:** DIRECT
**Source location:** para 4
**What happens:** Developers go red→green and move on without refactoring.
**Why it is negative:** Code becomes a messy aggregation of fragments. Fowler notes it's less painful than most design failures, because at least it has tests.
**Principle violated:** IMPLEMENT-FTDD-01, IMPLEMENT-FTDD-06.

## Contrastive pairs

### IMPLEMENT-FTDD-C01 — Full cycle vs. red-green only
**Good / preferred:** Red, green, then refactor new and old code.
**Bad / discouraged:** Red, green, next test (no refactor).
**Classification:** DIRECT (the bad side is named; the good side is the described process)
**Source location:** opening; para 4
**Distinguishing feature:** Whether structure is improved after each pass.

## Stop / go criteria

### GO
- A test list exists; one test picked (DIRECT).

### STOP / RETURN
- Green reached → don't move on until you've refactored (INFERRED from para 4).
- The source gives no overall termination criterion.

## Common failure modes
- Skipping refactoring (DIRECT, N01).

## Terms worth preserving
- `Red - Green - Refactor` — summary of the three repeated steps.
- `Test-First Programming` — XPE2's name for writing the test first.
- `SelfTestingCode` — code with its own tests; a benefit of test-first.

## Candidate Skill rules
- `[DERIVED from para 2]` Write the test list before the first red test; pick tests that reach the key design decisions early.
- `[DERIVED from para 3]` Use the first test to decide the interface (how the behavior is called) before implementing.
- `[DERIVED from para 4]` After green, make a refactoring decision explicitly; do not silently skip it.

## Derived developer examples

### IMPLEMENT-FTDD-D01 — New REST endpoint
**Classification:** DERIVED
**Grounded in:** Fowler TDD — interface-first thinking (IMPLEMENT-FTDD-05), refactor step (N01)
**Preferred:** First test calls `POST /projects/:id/archive` and asserts on the 204 and the archived flag. This fixes the route and payload before the handler exists. After green, extract the duplicated permission check shared with `/unarchive`.
**Discouraged:** Get each endpoint test green and move on. After six endpoints, each has its own copy-pasted permission check.

## Source limitations
- Very short. No worked examples, no stop criterion, no treatment of discovered work beyond "add to list".
- **Tension with Beck:** Fowler stresses the risk of *neglecting* refactoring. Beck makes it *optional* per cycle and warns against refactoring *too far*. Both views are preserved; the Skill should say both "don't skip the refactor decision" and "don't over-refactor", without claiming the sources agree on emphasis.
- No bearing on clarify/slice/estimate/commit stages beyond the test list.

## ID register
| ID | Stage | Type | Short label | Classification | Location |
|---|---|---|---|---|---|
| IMPLEMENT-FTDD-01 | IMPLEMENT | rule | Test / pass / refactor new+old | DIRECT | opening |
| IMPLEMENT-FTDD-02 | IMPLEMENT | rule | Test list first, pick one | DIRECT | para 2 |
| IMPLEMENT-FTDD-03 | IMPLEMENT | rule | Sequence to salient design points | DIRECT | para 2 |
| IMPLEMENT-FTDD-04 | IMPLEMENT | rule | Add tests to list as they occur | DIRECT | para 2 |
| IMPLEMENT-FTDD-05 | IMPLEMENT | rule | Benefits: self-testing code, interface first | DIRECT | para 3 |
| IMPLEMENT-FTDD-06 | IMPLEMENT | rule | Neglecting refactor = most common screw-up | DIRECT | para 4 |
| IMPLEMENT-FTDD-07 | IMPLEMENT | rule | Canon TDD is the key summary | DIRECT | Further Reading |
| IMPLEMENT-FTDD-08 | IMPLEMENT | rule | Refactor includes old code | INFERRED | opening |
| IMPLEMENT-FTDD-09 | IMPLEMENT | gate | Code only in response to a test | DIRECT | para 3 |
| IMPLEMENT-FTDD-10 | IMPLEMENT | gate | Choose next test by design salience | DIRECT | para 2 |
| IMPLEMENT-FTDD-11 | IMPLEMENT | gate | Don't skip refactor | INFERRED | para 4 |
| IMPLEMENT-FTDD-Q01 | IMPLEMENT | question | Which test reaches salient design fastest? | INFERRED | para 2 |
| IMPLEMENT-FTDD-Q02 | IMPLEMENT | question | What is the interface? | INFERRED | para 3 |
| IMPLEMENT-FTDD-Q03 | IMPLEMENT | question | Well structured after green? | INFERRED | para 4 |
| IMPLEMENT-FTDD-N01 | IMPLEMENT | negative | Neglecting refactor | DIRECT | para 4 |
| IMPLEMENT-FTDD-C01 | IMPLEMENT | pair | Full cycle vs red-green only | DIRECT | opening; para 4 |
| IMPLEMENT-FTDD-D01 | IMPLEMENT | derived | Endpoint interface-first + refactor | DERIVED | — |
