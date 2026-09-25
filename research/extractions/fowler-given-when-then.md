# Given When Then

## Source
- Author: Martin Fowler
- URL: https://martinfowler.com/bliki/GivenWhenThen.html (2013-08-21)
- Normalized file: `sources/fowler-given-when-then.md`
- Relevant workflow stages: CLARIFY (primary: scenario structure); IMPLEMENT (supporting: test structure)

## Core principles

### DIRECT
- **CLARIFY-GWT-01** — Given-When-Then is a style for representing tests, or for specifying a system's behavior using Specification By Example. It comes from BDD (Terhorst-North, Matts). *(para 1)*
- **CLARIFY-GWT-02** — Split a scenario into three sections: **given**, the state of the world before the behavior (pre-conditions); **when**, the behavior being specified; **then**, the changes expected due to that behavior. *(para 2 list)*
- **CLARIFY-GWT-03** — "And" is commonly used to combine multiple expressions within each clause. *(after example)*
- **IMPLEMENT-GWT-01** — Frameworks interpret *givens* as commands that bring the system under test into the right state ("setup"). *Then* clauses are queries and "should be free of side-effects". *(para on pre-condition state)*
- **IMPLEMENT-GWT-02** — The style is not limited to Cucumber/Gherkin or business-facing tests. It can mark informal blocks inside unit tests, and can structure informal prose. *(after example)*
- **IMPLEMENT-GWT-03** — Equivalent formulations: Meszaros's Four-Phase Test (Setup=Given, Exercise=When, Verify=Then, plus Teardown) and Wake's Arrange-Act-Assert. Teardown adds little to specification by example's communication role. *(final para; note 5)*

### INFERRED
- **CLARIFY-GWT-04** — A scenario specifies one behavior (the single *when*). Pre-conditions and expected changes are stated explicitly, including things that should *not* change (the example asserts APPL holdings stay at 150). *(example)*
- **CLARIFY-GWT-05** — Fowler describes *given* as a state description rather than a list of setup steps. This keeps the scenario readable as a specification. *(pre-condition para)*

## Procedure / workflow
No procedure is presented, only a three-part structure (CLARIFY-GWT-02). Not a DIRECT workflow.

## Decision rules and gates
- **CLARIFY-GWT-06** — Each scenario should have a clear pre-condition state, the behavior under specification, and expected changes. *(para 2)* — DIRECT (structure)
- **IMPLEMENT-GWT-04** — Keep *then* checks free of side-effects. *(pre-condition para)* — DIRECT

## Questions the future agent could ask
- **CLARIFY-GWT-Q01** — What is the state of the world before this behavior starts (given)? `[DIRECT]` *(para 2)*
- **CLARIFY-GWT-Q02** — What exactly is the one action or behavior we are specifying (when)? `[DIRECT]` *(para 2)*
- **CLARIFY-GWT-Q03** — What changes do we expect as a result, and what should stay the same (then)? `[INFERRED]` *(para 2 + example)*
- **CLARIFY-GWT-Q04** — Are there other pre-conditions (e.g., time of day) that change the outcome and deserve their own scenario? `[DERIVED]` (suggested by the "before close of trading" given)

## Positive examples from the source

### CLARIFY-GWT-P01 — User sells stock before close of trading
**Classification:** DIRECT
**Source location:** example (from Pete Hodgson)
**What happens:** Given 100 MSFT and 150 APPL shares, and the time is before close of trading; When I ask to sell 20 MSFT; Then I have 80 MSFT, still 150 APPL, and a sell order for 20 MSFT was executed.
**Why it is positive:** Fowler presents it as the illustration of the style. Each clause is concrete; the time pre-condition is explicit; the *then* includes an unchanged-state check and an observable side effect (order executed).
**Principle illustrated:** CLARIFY-GWT-02, CLARIFY-GWT-03, CLARIFY-GWT-04.

## Negative examples / anti-patterns from the source
The source gives essentially no negative examples. The only cautionary note:

### IMPLEMENT-GWT-N01 — Side-effecting *then* queries
**Classification:** DIRECT (stated as a "should", no scenario)
**Source location:** pre-condition paragraph
**What happens:** Then-clauses implemented with queries that change state.
**Why it is negative:** Fowler says *then* query methods "should be free of side-effects".
**Principle violated:** IMPLEMENT-GWT-04.

## Contrastive pairs
The source contains no DIRECT contrastive pairs.

### CLARIFY-GWT-C01 — Concrete scenario vs. vague requirement (DERIVED)
**Good / preferred:** A GWT scenario with explicit pre-state, one action, and expected changes (including unchanged state).
**Bad / discouraged:** "User can sell stock."
**Classification:** DERIVED
**Source location:** built on the example
**Distinguishing feature:** Whether pre-conditions, trigger and outcome are explicit and checkable.

## Stop / go criteria

### GO
- The behavior can be written with a concrete given, a single when, and observable thens (INFERRED).

### STOP / RETURN
- The source states no stop conditions. (DERIVED: if you can't state the *when* as one behavior, or the *then* as observable changes, the behavior isn't clear yet → stay in CLARIFY or split.)

## Common failure modes
- Side-effecting then-queries (DIRECT, N01). Nothing else in the source.

## Terms worth preserving
- `Given / When / Then` — pre-condition state / behavior under specification / expected changes.
- `Scenario` — one specified example of behavior.
- `Gherkin` — Cucumber's DSL.
- `Four-Phase Test` — Setup, Exercise, Verify, Teardown (Meszaros).
- `Arrange, Act, Assert` — Wake's formulation.
- `BusinessFacingTest` — the kind of test Cucumber is often used for.

## Candidate Skill rules
- `[DERIVED from para 2]` Express each clarified behavior as at least one Given/When/Then scenario before slicing or implementing.
- `[DERIVED from example]` Include in *then* what must remain unchanged, not only what changes.
- `[DERIVED from para 2]` If a scenario needs more than one *when*, split it into separate scenarios.
- `[DERIVED from final para]` Reuse the scenario directly as the Arrange/Act/Assert structure of the first test.

## Derived developer examples

### CLARIFY-GWT-D01 — Authenticated "delete comment" action
**Classification:** DERIVED
**Grounded in:** Fowler GWT — three-part structure, unchanged-state thens (CLARIFY-GWT-02, CLARIFY-GWT-04)
**Preferred:**
- Given I am logged in as Ana, and comment #7 was written by Ana, and comment #8 was written by Ben
- When I delete comment #7
- Then comment #7 is gone, and comment #8 is still visible, and the response is 204

Second scenario: Given I am logged in as Ana, When I delete comment #8, Then the response is 403 and #8 still exists.
**Discouraged:** "Users can delete comments." Implement a delete button that calls the API, with no statement of whose comments or what happens otherwise.

### CLARIFY-GWT-D02 — Adding a DB field plus behavior
**Classification:** DERIVED
**Grounded in:** Fowler GWT — single *when* per scenario
**Preferred:** Scenario 1: Given a user with no `timezone` set, When they view the dashboard, Then times display in UTC. Scenario 2: Given `timezone = Europe/Zurich`, When they view the dashboard, Then times display in CET/CEST.
**Discouraged:** One scenario covering "user sets timezone and views dashboard and gets email digest", with three whens. Its failure can't be localized.

## Source limitations
- Structural only: it tells you how to shape a scenario, not how to find the right scenarios, how many are enough, or whether they're valuable.
- Almost no negative examples or pitfalls; don't invent any as DIRECT.
- Not about effort, estimation or slicing (though a single *when* aligns with Wake's split-condition idea; that link is DERIVED).
- Depends on Specification By Example for its rationale.

## ID register
| ID | Stage | Type | Short label | Classification | Location |
|---|---|---|---|---|---|
| CLARIFY-GWT-01 | CLARIFY | rule | GWT as style for SbE / BDD | DIRECT | para 1 |
| CLARIFY-GWT-02 | CLARIFY | rule | Given=pre-state, When=behavior, Then=changes | DIRECT | para 2 |
| CLARIFY-GWT-03 | CLARIFY | rule | "And" chains within clauses | DIRECT | after example |
| IMPLEMENT-GWT-01 | IMPLEMENT | rule | Givens = setup; thens = side-effect-free queries | DIRECT | pre-condition para |
| IMPLEMENT-GWT-02 | IMPLEMENT | rule | Usable in any test and in prose | DIRECT | after example |
| IMPLEMENT-GWT-03 | IMPLEMENT | rule | Four-Phase Test / AAA equivalence | DIRECT | final para; note 5 |
| CLARIFY-GWT-04 | CLARIFY | rule | One behavior; explicit unchanged state | INFERRED | example |
| CLARIFY-GWT-05 | CLARIFY | rule | Given as state, not steps | INFERRED | pre-condition para |
| CLARIFY-GWT-06 | CLARIFY | gate | Scenario must have all three parts | DIRECT | para 2 |
| IMPLEMENT-GWT-04 | IMPLEMENT | gate | Then side-effect free | DIRECT | pre-condition para |
| CLARIFY-GWT-Q01 | CLARIFY | question | What is the pre-state? | DIRECT | para 2 |
| CLARIFY-GWT-Q02 | CLARIFY | question | What is the one behavior? | DIRECT | para 2 |
| CLARIFY-GWT-Q03 | CLARIFY | question | What changes / what stays same? | INFERRED | para 2 + example |
| CLARIFY-GWT-Q04 | CLARIFY | question | Other outcome-changing pre-conditions? | DERIVED | — |
| CLARIFY-GWT-P01 | CLARIFY | positive | Stock sell before close | DIRECT | example |
| IMPLEMENT-GWT-N01 | IMPLEMENT | negative | Side-effecting then-queries | DIRECT | pre-condition para |
| CLARIFY-GWT-C01 | CLARIFY | pair | Concrete scenario vs vague requirement | DERIVED | — |
| CLARIFY-GWT-D01 | CLARIFY | derived | Delete own comment scenarios | DERIVED | — |
| CLARIFY-GWT-D02 | CLARIFY | derived | Timezone field, one when per scenario | DERIVED | — |
