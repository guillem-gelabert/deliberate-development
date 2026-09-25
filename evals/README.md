# Evals

Markdown scenarios for checking that the skills produce the intended behavior, and for comparing models (GPT-5.6 Sol, Claude Opus 5.5) on the same cases. There is no harness yet. Each scenario is a fixture plus a checklist a human or grader model can apply to a transcript and the resulting task files.

## Layout

- `expected-behaviors.md` — the catalog of observable behaviors (`EB-xx`) that scenarios cite.
- `scenarios/NN-*.md` — one case each: skill under test, setup, prompt, expected checks, failure signals.
- `results/` — dated run results, including the model, score, evidence, and limits of the run.

| # | Scenario | Skill | Key behaviors |
|---|---|---|---|
| 01 | Ambiguous ticket | dd:ground | EB-03, EB-04, EB-51, EB-05 |
| 02 | Unfamiliar relevant code path | dd:ground | EB-01, EB-06, EB-34 |
| 03 | Oversized / horizontal proposed plan | dd:shape | EB-10, EB-11, EB-12 |
| 04 | Hidden third-party API uncertainty | dd:shape | EB-13, EB-21 |
| 05 | Unresolved material dependency | dd:shape | EB-14, EB-04 |
| 06 | Interrupted halfway through dd:shape | dd:shape | EB-30, EB-31 |
| 07 | New requirement during implementation | dd:execute | EB-25, EB-07 |
| 08 | Unrelated bug during current slice | dd:execute | EB-23, EB-24 |
| 09 | Slice exceeds estimate / timebox | dd:execute | EB-20, EB-26 |
| 10 | Dependency stub vs faking target | dd:execute | EB-27, EB-28 |
| 11 | Slice readiness exposes a design problem | dd:shape | EB-16, EB-14 |
| 12 | Calibration at prepare and close | dd:execute | EB-36, EB-20, EB-29 |
| 13 | Existing half-implemented task, no workspace | dd:state (adopt) | EB-37, EB-47, EB-38, EB-32 |
| 14 | Stale `STATUS.md` | dd:state (resume); dd:execute | EB-39, EB-31 |
| 15 | Fresh conversation, workspace exists | dd:state (resume) | EB-40, EB-30, EB-39 |
| 16 | Architecture invalidated during implementation | dd:execute; dd:state | EB-31, EB-41, EB-06 |
| 17 | "What next?" with several future slices | dd:state (next) | EB-42, EB-39 |
| 18 | Checkpoint halfway through a slice | dd:state (checkpoint) | EB-43, EB-32, EB-33 |
| 19 | Backfilled architecture marked review-needed | dd:state (resume) | EB-44, EB-41, EB-39 |
| 20 | Generic resume vs explicit implementation | dd:state; dd:execute | EB-45, EB-30, EB-39 |
| 21 | Bare invocation, no workspace | dd:state (entry) | EB-46, EB-51, EB-40 |
| 22 | Explicit adoption request | dd:state (adopt) | EB-47, EB-37, EB-38 |
| 23 | Bare invocation, workspace exists | dd:state (state) | EB-48, EB-39, EB-44 |
| 24 | Which command should I use? | dd:help | EB-49 |
| 25 | Task next step vs command help | dd:state (next) | EB-50, EB-42 |
| 26 | Ambiguous task identity | dd:state (entry) | EB-51, EB-46, EB-47 |
| 27 | No interactive question tool | dd:state; dd:ground | EB-52, EB-46 |
| 28 | Routine implementation, no questions | dd:execute | EB-53, EB-22 |
| 29 | Stage skill hands adoption to dd:state | dd:execute → dd:state | EB-54, EB-46, EB-47 |
| 30 | Existing test and CI setup | dd:execute | EB-55, EB-22, EB-34 |
| 31 | No suitable test framework | dd:execute | EB-56, EB-53, EB-28 |

## Running a scenario

1. Build the setup in a scratch repository. The setup paragraph and inline fixtures are enough to recreate it. Keep the fixture repo small.
2. Install only the skill under test (from `dist/`), plus the others if the scenario spans stages.
3. Send the prompt in a fresh conversation.
4. Grade each `Expected` checkbox as pass/fail from the transcript, the task files and the diff. Run `validate_work.py` on the resulting workspace. A failure there fails EB-32.
5. Record results per model: `scenario, model, date, passed/total, failed EB IDs, notes`.

Grade observable behavior only. Wording, length and politeness are not graded.

## Adding scenarios

Add one when a real session shows a failure mode not covered here. Cite existing `EB-xx` IDs, or add a new one to `expected-behaviors.md`. Scenario claims about the sources should cite `research/synthesis/`.
