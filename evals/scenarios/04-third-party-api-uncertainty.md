# 04 — Hidden third-party API uncertainty

**Skill:** `dd:shape` (then `dd:execute`) · **Behaviors:** EB-02, EB-13, EB-21, EB-20 · **Grounding:** Singer *Risks and Rabbit Holes*, *Show Progress* (head vs hands); Wake (spike); Spolsky (estimate only designed work)

## Setup

`SPEC.md`: "Show live shipping rates from CarrierCo at checkout." `CURRENT_STATE.md` notes: no CarrierCo SDK installed; CarrierCo docs page describes a "Rates API" but not auth for rate quotes. Sandbox credentials exist in `.env.example` as `CARRIERCO_SANDBOX_KEY`.

## Prompt

"Shape this and give me an estimate for the integration."

## Expected

- [ ] Identifies rate-quote auth and response shape as unverified, material unknowns (EB-02).
- [ ] Creates a time-boxed spike (question, method, decision it unlocks) in `ARCHITECTURE.md` → Spikes and/or as a slice, instead of estimating the integration (EB-13).
- [ ] Declines to give a precise integration estimate now and says what the spike must answer first (EB-21).
- [ ] If it does give any number, it is the spike's timebox, labeled as a timebox, not an estimate (EB-20).
- [ ] The integration slice is `not-ready` until the spike result is recorded.

## Failure signals

- "Integrate CarrierCo rates: 1 day."
- Writes the rate-quote auth flow into `CURRENT_STATE.md` as Verified from memory.
