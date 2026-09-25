# Specification By Example

## Source
- Author: Martin Fowler
- URL: https://martinfowler.com/bliki/SpecificationByExample.html (2004-03-18; reposted 2011-11-17)
- Normalized file: `sources/fowler-specification-by-example.md`
- Relevant workflow stages: CLARIFY (primary); IMPLEMENT (supporting: tests as double-check)

## Core principles

### DIRECT
- **CLARIFY-SBE-01** — Specification By Example names one role of testing in XP: examples act as the specification. *(para 1)*
- **CLARIFY-SBE-02** — Examples highlight only a few points, and readers must infer the generalizations. So SbE "can't be the only requirements technique you use", though it can take a leading role. *(para 3)*
- **CLARIFY-SBE-03** — Pre/post conditions (formal methods, Design by Contract) can be as hard to write as the solution. Examples are usually much easier to come up with, especially for the non-technical people the software is written for. Budd's example: pre/post conditions struggle to show a stack's LIFO property. *(para 4)*
- **IMPLEMENT-SBE-01** — TDD tests are a double-check: things are said twice, once in code and once in tests. The value depends on the two sides using *different methods*. SbE plus production code says things quite differently, which improves error-finding. *(para 5)*
- **CLARIFY-SBE-04** — Checking whether a design satisfies an example-based spec is easy (run it), unlike formal specs. "Less valuable in theory but more valuable in practice." *(para 6)*
- **CLARIFY-SBE-05** — Tests are always incomplete. A supplier could satisfy a test-only spec with hard-coded responses, so SbE must be backed up by other mechanisms. *(para 7)*
- **CLARIFY-SBE-06** — A dangerous thing about traditional requirements specs is that people think that once they've written one, they're done communicating. *(para 7)*
- **CLARIFY-SBE-07** — SbE works only within a collaborative, not adversarial, working relationship. Examples "trigger abstractions in the design team while keeping the abstractions grounded". It needs complements: regular conversation, Domain-Driven Design, even some Design by Contract. It is "never my only tool". *(para 8)*

### INFERRED
- **CLARIFY-SBE-08** — Because SbE is incomplete by design, a set of examples should be treated as the start of an ongoing conversation, not a closed contract. *(paras 7–8)*
- **CLARIFY-SBE-09** — A concrete example is a good test of whether a requirement is understood: if nobody can produce one, the abstraction isn't grounded yet. *(para 8 — "keeping the abstractions grounded")*

## Procedure / workflow
The source presents no procedure. (No DIRECT workflow.)

## Decision rules and gates
- **CLARIFY-SBE-10** — Do not rely on examples alone; back them with conversation and other mechanisms. *(paras 7–8)* — DIRECT
- **CLARIFY-SBE-11** — Prefer examples where pre/post conditions would be as hard as the solution. *(para 4)* — INFERRED
- **CLARIFY-SBE-12** — Keep the spec and code independent in method so the double-check works. *(para 5)* — INFERRED

## Questions the future agent could ask
- **CLARIFY-SBE-Q01** — Can you give me a concrete example of the input and the expected result? `[INFERRED]` *(para 4)*
- **CLARIFY-SBE-Q02** — What generalization are these examples meant to imply, and is there an example that would contradict it? `[INFERRED]` *(para 3)*
- **CLARIFY-SBE-Q03** — Would a hard-coded response pass these examples? If yes, what other mechanism or conversation covers the general rule? `[INFERRED]` *(para 7)*
- **CLARIFY-SBE-Q04** — Who else should see these examples before we treat them as agreed? `[DERIVED]`

## Positive examples from the source

### CLARIFY-SBE-P01 — Examples easier than pre/post conditions (stack LIFO)
**Classification:** DIRECT
**Source location:** para 4 (citing Timothy Budd)
**What happens:** You can show much of a stack's behavior with pre/post conditions, but writing them to show LIFO is very tricky. Examples show it easily.
**Why it is positive:** Shows where concrete examples beat general formal specification.
**Principle illustrated:** CLARIFY-SBE-03.

### CLARIFY-SBE-P02 — Tests as spec for `Math.pow`
**Classification:** DIRECT (pointer only)
**Source location:** Some Later Comments
**What happens:** Fowler points to Jeff Langr's example of using tests as a specification for Java's `Math.pow`. The example itself is not in the source.
**Why it is positive:** Offered as a "nice example" of the technique.
**Principle illustrated:** CLARIFY-SBE-01.

## Negative examples / anti-patterns from the source

### CLARIFY-SBE-N01 — Treating a written spec as the end of communication
**Classification:** DIRECT
**Source location:** para 7
**What happens:** A requirements document is treated as the end of communication.
**Why it is negative:** Fowler calls it one of the most dangerous things about traditional specs.
**Principle violated:** CLARIFY-SBE-06, CLARIFY-SBE-07.

### CLARIFY-SBE-N02 — Satisfying the examples with hard-coded responses
**Classification:** DIRECT
**Source location:** para 7
**What happens:** A supplier returns hard-coded outputs for the specific test inputs.
**Why it is negative:** It shows tests are incomplete and need backing by other mechanisms. Fowler treats the concern as serious, while noting that if you fear this, you have bigger problems.
**Principle violated:** CLARIFY-SBE-05.

### CLARIFY-SBE-N03 — Using SbE in an adversarial relationship
**Classification:** DIRECT (condition stated, no scenario)
**Source location:** para 8
**What happens:** Examples are used between parties who are "fighting".
**Why it is negative:** SbE "only works" in collaboration.
**Principle violated:** CLARIFY-SBE-07.

## Contrastive pairs

### CLARIFY-SBE-C01 — Examples as spec vs. pre/post conditions
**Good / preferred:** Concrete examples, easy to produce and to check.
**Bad / discouraged:** Relying on pre/post conditions where they are as hard to write as the solution.
**Classification:** DIRECT
**Source location:** para 4, para 6
**Distinguishing feature:** How easily the spec can be produced by non-technical people and verified against the design. Fowler says pre/post conditions "have their place".

### CLARIFY-SBE-C02 — Spec as ongoing conversation vs. spec as closed deliverable
**Good / preferred:** Examples plus regular conversation and other techniques.
**Bad / discouraged:** Writing the spec and considering communication finished.
**Classification:** DIRECT
**Source location:** paras 7–8
**Distinguishing feature:** Whether writing the spec ends or continues the dialogue.

## Stop / go criteria

### GO
- Concrete examples exist that the people the software is for can understand and agree on (INFERRED, para 4, para 8).

### STOP / RETURN
- Examples alone are being treated as the complete requirement → add conversation or other mechanisms (DIRECT, paras 7–8).
- No working collaborative relationship → SbE is not expected to work (DIRECT, para 8).

## Common failure modes
- Treating the written spec as the end of communication (N01).
- Treating examples as complete (N02).
- Using SbE as the only technique (para 3, para 8).

## Terms worth preserving
- `Specification By Example` — using concrete examples, typically as tests, as the specification.
- `double-check` — saying things twice (code and tests) using different methods.
- `Design by Contract` / `pre and post conditions` — the formal-spec alternative, with its place but often hard to write.

## Candidate Skill rules
- `[DERIVED from para 4]` When a requirement is abstract, ask for or propose 2–3 concrete input→outcome examples before implementing.
- `[DERIVED from para 7]` Treat examples as incomplete. State the general rule they imply, and confirm it in conversation.
- `[DERIVED from para 7]` Do not treat an agreed set of examples as the end of clarification; if implementation reveals new cases, return to CLARIFY.
- `[DERIVED from para 5]` Write expected outcomes independently of the implementation.

## Derived developer examples

### CLARIFY-SBE-D01 — Discount rule on a checkout API
**Classification:** DERIVED
**Grounded in:** Fowler SbE — examples ground abstractions (CLARIFY-SBE-07), incompleteness (CLARIFY-SBE-05)
**Preferred:** "10% off orders over €100" becomes examples: €99.99 → no discount; €100.00 → ? (ask); €150 → €135; €150 with a coupon → ? (ask). The boundary and coupon questions go back to the product owner.
**Discouraged:** Implement `if total > 100` from the sentence alone and consider the requirement settled; the €100.00 and coupon cases surface in production.

### CLARIFY-SBE-D02 — Browser-specific bug
**Classification:** DERIVED
**Grounded in:** Fowler SbE — concrete examples as spec
**Preferred:** "Date picker broken in Safari" becomes: in Safari 17, choosing 2026-03-29 (DST change) shows 2026-03-28; expected 2026-03-29. Chrome behaves correctly.
**Discouraged:** Starting to rewrite the date picker from the vague report.

## Source limitations
- Says nothing about effort, estimation, slicing or scheduling. Concrete examples don't tell you how long implementation takes.
- No procedure for eliciting examples, and no format (see GWT for structure).
- Old (2004) and short; the discussion is mostly conceptual (vs. Design by Contract).
- Assumes a customer/developer collaboration. For a solo developer, "the other side" may be a ticket author or stakeholder, which requires adaptation.

## ID register
| ID | Stage | Type | Short label | Classification | Location |
|---|---|---|---|---|---|
| CLARIFY-SBE-01 | CLARIFY | rule | Examples as specification | DIRECT | para 1 |
| CLARIFY-SBE-02 | CLARIFY | rule | Examples partial; not the only technique | DIRECT | para 3 |
| CLARIFY-SBE-03 | CLARIFY | rule | Examples easier than pre/post conditions | DIRECT | para 4 |
| IMPLEMENT-SBE-01 | IMPLEMENT | rule | Double-check via different methods | DIRECT | para 5 |
| CLARIFY-SBE-04 | CLARIFY | rule | Easy to verify design vs examples | DIRECT | para 6 |
| CLARIFY-SBE-05 | CLARIFY | rule | Tests incomplete; hard-coding objection | DIRECT | para 7 |
| CLARIFY-SBE-06 | CLARIFY | rule | Written spec ≠ done communicating | DIRECT | para 7 |
| CLARIFY-SBE-07 | CLARIFY | rule | Needs collaboration; ground abstractions; never only tool | DIRECT | para 8 |
| CLARIFY-SBE-08 | CLARIFY | rule | Examples start a conversation | INFERRED | paras 7–8 |
| CLARIFY-SBE-09 | CLARIFY | rule | No example = ungrounded abstraction | INFERRED | para 8 |
| CLARIFY-SBE-10 | CLARIFY | gate | Back examples with other mechanisms | DIRECT | paras 7–8 |
| CLARIFY-SBE-11 | CLARIFY | gate | Prefer examples where pre/post is hard | INFERRED | para 4 |
| CLARIFY-SBE-12 | CLARIFY | gate | Keep spec and code methodologically independent | INFERRED | para 5 |
| CLARIFY-SBE-Q01 | CLARIFY | question | Concrete input and expected result? | INFERRED | para 4 |
| CLARIFY-SBE-Q02 | CLARIFY | question | Which generalization; counter-example? | INFERRED | para 3 |
| CLARIFY-SBE-Q03 | CLARIFY | question | Would hard-coding pass? | INFERRED | para 7 |
| CLARIFY-SBE-Q04 | CLARIFY | question | Who else should see the examples? | DERIVED | — |
| CLARIFY-SBE-P01 | CLARIFY | positive | Stack LIFO via examples | DIRECT | para 4 |
| CLARIFY-SBE-P02 | CLARIFY | positive | Math.pow tests-as-spec (pointer) | DIRECT | Later Comments |
| CLARIFY-SBE-N01 | CLARIFY | negative | Done communicating after writing spec | DIRECT | para 7 |
| CLARIFY-SBE-N02 | CLARIFY | negative | Hard-coded responses satisfy tests | DIRECT | para 7 |
| CLARIFY-SBE-N03 | CLARIFY | negative | Adversarial relationship | DIRECT | para 8 |
| CLARIFY-SBE-C01 | CLARIFY | pair | Examples vs pre/post conditions | DIRECT | paras 4, 6 |
| CLARIFY-SBE-C02 | CLARIFY | pair | Ongoing conversation vs closed spec | DIRECT | paras 7–8 |
| CLARIFY-SBE-D01 | CLARIFY | derived | Checkout discount boundaries | DERIVED | — |
| CLARIFY-SBE-D02 | CLARIFY | derived | Safari date bug as example | DERIVED | — |
