# Principles of Shaping (Shape Up, ch. 2)

## Source
- Author: Ryan Singer
- URL: https://basecamp.com/shapeup/1.1-chapter-02
- Normalized file: `sources/singer-principles-of-shaping.md`
- Relevant workflow stages: CLARIFY (level of abstraction), DERISK (solved), COMMIT (bounded/appetite), SLICE (secondary: what's in/out)

## Core principles

### DIRECT
- **CLARIFY-SHAPING-01** Work must be shaped at the right level of abstraction: neither too vague nor too concrete. (Intro)
- **CLARIFY-SHAPING-02** Going straight to wireframes/high-fidelity mockups defines too much detail too early, leaving no room for the builders' judgement. (Wireframes are too concrete)
- **ESTIMATE-SHAPING-03** Over-specifying makes work *harder* to estimate: making the interface "just so" can require solving hidden complexities not visible in the mockup; when scope isn't variable, the team can't reconsider a decision that costs more than it's worth. (Wireframes are too concrete)
- **CLARIFY-SHAPING-04** Projects defined in a few words ("Build a calendar view", "add group notifications") are too abstract: nobody knows what they entail, so trade-offs can't be made and there's no boundary for what's out of scope; they "naturally grow out of control." (Words are too abstract)
- **CLARIFY-SHAPING-05** Shaped work has three properties: **rough** (visibly unfinished, room for builders' judgement), **solved** (main elements at macro level thought through and connected; open questions/rabbit holes visible up front removed), **bounded** (says what *not* to do; a specific appetite; specific things left out). (Property 1–3)
- **DERISK-SHAPING-06** "Solved" does not mean specified down to tasks; surprises may still happen, but there is clear direction. (Property 2: It's solved)
- **COMMIT-SHAPING-07** "Bounded" means there is a specific appetite—the time the team is allowed to spend—and fitting it requires limiting scope. (Property 3: It's bounded)
- **DERISK-SHAPING-08** Unshaped work is risky and unknown and therefore can't really be scheduled; shaping and building run on separate tracks. (Two tracks)
- **CLARIFY-SHAPING-09** Shaping requires asking critically: What are we trying to solve? Why does it matter? What counts as success? Which customers are affected? What is the cost of doing this instead of something else? (Who shapes)
- **DERISK-SHAPING-10** Shapers must be technically literate: able to judge what's possible, easy, hard, using knowledge of how the system works. (Who shapes)

### INFERRED
- **DERISK-SHAPING-11** Readiness to build is a property of the *work*, not of the calendar: work lacking any of rough/solved/bounded is not yet ready to commit to. (Properties; Two tracks)
- **ESTIMATE-SHAPING-12** Both extremes damage estimation, for different reasons: concrete specs hide complexity inside fixed details; abstract specs have no boundary. (Wireframes / Words)

## Procedure / workflow
DIRECT — the source presents four shaping steps (Steps to shaping):
1. **Set boundaries** — how much time the raw idea is worth; define the problem.
2. **Rough out the elements** — sketch a solution above wireframe level that solves the problem within the appetite.
3. **Address risks and rabbit holes** — find holes/unanswered questions; amend, cut, or specify tricky spots.
4. **Write the pitch** — problem, constraints, solution, rabbit holes, limitations; goes to the betting table.

## Decision rules and gates
- **DERISK-SHAPING-13** Gate: work is ready to bet/build when it is rough, solved, and bounded. [INFERRED from Properties 1–3 + "Taken together…"]
- **CLARIFY-SHAPING-14** If a request is only a few words (a feature name), it is too abstract to build or estimate — shape it further. [INFERRED from Words are too abstract]
- **CLARIFY-SHAPING-15** If the definition fixes pixel-level details, loosen it so the builder can re-trade details that turn out costly. [INFERRED from Wireframes are too concrete]

## Questions the future agent could ask
- **CLARIFY-SHAPING-Q01** [DIRECT] What are we trying to solve? Why does it matter? What counts as success? (Who shapes)
- **CLARIFY-SHAPING-Q02** [DIRECT] Which customers are affected? What is the cost of doing this instead of something else? (Who shapes)
- **CLARIFY-SHAPING-Q03** [INFERRED] Is it clear what's in and what's out? (Dot Grid: "what's in and what's out")
- **DERISK-SHAPING-Q04** [INFERRED] Are the main elements of the solution known and do they connect, or are there open questions we can already see? (Property 2)
- **CLARIFY-SHAPING-Q05** [DERIVED] Is this description a feature name, a pixel-exact spec, or something in between that says how it works without fixing every detail?

## Positive examples from the source

### CLARIFY-SHAPING-P01 — The Dot Grid
**Classification:** DIRECT
**Source location:** Case study: The Dot Grid Calendar
**What happens:** Customers asked to "add a calendar." A full calendar could take 6+ months; only ~10% of customers used past calendars, so there was no appetite for that, but there was for one six-week cycle. The team narrowed a use case and defined a two-month read-only grid with dots per event and a list below; explicitly no dragging, no multi-day spans (repeat dots), no color coding. The rough sketch left visual design open but was specific about how it works and what's in/out.
**Why it is positive:** Rough (designers had room), solved (clear how it works), bounded (explicit exclusions, fits six weeks).
**Principle illustrated:** Right level of abstraction; bounded by appetite; explicit exclusions.

## Negative examples / anti-patterns from the source

### CLARIFY-SHAPING-N01 — Wireframe hand-off
**Classification:** DIRECT
**Source location:** Wireframes are too concrete
**What happens:** A design lead gives a designer a wireframe but wants them to rethink it; the concrete artifact makes that hard.
**Why it is negative:** Too much detail too early removes room for judgement and causes estimation errors via hidden complexity.
**Principle violated:** Rough.

### CLARIFY-SHAPING-N02 — "Build a calendar view"
**Classification:** DIRECT
**Source location:** Words are too abstract
**What happens:** A project defined in a few words; a programmer describes it as "solving a problem with no context… we'll know it when we see it."
**Why it is negative:** No information for trade-offs; no boundary; scope grows out of control.
**Principle violated:** Solved / bounded.

### CLARIFY-SHAPING-N03 — Calendar complexity list
**Classification:** DIRECT
**Source location:** Case study: The Dot Grid Calendar
**What happens:** The source lists what makes a "proper calendar" expensive (drag-drop between cells, wrapping multi-day events, month/week/day views, drag to resize, color coding, desktop vs mobile expectations).
**Why it is negative:** Taking the request at face value would pull in all of these.
**Principle violated:** Bounded.

## Contrastive pairs

### CLARIFY-SHAPING-C01 — Level of abstraction
**Good / preferred:** Rough-but-specific concept (Dot Grid sketch): how it works and what's in/out is clear; visual detail is open.
**Bad / discouraged:** (a) Wireframe/high-fidelity mockup up front; (b) a few-word project name.
**Classification:** DIRECT
**Source location:** Wireframes are too concrete; Words are too abstract; Case study
**Distinguishing feature:** Specific about mechanism and boundaries, unspecific about fine detail.

### ESTIMATE-SHAPING-C02 — Why each extreme breaks estimation
**Good / preferred:** Bounded concept with variable scope, so a costly detail can be reconsidered.
**Bad / discouraged:** Concrete spec with fixed scope (hidden complexity, can't renegotiate) or abstract spec (no boundary, grows out of control).
**Classification:** DIRECT
**Source location:** Wireframes are too concrete; Words are too abstract
**Distinguishing feature:** Whether a boundary exists *and* scope can flex.

## Stop / go criteria

### GO
- The work is rough, solved, and bounded (DERISK-SHAPING-13).
- Main elements are connected at macro level and visible rabbit holes are removed.

### STOP / RETURN
- The work is defined only by a name/few words → return to shaping/clarifying.
- The work is fixed in pixel/implementation detail with fixed scope → loosen.
- Unshaped/risky work is being scheduled as if it were build-ready → move it to the shaping track (DERISK-SHAPING-08).

## Common failure modes
- Erring to one extreme of abstraction (Intro; both sections).
- Treating a feature label as a specification.
- Fixing details that turn out to cost more than they're worth, with no scope flexibility.

## Terms worth preserving
- `shaping` — pre-work that makes an idea rough, solved, and bounded before commitment.
- `appetite` — the amount of time the team is allowed to spend on the project.
- `pitch` — write-up of problem, constraints, solution, rabbit holes, limitations.
- `betting table` — where pitches are considered for a cycle.
- `rough / solved / bounded` — the three properties of shaped work.
- `two tracks` — shaping and building run in parallel on separate tracks.

## Candidate Skill rules
- `[DERIVED from Words are too abstract]` Do not start implementing from a feature name alone; first state how it works and what is out.
- `[DERIVED from Wireframes are too concrete]` Do not lock in fine-grained details before the mechanism is settled; keep details negotiable when they turn out costly.
- `[DERIVED from Properties 1–3]` Before committing, check the work is rough, solved, and bounded; if any is missing, return to Clarify or De-risk.
- `[DERIVED from Two tracks]` If the work is still unknown/risky, treat it as shaping/investigation, not as scheduled build work.
- `[DERIVED from Who shapes]` Ask what problem is being solved, why it matters, and what counts as success before choosing a solution.

## Source limitations
- Written for product-level shaping by a senior shaper/small group for a team; not about an individual developer's task loop. For one developer, shaper and builder roles collapse into one person—an adaptation.
- The appetite scale is 1–6 weeks for a team; applying "bounded" at hours/days scale is not source-supported.
- Shaping is described as design work (interaction design from the user's perspective); it says little about purely technical tasks (refactors, bug fixes).
- No guidance on understanding existing code state (Orient).

## Derived developer examples

### CLARIFY-SHAPING-D01 — "Add CSV export"
**Classification:** DERIVED
**Grounded in:** Principles of Shaping — words too abstract vs. rough/solved/bounded
**Bad:** Ticket says "Add CSV export to reports." Developer starts building a generic exporter for every report type with column pickers.
**Good:** Before coding, state: export of the *orders* report only, current filters applied, fixed columns matching the on-screen table, synchronous download up to N rows; out: other reports, column selection, scheduled exports. Visual placement of the button left open.
**Distinguishing feature:** Mechanism and exclusions are explicit; cosmetic detail is not.

### CLARIFY-SHAPING-D02 — Pixel-perfect modal
**Classification:** DERIVED
**Grounded in:** Principles of Shaping — wireframes too concrete / estimation errors
**Bad:** Developer commits to a mockup's animated, focus-trapped modal exactly as drawn, then discovers the component library can't do it; spends two days on the animation.
**Good:** Treat the mockup's animation as negotiable; confirm the required behavior (confirm/cancel, keyboard accessible) and flag the animation as a detail to reconsider if costly.

## ID register
| ID | Stage | Type | Short label | Classification | Location |
|---|---|---|---|---|---|
| CLARIFY-SHAPING-01 | CLARIFY | rule | Right level of abstraction | DIRECT | Intro |
| CLARIFY-SHAPING-02 | CLARIFY | rule | Wireframes too concrete | DIRECT | Wireframes are too concrete |
| ESTIMATE-SHAPING-03 | ESTIMATE | rule | Over-specifying hurts estimation | DIRECT | Wireframes are too concrete |
| CLARIFY-SHAPING-04 | CLARIFY | rule | Words too abstract; no boundary | DIRECT | Words are too abstract |
| CLARIFY-SHAPING-05 | CLARIFY | rule | Rough / solved / bounded | DIRECT | Property 1–3 |
| DERISK-SHAPING-06 | DERISK | rule | Solved ≠ tasked out | DIRECT | Property 2 |
| COMMIT-SHAPING-07 | COMMIT | rule | Bounded = appetite + scope limits | DIRECT | Property 3 |
| DERISK-SHAPING-08 | DERISK | rule | Unshaped work can't be scheduled | DIRECT | Two tracks |
| CLARIFY-SHAPING-09 | CLARIFY | rule | Strategic shaping questions | DIRECT | Who shapes |
| DERISK-SHAPING-10 | DERISK | rule | Technical literacy to judge easy/hard | DIRECT | Who shapes |
| DERISK-SHAPING-11 | DERISK | rule | Readiness is property of the work | INFERRED | Properties; Two tracks |
| ESTIMATE-SHAPING-12 | ESTIMATE | rule | Both extremes damage estimation | INFERRED | Wireframes / Words |
| DERISK-SHAPING-13 | DERISK | gate | Rough+solved+bounded gate | INFERRED | Properties |
| CLARIFY-SHAPING-14 | CLARIFY | gate | Few words → shape further | INFERRED | Words are too abstract |
| CLARIFY-SHAPING-15 | CLARIFY | gate | Pixel detail → loosen | INFERRED | Wireframes are too concrete |
| CLARIFY-SHAPING-Q01 | CLARIFY | question | Solve / matter / success | DIRECT | Who shapes |
| CLARIFY-SHAPING-Q02 | CLARIFY | question | Who affected / opportunity cost | DIRECT | Who shapes |
| CLARIFY-SHAPING-Q03 | CLARIFY | question | What's in and out | INFERRED | Case study |
| DERISK-SHAPING-Q04 | DERISK | question | Elements connected, open questions | INFERRED | Property 2 |
| CLARIFY-SHAPING-Q05 | CLARIFY | question | Name vs spec vs shaped | DERIVED | — |
| CLARIFY-SHAPING-P01 | CLARIFY | positive | Dot Grid | DIRECT | Case study |
| CLARIFY-SHAPING-N01 | CLARIFY | negative | Wireframe hand-off | DIRECT | Wireframes are too concrete |
| CLARIFY-SHAPING-N02 | CLARIFY | negative | "Build a calendar view" | DIRECT | Words are too abstract |
| CLARIFY-SHAPING-N03 | CLARIFY | negative | Full-calendar complexity list | DIRECT | Case study |
| CLARIFY-SHAPING-C01 | CLARIFY | pair | Level of abstraction | DIRECT | Wireframes/Words/Case study |
| ESTIMATE-SHAPING-C02 | ESTIMATE | pair | Why extremes break estimation | DIRECT | Wireframes/Words |
| CLARIFY-SHAPING-D01 | CLARIFY | derived | CSV export shaped | DERIVED | — |
| CLARIFY-SHAPING-D02 | CLARIFY | derived | Pixel-perfect modal | DERIVED | — |
