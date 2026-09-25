# The Time-Block Planner (product page)

## Source
- Author: Cal Newport (product page, Penguin Random House)
- URL: https://www.timeblockplanner.com/
- Published: unknown (page footer © 2026)
- Normalized file: `sources/newport-time-block-planner.md`
- Relevant workflow stages: **COMMIT** (preliminary plan), **IMPLEMENT** (capturing discovered tasks without leaving the current block). Weak support.

**Evidence status:** This is a marketing page. Only the **"A Closer Look"** paragraph describes method: a preliminary plan, updating it when knocked off, and a collection page. The "Standard approach" and "Time blocking" bullets are **benefit claims** (e.g. "Enabling clear shutdowns," "Replacing stressful busyness…") with no mechanism. They are recorded below as claims, not as grounding. The "For fifteen years…" copy is promotional and isn't used.

## Core principles

### DIRECT
- **COMMIT-TBP-01** — Each day, fill out a time-block grid with a **preliminary** plan that gives every minute a job. *(A Closer Look)*
- **COMMIT-TBP-02** — If you get knocked off the schedule, update it the next time you get a chance. *(A Closer Look)*
- **IMPLEMENT-TBP-01** — Next to the grid is a **collection page** where you quickly capture tasks and notes to process later, so you don't have to disrupt your current time block. *(A Closer Look)*

### INFERRED
- **COMMIT-TBP-03** — The word "preliminary" marks the plan as expected to change. Its first version is a draft, not a contract. *(A Closer Look)*
- **CLOSE-TBP-01** — Captured tasks and notes are processed *later*, at some point outside the current block. The page doesn't say when. *(A Closer Look)*

### Benefit claims (NOT evidence; recorded for completeness)
- "Standard approach" bullets: reacting to messages creates distraction, anxiety, impeded deep work, and a feeling that work is never done.
- "Time blocking" bullets: balances important with urgent, minimizes the urge to give in to distractions, replaces busyness with intention, and enables clear shutdowns at the end of the day.
These are asserted, not demonstrated. "Clear shutdowns" is mentioned but no shutdown procedure is described on this page.

## Procedure / workflow
Described in "A Closer Look" (DIRECT; the page presents it as the whole method, "that's all there is to it"):
1. Each day, fill the grid with a preliminary plan in which every minute has a job.
2. If knocked off, update the plan at the next chance.
3. During a block, jot new tasks and notes on the collection page instead of acting on them.
4. Process the collected items later.

## Decision rules and gates
- **IMPLEMENT-TBP-02** — Rule: when a new task or thought comes up during a block, capture it on the collection page and continue the current block. *(DIRECT, A Closer Look)*
- **COMMIT-TBP-04** — Rule: if knocked off, update the plan. Don't abandon it. *(DIRECT, A Closer Look)*

## Questions the future agent could ask
- **IMPLEMENT-TBP-Q01** `[INFERRED]` — Is this new thing something to do *now*, or to capture and process later so the current block isn't disrupted? *(A Closer Look)*
- **COMMIT-TBP-Q01** `[INFERRED]` — What's today's preliminary plan for this work? *(A Closer Look)*
- **CLOSE-TBP-Q01** `[DERIVED]` — Which items captured during this block need to become slices, bugs, or notes?

## Positive examples from the source

### IMPLEMENT-TBP-P01 — Capture without disrupting
**Classification:** DIRECT
**Source location:** A Closer Look
**What happens:** Tasks and notes that come up are written on the collection page next to the grid, to be processed later.
**Why it is positive:** The page says this avoids disrupting the current time block.
**Principle illustrated:** IMPLEMENT-TBP-01.

## Negative examples / anti-patterns from the source
- None described as a method-level negative example. The "Standard approach" section (reacting to messages all day) is presented through benefit/harm claims, not a worked example. See the stronger DIRECT pair in `newport-focus-week-time-blocking.md` (COMMIT-TBLOCK-C01).

## Contrastive pairs

### IMPLEMENT-TBP-C01 — New task arises mid-block
**Good / preferred:** Capture it on the collection page and process it later. *(DIRECT)*
**Bad / discouraged:** *(DERIVED)* Switch to the new task immediately and abandon the current block.
**Classification:** Good side DIRECT; bad side DERIVED
**Source location:** A Closer Look
**Distinguishing feature:** Whether the current block is preserved.

## Stop / go criteria

### GO
- A preliminary plan exists for the day. *(DIRECT)*

### STOP / RETURN
- Knocked off the schedule: update the plan. *(DIRECT)*
- The page defines no stop condition for a block's task and no end-of-day procedure.

## Common failure modes
- (INFERRED from the capture rule) Acting on every new idea or task the moment it appears, which disrupts the current block.

## Terms worth preserving
- `preliminary plan` — the day's first draft of the time-block grid, expected to change.
- `collection page` — a place to quickly capture tasks and notes for later processing without disrupting the current block.
- `time block grid` — the daily layout where every minute gets a job.

## Candidate Skill rules
- `[DERIVED from A Closer Look]` Treat the day's block plan as preliminary. When it breaks, update it. Don't abandon it.
- `[DERIVED from A Closer Look]` When you discover a new task during implementation, write it to a capture list and continue the current slice. Process the list at CLOSE.
- `[DERIVED from A Closer Look]` At CLOSE, go through the captured items and turn each into a next slice, a bug, or a discarded note.

## Source limitations
- A product/marketing page. One paragraph of method; the rest is benefit claims and promotion.
- It doesn't say when or how to process collected items, and has no shutdown procedure despite claiming "clear shutdowns."
- It doesn't define block length, how to size work to a block, or what to do when a block's work isn't finished.
- It isn't software-specific. The link to "discovered work" in a dev loop (cf. Shape Up's imagined vs discovered tasks) is an adaptation, not a claim this page makes.
- The underlying book isn't a public source here. Methodological details from it are **not** grounded by this page.

## Derived developer examples

### IMPLEMENT-TBP-D01 — Discovered refactor during a feature slice
**Classification:** DERIVED
**Grounded in:** Time-Block Planner, A Closer Look (IMPLEMENT-TBP-01, -02; IMPLEMENT-TBP-C01)
**Preferred:** While adding a `phone` field to the user API response, the developer notices the serializer duplicates date formatting in three places. They add "dedupe date formatting in UserSerializer" to the capture list and finish the `phone` slice within the block. At close, the item becomes a candidate next slice.
**Discouraged:** The developer starts refactoring the serializer mid-block. The `phone` slice is still unfinished when the block ends, and the diff now mixes two changes.
**Distinguishing feature:** Whether discovered work is captured for later or pulled into the current block.

### COMMIT-TBP-D02 — Preliminary plan meets reality
**Classification:** DERIVED
**Grounded in:** Time-Block Planner, A Closer Look (COMMIT-TBP-01, -02, -03)
**Preferred:** The morning plan gives 9:00–11:00 to "reproduce Safari date-picker bug." Reproduction takes until 11:45, so the developer updates the grid and moves the lunch-adjacent review block to the afternoon.
**Discouraged:** The developer treats the 9–11 plan as broken and works without any plan for the rest of the day.
**Distinguishing feature:** Updating a preliminary plan versus discarding it.

## ID register
| ID | Stage | Type | Short label | Classification | Location |
|---|---|---|---|---|---|
| COMMIT-TBP-01 | COMMIT | rule | Daily preliminary plan, every minute a job | DIRECT | A Closer Look |
| COMMIT-TBP-02 | COMMIT | rule | Knocked off ⇒ update at next chance | DIRECT | A Closer Look |
| COMMIT-TBP-03 | COMMIT | rule | "Preliminary" = draft, expected to change | INFERRED | A Closer Look |
| COMMIT-TBP-04 | COMMIT | gate | Update, don't abandon | DIRECT | A Closer Look |
| IMPLEMENT-TBP-01 | IMPLEMENT | rule | Collection page: capture without disrupting block | DIRECT | A Closer Look |
| IMPLEMENT-TBP-02 | IMPLEMENT | gate | New task mid-block ⇒ capture, continue | DIRECT | A Closer Look |
| CLOSE-TBP-01 | CLOSE | rule | Captured items processed later | INFERRED | A Closer Look |
| IMPLEMENT-TBP-Q01 | IMPLEMENT | question | Now, or capture for later? | INFERRED | A Closer Look |
| COMMIT-TBP-Q01 | COMMIT | question | Today's preliminary plan? | INFERRED | A Closer Look |
| CLOSE-TBP-Q01 | CLOSE | question | Captured items → slices/bugs/notes? | DERIVED | — |
| IMPLEMENT-TBP-P01 | IMPLEMENT | positive | Capture without disrupting | DIRECT | A Closer Look |
| IMPLEMENT-TBP-C01 | IMPLEMENT | pair | Capture vs switch | DIRECT (good) / DERIVED (bad) | A Closer Look |
| IMPLEMENT-TBP-D01 | IMPLEMENT | derived | Discovered refactor mid-slice | DERIVED | A Closer Look |
| COMMIT-TBP-D02 | COMMIT | derived | Preliminary plan meets reality | DERIVED | A Closer Look |
