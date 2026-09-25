# Discovered scope and closing

Read when something unplanned appears, when a block ends, or when closing a slice. Tags: **[DIRECT: author]**, **[INFERRED: author]**, **[DERIVED]**.

## Grounding

- Discovered tasks are expected. They make up "the true bulk of the project", and lists grow as the work progresses. [DIRECT: Singer, *Hand Over Responsibility* / *Show Progress*]
- Capture new tasks without disrupting the current block, and process them later. [DIRECT / INFERRED: Newport, *Time-Block Planner*]
- Fix bugs in new code as you find them, and charge the time to the original task. [DIRECT: Spolsky]
- QA findings are nice-to-haves by default. Promote the must-haves. [DIRECT: Singer, *Decide When to Stop*]
- Before accepting new work mid-slice, ask: is there time for this? [DIRECT: Singer]
- Cutting scope is not lowering quality. [DIRECT: Singer]

Policy, which reconciles these (see the table in SKILL.md): **blocking → handle or re-plan now; non-blocking → capture as discovered work.** [DERIVED]

## Discovered-work entries

```markdown
## Discovered work

- [ ] D3 — Comment serializer exposes author_email in list responses (found during S1 implement; blocking: no; likely privacy bug → ask owner for priority)
- [ ] D4 — ~ Sort comments by edited time (found during S1; blocking: no; nice-to-have)
```

`~` marks a nice-to-have. [DIRECT: Singer] Entries do not become slices until `dd:shape` or the user promotes them.

## Contrastive examples [DERIVED]

**Unrelated bug**
- Preferred: while making "owner deletes comment" pass, you notice the serializer leaks `author_email`. Add D3 and continue the current test.
- Discouraged: dropping the red test to rewrite the serializer "while we're here".

**Blocking bug**
- Preferred: the existing `canEdit()` helper, which S1 reuses, returns true for any signed-in user. S1's "non-owner gets 403" example cannot pass without fixing it. Fix it inside S1, add a regression test, and note it in the slice's implementation notes and the actual.
- Discouraged: stubbing `canEdit()` to return the right answer in tests so the example goes green. That fakes the behavior under test.

**New requirement**
- Preferred: while implementing, you learn deleted comments must stay visible to moderators. Record it in `SPEC.md` → Open questions and ask. If the answer changes S1's behavior, set S1 `blocked` until it is answered.
- Discouraged: quietly adding a moderator view to S1.

**Block overrun**
- Preferred: the block ends with two test-list items left. One is known and must-have, so allocate a new block tomorrow and record it. The other hides an unknown, so return it to `dd:shape` as a spike.
- Discouraged: carrying on into the evening "because it's almost done", with no record.

## Closing a slice or block

1. Verify by running tests and checks, and each `Done when` item. A claim without a run does not count when a run is possible.
2. Is it better than the baseline? Compare against what users have today, not against the ideal. [DIRECT: Singer]
3. Reconcile documents. Corrected facts go to `CURRENT_STATE.md`. Requirement changes go to `SPEC.md` (labeled). Design drift goes to `ARCHITECTURE.md`; mark known contradictions `stale`, and unconfirmed material needing reconciliation `review-needed`.
4. Record the actual: real elapsed time. Keep interruptions and in-slice bug fixes inside it, and do not "correct" for them, so calibration reflects reality. [DIRECT: Spolsky] Compare it with the estimate. If time was not tracked, say "not tracked" rather than inventing a number.
5. Triage discovered items: must-have for this task (propose a new slice), nice-to-have (`~`), or out of scope. Ask about each: could we ship without it, and what happens if we don't do it? [DIRECT: Singer, scope hammering]
6. Set the slice state, run the validator, and write one concrete `Next`.

Example record [DERIVED]:
```markdown
**Actual:** 12.5h over 3 blocks (incl. 1.5h rounding bug in this slice's code, 1h support call not paused). Estimate 8h raw → velocity 0.64.
```

The structured close/reconciliation procedure is thinly grounded. Only estimate-vs-actual and scope triage come from sources; the rest is DERIVED.
