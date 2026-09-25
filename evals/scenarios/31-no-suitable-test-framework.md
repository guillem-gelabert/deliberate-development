# 31 — No suitable test framework

**Skill:** `dd:execute` · **Behaviors:** EB-56, EB-53, EB-28 · **Grounding:** DERIVED preflight and non-TDD verification (methodology decision 10)

## Setup

A valid task workspace has `current_slice: S1`, `stage: execute`, and S1 `ready`. S1 says: "The production build excludes files under `examples/`." Its `Done when` requires a successful build and confirmation that `dist/` contains no example files. The slice's `Implementation notes` do not yet name a verification method.

The repository has `src/`, `examples/`, `scripts/build.js`, and `package.json` with only a `build` script (`node scripts/build.js`). The current build script copies both directories into `dist/`. `.github/workflows/ci.yml` runs `npm run build`. There is no test script, test framework, or nearby automated test. The change is confined to the build script.

## Prompt

"Implement S1."

## Expected

- [ ] Before changing the build script, inspects the package scripts, CI workflow, and relevant files; records the absence of a suitable test framework in S1's `Implementation notes` (EB-56).
- [ ] Defines the verification there before the change: run `npm run build`, then check that `dist/` has no example files (EB-56).
- [ ] Makes the build-script change, runs the chosen verification, and marks S1 done only after both `Done when` conditions pass (EB-56, EB-28).
- [ ] Does not silently install a test framework or ask the user to choose among routine verification commands (EB-56, EB-53).

## Failure signals

- A test framework is added solely to make this configuration change.
- Verification is chosen only after the build-script change, or the example-file check is skipped.
- The agent asks the user whether to run the existing build command.
