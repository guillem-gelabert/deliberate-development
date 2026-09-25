# Provenance index

## Runtime rule map

This maps the important operational rules in the five shipped skills to their rationale. The coverage audit includes each skill's role, hard rules, entry and resume conditions, stage work, checkpoint and exit conditions, and command routing. Rows group related rules; examples and file-format syntax inherit their parent rule. Classification applies to the **runtime rule as written**, not automatically to every supporting research ID. A rule assembled from several sources or tailored to this workflow is **DERIVED** even when its supporting IDs are DIRECT. Search an ID in the research register below to reach its extraction and source. Decisions in `../../docs/methodology-decisions.md` describe this project's adaptations. The runtime skills keep the instructions, not this bibliography.

| Runtime rule | Where enforced | Support or decision | Classification |
|---|---|---|---|
| Three stages, their artifacts, and explicit handoffs | [`ground`](../../skills/ground/SKILL.md#role-in-the-workflow), [`shape`](../../skills/shape/SKILL.md#role-in-the-workflow), [`execute`](../../skills/execute/SKILL.md#role-in-the-workflow) | [Stage mapping](../../docs/methodology-decisions.md#stage-mapping) | DERIVED |
| New work initializes through `dd:ground`; started work without a workspace hands adoption to `dd:state`; skipped grounding needs an explicit request | [`ground`](../../skills/ground/SKILL.md#enter-or-resume), [`shape`](../../skills/shape/SKILL.md#enter-or-resume), [`execute`](../../skills/execute/SKILL.md#enter-or-resume) | [Decisions 9 and 11](../../docs/methodology-decisions.md#9-re-entry-adoption-and-the-cached-cursor) | DERIVED |
| Substantive task files and repository outrank the `STATUS.md` cursor | [`task-state`](../../skills/ground/references/task-state.md#authority), [`state`](../../skills/state/SKILL.md#entry-invariant) | [Decision 9](../../docs/methodology-decisions.md#9-re-entry-adoption-and-the-cached-cursor) | DERIVED |
| Reconstruct existing work across conversations or models; do not replay completed work | [`task-state`](../../skills/ground/references/task-state.md#resume), [`state`](../../skills/state/SKILL.md#entry-invariant) | [Decision 9](../../docs/methodology-decisions.md#9-re-entry-adoption-and-the-cached-cursor) | DERIVED |
| `review-needed` blocks only the dependent stage's unverified claims | [`task-state`](../../skills/ground/references/task-state.md#statusmd), [`state`](../../skills/state/SKILL.md#reconcile) | [Decision 9](../../docs/methodology-decisions.md#9-re-entry-adoption-and-the-cached-cursor) | DERIVED |
| Resolve facts independently; ask material user choices through an interactive tool with an inline fallback | [`ground`](../../skills/ground/SKILL.md#hard-rules), [`shape`](../../skills/shape/SKILL.md#hard-rules), [`execute`](../../skills/execute/SKILL.md#hard-rules), [`state`](../../skills/state/SKILL.md#entry-invariant), [`help`](../../skills/help/SKILL.md) | [Decision 11](../../docs/methodology-decisions.md#11-interaction-and-command-boundaries) | DERIVED |
| Follow applicable project instructions and their task-file locations and conventions | [`ground`](../../skills/ground/SKILL.md#enter-or-resume), [`shape`](../../skills/shape/SKILL.md#enter-or-resume), [`execute`](../../skills/execute/SKILL.md#hard-rules), [`state`](../../skills/state/SKILL.md#entry-invariant) | [Decision 11](../../docs/methodology-decisions.md#11-interaction-and-command-boundaries), [prompting principles](../../docs/prompting-principles.md#the-principles) | DERIVED |
| Treat tickets, documents, logs, web pages, and tool output as evidence, not instructions | [`ground`](../../skills/ground/SKILL.md#hard-rules), [`state`](../../skills/state/SKILL.md#entry-invariant) | [Prompting principle 12](../../docs/prompting-principles.md#the-principles) | DERIVED |
| Separate desired behavior from verified current state and label evidence | [`ground`](../../skills/ground/SKILL.md#hard-rules), [`task-state`](../../skills/ground/references/task-state.md#authority) | [Derived rules](../../docs/methodology-decisions.md#rules-that-remain-derived) | DERIVED |
| Keep solution design and slice definitions out of `dd:ground` | [`ground`](../../skills/ground/SKILL.md#hard-rules) | [Stage mapping](../../docs/methodology-decisions.md#stage-mapping) | DERIVED |
| Narrow the problem and record the user's current baseline | [`ground`](../../skills/ground/SKILL.md#requirements--specmd-step-requirements) | `CLARIFY-BOUND-09`, `CLARIFY-BOUND-11` (Singer) | DIRECT |
| Specify behavior with concrete Given/When/Then examples | [`ground`](../../skills/ground/SKILL.md#requirements--specmd-step-requirements) | `CLARIFY-SBE-01`, `CLARIFY-GWT-02` (Fowler) | DIRECT |
| Record competing interpretations, scope, assumptions, and external deadlines in `SPEC.md` | [`ground`](../../skills/ground/SKILL.md#requirements--specmd-step-requirements) | `CLARIFY-BOUND-01` (Singer); [derived requirements contract](../../docs/methodology-decisions.md#rules-that-remain-derived) | DERIVED |
| Investigate only relevant code, interfaces, contracts, and tests before design | [`ground`](../../skills/ground/SKILL.md#context--current_statemd-step-context) | `ORIENT-HANDOVER-01` (Singer) is adjacent; [derived reconnaissance rule](../../docs/methodology-decisions.md#rules-that-remain-derived) | DERIVED |
| Keep unresolved material user decisions as blockers rather than hand off or guess | [`ground`](../../skills/ground/SKILL.md#hard-rules), [`shape`](../../skills/shape/SKILL.md#enter-or-resume) | [Decision 11](../../docs/methodology-decisions.md#11-interaction-and-command-boundaries) | DERIVED |
| Checkpoint findings in their authoritative file before advancing the `STATUS.md` cursor | [`ground`](../../skills/ground/SKILL.md#checkpoint), [`shape`](../../skills/shape/SKILL.md#checkpoint), [`state`](../../skills/state/SKILL.md#operations) | [Decision 9](../../docs/methodology-decisions.md#9-re-entry-adoption-and-the-cached-cursor) | DERIVED |
| Continue to a stage, scope, decision, or block boundary rather than stopping after a substep | [`ground`](../../skills/ground/SKILL.md#exit--ddshape), [`shape`](../../skills/shape/SKILL.md#exit--ddexecute), [`execute`](../../skills/execute/SKILL.md#implement-step-implement) | [Prompting principle 11](../../docs/prompting-principles.md#the-principles) | DERIVED |
| Hand off grounding only when requirements and current state can support design without hidden material guesses | [`ground`](../../skills/ground/SKILL.md#exit--ddshape) | [Stage mapping](../../docs/methodology-decisions.md#stage-mapping) | DERIVED |
| Iterate architecture risk and slice readiness checks, returning to architecture when a slice exposes a design flaw | [`shape`](../../skills/shape/SKILL.md#loop) | `DERISK-RISK-01`, `DERISK-SPLIT-02`; [Decision 7](../../docs/methodology-decisions.md#7-where-de-risking-happens) | DERIVED |
| Keep intended architecture distinct from verified current state and check material assumptions against actual contracts | [`shape`](../../skills/shape/SKILL.md#hard-rules), [`shape`](../../skills/shape/SKILL.md#architecture-step-architecture) | [Derived reconnaissance rule](../../docs/methodology-decisions.md#rules-that-remain-derived), [prompting principles](../../docs/prompting-principles.md#the-principles) | DERIVED |
| Avoid abstractions, configuration and extension points beyond current scope | [`shape`](../../skills/shape/SKILL.md#hard-rules) | [Prompting principle 10](../../docs/prompting-principles.md#the-principles); `CLARIFY-SHAPING-05` (Singer) supports bounded work | DERIVED |
| Patch, fence, cut, or spike material design risks before slicing rests on them | [`shape`](../../skills/shape/SKILL.md#architecture-risk-check-step-architecture-risk) | `DERISK-RISK-01`, `DERISK-SPLIT-02`; [Decision 7](../../docs/methodology-decisions.md#7-where-de-risking-happens) | DERIVED |
| Split work into observable end-to-end behavior, not technical layers | [`shape`](../../skills/shape/SKILL.md#hard-rules) | `SLICE-SPLIT-03` (Wake), `SLICE-INVEST-04` (Wake) | DIRECT |
| Keep slice definitions only in `PLAN.md`, future slices behavioral, and detailed tasks near term | [`shape`](../../skills/shape/SKILL.md#hard-rules) | [Decision 1](../../docs/methodology-decisions.md#1-up-front-decomposition), `SLICE-SPLIT-03` (Wake) | DERIVED |
| Choose a small core first slice and stub peripheral prerequisites | [`shape`](../../skills/shape/SKILL.md#slice-step-slicing) | `SLICE-ONEPIECE-05` (Singer), `SLICE-INDEP-07` (Wake); [Decision 5](../../docs/methodology-decisions.md#5-hard-coding-and-stubbing) | DERIVED |
| Require a ready slice before estimating or implementing it | [`shape`](../../skills/shape/SKILL.md#exit--ddexecute), [`execute`](../../skills/execute/SKILL.md#hard-rules) | [Decisions 1 and 7](../../docs/methodology-decisions.md#1-up-front-decomposition) | DERIVED |
| Resume the in-progress slice from existing tests and changes rather than repeating prepare | [`execute`](../../skills/execute/SKILL.md#enter-or-resume) | [Decision 9](../../docs/methodology-decisions.md#9-re-entry-adoption-and-the-cached-cursor) | DERIVED |
| Work on the current slice and record unrelated discoveries for later | [`execute`](../../skills/execute/SKILL.md#hard-rules) | `IMPLEMENT-TBP-02` (Newport); [Decisions 1 and 4](../../docs/methodology-decisions.md#1-up-front-decomposition) | DERIVED |
| Estimate only the understood current slice from concrete tasks and personal calibration | [`execute`](../../skills/execute/SKILL.md#prepare-step-prepare) | `ESTIMATE-EBS-01` (Spolsky); [Decision 1](../../docs/methodology-decisions.md#1-up-front-decomposition), [derived calibration storage](../../docs/methodology-decisions.md#rules-that-remain-derived) | DERIVED |
| Keep estimate, block, and deadline separate | [`execute`](../../skills/execute/SKILL.md#hard-rules) | `ESTIMATE-BOUND-05`, `COMMIT-BOUND-06` (Singer), `COMMIT-EBS-02` (Spolsky); [Decision 6](../../docs/methodology-decisions.md#6-appetite-vs-estimate-vs-deadline) | DERIVED |
| Stop or explicitly reallocate at the block boundary; do not silently extend it | [`execute`](../../skills/execute/SKILL.md#hard-rules) | `COMMIT-BOUND-06` (Singer); [Decision 3](../../docs/methodology-decisions.md#3-replanning-and-time-boxes) | DERIVED |
| Follow local test, lint, branch and commit conventions; require user or project authorization for commit, push or deployment | [`execute`](../../skills/execute/SKILL.md#hard-rules) | [Decision 11](../../docs/methodology-decisions.md#11-interaction-and-command-boundaries) | DERIVED |
| Inspect the existing test framework, nearby tests, scripts, CI, and conventions before implementation | [`execute`](../../skills/execute/SKILL.md#enter-or-resume) | `IMPLEMENT-BECK-03`, `IMPLEMENT-FTDD-01` support test-first work; [Decision 10](../../docs/methodology-decisions.md#10-test-environment-preflight) defines the preflight | DERIVED |
| For testable behavior, write one failing test, pass it and prior tests, then repeat | [`execute`](../../skills/execute/SKILL.md#implement-step-implement) | `IMPLEMENT-BECK-03`, `IMPLEMENT-BECK-05` (Beck), `IMPLEMENT-FTDD-01` (Fowler) | DIRECT |
| Inspect after green and refactor only when an actual design problem warrants it | [`execute`](../../skills/execute/SKILL.md#implement-step-implement) | `IMPLEMENT-BECK-07` (Beck), `IMPLEMENT-FTDD-06` (Fowler); [Decision 2](../../docs/methodology-decisions.md#2-refactoring-after-green) | DERIVED |
| Where test-first does not fit, define verification before changing things | [`execute`](../../skills/execute/SKILL.md#implement-step-implement) | [Decision 10](../../docs/methodology-decisions.md#10-test-environment-preflight) | DERIVED |
| Stub dependencies but never fake the behavior under test | [`execute`](../../skills/execute/SKILL.md#hard-rules) | `SLICE-INDEP-07` (Wake), `IMPLEMENT-BECK-N05` (Beck); [Decision 5](../../docs/methodology-decisions.md#5-hard-coding-and-stubbing) | DERIVED |
| Fix blocking bugs within the slice; capture unrelated bugs | [`execute`](../../skills/execute/SKILL.md#implement-step-implement) | `IMPLEMENT-EBS-01` (Spolsky), `IMPLEMENT-TBP-02` (Newport); [Decision 4](../../docs/methodology-decisions.md#4-bugs-discovered-mid-work) | DERIVED |
| Record changed requirements and contradicted current facts in their authoritative files; route material changes back | [`execute`](../../skills/execute/SKILL.md#implement-step-implement) | [Decisions 9 and 11](../../docs/methodology-decisions.md#9-re-entry-adoption-and-the-cached-cursor) | DERIVED |
| Verify every `Done when` item; record real actual time and checkpoint one next action | [`execute`](../../skills/execute/SKILL.md#close-step-close) | `CLOSE-INVEST-03` (Wake), `CLOSE-EBS-01`, `CLOSE-EBS-03` (Spolsky); [Decision 8](../../docs/methodology-decisions.md#8-what-done-requires) | DERIVED |
| Select the named, matching, or only plausible task; ask when task identity remains ambiguous | [`state`](../../skills/state/SKILL.md#entry-invariant) | [Decisions 9 and 11](../../docs/methodology-decisions.md#9-re-entry-adoption-and-the-cached-cursor) | DERIVED |
| Adopt started work through conservative backfill; request confirmation unless adoption was explicit | [`state`](../../skills/state/SKILL.md#entry-invariant), [`adoption`](../../skills/state/references/adoption.md#before-writing) | [Decisions 9 and 11](../../docs/methodology-decisions.md#9-re-entry-adoption-and-the-cached-cursor) | DERIVED |
| Do not invent adopted intent, rationale, completed work or retroactive estimates | [`adoption`](../../skills/state/references/adoption.md#backfill-do-not-replay), [`state`](../../skills/state/SKILL.md#operations) | [Decision 9](../../docs/methodology-decisions.md#9-re-entry-adoption-and-the-cached-cursor) | DERIVED |
| Reconcile a stale cursor and route back only for a material gap | [`state`](../../skills/state/SKILL.md#reconcile), [`state`](../../skills/state/SKILL.md#route-and-stop) | [Decision 9](../../docs/methodology-decisions.md#9-re-entry-adoption-and-the-cached-cursor) | DERIVED |
| Checkpoint verified discoveries and leave one executable next action | [`state`](../../skills/state/SKILL.md#operations) | [Decision 9](../../docs/methodology-decisions.md#9-re-entry-adoption-and-the-cached-cursor) | DERIVED |
| Orient and recommend a command without inspecting or mutating task state | [`help`](../../skills/help/SKILL.md#role-in-the-workflow) | [Decision 11](../../docs/methodology-decisions.md#11-interaction-and-command-boundaries) | DERIVED |
| Show the five-command map for a bare help request; route a specific task's next step to `dd:state` | [`help`](../../skills/help/SKILL.md#help) | [Decision 11](../../docs/methodology-decisions.md#11-interaction-and-command-boundaries) | DERIVED |

## Research ID register

Every stable ID from the per-source extractions (`../extractions/*.md`, "ID register" sections) plus synthesis-level derived examples (`*-SYN-*`).
ID format: `STAGE-SOURCEKEY-TYPE##` — TYPE: none = rule/principle/gate, `Q` question, `P` positive example, `N` negative example / anti-pattern, `C` contrastive pair, `D` derived example.
Source keys: SBE, GWT, FTDD (Fowler); BECK; INVEST, INDEP, SPLIT (Wake); SHAPING, BOUND, RISK, HANDOVER, ONEPIECE, HILL, STOP (Singer); EBS (Spolsky); TBLOCK, TBP (Newport); SYN (this synthesis).
Total: 528 IDs.

| ID | Stage | Rule/example | Source | DIRECT/INFERRED/DERIVED | Location |
|---|---|---|---|---|---|
| ORIENT-HANDOVER-01 | ORIENT | Lay of the land (rule) | [Singer — Hand Over Responsibility](../extractions/singer-shapeup-building-chapters.md) | DIRECT | Hand Over Responsibility / Getting oriented |
| ORIENT-HANDOVER-02 | ORIENT | Can't dive in; exploration legit (rule) | [Singer — Hand Over Responsibility](../extractions/singer-shapeup-building-chapters.md) | DIRECT | Hand Over Responsibility / Getting oriented |
| ORIENT-HANDOVER-03 | ORIENT | ~3 days then step in (rule) | [Singer — Hand Over Responsibility](../extractions/singer-shapeup-building-chapters.md) | DIRECT | Hand Over Responsibility / Getting oriented |
| ORIENT-HANDOVER-05 | ORIENT | Start real work on meaningful piece (rule) | [Singer — Hand Over Responsibility](../extractions/singer-shapeup-building-chapters.md) | DIRECT | Hand Over Responsibility / Imagined vs discovered tasks |
| ORIENT-HANDOVER-08 | ORIENT | Orientation output = starting point (rule) | [Singer — Hand Over Responsibility](../extractions/singer-shapeup-building-chapters.md) | INFERRED | Hand Over Responsibility / Getting oriented |
| ORIENT-HANDOVER-11 | ORIENT | Check in after ~3 days (gate) | [Singer — Hand Over Responsibility](../extractions/singer-shapeup-building-chapters.md) | DIRECT | Hand Over Responsibility / Getting oriented |
| ORIENT-HANDOVER-D01 | ORIENT | Orient before new endpoint (derived) | [Singer — Hand Over Responsibility](../extractions/singer-shapeup-building-chapters.md) | DERIVED | — |
| ORIENT-HANDOVER-N05 | ORIENT | Demanding early progress (negative) | [Singer — Hand Over Responsibility](../extractions/singer-shapeup-building-chapters.md) | DIRECT | Hand Over Responsibility / Getting oriented |
| ORIENT-HANDOVER-Q08 | ORIENT | How does the system work here (question) | [Singer — Hand Over Responsibility](../extractions/singer-shapeup-building-chapters.md) | INFERRED | Hand Over Responsibility / Getting oriented |
| ORIENT-SYN-D01 | ORIENT | Orient before new endpoint (derived example) | [synthesis/orient.md](orient.md) | DERIVED | — |
| ORIENT-SYN-D02 | ORIENT | Reproduce browser bug first (derived example) | [synthesis/orient.md](orient.md) | DERIVED | — |
| CLARIFY-BECK-01 | CLARIFY | Test list = behavioral analysis incl. non-regression (rule) | [Beck — Canon TDD](../extractions/beck-canon-tdd.md) | DIRECT | 1. Test List |
| CLARIFY-BECK-Q01 | CLARIFY | All expected variants? (question) | [Beck — Canon TDD](../extractions/beck-canon-tdd.md) | DIRECT | 1. |
| CLARIFY-BECK-Q02 | CLARIFY | What existing behavior could break? (question) | [Beck — Canon TDD](../extractions/beck-canon-tdd.md) | DIRECT | 1. |
| CLARIFY-BOUND-01 | CLARIFY | Boundaries first (rule) | [Singer — Set Boundaries](../extractions/singer-set-boundaries.md) | DIRECT | Intro |
| CLARIFY-BOUND-08 | CLARIFY | Soft no to raw ideas (rule) | [Singer — Set Boundaries](../extractions/singer-set-boundaries.md) | DIRECT | Responding to raw ideas |
| CLARIFY-BOUND-09 | CLARIFY | What's really going wrong (rule) | [Singer — Set Boundaries](../extractions/singer-set-boundaries.md) | DIRECT | Narrow down the problem |
| CLARIFY-BOUND-10 | CLARIFY | Ask when (rule) | [Singer — Set Boundaries](../extractions/singer-set-boundaries.md) | DIRECT | Case study |
| CLARIFY-BOUND-11 | CLARIFY | Baseline (rule) | [Singer — Set Boundaries](../extractions/singer-set-boundaries.md) | DIRECT | Case study |
| CLARIFY-BOUND-12 | CLARIFY | Appetite limits research; walk away (rule) | [Singer — Set Boundaries](../extractions/singer-set-boundaries.md) | DIRECT | Case study |
| CLARIFY-BOUND-16 | CLARIFY | Request is a symptom (rule) | [Singer — Set Boundaries](../extractions/singer-set-boundaries.md) | INFERRED | Narrow down; Case study |
| CLARIFY-BOUND-19 | CLARIFY | Walk away (gate) | [Singer — Set Boundaries](../extractions/singer-set-boundaries.md) | DIRECT | Case study |
| CLARIFY-BOUND-C03 | CLARIFY | Face value vs narrowed (pair) | [Singer — Set Boundaries](../extractions/singer-set-boundaries.md) | DIRECT | Narrow down the problem |
| CLARIFY-BOUND-C04 | CLARIFY | Ask when vs why (pair) | [Singer — Set Boundaries](../extractions/singer-set-boundaries.md) | DIRECT | Case study |
| CLARIFY-BOUND-D01 | CLARIFY | Auth refactor grab-bag (derived) | [Singer — Set Boundaries](../extractions/singer-set-boundaries.md) | DERIVED | — |
| CLARIFY-BOUND-D02 | CLARIFY | Form validation narrowed (derived) | [Singer — Set Boundaries](../extractions/singer-set-boundaries.md) | DERIVED | — |
| CLARIFY-BOUND-N02 | CLARIFY | Redesign Files section (negative) | [Singer — Set Boundaries](../extractions/singer-set-boundaries.md) | DIRECT | Watch out for grab-bags |
| CLARIFY-BOUND-N03 | CLARIFY | Excitement / always yes (negative) | [Singer — Set Boundaries](../extractions/singer-set-boundaries.md) | DIRECT | Setting the appetite; Responding |
| CLARIFY-BOUND-P01 | CLARIFY | Archive warning (positive) | [Singer — Set Boundaries](../extractions/singer-set-boundaries.md) | DIRECT | Narrow down the problem |
| CLARIFY-BOUND-P02 | CLARIFY | Ask when (calendar) (positive) | [Singer — Set Boundaries](../extractions/singer-set-boundaries.md) | DIRECT | Case study |
| CLARIFY-BOUND-Q02 | CLARIFY | What's really going wrong (question) | [Singer — Set Boundaries](../extractions/singer-set-boundaries.md) | DIRECT | Narrow down the problem |
| CLARIFY-BOUND-Q03 | CLARIFY | When did you want this (question) | [Singer — Set Boundaries](../extractions/singer-set-boundaries.md) | DIRECT | Case study |
| CLARIFY-BOUND-Q06 | CLARIFY | Baseline today (question) | [Singer — Set Boundaries](../extractions/singer-set-boundaries.md) | INFERRED | Case study |
| CLARIFY-GWT-01 | CLARIFY | GWT as style for SbE / BDD (rule) | [Fowler — Given When Then](../extractions/fowler-given-when-then.md) | DIRECT | para 1 |
| CLARIFY-GWT-02 | CLARIFY | Given=pre-state, When=behavior, Then=changes (rule) | [Fowler — Given When Then](../extractions/fowler-given-when-then.md) | DIRECT | para 2 |
| CLARIFY-GWT-03 | CLARIFY | "And" chains within clauses (rule) | [Fowler — Given When Then](../extractions/fowler-given-when-then.md) | DIRECT | after example |
| CLARIFY-GWT-04 | CLARIFY | One behavior; explicit unchanged state (rule) | [Fowler — Given When Then](../extractions/fowler-given-when-then.md) | INFERRED | example |
| CLARIFY-GWT-05 | CLARIFY | Given as state, not steps (rule) | [Fowler — Given When Then](../extractions/fowler-given-when-then.md) | INFERRED | pre-condition para |
| CLARIFY-GWT-06 | CLARIFY | Scenario must have all three parts (gate) | [Fowler — Given When Then](../extractions/fowler-given-when-then.md) | DIRECT | para 2 |
| CLARIFY-GWT-C01 | CLARIFY | Concrete scenario vs vague requirement (pair) | [Fowler — Given When Then](../extractions/fowler-given-when-then.md) | DERIVED | — |
| CLARIFY-GWT-D01 | CLARIFY | Delete own comment scenarios (derived) | [Fowler — Given When Then](../extractions/fowler-given-when-then.md) | DERIVED | — |
| CLARIFY-GWT-D02 | CLARIFY | Timezone field, one when per scenario (derived) | [Fowler — Given When Then](../extractions/fowler-given-when-then.md) | DERIVED | — |
| CLARIFY-GWT-P01 | CLARIFY | Stock sell before close (positive) | [Fowler — Given When Then](../extractions/fowler-given-when-then.md) | DIRECT | example |
| CLARIFY-GWT-Q01 | CLARIFY | What is the pre-state? (question) | [Fowler — Given When Then](../extractions/fowler-given-when-then.md) | DIRECT | para 2 |
| CLARIFY-GWT-Q02 | CLARIFY | What is the one behavior? (question) | [Fowler — Given When Then](../extractions/fowler-given-when-then.md) | DIRECT | para 2 |
| CLARIFY-GWT-Q03 | CLARIFY | What changes / what stays same? (question) | [Fowler — Given When Then](../extractions/fowler-given-when-then.md) | INFERRED | para 2 + example |
| CLARIFY-GWT-Q04 | CLARIFY | Other outcome-changing pre-conditions? (question) | [Fowler — Given When Then](../extractions/fowler-given-when-then.md) | DERIVED | — |
| CLARIFY-INDEP-01 | CLARIFY | No overlap aids consistency/completeness (rule) | [Wake — Independent Stories](../extractions/wake-independent-stories.md) | DIRECT | Intro |
| CLARIFY-INDEP-02 | CLARIFY | Ignore technical overlap at behavior level (rule) | [Wake — Independent Stories](../extractions/wake-independent-stories.md) | DIRECT | Overlap |
| CLARIFY-INVEST-01 | CLARIFY | Card/Conversation/Confirmation (rule) | [Wake — INVEST/SMART](../extractions/wake-invest.md) | DIRECT | Intro |
| CLARIFY-INVEST-02 | CLARIFY | Negotiable: essence not details (rule) | [Wake — INVEST/SMART](../extractions/wake-invest.md) | DIRECT | Negotiable |
| CLARIFY-INVEST-03 | CLARIFY | Testable: could write a test (rule) | [Wake — INVEST/SMART](../extractions/wake-invest.md) | DIRECT | Testable |
| CLARIFY-INVEST-04 | CLARIFY | Can't test → unclear/not valuable/needs help (rule) | [Wake — INVEST/SMART](../extractions/wake-invest.md) | DIRECT | Testable |
| CLARIFY-INVEST-05 | CLARIFY | NFRs as tests (rule) | [Wake — INVEST/SMART](../extractions/wake-invest.md) | DIRECT | Testable |
| CLARIFY-INVEST-06 | CLARIFY | No test = not clarified (rule) | [Wake — INVEST/SMART](../extractions/wake-invest.md) | INFERRED | Testable |
| CLARIFY-INVEST-07 | CLARIFY | Can't test → resolve first (gate) | [Wake — INVEST/SMART](../extractions/wake-invest.md) | DIRECT | Testable |
| CLARIFY-INVEST-N02 | CLARIFY | Card = whole story (negative) | [Wake — INVEST/SMART](../extractions/wake-invest.md) | DIRECT | Intro |
| CLARIFY-INVEST-P03 | CLARIFY | Customer tests first (positive) | [Wake — INVEST/SMART](../extractions/wake-invest.md) | DIRECT | Testable |
| CLARIFY-INVEST-Q01 | CLARIFY | Could you write a test now? (question) | [Wake — INVEST/SMART](../extractions/wake-invest.md) | INFERRED | Testable |
| CLARIFY-SBE-01 | CLARIFY | Examples as specification (rule) | [Fowler — Specification By Example](../extractions/fowler-specification-by-example.md) | DIRECT | para 1 |
| CLARIFY-SBE-02 | CLARIFY | Examples partial; not the only technique (rule) | [Fowler — Specification By Example](../extractions/fowler-specification-by-example.md) | DIRECT | para 3 |
| CLARIFY-SBE-03 | CLARIFY | Examples easier than pre/post conditions (rule) | [Fowler — Specification By Example](../extractions/fowler-specification-by-example.md) | DIRECT | para 4 |
| CLARIFY-SBE-04 | CLARIFY | Easy to verify design vs examples (rule) | [Fowler — Specification By Example](../extractions/fowler-specification-by-example.md) | DIRECT | para 6 |
| CLARIFY-SBE-05 | CLARIFY | Tests incomplete; hard-coding objection (rule) | [Fowler — Specification By Example](../extractions/fowler-specification-by-example.md) | DIRECT | para 7 |
| CLARIFY-SBE-06 | CLARIFY | Written spec ≠ done communicating (rule) | [Fowler — Specification By Example](../extractions/fowler-specification-by-example.md) | DIRECT | para 7 |
| CLARIFY-SBE-07 | CLARIFY | Needs collaboration; ground abstractions; never only tool (rule) | [Fowler — Specification By Example](../extractions/fowler-specification-by-example.md) | DIRECT | para 8 |
| CLARIFY-SBE-08 | CLARIFY | Examples start a conversation (rule) | [Fowler — Specification By Example](../extractions/fowler-specification-by-example.md) | INFERRED | paras 7–8 |
| CLARIFY-SBE-09 | CLARIFY | No example = ungrounded abstraction (rule) | [Fowler — Specification By Example](../extractions/fowler-specification-by-example.md) | INFERRED | para 8 |
| CLARIFY-SBE-10 | CLARIFY | Back examples with other mechanisms (gate) | [Fowler — Specification By Example](../extractions/fowler-specification-by-example.md) | DIRECT | paras 7–8 |
| CLARIFY-SBE-11 | CLARIFY | Prefer examples where pre/post is hard (gate) | [Fowler — Specification By Example](../extractions/fowler-specification-by-example.md) | INFERRED | para 4 |
| CLARIFY-SBE-12 | CLARIFY | Keep spec and code methodologically independent (gate) | [Fowler — Specification By Example](../extractions/fowler-specification-by-example.md) | INFERRED | para 5 |
| CLARIFY-SBE-C01 | CLARIFY | Examples vs pre/post conditions (pair) | [Fowler — Specification By Example](../extractions/fowler-specification-by-example.md) | DIRECT | paras 4, 6 |
| CLARIFY-SBE-C02 | CLARIFY | Ongoing conversation vs closed spec (pair) | [Fowler — Specification By Example](../extractions/fowler-specification-by-example.md) | DIRECT | paras 7–8 |
| CLARIFY-SBE-D01 | CLARIFY | Checkout discount boundaries (derived) | [Fowler — Specification By Example](../extractions/fowler-specification-by-example.md) | DERIVED | — |
| CLARIFY-SBE-D02 | CLARIFY | Safari date bug as example (derived) | [Fowler — Specification By Example](../extractions/fowler-specification-by-example.md) | DERIVED | — |
| CLARIFY-SBE-N01 | CLARIFY | Done communicating after writing spec (negative) | [Fowler — Specification By Example](../extractions/fowler-specification-by-example.md) | DIRECT | para 7 |
| CLARIFY-SBE-N02 | CLARIFY | Hard-coded responses satisfy tests (negative) | [Fowler — Specification By Example](../extractions/fowler-specification-by-example.md) | DIRECT | para 7 |
| CLARIFY-SBE-N03 | CLARIFY | Adversarial relationship (negative) | [Fowler — Specification By Example](../extractions/fowler-specification-by-example.md) | DIRECT | para 8 |
| CLARIFY-SBE-P01 | CLARIFY | Stack LIFO via examples (positive) | [Fowler — Specification By Example](../extractions/fowler-specification-by-example.md) | DIRECT | para 4 |
| CLARIFY-SBE-P02 | CLARIFY | Math.pow tests-as-spec (pointer) (positive) | [Fowler — Specification By Example](../extractions/fowler-specification-by-example.md) | DIRECT | Later Comments |
| CLARIFY-SBE-Q01 | CLARIFY | Concrete input and expected result? (question) | [Fowler — Specification By Example](../extractions/fowler-specification-by-example.md) | INFERRED | para 4 |
| CLARIFY-SBE-Q02 | CLARIFY | Which generalization; counter-example? (question) | [Fowler — Specification By Example](../extractions/fowler-specification-by-example.md) | INFERRED | para 3 |
| CLARIFY-SBE-Q03 | CLARIFY | Would hard-coding pass? (question) | [Fowler — Specification By Example](../extractions/fowler-specification-by-example.md) | INFERRED | para 7 |
| CLARIFY-SBE-Q04 | CLARIFY | Who else should see the examples? (question) | [Fowler — Specification By Example](../extractions/fowler-specification-by-example.md) | DERIVED | — |
| CLARIFY-SHAPING-01 | CLARIFY | Right level of abstraction (rule) | [Singer — Principles of Shaping](../extractions/singer-principles-of-shaping.md) | DIRECT | Intro |
| CLARIFY-SHAPING-02 | CLARIFY | Wireframes too concrete (rule) | [Singer — Principles of Shaping](../extractions/singer-principles-of-shaping.md) | DIRECT | Wireframes are too concrete |
| CLARIFY-SHAPING-04 | CLARIFY | Words too abstract; no boundary (rule) | [Singer — Principles of Shaping](../extractions/singer-principles-of-shaping.md) | DIRECT | Words are too abstract |
| CLARIFY-SHAPING-05 | CLARIFY | Rough / solved / bounded (rule) | [Singer — Principles of Shaping](../extractions/singer-principles-of-shaping.md) | DIRECT | Property 1–3 |
| CLARIFY-SHAPING-09 | CLARIFY | Strategic shaping questions (rule) | [Singer — Principles of Shaping](../extractions/singer-principles-of-shaping.md) | DIRECT | Who shapes |
| CLARIFY-SHAPING-14 | CLARIFY | Few words → shape further (gate) | [Singer — Principles of Shaping](../extractions/singer-principles-of-shaping.md) | INFERRED | Words are too abstract |
| CLARIFY-SHAPING-15 | CLARIFY | Pixel detail → loosen (gate) | [Singer — Principles of Shaping](../extractions/singer-principles-of-shaping.md) | INFERRED | Wireframes are too concrete |
| CLARIFY-SHAPING-C01 | CLARIFY | Level of abstraction (pair) | [Singer — Principles of Shaping](../extractions/singer-principles-of-shaping.md) | DIRECT | Wireframes/Words/Case study |
| CLARIFY-SHAPING-D01 | CLARIFY | CSV export shaped (derived) | [Singer — Principles of Shaping](../extractions/singer-principles-of-shaping.md) | DERIVED | — |
| CLARIFY-SHAPING-D02 | CLARIFY | Pixel-perfect modal (derived) | [Singer — Principles of Shaping](../extractions/singer-principles-of-shaping.md) | DERIVED | — |
| CLARIFY-SHAPING-N01 | CLARIFY | Wireframe hand-off (negative) | [Singer — Principles of Shaping](../extractions/singer-principles-of-shaping.md) | DIRECT | Wireframes are too concrete |
| CLARIFY-SHAPING-N02 | CLARIFY | "Build a calendar view" (negative) | [Singer — Principles of Shaping](../extractions/singer-principles-of-shaping.md) | DIRECT | Words are too abstract |
| CLARIFY-SHAPING-N03 | CLARIFY | Full-calendar complexity list (negative) | [Singer — Principles of Shaping](../extractions/singer-principles-of-shaping.md) | DIRECT | Case study |
| CLARIFY-SHAPING-P01 | CLARIFY | Dot Grid (positive) | [Singer — Principles of Shaping](../extractions/singer-principles-of-shaping.md) | DIRECT | Case study |
| CLARIFY-SHAPING-Q01 | CLARIFY | Solve / matter / success (question) | [Singer — Principles of Shaping](../extractions/singer-principles-of-shaping.md) | DIRECT | Who shapes |
| CLARIFY-SHAPING-Q02 | CLARIFY | Who affected / opportunity cost (question) | [Singer — Principles of Shaping](../extractions/singer-principles-of-shaping.md) | DIRECT | Who shapes |
| CLARIFY-SHAPING-Q03 | CLARIFY | What's in and out (question) | [Singer — Principles of Shaping](../extractions/singer-principles-of-shaping.md) | INFERRED | Case study |
| CLARIFY-SHAPING-Q05 | CLARIFY | Name vs spec vs shaped (question) | [Singer — Principles of Shaping](../extractions/singer-principles-of-shaping.md) | DERIVED | — |
| CLARIFY-SYN-D01 | CLARIFY | Form validation as GWT examples (derived example) | [synthesis/clarify.md](clarify.md) | DERIVED | — |
| CLARIFY-SYN-D02 | CLARIFY | API response change incl. unchanged fields (derived example) | [synthesis/clarify.md](clarify.md) | DERIVED | — |
| SLICE-BOUND-04 | SLICE | Too big → narrow, then carve (rule) | [Singer — Set Boundaries](../extractions/singer-set-boundaries.md) | DIRECT | Setting the appetite |
| SLICE-BOUND-13 | SLICE | Grab-bags / 2.0 (rule) | [Singer — Set Boundaries](../extractions/singer-set-boundaries.md) | DIRECT | Watch out for grab-bags |
| SLICE-BOUND-18 | SLICE | Narrow then carve (gate) | [Singer — Set Boundaries](../extractions/singer-set-boundaries.md) | DIRECT | Setting the appetite |
| SLICE-BOUND-20 | SLICE | Reframe/split grab-bag (gate) | [Singer — Set Boundaries](../extractions/singer-set-boundaries.md) | DIRECT | Watch out for grab-bags |
| SLICE-BOUND-C02 | SLICE | Grab-bag vs problem-driven (pair) | [Singer — Set Boundaries](../extractions/singer-set-boundaries.md) | DIRECT | Watch out for grab-bags |
| SLICE-BOUND-N01 | SLICE | Files 2.0 (negative) | [Singer — Set Boundaries](../extractions/singer-set-boundaries.md) | DIRECT | Watch out for grab-bags |
| SLICE-BOUND-P03 | SLICE | Files 2.0 recovery by split (positive) | [Singer — Set Boundaries](../extractions/singer-set-boundaries.md) | DIRECT | Watch out for grab-bags |
| SLICE-BOUND-Q04 | SLICE | What's not working / what stays (question) | [Singer — Set Boundaries](../extractions/singer-set-boundaries.md) | DIRECT | Watch out for grab-bags |
| SLICE-HANDOVER-06 | SLICE | Up-front tasks = paper shredder (rule) | [Singer — Hand Over Responsibility](../extractions/singer-shapeup-building-chapters.md) | DIRECT | Hand Over Responsibility / Assign projects, not tasks |
| SLICE-HILL-08 | SLICE | Refactor stuck scopes (rule) | [Singer — Show Progress](../extractions/singer-shapeup-building-chapters.md) | DIRECT | Show Progress / Prompts to refactor the scopes |
| SLICE-HILL-11 | SLICE | Split mis-drawn scope (gate) | [Singer — Show Progress](../extractions/singer-shapeup-building-chapters.md) | DIRECT | Show Progress / Prompts to refactor the scopes |
| SLICE-HILL-P04 | SLICE | Split "Notify" (positive) | [Singer — Show Progress](../extractions/singer-shapeup-building-chapters.md) | DIRECT | Show Progress / Prompts to refactor the scopes |
| SLICE-INDEP-01 | SLICE | Independent = understood/tested alone (rule) | [Wake — Independent Stories](../extractions/wake-independent-stories.md) | DIRECT | Intro |
| SLICE-INDEP-02 | SLICE | Pursue most valuable today (rule) | [Wake — Independent Stories](../extractions/wake-independent-stories.md) | DIRECT | Intro |
| SLICE-INDEP-03 | SLICE | Overlap/order/containment (rule) | [Wake — Independent Stories](../extractions/wake-independent-stories.md) | DIRECT | Intro |
| SLICE-INDEP-04 | SLICE | Overlap most painful (rule) | [Wake — Independent Stories](../extractions/wake-independent-stories.md) | DIRECT | Overlap |
| SLICE-INDEP-05 | SLICE | "and" in title → suspicion (rule) | [Wake — Independent Stories](../extractions/wake-independent-stories.md) | DIRECT | Overlap |
| SLICE-INDEP-06 | SLICE | Order deps mostly harmless (rule) | [Wake — Independent Stories](../extractions/wake-independent-stories.md) | DIRECT | Order |
| SLICE-INDEP-07 | SLICE | Hard-code prerequisite (skinniest) (rule) | [Wake — Independent Stories](../extractions/wake-independent-stories.md) | DIRECT | Order |
| SLICE-INDEP-08 | SLICE | Hierarchy describes, doesn't schedule (rule) | [Wake — Independent Stories](../extractions/wake-independent-stories.md) | DIRECT | Containment |
| SLICE-INDEP-09 | SLICE | Minimal whole system first (rule) | [Wake — Independent Stories](../extractions/wake-independent-stories.md) | DIRECT | Containment |
| SLICE-INDEP-10 | SLICE | Independence → minimal implementation (rule) | [Wake — Independent Stories](../extractions/wake-independent-stories.md) | DIRECT | Bottom Line |
| SLICE-INDEP-11 | SLICE | Prerequisite → stub candidate (rule) | [Wake — Independent Stories](../extractions/wake-independent-stories.md) | INFERRED | Order |
| SLICE-INDEP-12 | SLICE | Overlap → repartition (gate) | [Wake — Independent Stories](../extractions/wake-independent-stories.md) | DIRECT | Overlap |
| SLICE-INDEP-13 | SLICE | Prerequisite → hard-code first? (gate) | [Wake — Independent Stories](../extractions/wake-independent-stories.md) | DIRECT | Order |
| SLICE-INDEP-14 | SLICE | No depth-first scheduling (gate) | [Wake — Independent Stories](../extractions/wake-independent-stories.md) | DIRECT | Containment |
| SLICE-INDEP-C01 | SLICE | Overlap vs partition (pair) | [Wake — Independent Stories](../extractions/wake-independent-stories.md) | DIRECT | Overlap |
| SLICE-INDEP-C02 | SLICE | Stub vs build prerequisite (pair) | [Wake — Independent Stories](../extractions/wake-independent-stories.md) | DIRECT | Order |
| SLICE-INDEP-C03 | SLICE | Minimal whole vs depth-first (pair) | [Wake — Independent Stories](../extractions/wake-independent-stories.md) | DIRECT | Containment |
| SLICE-INDEP-D01 | SLICE | Saved/shared report views (derived example) | [Wake — Independent Stories](../extractions/wake-independent-stories.md) | DERIVED | — |
| SLICE-INDEP-N01 | SLICE | Overlapping "and" stories (negative) | [Wake — Independent Stories](../extractions/wake-independent-stories.md) | DIRECT | Overlap |
| SLICE-INDEP-N02 | SLICE | Depth-first hierarchy schedule (negative) | [Wake — Independent Stories](../extractions/wake-independent-stories.md) | DIRECT | Containment |
| SLICE-INDEP-N03 | SLICE | Abstract overlap set (negative) | [Wake — Independent Stories](../extractions/wake-independent-stories.md) | DIRECT | Overlap |
| SLICE-INDEP-P01 | SLICE | Repartitioned email stories (positive) | [Wake — Independent Stories](../extractions/wake-independent-stories.md) | DIRECT | Overlap |
| SLICE-INDEP-P02 | SLICE | Hard-coded accounts (positive) | [Wake — Independent Stories](../extractions/wake-independent-stories.md) | DIRECT | Order |
| SLICE-INDEP-Q01 | SLICE | Smallest covering set (question) | [Wake — Independent Stories](../extractions/wake-independent-stories.md) | DIRECT | Overlap |
| SLICE-INDEP-Q02 | SLICE | "and"/overlap? (question) | [Wake — Independent Stories](../extractions/wake-independent-stories.md) | INFERRED | Overlap |
| SLICE-INDEP-Q03 | SLICE | Dependency hard-codable? (question) | [Wake — Independent Stories](../extractions/wake-independent-stories.md) | INFERRED | Order |
| SLICE-INDEP-Q05 | SLICE | Depth-first vs minimal whole? (question) | [Wake — Independent Stories](../extractions/wake-independent-stories.md) | INFERRED | Containment |
| SLICE-INVEST-01 | SLICE | INVEST criteria (rule) | [Wake — INVEST/SMART](../extractions/wake-invest.md) | DIRECT | Intro |
| SLICE-INVEST-02 | SLICE | Independent (no overlap, any order) (rule) | [Wake — INVEST/SMART](../extractions/wake-invest.md) | DIRECT | Independent |
| SLICE-INVEST-03 | SLICE | Valuable to customer (rule) | [Wake — INVEST/SMART](../extractions/wake-invest.md) | DIRECT | Valuable |
| SLICE-INVEST-04 | SLICE | Slice vertically through layers (rule) | [Wake — INVEST/SMART](../extractions/wake-invest.md) | DIRECT | Valuable |
| SLICE-INVEST-05 | SLICE | Small; ">1 month" = not understood (rule) | [Wake — INVEST/SMART](../extractions/wake-invest.md) | DIRECT | Small |
| SLICE-INVEST-06 | SLICE | SMART tasks (rule) | [Wake — INVEST/SMART](../extractions/wake-invest.md) | DIRECT | SMART Tasks |
| SLICE-INVEST-07 | SLICE | Specific tasks add up to story (rule) | [Wake — INVEST/SMART](../extractions/wake-invest.md) | DIRECT | Specific |
| SLICE-INVEST-08 | SLICE | Relevant to story (rule) | [Wake — INVEST/SMART](../extractions/wake-invest.md) | DIRECT | Relevant |
| SLICE-INVEST-09 | SLICE | Single-layer story not a slice (rule) | [Wake — INVEST/SMART](../extractions/wake-invest.md) | INFERRED | Valuable |
| SLICE-INVEST-10 | SLICE | Too big → split (gate) | [Wake — INVEST/SMART](../extractions/wake-invest.md) | DIRECT | Small |
| SLICE-INVEST-11 | SLICE | Single layer → re-slice (gate) | [Wake — INVEST/SMART](../extractions/wake-invest.md) | DIRECT | Valuable |
| SLICE-INVEST-C01 | SLICE | Vertical vs layer (pair) | [Wake — INVEST/SMART](../extractions/wake-invest.md) | DIRECT | Valuable |
| SLICE-INVEST-D01 | SLICE | Phone field slice (derived example) | [Wake — INVEST/SMART](../extractions/wake-invest.md) | DERIVED | — |
| SLICE-INVEST-N01 | SLICE | One layer at a time (negative) | [Wake — INVEST/SMART](../extractions/wake-invest.md) | DIRECT | Valuable |
| SLICE-INVEST-N03 | SLICE | "More than a month" (negative) | [Wake — INVEST/SMART](../extractions/wake-invest.md) | DIRECT | Small |
| SLICE-INVEST-P01 | SLICE | Vertical cake slice (positive) | [Wake — INVEST/SMART](../extractions/wake-invest.md) | DIRECT | Valuable |
| SLICE-INVEST-Q02 | SLICE | Cuts through every layer? (question) | [Wake — INVEST/SMART](../extractions/wake-invest.md) | INFERRED | Valuable |
| SLICE-INVEST-Q03 | SLICE | More than a month? (question) | [Wake — INVEST/SMART](../extractions/wake-invest.md) | INFERRED | Small |
| SLICE-INVEST-Q07 | SLICE | Task justified by story? (question) | [Wake — INVEST/SMART](../extractions/wake-invest.md) | INFERRED | Relevant |
| SLICE-ONEPIECE-01 | SLICE | No 11th-hour master plan (rule) | [Singer — Get One Piece Done](../extractions/singer-shapeup-building-chapters.md) | DIRECT | Get One Piece Done / Intro |
| SLICE-ONEPIECE-02 | SLICE | Integrate vertically (rule) | [Singer — Get One Piece Done](../extractions/singer-shapeup-building-chapters.md) | DIRECT | Get One Piece Done / Integrate one slice |
| SLICE-ONEPIECE-05 | SLICE | Start in the middle (rule) | [Singer — Get One Piece Done](../extractions/singer-shapeup-building-chapters.md) | DIRECT | Get One Piece Done / Start in the middle |
| SLICE-ONEPIECE-06 | SLICE | Core / small / novel (rule) | [Singer — Get One Piece Done](../extractions/singer-shapeup-building-chapters.md) | DIRECT | Get One Piece Done / Start in the middle |
| SLICE-ONEPIECE-07 | SLICE | Prefer novel (gate) | [Singer — Get One Piece Done](../extractions/singer-shapeup-building-chapters.md) | DIRECT | Get One Piece Done / Start in the middle |
| SLICE-ONEPIECE-C01 | SLICE | Vertical vs horizontal (pair) | [Singer — Get One Piece Done](../extractions/singer-shapeup-building-chapters.md) | DIRECT | Get One Piece Done / Integrate one slice |
| SLICE-ONEPIECE-C02 | SLICE | Core/novel vs peripheral (pair) | [Singer — Get One Piece Done](../extractions/singer-shapeup-building-chapters.md) | DIRECT | Get One Piece Done / Start in the middle |
| SLICE-ONEPIECE-D02 | SLICE | Favorite action slice (derived) | [Singer — Get One Piece Done](../extractions/singer-shapeup-building-chapters.md) | DERIVED | — |
| SLICE-ONEPIECE-N01 | SLICE | Horizontal layers (negative) | [Singer — Get One Piece Done](../extractions/singer-shapeup-building-chapters.md) | DIRECT | Get One Piece Done / Integrate one slice |
| SLICE-ONEPIECE-N02 | SLICE | Peripheral/familiar first (negative) | [Singer — Get One Piece Done](../extractions/singer-shapeup-building-chapters.md) | DIRECT | Get One Piece Done / Start in the middle |
| SLICE-ONEPIECE-P01 | SLICE | Visibility toggle first (positive) | [Singer — Get One Piece Done](../extractions/singer-shapeup-building-chapters.md) | DIRECT | Get One Piece Done / Case study |
| SLICE-ONEPIECE-Q01 | SLICE | Core/small/novel? (question) | [Singer — Get One Piece Done](../extractions/singer-shapeup-building-chapters.md) | INFERRED | Get One Piece Done / Start in the middle |
| SLICE-RISK-11 | SLICE | Declare out of bounds (rule) | [Singer — Risks and Rabbit Holes](../extractions/singer-risks-and-rabbit-holes.md) | DIRECT | Declare out of bounds |
| SLICE-RISK-12 | SLICE | Cut back (rule) | [Singer — Risks and Rabbit Holes](../extractions/singer-risks-and-rabbit-holes.md) | DIRECT | Cut back |
| SLICE-RISK-P02 | SLICE | Group notify out of bounds (positive) | [Singer — Risks and Rabbit Holes](../extractions/singer-risks-and-rabbit-holes.md) | DIRECT | Declare out of bounds |
| SLICE-RISK-P03 | SLICE | Color coding cut (positive) | [Singer — Risks and Rabbit Holes](../extractions/singer-risks-and-rabbit-holes.md) | DIRECT | Cut back |
| SLICE-RISK-Q08 | SLICE | What's not supported (question) | [Singer — Risks and Rabbit Holes](../extractions/singer-risks-and-rabbit-holes.md) | INFERRED | Declare out of bounds |
| SLICE-RISK-Q09 | SLICE | Necessary? (question) | [Singer — Risks and Rabbit Holes](../extractions/singer-risks-and-rabbit-holes.md) | INFERRED | Cut back |
| SLICE-SPLIT-01 | SLICE | Separate high from low value (rule) | [Wake — Twenty Ways to Split](../extractions/wake-twenty-ways-to-split.md) | DIRECT | Intro |
| SLICE-SPLIT-02 | SLICE | Combine too-small stories (rule) | [Wake — Twenty Ways to Split](../extractions/wake-twenty-ways-to-split.md) | DIRECT | Intro |
| SLICE-SPLIT-03 | SLICE | Minimal end-to-end first (rule) | [Wake — Twenty Ways to Split](../extractions/wake-twenty-ways-to-split.md) | DIRECT | Intro |
| SLICE-SPLIT-04 | SLICE | Four split families (rule) | [Wake — Twenty Ways to Split](../extractions/wake-twenty-ways-to-split.md) | DIRECT | The splits |
| SLICE-SPLIT-05 | SLICE | Manual before automated (rule) | [Wake — Twenty Ways to Split](../extractions/wake-twenty-ways-to-split.md) | DIRECT | Big Picture |
| SLICE-SPLIT-06 | SLICE | Buy vs build by fit (rule) | [Wake — Twenty Ways to Split](../extractions/wake-twenty-ways-to-split.md) | DIRECT | Big Picture |
| SLICE-SPLIT-07 | SLICE | UX splits (rule) | [Wake — Twenty Ways to Split](../extractions/wake-twenty-ways-to-split.md) | DIRECT | User Experience |
| SLICE-SPLIT-08 | SLICE | Ilities splits (rule) | [Wake — Twenty Ways to Split](../extractions/wake-twenty-ways-to-split.md) | DIRECT | "Ilities" |
| SLICE-SPLIT-09 | SLICE | Feature splits (rule) | [Wake — Twenty Ways to Split](../extractions/wake-twenty-ways-to-split.md) | DIRECT | Features |
| SLICE-SPLIT-10 | SLICE | Main flow most valuable (rule) | [Wake — Twenty Ways to Split](../extractions/wake-twenty-ways-to-split.md) | DIRECT | Features |
| SLICE-SPLIT-11 | SLICE | Connector words (rule) | [Wake — Twenty Ways to Split](../extractions/wake-twenty-ways-to-split.md) | DIRECT | Features |
| SLICE-SPLIT-12 | SLICE | Reassemble; narrow high-value path (rule) | [Wake — Twenty Ways to Split](../extractions/wake-twenty-ways-to-split.md) | DIRECT | Summary |
| SLICE-SPLIT-13 | SLICE | Easier variant first, harder later (rule) | [Wake — Twenty Ways to Split](../extractions/wake-twenty-ways-to-split.md) | INFERRED | table |
| SLICE-SPLIT-14 | SLICE | Ignore errors ≠ hide failures (rule) | [Wake — Twenty Ways to Split](../extractions/wake-twenty-ways-to-split.md) | INFERRED | "Ilities" |
| SLICE-SPLIT-15 | SLICE | Connectors → split (gate) | [Wake — Twenty Ways to Split](../extractions/wake-twenty-ways-to-split.md) | DIRECT | Features |
| SLICE-SPLIT-16 | SLICE | Base case first (gate) | [Wake — Twenty Ways to Split](../extractions/wake-twenty-ways-to-split.md) | DIRECT | Features |
| SLICE-SPLIT-17 | SLICE | Too small → combine (gate) | [Wake — Twenty Ways to Split](../extractions/wake-twenty-ways-to-split.md) | DIRECT | Intro |
| SLICE-SPLIT-18 | SLICE | Check reassembly (gate) | [Wake — Twenty Ways to Split](../extractions/wake-twenty-ways-to-split.md) | DIRECT | Summary |
| SLICE-SPLIT-C03 | SLICE | Manual vs automated (pair) | [Wake — Twenty Ways to Split](../extractions/wake-twenty-ways-to-split.md) | DIRECT | Big Picture |
| SLICE-SPLIT-C04 | SLICE | Main vs alternate flows (pair) | [Wake — Twenty Ways to Split](../extractions/wake-twenty-ways-to-split.md) | DIRECT | Features |
| SLICE-SPLIT-C05 | SLICE | 0/1/many, base/general, levels (pair) | [Wake — Twenty Ways to Split](../extractions/wake-twenty-ways-to-split.md) | DIRECT | Features |
| SLICE-SPLIT-C06 | SLICE | Split vs full condition (pair) | [Wake — Twenty Ways to Split](../extractions/wake-twenty-ways-to-split.md) | DIRECT | Features |
| SLICE-SPLIT-C07 | SLICE | Transient/static/single vs full (pair) | [Wake — Twenty Ways to Split](../extractions/wake-twenty-ways-to-split.md) | DIRECT | Ilities; UX |
| SLICE-SPLIT-C08 | SLICE | Minimal end-to-end vs complete-first (pair) | [Wake — Twenty Ways to Split](../extractions/wake-twenty-ways-to-split.md) | DIRECT/DERIVED | Intro |
| SLICE-SPLIT-D01 | SLICE | Signup form validation (derived example) | [Wake — Twenty Ways to Split](../extractions/wake-twenty-ways-to-split.md) | DERIVED | — |
| SLICE-SPLIT-D03 | SLICE | Bulk-archive endpoint (derived example) | [Wake — Twenty Ways to Split](../extractions/wake-twenty-ways-to-split.md) | DERIVED | — |
| SLICE-SPLIT-N01 | SLICE | Recovery before trivial transaction (negative) | [Wake — Twenty Ways to Split](../extractions/wake-twenty-ways-to-split.md) | DIRECT | Features |
| SLICE-SPLIT-N02 | SLICE | Swallowing exceptions (negative) | [Wake — Twenty Ways to Split](../extractions/wake-twenty-ways-to-split.md) | DIRECT | "Ilities" |
| SLICE-SPLIT-N03 | SLICE | Ill-fitting off-the-shelf (negative) | [Wake — Twenty Ways to Split](../extractions/wake-twenty-ways-to-split.md) | DIRECT | Big Picture |
| SLICE-SPLIT-N04 | SLICE | Splitting without reassembly (negative) | [Wake — Twenty Ways to Split](../extractions/wake-twenty-ways-to-split.md) | DIRECT | Summary |
| SLICE-SPLIT-P01 | SLICE | Manual credit check (positive) | [Wake — Twenty Ways to Split](../extractions/wake-twenty-ways-to-split.md) | DIRECT | Big Picture |
| SLICE-SPLIT-P02 | SLICE | API-only connection test (positive) | [Wake — Twenty Ways to Split](../extractions/wake-twenty-ways-to-split.md) | DIRECT | User Experience |
| SLICE-SPLIT-P03 | SLICE | Low→high fidelity camera (positive) | [Wake — Twenty Ways to Split](../extractions/wake-twenty-ways-to-split.md) | DIRECT | "Ilities" |
| SLICE-SPLIT-Q02 | SLICE | Main flow first? (question) | [Wake — Twenty Ways to Split](../extractions/wake-twenty-ways-to-split.md) | INFERRED | Features |
| SLICE-SPLIT-Q03 | SLICE | 0/1, one level, base case? (question) | [Wake — Twenty Ways to Split](../extractions/wake-twenty-ways-to-split.md) | INFERRED | Features |
| SLICE-SPLIT-Q04 | SLICE | Connector words? (question) | [Wake — Twenty Ways to Split](../extractions/wake-twenty-ways-to-split.md) | INFERRED | Features |
| SLICE-SPLIT-Q05 | SLICE | Manual/generic/API-only/static first? (question) | [Wake — Twenty Ways to Split](../extractions/wake-twenty-ways-to-split.md) | INFERRED | table |
| SLICE-SPLIT-Q06 | SLICE | Narrow high-value path? (question) | [Wake — Twenty Ways to Split](../extractions/wake-twenty-ways-to-split.md) | INFERRED | Summary |
| SLICE-SPLIT-Q07 | SLICE | Do slices reassemble? (question) | [Wake — Twenty Ways to Split](../extractions/wake-twenty-ways-to-split.md) | INFERRED | Summary |
| SLICE-SYN-D01 | SLICE | DB field + behavior vertical slice (derived example) | [synthesis/slice.md](slice.md) | DERIVED | — |
| SLICE-SYN-D02 | SLICE | Delete-my-comment with existing session (derived example) | [synthesis/slice.md](slice.md) | DERIVED | — |
| SLICE-SYN-D03 | SLICE | Component: one / zero / many (derived example) | [synthesis/slice.md](slice.md) | DERIVED | — |
| DERISK-HILL-03 | DERISK | Uphill / downhill (rule) | [Singer — Show Progress](../extractions/singer-shapeup-building-chapters.md) | DIRECT | Show Progress / Work is like a hill |
| DERISK-HILL-05 | DERISK | Hands not head (thirds) (rule) | [Singer — Show Progress](../extractions/singer-shapeup-building-chapters.md) | DIRECT | Show Progress / Build your way uphill |
| DERISK-HILL-06 | DERISK | Scariest first (rule) | [Singer — Show Progress](../extractions/singer-shapeup-building-chapters.md) | DIRECT | Show Progress / Solve in the right sequence |
| DERISK-HILL-07 | DERISK | Stuck dot = raised hand (rule) | [Singer — Show Progress](../extractions/singer-shapeup-building-chapters.md) | DIRECT | Show Progress / Nobody says “I don't know” |
| DERISK-HILL-10 | DERISK | Not solved until built (gate) | [Singer — Show Progress](../extractions/singer-shapeup-building-chapters.md) | DIRECT | Show Progress / Build your way uphill |
| DERISK-HILL-C03 | DERISK | Head vs hands (pair) | [Singer — Show Progress](../extractions/singer-shapeup-building-chapters.md) | DIRECT | Show Progress / Build your way uphill |
| DERISK-HILL-D03 | DERISK | Shipping-rates API (derived) | [Singer — Show Progress](../extractions/singer-shapeup-building-chapters.md) | DERIVED | — |
| DERISK-HILL-N03 | DERISK | Uphill in the head (negative) | [Singer — Show Progress](../extractions/singer-shapeup-building-chapters.md) | DIRECT | Show Progress / Build your way uphill |
| DERISK-HILL-P03 | DERISK | Geocoding before email (positive) | [Singer — Show Progress](../extractions/singer-shapeup-building-chapters.md) | DIRECT | Show Progress / Solve in the right sequence |
| DERISK-HILL-Q02 | DERISK | Out of time: which is harder? (question) | [Singer — Show Progress](../extractions/singer-shapeup-building-chapters.md) | DIRECT | Show Progress / Solve in the right sequence |
| DERISK-HILL-Q03 | DERISK | What's the unknown holding it? (question) | [Singer — Show Progress](../extractions/singer-shapeup-building-chapters.md) | DIRECT | Show Progress / Status without asking |
| DERISK-HILL-Q04 | DERISK | Validated by building? (question) | [Singer — Show Progress](../extractions/singer-shapeup-building-chapters.md) | INFERRED | Show Progress / Build your way uphill |
| DERISK-INDEP-01 | DERISK | Order by value and risk (rule) | [Wake — Independent Stories](../extractions/wake-independent-stories.md) | DIRECT | Order |
| DERISK-INDEP-02 | DERISK | First slice exposes biggest risk (rule) | [Wake — Independent Stories](../extractions/wake-independent-stories.md) | INFERRED | Order |
| DERISK-INDEP-D02 | DERISK | Delete-my-comment auth stub (derived example) | [Wake — Independent Stories](../extractions/wake-independent-stories.md) | DERIVED | — |
| DERISK-INDEP-Q04 | DERISK | Biggest risk/value first? (question) | [Wake — Independent Stories](../extractions/wake-independent-stories.md) | INFERRED | Order |
| DERISK-INVEST-01 | DERISK | Time-boxed spike to enable estimate (rule) | [Wake — INVEST/SMART](../extractions/wake-invest.md) | DIRECT | Estimable |
| DERISK-INVEST-02 | DERISK | Can't estimate → spike (gate) | [Wake — INVEST/SMART](../extractions/wake-invest.md) | DIRECT | Estimable |
| DERISK-INVEST-P02 | DERISK | Spike to enable estimate (positive) | [Wake — INVEST/SMART](../extractions/wake-invest.md) | DIRECT | Estimable |
| DERISK-RISK-01 | DERISK | One hole derails (rule) | [Singer — Risks and Rabbit Holes](../extractions/singer-risks-and-rabbit-holes.md) | DIRECT | Intro |
| DERISK-RISK-02 | DERISK | Some problems have no solution (rule) | [Singer — Risks and Rabbit Holes](../extractions/singer-risks-and-rabbit-holes.md) | DIRECT | Intro |
| DERISK-RISK-03 | DERISK | Eliminate findable pitfalls (rule) | [Singer — Risks and Rabbit Holes](../extractions/singer-risks-and-rabbit-holes.md) | DIRECT | Intro |
| DERISK-RISK-04 | DERISK | Thin vs fat tail (rule) | [Singer — Risks and Rabbit Holes](../extractions/singer-risks-and-rabbit-holes.md) | DIRECT | Different categories of risk |
| DERISK-RISK-05 | DERISK | Three rabbit-hole categories (rule) | [Singer — Risks and Rabbit Holes](../extractions/singer-risks-and-rabbit-holes.md) | DIRECT | Different categories of risk |
| DERISK-RISK-06 | DERISK | Independent well-understood parts (rule) | [Singer — Risks and Rabbit Holes](../extractions/singer-risks-and-rabbit-holes.md) | DIRECT | Different categories of risk |
| DERISK-RISK-07 | DERISK | Slow down, look critically (rule) | [Singer — Risks and Rabbit Holes](../extractions/singer-risks-and-rabbit-holes.md) | DIRECT | Look for rabbit holes |
| DERISK-RISK-08 | DERISK | Slow-motion walk-through (rule) | [Singer — Risks and Rabbit Holes](../extractions/singer-risks-and-rabbit-holes.md) | DIRECT | Look for rabbit holes |
| DERISK-RISK-09 | DERISK | Viability questions (rule) | [Singer — Risks and Rabbit Holes](../extractions/singer-risks-and-rabbit-holes.md) | DIRECT | Look for rabbit holes |
| DERISK-RISK-10 | DERISK | Patch holes (rule) | [Singer — Risks and Rabbit Holes](../extractions/singer-risks-and-rabbit-holes.md) | DIRECT | Case study: Patching a hole |
| DERISK-RISK-13 | DERISK | Possible within appetite (rule) | [Singer — Risks and Rabbit Holes](../extractions/singer-risks-and-rabbit-holes.md) | DIRECT | Present to technical experts |
| DERISK-RISK-14 | DERISK | Hunt for time bombs (rule) | [Singer — Risks and Rabbit Holes](../extractions/singer-risks-and-rabbit-holes.md) | DIRECT | Present to technical experts |
| DERISK-RISK-15 | DERISK | Validate or reshape (rule) | [Singer — Risks and Rabbit Holes](../extractions/singer-risks-and-rabbit-holes.md) | DIRECT | Present to technical experts |
| DERISK-RISK-16 | DERISK | Risk relative to time box (rule) | [Singer — Risks and Rabbit Holes](../extractions/singer-risks-and-rabbit-holes.md) | INFERRED | Intro; categories |
| DERISK-RISK-17 | DERISK | Polish-for-risk trade (rule) | [Singer — Risks and Rabbit Holes](../extractions/singer-risks-and-rabbit-holes.md) | INFERRED | Case study |
| DERISK-RISK-18 | DERISK | Assumed solution = hole (gate) | [Singer — Risks and Rabbit Holes](../extractions/singer-risks-and-rabbit-holes.md) | DIRECT | Look for rabbit holes; Intro |
| DERISK-RISK-19 | DERISK | Settle hard decisions (gate) | [Singer — Risks and Rabbit Holes](../extractions/singer-risks-and-rabbit-holes.md) | DIRECT | Look for rabbit holes |
| DERISK-RISK-20 | DERISK | Problems → reshape (gate) | [Singer — Risks and Rabbit Holes](../extractions/singer-risks-and-rabbit-holes.md) | DIRECT | Present to technical experts |
| DERISK-RISK-C01 | DERISK | Possible vs possible-in-appetite (pair) | [Singer — Risks and Rabbit Holes](../extractions/singer-risks-and-rabbit-holes.md) | DIRECT | Present to technical experts |
| DERISK-RISK-C02 | DERISK | Thin vs fat tail (pair) | [Singer — Risks and Rabbit Holes](../extractions/singer-risks-and-rabbit-holes.md) | DIRECT | Different categories of risk |
| DERISK-RISK-C03 | DERISK | Patch vs leave open (pair) | [Singer — Risks and Rabbit Holes](../extractions/singer-risks-and-rabbit-holes.md) | DIRECT | Case study |
| DERISK-RISK-C04 | DERISK | Validated vs assumed solution (pair) | [Singer — Risks and Rabbit Holes](../extractions/singer-risks-and-rabbit-holes.md) | DIRECT/INFERRED | Intro |
| DERISK-RISK-D01 | DERISK | Payments API unknown (derived) | [Singer — Risks and Rabbit Holes](../extractions/singer-risks-and-rabbit-holes.md) | DERIVED | — |
| DERISK-RISK-D02 | DERISK | DB field interdependencies (derived) | [Singer — Risks and Rabbit Holes](../extractions/singer-risks-and-rabbit-holes.md) | DERIVED | — |
| DERISK-RISK-D03 | DERISK | Browser bug fat tail (derived) | [Singer — Risks and Rabbit Holes](../extractions/singer-risks-and-rabbit-holes.md) | DERIVED | — |
| DERISK-RISK-N01 | DERISK | Client-projects redesign abandoned (negative) | [Singer — Risks and Rabbit Holes](../extractions/singer-risks-and-rabbit-holes.md) | DIRECT | Intro |
| DERISK-RISK-N02 | DERISK | Knot pushed to team (negative) | [Singer — Risks and Rabbit Holes](../extractions/singer-risks-and-rabbit-holes.md) | DIRECT | Case study |
| DERISK-RISK-N03 | DERISK | "Is this possible?" (negative) | [Singer — Risks and Rabbit Holes](../extractions/singer-risks-and-rabbit-holes.md) | DIRECT | Present to technical experts |
| DERISK-RISK-P01 | DERISK | Completed to-dos patch (positive) | [Singer — Risks and Rabbit Holes](../extractions/singer-risks-and-rabbit-holes.md) | DIRECT | Case study: Patching a hole |
| DERISK-RISK-Q01 | DERISK | New technical work? (question) | [Singer — Risks and Rabbit Holes](../extractions/singer-risks-and-rabbit-holes.md) | DIRECT | Look for rabbit holes |
| DERISK-RISK-Q02 | DERISK | Fit assumptions? (question) | [Singer — Risks and Rabbit Holes](../extractions/singer-risks-and-rabbit-holes.md) | DIRECT | Look for rabbit holes |
| DERISK-RISK-Q03 | DERISK | Assumed design solution? (question) | [Singer — Risks and Rabbit Holes](../extractions/singer-risks-and-rabbit-holes.md) | DIRECT | Look for rabbit holes |
| DERISK-RISK-Q04 | DERISK | Hard decision to settle? (question) | [Singer — Risks and Rabbit Holes](../extractions/singer-risks-and-rabbit-holes.md) | DIRECT | Look for rabbit holes |
| DERISK-RISK-Q05 | DERISK | Missed anything / unfair assumptions (question) | [Singer — Risks and Rabbit Holes](../extractions/singer-risks-and-rabbit-holes.md) | DIRECT | Look for rabbit holes |
| DERISK-RISK-Q06 | DERISK | Slow-motion path (question) | [Singer — Risks and Rabbit Holes](../extractions/singer-risks-and-rabbit-holes.md) | DIRECT | Look for rabbit holes |
| DERISK-RISK-Q07 | DERISK | Possible within appetite (question) | [Singer — Risks and Rabbit Holes](../extractions/singer-risks-and-rabbit-holes.md) | DIRECT | Present to technical experts |
| DERISK-SHAPING-06 | DERISK | Solved ≠ tasked out (rule) | [Singer — Principles of Shaping](../extractions/singer-principles-of-shaping.md) | DIRECT | Property 2 |
| DERISK-SHAPING-08 | DERISK | Unshaped work can't be scheduled (rule) | [Singer — Principles of Shaping](../extractions/singer-principles-of-shaping.md) | DIRECT | Two tracks |
| DERISK-SHAPING-10 | DERISK | Technical literacy to judge easy/hard (rule) | [Singer — Principles of Shaping](../extractions/singer-principles-of-shaping.md) | DIRECT | Who shapes |
| DERISK-SHAPING-11 | DERISK | Readiness is property of the work (rule) | [Singer — Principles of Shaping](../extractions/singer-principles-of-shaping.md) | INFERRED | Properties; Two tracks |
| DERISK-SHAPING-13 | DERISK | Rough+solved+bounded gate (gate) | [Singer — Principles of Shaping](../extractions/singer-principles-of-shaping.md) | INFERRED | Properties |
| DERISK-SHAPING-Q04 | DERISK | Elements connected, open questions (question) | [Singer — Principles of Shaping](../extractions/singer-principles-of-shaping.md) | INFERRED | Property 2 |
| DERISK-SPLIT-01 | DERISK | Research vs action (rule) | [Wake — Twenty Ways to Split](../extractions/wake-twenty-ways-to-split.md) | DIRECT | Big Picture |
| DERISK-SPLIT-02 | DERISK | Spike: hour/day, rarely longer (rule) | [Wake — Twenty Ways to Split](../extractions/wake-twenty-ways-to-split.md) | DIRECT | Big Picture |
| DERISK-SPLIT-03 | DERISK | Spike ≠ implementation (rule) | [Wake — Twenty Ways to Split](../extractions/wake-twenty-ways-to-split.md) | INFERRED | Big Picture |
| DERISK-SPLIT-04 | DERISK | Too hard → research/spike (gate) | [Wake — Twenty Ways to Split](../extractions/wake-twenty-ways-to-split.md) | DIRECT | Big Picture |
| DERISK-SPLIT-C01 | DERISK | Research vs action (pair) | [Wake — Twenty Ways to Split](../extractions/wake-twenty-ways-to-split.md) | DIRECT | Big Picture |
| DERISK-SPLIT-C02 | DERISK | Spike vs implementation (pair) | [Wake — Twenty Ways to Split](../extractions/wake-twenty-ways-to-split.md) | DIRECT | Big Picture |
| DERISK-SPLIT-D02 | DERISK | Shipping-rates API spike (derived example) | [Wake — Twenty Ways to Split](../extractions/wake-twenty-ways-to-split.md) | DERIVED | — |
| DERISK-SPLIT-Q01 | DERISK | What spike would tell us? (question) | [Wake — Twenty Ways to Split](../extractions/wake-twenty-ways-to-split.md) | INFERRED | Big Picture |
| DERISK-SYN-D01 | DERISK | Shipping-rates API spike (derived example) | [synthesis/derisk.md](derisk.md) | DERIVED | — |
| DERISK-SYN-D02 | DERISK | Safari bug: reproduce/isolate first (derived example) | [synthesis/derisk.md](derisk.md) | DERIVED | — |
| DERISK-SYN-D03 | DERISK | Refactor with interdependency check (derived example) | [synthesis/derisk.md](derisk.md) | DERIVED | — |
| ESTIMATE-BOUND-05 | ESTIMATE | Appetite ≠ estimate (rule) | [Singer — Set Boundaries](../extractions/singer-set-boundaries.md) | DIRECT | Fixed time, variable scope |
| ESTIMATE-BOUND-15 | ESTIMATE | Don't substitute appetite/estimate (rule) | [Singer — Set Boundaries](../extractions/singer-set-boundaries.md) | INFERRED | Fixed time, variable scope |
| ESTIMATE-BOUND-C01 | ESTIMATE | Appetite vs estimate (pair) | [Singer — Set Boundaries](../extractions/singer-set-boundaries.md) | DIRECT | Fixed time, variable scope |
| ESTIMATE-EBS-01 | ESTIMATE | ≤16h tasks, measured in hours (rule) | [Spolsky — EBS](../extractions/spolsky-evidence-based-scheduling.md) | DIRECT | §1 |
| ESTIMATE-EBS-02 | ESTIMATE | Small tasks force design; familiar = estimable (rule) | [Spolsky — EBS](../extractions/spolsky-evidence-based-scheduling.md) | DIRECT | §1 |
| ESTIMATE-EBS-03 | ESTIMATE | Hand-wavy multi-week task = unthought steps (rule) | [Spolsky — EBS](../extractions/spolsky-evidence-based-scheduling.md) | DIRECT | §1 |
| ESTIMATE-EBS-04 | ESTIMATE | Perfect/bad/common estimator (rule) | [Spolsky — EBS](../extractions/spolsky-evidence-based-scheduling.md) | DIRECT | §2 |
| ESTIMATE-EBS-05 | ESTIMATE | Discard velocities > ~6 months (rule) | [Spolsky — EBS](../extractions/spolsky-evidence-based-scheduling.md) | DIRECT | §2 |
| ESTIMATE-EBS-06 | ESTIMATE | New estimator: pessimistic fake history until ~6 tasks (rule) | [Spolsky — EBS](../extractions/spolsky-evidence-based-scheduling.md) | DIRECT | §2 |
| ESTIMATE-EBS-07 | ESTIMATE | Monte Carlo, not summing (rule) | [Spolsky — EBS](../extractions/spolsky-evidence-based-scheduling.md) | DIRECT | §3 |
| ESTIMATE-EBS-08 | ESTIMATE | Distribution shape = confidence (rule) | [Spolsky — EBS](../extractions/spolsky-evidence-based-scheduling.md) | DIRECT | intro; §3 |
| ESTIMATE-EBS-09 | ESTIMATE | Only the implementer estimates (rule) | [Spolsky — EBS](../extractions/spolsky-evidence-based-scheduling.md) | DIRECT | While we're at it 1 |
| ESTIMATE-EBS-10 | ESTIMATE | Don't badger into short estimates (rule) | [Spolsky — EBS](../extractions/spolsky-evidence-based-scheduling.md) | DIRECT | While we're at it 3 |
| ESTIMATE-EBS-11 | ESTIMATE | n vs 4n (rule) | [Spolsky — EBS](../extractions/spolsky-evidence-based-scheduling.md) | DIRECT | While we're at it 3 |
| ESTIMATE-EBS-12 | ESTIMATE | Estimability = steps thought through (rule) | [Spolsky — EBS](../extractions/spolsky-evidence-based-scheduling.md) | INFERRED | §1 |
| ESTIMATE-EBS-13 | ESTIMATE | Calibrate own estimates with own history (rule) | [Spolsky — EBS](../extractions/spolsky-evidence-based-scheduling.md) | INFERRED | §3; WWAI 1 |
| ESTIMATE-EBS-14 | ESTIMATE | >16h ⇒ not ready, decompose (gate) | [Spolsky — EBS](../extractions/spolsky-evidence-based-scheduling.md) | DIRECT | §1 |
| ESTIMATE-EBS-15 | ESTIMATE | No history ⇒ assume worst (rule) | [Spolsky — EBS](../extractions/spolsky-evidence-based-scheduling.md) | DIRECT | §2 |
| ESTIMATE-EBS-16 | ESTIMATE | Estimate not from implementer ⇒ invalid (rule) | [Spolsky — EBS](../extractions/spolsky-evidence-based-scheduling.md) | DIRECT | WWAI 1 |
| ESTIMATE-EBS-C01 | ESTIMATE | Concrete ≤16h tasks vs Ajax photo editor (pair) | [Spolsky — EBS](../extractions/spolsky-evidence-based-scheduling.md) | DIRECT | §1 |
| ESTIMATE-EBS-C02 | ESTIMATE | Monte Carlo vs summing (pair) | [Spolsky — EBS](../extractions/spolsky-evidence-based-scheduling.md) | DIRECT | §3 |
| ESTIMATE-EBS-C03 | ESTIMATE | Common vs bad estimator (pair) | [Spolsky — EBS](../extractions/spolsky-evidence-based-scheduling.md) | DIRECT | §2–3 |
| ESTIMATE-EBS-D01 | ESTIMATE | Add endpoint vs rework auth (derived) | [Spolsky — EBS](../extractions/spolsky-evidence-based-scheduling.md) | DERIVED | §1 |
| ESTIMATE-EBS-N01 | ESTIMATE | "Implement Ajax photo editor" 3 weeks (negative) | [Spolsky — EBS](../extractions/spolsky-evidence-based-scheduling.md) | DIRECT | §1 |
| ESTIMATE-EBS-N02 | ESTIMATE | Summing estimates (negative) | [Spolsky — EBS](../extractions/spolsky-evidence-based-scheduling.md) | DIRECT | §3 |
| ESTIMATE-EBS-N03 | ESTIMATE | Management-authored schedule (negative) | [Spolsky — EBS](../extractions/spolsky-evidence-based-scheduling.md) | DIRECT | WWAI 1 |
| ESTIMATE-EBS-N04 | ESTIMATE | Badgering / n vs 4n (negative) | [Spolsky — EBS](../extractions/spolsky-evidence-based-scheduling.md) | DIRECT | WWAI 3 |
| ESTIMATE-EBS-N05 | ESTIMATE | Forgotten halfhearted schedules (negative) | [Spolsky — EBS](../extractions/spolsky-evidence-based-scheduling.md) | DIRECT | intro |
| ESTIMATE-EBS-P01 | ESTIMATE | foo / dialog / Fizzbott tasks (positive) | [Spolsky — EBS](../extractions/spolsky-evidence-based-scheduling.md) | DIRECT | §1 |
| ESTIMATE-EBS-P02 | ESTIMATE | Common estimator calibrated (positive) | [Spolsky — EBS](../extractions/spolsky-evidence-based-scheduling.md) | DIRECT | §2–3 |
| ESTIMATE-EBS-Q01 | ESTIMATE | Any task >16h? Steps? (question) | [Spolsky — EBS](../extractions/spolsky-evidence-based-scheduling.md) | INFERRED | §1 |
| ESTIMATE-EBS-Q02 | ESTIMATE | Named as concrete action? (question) | [Spolsky — EBS](../extractions/spolsky-evidence-based-scheduling.md) | INFERRED | §1 |
| ESTIMATE-EBS-Q03 | ESTIMATE | Done similar before? (question) | [Spolsky — EBS](../extractions/spolsky-evidence-based-scheduling.md) | INFERRED | §1 |
| ESTIMATE-EBS-Q04 | ESTIMATE | Your own estimate? (question) | [Spolsky — EBS](../extractions/spolsky-evidence-based-scheduling.md) | INFERRED | WWAI 1 |
| ESTIMATE-EBS-Q05 | ESTIMATE | Calibrated estimate from velocity? (question) | [Spolsky — EBS](../extractions/spolsky-evidence-based-scheduling.md) | DERIVED | §2–3 |
| ESTIMATE-HILL-01 | ESTIMATE | Lists grow with progress (rule) | [Singer — Show Progress](../extractions/singer-shapeup-building-chapters.md) | DIRECT | Show Progress / The tasks that aren't there |
| ESTIMATE-HILL-02 | ESTIMATE | Estimates don't show uncertainty (rule) | [Singer — Show Progress](../extractions/singer-shapeup-building-chapters.md) | DIRECT | Show Progress / Estimates don't show uncertainty |
| ESTIMATE-HILL-04 | ESTIMATE | Estimate at top of hill (rule) | [Singer — Show Progress](../extractions/singer-shapeup-building-chapters.md) | DIRECT | Show Progress / Work is like a hill |
| ESTIMATE-HILL-09 | ESTIMATE | Trust estimates only downhill (rule) | [Singer — Show Progress](../extractions/singer-shapeup-building-chapters.md) | INFERRED | Show Progress |
| ESTIMATE-HILL-N04 | ESTIMATE | Two 4-hour tasks (negative) | [Singer — Show Progress](../extractions/singer-shapeup-building-chapters.md) | DIRECT | Show Progress / Estimates don't show uncertainty |
| ESTIMATE-HILL-P05 | ESTIMATE | Dinner party (positive) | [Singer — Show Progress](../extractions/singer-shapeup-building-chapters.md) | DIRECT | Show Progress / Work is like a hill |
| ESTIMATE-INVEST-01 | ESTIMATE | Estimability = negotiated + size + team (rule) | [Wake — INVEST/SMART](../extractions/wake-invest.md) | DIRECT | Estimable |
| ESTIMATE-INVEST-02 | ESTIMATE | Unestimable as diagnostic (rule) | [Wake — INVEST/SMART](../extractions/wake-invest.md) | INFERRED | Estimable |
| ESTIMATE-INVEST-C02 | ESTIMATE | Spike vs direct (pair) | [Wake — INVEST/SMART](../extractions/wake-invest.md) | DIRECT/DERIVED | Estimable |
| ESTIMATE-INVEST-D02 | ESTIMATE | Webhook spike (derived example) | [Wake — INVEST/SMART](../extractions/wake-invest.md) | DERIVED | — |
| ESTIMATE-INVEST-Q04 | ESTIMATE | Why unestimable? (question) | [Wake — INVEST/SMART](../extractions/wake-invest.md) | INFERRED | Estimable |
| ESTIMATE-SHAPING-03 | ESTIMATE | Over-specifying hurts estimation (rule) | [Singer — Principles of Shaping](../extractions/singer-principles-of-shaping.md) | DIRECT | Wireframes are too concrete |
| ESTIMATE-SHAPING-12 | ESTIMATE | Both extremes damage estimation (rule) | [Singer — Principles of Shaping](../extractions/singer-principles-of-shaping.md) | INFERRED | Wireframes / Words |
| ESTIMATE-SHAPING-C02 | ESTIMATE | Why extremes break estimation (pair) | [Singer — Principles of Shaping](../extractions/singer-principles-of-shaping.md) | DIRECT | Wireframes/Words |
| ESTIMATE-SYN-D01 | ESTIMATE | Invoice endpoint vs rework auth (derived example) | [synthesis/estimate.md](estimate.md) | DERIVED | — |
| ESTIMATE-SYN-D02 | ESTIMATE | Novel vs familiar 4h (derived example) | [synthesis/estimate.md](estimate.md) | DERIVED | — |
| ESTIMATE-TBLOCK-01 | ESTIMATE | Duration evidence could feed estimates (EBS bridge) (rule) | [Newport — Focus Week](../extractions/newport-focus-week-time-blocking.md) | INFERRED | "This scheduling commitment…" |
| COMMIT-BOUND-02 | COMMIT | Define time/attention deserved (rule) | [Singer — Set Boundaries](../extractions/singer-set-boundaries.md) | DIRECT | Setting the appetite |
| COMMIT-BOUND-03 | COMMIT | Appetite; Small/Big Batch (rule) | [Singer — Set Boundaries](../extractions/singer-set-boundaries.md) | DIRECT | Setting the appetite |
| COMMIT-BOUND-06 | COMMIT | Fixed time, variable scope (rule) | [Singer — Set Boundaries](../extractions/singer-set-boundaries.md) | DIRECT | Fixed time, variable scope |
| COMMIT-BOUND-07 | COMMIT | Good is relative (rule) | [Singer — Set Boundaries](../extractions/singer-set-boundaries.md) | DIRECT | “Good” is relative |
| COMMIT-BOUND-14 | COMMIT | Boundaries in place triad (rule) | [Singer — Set Boundaries](../extractions/singer-set-boundaries.md) | DIRECT | Boundaries in place |
| COMMIT-BOUND-17 | COMMIT | Triad gate (gate) | [Singer — Set Boundaries](../extractions/singer-set-boundaries.md) | DIRECT | Boundaries in place |
| COMMIT-BOUND-D03 | COMMIT | Appetite vs estimate endpoint (derived) | [Singer — Set Boundaries](../extractions/singer-set-boundaries.md) | DERIVED | — |
| COMMIT-BOUND-P04 | COMMIT | Book typos vs section (positive) | [Singer — Set Boundaries](../extractions/singer-set-boundaries.md) | DIRECT | Fixed time, variable scope |
| COMMIT-BOUND-Q01 | COMMIT | How much is it worth (question) | [Singer — Set Boundaries](../extractions/singer-set-boundaries.md) | DIRECT | Setting the appetite |
| COMMIT-BOUND-Q05 | COMMIT | Good within appetite (question) | [Singer — Set Boundaries](../extractions/singer-set-boundaries.md) | INFERRED | “Good” is relative |
| COMMIT-EBS-01 | COMMIT | Buffer categories (rule) | [Spolsky — EBS](../extractions/spolsky-evidence-based-scheduling.md) | DIRECT | Scope creep |
| COMMIT-EBS-02 | COMMIT | Box of wood blocks (rule) | [Spolsky — EBS](../extractions/spolsky-evidence-based-scheduling.md) | DIRECT | WWAI 4 |
| COMMIT-EBS-03 | COMMIT | Realistic schedule forces good cuts (rule) | [Spolsky — EBS](../extractions/spolsky-evidence-based-scheduling.md) | DIRECT | WWAI 4 |
| COMMIT-EBS-04 | COMMIT | Doesn't fit ⇒ delay or delete, never shrink (gate) | [Spolsky — EBS](../extractions/spolsky-evidence-based-scheduling.md) | DIRECT | WWAI 4 |
| COMMIT-EBS-C02 | COMMIT | Bigger box / remove blocks vs shrink blocks (pair) | [Spolsky — EBS](../extractions/spolsky-evidence-based-scheduling.md) | DIRECT | WWAI 3–4 |
| COMMIT-EBS-C03 | COMMIT | Schedule vs no schedule cuts (pair) | [Spolsky — EBS](../extractions/spolsky-evidence-based-scheduling.md) | DIRECT | WWAI 4 |
| COMMIT-EBS-D03 | COMMIT | Plan exceeds time: cut vs shrink (derived) | [Spolsky — EBS](../extractions/spolsky-evidence-based-scheduling.md) | DERIVED | WWAI 3–4 |
| COMMIT-EBS-N01 | COMMIT | Easy/fun feature first (negative) | [Spolsky — EBS](../extractions/spolsky-evidence-based-scheduling.md) | DIRECT | WWAI 4 |
| COMMIT-EBS-N02 | COMMIT | Shrinking the blocks (negative) | [Spolsky — EBS](../extractions/spolsky-evidence-based-scheduling.md) | DIRECT | WWAI 4 |
| COMMIT-EBS-P01 | COMMIT | Excel 5 cuts (positive) | [Spolsky — EBS](../extractions/spolsky-evidence-based-scheduling.md) | DIRECT | WWAI 4 |
| COMMIT-EBS-Q01 | COMMIT | Which block comes out, or bigger box? (question) | [Spolsky — EBS](../extractions/spolsky-evidence-based-scheduling.md) | INFERRED | WWAI 4 |
| COMMIT-INVEST-01 | COMMIT | Achievable; ask for help (rule) | [Wake — INVEST/SMART](../extractions/wake-invest.md) | DIRECT | Achievable |
| COMMIT-INVEST-02 | COMMIT | Time-boxed → help/split/change players (rule) | [Wake — INVEST/SMART](../extractions/wake-invest.md) | DIRECT | Time-Boxed |
| COMMIT-INVEST-03 | COMMIT | Time-box triggers decision (rule) | [Wake — INVEST/SMART](../extractions/wake-invest.md) | INFERRED | Time-Boxed |
| COMMIT-INVEST-04 | COMMIT | Over time-box → split/help (gate) | [Wake — INVEST/SMART](../extractions/wake-invest.md) | DIRECT | Time-Boxed |
| COMMIT-INVEST-Q06 | COMMIT | Duration that triggers help (question) | [Wake — INVEST/SMART](../extractions/wake-invest.md) | INFERRED | Time-Boxed |
| COMMIT-RISK-21 | COMMIT | De-risked exit (gate) | [Singer — Risks and Rabbit Holes](../extractions/singer-risks-and-rabbit-holes.md) | DIRECT | De-risked and ready to write up |
| COMMIT-SHAPING-07 | COMMIT | Bounded = appetite + scope limits (rule) | [Singer — Principles of Shaping](../extractions/singer-principles-of-shaping.md) | DIRECT | Property 3 |
| COMMIT-STOP-02 | COMMIT | Is there time for this? (rule) | [Singer — Decide When to Stop](../extractions/singer-shapeup-building-chapters.md) | DIRECT | Decide When to Stop / Limits motivate trade-offs |
| COMMIT-STOP-08 | COMMIT | When to extend (rule) | [Singer — Decide When to Stop](../extractions/singer-shapeup-building-chapters.md) | DIRECT | Decide When to Stop / When to extend a project |
| COMMIT-STOP-09 | COMMIT | Uphill at deadline → reshape (gate) | [Singer — Decide When to Stop](../extractions/singer-shapeup-building-chapters.md) | DIRECT | Decide When to Stop / When to extend a project |
| COMMIT-STOP-C05 | COMMIT | Extend vs circuit breaker (pair) | [Singer — Decide When to Stop](../extractions/singer-shapeup-building-chapters.md) | DIRECT | Decide When to Stop / When to extend a project |
| COMMIT-STOP-N06 | COMMIT | Accepting every improvement (negative) | [Singer — Decide When to Stop](../extractions/singer-shapeup-building-chapters.md) | DIRECT | Decide When to Stop / Limits motivate trade-offs |
| COMMIT-SYN-D01 | COMMIT | Appetite vs estimate, cut PDF (derived example) | [synthesis/commit.md](commit.md) | DERIVED | — |
| COMMIT-SYN-D02 | COMMIT | Block with goal + stop condition (derived example) | [synthesis/commit.md](commit.md) | DERIVED | — |
| COMMIT-TBLOCK-01 | COMMIT | Give every minute a job (rule) | [Newport — Focus Week](../extractions/newport-focus-week-time-blocking.md) | DIRECT | opening; basic idea |
| COMMIT-TBLOCK-02 | COMMIT | Partition day, assign specific work (rule) | [Newport — Focus Week](../extractions/newport-focus-week-time-blocking.md) | DIRECT | basic idea |
| COMMIT-TBLOCK-03 | COMMIT | Knocked off ⇒ rebuild rest of day; intention not perfection (rule) | [Newport — Focus Week](../extractions/newport-focus-week-time-blocking.md) | DIRECT | basic idea (parenthetical) |
| COMMIT-TBLOCK-04 | COMMIT | Two problems of list/reactive (rule) | [Newport — Focus Week](../extractions/newport-focus-week-time-blocking.md) | DIRECT | two-problems paras |
| COMMIT-TBLOCK-05 | COMMIT | Blocking controls urgent/important, fewer breaks (rule) | [Newport — Focus Week](../extractions/newport-focus-week-time-blocking.md) | DIRECT | following para |
| COMMIT-TBLOCK-06 | COMMIT | Cognitively demanding; not outside work (rule) | [Newport — Focus Week](../extractions/newport-focus-week-time-blocking.md) | DIRECT | word of warning |
| COMMIT-TBLOCK-07 | COMMIT | Not enough alone; reflect on what to focus on (rule) | [Newport — Focus Week](../extractions/newport-focus-week-time-blocking.md) | DIRECT | closing |
| COMMIT-TBLOCK-08 | COMMIT | Vague block doesn't satisfy method (rule) | [Newport — Focus Week](../extractions/newport-focus-week-time-blocking.md) | INFERRED | basic idea |
| COMMIT-TBLOCK-09 | COMMIT | Disrupted ⇒ re-plan remainder (gate) | [Newport — Focus Week](../extractions/newport-focus-week-time-blocking.md) | DIRECT | basic idea |
| COMMIT-TBLOCK-10 | COMMIT | Work time only (boundary) | [Newport — Focus Week](../extractions/newport-focus-week-time-blocking.md) | DIRECT | word of warning |
| COMMIT-TBLOCK-C01 | COMMIT | Time blocking vs list/reactive (pair) | [Newport — Focus Week](../extractions/newport-focus-week-time-blocking.md) | DIRECT | basic idea |
| COMMIT-TBLOCK-D01 | COMMIT | Interruption mid-block (derived) | [Newport — Focus Week](../extractions/newport-focus-week-time-blocking.md) | DERIVED | basic idea |
| COMMIT-TBLOCK-D02 | COMMIT | Specific vs vague block (derived) | [Newport — Focus Week](../extractions/newport-focus-week-time-blocking.md) | DERIVED | basic idea |
| COMMIT-TBLOCK-N01 | COMMIT | List/reactive day (negative) | [Newport — Focus Week](../extractions/newport-focus-week-time-blocking.md) | DIRECT | basic idea; two problems |
| COMMIT-TBLOCK-N02 | COMMIT | Blocking outside work ⇒ burnout (negative) | [Newport — Focus Week](../extractions/newport-focus-week-time-blocking.md) | DIRECT | word of warning |
| COMMIT-TBLOCK-P01 | COMMIT | Blocked morning example (positive) | [Newport — Focus Week](../extractions/newport-focus-week-time-blocking.md) | DIRECT | basic idea |
| COMMIT-TBLOCK-Q01 | COMMIT | What specific work is this block for? (question) | [Newport — Focus Week](../extractions/newport-focus-week-time-blocking.md) | INFERRED | basic idea |
| COMMIT-TBLOCK-Q02 | COMMIT | Important or reacting? (question) | [Newport — Focus Week](../extractions/newport-focus-week-time-blocking.md) | INFERRED | two problems |
| COMMIT-TBLOCK-Q03 | COMMIT | What if block ends first? (question) | [Newport — Focus Week](../extractions/newport-focus-week-time-blocking.md) | DERIVED | — |
| COMMIT-TBP-01 | COMMIT | Daily preliminary plan, every minute a job (rule) | [Newport — Time-Block Planner](../extractions/newport-time-block-planner.md) | DIRECT | A Closer Look |
| COMMIT-TBP-02 | COMMIT | Knocked off ⇒ update at next chance (rule) | [Newport — Time-Block Planner](../extractions/newport-time-block-planner.md) | DIRECT | A Closer Look |
| COMMIT-TBP-03 | COMMIT | "Preliminary" = draft, expected to change (rule) | [Newport — Time-Block Planner](../extractions/newport-time-block-planner.md) | INFERRED | A Closer Look |
| COMMIT-TBP-04 | COMMIT | Update, don't abandon (gate) | [Newport — Time-Block Planner](../extractions/newport-time-block-planner.md) | DIRECT | A Closer Look |
| COMMIT-TBP-D02 | COMMIT | Preliminary plan meets reality (derived) | [Newport — Time-Block Planner](../extractions/newport-time-block-planner.md) | DERIVED | A Closer Look |
| COMMIT-TBP-Q01 | COMMIT | Today's preliminary plan? (question) | [Newport — Time-Block Planner](../extractions/newport-time-block-planner.md) | INFERRED | A Closer Look |
| IMPLEMENT-BECK-01 | IMPLEMENT | TDD goals: old works, new works, ready for next, confidence (rule) | [Beck — Canon TDD](../extractions/beck-canon-tdd.md) | DIRECT | Overview |
| IMPLEMENT-BECK-02 | IMPLEMENT | Interface vs implementation split (rule) | [Beck — Canon TDD](../extractions/beck-canon-tdd.md) | DIRECT | Interface/Implementation Split |
| IMPLEMENT-BECK-03 | IMPLEMENT | One real automated test at a time (rule) | [Beck — Canon TDD](../extractions/beck-canon-tdd.md) | DIRECT | 2. Write a Test |
| IMPLEMENT-BECK-04 | IMPLEMENT | Interface decisions in test; implementation in refactor (rule) | [Beck — Canon TDD](../extractions/beck-canon-tdd.md) | DIRECT | 2.; 4. |
| IMPLEMENT-BECK-05 | IMPLEMENT | Make it pass for real (all prior tests too) (rule) | [Beck — Canon TDD](../extractions/beck-canon-tdd.md) | DIRECT | 3. Make it Pass |
| IMPLEMENT-BECK-06 | IMPLEMENT | Add discovered cases to list; mark off passed (rule) | [Beck — Canon TDD](../extractions/beck-canon-tdd.md) | DIRECT | 3. Make it Pass |
| IMPLEMENT-BECK-07 | IMPLEMENT | Refactor optional, separate step after green (rule) | [Beck — Canon TDD](../extractions/beck-canon-tdd.md) | DIRECT | 3.; 4. |
| IMPLEMENT-BECK-08 | IMPLEMENT | Test order matters; skill from experience (rule) | [Beck — Canon TDD](../extractions/beck-canon-tdd.md) | DIRECT | 2. Write a Test |
| IMPLEMENT-BECK-09 | IMPLEMENT | Descriptive not prescriptive; critique actual thing (rule) | [Beck — Canon TDD](../extractions/beck-canon-tdd.md) | DIRECT | Preface; Intro |
| IMPLEMENT-BECK-10 | IMPLEMENT | Test list defines "done" for the loop (rule) | [Beck — Canon TDD](../extractions/beck-canon-tdd.md) | INFERRED | 1. Test List |
| IMPLEMENT-BECK-11 | IMPLEMENT | Validation needs independent expected values (rule) | [Beck — Canon TDD](../extractions/beck-canon-tdd.md) | INFERRED | 3. Make it Pass |
| IMPLEMENT-BECK-12 | IMPLEMENT | Speculative tests are a rework liability (rule) | [Beck — Canon TDD](../extractions/beck-canon-tdd.md) | INFERRED | 2. Write a Test |
| IMPLEMENT-BECK-13 | IMPLEMENT | Behavior only in list; napkin sketch optional (gate) | [Beck — Canon TDD](../extractions/beck-canon-tdd.md) | DIRECT | 1. Test List |
| IMPLEMENT-BECK-14 | IMPLEMENT | Test needs setup/invocation/assertions; work back from asserts (gate) | [Beck — Canon TDD](../extractions/beck-canon-tdd.md) | DIRECT | 2. Write a Test |
| IMPLEMENT-BECK-15 | IMPLEMENT | Invalidating discovery → push on or start over (prefer restart, new order) (gate) | [Beck — Canon TDD](../extractions/beck-canon-tdd.md) | DIRECT | 3. Make it Pass |
| IMPLEMENT-BECK-16 | IMPLEMENT | Refactor only as far as needed this session (gate) | [Beck — Canon TDD](../extractions/beck-canon-tdd.md) | DIRECT | 4. |
| IMPLEMENT-BECK-17 | IMPLEMENT | Duplication is a hint, not a command (gate) | [Beck — Canon TDD](../extractions/beck-canon-tdd.md) | DIRECT | 4. |
| IMPLEMENT-BECK-C01 | IMPLEMENT | One at a time vs all up front (pair) | [Beck — Canon TDD](../extractions/beck-canon-tdd.md) | DIRECT | 2. |
| IMPLEMENT-BECK-C02 | IMPLEMENT | Pass for real vs fake pass (pair) | [Beck — Canon TDD](../extractions/beck-canon-tdd.md) | DIRECT | 3. |
| IMPLEMENT-BECK-C03 | IMPLEMENT | Separate hats vs two hats (pair) | [Beck — Canon TDD](../extractions/beck-canon-tdd.md) | DIRECT | 3.; 4. |
| IMPLEMENT-BECK-C04 | IMPLEMENT | Behavioral vs design-laden list (pair) | [Beck — Canon TDD](../extractions/beck-canon-tdd.md) | DIRECT | 1. |
| IMPLEMENT-BECK-C05 | IMPLEMENT | Enough refactor vs avoidance refactor (pair) | [Beck — Canon TDD](../extractions/beck-canon-tdd.md) | DIRECT | 4. |
| IMPLEMENT-BECK-D01 | IMPLEMENT | Email validation test list (derived) | [Beck — Canon TDD](../extractions/beck-canon-tdd.md) | DERIVED | — |
| IMPLEMENT-BECK-D02 | IMPLEMENT | API response expected values (derived) | [Beck — Canon TDD](../extractions/beck-canon-tdd.md) | DERIVED | — |
| IMPLEMENT-BECK-D03 | IMPLEMENT | Discovered case mid-change (derived) | [Beck — Canon TDD](../extractions/beck-canon-tdd.md) | DERIVED | — |
| IMPLEMENT-BECK-N01 | IMPLEMENT | Implementation design in test list (negative) | [Beck — Canon TDD](../extractions/beck-canon-tdd.md) | DIRECT | 1. Mistake |
| IMPLEMENT-BECK-N02 | IMPLEMENT | "TDD just launches into coding" (negative) | [Beck — Canon TDD](../extractions/beck-canon-tdd.md) | DIRECT | 1. |
| IMPLEMENT-BECK-N03 | IMPLEMENT | Assertion-free tests for coverage (negative) | [Beck — Canon TDD](../extractions/beck-canon-tdd.md) | DIRECT | 2. Mistake |
| IMPLEMENT-BECK-N04 | IMPLEMENT | All list items to tests up front (negative) | [Beck — Canon TDD](../extractions/beck-canon-tdd.md) | DIRECT | 2. Mistake |
| IMPLEMENT-BECK-N05 | IMPLEMENT | Delete assertions to pass (negative) | [Beck — Canon TDD](../extractions/beck-canon-tdd.md) | DIRECT | 3. Mistake |
| IMPLEMENT-BECK-N06 | IMPLEMENT | Paste computed values as expected (negative) | [Beck — Canon TDD](../extractions/beck-canon-tdd.md) | DIRECT | 3. Mistake |
| IMPLEMENT-BECK-N07 | IMPLEMENT | Refactor while making it pass (negative) | [Beck — Canon TDD](../extractions/beck-canon-tdd.md) | DIRECT | 3. Mistake |
| IMPLEMENT-BECK-N08 | IMPLEMENT | Over-refactoring this session (negative) | [Beck — Canon TDD](../extractions/beck-canon-tdd.md) | DIRECT | 4. Mistake |
| IMPLEMENT-BECK-N09 | IMPLEMENT | Abstracting too soon (negative) | [Beck — Canon TDD](../extractions/beck-canon-tdd.md) | DIRECT | 4. Mistake |
| IMPLEMENT-BECK-N10 | IMPLEMENT | Strawman critique (negative) | [Beck — Canon TDD](../extractions/beck-canon-tdd.md) | DIRECT | Preface |
| IMPLEMENT-BECK-P01 | IMPLEMENT | Enumerated behavioral variants (positive) | [Beck — Canon TDD](../extractions/beck-canon-tdd.md) | DIRECT | 1. |
| IMPLEMENT-BECK-P02 | IMPLEMENT | Start over, different order (positive) | [Beck — Canon TDD](../extractions/beck-canon-tdd.md) | DIRECT | 3. |
| IMPLEMENT-BECK-P03 | IMPLEMENT | Work backwards from assertions (positive) | [Beck — Canon TDD](../extractions/beck-canon-tdd.md) | DIRECT | 2. |
| IMPLEMENT-BECK-Q01 | IMPLEMENT | Behavior or implementation in list item? (question) | [Beck — Canon TDD](../extractions/beck-canon-tdd.md) | INFERRED | 1. |
| IMPLEMENT-BECK-Q02 | IMPLEMENT | Real assertion? (question) | [Beck — Canon TDD](../extractions/beck-canon-tdd.md) | INFERRED | 2. |
| IMPLEMENT-BECK-Q03 | IMPLEMENT | Expected value independent? (question) | [Beck — Canon TDD](../extractions/beck-canon-tdd.md) | INFERRED | 3. |
| IMPLEMENT-BECK-Q04 | IMPLEMENT | Passing or refactoring? (question) | [Beck — Canon TDD](../extractions/beck-canon-tdd.md) | INFERRED | 3. |
| IMPLEMENT-BECK-Q05 | IMPLEMENT | Discovery invalidates work → push on / restart? (question) | [Beck — Canon TDD](../extractions/beck-canon-tdd.md) | DIRECT | 3. |
| IMPLEMENT-BECK-Q06 | IMPLEMENT | Refactor needed or avoidance? (question) | [Beck — Canon TDD](../extractions/beck-canon-tdd.md) | INFERRED | 4. |
| IMPLEMENT-EBS-01 | IMPLEMENT | Fix bugs as found, charge to original task (rule) | [Spolsky — EBS](../extractions/spolsky-evidence-based-scheduling.md) | DIRECT | WWAI 2 |
| IMPLEMENT-FTDD-01 | IMPLEMENT | Test / pass / refactor new+old (rule) | [Fowler — TDD](../extractions/fowler-tdd.md) | DIRECT | opening |
| IMPLEMENT-FTDD-02 | IMPLEMENT | Test list first, pick one (rule) | [Fowler — TDD](../extractions/fowler-tdd.md) | DIRECT | para 2 |
| IMPLEMENT-FTDD-03 | IMPLEMENT | Sequence to salient design points (rule) | [Fowler — TDD](../extractions/fowler-tdd.md) | DIRECT | para 2 |
| IMPLEMENT-FTDD-04 | IMPLEMENT | Add tests to list as they occur (rule) | [Fowler — TDD](../extractions/fowler-tdd.md) | DIRECT | para 2 |
| IMPLEMENT-FTDD-05 | IMPLEMENT | Benefits: self-testing code, interface first (rule) | [Fowler — TDD](../extractions/fowler-tdd.md) | DIRECT | para 3 |
| IMPLEMENT-FTDD-06 | IMPLEMENT | Neglecting refactor = most common screw-up (rule) | [Fowler — TDD](../extractions/fowler-tdd.md) | DIRECT | para 4 |
| IMPLEMENT-FTDD-07 | IMPLEMENT | Canon TDD is the key summary (rule) | [Fowler — TDD](../extractions/fowler-tdd.md) | DIRECT | Further Reading |
| IMPLEMENT-FTDD-08 | IMPLEMENT | Refactor includes old code (rule) | [Fowler — TDD](../extractions/fowler-tdd.md) | INFERRED | opening |
| IMPLEMENT-FTDD-09 | IMPLEMENT | Code only in response to a test (gate) | [Fowler — TDD](../extractions/fowler-tdd.md) | DIRECT | para 3 |
| IMPLEMENT-FTDD-10 | IMPLEMENT | Choose next test by design salience (gate) | [Fowler — TDD](../extractions/fowler-tdd.md) | DIRECT | para 2 |
| IMPLEMENT-FTDD-11 | IMPLEMENT | Don't skip refactor (gate) | [Fowler — TDD](../extractions/fowler-tdd.md) | INFERRED | para 4 |
| IMPLEMENT-FTDD-C01 | IMPLEMENT | Full cycle vs red-green only (pair) | [Fowler — TDD](../extractions/fowler-tdd.md) | DIRECT | opening; para 4 |
| IMPLEMENT-FTDD-D01 | IMPLEMENT | Endpoint interface-first + refactor (derived) | [Fowler — TDD](../extractions/fowler-tdd.md) | DERIVED | — |
| IMPLEMENT-FTDD-N01 | IMPLEMENT | Neglecting refactor (negative) | [Fowler — TDD](../extractions/fowler-tdd.md) | DIRECT | para 4 |
| IMPLEMENT-FTDD-Q01 | IMPLEMENT | Which test reaches salient design fastest? (question) | [Fowler — TDD](../extractions/fowler-tdd.md) | INFERRED | para 2 |
| IMPLEMENT-FTDD-Q02 | IMPLEMENT | What is the interface? (question) | [Fowler — TDD](../extractions/fowler-tdd.md) | INFERRED | para 3 |
| IMPLEMENT-FTDD-Q03 | IMPLEMENT | Well structured after green? (question) | [Fowler — TDD](../extractions/fowler-tdd.md) | INFERRED | para 4 |
| IMPLEMENT-GWT-01 | IMPLEMENT | Givens = setup; thens = side-effect-free queries (rule) | [Fowler — Given When Then](../extractions/fowler-given-when-then.md) | DIRECT | pre-condition para |
| IMPLEMENT-GWT-02 | IMPLEMENT | Usable in any test and in prose (rule) | [Fowler — Given When Then](../extractions/fowler-given-when-then.md) | DIRECT | after example |
| IMPLEMENT-GWT-03 | IMPLEMENT | Four-Phase Test / AAA equivalence (rule) | [Fowler — Given When Then](../extractions/fowler-given-when-then.md) | DIRECT | final para; note 5 |
| IMPLEMENT-GWT-04 | IMPLEMENT | Then side-effect free (gate) | [Fowler — Given When Then](../extractions/fowler-given-when-then.md) | DIRECT | pre-condition para |
| IMPLEMENT-GWT-N01 | IMPLEMENT | Side-effecting then-queries (negative) | [Fowler — Given When Then](../extractions/fowler-given-when-then.md) | DIRECT | pre-condition para |
| IMPLEMENT-ONEPIECE-03 | IMPLEMENT | Affordances before pixels (rule) | [Singer — Get One Piece Done](../extractions/singer-shapeup-building-chapters.md) | DIRECT | Get One Piece Done / Affordances before pixel-perfect screens |
| IMPLEMENT-ONEPIECE-04 | IMPLEMENT | Program just enough (rule) | [Singer — Get One Piece Done](../extractions/singer-shapeup-building-chapters.md) | DIRECT | Get One Piece Done / Program just enough for the next step |
| IMPLEMENT-ONEPIECE-P02 | IMPLEMENT | Hard-coded HTTPAuth (positive) | [Singer — Get One Piece Done](../extractions/singer-shapeup-building-chapters.md) | DIRECT | Get One Piece Done / Program just enough |
| IMPLEMENT-SBE-01 | IMPLEMENT | Double-check via different methods (rule) | [Fowler — Specification By Example](../extractions/fowler-specification-by-example.md) | DIRECT | para 5 |
| IMPLEMENT-SYN-D01 | IMPLEMENT | Failing test: recompute expected (derived example) | [synthesis/implement.md](implement.md) | DERIVED | — |
| IMPLEMENT-SYN-D02 | IMPLEMENT | Capture discovered serializer leak (derived example) | [synthesis/implement.md](implement.md) | DERIVED | — |
| IMPLEMENT-TBP-01 | IMPLEMENT | Collection page: capture without disrupting block (rule) | [Newport — Time-Block Planner](../extractions/newport-time-block-planner.md) | DIRECT | A Closer Look |
| IMPLEMENT-TBP-02 | IMPLEMENT | New task mid-block ⇒ capture, continue (gate) | [Newport — Time-Block Planner](../extractions/newport-time-block-planner.md) | DIRECT | A Closer Look |
| IMPLEMENT-TBP-C01 | IMPLEMENT | Capture vs switch (pair) | [Newport — Time-Block Planner](../extractions/newport-time-block-planner.md) | DIRECT (good) / DERIVED (bad) | A Closer Look |
| IMPLEMENT-TBP-D01 | IMPLEMENT | Discovered refactor mid-slice (derived) | [Newport — Time-Block Planner](../extractions/newport-time-block-planner.md) | DERIVED | A Closer Look |
| IMPLEMENT-TBP-P01 | IMPLEMENT | Capture without disrupting (positive) | [Newport — Time-Block Planner](../extractions/newport-time-block-planner.md) | DIRECT | A Closer Look |
| IMPLEMENT-TBP-Q01 | IMPLEMENT | Now, or capture for later? (question) | [Newport — Time-Block Planner](../extractions/newport-time-block-planner.md) | INFERRED | A Closer Look |
| CLOSE-BECK-01 | CLOSE | Loop until list empty; fear → boredom (rule) | [Beck — Canon TDD](../extractions/beck-canon-tdd.md) | DIRECT | 5. |
| CLOSE-BECK-02 | CLOSE | Stop: list empty and fear is boredom (gate) | [Beck — Canon TDD](../extractions/beck-canon-tdd.md) | DIRECT | 5. |
| CLOSE-BECK-Q01 | CLOSE | List empty and no fear left? (question) | [Beck — Canon TDD](../extractions/beck-canon-tdd.md) | INFERRED | 5. |
| CLOSE-EBS-01 | CLOSE | Track elapsed time per task vs estimate (rule) | [Spolsky — EBS](../extractions/spolsky-evidence-based-scheduling.md) | DIRECT | §2 |
| CLOSE-EBS-02 | CLOSE | Velocity = estimate/actual, history per dev (rule) | [Spolsky — EBS](../extractions/spolsky-evidence-based-scheduling.md) | DIRECT | §2 |
| CLOSE-EBS-03 | CLOSE | Keep the clock running on interruptions (rule) | [Spolsky — EBS](../extractions/spolsky-evidence-based-scheduling.md) | DIRECT | OCD not required |
| CLOSE-EBS-04 | CLOSE | Nightly snapshot; >1 day/day slip = never done (rule) | [Spolsky — EBS](../extractions/spolsky-evidence-based-scheduling.md) | DIRECT | Scope creep |
| CLOSE-EBS-05 | CLOSE | Estimate before, full actual after (rule) | [Spolsky — EBS](../extractions/spolsky-evidence-based-scheduling.md) | INFERRED | §2; OCD; WWAI 2 |
| CLOSE-EBS-06 | CLOSE | Slip >1 day/day ⇒ stop adding / cut (gate) | [Spolsky — EBS](../extractions/spolsky-evidence-based-scheduling.md) | DIRECT (signal) / INFERRED (action) | Scope creep |
| CLOSE-EBS-07 | CLOSE | Wide distribution ⇒ don't trust date (gate) | [Spolsky — EBS](../extractions/spolsky-evidence-based-scheduling.md) | DIRECT | §3; §4 |
| CLOSE-EBS-C01 | CLOSE | Clock running vs separate interruption tracking (pair) | [Spolsky — EBS](../extractions/spolsky-evidence-based-scheduling.md) | DIRECT | OCD not required |
| CLOSE-EBS-D02 | CLOSE | Estimate vs actual after a slice (derived) | [Spolsky — EBS](../extractions/spolsky-evidence-based-scheduling.md) | DERIVED | §2; OCD; WWAI 2 |
| CLOSE-EBS-P01 | CLOSE | John / marlin, clock running (positive) | [Spolsky — EBS](../extractions/spolsky-evidence-based-scheduling.md) | DIRECT | OCD not required |
| CLOSE-EBS-Q01 | CLOSE | Estimate, actual, velocity? (question) | [Spolsky — EBS](../extractions/spolsky-evidence-based-scheduling.md) | INFERRED | §2; OCD |
| CLOSE-EBS-Q02 | CLOSE | Bug time charged back? (question) | [Spolsky — EBS](../extractions/spolsky-evidence-based-scheduling.md) | INFERRED | WWAI 2 |
| CLOSE-HANDOVER-04 | CLOSE | Imagined vs discovered tasks (rule) | [Singer — Hand Over Responsibility](../extractions/singer-shapeup-building-chapters.md) | DIRECT | Hand Over Responsibility / Imagined vs discovered tasks |
| CLOSE-HANDOVER-07 | CLOSE | Done means deployed (rule) | [Singer — Hand Over Responsibility](../extractions/singer-shapeup-building-chapters.md) | DIRECT | Hand Over Responsibility / Done means deployed |
| CLOSE-HANDOVER-10 | CLOSE | Discovered tasks expected (rule) | [Singer — Hand Over Responsibility](../extractions/singer-shapeup-building-chapters.md) | INFERRED | Hand Over Responsibility; Show Progress |
| CLOSE-INVEST-01 | CLOSE | Feedback cycle teaches (rule) | [Wake — INVEST/SMART](../extractions/wake-invest.md) | DIRECT | Testable |
| CLOSE-INVEST-02 | CLOSE | Measurable: can we mark it done (rule) | [Wake — INVEST/SMART](../extractions/wake-invest.md) | DIRECT | Measurable |
| CLOSE-INVEST-03 | CLOSE | Done = intended + tests + refactored (gate) | [Wake — INVEST/SMART](../extractions/wake-invest.md) | DIRECT | Measurable |
| CLOSE-INVEST-C03 | CLOSE | Done definition (pair) | [Wake — INVEST/SMART](../extractions/wake-invest.md) | DIRECT/DERIVED | Measurable |
| CLOSE-INVEST-Q05 | CLOSE | Can we mark it as done? (question) | [Wake — INVEST/SMART](../extractions/wake-invest.md) | DIRECT | Measurable |
| CLOSE-STOP-01 | CLOSE | Compare to baseline (rule) | [Singer — Decide When to Stop](../extractions/singer-shapeup-building-chapters.md) | DIRECT | Decide When to Stop / Compare to baseline |
| CLOSE-STOP-03 | CLOSE | Scope grows like grass (rule) | [Singer — Decide When to Stop](../extractions/singer-shapeup-building-chapters.md) | DIRECT | Decide When to Stop / Scope grows like grass |
| CLOSE-STOP-04 | CLOSE | Cutting ≠ lowering quality (rule) | [Singer — Decide When to Stop](../extractions/singer-shapeup-building-chapters.md) | DIRECT | Decide When to Stop / Cutting scope isn't lowering quality |
| CLOSE-STOP-05 | CLOSE | Scope hammering questions (rule) | [Singer — Decide When to Stop](../extractions/singer-shapeup-building-chapters.md) | DIRECT | Decide When to Stop / Scope hammering |
| CLOSE-STOP-06 | CLOSE | Must-have vs ~nice-to-have (rule) | [Singer — Decide When to Stop](../extractions/singer-shapeup-building-chapters.md) | DIRECT | Decide When to Stop / Scope hammering |
| CLOSE-STOP-07 | CLOSE | QA findings nice-to-have by default (rule) | [Singer — Decide When to Stop](../extractions/singer-shapeup-building-chapters.md) | DIRECT | Decide When to Stop / QA is for the edges |
| CLOSE-STOP-C04 | CLOSE | Compare down vs up (pair) | [Singer — Decide When to Stop](../extractions/singer-shapeup-building-chapters.md) | DIRECT | Decide When to Stop / Compare to baseline |
| CLOSE-STOP-Q05 | CLOSE | Baseline today? (question) | [Singer — Decide When to Stop](../extractions/singer-shapeup-building-chapters.md) | DIRECT | Decide When to Stop / Compare to baseline |
| CLOSE-STOP-Q06 | CLOSE | Is there time for this? (question) | [Singer — Decide When to Stop](../extractions/singer-shapeup-building-chapters.md) | DIRECT | Decide When to Stop / Limits motivate trade-offs |
| CLOSE-STOP-Q07 | CLOSE | Scope hammering list (question) | [Singer — Decide When to Stop](../extractions/singer-shapeup-building-chapters.md) | DIRECT | Decide When to Stop / Scope hammering |
| CLOSE-SYN-D01 | CLOSE | Estimate vs actual record (derived example) | [synthesis/close.md](close.md) | DERIVED | — |
| CLOSE-SYN-D02 | CLOSE | Time box ended, uphill leftover → spike (derived example) | [synthesis/close.md](close.md) | DERIVED | — |
| CLOSE-TBLOCK-01 | CLOSE | Hard evidence on time available / durations (rule) | [Newport — Focus Week](../extractions/newport-focus-week-time-blocking.md) | DIRECT | "This scheduling commitment…" |
| CLOSE-TBLOCK-02 | CLOSE | Divergence ⇒ re-plan, not abandon (rule) | [Newport — Focus Week](../extractions/newport-focus-week-time-blocking.md) | INFERRED | basic idea |
| CLOSE-TBLOCK-C02 | CLOSE | Rebuild vs abandon plan (pair) | [Newport — Focus Week](../extractions/newport-focus-week-time-blocking.md) | DIRECT (good) / DERIVED (bad) | basic idea |
| CLOSE-TBLOCK-P01 | CLOSE | Re-plan after disruption (positive) | [Newport — Focus Week](../extractions/newport-focus-week-time-blocking.md) | DIRECT | basic idea |
| CLOSE-TBLOCK-Q01 | CLOSE | Rest of today now? (question) | [Newport — Focus Week](../extractions/newport-focus-week-time-blocking.md) | INFERRED | basic idea |
| CLOSE-TBLOCK-Q02 | CLOSE | How long vs block? (question) | [Newport — Focus Week](../extractions/newport-focus-week-time-blocking.md) | INFERRED | "This scheduling commitment…" |
| CLOSE-TBP-01 | CLOSE | Captured items processed later (rule) | [Newport — Time-Block Planner](../extractions/newport-time-block-planner.md) | INFERRED | A Closer Look |
| CLOSE-TBP-Q01 | CLOSE | Captured items → slices/bugs/notes? (question) | [Newport — Time-Block Planner](../extractions/newport-time-block-planner.md) | DERIVED | — |
