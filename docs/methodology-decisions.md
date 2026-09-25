# Methodology decisions

Where the sources disagree, and what this skillset does about it. Source conflicts are recorded, not averaged away: the adaptation is labeled as this skillset's decision (DERIVED), and the sources keep their own positions.

IDs refer to `research/synthesis/provenance-index.md`. Labels: **DIRECT** (explicit in the source), **INFERRED** (conservative restatement), **DERIVED** (created for this skillset).

## Stage mapping

The research corpus is organized around eight stages. The skillset groups them into three stage skills, plus `dd:state`, which maps to no research stage.

| Research stage (`research/synthesis/`) | Skill | Notes |
|---|---|---|
| Orient (`orient.md`) | `dd:ground` → context | Weakest-grounded stage (see below). |
| Clarify (`clarify.md`) | `dd:ground` → requirements | Well grounded. |
| De-risk (`derisk.md`) | `dd:shape` → architecture risk check, slice readiness/risk check | Research places one de-risk step after slicing. The skillset runs two checks in a loop (see decision 7). DERIVED ordering. |
| Slice (`slice.md`) | `dd:shape` | Well grounded. |
| Estimate (`estimate.md`) | `dd:execute` → prepare | Estimates only the current, de-risked slice. |
| Commit (`commit.md`) | `dd:execute` → prepare | Appetite and block allocation. |
| Implement (`implement.md`) | `dd:execute` → implement | Strongest-grounded stage. |
| Close (`close.md`) | `dd:execute` → close | Retrospective part is thin. |

The three-stage split, the five task files, `STATUS.md` as a cached cursor, the resume/checkpoint protocol, and the whole of `dd:state` are DERIVED. No source discusses agent state across sessions (see decision 9).

## Source conflicts and adaptations

### 1. Up-front decomposition

- **Spolsky** (DIRECT, ESTIMATE-EBS-01/-02/-03/-14): break work into tasks of 16 hours or less up front. Small tasks force you to design the feature. A multi-week task means the steps have not been thought through.
- **Singer** (DIRECT, CLOSE-HANDOVER-04, ESTIMATE-HILL-01/-02): teams start with imagined tasks. Discovered tasks are "the true bulk of the project". Estimates don't show uncertainty. A to-do list with nothing open can mean tasks have not been discovered yet.
- **Adaptation** (DERIVED): `dd:shape` identifies behavioral slices ahead of time. `dd:execute` estimates only the current or near-term slice once it is understood, and breaks only that slice into concrete tasks. No one fabricates a complete implementation task list to make the project look predictable. Discovered tasks are expected and recorded.

### 2. Refactoring after green

- **Beck** (DIRECT, IMPLEMENT-BECK-07, -N08, -N09): refactoring is *optional* per cycle. Refactoring further than the session needs, and abstracting too soon, are named mistakes.
- **Fowler** (DIRECT, IMPLEMENT-FTDD-06): neglecting the refactor step is "the most common way" to screw up TDD, ending in "a messy aggregation of code fragments".
- **Adaptation** (DERIVED): after each green, inspect the code just written for an actual design problem (duplication that obscures intent, a misleading name, a tangled conditional). Refactor when there is one. Do not refactor ceremonially. "Optional" never means "skip the look".

### 3. Replanning and time boxes

- **Newport** (DIRECT, COMMIT-TBLOCK-03, COMMIT-TBP-02): when knocked off the schedule, build an updated schedule for the rest of the day. The goal is intention, not perfection.
- **Shape Up** (DIRECT, COMMIT-BOUND-06, COMMIT-STOP-08/-09): fixed time, variable scope. The time box is a circuit breaker. Extend only when the remaining work is must-have *and* downhill.
- **Adaptation** (DERIVED): the broader schedule (which block happens when) may be rebuilt freely. The current block's allocation is not silently extended because work grew. At the stop condition: finish, cut scope, or explicitly allocate another block and record it.

### 4. Bugs discovered mid-work

- **Spolsky** (DIRECT, IMPLEMENT-EBS-01): fix bugs as you find them, and charge the time to the original task.
- **Newport** (DIRECT, IMPLEMENT-TBP-01/-02): capture new tasks without disrupting the current block.
- **Shape Up** (DIRECT, CLOSE-STOP-07): QA findings are nice-to-haves by default.
- **Adaptation** (DERIVED, refining the INFERRED reading in `implement.md`): if the bug blocks or invalidates the current slice (including bugs in the slice's own new code), fix it now and count the time in the slice's actual. Otherwise record it in `PLAN.md` → Discovered work and continue. Never silently absorb unrelated repair work.

### 5. Hard-coding and stubbing

- **Wake / Singer** (DIRECT, SLICE-INDEP-07, SLICE-ONEPIECE-05, IMPLEMENT-ONEPIECE-P02): hard-code or stub prerequisites (accounts, login, setup) to reach the interesting part first.
- **Beck / Fowler** (DIRECT, IMPLEMENT-BECK-05/-N05/-N06, CLARIFY-SBE-05): make the test pass for real. Deleting assertions or pasting computed values defeats the check. Examples can be satisfied by hard-coded responses, which is exactly what must not count.
- **Adaptation** (DERIVED): stubbing a *dependency or deferred prerequisite* is allowed when the slice still exercises its target behavior, and the stub is recorded in the slice's implementation notes. Faking *the behavior under test* (returning the expected literal, special-casing the test input, weakening assertions) is never done.

### 6. Appetite vs estimate vs deadline

- **Shape Up** (DIRECT, COMMIT-BOUND-02/-03, ESTIMATE-BOUND-05): appetite is a time budget that shapes the design. It starts from a number and ends with a design. An estimate starts from a design and ends with a number.
- **Spolsky** (DIRECT, COMMIT-EBS-02/-04): if it doesn't fit, get a bigger box or remove blocks. Never pretend to shrink the blocks.
- **Adaptation** (DERIVED): three separate records. The **estimate** is a prediction of effort. The **block** (timebox/appetite at hour scale) is a decision about how much time to spend now. The **deadline** is an external commitment and lives in `SPEC.md`. None of them is derived from another, and none is edited to fit another. Scaling appetite to hours is an adaptation. Shape Up defines only 1–2 week and 6-week batches.

### 7. Where de-risking happens

- **Shape Up** de-risks during shaping, before the bet (DERISK-RISK-01/-03), but also sequences uphill work first inside the cycle (DERISK-HILL-06).
- **Wake** places spikes inside the story flow (DERISK-SPLIT-02).
- **Research synthesis** orders Slice → De-risk (`derisk.md` entry condition: "a candidate slice exists").
- **Adaptation** (DERIVED): `dd:shape` iterates `architecture → architecture risk check → slice → slice readiness/risk check`.
  - The architecture risk check resolves unknowns that could change the design, feasibility, data or permissions, before any slicing rests on them. This is Singer's shaping-time de-risking.
  - The slice readiness check applies to individual slices (observable, end to end, independent, downhill, small, consistent with the architecture). It covers Wake's per-story spikes and the synthesis's slice-level de-risk.
  - A design-level finding from the slice check returns the loop to architecture. A slice-local finding becomes a re-slice or a spike slice. `dd:execute` refuses to estimate a slice that failed the readiness check.

### 8. What "done" requires

- **Wake** (DIRECT, CLOSE-INVEST-03): intended behavior, tests, refactored. **Shape Up** (DIRECT, CLOSE-HANDOVER-07): deployed. **Beck** (DIRECT, CLOSE-BECK-01): list empty, fear turned to boredom.
- **Adaptation** (DERIVED): a slice is `done` when every `Done when` box is checked and validated by running something (tests, a command, an observed behavior). Deployment is part of `Done when` only if `SPEC.md` says so.

### 9. Re-entry, adoption and the cached cursor

- **The corpus is silent.** No source discusses resuming an agent's work across sessions, adopting work already in progress into a method, reconciling a stale progress record, routing between stages, or checkpointing for a successor.
- **Adjacent ideas, not attributed.** Singer's orientation (ORIENT-HANDOVER-01/-02/-05: getting oriented is legitimate work and ends in a starting point) and hill charts (showing known vs unknown work) are loosely analogous to adoption and routing. Neither is about adopting started work or re-entering a workflow, so neither is cited as a source for these rules.
- **Adaptation** (DERIVED, all of it):
  - a fourth skill, `dd:state`, for state, next, resume, adopt and checkpoint (a fifth, `dd:help`, only explains the commands and carries no methodology);
  - the authority split: the substantive files plus the repository are authoritative, and `STATUS.md` is a cached cursor that is reconciled when evidence shows it is stale;
  - `review-needed` as a dependency-specific reconciliation gate for reconstructed or otherwise unconfirmed content; evidence can clear it without a ceremonial human review, while known contradictions are `stale`;
  - adoption by conservative backfill instead of replaying the workflow, with "reconstruct state from evidence, not fictional history" (inferred history is labeled Inferred, never Verified);
  - "route backward only as far as a material gap requires", and the routing table;
  - a model-independent task workspace: the files and repository, rather than a conversation or model's memory, carry progress across agents and sessions;
  - no retroactive estimates for adopted slices (this keeps the calibration log honest; the Spolsky rule about not inventing actuals still applies, IMPLEMENT-EBS-01/CLOSE-EBS-03).
- The evidence labels the adoption rules rely on predate this change and are equally DERIVED.

### 10. Test-environment preflight

- **TDD sources** (DIRECT, IMPLEMENT-BECK-03/-05 and IMPLEMENT-FTDD-01) describe writing a real failing test, making it and prior tests pass, and refactoring. They do not prescribe how to discover an unfamiliar repository's test setup.
- **Adaptation** (DERIVED): before implementing a ready or in-progress slice, `dd:execute` inspects nearby tests, the framework, scripts, CI checks, and local conventions. It records the chosen verification path. New testable behavior starts with a failing test when a suitable path exists; an in-progress slice resumes from tests already present. Without a suitable path, the agent records the gap and defines proportionate verification before changing code; it does not silently add a framework or ask about routine implementation judgment.

### 11. Interaction and command boundaries

- **Adaptation** (DERIVED): the five commands have separate entry intents. `dd:ground`, `dd:shape`, and `dd:execute` own stages; `dd:state` owns generic re-entry and adoption; `dd:help` explains and routes; it lists which workspaces exist but does not read or change task state. A stage command encountering started work without a workspace hands adoption to `dd:state`.
- **Adaptation** (DERIVED): resolve technical facts from evidence and decide routine implementation details without asking. When a material choice or adoption confirmation belongs to the user, use the environment's native interactive question tool if available, with short exclusive options; otherwise ask one concise inline question. An explicit adoption request already supplies consent, unless inspection reveals a new material ambiguity.
- **Adaptation** (DERIVED): follow applicable project instructions and conventions, including test, lint, branch and commit practices. Implementation intent alone does not authorize a commit, push or deployment; require a user or project instruction for those actions. This is an execution boundary, not a claim from the research corpus.

## Rules that remain DERIVED

The sources do not cover these. They are this skillset's policy and must not be attributed to an author.

- **Unfamiliar-codebase reconnaissance.** How to find relevant code, integrations, package/API contracts and analogous implementations, and what to write in `CURRENT_STATE.md`. Only fragments ground it: orientation is legitimate work (ORIENT-HANDOVER-01/-02), baseline (CLARIFY-BOUND-11), must-not-break behavior (CLARIFY-BECK-01). Grounding a requirement in current behavior before designing is an inference; the rest is DERIVED.
- **The requirement vs context split** inside `dd:ground`, and the ambiguity checklist (undefined terms, missing states, permissions, error behavior, migration). Clarify sources ground examples and narrowing; the checklist itself is DERIVED.
- **The ask-the-user threshold.** Resolve from evidence first. Ask only when the answer is material to observable behavior, scope, data handling, permissions or architecture.
- **Interactive questions and command boundaries.** The tool choice, inline fallback, `dd:help` orientation role, and separation of generic re-entry from explicit implementation are project interaction rules (decision 11).
- **Test-environment preflight.** Inspect existing verification conventions before implementation; the exact preflight is a project rule, not a claim from Beck or Fowler (decision 10).
- **Block goal + stop condition.** Newport gives no stop condition inside a block (see `gaps.md`). Assembled from appetite, Wake's time-boxed tasks and Beck's empty list.
- **Close / reconciliation.** Structured intent-vs-outcome review beyond estimate vs actual and scope triage is thin in the corpus.
- **Spike output format.** What a spike must produce (question, answer, consequence). The sources give only its purpose and Wake's "an hour or a day, rarely longer".
- **Solo-agent adaptation throughout.** Shape Up and Wake assume teams and customers; EBS assumes a team and timesheet history. Applying them to one agent/developer is an adaptation.
- **The task-state contract, resume protocol and validation script.**
- **`dd:state` as a whole** (decision 9): task adoption, stale-cursor reconciliation, routing, the checkpoint operation, and the stale-cursor warnings in `validate_work.py`.
- **The persistent calibration log** (`~/.deliberate-development/calibration.jsonl`): its location, schema, per-estimator filtering, append-only/correction rules and six-month window. The calibration core (velocity = estimate ÷ actual, discard data older than about six months, assume the worst under about six records, keep interruptions and bug time in the actual) is DIRECT from Spolsky (ESTIMATE-EBS-04/-05/-06, CLOSE-EBS-03, IMPLEMENT-EBS-01). The storage contract and its use by an agent are DERIVED.
- **The dd:shape loop and the slice readiness checklist** (decision 7).
- **Prompting principles** (`docs/prompting-principles.md`).

## Evidence-weak areas to revisit

From `research/synthesis/gaps.md`: codebase reconnaissance (Feathers, *Working Effectively with Legacy Code*), example selection (Adzic), picking the next test (Beck, *TDD by Example*), block shutdown (Newport, *Deep Work*), and retrospection. None of these are in the corpus. Adding one means new files in `research/sources/` and `research/extractions/` before any runtime rule changes.
