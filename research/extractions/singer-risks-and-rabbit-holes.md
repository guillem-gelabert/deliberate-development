# Risks and Rabbit Holes (Shape Up, ch. 5)

## Source
- Author: Ryan Singer
- URL: https://basecamp.com/shapeup/1.4-chapter-05
- Normalized file: `sources/singer-risks-and-rabbit-holes.md`
- Relevant workflow stages: DERISK (primary), SLICE (out of bounds, cut back), COMMIT (safe to bet)

## Core principles

### DIRECT
- **DERISK-RISK-01** One hole in the concept can derail a fixed-time project; an unanticipated two-week problem burns a third of a six-week budget. (Intro)
- **DERISK-RISK-02** Some problems have no apparent solution at all; not validating in shaping that a viable approach exists can force abandonment. (Intro)
- **DERISK-RISK-03** There will always be unknowns, but look for the pitfalls you *can* find up front and eliminate them before betting; a shaped project should be as free of holes as possible. (Intro)
- **DERISK-RISK-04** Well-shaped work is a thin-tailed distribution (maybe an extra week); rabbit holes make it fat-tailed—multiple times the appetite. (Different categories of risk)
- **DERISK-RISK-05** Three categories of rabbit hole: technical unknowns, unsolved design problems, misunderstood interdependencies. (Different categories of risk)
- **DERISK-RISK-06** Aim for independent, well-understood parts that assemble in known ways. (Different categories of risk)
- **DERISK-RISK-07** After fast breadth-first exploration, slow down and look critically: did we miss anything? Are our technical assumptions fair? (Look for rabbit holes)
- **DERISK-RISK-08** Walk through a use case in slow motion: how exactly does a user get from start to end? This reveals gaps. (Look for rabbit holes)
- **DERISK-RISK-09** Question the viability of each part you think you solved using four questions (below). (Look for rabbit holes)
- **DERISK-RISK-10** Patch holes by dictating a solution in the concept where leaving it open would push a deep design problem onto the team under deadline. (Case study: Patching a hole)
- **SLICE-RISK-11** Declare out of bounds: explicitly call out cases you aren't supporting. (Declare out of bounds)
- **SLICE-RISK-12** Cut back: flag parts you got excited about but aren't necessary; everyone assumes the feature is valuable without them. (Cut back)
- **DERISK-RISK-13** Verify uncertain technical assumptions with experts; ask "is X possible within the appetite?" not "is X possible?"—"everything is possible but nothing is free." (Present to technical experts)
- **DERISK-RISK-14** The expert conversation is a hunt for time bombs that might blow up the project, not a general "what do you think." (Present to technical experts)
- **DERISK-RISK-15** Outcome of the expert review is either validation or discovered problems that send you back to shaping. (Present to technical experts)

### INFERRED
- **DERISK-RISK-16** Risk is judged relative to the fixed time box: a risk matters by how much of the budget it could consume. (Intro; categories)
- **DERISK-RISK-17** Trading some polish for removal of a risk tail is legitimate when it preserves what made the work worth doing. (Case study: Patching a hole)

## Procedure / workflow
Chapter order (presented as sequential steps of this shaping stage; DIRECT as chapter structure, not as a numbered list):
1. Look for rabbit holes: slow down; slow-motion use case walk-through; ask the viability questions.
2. Patch holes: decide tricky points in advance.
3. Declare out of bounds.
4. Cut back unnecessary parts.
5. Present to technical experts; hunt for time bombs; either validate or return to shaping.
6. Exit: elements + patches + fences → ready to write up.

## Decision rules and gates
- **DERISK-RISK-18** If you are assuming a design solution exists that you couldn't come up with yourself, treat it as a hole. [DIRECT, question list; reinforced by client-projects case]
- **DERISK-RISK-19** If a hard decision could trip up the builders, settle it in advance. [DIRECT, question list]
- **DERISK-RISK-20** If expert review uncovers problems, go back for another round of shaping. [DIRECT, Present to technical experts]
- **COMMIT-RISK-21** Gate "de-risked": elements of the solution, patches for rabbit holes, fences around out-of-bounds areas. [DIRECT, De-risked and ready to write up]

## Questions the future agent could ask
- **DERISK-RISK-Q01** [DIRECT] Does this require new technical work we've never done before?
- **DERISK-RISK-Q02** [DIRECT] Are we making assumptions about how the parts fit together?
- **DERISK-RISK-Q03** [DIRECT] Are we assuming a design solution exists that we couldn't come up with ourselves?
- **DERISK-RISK-Q04** [DIRECT] Is there a hard decision we should settle in advance so it doesn't trip up the team?
- **DERISK-RISK-Q05** [DIRECT] Did we miss anything? Are we making technical assumptions that aren't fair? (Look for rabbit holes)
- **DERISK-RISK-Q06** [DIRECT] How exactly would a user get from the starting point to the end? (slow-motion walk-through)
- **DERISK-RISK-Q07** [DIRECT] Is X possible within the appetite (e.g., "in 6 weeks")? (Present to technical experts)
- **SLICE-RISK-Q08** [INFERRED] Which cases are we explicitly *not* supporting? (Declare out of bounds)
- **SLICE-RISK-Q09** [INFERRED] Is this part necessary, or is the work valuable without it? (Cut back)

All [DIRECT] items above are from "Look for rabbit holes" unless noted.

## Positive examples from the source

### DERISK-RISK-P01 — Patching the completed-to-dos hole
**Classification:** DIRECT
**Source location:** Case study: Patching a hole
**What happens:** To-Do Groups introduced dividers, but didn't address how completed items display. Knowing changes to completed-item rendering have complex UX/navigation/performance implications, shapers dictated: leave completed items as they were, append the group name to each. Slightly messy, but it drastically simplified the problem; the patch was called out in the pitch.
**Why it is positive:** Cut off a big tail of risk while keeping the core value.
**Principle illustrated:** Settle hard decisions in advance; trade polish for risk.

### SLICE-RISK-P02 — Group notification: out of bounds
**Classification:** DIRECT
**Source location:** Declare out of bounds
**What happens:** Selecting a group ("Programmers") to notify could apply to messages, to-do assignment, chat mentions. They defined core value as narrowing who to notify about a message and marked other cases out of bounds.
**Why it is positive:** Kept the project within appetite, focused on one win.
**Principle illustrated:** Explicit exclusions.

### SLICE-RISK-P03 — Color-coded groups cut
**Classification:** DIRECT
**Source location:** Cut back
**What happens:** Color-coding to-do groups was attractive but flagged as unnecessary; mentioned only as nice-to-have.
**Why it is positive:** Core stays valuable without it.
**Principle illustrated:** Cut back.

## Negative examples / anti-patterns from the source

### DERISK-RISK-N01 — Clients-on-home-screen redesign abandoned
**Classification:** DIRECT
**Source location:** Intro
**What happens:** They bet on redesigning how projects with clients appear on the home screen, assuming the designer would figure it out, without validating in shaping that a viable approach existed. No suitable design found in six weeks; project abandoned and rethought later.
**Why it is negative:** An unvalidated "a solution exists" assumption.
**Principle violated:** Look for rabbit holes before betting (Q03).

### DERISK-RISK-N02 — Pushing the knot to the team
**Classification:** DIRECT
**Source location:** Case study: Patching a hole
**What happens:** Leaving the completed-items question open would push a deep design problem onto the team to solve under deadline; a designer could waste days experimenting with styling down a dead end.
**Why it is negative:** "It's not responsible to give the team a tangled knot of interdependencies" to untangle in a short fixed window.
**Principle violated:** Patch holes in shaping.

### DERISK-RISK-N03 — "Is this possible?"
**Classification:** DIRECT
**Source location:** Present to technical experts
**What happens:** Asking whether something is possible at all.
**Why it is negative:** In software everything is possible; the question hides cost.
**Principle violated:** Ask relative to appetite.

## Contrastive pairs

### DERISK-RISK-C01 — Expert question framing
**Good / preferred:** "Is X possible in 6 weeks?"
**Bad / discouraged:** "Is it possible to do X?"
**Classification:** DIRECT
**Source location:** Present to technical experts
**Distinguishing feature:** Bounded by appetite.

### DERISK-RISK-C02 — Thin vs fat tail
**Good / preferred:** Thin-tailed: well-understood, independent parts; at worst ~one extra week.
**Bad / discouraged:** Fat-tailed: technical unknowns, unsolved design, misunderstood interdependencies; possible 3x delay.
**Classification:** DIRECT
**Source location:** Different categories of risk
**Distinguishing feature:** Presence of rabbit holes.

### DERISK-RISK-C03 — Patch vs leave open
**Good / preferred:** Dictate a simple solution for the risky spot in the concept (completed items unchanged + group label).
**Bad / discouraged:** Leave it for the team to figure out under deadline.
**Classification:** DIRECT
**Source location:** Case study: Patching a hole
**Distinguishing feature:** Who resolves the risk, and when.

### DERISK-RISK-C04 — Validated vs assumed solution
**Good / preferred:** Validate in shaping that a viable approach exists.
**Bad / discouraged:** Assume the designer will figure it out (client-projects redesign).
**Classification:** DIRECT (bad side, explicit); good side INFERRED from "we didn't do the work in the shaping phase to validate that a viable approach existed."
**Source location:** Intro

## Stop / go criteria

### GO
- Solution elements exist, rabbit holes are patched, out-of-bounds areas are fenced (COMMIT-RISK-21).
- Expert walk-through validated the approach within the appetite.
- Remaining work looks thin-tailed.

### STOP / RETURN
- Any viability question answered "yes, and we don't know how" → patch, cut, or return to shaping.
- Assuming a solution exists that you couldn't produce yourself → stop and validate.
- Expert review reveals problems → another round of shaping.
- Slow-motion walk-through reveals missing pieces → design them first.

## Common failure modes
- Moving too fast (breadth) without the slow critical pass.
- Assuming "the designer/programmer will figure it out."
- Unfair technical assumptions ("I'll just use that API" — see Show Progress chapter for the parallel).
- Covering every use case the team can imagine.
- Asking "is it possible?" instead of "within the appetite?"

## Terms worth preserving
- `rabbit hole` — a technical unknown, unsolved design problem, or misunderstood interdependency that could make work take multiples of the appetite.
- `thin-tailed / fat-tailed` — probability distribution of time-to-ship.
- `patch` — a decision made in shaping to close a hole.
- `out of bounds` — explicitly unsupported cases.
- `cut back` — removing nice-to-haves from the core.
- `time bombs` — hidden risks that blow up the project once committed.
- `keep the clay wet` — review at a whiteboard, not a finished document.

## Candidate Skill rules
- `[DERIVED from Look for rabbit holes]` Before committing, walk through the change end to end in slow motion and list gaps.
- `[DERIVED from Look for rabbit holes]` Ask the four viability questions; any "yes" without an answer is a risk to patch, cut, or spike.
- `[DERIVED from Intro]` Do not assume a solution exists for a part you can't sketch yourself; validate it first.
- `[DERIVED from Case study: Patching a hole]` If a risky detail has a simple acceptable answer, decide it now and write it down rather than leaving it open during implementation.
- `[DERIVED from Declare out of bounds]` Write down which cases are explicitly not handled in this slice.
- `[DERIVED from Cut back]` Remove attractive-but-unnecessary parts from the core; list them as nice-to-have.
- `[DERIVED from Present to technical experts]` When asking for input, ask "can this be done within <time budget>?" and ask specifically for risks.
- `[DERIVED from Different categories of risk]` If the work still has technical unknowns, unsolved design, or unclear interdependencies, do not treat it as ready-to-build; return to De-risk.

## Source limitations
- Written for shapers de-risking before a team bet; for an individual developer, shaper and builder are the same person, so "patching before handing over" becomes "deciding before starting to code"—an adaptation.
- The "possible in 6 weeks" framing is at team-cycle scale; applying it to hours/days is not source-supported.
- Does not specify how to resolve a technical unknown hands-on (no spike method); Wake's spike split and Show Progress's "hands not head" are the nearest supports.
- Presenting to technical experts assumes colleagues are available.

## Derived developer examples

### DERISK-RISK-D01 — Unfamiliar payments API
**Classification:** DERIVED
**Grounded in:** Risks and Rabbit Holes — technical unknowns; "is X possible within the appetite"; validated vs assumed solution
**Bad:** Estimate "integrate refunds via provider API: 1 day" and start wiring UI, assuming the API supports partial refunds on captured payments.
**Good:** Flag "new technical work we've never done" → time-box a short check of the API docs/sandbox for partial refunds before committing; if unsupported, patch the concept (full refunds only) or return to Clarify.

### DERISK-RISK-D02 — Adding a DB field used across features
**Classification:** DERIVED
**Grounded in:** Risks and Rabbit Holes — misunderstood interdependencies; slow-motion walk-through; out of bounds
**Bad:** Add `archived_at` column and filter it in the list view; later discover search, exports and API all return archived records.
**Good:** Walk through every read path in slow motion first; decide explicitly: list view and API filter archived; export and search declared out of bounds for this slice.

### DERISK-RISK-D03 — Browser-specific bug
**Classification:** DERIVED
**Grounded in:** Risks and Rabbit Holes — thin vs fat tail
**Bad:** Commit to "fix Safari date-picker bug today" without reproducing it.
**Good:** Treat it as fat-tailed until reproduced; first step is reproduction and root-cause identification; commit to the fix only once the cause is known.

## ID register
| ID | Stage | Type | Short label | Classification | Location |
|---|---|---|---|---|---|
| DERISK-RISK-01 | DERISK | rule | One hole derails | DIRECT | Intro |
| DERISK-RISK-02 | DERISK | rule | Some problems have no solution | DIRECT | Intro |
| DERISK-RISK-03 | DERISK | rule | Eliminate findable pitfalls | DIRECT | Intro |
| DERISK-RISK-04 | DERISK | rule | Thin vs fat tail | DIRECT | Different categories of risk |
| DERISK-RISK-05 | DERISK | rule | Three rabbit-hole categories | DIRECT | Different categories of risk |
| DERISK-RISK-06 | DERISK | rule | Independent well-understood parts | DIRECT | Different categories of risk |
| DERISK-RISK-07 | DERISK | rule | Slow down, look critically | DIRECT | Look for rabbit holes |
| DERISK-RISK-08 | DERISK | rule | Slow-motion walk-through | DIRECT | Look for rabbit holes |
| DERISK-RISK-09 | DERISK | rule | Viability questions | DIRECT | Look for rabbit holes |
| DERISK-RISK-10 | DERISK | rule | Patch holes | DIRECT | Case study: Patching a hole |
| SLICE-RISK-11 | SLICE | rule | Declare out of bounds | DIRECT | Declare out of bounds |
| SLICE-RISK-12 | SLICE | rule | Cut back | DIRECT | Cut back |
| DERISK-RISK-13 | DERISK | rule | Possible within appetite | DIRECT | Present to technical experts |
| DERISK-RISK-14 | DERISK | rule | Hunt for time bombs | DIRECT | Present to technical experts |
| DERISK-RISK-15 | DERISK | rule | Validate or reshape | DIRECT | Present to technical experts |
| DERISK-RISK-16 | DERISK | rule | Risk relative to time box | INFERRED | Intro; categories |
| DERISK-RISK-17 | DERISK | rule | Polish-for-risk trade | INFERRED | Case study |
| DERISK-RISK-18 | DERISK | gate | Assumed solution = hole | DIRECT | Look for rabbit holes; Intro |
| DERISK-RISK-19 | DERISK | gate | Settle hard decisions | DIRECT | Look for rabbit holes |
| DERISK-RISK-20 | DERISK | gate | Problems → reshape | DIRECT | Present to technical experts |
| COMMIT-RISK-21 | COMMIT | gate | De-risked exit | DIRECT | De-risked and ready to write up |
| DERISK-RISK-Q01 | DERISK | question | New technical work? | DIRECT | Look for rabbit holes |
| DERISK-RISK-Q02 | DERISK | question | Fit assumptions? | DIRECT | Look for rabbit holes |
| DERISK-RISK-Q03 | DERISK | question | Assumed design solution? | DIRECT | Look for rabbit holes |
| DERISK-RISK-Q04 | DERISK | question | Hard decision to settle? | DIRECT | Look for rabbit holes |
| DERISK-RISK-Q05 | DERISK | question | Missed anything / unfair assumptions | DIRECT | Look for rabbit holes |
| DERISK-RISK-Q06 | DERISK | question | Slow-motion path | DIRECT | Look for rabbit holes |
| DERISK-RISK-Q07 | DERISK | question | Possible within appetite | DIRECT | Present to technical experts |
| SLICE-RISK-Q08 | SLICE | question | What's not supported | INFERRED | Declare out of bounds |
| SLICE-RISK-Q09 | SLICE | question | Necessary? | INFERRED | Cut back |
| DERISK-RISK-P01 | DERISK | positive | Completed to-dos patch | DIRECT | Case study: Patching a hole |
| SLICE-RISK-P02 | SLICE | positive | Group notify out of bounds | DIRECT | Declare out of bounds |
| SLICE-RISK-P03 | SLICE | positive | Color coding cut | DIRECT | Cut back |
| DERISK-RISK-N01 | DERISK | negative | Client-projects redesign abandoned | DIRECT | Intro |
| DERISK-RISK-N02 | DERISK | negative | Knot pushed to team | DIRECT | Case study |
| DERISK-RISK-N03 | DERISK | negative | "Is this possible?" | DIRECT | Present to technical experts |
| DERISK-RISK-C01 | DERISK | pair | Possible vs possible-in-appetite | DIRECT | Present to technical experts |
| DERISK-RISK-C02 | DERISK | pair | Thin vs fat tail | DIRECT | Different categories of risk |
| DERISK-RISK-C03 | DERISK | pair | Patch vs leave open | DIRECT | Case study |
| DERISK-RISK-C04 | DERISK | pair | Validated vs assumed solution | DIRECT/INFERRED | Intro |
| DERISK-RISK-D01 | DERISK | derived | Payments API unknown | DERIVED | — |
| DERISK-RISK-D02 | DERISK | derived | DB field interdependencies | DERIVED | — |
| DERISK-RISK-D03 | DERISK | derived | Browser bug fat tail | DERIVED | — |
