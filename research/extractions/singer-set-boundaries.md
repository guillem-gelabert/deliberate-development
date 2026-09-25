# Set Boundaries (Shape Up, ch. 3)

## Source
- Author: Ryan Singer
- URL: https://basecamp.com/shapeup/1.2-chapter-03
- Normalized file: `sources/singer-set-boundaries.md`
- Relevant workflow stages: CLARIFY (narrow the problem), COMMIT (appetite, fixed time/variable scope), SLICE (grab-bag splitting), ESTIMATE (appetite ≠ estimate)

## Core principles

### DIRECT
- **CLARIFY-BOUND-01** The first shaping step is setting boundaries; conversations differ entirely depending on whether people think it's a small improvement or a major redesign. (Intro)
- **COMMIT-BOUND-02** Explicitly define how much time and attention the subject deserves before discussing solutions—quick fix? whole cycle? redesign? minor tweak only? (Setting the appetite)
- **COMMIT-BOUND-03** Appetite = a time budget for a standard team size; set in two sizes: Small Batch (1 designer + 1–2 programmers, 1–2 weeks) and Big Batch (same team, full six weeks). (Setting the appetite)
- **SLICE-BOUND-04** If scope is too big for six weeks, narrow the problem definition; if it still can't shrink, break off a meaningful part that can be shaped to six weeks. (Setting the appetite)
- **ESTIMATE-BOUND-05** "An appetite is completely different from an estimate. Estimates start with a design and end with a number. Appetites start with a number and end with a design." The appetite is a creative constraint on design. (Fixed time, variable scope)
- **COMMIT-BOUND-06** Fixed time, variable scope: a deadline forces decisions between time, quality and scope; without variable scope, quality suffers. Applied at shaping (constrains solution) and building (pushes team to separate core from peripheral). (Fixed time, variable scope)
- **COMMIT-BOUND-07** "Good" is relative to constraints; without a time limit there's always a better version (ten-course dinner vs hot dog). (“Good” is relative)
- **CLARIFY-BOUND-08** Default response to a raw idea: "Interesting. Maybe some day." — a soft no; don't commit to what you don't yet understand; don't put it in a backlog. (Responding to raw ideas)
- **CLARIFY-BOUND-09** Narrow the problem: don't take a request at face value; dig into what's really going wrong. Flip from "What could we build?" to "What's really going wrong?" and ask at what point the workflow breaks down. (Narrow down the problem)
- **CLARIFY-BOUND-10** Ask *when* the person wanted the thing (what were they doing when the thought occurred), not why they want it or what it should look like. (Case study: Defining “calendar”)
- **CLARIFY-BOUND-11** A specific `baseline` (current behavior/workaround) gives something to design against. (Case study: Defining “calendar”)
- **CLARIFY-BOUND-12** Appetite also limits how much research is worthwhile; if the problem isn't critical and can't be pinned down, walk away. (Case study, final paragraph)
- **SLICE-BOUND-13** Watch out for grab-bags: redesigns/refactorings not driven by a single problem or use case; "2.0" is a tell-tale sign. (Watch out for grab-bags)
- **COMMIT-BOUND-14** Boundaries are in place when you have a raw idea, an appetite, and a narrow problem definition. (Boundaries in place)

### INFERRED
- **ESTIMATE-BOUND-15** Appetite answers "how much is this worth?"; an estimate answers "how long will this design take?" They should not be substituted for one another. (Fixed time, variable scope)
- **CLARIFY-BOUND-16** A request is a symptom description; the real problem is found in the concrete situation where the workflow broke. (Narrow down the problem; Case study)

## Procedure / workflow
Not presented as a numbered procedure. INFERRED ordering from the chapter structure:
1. Receive raw idea; respond neutrally, don't commit.
2. Set appetite (how much is it worth).
3. Narrow the problem (ask when/what broke; find baseline).
4. Check for grab-bag; split if so.
5. Gate: raw idea + appetite + narrow problem → proceed to elements.

## Decision rules and gates
- **COMMIT-BOUND-17** Gate: do not move to solution elements until raw idea, appetite, and narrow problem exist. [DIRECT, Boundaries in place]
- **SLICE-BOUND-18** If the work is too big for the appetite: first narrow the problem, then carve off a meaningful part. [DIRECT, Setting the appetite]
- **CLARIFY-BOUND-19** If you can't find a specific pain point and it's not critical, walk away. [DIRECT, Case study]
- **SLICE-BOUND-20** If the work is labeled as a redesign/refactor/"2.0" with no single driving problem, reframe around a specific problem or split into smaller projects. [DIRECT, Watch out for grab-bags]

## Questions the future agent could ask
- **COMMIT-BOUND-Q01** [DIRECT] Is this worth a quick fix? A whole cycle? Would we redesign what exists? Only consider it as a minor tweak? (Setting the appetite)
- **CLARIFY-BOUND-Q02** [DIRECT] What's really going wrong? At what point does the current workflow break down without this? (Narrow down the problem)
- **CLARIFY-BOUND-Q03** [DIRECT] *When* did you want this—what were you doing when it occurred to you? (Case study)
- **SLICE-BOUND-Q04** [DIRECT] What's not working? In what context? What parts can stay the same and what must change? (Watch out for grab-bags)
- **COMMIT-BOUND-Q05** [INFERRED] Given the time we're willing to spend, what is the "good" solution—not the best one? (“Good” is relative)
- **CLARIFY-BOUND-Q06** [INFERRED] What is the baseline—how is this handled today? (Case study)

## Positive examples from the source

### CLARIFY-BOUND-P01 — Permissions → archive warning
**Classification:** DIRECT
**Source location:** Narrow down the problem
**What happens:** A customer asked for more complex permission rules (~six weeks). Digging deeper: someone archived a file not knowing it would disappear for everyone. Fix: a warning on the archive action explaining the impact — a one-day change.
**Why it is positive:** Narrowing to the real failure point shrank scope from six weeks to one day.
**Principle illustrated:** Don't take requests at face value.

### CLARIFY-BOUND-P02 — Defining "calendar" by asking *when*
**Classification:** DIRECT
**Source location:** Case study: Defining “calendar”
**What happens:** Asked a customer when she wanted a calendar; she had to drive to the office to check a wall calendar for free meeting rooms. Need narrowed from "do everything a calendar does" to "help me see free spaces"; baseline was the agenda view that couldn't show empty space.
**Why it is positive:** Produced a specific problem that fit the appetite, leading to the Dot Grid.
**Principle illustrated:** Ask when, find baseline, narrow.

### SLICE-BOUND-P03 — Files 2.0 recovery
**Classification:** DIRECT
**Source location:** Watch out for grab-bags
**What happens:** After the failed "Files 2.0", they split it into "Better file previews" and "Custom folder colors", set appetites and clear expectations on each, and shipped.
**Why it is positive:** Each piece had a clear problem and done-state.
**Principle illustrated:** Split grab-bags into problem-driven projects.

### COMMIT-BOUND-P04 — Book deadline trade-off
**Classification:** DIRECT
**Source location:** Fixed time, variable scope
**What happens:** With one week left, the author chooses fixing typos over adding a new section.
**Why it is positive:** Fixed time forces a scope decision that protects quality.
**Principle illustrated:** Fixed time, variable scope.

## Negative examples / anti-patterns from the source

### SLICE-BOUND-N01 — Files 2.0
**Classification:** DIRECT
**Source location:** Watch out for grab-bags
**What happens:** Kicked off "Files 2.0" without considering what it meant; didn't know what "done" looked like; project was a mess.
**Why it is negative:** Grab-bag with no single problem; no start/end.
**Principle violated:** Narrow problem definition.

### CLARIFY-BOUND-N02 — "Redesign the Files section"
**Classification:** DIRECT
**Source location:** Watch out for grab-bags
**What happens:** A proposal with no driving problem; hard to know what it means, where it starts and ends.
**Why it is negative:** Grab-bag.
**Principle violated:** Problem-driven scope.

### CLARIFY-BOUND-N03 — Jumping in on excitement / always saying yes
**Classification:** DIRECT
**Source location:** Setting the appetite; Responding to raw ideas
**What happens:** Excitement leads to committing resources or long solution discussions without checking value; always saying "yes" yields an ever-growing pile.
**Why it is negative:** Commitment before understanding.
**Principle violated:** Set appetite first; soft no.

## Contrastive pairs

### ESTIMATE-BOUND-C01 — Appetite vs estimate
**Good / preferred:** Appetite: start with a number (time worth spending), end with a design that fits it.
**Bad / discouraged:** Treating the appetite as if it were an estimate (start with a design, end with a number).
**Classification:** DIRECT (the distinction); the "bad" framing as confusion is INFERRED.
**Source location:** Fixed time, variable scope
**Distinguishing feature:** Direction of derivation: number→design vs design→number.

### SLICE-BOUND-C02 — Grab-bag vs problem-driven
**Good / preferred:** "Rethink the Files section because sharing multiple files takes too many steps."
**Bad / discouraged:** "Redesign the Files section" / "Files 2.0".
**Classification:** DIRECT
**Source location:** Watch out for grab-bags
**Distinguishing feature:** A single named problem that defines start and end.

### CLARIFY-BOUND-C03 — Face value vs narrowed request
**Good / preferred:** Archive warning (one day), after finding the real failure.
**Bad / discouraged:** Complex permission rules as requested (six weeks).
**Classification:** DIRECT
**Source location:** Narrow down the problem
**Distinguishing feature:** Solving the concrete breakdown vs the requested solution.

### CLARIFY-BOUND-C04 — Ask when vs ask why/what
**Good / preferred:** Ask *when* she wanted a calendar.
**Bad / discouraged:** Ask why she wants a calendar and what it should look like.
**Classification:** DIRECT
**Source location:** Case study: Defining “calendar”
**Distinguishing feature:** Concrete situation vs abstract justification/design.

## Stop / go criteria

### GO
- Raw idea + appetite + narrow problem definition are all present (COMMIT-BOUND-17).

### STOP / RETURN
- No appetite has been stated → set one before discussing solutions.
- Request taken at face value, no failure point identified → narrow.
- Grab-bag / "2.0" / redesign without problem → reframe or split.
- Too big for the largest appetite → narrow, then carve off a meaningful part.
- No specific pain point and not critical → walk away.

## Common failure modes
- Excitement → premature commitment or endless solution talk.
- Always saying yes → growing pile.
- Taking the request literally.
- Grab-bag projects without a "done."
- Conflating appetite with estimate.

## Terms worth preserving
- `raw idea` — an unshaped request ("customers are asking for group notifications").
- `appetite` — time budget for a standard team size; a creative constraint.
- `Small Batch` / `Big Batch` — 1–2 weeks / six weeks for 1 designer + 1–2 programmers.
- `fixed time, variable scope` — deadline fixed, scope flexes.
- `baseline` — the current reality/workaround the design is compared against.
- `grab-bag` — unfocused bundle (redesign/refactor/"2.0") not driven by one problem.

## Candidate Skill rules
- `[DERIVED from Setting the appetite]` Before discussing solutions, state how much time the work is worth.
- `[DERIVED from Fixed time, variable scope]` Do not treat an appetite as an estimate or vice versa; record them separately.
- `[DERIVED from Narrow down the problem]` Do not implement the requested solution at face value; first identify the concrete point where the current behavior breaks.
- `[DERIVED from Case study]` Ask when/in what situation the problem appeared, and record the baseline behavior.
- `[DERIVED from Watch out for grab-bags]` If the task is a "refactor/redesign/v2" with no single driving problem, return to Clarify and name the problem, or split.
- `[DERIVED from Boundaries in place]` Do not proceed until problem, appetite and narrow definition are written down.
- `[DERIVED from Case study, last paragraph]` If no specific pain point can be found and it isn't critical, recommend dropping it.

## Source limitations
- Appetite is defined at team scale (1–2 weeks / six weeks). Setting an appetite for an individual developer's hours/days slice is an adaptation, not source-supported.
- Assumes access to customers and product authority to say "maybe some day"; an individual developer usually receives assigned tickets—they can propose narrowing but often can't decline.
- Addresses product features, not bug fixes or technical debt directly (though it warns against problem-less refactorings).
- No method for estimating; explicitly separates appetite from estimation.

## Derived developer examples

### CLARIFY-BOUND-D01 — "Refactor the auth module"
**Classification:** DERIVED
**Grounded in:** Set Boundaries — grab-bags; problem-driven framing
**Bad:** Start a branch "auth-v2" rewriting session handling, token refresh and role checks together.
**Good:** Name the problem: "Token refresh races cause random logouts on multi-tab use." Scope: refresh logic only; roles and session storage unchanged.

### CLARIFY-BOUND-D02 — Form validation request
**Classification:** DERIVED
**Grounded in:** Set Boundaries — narrow the problem; ask when
**Bad:** "Add full client-side validation to the signup form" → developer adds a validation library and rules for every field.
**Good:** Ask when users hit problems: support tickets show failures only from mistyped emails causing undeliverable confirmations. Slice: email format check + confirmation field; other fields unchanged.

### COMMIT-BOUND-D03 — Appetite vs estimate for an endpoint
**Classification:** DERIVED
**Grounded in:** Set Boundaries — appetite ≠ estimate
**Bad:** "It'll take as long as it takes" — design a fully filterable/paginated endpoint and then estimate 5 days.
**Good:** "This is worth ~1 day" (appetite, adapted to individual scale) → design fits: one fixed filter, simple limit/offset; then estimate that design separately.

## ID register
| ID | Stage | Type | Short label | Classification | Location |
|---|---|---|---|---|---|
| CLARIFY-BOUND-01 | CLARIFY | rule | Boundaries first | DIRECT | Intro |
| COMMIT-BOUND-02 | COMMIT | rule | Define time/attention deserved | DIRECT | Setting the appetite |
| COMMIT-BOUND-03 | COMMIT | rule | Appetite; Small/Big Batch | DIRECT | Setting the appetite |
| SLICE-BOUND-04 | SLICE | rule | Too big → narrow, then carve | DIRECT | Setting the appetite |
| ESTIMATE-BOUND-05 | ESTIMATE | rule | Appetite ≠ estimate | DIRECT | Fixed time, variable scope |
| COMMIT-BOUND-06 | COMMIT | rule | Fixed time, variable scope | DIRECT | Fixed time, variable scope |
| COMMIT-BOUND-07 | COMMIT | rule | Good is relative | DIRECT | “Good” is relative |
| CLARIFY-BOUND-08 | CLARIFY | rule | Soft no to raw ideas | DIRECT | Responding to raw ideas |
| CLARIFY-BOUND-09 | CLARIFY | rule | What's really going wrong | DIRECT | Narrow down the problem |
| CLARIFY-BOUND-10 | CLARIFY | rule | Ask when | DIRECT | Case study |
| CLARIFY-BOUND-11 | CLARIFY | rule | Baseline | DIRECT | Case study |
| CLARIFY-BOUND-12 | CLARIFY | rule | Appetite limits research; walk away | DIRECT | Case study |
| SLICE-BOUND-13 | SLICE | rule | Grab-bags / 2.0 | DIRECT | Watch out for grab-bags |
| COMMIT-BOUND-14 | COMMIT | rule | Boundaries in place triad | DIRECT | Boundaries in place |
| ESTIMATE-BOUND-15 | ESTIMATE | rule | Don't substitute appetite/estimate | INFERRED | Fixed time, variable scope |
| CLARIFY-BOUND-16 | CLARIFY | rule | Request is a symptom | INFERRED | Narrow down; Case study |
| COMMIT-BOUND-17 | COMMIT | gate | Triad gate | DIRECT | Boundaries in place |
| SLICE-BOUND-18 | SLICE | gate | Narrow then carve | DIRECT | Setting the appetite |
| CLARIFY-BOUND-19 | CLARIFY | gate | Walk away | DIRECT | Case study |
| SLICE-BOUND-20 | SLICE | gate | Reframe/split grab-bag | DIRECT | Watch out for grab-bags |
| COMMIT-BOUND-Q01 | COMMIT | question | How much is it worth | DIRECT | Setting the appetite |
| CLARIFY-BOUND-Q02 | CLARIFY | question | What's really going wrong | DIRECT | Narrow down the problem |
| CLARIFY-BOUND-Q03 | CLARIFY | question | When did you want this | DIRECT | Case study |
| SLICE-BOUND-Q04 | SLICE | question | What's not working / what stays | DIRECT | Watch out for grab-bags |
| COMMIT-BOUND-Q05 | COMMIT | question | Good within appetite | INFERRED | “Good” is relative |
| CLARIFY-BOUND-Q06 | CLARIFY | question | Baseline today | INFERRED | Case study |
| CLARIFY-BOUND-P01 | CLARIFY | positive | Archive warning | DIRECT | Narrow down the problem |
| CLARIFY-BOUND-P02 | CLARIFY | positive | Ask when (calendar) | DIRECT | Case study |
| SLICE-BOUND-P03 | SLICE | positive | Files 2.0 recovery by split | DIRECT | Watch out for grab-bags |
| COMMIT-BOUND-P04 | COMMIT | positive | Book typos vs section | DIRECT | Fixed time, variable scope |
| SLICE-BOUND-N01 | SLICE | negative | Files 2.0 | DIRECT | Watch out for grab-bags |
| CLARIFY-BOUND-N02 | CLARIFY | negative | Redesign Files section | DIRECT | Watch out for grab-bags |
| CLARIFY-BOUND-N03 | CLARIFY | negative | Excitement / always yes | DIRECT | Setting the appetite; Responding |
| ESTIMATE-BOUND-C01 | ESTIMATE | pair | Appetite vs estimate | DIRECT | Fixed time, variable scope |
| SLICE-BOUND-C02 | SLICE | pair | Grab-bag vs problem-driven | DIRECT | Watch out for grab-bags |
| CLARIFY-BOUND-C03 | CLARIFY | pair | Face value vs narrowed | DIRECT | Narrow down the problem |
| CLARIFY-BOUND-C04 | CLARIFY | pair | Ask when vs why | DIRECT | Case study |
| CLARIFY-BOUND-D01 | CLARIFY | derived | Auth refactor grab-bag | DERIVED | — |
| CLARIFY-BOUND-D02 | CLARIFY | derived | Form validation narrowed | DERIVED | — |
| COMMIT-BOUND-D03 | COMMIT | derived | Appetite vs estimate endpoint | DERIVED | — |
