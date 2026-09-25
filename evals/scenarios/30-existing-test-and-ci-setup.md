# 30 — Existing test and CI setup

**Skill:** `dd:execute` · **Behaviors:** EB-55, EB-22, EB-34, EB-53 · **Grounding:** DERIVED preflight (methodology decision 10); Beck/Fowler TDD loop

## Setup

A valid task workspace has `current_slice: S1`, `stage: execute`, and S1 `ready`. S1 says: "POST /profile with a blank display name returns 422 with `{ field: "displayName", code: "required" }`." Its `Done when` includes a passing API test. `Implementation notes` list the blank-name case but do not name a test file or command.

The repository already uses Node's built-in test runner. `package.json` has `test: node --test` and `lint: node --check src/api/profile.js`; `tests/api/profile.test.js` contains a passing accepted-name case using the exported `postProfile` function; `.github/workflows/ci.yml` runs the test and lint scripts. `src/api/profile.js` currently accepts a blank name. The existing test passes before the change.

## Prompt

"Implement S1."

## Expected

- [ ] Before changing `src/api/profile.js`, inspects `package.json`, the nearby test, and the CI workflow; identifies the existing test runner and naming/assertion style (EB-55, EB-34).
- [ ] Records the selected test file and command in S1's `Implementation notes` (EB-55).
- [ ] Adds one blank-name test to the existing suite, runs it, and observes failure because blank names are still accepted before changing production code (EB-55, EB-22).
- [ ] Makes the new and earlier tests pass, runs the relevant project checks, and verifies the `Done when` condition before marking S1 done (EB-22, EB-28).
- [ ] Does not install a new test framework, create a parallel harness, or ask the user which routine test command to use (EB-55, EB-53).

## Failure signals

- Production code changes before the existing verification setup is inspected or the new test is seen failing for the intended reason.
- A new test runner or parallel test directory appears despite the working Node test suite.
- `Implementation notes` do not say how the slice was verified.
