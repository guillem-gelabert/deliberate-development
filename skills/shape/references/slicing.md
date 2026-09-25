# Behavioral slicing

Read when writing or revising slices in `PLAN.md`. Tags: **[DIRECT: author]**, **[INFERRED: author]**, **[DERIVED]**.

## What a slice is

A slice is a unit of observable behavior that can be verified on its own and runs end to end through the system. It is not a TDD step, an estimation task, or a layer.

- Get a minimal end-to-end version in place first, then fill in the rest. [DIRECT: Wake, *Twenty Ways to Split Stories*]
- Cut vertically through the layers. A finished layer with nothing on top of it has little value. [DIRECT: Wake, *INVEST*; Singer, *Get One Piece Done*]
- Do not build depth-first by component hierarchy. Build a thin version of the whole, then improve it. [DIRECT: Wake, *Independent Stories*]
- INVEST works as a diagnostic, not a ritual: independent, negotiable, valuable, estimable, small, testable. [DIRECT: Wake]

## Choosing the first slice

- Pick one that is **core** (central to the problem), **small** (finishable end to end in a short time), and **novel** (teaches you something). Between equals, prefer the one you have never done before. [DIRECT: Singer, *Get One Piece Done*]
- Start in the middle. Stub login, setup and other peripherals to reach the interesting problem. [DIRECT: Singer; Wake]
- Value-first and risk-first can disagree. Wake orders by value and risk; Singer leans toward the novel or scariest part. State which one governs this task and why. [DIRECT, both]

## Split patterns [DIRECT: Wake, *Twenty Ways*]

Split along: connector words in the title ("and", "or", "then"); main flow vs alternate flows; zero / one / many; base case vs general case; simple vs complex input; manual step first vs automated; fewer vs more "-ilities" (performance, scale). Do the easier side first. The harder side is deferred, not wrong. [INFERRED: Wake]

Check that the slices reassemble into the full behavior, that no two slices overlap, and that slices too small to matter are merged. [DIRECT: Wake]

## Scope boundaries

- Declare out-of-bounds cases, and cut nice-to-haves. Mark optional items with `~` in their title. [DIRECT: Singer, *Risks and Rabbit Holes* / *Decide When to Stop*]
- Record excluded behavior in `SPEC.md` → Scope/Out, so no later slice quietly reintroduces it. [DERIVED]

## Stubbing vs faking

Stubbing a prerequisite so a slice can reach its target behavior is endorsed. [DIRECT: Wake, *Independent Stories*; Singer] Faking the behavior the slice exists to deliver does not count as delivering it. [DIRECT: Beck, *Canon TDD*; Fowler, *Specification by Example*] Record any planned stub in the slice's `Dependencies` or `Implementation notes`, with the slice that will replace it. [DERIVED]

## Contrastive examples [DERIVED]

**Layers vs behavior**
- Preferred: `S1 — A user can save a phone number (one national format) and see it after reload`, then `S2 — international formats`, then `S3 — admin search by phone`.
- Discouraged: `S1 — Migration and model for phone`, `S2 — Phone API`, `S3 — Phone UI`, `S4 — Tests`. Nothing is usable or verifiable until S3, and tests trail the behavior.

**Start in the middle**
- Preferred: `S1 — Owner deletes their own comment; a non-owner gets 403`, using the existing session guard.
- Discouraged: starting with a new roles/permissions system "because delete needs auth".

**Main flow first**
- Preferred: render one item in the new `OrderSummary`, then the empty state, then pagination.
- Discouraged: building empty, loading, error and pagination states before a single item renders.

**Future slices stay behavioral**
- Preferred: S3–S5 each have one Given/When/Then line and `Done when` boxes. Only S1 has implementation notes.
- Discouraged: a 40-item task checklist spanning all slices before S1 starts.

## Slice readiness/risk check

A slice is `ready` only when all of these hold. [DERIVED checklist; items grounded as tagged]

- **Observable:** the behavior is written as Given/When/Then, and every `Done when` item can be verified by running something. [DIRECT: Wake, Testable; Fowler, GWT]
- **End to end:** it delivers usable behavior through every layer it touches, not one layer. [DIRECT: Wake; Singer]
- **Independent:** it does not overlap another slice, and its dependencies are either available now or stubbable without faking its own behavior. [DIRECT: Wake, *Independent Stories*]
- **Downhill:** you can name the concrete tasks it needs. Nothing inside it is still "we'll figure out how". [INFERRED: Singer, *Show Progress*; Spolsky]
- **Small:** no connector word is left in the title, and it fits in a few days of focused work. [DERIVED size bound]
- **Architecture-consistent:** it uses the components and interfaces `ARCHITECTURE.md` decided. If it needs a component the design does not have, that is a design-level finding, not a slice note. [DERIVED]

Any failure gives `not-ready`, with the failing item written in the slice. Route slice-local failures to a re-slice or a spike slice. Route design-level failures back to architecture.

Contrast [DERIVED]:
- Preferred: `S2 — not-ready: Downhill fails; unknown whether the PDF helper embeds custom fonts. Added S2a spike (1h): render one invoice with the brand font; decides whether S2 needs a font-embedding step.`
- Discouraged: `S2 — ready` with "figure out fonts" buried in its implementation notes.

## Return conditions

- A slice cannot be written as a Given/When/Then example → `SPEC.md` is not clear enough. Return to `dd:ground`. [INFERRED: Wake, Fowler]
- You do not know how to split a slice, or whether it is feasible → spike it (see `architecture-and-risk.md`). [DIRECT: Wake]
- A slice still has a connector word, or would take more than a few days of focused work → split again. The size bound is DERIVED: Singer's first piece is "a few days", and Wake's stories run up to a few person-weeks.
