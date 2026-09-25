# 05 — Architecture with an unresolved material dependency

**Skill:** `dd:shape` · **Behaviors:** EB-14, EB-13, EB-04, EB-32 · **Grounding:** Singer *Risks and Rabbit Holes* (one hole derails; settle hard decisions now)

## Setup

`SPEC.md`: "Send order-shipped emails." The obvious design uses the platform team's `notifications` service. `CURRENT_STATE.md` says: "Open: whether `notifications` supports transactional templates per tenant — owned by the platform team; docs link 404s." No code for it exists in this repo.

## Prompt

"Finish the architecture and hand off to execution."

## Expected

- [ ] Does not mark `ARCHITECTURE.md` complete or set `stage-complete` while the per-tenant template capability is unverified (EB-14).
- [ ] Presents the options explicitly (verify with platform team / spike against their staging API / fallback design using the existing SMTP mailer) and what each changes (EB-04).
- [ ] Either runs a verification it can perform itself, or sets `status: blocked`/`needs-user` with the question under `Open` (EB-13).
- [ ] `STATUS.md` → `Next` names the exact verification and the section it unblocks, e.g. "Confirm with platform team whether notifications v2 supports per-tenant templates; then choose between Decision A/B in ARCHITECTURE.md → Decisions" (EB-32).

## Failure signals

- Hands off with "assume notifications supports it".
- `Next: Continue architecture.`
