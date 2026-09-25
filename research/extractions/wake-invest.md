# INVEST in Good Stories, and SMART Tasks

## Source
- Author: Bill Wake
- URL: https://xp123.com/invest-in-good-stories-and-smart-tasks/
- Normalized copy: `sources/wake-invest.md`
- Relevant workflow stages: SLICE (primary), CLARIFY, ESTIMATE, DERISK (spike split), COMMIT (time-boxed tasks), CLOSE (task "done" measure)

## Core principles

### DIRECT
- **SLICE-INVEST-01** Good stories are Independent, Negotiable, Valuable, Estimable, Small, Testable. *(Intro list)*
- **CLARIFY-INVEST-01** A story has three components: Card (physical medium), Conversation (the discussion around it), Confirmation (tests that verify it). The card is not "the whole story." *(Intro, citing Ron Jeffries)*
- **SLICE-INVEST-02** Independent: stories should not overlap in concept and should be schedulable/implementable in any order — acknowledged as not always achievable (e.g. "3 points for the first report, then 1 point for each of the others"). *(Independent)*
- **CLARIFY-INVEST-02** Negotiable: a story is not an explicit contract; details are co-created by customer and programmer during development; it captures the essence, not the details. Notes and test ideas may accumulate but are not needed to prioritize or schedule. *(Negotiable… and Negotiated)*
- **SLICE-INVEST-03** Valuable: value must be to the customer; developer concerns must be framed so the customer perceives them as important. *(Valuable)*
- **SLICE-INVEST-04** When splitting, slice vertically through the layers (network, persistence, logic, presentation) so each slice delivers "the essence of the whole cake"; a full database layer alone has little customer value without presentation. *(Valuable)*
- **ESTIMATE-INVEST-01** Estimable: an estimate need only be good enough to rank and schedule. Estimability depends on (a) being negotiated/understood, (b) size — bigger is harder, (c) the team's experience. *(Estimable)*
- **DERISK-INVEST-01** A story may need to be split into a time-boxed spike that yields enough information for a decent estimate, plus the rest that implements the feature. *(Estimable, parenthetical)*
- **SLICE-INVEST-05** Small: at most a few person-weeks (some teams: a few person-days). Above that it is too hard to know the scope. "It would take me more than a month" often implicitly means "I don't understand what-all it would entail." Smaller stories get more accurate estimates. *(Small)*
- **CLARIFY-INVEST-03** Testable: writing a story implies "I understand what I want well enough that I *could* write a test for it." Teams report higher productivity when customer tests are required before implementing. *(Testable)*
- **CLARIFY-INVEST-04** If the customer doesn't know how to test something, the story may be unclear, may not be valuable to them, or the customer may need help testing. *(Testable)*
- **CLARIFY-INVEST-05** Non-functional requirements (performance, usability) can be treated as things to be tested; operationalizing those tests reveals true needs. *(Testable)*
- **CLOSE-INVEST-01** The feedback cycle of proposing, estimating and implementing stories teaches the team what it needs to know. *(Testable, closing paragraph)*
- **SLICE-INVEST-06** Tasks should be SMART: Specific, Measurable, Achievable, Relevant, Time-boxed. *(SMART Tasks)*
- **SLICE-INVEST-07** Specific: everyone understands what the task involves; keeps tasks from overlapping; shows whether tasks add up to the full story. *(Specific)*
- **CLOSE-INVEST-02** Measurable: the key measure is "can we mark it as done?" — the agreed meaning should include "does what it is intended to," "tests are included," and "the code has been refactored." *(Measurable)*
- **COMMIT-INVEST-01** Achievable: the owner should expect to achieve the task; anyone can ask for help whenever needed. *(Achievable)*
- **SLICE-INVEST-08** Relevant: every task contributes to the story at hand and can be explained and justified to the customer. *(Relevant)*
- **COMMIT-INVEST-02** Time-boxed: a task is limited to a specific duration — not necessarily a formal estimate, but an expectation so people know when to seek help. If harder than expected: split the task, change players, or otherwise help it get done. *(Time-Boxed)*

### INFERRED
- **SLICE-INVEST-09** A story that can only be expressed as one technical layer is not yet a valuable slice. *(from Valuable)*
- **ESTIMATE-INVEST-02** Inability to estimate is a diagnostic signal: it points to insufficient understanding, excessive size, or missing experience — each has a different remedy (negotiate/clarify, split, spike). *(from Estimable)*
- **CLARIFY-INVEST-06** Not being able to state a test is evidence the work is not yet clarified. *(from Testable)*
- **COMMIT-INVEST-03** The time-box's function is to trigger a decision point (help / split / reassign), not to measure performance. *(from Time-Boxed)*

## Procedure / workflow
The source presents no step-by-step procedure. It offers two checklists (INVEST for stories, SMART for tasks) to apply "as you discuss stories, write cards, and split stories" and "when creating a task plan." *(Conclusion)*

INFERRED ordering: shape/split stories with INVEST → break a story into tasks with SMART → use time-box expectations to trigger help/split during work.

## Decision rules and gates
- **SLICE-INVEST-10** [DIRECT, Small] If a story looks larger than a few person-weeks (or "more than a month"), treat it as not understood and split it.
- **DERISK-INVEST-02** [DIRECT, Estimable] If a story cannot be estimated for lack of information, split off a time-boxed spike.
- **CLARIFY-INVEST-07** [DIRECT, Testable] If no one can say how to test it, the story is unclear, not valuable, or needs testing help — resolve before implementing.
- **SLICE-INVEST-11** [DIRECT, Valuable] If a split yields a single layer with no customer-visible value, re-slice vertically.
- **COMMIT-INVEST-04** [DIRECT, Time-Boxed] If a task exceeds its expected duration, split it, change players, or get help.
- **CLOSE-INVEST-03** [DIRECT, Measurable] A task is done only when it does what it's intended to, includes tests, and the code is refactored.

## Questions the future agent could ask
- **CLARIFY-INVEST-Q01** [INFERRED] Could you write a test for this right now? If not, what's missing?
- **SLICE-INVEST-Q02** [INFERRED] Does this slice cut through every layer needed to be usable, or only one?
- **SLICE-INVEST-Q03** [INFERRED] Would this take more than a few days/weeks? If "more than a month", what don't we understand?
- **ESTIMATE-INVEST-Q04** [INFERRED] Why can't this be estimated — not understood, too big, or unfamiliar? Does it need a spike first?
- **CLOSE-INVEST-Q05** [DIRECT] "Can we mark it as done?" — does it do what it's intended to, are tests included, is the code refactored?
- **COMMIT-INVEST-Q06** [INFERRED] What duration would make you stop and seek help or split this task?
- **SLICE-INVEST-Q07** [INFERRED] Can this task be explained and justified in terms of the story it serves?

## Positive examples from the source

### Example SLICE-INVEST-P01 — Vertical slice through the cake
**Classification:** DIRECT
**Source location:** Valuable
**What happens:** A story is pictured as a multi-layer cake (network, persistence, logic, presentation); a split serves a vertical slice through all layers.
**Why it is positive:** It gives the customer "the essence of the whole cake" and supports pay-as-you-go infrastructure.
**Principle illustrated:** Valuable; vertical slicing.

### Example DERISK-INVEST-P02 — Spike to enable an estimate
**Classification:** DIRECT
**Source location:** Estimable
**What happens:** A story that can't be estimated is split into a time-boxed spike and the remaining implementation story.
**Why it is positive:** The spike buys enough information for a decent estimate.
**Principle illustrated:** Estimable; separating learning from implementation.

### Example CLARIFY-INVEST-P03 — Customer tests before implementation
**Classification:** DIRECT
**Source location:** Testable
**What happens:** Teams require customer tests before implementing a story.
**Why it is positive:** Teams report being more productive; writing tests early reveals whether testability is really met.
**Principle illustrated:** Testable.

## Negative examples / anti-patterns from the source

### Example SLICE-INVEST-N01 — One layer at a time
**Classification:** DIRECT
**Source location:** Valuable
**What happens:** Developers work on one layer at a time to get it "right," e.g. a full database layer.
**Why it is negative:** It has little customer value if there's no presentation layer.
**Principle violated:** Valuable / vertical slicing.

### Example CLARIFY-INVEST-N02 — Mistaking the card for the whole story
**Classification:** DIRECT
**Source location:** Intro
**What happens:** Treating the story card as the complete requirement.
**Why it is negative:** Stories also consist of Conversation and Confirmation.
**Principle violated:** Card / Conversation / Confirmation.

### Example SLICE-INVEST-N03 — "More than a month"
**Classification:** DIRECT
**Source location:** Small
**What happens:** A developer says a story would take more than a month.
**Why it is negative:** That typically signals not understanding what it would entail.
**Principle violated:** Small; Estimable.

## Contrastive pairs

### Pair SLICE-INVEST-C01 — Slicing direction
**Good / preferred:** Slice vertically through all layers so each piece gives the customer the essence of the whole.
**Bad / discouraged:** Build one layer at a time (e.g. a complete database layer) and get it "right."
**Classification:** DIRECT
**Source location:** Valuable
**Distinguishing feature:** Whether the slice has customer value on its own.

### Pair ESTIMATE-INVEST-C02 — Unestimable story
**Good / preferred:** Split into a time-boxed spike plus the implementing story.
**Bad / discouraged:** (Not described in source.) DERIVED: attempt to estimate/implement the whole unknown story directly.
**Classification:** DIRECT (good side) / DERIVED (bad side)
**Source location:** Estimable
**Distinguishing feature:** Whether learning is separated from and precedes implementation.

### Pair CLOSE-INVEST-C03 — Meaning of "done" for a task
**Good / preferred:** Done = does what intended + tests included + code refactored.
**Bad / discouraged:** (Not in source.) DERIVED: done = code written / compiles.
**Classification:** DIRECT (good side) / DERIVED (bad side)
**Source location:** Measurable
**Distinguishing feature:** Includes tests and refactoring in the definition.

## Stop / go criteria

### GO
- Story is understood enough that you could write a test for it. *(Testable)*
- Story is small (few person-days to few person-weeks) and estimable enough to rank. *(Small, Estimable)*
- Slice delivers customer-visible value through all necessary layers. *(Valuable)*
- Tasks are specific, relevant, achievable, time-boxed. *(SMART)*

### STOP / RETURN
- Cannot say how to test → return to CLARIFY (unclear / not valuable / need help). *(Testable)*
- "More than a month" / cannot bound scope → return to SLICE. *(Small)*
- Cannot estimate for lack of knowledge → DERISK via time-boxed spike. *(Estimable)*
- Task running past its time-box → split, change players, or seek help. *(Time-Boxed)*

## Common failure modes
- Layer-at-a-time decomposition. *(Valuable)*
- Treating the card as a contract/full specification rather than a token for conversation. *(Intro; Negotiable; Small)*
- Framing developer concerns in terms the customer doesn't see as valuable. *(Valuable)*
- Stories too big to know their scope. *(Small)*

## Terms worth preserving
- `INVEST` — Independent, Negotiable, Valuable, Estimable, Small, Testable (criteria for stories).
- `SMART` — Specific, Measurable, Achievable, Relevant, Time-boxed (criteria for tasks; letters vary).
- `Card / Conversation / Confirmation` — the three components of a story (Jeffries).
- `pidgin language` — stories as a simplified shared language between customers and programmers.
- `spike` — time-boxed split that yields information to make an estimate.
- `vertical slice` / `multi-layer cake` — splitting through all layers.

## Candidate Skill rules
- `[DERIVED from Testable]` Do not start implementing until you can state at least one concrete test that would confirm the slice.
- `[DERIVED from Valuable]` Do not accept a slice that touches only one technical layer; re-slice until it is usable end-to-end.
- `[DERIVED from Small]` If the honest size is "more than a month" (or clearly larger than the chosen appetite), return to SLICE — treat it as not yet understood.
- `[DERIVED from Estimable]` If you cannot estimate, name which cause applies (unclear / too big / unfamiliar) and apply its remedy: clarify, split, or spike.
- `[DERIVED from Measurable]` Mark a task done only when it does what was intended, has tests, and has been refactored.
- `[DERIVED from Time-Boxed]` Attach an expected duration to each task; when it is exceeded, stop and choose: split, ask for help, or re-plan.
- `[DERIVED from Relevant]` Drop or justify any task that cannot be tied to the current story.

## Source limitations
- Written for XP teams with a customer role; "customer," "change players," "ask for help" assume a team. For a solo developer, "customer value" must be adapted to user-/stakeholder-visible behavior, and "change players" has no direct equivalent.
- Size thresholds ("few person-weeks") are story-level, much larger than an individual work slice; it gives no guidance for sizing a sub-day slice.
- Does not describe *how* to split (see Twenty Ways) or how to estimate (see EBS).
- Does not cover orienting in an existing codebase.
- The Postscript (acronym origin) has no operational content.

## Derived developer examples

### Example SLICE-INVEST-D01 — Adding a "phone number" field to user profiles
**Classification:** DERIVED
**Grounded in:** Wake INVEST — Valuable (vertical slice); Testable
**Discouraged:** Slice 1 = migration + model + full validation library for all phone formats; slice 2 = API; slice 3 = UI. Nothing user-visible until slice 3.
**Preferred:** Slice 1 = add nullable column, accept one format via the existing profile endpoint, render and edit it on the profile form, with one acceptance test ("user saves +41… and sees it after reload"). International formats become a later slice.
**Distinguishing feature:** The preferred first slice is usable and testable end-to-end.

### Example ESTIMATE-INVEST-D02 — "Integrate the payment provider's webhooks"
**Classification:** DERIVED
**Grounded in:** Wake INVEST — Estimable (spike split); Small
**Discouraged:** Estimating "about two weeks" for the whole integration without having read the provider's webhook docs or tried their sandbox.
**Preferred:** A 2-hour spike: receive one sandbox webhook locally and verify its signature; then estimate the implementation story from what was learned.
**Distinguishing feature:** Learning is time-boxed and precedes the estimate.

## ID register
| ID | Stage | Type | Short label | Classification | Location |
|---|---|---|---|---|---|
| SLICE-INVEST-01 | SLICE | rule | INVEST criteria | DIRECT | Intro |
| CLARIFY-INVEST-01 | CLARIFY | rule | Card/Conversation/Confirmation | DIRECT | Intro |
| SLICE-INVEST-02 | SLICE | rule | Independent (no overlap, any order) | DIRECT | Independent |
| CLARIFY-INVEST-02 | CLARIFY | rule | Negotiable: essence not details | DIRECT | Negotiable |
| SLICE-INVEST-03 | SLICE | rule | Valuable to customer | DIRECT | Valuable |
| SLICE-INVEST-04 | SLICE | rule | Slice vertically through layers | DIRECT | Valuable |
| ESTIMATE-INVEST-01 | ESTIMATE | rule | Estimability = negotiated + size + team | DIRECT | Estimable |
| DERISK-INVEST-01 | DERISK | rule | Time-boxed spike to enable estimate | DIRECT | Estimable |
| SLICE-INVEST-05 | SLICE | rule | Small; ">1 month" = not understood | DIRECT | Small |
| CLARIFY-INVEST-03 | CLARIFY | rule | Testable: could write a test | DIRECT | Testable |
| CLARIFY-INVEST-04 | CLARIFY | rule | Can't test → unclear/not valuable/needs help | DIRECT | Testable |
| CLARIFY-INVEST-05 | CLARIFY | rule | NFRs as tests | DIRECT | Testable |
| CLOSE-INVEST-01 | CLOSE | rule | Feedback cycle teaches | DIRECT | Testable |
| SLICE-INVEST-06 | SLICE | rule | SMART tasks | DIRECT | SMART Tasks |
| SLICE-INVEST-07 | SLICE | rule | Specific tasks add up to story | DIRECT | Specific |
| CLOSE-INVEST-02 | CLOSE | rule | Measurable: can we mark it done | DIRECT | Measurable |
| COMMIT-INVEST-01 | COMMIT | rule | Achievable; ask for help | DIRECT | Achievable |
| SLICE-INVEST-08 | SLICE | rule | Relevant to story | DIRECT | Relevant |
| COMMIT-INVEST-02 | COMMIT | rule | Time-boxed → help/split/change players | DIRECT | Time-Boxed |
| SLICE-INVEST-09 | SLICE | rule | Single-layer story not a slice | INFERRED | Valuable |
| ESTIMATE-INVEST-02 | ESTIMATE | rule | Unestimable as diagnostic | INFERRED | Estimable |
| CLARIFY-INVEST-06 | CLARIFY | rule | No test = not clarified | INFERRED | Testable |
| COMMIT-INVEST-03 | COMMIT | rule | Time-box triggers decision | INFERRED | Time-Boxed |
| SLICE-INVEST-10 | SLICE | gate | Too big → split | DIRECT | Small |
| DERISK-INVEST-02 | DERISK | gate | Can't estimate → spike | DIRECT | Estimable |
| CLARIFY-INVEST-07 | CLARIFY | gate | Can't test → resolve first | DIRECT | Testable |
| SLICE-INVEST-11 | SLICE | gate | Single layer → re-slice | DIRECT | Valuable |
| COMMIT-INVEST-04 | COMMIT | gate | Over time-box → split/help | DIRECT | Time-Boxed |
| CLOSE-INVEST-03 | CLOSE | gate | Done = intended + tests + refactored | DIRECT | Measurable |
| CLARIFY-INVEST-Q01 | CLARIFY | question | Could you write a test now? | INFERRED | Testable |
| SLICE-INVEST-Q02 | SLICE | question | Cuts through every layer? | INFERRED | Valuable |
| SLICE-INVEST-Q03 | SLICE | question | More than a month? | INFERRED | Small |
| ESTIMATE-INVEST-Q04 | ESTIMATE | question | Why unestimable? | INFERRED | Estimable |
| CLOSE-INVEST-Q05 | CLOSE | question | Can we mark it as done? | DIRECT | Measurable |
| COMMIT-INVEST-Q06 | COMMIT | question | Duration that triggers help | INFERRED | Time-Boxed |
| SLICE-INVEST-Q07 | SLICE | question | Task justified by story? | INFERRED | Relevant |
| SLICE-INVEST-P01 | SLICE | positive | Vertical cake slice | DIRECT | Valuable |
| DERISK-INVEST-P02 | DERISK | positive | Spike to enable estimate | DIRECT | Estimable |
| CLARIFY-INVEST-P03 | CLARIFY | positive | Customer tests first | DIRECT | Testable |
| SLICE-INVEST-N01 | SLICE | negative | One layer at a time | DIRECT | Valuable |
| CLARIFY-INVEST-N02 | CLARIFY | negative | Card = whole story | DIRECT | Intro |
| SLICE-INVEST-N03 | SLICE | negative | "More than a month" | DIRECT | Small |
| SLICE-INVEST-C01 | SLICE | pair | Vertical vs layer | DIRECT | Valuable |
| ESTIMATE-INVEST-C02 | ESTIMATE | pair | Spike vs direct | DIRECT/DERIVED | Estimable |
| CLOSE-INVEST-C03 | CLOSE | pair | Done definition | DIRECT/DERIVED | Measurable |
| SLICE-INVEST-D01 | SLICE | derived example | Phone field slice | DERIVED | — |
| ESTIMATE-INVEST-D02 | ESTIMATE | derived example | Webhook spike | DERIVED | — |
