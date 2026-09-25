# State reconciliation and routing

Read when `STATUS.md` disagrees with evidence, an artifact is `review-needed` or `stale`, or the next stage is unclear. These state and routing rules are **[DERIVED]** Deliberate Development workflow rules, not claims about Singer or other research authors.

## Inspect the dependency, not the whole document

Start with the action in `STATUS.md` and the current or next slice. For each relevant artifact marked `review-needed`, list the exact claims or sections the action needs. Trace each claim to the ticket, confirmed requirements, code, tests, authoritative docs or a focused probe. Record the evidence and update labels. If those claims are sufficiently verified and the artifact has no material uncertainty for the next stage, set its artifact state to `complete`. Other labeled uncertainty may remain and can be revisited when a later slice needs it. Do not send the whole document to a person for ceremonial review.

If a needed claim cannot be established, record the question in the artifact and `STATUS.md` → Open. Ask the user only for intent or a decision evidence cannot establish; route technical investigation to `dd:ground` context or design reconciliation to `dd:shape`. Do not execute a slice against a material unresolved claim.

`draft` means normal incomplete content. `review-needed` means content is present but its reliability is unconfirmed. `stale` means known evidence contradicts the artifact. For `stale`, name the contradicted section and evidence, repair only the affected part through its owning stage, and re-check dependent slices. A validator warning does not determine materiality.

## Stale cursor

Check whether the `Next` action already happened, whether `PLAN.md` states agree with tests/code, and what changed since `updated` (including uncommitted changes). Run the current slice's tests when their result decides progress. Correct `PLAN.md` and `STATUS.md` to the observed state; never change substance merely to match the cursor.

Example: `Next` says to add a failing validation test, but the test and partial implementation already exist. Read and run that test, record actual slice progress, and name the next unfinished action. A test's existence alone does not prove it passes or expresses a confirmed requirement.

If implementation contradicts `CURRENT_STATE.md`, correct the observed fact there. If an architecture assumption depends on the old fact, set `ARCHITECTURE.md` to `stale`, identify the affected decision and route to shaping. Preserve unaffected decisions and completed slices.

## Routing

Take the first material match. An unrelated Open item stays recorded and does not block the current slice.

| Observed state | `stage` / `step` |
|---|---|
| Material requirement ambiguity or user decision | `ground` / `requirements` |
| Current-system behavior needed next is unknown | `ground` / `context` |
| Desired/current state known; architecture unresolved or materially stale | `shape` / `architecture` |
| Current slice too large, risky or not ready | `shape` / `slice-readiness` |
| Ready slice, none in progress | `execute` / `prepare` |
| In-progress slice still valid | `execute` / `implement` |
| Every slice `done` or `dropped` | Run the `SPEC.md` acceptance examples; when verified, set `status: done` |

Example: an adopted `ARCHITECTURE.md` infers a shared error map from code. S2 depends on that design. Inspect the changed code, tests and affected interfaces. If the behavior and approach are supported, record the evidence and clear `review-needed`. If the shared map is merely a partial experiment and the required error semantics remain unclear, keep the relevant uncertainty open and route to `dd:shape` or `dd:ground`; do not continue S2 just because the file exists. An unrelated later 409 decision need not block S2.

At a checkpoint, put new facts and decisions in their own files, check only verified `Done when` boxes, preserve the remaining test list under the slice, and keep `STATUS.md` as a compact pointer to one next action.
