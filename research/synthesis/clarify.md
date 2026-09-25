# Clarify

## Purpose
Make the desired behavior concrete enough that someone could write a test for it, and narrow the request to the real problem. Examples and scenarios are the main tool. Clarify does **not** set size or effort; Slice, Estimate and Commit handle those.

## Primary grounding sources
- Fowler, *Specification By Example*: primary for concrete examples as specs and their limits.
- Fowler, *Given When Then*: primary for scenario structure.
- Singer, *Set Boundaries*: primary for narrowing the problem, "ask when", baseline and grab-bags.
- Singer, *Principles of Shaping*: primary for the right level of abstraction.
- Wake, *INVEST*: supporting. Testable, Negotiable, Card/Conversation/Confirmation.
- Beck, *Canon TDD*: supporting. The test list as behavioral analysis.

## Entry conditions
- Orient is done, or the developer knowingly skipped it and knows the relevant current behavior.

## Agent questions
1. What is really going wrong, and at what point does the current workflow break down? (DIRECT, CLARIFY-BOUND-Q02)
2. *When* did the requester want this, and what were they doing at that moment? (DIRECT, CLARIFY-BOUND-Q03)
3. Can you give concrete examples with a starting state, one action and the expected outcome? (INFERRED, CLARIFY-SBE-Q01 + CLARIFY-GWT-Q01/Q02)
4. Could you write a test for this right now? If not, is it unclear, not valuable, or do you need help testing it? (DIRECT, CLARIFY-INVEST-03/-04)
5. What are all the expected variants (basic case, failures, missing data), and what existing behavior must not change? (DIRECT, CLARIFY-BECK-Q01/Q02)
6. Would a hard-coded implementation pass these examples? If so, what example is missing? (INFERRED, CLARIFY-SBE-Q03)

## Rules
- **Narrow the problem before designing a solution.** Flip from "What could we build?" to "What's really going wrong?" (DIRECT, CLARIFY-BOUND-09)
- **Ask *when*, not why.** Get the concrete situation in which the need arose. (DIRECT, CLARIFY-BOUND-10)
- **Use concrete examples as the specification.** They are easier to produce than general pre/post conditions and easy to check against the implementation. (DIRECT, CLARIFY-SBE-01/-03/-04)
- **Structure each example as Given (pre-state) / When (the one behavior) / Then (expected changes).** (DIRECT, CLARIFY-GWT-02)
- **Examples are never the whole spec.** Back them with conversation and other techniques, and do not treat a written spec as the end of communication. (DIRECT, CLARIFY-SBE-02/-06/-07)
- **Pitch the shaped description at the right level:** neither wireframe-concrete nor a few vague words. (DIRECT, CLARIFY-SHAPING-01/-02/-04)
- **A story is testable if you could write a test for it.** If you can't, clarify further first. (DIRECT, CLARIFY-INVEST-03/-07)
- **Keep behavior separate from implementation.** The test list is behavioral analysis only. (DIRECT, CLARIFY-BECK-01; IMPLEMENT-BECK-N01)

## Positive patterns
- The permission request narrowed to "archiving hides a file for everyone" led to a warning on the archive action: one day instead of six weeks. (DIRECT, CLARIFY-BOUND-P01)
- Calling the customer and asking *when* she wanted a calendar surfaced the real need, "see free spaces". (DIRECT, CLARIFY-BOUND-P02)
- The stock-sell scenario states the pre-state for two holdings, one action, and outcomes that include the *unchanged* holding. (DIRECT, CLARIFY-GWT-P01)
- Stack LIFO behavior is easy to show with examples but hard to state with pre/post conditions. (DIRECT, CLARIFY-SBE-P01)

## Anti-patterns
- "Build a calendar view" or "add group notifications": too abstract, so nobody knows what is in or out. (DIRECT, CLARIFY-SHAPING-N02)
- Handing over a wireframe, which is too concrete and hides complexity. (DIRECT, CLARIFY-SHAPING-N01)
- "Redesign the Files section": a grab-bag, not a problem. (DIRECT, CLARIFY-BOUND-N02)
- Thinking you're done communicating once the spec is written. (DIRECT, CLARIFY-SBE-N01)
- Taking the card as the whole story and forgetting the conversation and confirmation. (DIRECT, CLARIFY-INVEST-N02)
- Mixing implementation decisions into the list of behaviors. (DIRECT, IMPLEMENT-BECK-N01)

## Contrastive examples

**CLARIFY-SYN-D01: Adding validation to a form** (DERIVED; grounded in CLARIFY-BOUND-09, CLARIFY-GWT-02, CLARIFY-SBE-Q03)
- *Preferred:* "Given a signup form with email `a@b`, when the user submits, then the form shows 'Enter a full email address' and no request is sent. Given `ann@example.com` with trailing spaces, when submitted, then it is accepted and stored trimmed." The request was traced to support tickets about typo'd emails.
- *Discouraged:* "Add full validation to the signup form." No examples, no trigger, and no way to tell when it is done.
- *Distinguishing feature:* concrete pre-state, action and outcome, plus the real problem behind the request.

**CLARIFY-SYN-D02: Changing an API response** (DERIVED; grounded in CLARIFY-BECK-01, CLARIFY-GWT-P01 unchanged-state pattern)
- *Preferred:* Examples for the new `currency` field, **plus** an example saying existing fields and their types are unchanged for current clients.
- *Discouraged:* Examples only for the new field, so the regression surface stays invisible.

## Stop / return conditions
- No concrete example can be produced → the problem isn't understood. Return to narrowing (Set Boundaries) or Orient.
- No specific pain point can be found → the appetite limits how much research is worthwhile. Walk away for now. (DIRECT, CLARIFY-BOUND-12/-19)
- The request is a redesign, refactor or "2.0" with no single problem → reframe it around one problem or split it (→ Slice). (DIRECT, SLICE-BOUND-20)
- Examples keep adding "and"-joined behaviors → Slice. (DIRECT, SLICE-INDEP-05, SLICE-SPLIT-11)

## Exit criteria
- A narrowed problem statement tied to a concrete situation.
- A set of Given/When/Then examples that includes the must-not-break behavior.
- A sentence stating what is out of scope. This overlaps with De-risk (declare out of bounds).

## Unresolved tensions between sources
- **Completeness.** Beck's test list aims to capture "all the expected variants". Fowler says examples are always incomplete and must be backed by other mechanisms. These two can coexist: the list is exhaustive *as an intention* and never a proof.
- **Level of detail.** Shape Up wants *rough* shaped work that leaves room for builders. Specification by Example wants *concrete* examples. They operate at different levels (solution outline vs behavioral examples), and the Skill should not merge them.
- Specification by Example says nothing about effort. Concrete examples do not by themselves make work estimable.

## Provenance map
| Rule / example | Source | Classification | Source section |
|---|---|---|---|
| Narrow the problem (what's going wrong) | Singer, Set Boundaries | DIRECT | Narrow down the problem |
| Ask when, not why | Singer, Set Boundaries | DIRECT | Case study: Defining "calendar" |
| Examples as specs; easier than pre/post | Fowler, SbE | DIRECT | paras 1, 4 |
| Tests incomplete; not the only tool | Fowler, SbE | DIRECT | paras 3, 7, 8 |
| Given/When/Then semantics | Fowler, GWT | DIRECT | para 2 |
| Right level of abstraction | Singer, Principles of Shaping | DIRECT | Wireframes / Words |
| Testable = could write a test | Wake, INVEST | DIRECT | Testable |
| Test list = behavioral analysis | Beck, Canon TDD | DIRECT | 1. Test List |
| Grab-bags | Singer, Set Boundaries | DIRECT | Watch out for grab-bags |
| CLARIFY-SYN-D01, D02 | — | DERIVED | — |
