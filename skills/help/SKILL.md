---
name: help
description: Explain Deliberate Development and point to the right dd command. Use for help, how does Deliberate Development work, which dd command should I use, what are the dd commands, what should I run first, or I'm not sure where to start. Questions about a specific task's state or next step, such as what should I do next on PHS-1234, belong to dd:state.
---

# Help

## Role in the workflow

- **Purpose:** Explain Deliberate Development and recommend the command that fits the user's situation.
- **Position:** Orientation layer outside the task stages.
- **Consumes:** The user's question and a listing of the task-doc root, which shows which task workspaces exist. No task file contents or other repository state.
- **Produces:** A concise explanation or command recommendation; does not mutate task state.
- **Handoff:** Stop when the question is answered. Point to `dd:ground`, `dd:shape`, `dd:execute`, or `dd:state` as appropriate; do not start that skill's work.

Orient the user and name the command that fits. First, before writing any reply, check whether Deliberate Development is in use here: take the task-doc location from applicable project instructions, else `.work/` at the repository root, and list it (for example `ls -d .work/*/STATUS.md`). Each subdirectory holding `STATUS.md` is a task workspace. Never write the project-state line from assumption; if the listing cannot be run, say that the check was skipped. Do not open task files, inspect git, or report a task's stage or next step; that is `dd:state`'s job. Write nothing, and do not start another skill's work. If the user asks about a specific task's progress or next step, say that `dd:state` answers it and offer to run it.

The project-state line is one of these, with the real workspace names:

- Workspaces found: `Task workspaces here: PHS-1234, PHS-1288. To pick one up, run dd:state.` Past about five, give the count and the first few names.
- None found: `No Deliberate Development task workspaces here yet. Start a new task with dd:ground; bring work already under way in with dd:state.`

On a bare invocation, reply with the project-state line, then this cheat sheet and workflow map, then stop:

| Command | Use it to |
|---|---|
| `dd:ground` | understand the task and the current system |
| `dd:shape` | design, de-risk and slice the work |
| `dd:execute` | implement a ready slice |
| `dd:state` | resume, inspect, adopt, checkpoint, or find the next action |
| `dd:help` | explain the workflow and the commands |

```text
                  ┌─────────────┐
                  │   dd:help   │
                  └──────┬──────┘
                         │
                         ▼
dd:ground → dd:shape → dd:execute
    ▲          ▲            ▲
    └──────────┴──── dd:state ┘
```

Repeat `dd:execute` per slice. `dd:state` is the way in and back in: use it when returning to a task, when work started outside the workflow, or to checkpoint before stopping. Task state lives in `.work/<task-id>/` (or the project's own task-doc location, if its instructions define one), so any agent or conversation can pick it up.

Which command for which situation:

- New or unclear task → `dd:ground`
- Requirements understood, design or slices unclear → `dd:shape`
- A ready slice to implement → `dd:execute`
- An existing task, interrupted work, or "where was I?" → `dd:state`
- Unsure → `dd:help`

For a more specific question, answer it in a few sentences and name one command, using the project state where it changes the answer. If the user wants help choosing but their situation is unclear, you may ask "What are you trying to do?" through the environment's native interactive question tool (in Claude Code, `AskUserQuestion`), with options such as *Start or clarify a task* (`dd:ground`), *Design or slice known work* (`dd:shape`), *Implement ready work* (`dd:execute`) and *Resume, check or adopt existing work* (`dd:state`); without the tool, show the list above. A bare invocation always gets the cheat sheet without a question. Leave the methodology details to the skill that owns them.
