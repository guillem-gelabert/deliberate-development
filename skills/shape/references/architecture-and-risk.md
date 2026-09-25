# Architecture and de-risking

Read during the architecture risk check, and whenever an unknown needs a response. Tags: **[DIRECT: author]**, **[INFERRED: author]**, **[DERIVED]**.

## Solved enough, bounded enough

- Shaped work is rough (it leaves implementation latitude), solved (no major open design question), and bounded (what is out is stated). [DIRECT: Singer, *Principles of Shaping*]
- One unaddressed hole can derail the whole effort. Find the pitfalls you can find up front and remove them before committing. The aim is thin-tailed work, where plausible duration does not stretch to a multiple of the plan. [DIRECT: Singer, *Risks and Rabbit Holes*]

## Viability questions [DIRECT: Singer]

Ask of the design:

1. Does it need technical work we have never done before?
2. Are we assuming how the parts fit together?
3. Are we assuming a design solution exists that we could not produce ourselves?
4. Is there a hard decision to settle now so it does not trip up the work later?

Then walk the use case through in slow motion, from where the user starts to where they end up, and note what is missing.

"Possible?" is the wrong question, because everything is possible in software. Ask "possible within the time we are willing to spend?" [DIRECT: Singer]

## Responses to a risk

- **Patch:** decide a simpler solution for the tricky spot now. [DIRECT: Singer]
- **Fence off:** declare the case out of bounds, and record it in `ARCHITECTURE.md` → Out of scope and `SPEC.md` → Scope/Out. [DIRECT: Singer]
- **Cut:** drop the unnecessary part. [DIRECT: Singer]
- **Spike:** run a focused, hands-on experiment to buy learning. Wake: "an hour, or a day, rarely longer". [DIRECT: Wake, *Twenty Ways to Split Stories*] A spike buys learning, not implementation. [INFERRED: Wake]

## Head vs hands

A theory ("we'll just use that API") is only the first third of the hill. Next comes "approach validated with running code", then "built far enough that no unknowns remain". Push the scariest unknowns uphill first and leave routine work for later. [DIRECT: Singer, *Show Progress*]

An integration counts as understood only after you have seen its real contract: the installed version's source or types, or a probe call. Reading marketing docs, or remembering the API, does not count. [DERIVED]

## Spike format [DERIVED]

Record in `ARCHITECTURE.md` → Spikes (and as a slice in `PLAN.md` if it needs its own block):

```markdown
- **Spike: refresh-token support in provider X** (timebox 1h)
  Question: does X's SDK v4 support refresh tokens for the client-credentials flow?
  Method: call the sandbox with a test app; read the SDK source for `refresh`.
  Decision it unlocks: whether S2 can use X directly or needs our own token cache.
  Result: <yes/no + evidence + consequence>, or "timebox hit: <what is still unknown>".
```

A spike that needs its own block becomes a slice in the contract format, titled `S<n> — Spike: <question>`. Its `Done when` boxes must be satisfiable either way the answer falls: the question answered (or the timebox hit), and the result recorded in `ARCHITECTURE.md` → Spikes. The timebox goes on the slice's `**Block:**` line; a spike slice never gets an `**Estimate:**`, because its number is a timebox, not a prediction.

The spike's code is thrown away unless the architecture explicitly adopts it. When the timebox is hit, stop and re-plan. Do not extend silently.

## Contrast [DERIVED]

- Preferred: before slicing checkout shipping rates, run a 2h spike against the carrier sandbox for one domestic address to confirm the auth flow and response shape. Only then slice "show rates at checkout" and estimate it.
- Discouraged: `S2 — Integrate carrier rates (1 day)` based on the carrier's landing page. On day 3 it turns out rates need an account-level token and a contract.
- The difference: the preferred version resolves the uncertainty with running code before anything is committed.

## Where de-risking belongs [DERIVED; sources differ]

Shape Up de-risks during shaping, before the bet, and also sequences uphill work first during the build. Wake places spikes inside the story flow. This skillset de-risks twice, in a loop. The **architecture risk check** handles unknowns that could change the design, feasibility, data or permissions. The **slice readiness/risk check** (see `slicing.md`) handles unknowns confined to one slice. When a slice-level check exposes a design-level problem, the loop returns to architecture. `dd:execute` does not estimate a slice that failed its readiness check.
