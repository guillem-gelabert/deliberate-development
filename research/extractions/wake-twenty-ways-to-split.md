# Twenty Ways to Split Stories

## Source
- Author: Bill Wake
- URL: https://xp123.com/twenty-ways-to-split-stories/
- Normalized copy: `sources/wake-twenty-ways-to-split.md` (tables rebuilt from HTML; linked PDF summary sheet not fetched)
- Relevant workflow stages: SLICE (primary), DERISK (research/spike splits)

Framing note: every row of the source table is an **Easier → Harder** pair of split dimensions. The "harder" side is not bad; it is the fuller version that is deferred. The contrastive pairs below preserve that framing.

## Core principles

### DIRECT
- **SLICE-SPLIT-01** Splitting separates high-value parts from low-value parts so time goes to the valuable parts. *(Intro)*
- **SLICE-SPLIT-02** Occasionally go the other way: combine stories so they become big enough to be interesting. *(Intro)*
- **SLICE-SPLIT-03** There is usually a lot of value in getting a minimal, end-to-end solution present, then filling in the rest. *(Intro)*
- **SLICE-SPLIT-04** Splits are grouped into four families: The Big Picture, User Experience, "Ilities", Features. *(The splits)*
- **DERISK-SPLIT-01** Research vs Action: researching how to do something is easier than doing it; if a story is too hard, one split is to spend time researching solutions. *(The Big Picture)*
- **DERISK-SPLIT-02** Spike vs Implementation: when developers lack a feel for how to do something — or for the dimensions along which to split — buy learning with a spike: a focused, hands-on experiment on some aspect of the system, lasting an hour or a day, "rarely longer." *(The Big Picture)*
- **SLICE-SPLIT-05** Manual vs Automated: use an existing manual process first (credit-check example — see P01). *(The Big Picture)*
- **SLICE-SPLIT-06** Buy vs Build, and Build vs Buy: buying can be much cheaper; but an off-the-shelf solution that fits poorly can cost more in customization than building. *(The Big Picture)*
- **SLICE-SPLIT-07** User Experience splits: batch before online; single-user before multi-user; API only before UI (e.g. first cut of a connection is a unit test calling connection objects); character/script UI before GUI; generic UI before custom UI. *(User Experience)*
- **SLICE-SPLIT-08** "Ilities" splits: static before dynamic; ignore errors before handle errors — but do not swallow exceptions, minimize recovery code; transient before persistent; low before high fidelity; unreliable before reliable; small before large scale; fewer non-functional requirements first (spikes as side projects to prove architecture). *("Ilities")*
- **SLICE-SPLIT-09** Features splits: few before many features; main flow (happy path) before alternate flows; 0 then 1 then many ("0, 1, infinity"); split condition before full condition; one level before all levels; base case before general case. *(Features)*
- **SLICE-SPLIT-10** Main flow usually carries the most value: "If you can't complete the most trivial transaction, who cares that you have great recovery if step 3 goes bad?" *(Features — Main flow)*
- **SLICE-SPLIT-11** Treat "and," "or," "then" and other connector words as opportunities to split; simplify a condition or do only one part of a multi-step sequence. *(Features — Split condition)*
- **SLICE-SPLIT-12** Splits are aids for moving forward in small steps; you must reassemble them to get full functionality; usually there is a narrow but high-value path through the system. *(Summary)*

### INFERRED
- **DERISK-SPLIT-03** Research/spike splits are a distinct kind of work from implementation: they buy information, are strictly short, and precede the implementing slice. *(from The Big Picture)*
- **SLICE-SPLIT-13** The general move in every row is: deliver the easier variant end-to-end first, and make the harder variant a later slice. *(from table structure + Intro)*
- **SLICE-SPLIT-14** "Ignore errors" is a scope reduction of recovery behavior, not permission to hide failures. *(from "Ilities" — Ignore errors)*

## Procedure / workflow
No procedure is presented. The source is a menu of split dimensions "may help give you ideas when you're looking for a way to move forward in small steps." *(Summary)*

INFERRED usage: when a story is too big or too hard, scan the dimensions; pick the split that yields a minimal end-to-end path; defer the harder variants; remember to reassemble.

## Decision rules and gates
- **DERISK-SPLIT-04** [DIRECT, The Big Picture] If a story is too hard, split off research; if you don't know how to do it or how to split it, run a spike (hour/day, rarely longer).
- **SLICE-SPLIT-15** [DIRECT, Features] If a story contains connector words ("and," "or," "then"), consider splitting on them.
- **SLICE-SPLIT-16** [DIRECT, Features] If a problem is recursive/multi-level, do the base case / one level first.
- **SLICE-SPLIT-17** [DIRECT, Intro] If a split makes stories too small to be interesting, combine them.
- **SLICE-SPLIT-18** [DIRECT, Summary] After splitting, check that the pieces reassemble into the full functionality.

## Questions the future agent could ask
- **DERISK-SPLIT-Q01** [INFERRED] Do we know how to do this? If not, what hour-to-day spike would tell us?
- **SLICE-SPLIT-Q02** [INFERRED] What is the main flow / happy path, and can it be delivered before any alternate flow?
- **SLICE-SPLIT-Q03** [INFERRED] Can we do 0 or 1 before many? One level before all levels? Base case before general?
- **SLICE-SPLIT-Q04** [INFERRED] Which connector words ("and," "or," "then") appear in the request, and what happens if we split there?
- **SLICE-SPLIT-Q05** [INFERRED] Is there an existing manual process, generic UI, API-only path or static version that suffices for the first slice?
- **SLICE-SPLIT-Q06** [INFERRED] What is the narrow but high-value path through the system?
- **SLICE-SPLIT-Q07** [INFERRED] Do the slices still add up to the full functionality?

## Positive examples from the source

### Example SLICE-SPLIT-P01 — Manual credit check first
**Classification:** DIRECT
**Source location:** The Big Picture — Manual vs Automated
**What happens:** A sales system needed credit checks; the first release routed requests to a group doing them manually; automated checks came later.
**Why it is positive:** The system released earlier, and the manual work was not throw-away — a manual process was always needed for borderline scores.
**Principle illustrated:** Manual before automated; release a narrow path early.

### Example SLICE-SPLIT-P02 — API-only first cut for a connection
**Classification:** DIRECT
**Source location:** User Experience — API only vs User Interface
**What happens:** Testing the ability to connect to another system, the first cut is a unit test calling the connection objects, no UI.
**Why it is positive:** Easier; proves the critical area without UI work.
**Principle illustrated:** API only before UI.

### Example SLICE-SPLIT-P03 — Low-to-high fidelity camera
**Classification:** DIRECT (credited to William Pietri)
**Source location:** "Ilities" — Low fidelity vs High fidelity
**What happens:** A digital camera could start as a 1-pixel black-and-white camera, then improve pixels, color depth and accuracy step by step.
**Why it is positive:** Breaks a feature down by quality of result along several axes.
**Principle illustrated:** Fidelity as a split dimension.

## Negative examples / anti-patterns from the source

### Example SLICE-SPLIT-N01 — Polishing recovery before the trivial transaction works
**Classification:** DIRECT (as a rhetorical counterexample)
**Source location:** Features — Main flow vs Alternate flows
**What happens:** Great recovery for "step 3 goes bad" while the most trivial transaction can't be completed.
**Why it is negative:** The main flow carries the most value.
**Principle violated:** Main flow first.

### Example SLICE-SPLIT-N02 — Swallowing exceptions under "ignore errors"
**Classification:** DIRECT (warning)
**Source location:** "Ilities" — Ignore errors vs Handle errors
**What happens:** Treating "ignore errors" as swallowing exceptions.
**Why it is negative:** The source says it "doesn't mean you should swallow exceptions"; only recovery code is minimized.
**Principle violated:** Scope-reduce, don't hide failures.

### Example SLICE-SPLIT-N03 — Poorly fitting off-the-shelf solution
**Classification:** DIRECT
**Source location:** The Big Picture — Build vs Buy
**What happens:** Customizing an off-the-shelf solution that is a poor match.
**Why it is negative:** That time might have been better spent building.
**Principle violated:** Choose buy/build by fit, not by default.

### Example SLICE-SPLIT-N04 — Splitting without reassembly
**Classification:** DIRECT (warning)
**Source location:** Summary
**What happens:** Splitting stories and forgetting they must be reassembled to get full functionality.
**Principle violated:** Splits serve the whole.

## Contrastive pairs
All pairs are DIRECT from the table; the "later" side is deferred, not discouraged.

### Pair DERISK-SPLIT-C01 — Research vs Action
**Earlier / easier:** Spend time researching solutions.
**Later / harder:** Do it (including whatever research it needs).
**Classification:** DIRECT
**Source location:** The Big Picture
**Distinguishing feature:** Output is knowledge, not the feature.

### Pair DERISK-SPLIT-C02 — Spike vs Implementation
**Earlier / easier:** A focused hands-on experiment, an hour or a day, rarely longer.
**Later / harder:** Implementation.
**Classification:** DIRECT
**Source location:** The Big Picture
**Distinguishing feature:** Short, bounded learning vs building.

### Pair SLICE-SPLIT-C03 — Manual vs Automated
**Earlier / easier:** Use the existing manual process (credit checks).
**Later / harder:** Automate.
**Classification:** DIRECT
**Source location:** The Big Picture

### Pair SLICE-SPLIT-C04 — Main flow vs Alternate flows
**Earlier / easier:** Happy path.
**Later / harder:** Alternate/recovery flows.
**Classification:** DIRECT
**Source location:** Features

### Pair SLICE-SPLIT-C05 — 0 / 1 / Many; Base case vs General case; One level vs All levels
**Earlier / easier:** 0, then 1; base case; one level.
**Later / harder:** Many; general case; all levels.
**Classification:** DIRECT
**Source location:** Features

### Pair SLICE-SPLIT-C06 — Split condition vs Full condition
**Earlier / easier:** One branch of an "and/or/then," or one step of a multi-step sequence.
**Later / harder:** The full condition/sequence.
**Classification:** DIRECT
**Source location:** Features

### Pair SLICE-SPLIT-C07 — Transient/Static/Single-user vs Persistent/Dynamic/Multi-user
**Earlier / easier:** Transient objects; compute once; single user.
**Later / harder:** Persistence mapping; keep values current; concurrency and accounts.
**Classification:** DIRECT
**Source location:** "Ilities"; User Experience

### Pair SLICE-SPLIT-C08 — Minimal end-to-end vs complete-first
**Good / preferred:** Get a minimal, end-to-end solution present, then fill in the rest.
**Bad / discouraged:** (Not stated in source.) DERIVED: build one part completely before anything works end-to-end.
**Classification:** DIRECT (good side) / DERIVED (bad side)
**Source location:** Intro

## Stop / go criteria

### GO
- A narrow, high-value, end-to-end path has been identified and the harder variants are deferred. *(Intro, Summary)*
- You know how to do the slice (otherwise spike first). *(The Big Picture)*

### STOP / RETURN
- Story too hard → split off research. *(Research vs Action)*
- Unclear how to do it or how to split it → spike (hour/day). *(Spike vs Implementation)*
- Slices too small to be interesting → combine. *(Intro)*
- Slices no longer reassemble into the whole → revisit. *(Summary)*

## Common failure modes
- Starting with alternate flows/recovery before the main flow works. *(Features)*
- Swallowing exceptions in the name of scope reduction. *("Ilities")*
- Spikes that run long ("rarely longer" than a day). *(The Big Picture)*
- Over-splitting into uninteresting fragments. *(Intro)*
- Forgetting reassembly. *(Summary)*

## Terms worth preserving
- `spike` — "a focused, hands-on experiment on some aspect of the system"; hour to a day, rarely longer.
- `research vs action` — learning how vs doing.
- `main flow` / `alternate flows` — use-case terms; happy path vs variations.
- `0, 1, infinity` — the easiest three values to handle.
- `connectors` — "and," "or," "then" as split points.
- `ilities` — non-functional qualities (reliability, scale, fidelity, performance).
- `narrow but high-value path` — the minimal valuable route through the system.

## Candidate Skill rules
- `[DERIVED from Intro]` Before implementing, identify a minimal end-to-end path and defer everything else to later slices.
- `[DERIVED from The Big Picture]` If you do not know how to do the slice, stop and run a spike of at most a day with a stated question; do not call it implementation.
- `[DERIVED from Features — Main flow]` Deliver the happy path before alternate or error-recovery flows.
- `[DERIVED from Features — Split condition]` Scan the request for "and," "or," "then"; each is a candidate split point.
- `[DERIVED from Features — 0/1/Many, Base case]` Start with zero/one items, one level, or the base case before collections, all levels, or the general case.
- `[DERIVED from "Ilities" — Ignore errors]` When deferring error handling, still surface errors; never swallow exceptions.
- `[DERIVED from Summary]` After splitting, list how the slices reassemble into the requested functionality.
- `[DERIVED from Intro]` If a slice is too small to be worth a verification cycle, merge it with its neighbor.

## Source limitations
- A menu of ideas, not a method: it does not say which dimension to pick first or how to judge value.
- Story-level and customer-oriented (XP teams); the value judgments assume a customer role.
- Spike duration ("an hour, or a day, rarely longer") is the only quantitative guidance; nothing on how to run or close a spike.
- Some examples are dated (Naked Objects, character UI) — the dimension still applies, the examples less so.
- The linked PDF summary sheet was not fetched.

## Derived developer examples

### Example SLICE-SPLIT-D01 — Form validation for a signup form
**Classification:** DERIVED
**Grounded in:** Wake SPLIT — Main flow vs Alternate flows; Split condition; Ignore vs Handle errors
**Discouraged:** First slice implements every rule (email format, password strength, uniqueness check, i18n messages, inline async validation) at once.
**Preferred:** Slice 1: required email + server-side "already registered" error shown on submit (main flow + one rule, errors surfaced but not polished). Later slices: password strength, inline async checks, localized messages.
**Distinguishing feature:** A working, tested path exists after the first slice; harder variants are deferred, not dropped.

### Example DERISK-SPLIT-D02 — Unfamiliar third-party shipping-rates API
**Classification:** DERIVED
**Grounded in:** Wake SPLIT — Spike vs Implementation; API only vs UI
**Discouraged:** Starting a "shipping options in checkout" ticket, discovering auth and rate-limit quirks midway through UI work.
**Preferred:** A ≤2-hour spike: one script calls the sandbox API for one address and prints rates; question answered: "can we get rates for a domestic address and what does auth need?" Then the first implementation slice is API-only (a service + unit test), UI after.
**Distinguishing feature:** Learning is bounded and labeled as a spike; the first implementation slice has no UI.

### Example SLICE-SPLIT-D03 — Bulk-archive endpoint
**Classification:** DERIVED
**Grounded in:** Wake SPLIT — 1 vs Many; Transient/Static first
**Discouraged:** Designing the batch job, progress reporting and partial-failure semantics before archiving a single item works.
**Preferred:** Slice 1: `POST /items/:id/archive` for one item; Slice 2: accept a list synchronously; Slice 3: background job and progress.
**Distinguishing feature:** One before many.

## ID register
| ID | Stage | Type | Short label | Classification | Location |
|---|---|---|---|---|---|
| SLICE-SPLIT-01 | SLICE | rule | Separate high from low value | DIRECT | Intro |
| SLICE-SPLIT-02 | SLICE | rule | Combine too-small stories | DIRECT | Intro |
| SLICE-SPLIT-03 | SLICE | rule | Minimal end-to-end first | DIRECT | Intro |
| SLICE-SPLIT-04 | SLICE | rule | Four split families | DIRECT | The splits |
| DERISK-SPLIT-01 | DERISK | rule | Research vs action | DIRECT | Big Picture |
| DERISK-SPLIT-02 | DERISK | rule | Spike: hour/day, rarely longer | DIRECT | Big Picture |
| SLICE-SPLIT-05 | SLICE | rule | Manual before automated | DIRECT | Big Picture |
| SLICE-SPLIT-06 | SLICE | rule | Buy vs build by fit | DIRECT | Big Picture |
| SLICE-SPLIT-07 | SLICE | rule | UX splits | DIRECT | User Experience |
| SLICE-SPLIT-08 | SLICE | rule | Ilities splits | DIRECT | "Ilities" |
| SLICE-SPLIT-09 | SLICE | rule | Feature splits | DIRECT | Features |
| SLICE-SPLIT-10 | SLICE | rule | Main flow most valuable | DIRECT | Features |
| SLICE-SPLIT-11 | SLICE | rule | Connector words | DIRECT | Features |
| SLICE-SPLIT-12 | SLICE | rule | Reassemble; narrow high-value path | DIRECT | Summary |
| DERISK-SPLIT-03 | DERISK | rule | Spike ≠ implementation | INFERRED | Big Picture |
| SLICE-SPLIT-13 | SLICE | rule | Easier variant first, harder later | INFERRED | table |
| SLICE-SPLIT-14 | SLICE | rule | Ignore errors ≠ hide failures | INFERRED | "Ilities" |
| DERISK-SPLIT-04 | DERISK | gate | Too hard → research/spike | DIRECT | Big Picture |
| SLICE-SPLIT-15 | SLICE | gate | Connectors → split | DIRECT | Features |
| SLICE-SPLIT-16 | SLICE | gate | Base case first | DIRECT | Features |
| SLICE-SPLIT-17 | SLICE | gate | Too small → combine | DIRECT | Intro |
| SLICE-SPLIT-18 | SLICE | gate | Check reassembly | DIRECT | Summary |
| DERISK-SPLIT-Q01 | DERISK | question | What spike would tell us? | INFERRED | Big Picture |
| SLICE-SPLIT-Q02 | SLICE | question | Main flow first? | INFERRED | Features |
| SLICE-SPLIT-Q03 | SLICE | question | 0/1, one level, base case? | INFERRED | Features |
| SLICE-SPLIT-Q04 | SLICE | question | Connector words? | INFERRED | Features |
| SLICE-SPLIT-Q05 | SLICE | question | Manual/generic/API-only/static first? | INFERRED | table |
| SLICE-SPLIT-Q06 | SLICE | question | Narrow high-value path? | INFERRED | Summary |
| SLICE-SPLIT-Q07 | SLICE | question | Do slices reassemble? | INFERRED | Summary |
| SLICE-SPLIT-P01 | SLICE | positive | Manual credit check | DIRECT | Big Picture |
| SLICE-SPLIT-P02 | SLICE | positive | API-only connection test | DIRECT | User Experience |
| SLICE-SPLIT-P03 | SLICE | positive | Low→high fidelity camera | DIRECT | "Ilities" |
| SLICE-SPLIT-N01 | SLICE | negative | Recovery before trivial transaction | DIRECT | Features |
| SLICE-SPLIT-N02 | SLICE | negative | Swallowing exceptions | DIRECT | "Ilities" |
| SLICE-SPLIT-N03 | SLICE | negative | Ill-fitting off-the-shelf | DIRECT | Big Picture |
| SLICE-SPLIT-N04 | SLICE | negative | Splitting without reassembly | DIRECT | Summary |
| DERISK-SPLIT-C01 | DERISK | pair | Research vs action | DIRECT | Big Picture |
| DERISK-SPLIT-C02 | DERISK | pair | Spike vs implementation | DIRECT | Big Picture |
| SLICE-SPLIT-C03 | SLICE | pair | Manual vs automated | DIRECT | Big Picture |
| SLICE-SPLIT-C04 | SLICE | pair | Main vs alternate flows | DIRECT | Features |
| SLICE-SPLIT-C05 | SLICE | pair | 0/1/many, base/general, levels | DIRECT | Features |
| SLICE-SPLIT-C06 | SLICE | pair | Split vs full condition | DIRECT | Features |
| SLICE-SPLIT-C07 | SLICE | pair | Transient/static/single vs full | DIRECT | Ilities; UX |
| SLICE-SPLIT-C08 | SLICE | pair | Minimal end-to-end vs complete-first | DIRECT/DERIVED | Intro |
| SLICE-SPLIT-D01 | SLICE | derived example | Signup form validation | DERIVED | — |
| DERISK-SPLIT-D02 | DERISK | derived example | Shipping-rates API spike | DERIVED | — |
| SLICE-SPLIT-D03 | SLICE | derived example | Bulk-archive endpoint | DERIVED | — |
