# Independent Stories in the INVEST Model

## Source
- Author: Bill Wake
- URL: https://xp123.com/independent-stories-in-the-invest-model/
- Normalized copy: `sources/wake-independent-stories.md`
- Relevant workflow stages: SLICE (primary), DERISK (risk as negative value), CLARIFY (behavior partitioning)

## Core principles

### DIRECT
- **SLICE-INDEP-01** Independent stories each describe different aspects of a system's capabilities and can be (mostly) understood, tracked, implemented and tested on their own. *(Intro)*
- **SLICE-INDEP-02** Independence lets you pursue what is most valuable today rather than a "take it or leave it" lump. *(Intro)*
- **CLARIFY-INDEP-01** Avoiding overlap reduces contradictory descriptions and makes it easier to check completeness. *(Intro)*
- **SLICE-INDEP-03** Three dependency types: overlap (undesirable), order (mostly can be worked around), containment (sometimes helpful). *(Intro)*
- **SLICE-INDEP-04** Overlap is the most painful: it is hard to ensure everything is covered at least once and confusing when covered more than once. *(Overlap Dependency)*
- **SLICE-INDEP-05** The word "and" in a story title should make you suspicious of overlap, but you must compare multiple stories to know. *(Overlap Dependency)*
- **CLARIFY-INDEP-02** At the behavioral level, technical overlap (shared implementation tasks) is not the concern; design and scheduling are not the primary concern when trying to understand behavior. *(Overlap Dependency, parenthetical)*
- **SLICE-INDEP-06** Order dependencies are mostly harmless: some follow the problem's nature and the business will schedule accordingly; there's only a 50/50 chance you'd want the "wrong" order; most can be removed cleverly. *(Order Dependency)*
- **SLICE-INDEP-07** Remove an order dependency by hard-coding the prerequisite — "the skinniest possible version" (e.g. hard-coded accounts instead of account management first). *(Order Dependency)*
- **DERISK-INDEP-01** Order work by value and risk; treat risks as negative value. Hard-coded accounts were enough to explore a usability risk early. *(Order Dependency)*
- **SLICE-INDEP-08** Hierarchy (themes/epics/stories) is a good tool for describing and understanding, but rarely the best for scheduling; it encourages depth-first scheduling. *(Containment Dependency)*
- **SLICE-INDEP-09** Build a minimal version of the whole system first, then a fancier version with the next most important feature, and so on. *(Containment Dependency)*
- **SLICE-INDEP-10** Technically, independent stories encourage minimal implementation and designs that minimize and manage implementation dependencies. *(Bottom Line)*

### INFERRED
- **SLICE-INDEP-11** A perceived prerequisite is often a candidate for a stub or hard-coded stand-in rather than a blocker. *(from Order Dependency)*
- **DERISK-INDEP-02** Choosing what to do first is partly a de-risking decision: pick the slice that exposes the biggest risk, even if a "natural" prerequisite isn't built yet. *(from Order Dependency)*

## Procedure / workflow
No procedure is presented. The article is a taxonomy (overlap / order / containment) with a remedy for each:
- Overlap → repartition stories so each capability appears once. *(DIRECT, Overlap)*
- Order → hard-code/skinny the prerequisite; schedule by value and risk. *(DIRECT, Order)*
- Containment → use hierarchy to describe, but schedule minimal-whole-system-first. *(DIRECT, Containment)*

## Decision rules and gates
- **SLICE-INDEP-12** [DIRECT, Overlap] If two stories cover the same capability, repartition so each capability is covered once.
- **SLICE-INDEP-13** [DIRECT, Order] If story B "requires" story A, first ask whether A can be hard-coded as its skinniest version.
- **SLICE-INDEP-14** [DIRECT, Containment] Do not schedule by walking the hierarchy depth-first; prefer breadth (minimal whole system first).

## Questions the future agent could ask
- **SLICE-INDEP-Q01** [DIRECT] "What's the smallest set of stories that ensure that capabilities … are present?" — can we get these and nothing else?
- **SLICE-INDEP-Q02** [INFERRED] Does this slice description contain "and"? Does it overlap another planned slice?
- **SLICE-INDEP-Q03** [INFERRED] What does this slice depend on, and could that dependency be hard-coded for now?
- **DERISK-INDEP-Q04** [INFERRED] Which slice first addresses the biggest risk or the most value?
- **SLICE-INDEP-Q05** [INFERRED] Are we finishing one area depth-first when a minimal end-to-end version of the whole would teach more?

## Positive examples from the source

### Example SLICE-INDEP-P01 — Repartitioned email stories
**Classification:** DIRECT
**Source location:** Overlap Dependency
**What happens:** Overlapping stories are re-cut into "User sends [new] message," "User receives message," "User replies to message."
**Why it is positive:** Each capability appears once; no overlap.
**Principle illustrated:** Avoid overlap dependency.

### Example SLICE-INDEP-P02 — Hard-coded accounts
**Classification:** DIRECT
**Source location:** Order Dependency
**What happens:** Instead of implementing account management before sending email, initial accounts are hard-coded.
**Why it is positive:** Far less work, removes the order dependency, and still lets the team explore the usability risk.
**Principle illustrated:** Skinniest possible version; order by value and risk.

## Negative examples / anti-patterns from the source

### Example SLICE-INDEP-N01 — Overlapping "and" stories
**Classification:** DIRECT
**Source location:** Overlap Dependency
**What happens:** "User sends and receives messages" and "User sends and replies to messages" both include sending.
**Why it is negative:** Overlap makes coverage hard to verify and causes confusion.
**Principle violated:** Independent (no overlap).

### Example SLICE-INDEP-N02 — Depth-first scheduling from a hierarchy
**Classification:** DIRECT
**Source location:** Containment Dependency
**What happens:** Scheduling finishes one area of the hierarchy before moving to the next.
**Why it is negative:** The most valuable stories are unlikely to all be in one area.
**Principle violated:** Minimal whole system first.

### Example SLICE-INDEP-N03 — Abstract overlap set
**Classification:** DIRECT
**Source location:** Overlap Dependency
**What happens:** Stories cover overlapping subsets of capabilities {A–F}, making it hard to pick a minimal covering set.
**Why it is negative:** Illustrates the coverage/confusion cost of overlap.
**Principle violated:** Independent.

## Contrastive pairs

### Pair SLICE-INDEP-C01 — Overlap vs partition
**Good / preferred:** Sends new / receives / replies — one capability per story.
**Bad / discouraged:** "Sends and receives" + "sends and replies."
**Classification:** DIRECT
**Source location:** Overlap Dependency
**Distinguishing feature:** Each capability appears in exactly one story.

### Pair SLICE-INDEP-C02 — Prerequisite handling
**Good / preferred:** Hard-code initial accounts (skinniest version) and go straight to the area you want to explore.
**Bad / discouraged:** Implement account management stories first because sending "needs" accounts.
**Classification:** DIRECT
**Source location:** Order Dependency
**Distinguishing feature:** Whether the prerequisite is stubbed or fully built before the valuable/risky part.

### Pair SLICE-INDEP-C03 — Scheduling through hierarchy
**Good / preferred:** Minimal version of the whole system, then a fancier version with the next most important feature.
**Bad / discouraged:** Depth-first: complete an area, then move to the next.
**Classification:** DIRECT
**Source location:** Containment Dependency
**Distinguishing feature:** Breadth-first minimal whole vs depth-first by area.

## Stop / go criteria

### GO
- Slices don't overlap in behavior; each can be understood, implemented and tested on its own. *(Intro, Overlap)*
- Prerequisites are either genuinely natural (and scheduled accordingly) or stubbed. *(Order)*

### STOP / RETURN
- Two slices cover the same capability → repartition. *(Overlap)*
- A slice is blocked on a full prerequisite that could be hard-coded → re-slice. *(Order)*
- Plan follows the hierarchy depth-first → re-plan for a minimal whole. *(Containment)*

## Common failure modes
- Compound "and" stories that silently overlap. *(Overlap)*
- Building infrastructure prerequisites (e.g. account management) before the valuable/risky behavior. *(Order)*
- Using a descriptive hierarchy as the schedule. *(Containment)*

## Terms worth preserving
- `overlap dependency` — stories covering the same capability; undesirable.
- `order dependency` — "this story must be implemented before that one"; usually workable.
- `containment dependency` — hierarchical stories (themes/epics/stories); helpful for describing, not scheduling.
- `skinniest possible version` — hard-coded/minimal stand-in for a prerequisite.
- `risk as negative value` — risks weighed alongside value in ordering.

## Candidate Skill rules
- `[DERIVED from Overlap Dependency]` When a slice name contains "and", check it against the other planned slices and repartition if they overlap.
- `[DERIVED from Order Dependency]` Before building a prerequisite, try hard-coding or stubbing it so you can reach the valuable or risky behavior first.
- `[DERIVED from Order Dependency]` Order slices by value and by risk; pick the one that exposes the biggest risk early.
- `[DERIVED from Containment Dependency]` Do not schedule by walking a feature tree depth-first; aim for a minimal end-to-end version first.
- `[DERIVED from Overlap Dependency]` When clarifying behavior, ignore shared technical tasks; partition by behavior.

## Source limitations
- Story-level and team/business-oriented ("the business will tend to schedule"); a solo developer must play both business and technical roles.
- The 50/50 claim about order is a heuristic assertion, not evidence.
- Does not address implementation-level dependencies inside a slice (explicitly out of its concern).
- No guidance on orienting, estimating, or committing.

## Derived developer examples

### Example SLICE-INDEP-D01 — "Users can save and share filtered report views"
**Classification:** DERIVED
**Grounded in:** Wake INDEP — Overlap ("and" suspicion); Order (skinniest prerequisite)
**Discouraged:** Stories "User saves and shares a view" and "User saves and renames a view," and building the full saved-views management UI before sharing can be tried.
**Preferred:** Partition into "save view," "share view (link)," "rename view"; for the first sharing slice, share a view whose filters are encoded in the URL — the skinniest stand-in for persistence — to test whether recipients understand the shared report.
**Distinguishing feature:** No overlap; prerequisite stubbed so the risky part (does sharing make sense?) comes first.

### Example DERISK-INDEP-D02 — Authenticated "delete my comment" action
**Classification:** DERIVED
**Grounded in:** Wake INDEP — Order dependency; risk as negative value
**Discouraged:** Waiting for the new role/permission system to be finished before starting the delete action.
**Preferred:** Use the existing "author == current user" check as the skinniest authorization and deliver the delete flow; wire in the permission system as a later slice.
**Distinguishing feature:** Prerequisite is stubbed by an existing minimal rule rather than blocking.

## ID register
| ID | Stage | Type | Short label | Classification | Location |
|---|---|---|---|---|---|
| SLICE-INDEP-01 | SLICE | rule | Independent = understood/tested alone | DIRECT | Intro |
| SLICE-INDEP-02 | SLICE | rule | Pursue most valuable today | DIRECT | Intro |
| CLARIFY-INDEP-01 | CLARIFY | rule | No overlap aids consistency/completeness | DIRECT | Intro |
| SLICE-INDEP-03 | SLICE | rule | Overlap/order/containment | DIRECT | Intro |
| SLICE-INDEP-04 | SLICE | rule | Overlap most painful | DIRECT | Overlap |
| SLICE-INDEP-05 | SLICE | rule | "and" in title → suspicion | DIRECT | Overlap |
| CLARIFY-INDEP-02 | CLARIFY | rule | Ignore technical overlap at behavior level | DIRECT | Overlap |
| SLICE-INDEP-06 | SLICE | rule | Order deps mostly harmless | DIRECT | Order |
| SLICE-INDEP-07 | SLICE | rule | Hard-code prerequisite (skinniest) | DIRECT | Order |
| DERISK-INDEP-01 | DERISK | rule | Order by value and risk | DIRECT | Order |
| SLICE-INDEP-08 | SLICE | rule | Hierarchy describes, doesn't schedule | DIRECT | Containment |
| SLICE-INDEP-09 | SLICE | rule | Minimal whole system first | DIRECT | Containment |
| SLICE-INDEP-10 | SLICE | rule | Independence → minimal implementation | DIRECT | Bottom Line |
| SLICE-INDEP-11 | SLICE | rule | Prerequisite → stub candidate | INFERRED | Order |
| DERISK-INDEP-02 | DERISK | rule | First slice exposes biggest risk | INFERRED | Order |
| SLICE-INDEP-12 | SLICE | gate | Overlap → repartition | DIRECT | Overlap |
| SLICE-INDEP-13 | SLICE | gate | Prerequisite → hard-code first? | DIRECT | Order |
| SLICE-INDEP-14 | SLICE | gate | No depth-first scheduling | DIRECT | Containment |
| SLICE-INDEP-Q01 | SLICE | question | Smallest covering set | DIRECT | Overlap |
| SLICE-INDEP-Q02 | SLICE | question | "and"/overlap? | INFERRED | Overlap |
| SLICE-INDEP-Q03 | SLICE | question | Dependency hard-codable? | INFERRED | Order |
| DERISK-INDEP-Q04 | DERISK | question | Biggest risk/value first? | INFERRED | Order |
| SLICE-INDEP-Q05 | SLICE | question | Depth-first vs minimal whole? | INFERRED | Containment |
| SLICE-INDEP-P01 | SLICE | positive | Repartitioned email stories | DIRECT | Overlap |
| SLICE-INDEP-P02 | SLICE | positive | Hard-coded accounts | DIRECT | Order |
| SLICE-INDEP-N01 | SLICE | negative | Overlapping "and" stories | DIRECT | Overlap |
| SLICE-INDEP-N02 | SLICE | negative | Depth-first hierarchy schedule | DIRECT | Containment |
| SLICE-INDEP-N03 | SLICE | negative | Abstract overlap set | DIRECT | Overlap |
| SLICE-INDEP-C01 | SLICE | pair | Overlap vs partition | DIRECT | Overlap |
| SLICE-INDEP-C02 | SLICE | pair | Stub vs build prerequisite | DIRECT | Order |
| SLICE-INDEP-C03 | SLICE | pair | Minimal whole vs depth-first | DIRECT | Containment |
| SLICE-INDEP-D01 | SLICE | derived example | Saved/shared report views | DERIVED | — |
| DERISK-INDEP-D02 | DERISK | derived example | Delete-my-comment auth stub | DERIVED | — |
