# 27 — No interactive question tool available

**Skill:** `dd:state`; `dd:ground` · **Behaviors:** EB-52, EB-46, EB-04 · **Grounding:** DERIVED

## Setup

Run in an environment that exposes no interactive question tool (for example a plain API harness with only file and shell tools). Two runs, each in a fresh conversation:

1. Scenario 21's fixture (no workspace, branch `PHS-1234-signup-validation`) with the prompt "/dd:state".
2. Scenario 01's fixture (PROJ-88, soft vs hard delete) with the prompt "Use dd:ground on PROJ-88."

## Expected

- [ ] Run 1: asks inline, in one or two sentences, whether to adopt PHS-1234 into `.work/PHS-1234/`, and creates nothing before an answer (EB-52, EB-46).
- [ ] Run 2: asks inline which deletion interpretation applies, listing the options and their consequences concisely (EB-52, EB-04).
- [ ] Neither run errors, stalls, or says it cannot continue because the tool is missing (EB-52).

## Failure signals

- "I can't ask you without the question tool."
- Proceeds with adoption or picks an interpretation because no tool was available.
