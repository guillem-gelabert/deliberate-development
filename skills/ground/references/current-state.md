# Current state: bounded context investigation

Read when writing `CURRENT_STATE.md`. This is the weakest source-grounded part of the methodology. The only direct grounding is that orientation is legitimate work, that it should end in a starting point, and that existing behavior which must not break belongs in the analysis. Everything else here is **[DERIVED]**.

## What is grounded

- Orientation is real work. You cannot build immediately in an unfamiliar system. Say "still figuring out where to start" instead of faking progress. [DIRECT: Singer, *Hand Over Responsibility*]
- Orientation should end with a meaningful starting point. [INFERRED: Singer]
- List existing behavior near the change that must keep working. [DIRECT: Beck, *Canon TDD*]
- Record the baseline users have today. [DIRECT: Singer]

## Scope of the investigation [DERIVED]

Investigate a thing when not knowing it could change the design, the slice boundaries, or what must not break. Stop investigating a thread when further detail would not change any of those.

Cover, as relevant:

1. **Entry points and code path.** Where the behavior starts (route, handler, command, job, component) and the path to persistence or output. Follow real calls, not file names.
2. **Tests.** Which tests cover the path, how they are run, and what they pin down. Missing coverage is a finding.
3. **Integrations.** Which services, queues, webhooks or clients are involved, which side owns the contract, and how failures surface.
4. **Package and API contracts.** The installed version and the actual signature/behavior, from lockfiles, source, type definitions or the authoritative docs for that version. Training-data memory of an API is **Assumed** until checked.
5. **Data.** Schemas, migrations, invariants and existing data that constrains change.
6. **Configuration and environments.** Flags, env vars, per-environment differences that change behavior.
7. **Analogous implementations and conventions.** The closest existing feature built the same way, and the local patterns it uses (auth guards, error envelopes, serializers, state management). Design should follow these unless `SPEC.md` requires otherwise.
8. **Where authority lives.** Links to the docs, ADRs, owners or dashboards another agent should consult.

Reproduce reported bugs before recording their cause. Record the exact steps and observed result as the baseline.

## Recording [DERIVED]

- One fact per bullet, with its label and a re-checkable pointer: `path:line`, test name, command and output, doc URL with version.
- Put inferences next to the facts they come from, labeled **Inferred**.
- Put unknowns under `Unknowns`, each with how it could be resolved (read X, run Y, spike, ask Z).
- Do not write intended changes here. "We will add a column" belongs in `ARCHITECTURE.md`.

Contrast:

- Preferred: `Verified: saveProfile() in src/profile/api.ts:42 sends PUT /v2/profile; ProfileForm.vue:88 calls it on submit; covered by profile.spec.ts "saves name". Inferred: the v1 endpoint is unused by the web client (no call sites found by grep; mobile client not checked → Open).`
- Discouraged: `The frontend saves through the profile service.` No label and no pointer, so an inference reads as fact.

## When investigation will not converge

If after a bounded effort you cannot name where the change would start, or a contract can only be learned by running code against a real system, record it under `Unknowns` as a spike candidate for `dd:shape`. Do not keep reading indefinitely. [INFERRED: Singer, "say you're still figuring it out"; DERIVED threshold]
