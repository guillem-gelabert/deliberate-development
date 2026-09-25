# 24 — Which command should I use?

**Skill:** `dd:help` · **Behaviors:** EB-49 · **Grounding:** DERIVED (skill routing)

## Setup

Any repository with the plugin installed. Run the prompt twice:

- **(a)** no `.work/` directory;
- **(b)** a workspace `.work/PHS-1234/` containing `STATUS.md`.

## Prompt

"I've installed Deliberate Development but don't know which command to use."

## Expected

- [ ] Selects `dd:help` (EB-49).
- [ ] Lists the five commands (`dd:ground`, `dd:shape`, `dd:execute`, `dd:state`, `dd:help`) with a one-line purpose each, and the normal flow `dd:ground → dd:shape → dd:execute` (EB-49).
- [ ] Says which command to start with for common situations, such as a new task or returning to one (EB-49).
- [ ] In (a), says no task workspaces exist yet and points to `dd:ground` for a new task, or `dd:state` for work already under way (EB-49).
- [ ] In (b), names `PHS-1234` as an existing workspace and points to `dd:state` to pick it up (EB-49).
- [ ] Creates, edits or deletes nothing; no `.work/` appears in (a) and `init_work.py` is not run (EB-49).
- [ ] Does not start grounding, shaping or execution, and does not inspect the repository to reconcile task state (EB-49).

## Failure signals

- Starts `dd:ground` on whatever the branch contains.
- Reports PHS-1234's stage, slice or next action (that belongs to `dd:state`).
- Opens files inside `.work/PHS-1234/`.
- A multi-page restatement of the methodology.
