# 17 — "What next?" with several future slices

**Skill:** `dd:state` (next) · **Behaviors:** EB-42, EB-39, EB-40 · **Grounding:** DERIVED

## Setup

`PLAN.md`: S1 and S2 are `done`, S3 "Customer sees shipping rates for a domestic address" is `in-progress`, and S4–S7 are `candidate`/`ready`. S3's implementation notes contain a test list with three of five items checked. The next unchecked item is "rates sorted by price". The repository matches: the tests for the checked items pass, and no test for sorting exists yet. `STATUS.md` agrees.

## Prompt

"What should I do next?"

## Expected

- [ ] Returns one concrete action, for example: "Write a failing test in tests/rates.spec.ts that the rates for a domestic address come back sorted by price, then make it pass in RatesService." (EB-42)
- [ ] Does not list S4–S7 or give a plan overview unless asked (EB-42).
- [ ] Checks the claim against the tests before answering, rather than echoing `STATUS.md` (EB-39).
- [ ] Changes no files, because nothing was stale.

## Failure signals

- "Continue implementing S3."
- A bulleted walkthrough of every remaining slice.
