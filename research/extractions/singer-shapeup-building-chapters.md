# Shape Up — Building chapters (ch. 10, 11, 13, 14)

Combined extraction of four optional Shape Up chapters. Only material that materially clarifies a workflow stage and is not already captured from ch. 2, 3, 5 is included.

## Source
- Author: Ryan Singer
- URLs:
  - Hand Over Responsibility (ch. 10) — https://basecamp.com/shapeup/3.1-chapter-10 — key HANDOVER — `sources/singer-hand-over-responsibility.md`
  - Get One Piece Done (ch. 11) — https://basecamp.com/shapeup/3.2-chapter-11 — key ONEPIECE — `sources/singer-get-one-piece-done.md`
  - Show Progress (ch. 13) — https://basecamp.com/shapeup/3.4-chapter-13 — key HILL — `sources/singer-show-progress.md`
  - Decide When to Stop (ch. 14) — https://basecamp.com/shapeup/3.5-chapter-14 — key STOP — `sources/singer-decide-when-to-stop.md`
- Relevant workflow stages: ORIENT (getting oriented), SLICE (one integrated slice; core/small/novel), DERISK (hill; build uphill with hands; sequence scariest first), ESTIMATE (estimates don't show uncertainty), IMPLEMENT (program just enough; affordances first), COMMIT/CLOSE (baseline, scope hammering, must/nice-to-have, when to extend; discovered tasks)

## Core principles

### DIRECT
- **ORIENT-HANDOVER-01** The first days don't look like "work": builders are figuring out how the existing system works and which starting point is best—"learning the lay of the land." (Hand Over Responsibility / Getting oriented)
- **ORIENT-HANDOVER-02** Teams can't dive into a code base and build immediately; they must acquaint themselves with relevant code, think through the pitch, and go down short dead ends to find a starting point. This exploration happens anyway; demanding visible progress pushes it underground. It's legitimate to say "I'm still figuring out how to start." (Getting oriented)
- **ORIENT-HANDOVER-03** If the silence doesn't break after about three days, that's a reasonable time to step in. (Getting oriented)
- **CLOSE-HANDOVER-04** Distinguish *imagined* tasks (assumed at the start) from *discovered* tasks (found by doing real work); discovered tasks make up the true bulk and often the hardest parts. (Imagined vs discovered tasks)
- **ORIENT-HANDOVER-05** "The way to really figure out what needs to be done is to start doing real work"—but pick something meaningful first: central yet small enough to be done end-to-end, with working UI and code, in a few days. (Imagined vs discovered tasks)
- **SLICE-HANDOVER-06** Splitting a project into tasks up front "is like putting the pitch through a paper shredder"; planning up front makes you blind to reality along the way. (Assign projects, not tasks)
- **CLOSE-HANDOVER-07** Done means deployed, within the cycle, including testing/QA; otherwise appetite and budget mean nothing. (Done means deployed)
- **SLICE-ONEPIECE-01** Don't build a master plan of parts that come together at the 11th hour; many completed tasks with nothing to click on means nothing is *really* done. (Get One Piece Done / Intro)
- **SLICE-ONEPIECE-02** Integrate vertically on one small piece rather than chipping at horizontal layers; front-end without back-end (or vice versa) stays hypothetical. (Integrate one slice)
- **IMPLEMENT-ONEPIECE-03** Affordances before pixel-perfect screens: first make it work, then make it beautiful. The biggest early uncertainties are whether it works, makes sense, and how hard it is to implement. (Affordances before pixel-perfect screens)
- **IMPLEMENT-ONEPIECE-04** Program just enough for the next step; early back-end can be "strategically patchy" (controller without model, mock data, hard-coded HTTPAuth password). (Program just enough for the next step)
- **SLICE-ONEPIECE-05** Start in the middle: jump to the interesting problem and stub everything else (don't build login first). (Start in the middle)
- **SLICE-ONEPIECE-06** Choose the first piece by three criteria: **core** (without it the rest means nothing), **small** (finish something meaningful in a few days), **novel** (among core+small, prefer what you've never done—it eliminates uncertainty). (Start in the middle)
- **ESTIMATE-HILL-01** To-do lists grow as the team makes progress; an empty list may mean done or tasks not yet discovered. (Show Progress / The tasks that aren't there)
- **ESTIMATE-HILL-02** Estimates don't show uncertainty: two 4-hour tasks mean different things if one was done ten times before and the other is novel or has unclear interdependencies (might take 2–3 days). (Estimates don't show uncertainty)
- **DERISK-HILL-03** Work is like a hill: uphill = figuring out the approach (uncertainty, problem solving); downhill = execution (certainty, can see all the work). (Work is like a hill)
- **ESTIMATE-HILL-04** At the top of the hill it becomes fair to estimate the remaining work; before that, "percent complete" and prep-time estimates don't make sense (dinner party example). (Work is like a hill)
- **DERISK-HILL-05** Build your way uphill with hands, not head: first third "I've thought about this", second "I've validated my approach", final third "I'm far enough with what I've built that I don't believe there are other unknowns." Backsliding happens when uphill work was done in the head ("I'll just use that API"). (Build your way uphill)
- **DERISK-HILL-06** Solve in the right sequence: push the scariest/most unknown work uphill first; leave routine work for last (inverted pyramid). Ask: if out of time, which could we whip together and which might be harder than we think? (Solve in the right sequence)
- **DERISK-HILL-07** A stuck dot is a raised hand; nobody likes to say "I don't know," which hides uncertainty and accumulates risk. (Nobody says “I don't know”)
- **SLICE-HILL-08** A scope stuck on the hill may be mis-drawn (e.g. "Notify" = email design + delivery + in-app display); break it into smaller scopes that can move independently. (Prompts to refactor the scopes)
- **CLOSE-STOP-01** Compare down to `baseline` (current customer reality), not up to an ideal: "better than what they have now." (Decide When to Stop / Compare to baseline)
- **COMMIT-STOP-02** Limits motivate trade-offs: when someone says "wouldn't it be better if…" or finds an edge case, first ask "Is there time for this?"; question new work before accepting it as necessary. (Limits motivate trade-offs)
- **CLOSE-STOP-03** Scope grows like grass—naturally, not through anyone's fault; give people the authority and responsibility to keep cutting it. (Scope grows like grass)
- **CLOSE-STOP-04** Cutting scope isn't lowering quality; choose which things matter for core use cases. (Cutting scope isn't lowering quality)
- **CLOSE-STOP-05** Scope hammering questions (below) applied to every new fix/add/improve. (Scope hammering)
- **CLOSE-STOP-06** Must-haves are tasks on the scope; nice-to-haves are marked with `~`, done only if time remains, usually never built; "The act of marking them as a nice-to-have is the scope hammering." (Scope hammering)
- **CLOSE-STOP-07** QA-discovered tasks are nice-to-haves by default; the team triages and elevates some to must-haves. Programmers write their own tests; QA is a level-up, not a gate. (QA is for the edges)
- **COMMIT-STOP-08** Extend only if (1) outstanding tasks are true must-haves that survived hammering and (2) all remaining work is downhill. Uphill work at the end signals a shaping hole → put it back into shaping. Even then, prefer enforcing the appetite. (When to extend a project)

### INFERRED
- **ORIENT-HANDOVER-08** Orientation is real work with a time bound; its output is a chosen starting point, not a deliverable. (Getting oriented)
- **ESTIMATE-HILL-09** An estimate is trustworthy only for downhill work; for uphill work the first job is to reduce unknowns, not to refine the number. (Estimates don't show uncertainty; Work is like a hill)
- **CLOSE-HANDOVER-10** Discovered tasks are expected output of working, and should be captured, not treated as plan failure. (Imagined vs discovered tasks; The tasks that aren't there)

## Procedure / workflow
Not presented as a single procedure. INFERRED sequence across chapters:
1. Get oriented in the existing code (time-bounded; say so if still figuring out).
2. Pick a first piece: core, small, novel; start in the middle; stub the rest.
3. Integrate one vertical slice end-to-end; affordances first, program just enough.
4. Push the scariest unknowns uphill first, with hands not head.
5. Capture discovered tasks; hammer scope (must-have vs `~` nice-to-have).
6. Near the end: compare to baseline; extend only if must-haves and all downhill; otherwise return to shaping.

## Decision rules and gates
- **SLICE-ONEPIECE-07** If two candidate first pieces are both core and small, prefer the novel one. [DIRECT, Start in the middle]
- **DERISK-HILL-10** Don't mark something "solved/over the hill" until you've built enough that you believe no other unknowns remain. [DIRECT, Build your way uphill]
- **SLICE-HILL-11** If a scope seems stuck but parts are moving, split it into independent scopes. [DIRECT, Prompts to refactor the scopes]
- **COMMIT-STOP-09** If work is uphill at the deadline, do not extend; return it to shaping. [DIRECT, When to extend a project]
- **ORIENT-HANDOVER-11** If orientation shows no sign of breaking after ~3 days, check in. [DIRECT, Getting oriented — at team scale]

## Questions the future agent could ask
- **SLICE-ONEPIECE-Q01** [INFERRED] What's the core piece without which nothing else means anything? Is it small enough to finish in a few days? Is it the novel one? (Start in the middle)
- **DERISK-HILL-Q02** [DIRECT] If we were out of time, which of these could we easily whip together and which might prove harder than we think? (Solve in the right sequence)
- **DERISK-HILL-Q03** [DIRECT] What's the unknown that's holding it back? / What can we solve to get that over the hill? (Status without asking; Nobody says “I don't know”)
- **DERISK-HILL-Q04** [INFERRED] Have I validated this approach with something built, or only thought about it? (Build your way uphill)
- **CLOSE-STOP-Q05** [DIRECT] How do customers solve this today? What workaround does this eliminate? (Compare to baseline)
- **CLOSE-STOP-Q06** [DIRECT] Is there time for this? (Limits motivate trade-offs)
- **CLOSE-STOP-Q07** [DIRECT] Scope hammering: Is this a must-have? Could we ship without this? What happens if we don't do this? Is this new or pre-existing? How likely is it? Which customers see it—core or edge? What's the actual impact? How aligned is that use case with the intended audience? (Scope hammering)
- **ORIENT-HANDOVER-Q08** [INFERRED] How does the existing system work here, and which starting point is best? (Getting oriented)

## Positive examples from the source

### SLICE-ONEPIECE-P01 — Clients in projects: visibility toggle first
**Classification:** DIRECT
**Source location:** Get One Piece Done / Case study: Clients in projects
**What happens:** Three parts: client access (major back-end/caching implications), client management, visibility toggle. After orienting, the designer chose the toggle (most central UI) to integrate first; programmer spiked the access model meanwhile, then wired the toggle to appear, change state and persist—without yet changing visibility. Demoed in ~3 days, tweaked, called "done."
**Why it is positive:** Tangible, integrated, validated piece early; built confidence.
**Principle illustrated:** Integrate one slice; core/small/novel.

### IMPLEMENT-ONEPIECE-P02 — Hard-coded HTTPAuth
**Classification:** DIRECT
**Source location:** Program just enough for the next step
**What happens:** Interview app needed protection for sensitive data; they used plain HTTPAuth with a hard-coded password instead of building auth.
**Why it is positive:** Enabled real data early without work that taught them nothing about the problem.
**Principle illustrated:** Program just enough; start in the middle.

### DERISK-HILL-P03 — Geocoding before email template
**Classification:** DIRECT
**Source location:** Show Progress / Solve in the right sequence
**What happens:** Two scopes with unknowns: geocoding (never done) and email notification. Push geocoding uphill first; an email template can be worked out in a day at the end.
**Why it is positive:** Surprises surface early, not at the end.
**Principle illustrated:** Scariest work first.

### SLICE-HILL-P04 — Splitting "Notify"
**Classification:** DIRECT
**Source location:** Prompts to refactor the scopes
**What happens:** "Notify" seemed stuck; it was three things (email design, delivery, in-app menu). Split into three scopes that move independently.
**Why it is positive:** Status becomes accurate; progress visible more often.

### ESTIMATE-HILL-P05 — Dinner party hill
**Classification:** DIRECT
**Source location:** Work is like a hill
**What happens:** Before choosing a dish, "percent complete" and prep-time estimates are meaningless; after choosing a recipe and shopping list (top of hill), estimating remaining steps is fair.
**Principle illustrated:** Estimate downhill work only.

## Negative examples / anti-patterns from the source

### SLICE-ONEPIECE-N01 — Horizontal layers
**Classification:** DIRECT
**Source location:** Integrate one slice
**What happens:** Designing many screens/templates not wired to a back-end, or back-end tasks checked off without UI.
**Why it is negative:** Work stays hypothetical; can't judge if logic is right without interacting.

### SLICE-ONEPIECE-N02 — Building peripheral/known first
**Classification:** DIRECT
**Source location:** Start in the middle
**What happens:** Starting with client-adding UI (same as regular user UI) or with login would move forward but teach nothing.
**Why it is negative:** Doesn't eliminate uncertainty.

### DERISK-HILL-N03 — Uphill in the head
**Classification:** DIRECT
**Source location:** Build your way uphill
**What happens:** Scope moved to the top of the hill on a theory ("I'll just use that API"), then slides back when reality is more complicated.
**Principle violated:** Validate with hands.

### ESTIMATE-HILL-N04 — Same estimate, different uncertainty
**Classification:** DIRECT
**Source location:** Estimates don't show uncertainty
**What happens:** Two "4 hour" tasks; one familiar, one novel—the novel one might take 2–3 days. "4 hours, or maybe 3 days" isn't a meaningful estimate.

### ORIENT-HANDOVER-N05 — Demanding early visible progress
**Classification:** DIRECT
**Source location:** Getting oriented
**What happens:** Managers ask for status too early; exploration goes underground.

### COMMIT-STOP-N06 — Accepting every "wouldn't it be better if…"
**Classification:** DIRECT
**Source location:** Limits motivate trade-offs
**What happens:** Without a deadline, a team easily delays the project for changes that don't deserve extra time.

## Contrastive pairs

### SLICE-ONEPIECE-C01 — Vertical vs horizontal
**Good / preferred:** One integrated slice you can click through (toggle wired to DB).
**Bad / discouraged:** Many unwired screens or back-end with no UI.
**Classification:** DIRECT
**Source location:** Integrate one slice; Case study
**Distinguishing feature:** Something real to try.

### SLICE-ONEPIECE-C02 — Core/novel vs peripheral/familiar first
**Good / preferred:** Visibility toggle (core, novel).
**Bad / discouraged:** Rename a client (peripheral) / add-client UI (familiar).
**Classification:** DIRECT
**Source location:** Start in the middle

### DERISK-HILL-C03 — Head vs hands
**Good / preferred:** "I'm far enough with what I've built that I don't believe there are other unknowns."
**Bad / discouraged:** "I've thought about this" treated as over the hill.
**Classification:** DIRECT
**Source location:** Build your way uphill

### CLOSE-STOP-C04 — Compare down vs up
**Good / preferred:** Compare to baseline ("better than what they have now").
**Bad / discouraged:** Compare to ideal ("never good enough").
**Classification:** DIRECT
**Source location:** Compare to baseline

### COMMIT-STOP-C05 — Extend vs circuit breaker
**Good / preferred (extend acceptable):** Only true must-haves remain, all downhill.
**Bad / discouraged:** Extending when uphill work remains.
**Classification:** DIRECT
**Source location:** When to extend a project

## Stop / go criteria

### GO
- A starting point has been chosen after orientation (core, small, novel).
- A piece is integrated end-to-end and clickable → can call it done and move on.
- Remaining work is downhill → estimation and finishing are appropriate.
- Only must-haves remain and all downhill → extension may be considered (rarely).

### STOP / RETURN
- Many tasks done, nothing clickable → stop and integrate one slice.
- Scope moved "over the hill" on theory only → return uphill; validate with code.
- Scope stuck → ask what the unknown is; split the scope if mis-drawn.
- Uphill work at the deadline → don't extend; return to shaping.
- New idea/edge case appears → ask "Is there time for this?" and hammer.

## Common failure modes
- Master plan of parts assembled at the end.
- Pixel-perfect design before wiring.
- Building login/setup first instead of the middle.
- Doing the easy/routine scope first; surprises at the end.
- Hiding "I don't know."
- Status by counting tasks.
- Comparing to an ideal and never shipping.

## Terms worth preserving
- `imagined tasks` / `discovered tasks` — assumed at start vs found by doing.
- `scope` — a named, independently completable part of the project (language of the project).
- `hill chart` / `uphill` / `downhill` — figuring out vs executing.
- `core / small / novel` — criteria for the first piece.
- `affordances` — inputs, buttons, places where data appears; the core of UI.
- `baseline` — customers' current reality.
- `scope hammering` — forcefully cutting scope to fit the time box.
- `must-have` / `nice-to-have (~)`.
- `circuit breaker` — unfinished work does not automatically get more time.
- `cool-down` — two-week slack between cycles.

## Candidate Skill rules
- `[DERIVED from Getting oriented]` Treat orientation in unfamiliar code as legitimate, time-bounded work; say explicitly "still figuring out where to start" rather than faking progress.
- `[DERIVED from Imagined vs discovered tasks]` Expect to discover tasks while working; record them as discovered, don't silently absorb them.
- `[DERIVED from Integrate one slice]` Do not build one layer fully before another; get one thin piece working end-to-end first.
- `[DERIVED from Start in the middle]` Choose the first piece that is core, small and novel; stub setup/peripheral parts.
- `[DERIVED from Program just enough]` Hard-code or stub what doesn't teach you anything about the problem.
- `[DERIVED from Build your way uphill]` Do not declare an approach validated until you've built enough to believe no unknowns remain.
- `[DERIVED from Solve in the right sequence]` Tackle the most uncertain part first; leave routine parts for last.
- `[DERIVED from Estimates don't show uncertainty]` Before trusting an estimate, ask whether the work is uphill or downhill; if uphill, reduce unknowns first.
- `[DERIVED from Scope hammering]` When new work appears, ask "is there time for this?" and classify it as must-have or nice-to-have (`~`).
- `[DERIVED from Compare to baseline]` Judge "good enough" against current behavior, not an ideal.
- `[DERIVED from When to extend]` If time runs out and unknowns remain, stop and return to de-risking instead of extending.

## Source limitations
- All four chapters describe a team (designer + programmers) in a six-week cycle with managers observing; for an individual developer, "managers stepping in after three days", hill charts and QA roles need adaptation. The three-day orientation threshold is team/cycle-scale and not a source-supported number for a small task.
- "Getting oriented" is described as necessary but the source gives no method for *how* to orient (what to read, how to map the code). ORIENT remains thinly grounded.
- The hill is a status/uncertainty tool, not an estimation method; it doesn't say how to estimate downhill work (EBS covers that).
- "Done means deployed" presumes deploy authority within the cycle.
- Scope hammering presumes the team has authority to cut scope; an individual developer may need to negotiate.

## Derived developer examples

### ORIENT-HANDOVER-D01 — Unfamiliar code base, new endpoint
**Classification:** DERIVED
**Grounded in:** Hand Over Responsibility — getting oriented; imagined vs discovered tasks
**Bad:** Immediately scaffold a new `/reports` endpoint in a new style, then discover the project has a routing convention, shared auth middleware and a serializer layer; rewrite.
**Good:** Spend a bounded block reading an existing comparable endpoint end-to-end (route → auth → handler → serializer → test), note the starting point, then begin; record discovered tasks (e.g. "serializer needs date format helper") as they appear.

### SLICE-ONEPIECE-D02 — Authenticated "favorite item" action
**Classification:** DERIVED
**Grounded in:** Get One Piece Done — integrate one slice; start in the middle; program just enough
**Bad:** Build the DB table, repository, service and full REST API for favorites, then the React button a week later.
**Good:** First slice: a button on the item page that calls one POST endpoint, saves a row for the current user and shows filled state on reload. Listing favorites, unfavoriting and counts come after.

### DERISK-HILL-D03 — Third-party API "I'll just use that API"
**Classification:** DERIVED
**Grounded in:** Show Progress — build uphill with hands; solve scariest first
**Bad:** Build the settings UI for a shipping-rates integration first, assuming the carrier API returns rates per package; at the end discover it needs dimensional weight and account-specific auth.
**Good:** First make one real sandbox call returning a rate for a hard-coded package; only then build the UI.

## ID register
| ID | Stage | Type | Short label | Classification | Location |
|---|---|---|---|---|---|
| ORIENT-HANDOVER-01 | ORIENT | rule | Lay of the land | DIRECT | Hand Over Responsibility / Getting oriented |
| ORIENT-HANDOVER-02 | ORIENT | rule | Can't dive in; exploration legit | DIRECT | Hand Over Responsibility / Getting oriented |
| ORIENT-HANDOVER-03 | ORIENT | rule | ~3 days then step in | DIRECT | Hand Over Responsibility / Getting oriented |
| CLOSE-HANDOVER-04 | CLOSE | rule | Imagined vs discovered tasks | DIRECT | Hand Over Responsibility / Imagined vs discovered tasks |
| ORIENT-HANDOVER-05 | ORIENT | rule | Start real work on meaningful piece | DIRECT | Hand Over Responsibility / Imagined vs discovered tasks |
| SLICE-HANDOVER-06 | SLICE | rule | Up-front tasks = paper shredder | DIRECT | Hand Over Responsibility / Assign projects, not tasks |
| CLOSE-HANDOVER-07 | CLOSE | rule | Done means deployed | DIRECT | Hand Over Responsibility / Done means deployed |
| ORIENT-HANDOVER-08 | ORIENT | rule | Orientation output = starting point | INFERRED | Hand Over Responsibility / Getting oriented |
| CLOSE-HANDOVER-10 | CLOSE | rule | Discovered tasks expected | INFERRED | Hand Over Responsibility; Show Progress |
| ORIENT-HANDOVER-11 | ORIENT | gate | Check in after ~3 days | DIRECT | Hand Over Responsibility / Getting oriented |
| ORIENT-HANDOVER-Q08 | ORIENT | question | How does the system work here | INFERRED | Hand Over Responsibility / Getting oriented |
| ORIENT-HANDOVER-N05 | ORIENT | negative | Demanding early progress | DIRECT | Hand Over Responsibility / Getting oriented |
| ORIENT-HANDOVER-D01 | ORIENT | derived | Orient before new endpoint | DERIVED | — |
| SLICE-ONEPIECE-01 | SLICE | rule | No 11th-hour master plan | DIRECT | Get One Piece Done / Intro |
| SLICE-ONEPIECE-02 | SLICE | rule | Integrate vertically | DIRECT | Get One Piece Done / Integrate one slice |
| IMPLEMENT-ONEPIECE-03 | IMPLEMENT | rule | Affordances before pixels | DIRECT | Get One Piece Done / Affordances before pixel-perfect screens |
| IMPLEMENT-ONEPIECE-04 | IMPLEMENT | rule | Program just enough | DIRECT | Get One Piece Done / Program just enough for the next step |
| SLICE-ONEPIECE-05 | SLICE | rule | Start in the middle | DIRECT | Get One Piece Done / Start in the middle |
| SLICE-ONEPIECE-06 | SLICE | rule | Core / small / novel | DIRECT | Get One Piece Done / Start in the middle |
| SLICE-ONEPIECE-07 | SLICE | gate | Prefer novel | DIRECT | Get One Piece Done / Start in the middle |
| SLICE-ONEPIECE-Q01 | SLICE | question | Core/small/novel? | INFERRED | Get One Piece Done / Start in the middle |
| SLICE-ONEPIECE-P01 | SLICE | positive | Visibility toggle first | DIRECT | Get One Piece Done / Case study |
| IMPLEMENT-ONEPIECE-P02 | IMPLEMENT | positive | Hard-coded HTTPAuth | DIRECT | Get One Piece Done / Program just enough |
| SLICE-ONEPIECE-N01 | SLICE | negative | Horizontal layers | DIRECT | Get One Piece Done / Integrate one slice |
| SLICE-ONEPIECE-N02 | SLICE | negative | Peripheral/familiar first | DIRECT | Get One Piece Done / Start in the middle |
| SLICE-ONEPIECE-C01 | SLICE | pair | Vertical vs horizontal | DIRECT | Get One Piece Done / Integrate one slice |
| SLICE-ONEPIECE-C02 | SLICE | pair | Core/novel vs peripheral | DIRECT | Get One Piece Done / Start in the middle |
| SLICE-ONEPIECE-D02 | SLICE | derived | Favorite action slice | DERIVED | — |
| ESTIMATE-HILL-01 | ESTIMATE | rule | Lists grow with progress | DIRECT | Show Progress / The tasks that aren't there |
| ESTIMATE-HILL-02 | ESTIMATE | rule | Estimates don't show uncertainty | DIRECT | Show Progress / Estimates don't show uncertainty |
| DERISK-HILL-03 | DERISK | rule | Uphill / downhill | DIRECT | Show Progress / Work is like a hill |
| ESTIMATE-HILL-04 | ESTIMATE | rule | Estimate at top of hill | DIRECT | Show Progress / Work is like a hill |
| DERISK-HILL-05 | DERISK | rule | Hands not head (thirds) | DIRECT | Show Progress / Build your way uphill |
| DERISK-HILL-06 | DERISK | rule | Scariest first | DIRECT | Show Progress / Solve in the right sequence |
| DERISK-HILL-07 | DERISK | rule | Stuck dot = raised hand | DIRECT | Show Progress / Nobody says “I don't know” |
| SLICE-HILL-08 | SLICE | rule | Refactor stuck scopes | DIRECT | Show Progress / Prompts to refactor the scopes |
| ESTIMATE-HILL-09 | ESTIMATE | rule | Trust estimates only downhill | INFERRED | Show Progress |
| DERISK-HILL-10 | DERISK | gate | Not solved until built | DIRECT | Show Progress / Build your way uphill |
| SLICE-HILL-11 | SLICE | gate | Split mis-drawn scope | DIRECT | Show Progress / Prompts to refactor the scopes |
| DERISK-HILL-Q02 | DERISK | question | Out of time: which is harder? | DIRECT | Show Progress / Solve in the right sequence |
| DERISK-HILL-Q03 | DERISK | question | What's the unknown holding it? | DIRECT | Show Progress / Status without asking |
| DERISK-HILL-Q04 | DERISK | question | Validated by building? | INFERRED | Show Progress / Build your way uphill |
| DERISK-HILL-P03 | DERISK | positive | Geocoding before email | DIRECT | Show Progress / Solve in the right sequence |
| SLICE-HILL-P04 | SLICE | positive | Split "Notify" | DIRECT | Show Progress / Prompts to refactor the scopes |
| ESTIMATE-HILL-P05 | ESTIMATE | positive | Dinner party | DIRECT | Show Progress / Work is like a hill |
| DERISK-HILL-N03 | DERISK | negative | Uphill in the head | DIRECT | Show Progress / Build your way uphill |
| ESTIMATE-HILL-N04 | ESTIMATE | negative | Two 4-hour tasks | DIRECT | Show Progress / Estimates don't show uncertainty |
| DERISK-HILL-C03 | DERISK | pair | Head vs hands | DIRECT | Show Progress / Build your way uphill |
| DERISK-HILL-D03 | DERISK | derived | Shipping-rates API | DERIVED | — |
| CLOSE-STOP-01 | CLOSE | rule | Compare to baseline | DIRECT | Decide When to Stop / Compare to baseline |
| COMMIT-STOP-02 | COMMIT | rule | Is there time for this? | DIRECT | Decide When to Stop / Limits motivate trade-offs |
| CLOSE-STOP-03 | CLOSE | rule | Scope grows like grass | DIRECT | Decide When to Stop / Scope grows like grass |
| CLOSE-STOP-04 | CLOSE | rule | Cutting ≠ lowering quality | DIRECT | Decide When to Stop / Cutting scope isn't lowering quality |
| CLOSE-STOP-05 | CLOSE | rule | Scope hammering questions | DIRECT | Decide When to Stop / Scope hammering |
| CLOSE-STOP-06 | CLOSE | rule | Must-have vs ~nice-to-have | DIRECT | Decide When to Stop / Scope hammering |
| CLOSE-STOP-07 | CLOSE | rule | QA findings nice-to-have by default | DIRECT | Decide When to Stop / QA is for the edges |
| COMMIT-STOP-08 | COMMIT | rule | When to extend | DIRECT | Decide When to Stop / When to extend a project |
| COMMIT-STOP-09 | COMMIT | gate | Uphill at deadline → reshape | DIRECT | Decide When to Stop / When to extend a project |
| CLOSE-STOP-Q05 | CLOSE | question | Baseline today? | DIRECT | Decide When to Stop / Compare to baseline |
| CLOSE-STOP-Q06 | CLOSE | question | Is there time for this? | DIRECT | Decide When to Stop / Limits motivate trade-offs |
| CLOSE-STOP-Q07 | CLOSE | question | Scope hammering list | DIRECT | Decide When to Stop / Scope hammering |
| COMMIT-STOP-N06 | COMMIT | negative | Accepting every improvement | DIRECT | Decide When to Stop / Limits motivate trade-offs |
| CLOSE-STOP-C04 | CLOSE | pair | Compare down vs up | DIRECT | Decide When to Stop / Compare to baseline |
| COMMIT-STOP-C05 | COMMIT | pair | Extend vs circuit breaker | DIRECT | Decide When to Stop / When to extend a project |
