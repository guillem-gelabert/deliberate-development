# De-risk

## Purpose
Find the unknowns in the chosen slice before committing to it: technical unknowns, unsolved design problems and misunderstood interdependencies. Then patch them, fence them off, cut them, or turn them into a spike. The goal is thin-tailed work, meaning work whose plausible duration does not stretch to multiples of the plan.

## Primary grounding sources
- Singer, *Risks and Rabbit Holes*: primary.
- Singer, *Show Progress*: primary for uphill/downhill, "build your way uphill" and sequencing risky work first.
- Wake, *Twenty Ways to Split* / *INVEST*: primary for spike vs implementation and research vs action.
- Singer, *Principles of Shaping*: supporting. Solved; unshaped work can't be scheduled.
- Wake, *Independent Stories*: supporting. Order by value and risk.

## Entry conditions
- A candidate slice exists (Slice exit).

## Agent questions
1. Does this require new technical work you've never done before? (DIRECT, DERISK-RISK-Q01)
2. Are you making assumptions about how the parts fit together? (DIRECT, DERISK-RISK-Q02)
3. Are you assuming a design solution exists that you couldn't come up with yourself? (DIRECT, DERISK-RISK-Q03)
4. Is there a hard decision you should settle now so it doesn't trip you up mid-work? (DIRECT, DERISK-RISK-Q04)
5. Walk the use case through in slow motion. Where exactly does the user go from start to end, and what is missing? (DIRECT, DERISK-RISK-Q06)
6. Is it possible *within the time you're willing to spend*, not just possible? (DIRECT, DERISK-RISK-Q07 / C01)
7. Have you validated the approach with your hands (code that runs), or only in your head? (INFERRED, DERISK-HILL-Q04)
8. If you ran out of time, which part could you whip together anyway, and which might prove harder than you think? (DIRECT, DERISK-HILL-Q02)

## Rules
- **One hole can derail the whole thing.** Look for the pitfalls you *can* find up front and eliminate them before committing. (DIRECT, DERISK-RISK-01/-03)
- **Aim for thin-tailed work.** Rabbit holes make the right tail stretch to multiples of the plan. (DIRECT, DERISK-RISK-04/-05)
- **Patch, fence off, or cut.** Dictate a simpler solution for a tricky spot (patch), declare cases out of bounds, and cut unnecessary parts. (DIRECT, DERISK-RISK-10; SLICE-RISK-11/-12)
- **If a slice is too hard to estimate or implement, split off research or a spike.** A spike is a focused, hands-on experiment that lasts an hour or a day, rarely longer. (DIRECT, DERISK-SPLIT-01/-02/-04; DERISK-INVEST-01/-02)
- **A spike buys learning. It is not implementation.** Keep the two separate. (INFERRED, DERISK-SPLIT-03)
- **Build your way uphill.** A theory in your head ("I'll just use that API") is only the first third of the hill. After that comes "I've validated my approach", then "far enough built that I don't believe there are other unknowns". (DIRECT, DERISK-HILL-05/-10)
- **Push the scariest work uphill first.** Leave routine work for later. (DIRECT, DERISK-HILL-06; DERISK-INDEP-01)
- **Ask "possible in <time box>?", not "possible?"** In software everything is possible, but nothing is free. (DIRECT, DERISK-RISK-13, DERISK-RISK-N03)

## Positive patterns
- Completed to-dos in To-Do Groups: a hole was found during shaping and patched with a simple dictated rule (append the group name). A deep design problem was not pushed down to the builders. (DIRECT, DERISK-RISK-P01)
- Geocoding (never done before) was pushed uphill before the email template (routine). (DIRECT, DERISK-HILL-P03)
- A time-boxed spike separated from the rest of the story to get enough information to estimate. (DIRECT, DERISK-INVEST-P02)

## Anti-patterns
- The client-projects home-screen redesign: the team assumed the designer would figure it out, no viable approach was validated, and the project was abandoned after six weeks. (DIRECT, DERISK-RISK-N01)
- Handing someone a "tangled knot of interdependencies" to untangle under a deadline. (DIRECT, DERISK-RISK-N02)
- Doing uphill work in your head and then sliding back when reality turns out more complicated. (DIRECT, DERISK-HILL-N03)
- Asking "is this possible?" instead of asking about the time box. (DIRECT, DERISK-RISK-N03)

## Contrastive examples

**DERISK-SYN-D01: Unfamiliar third-party API (shipping rates)** (DERIVED; grounded in DERISK-SPLIT-02, DERISK-HILL-05)
- *Preferred:* A 2-hour spike: call the sandbox for one domestic address, confirm the auth flow and the response shape, then throw the code away. Only after that, slice and estimate "show rates at checkout".
- *Discouraged:* Estimate "integrate shipping rates: 1 day" from reading the marketing docs, then learn on day 3 that rates need a separate account-level token and carrier contracts.
- *Distinguishing feature:* the uncertainty was resolved with running code before any commitment was made.

**DERISK-SYN-D02: Browser-specific bug** (DERIVED; grounded in DERISK-RISK-04, DERISK-RISK-Q01)
- *Preferred:* Recognize that "fix Safari date-picker bug" is fat-tailed until it is reproduced and its cause isolated. Commit only to "reproduce and isolate (≤1h)" first.
- *Discouraged:* Commit to "fix today" with no reproduction.

**DERISK-SYN-D03: Refactoring existing code safely** (DERIVED; grounded in DERISK-RISK-Q02 interdependencies, SLICE-RISK-11 out of bounds)
- *Preferred:* Before extracting a shared `formatDate` helper, grep its call sites, note the two that rely on local-time quirks, and declare those out of bounds for this slice.
- *Discouraged:* Start the extraction and discover the timezone interdependency halfway through, with half the call sites changed.

## Stop / return conditions
- A viability question gets the answer "yes, but we don't know how" → patch it, cut it, spike it, or return to Clarify/Slice. (INFERRED, DERISK-RISK-18/-20)
- Talking it through with someone who knows the code finds problems → reshape. (DIRECT, DERISK-RISK-15/-20)
- A spike runs past its time box → stop and re-plan. (INFERRED from the spike duration, DERISK-SPLIT-02, and the time-box rule, COMMIT-INVEST-02/-04)

## Exit criteria
- Every identified rabbit hole is patched, declared out of bounds, cut, or assigned to a separate time-boxed spike.
- The remaining work is judged downhill-ish: known steps, familiar parts, and interfaces that fit in known ways. (INFERRED, DERISK-SHAPING-13, COMMIT-RISK-21)

## Unresolved tensions between sources
- **Where de-risking happens.** Shape Up de-risks during *shaping*, before the bet. Uphill work at the end of a cycle signals a shaping failure (COMMIT-STOP-09). Shape Up also expects in-cycle uphill work and sequences it first (DERISK-HILL-06). Wake puts spikes inside the story flow. For an individual developer these collapse into "spike before commit", which is an adaptation.
- **Spike length.** Wake: an hour or a day, rarely longer. INVEST: "time-boxed", unspecified. Shape Up gives no spike length. The Skill should take Wake's figure only as Wake's.
- Shape Up's thin/fat-tail distributions describe *project* risk qualitatively. EBS produces *quantitative* distributions from velocity history. These are related ideas, not the same instrument.

## Provenance map
| Rule / example | Source | Classification | Source section |
|---|---|---|---|
| One hole derails; remove findable pitfalls | Singer, Risks and Rabbit Holes | DIRECT | Intro |
| Three rabbit-hole categories; thin vs fat tail | Singer, Risks and Rabbit Holes | DIRECT | Different categories of risk |
| Four viability questions; slow-motion walk-through | Singer, Risks and Rabbit Holes | DIRECT | Look for rabbit holes |
| Patch a hole | Singer, Risks and Rabbit Holes | DIRECT | Case study: Patching a hole |
| Possible within appetite | Singer, Risks and Rabbit Holes | DIRECT | Present to technical experts |
| Spike (hour/day) / research vs action | Wake, Twenty Ways | DIRECT | The Big Picture |
| Spike to enable estimate | Wake, INVEST | DIRECT | Estimable |
| Head vs hands; thirds of the hill | Singer, Show Progress | DIRECT | Build your way uphill |
| Scariest first | Singer, Show Progress | DIRECT | Solve in the right sequence |
| Spike ≠ implementation | Wake, Twenty Ways | INFERRED | The Big Picture |
| DERISK-SYN-D01–D03 | — | DERIVED | — |
