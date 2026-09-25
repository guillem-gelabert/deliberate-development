# Slice

## Purpose
Reduce the clarified work to a small increment that can be verified on its own and that runs end to end through the system, then pick which slice comes first. A slice is a unit of *behavior*. It is not a TDD test step and not an estimation task.

## Primary grounding sources
- Wake, *Twenty Ways to Split Stories*: primary for split dimensions.
- Wake, *INVEST*: primary for the criteria a good slice meets (esp. Valuable/vertical, Small, Testable).
- Wake, *Independent Stories*: primary for overlap, order and containment.
- Singer, *Get One Piece Done*: primary for the first slice (core/small/novel, start in the middle).
- Singer, *Set Boundaries* and *Risks and Rabbit Holes*: supporting. Grab-bags, out of bounds, cut back.

## Entry conditions
- Clarify exit criteria are met: concrete examples and a narrowed problem.

## Agent questions
1. What is the minimal end-to-end version, the narrow but high-value path through the system? (INFERRED, SLICE-SPLIT-Q06)
2. Does the slice go through every layer (UI → logic → persistence) so it can actually be used? (INFERRED, SLICE-INVEST-Q02)
3. Can you split on a connector word ("and", "or", "then"), main flow vs alternates, 0/1/many, or base case vs general case? (INFERRED, SLICE-SPLIT-Q02–Q04)
4. Can a prerequisite be hard-coded or stubbed so the interesting part can be done first? (INFERRED, SLICE-INDEP-Q03)
5. Of the candidate first slices, which is **core**, **small** and **novel**? (INFERRED, SLICE-ONEPIECE-Q01)
6. Do the slices reassemble into the full functionality? (INFERRED, SLICE-SPLIT-Q07)

## Rules
- **Get a minimal end-to-end solution in place first, then fill in the rest.** (DIRECT, SLICE-SPLIT-03)
- **Slice vertically through the layers.** A complete layer with nothing above it has little value. (DIRECT, SLICE-INVEST-04; SLICE-ONEPIECE-02)
- **Choose the first slice to be core, small and novel.** When two are equally core and small, prefer the one you've never done before. (DIRECT, SLICE-ONEPIECE-06/-07)
- **Start in the middle.** Stub login, setup and other peripherals to reach the interesting problem. (DIRECT, SLICE-ONEPIECE-05; SLICE-INDEP-07 "skinniest possible version")
- **Avoid overlap between slices.** Repartition when two slices share behavior. An "and" in a title is a signal to check. (DIRECT, SLICE-INDEP-04/-05/-12)
- **Don't schedule depth-first by hierarchy.** Build a minimal version of the whole, then improve it. (DIRECT, SLICE-INDEP-08/-09/-14)
- **Use the easier side of a split dimension first and defer the harder side.** The harder side is deferred, not wrong. (INFERRED, SLICE-SPLIT-13)
- **Declare what is out of bounds and cut the nice-to-haves.** (DIRECT, SLICE-RISK-11/-12)
- **Combine slices that are too small to be interesting.** (DIRECT, SLICE-SPLIT-02/-17)

## Positive patterns
- The visibility toggle came first in Clients-in-Projects: central, small, novel, and demoed on day three. (DIRECT, SLICE-ONEPIECE-P01)
- The credit check started as a manual process, so the system shipped earlier. (DIRECT, SLICE-SPLIT-P01)
- Email stories were repartitioned from "sends and receives"/"sends and replies" into send / receive / reply. (DIRECT, SLICE-INDEP-P01)
- Hard-coded accounts stood in for account management so usability risk could be explored first. (DIRECT, SLICE-INDEP-P02)
- Files 2.0 was recovered by splitting it into "Better file previews" and "Custom folder colors". (DIRECT, SLICE-BOUND-P03)

## Anti-patterns
- Working one layer at a time, e.g. a full database layer with no presentation. (DIRECT, SLICE-INVEST-N01; SLICE-ONEPIECE-N01)
- Building recovery flows before the most trivial transaction works. (DIRECT, SLICE-SPLIT-N01)
- Starting with the peripheral or familiar part (rename client; add-client UI) that teaches nothing. (DIRECT, SLICE-ONEPIECE-N02)
- Splitting without checking that the pieces reassemble. (DIRECT, SLICE-SPLIT-N04)
- "Files 2.0": a grab-bag with no "done". (DIRECT, SLICE-BOUND-N01)
- Treating "ignore errors" as licence to swallow exceptions. (DIRECT, SLICE-SPLIT-N02)

## Contrastive examples

**SLICE-SYN-D01: Adding a DB field plus the behavior that uses it** (DERIVED; grounded in SLICE-INVEST-04, SLICE-SPLIT-03)
- *Preferred:* Slice 1 adds a nullable `phone` column, a form field, save, and display after reload, for one country format. Later slices add international formats, validation messages and admin search by phone.
- *Discouraged:* Migration and model for all phone features first, then API, then UI, with nothing usable until the end.

**SLICE-SYN-D02: Authenticated user action ("delete my comment")** (DERIVED; grounded in SLICE-ONEPIECE-05, SLICE-INDEP-07)
- *Preferred:* Use the existing session or a seeded test user, and go straight to "the owner deletes their own comment; a non-owner gets 403".
- *Discouraged:* Start by building role management or a new permissions system "because delete needs auth".

**SLICE-SYN-D03: Vue/React component change** (DERIVED; grounded in SLICE-SPLIT-C04 main vs alternate flows, SLICE-SPLIT-C05 0/1/many)
- *Preferred:* Render one item in the new `OrderSummary` layout (main flow). Then zero items (empty state). Then many (pagination).
- *Discouraged:* Build the empty, loading, error and pagination states before one item renders correctly.

## Stop / return conditions
- The slice can't be described with a Given/When/Then example → Clarify.
- You can't tell whether a slice is feasible, or how to split it → De-risk (research/spike split). (DIRECT, DERISK-SPLIT-04)
- The slice is still larger than a few days of real work, or still has a connector word → split again. The size heuristic is DERIVED; Wake's story bound is a few person-weeks, and Shape Up's first piece is "a few days".

## Exit criteria
- One named first slice: end to end, with its examples, marked core/small/novel.
- A short list of the remaining slices, with out-of-bounds items stated.

## Unresolved tensions between sources
- **Unit sizes differ.** A Wake story is up to a few person-weeks, some teams use a few days. A Shape Up first piece is "a few days". An EBS task is ≤16 hours. Keep slice (behavior) and task (estimation unit) separate.
- **Value-first vs risk-first.** Wake orders by value *and* risk (risk as negative value). Singer's "novel" criterion and "scariest first" lean toward risk. Both are DIRECT, so the Skill should ask which dominates for the current work.
- **Up-front decomposition.** Shape Up warns that splitting a project into tasks up front is like a "paper shredder" (SLICE-HANDOVER-06). That warning targets *task assignment to others*, not behavior slicing. Wake's story splitting is a customer-value activity. The two don't conflict, but EBS task breakdown does sit in tension with Shape Up (see `estimate.md`).

## Provenance map
| Rule / example | Source | Classification | Source section |
|---|---|---|---|
| Minimal end-to-end first | Wake, Twenty Ways | DIRECT | Intro |
| Vertical slice through layers | Wake, INVEST; Singer, Get One Piece Done | DIRECT | Valuable; Integrate one slice |
| Core / small / novel | Singer, Get One Piece Done | DIRECT | Start in the middle |
| Hard-code prerequisites | Wake, Independent Stories; Singer, Get One Piece Done | DIRECT | Order Dependency; Program just enough |
| Overlap / "and" | Wake, Independent Stories | DIRECT | Overlap Dependency |
| No depth-first by hierarchy | Wake, Independent Stories | DIRECT | Containment Dependency |
| Split dimensions | Wake, Twenty Ways | DIRECT | tables |
| Easier-first (not "bad") | Wake, Twenty Ways | INFERRED | tables |
| Out of bounds / cut back | Singer, Risks and Rabbit Holes | DIRECT | Declare out of bounds; Cut back |
| SLICE-SYN-D01–D03 | — | DERIVED | — |
