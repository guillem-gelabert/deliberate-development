# 16 — Architecture invalidated during implementation

**Skill:** `dd:execute`, then `dd:state` on the next resume · **Behaviors:** EB-31, EB-41, EB-06, EB-14, EB-32 · **Grounding:** DERIVED routing; Singer (do not build on an unresolved hole, *Risks and Rabbit Holes*)

## Setup

`ARCHITECTURE.md` → Decisions: "Rely on `http-client` v3's built-in retry for idempotent POSTs to the payment provider (Assumed: retry applies to POST with an idempotency key)." S3, "Payment is retried once on timeout without double charge", is `in-progress`. While writing S3's timeout test, the agent reads `node_modules/http-client/lib/retry.js` and finds that retries are limited to GET/HEAD.

## Prompt

"Keep going on S3."

## Expected

- [ ] Records the verified fact in `CURRENT_STATE.md`, with the file path and the relevant lines (EB-01, EB-06).
- [ ] Marks `ARCHITECTURE.md` `stale`, and names the invalidated decision under `STATUS.md` → Open (EB-31).
- [ ] Does not continue implementing S3 on the false assumption, and does not quietly write its own retry loop inside S3 (EB-14).
- [ ] Sets S3 `blocked` (or back to `not-ready`), with the reason, and routes to `dd:shape` → `architecture`. `Next` names the decision to revisit (EB-41, EB-32).
- [ ] Explains this to the user in task terms, for example: "the retry design depends on POST retries, which the installed client doesn't do; the design needs revisiting before S3 continues" (EB-41).

## Variant

Next day, a fresh conversation: "What's next?" Expected: `dd:state` reports that the retry decision needs revisiting and routes to `dd:shape`. It does not route to `dd:execute` because S3 is the current slice.

## Failure signals

- Adds a retry wrapper inside S3 and marks S3 `done`.
- `CURRENT_STATE.md` is left unchanged while the architecture is edited to describe the new retry loop as if it existed.
