# `dd:execute` preflight dry runs — 2026-09-25

These were isolated scratch runs against `skills/execute/SKILL.md`. The `dist/dd-execute.zip` copy of `SKILL.md` was byte-identical at review time, but the agents did not install the ZIP in fresh conversations. Scores are provisional: final artifacts and final checks were reviewed independently, while the red-before-green chronology comes from each agent's run report and `PLAN.md` notes rather than a preserved command transcript.

| Scenario | Model | Passed/total | Failed EB IDs | Result and evidence |
|---|---|---:|---|---|
| 30 — Existing test and CI setup | Codex subagent (`gpt-6-sol`, self-recorded) | 5/5 | None observed | Inspected package scripts, nearby test and CI; recorded `npm test`/`npm run lint` in S1. Reported an empty-name test failing with actual 201 before the implementation change. Final rerun: 3 tests passed, lint passed, and workspace validation found 0 warnings. No new test runner or harness. |
| 31 — No suitable test framework | Codex subagent (`gpt-6-sol`, self-recorded) | 4/4 | None observed | Inspected build script, package scripts and CI; recorded the missing test path and build/output check in S1. Reported a baseline output assertion failing because `examples/` was present. Final rerun: build passed, `dist/src/index.js` existed, `dist/examples/` did not, and workspace validation found 0 warnings. No framework added. |

The fixtures were under `/tmp/dd-preflight-existing-tests` and `/tmp/dd-preflight-no-tests`. The final checks were rerun with `npm test`, `npm run lint`, `npm run build`, an output assertion, and `python3 skills/ground/scripts/validate_work.py` for each workspace. The pre-change failure reports were not independently replayed because the runs had already updated their scratch source files.
