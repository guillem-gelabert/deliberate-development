#!/usr/bin/env python3
"""Check the mechanical invariants of a deliberate-development task workspace.

Usage:
    validate_work.py <workspace-dir>

Checks structure only: required files, STATUS.md frontmatter and vocabulary,
artifact-state lines, slice IDs and states in PLAN.md, current_slice
consistency, and state contradictions that can be detected without judgment.
Warnings flag places where the STATUS.md cursor looks stale against PLAN.md;
deciding what the real state is stays with the agent. It never judges
requirements, design, risk, slicing or estimates, never reads the repository,
and never modifies files. Exit code: 0 = no errors (warnings allowed), 1 = errors.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

FILES = ["STATUS.md", "SPEC.md", "CURRENT_STATE.md", "ARCHITECTURE.md", "PLAN.md"]
STEPS = {
    "ground": {"requirements", "context", "handoff"},
    "shape": {"architecture", "architecture-risk", "slicing", "slice-readiness", "handoff"},
    "execute": {"prepare", "implement", "close"},
}
# Stage names before the 0.5.0 rename; accepted so existing workspaces keep validating.
LEGACY_STAGES = {"ground-work": "ground", "shape-work": "shape", "execute-work": "execute"}
STATUSES = {"in-progress", "blocked", "needs-user", "stage-complete", "done"}
ARTIFACT_STATES = {"not-started", "draft", "blocked", "review-needed", "complete", "stale"}
SLICE_STATES = {"candidate", "not-ready", "ready", "in-progress", "blocked", "done", "dropped"}
UNSETTLED = {"not-started", "draft", "blocked"}

H2 = re.compile(r"^##\s+(.+?)\s*$", re.MULTILINE)
SLICE_HEADING = re.compile(r"^S(\d+)\b")
CHECKBOX = re.compile(r"^\s*[-*]\s+\[( |x|X)\]", re.MULTILINE)


def parse_frontmatter(text: str) -> dict[str, str] | None:
    text = text.replace("\r\n", "\n")
    if not text.startswith("---\n"):
        return None
    end = text.find("\n---", 4)
    if end < 0:
        return None
    data: dict[str, str] = {}
    for line in text[4:end].splitlines():
        line = re.sub(r"\s+#.*$", "", line).rstrip()
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if ":" not in line:
            return None
        key, value = line.split(":", 1)
        data[key.strip()] = value.strip().strip("'\"")
    return data


def sections(text: str) -> list[tuple[str, str]]:
    """Level-2 sections as (heading, body)."""
    matches = list(H2.finditer(text))
    out = []
    for i, m in enumerate(matches):
        end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        out.append((m.group(1), text[m.end():end]))
    return out


def section(text: str, name: str) -> str | None:
    for heading, body in sections(text):
        if heading.strip().lower() == name.lower():
            return body
    return None


def strip_comments(text: str) -> str:
    return re.sub(r"<!--.*?-->", "", text, flags=re.DOTALL)


def done_when_boxes(body: str) -> list[bool] | None:
    """Checked flags for boxes under **Done when**; None if the block is absent."""
    m = re.search(r"^\*\*Done when\*\*\s*$", body, re.MULTILINE)
    if not m:
        return None
    rest = body[m.end():]
    nxt = re.search(r"^\*\*[^*]+\*\*", rest, re.MULTILINE)
    block = rest[: nxt.start()] if nxt else rest
    return [c.lower() == "x" for c in CHECKBOX.findall(block)]


def main() -> int:
    if len(sys.argv) != 2 or sys.argv[1] in {"-h", "--help"}:
        print(__doc__.strip())
        return 0 if len(sys.argv) == 2 else 1
    root = Path(sys.argv[1])
    errors: list[str] = []
    warnings: list[str] = []

    missing = [n for n in FILES if not (root / n).is_file()]
    if missing:
        for n in missing:
            print(f"ERROR: missing {root / n}")
        return 1
    status_text = (root / "STATUS.md").read_text(encoding="utf-8")
    plan_text = (root / "PLAN.md").read_text(encoding="utf-8")

    # --- STATUS.md frontmatter
    fm = parse_frontmatter(status_text)
    if fm is None:
        print("ERROR: STATUS.md has no parseable '---' frontmatter")
        return 1
    stage, step, status = fm.get("stage", ""), fm.get("step", ""), fm.get("status", "")
    if stage in LEGACY_STAGES:
        warnings.append(f"STATUS.md: legacy stage '{stage}'; rename it to '{LEGACY_STAGES[stage]}'")
        stage = LEGACY_STAGES[stage]
    current = fm.get("current_slice", "")
    for key in ("stage", "step", "status"):
        if not fm.get(key):
            errors.append(f"STATUS.md frontmatter: '{key}' is empty or missing")
    if "current_slice" not in fm:
        errors.append("STATUS.md frontmatter: 'current_slice' key missing (leave it empty if none)")
    if not fm.get("updated"):
        warnings.append("STATUS.md frontmatter: 'updated' is empty")
    elif not re.fullmatch(r"\d{4}-\d{2}-\d{2}", fm["updated"]):
        errors.append(f"STATUS.md frontmatter: 'updated' is '{fm['updated']}', expected an ISO date (YYYY-MM-DD)")
    if stage and stage not in STEPS:
        errors.append(f"STATUS.md: unknown stage '{stage}' (expected one of {sorted(STEPS)})")
    elif stage and step and step not in STEPS[stage]:
        errors.append(f"STATUS.md: step '{step}' is not valid for {stage} (expected one of {sorted(STEPS[stage])})")
    if status and status not in STATUSES:
        errors.append(f"STATUS.md: unknown status '{status}' (expected one of {sorted(STATUSES)})")

    # --- STATUS.md artifact states
    artifacts: dict[str, str] = {}
    art_body = section(status_text, "Artifact state")
    if art_body is None:
        errors.append("STATUS.md: missing '## Artifact state' section")
    else:
        for m in re.finditer(r"^\s*[-*]\s+`?([A-Z_]+\.md)`?\s*:\s*`?([a-z-]+)`?", art_body, re.MULTILINE):
            artifacts[m.group(1)] = m.group(2)
        for name in FILES[1:]:
            state = artifacts.get(name)
            if state is None:
                errors.append(f"STATUS.md: no artifact state line for {name}")
            elif state not in ARTIFACT_STATES:
                errors.append(f"STATUS.md: {name} has unknown state '{state}' (expected one of {sorted(ARTIFACT_STATES)})")

    # --- STATUS.md open / next
    open_body = section(status_text, "Open")
    if open_body is None:
        errors.append("STATUS.md: missing '## Open' section")
    next_body = section(status_text, "Next")
    if next_body is None:
        errors.append("STATUS.md: missing '## Next' section")
    else:
        nxt = strip_comments(next_body).strip()
        if not nxt:
            errors.append("STATUS.md: '## Next' is empty; write one concrete next action")
        else:
            bullets = re.findall(r"^\s*(?:[-*]|\d+\.)\s+", nxt, re.MULTILINE)
            if len(bullets) > 1:
                warnings.append("STATUS.md: '## Next' lists several items; the contract expects one action")
            if len(nxt.split()) < 6:
                warnings.append(f"STATUS.md: '## Next' is very short ('{nxt}'); name the action and the file/section it updates")
    if status in {"blocked", "needs-user"} and open_body is not None:
        items = [l for l in strip_comments(open_body).splitlines() if l.strip() and "none recorded" not in l.lower()]
        if not items:
            warnings.append(f"STATUS.md: status is {status} but '## Open' records no blocker or question")

    # --- PLAN.md slices
    slices: dict[str, dict] = {}
    discovered_ids: list[str] = []
    has_discovered = False
    for heading, body in sections(plan_text):
        if heading.strip().lower() == "discovered work":
            has_discovered = True
            discovered_ids = re.findall(r"^\s*[-*]\s+(?:\[[ xX]\]\s+)?(D\d+)\b", body, re.MULTILINE)
            continue
        m = SLICE_HEADING.match(heading)
        if not m:
            continue
        sid = f"S{m.group(1)}"
        if sid in slices:
            errors.append(f"PLAN.md: duplicate slice id {sid}")
            continue
        sm = re.search(r"^\*\*Status:\*\*\s*`?([a-z-]+)`?\s*$", body, re.MULTILINE)
        slices[sid] = {
            "status": sm.group(1) if sm else None,
            "boxes": done_when_boxes(body),
            "estimate": bool(re.search(r"^\*\*Estimate:\*\*\s*\S", body, re.MULTILINE)),
            "actual": bool(re.search(r"^\*\*Actual:\*\*\s*\S", body, re.MULTILINE)),
        }
    if not has_discovered:
        warnings.append("PLAN.md: missing '## Discovered work' section")
    for did in sorted({d for d in discovered_ids if discovered_ids.count(d) > 1}):
        errors.append(f"PLAN.md: duplicate discovered-work id {did}")

    for sid, s in slices.items():
        st = s["status"]
        if st is None:
            errors.append(f"PLAN.md: {sid} has no '**Status:** <state>' line")
            continue
        if st not in SLICE_STATES:
            errors.append(f"PLAN.md: {sid} has unknown status '{st}' (expected one of {sorted(SLICE_STATES)})")
            continue
        boxes = s["boxes"]
        if st in {"ready", "in-progress", "done"} and not boxes:
            errors.append(f"PLAN.md: {sid} is {st} but has no '**Done when**' checkboxes")
        if st == "done" and boxes and not all(boxes):
            errors.append(f"PLAN.md: {sid} is done but {boxes.count(False)} 'Done when' box(es) are unchecked")
        if st == "done" and s["estimate"] and not s["actual"]:
            warnings.append(f"PLAN.md: {sid} is done with an Estimate but no Actual recorded")

    in_progress = [sid for sid, s in slices.items() if s["status"] == "in-progress"]
    if len(in_progress) > 1:
        errors.append(f"PLAN.md: more than one slice in-progress: {', '.join(in_progress)}")
    if in_progress and current != in_progress[0] and len(in_progress) == 1:
        errors.append(f"STATUS.md current_slice is '{current or '(empty)'}' but {in_progress[0]} is in-progress in PLAN.md")

    # --- current_slice compatibility
    if current:
        if current not in slices:
            errors.append(f"STATUS.md current_slice {current} does not exist in PLAN.md")
        else:
            cs = slices[current]["status"]
            if stage == "execute" and status in {"in-progress", "needs-user"} and cs not in {"ready", "in-progress"}:
                errors.append(f"STATUS.md: executing {current} but its PLAN.md status is '{cs}' (expected ready or in-progress)")
            if stage == "execute" and status == "blocked" and cs not in {"blocked", "in-progress", "ready"}:
                errors.append(f"STATUS.md: blocked on {current} but its PLAN.md status is '{cs}'")
    elif stage == "execute" and status in {"in-progress", "needs-user", "blocked"}:
        errors.append("STATUS.md: stage is execute but current_slice is empty")

    # --- cursor possibly stale (warnings: the agent decides what is true)
    if current in slices and slices[current]["status"] == "in-progress":
        boxes = slices[current]["boxes"]
        if boxes and all(boxes):
            warnings.append(f"PLAN.md: {current} is in-progress but every 'Done when' box is checked; "
                            "verify and close it, or uncheck what is not verified")
    if stage in {"ground", "shape"} and in_progress:
        warnings.append(f"STATUS.md: stage is {stage} but {in_progress[0]} is in-progress in PLAN.md; "
                        "the cursor or the slice state is stale")
    if stage == "execute" and status == "in-progress":
        for name in ("SPEC.md", "ARCHITECTURE.md"):
            if artifacts.get(name) == "stale":
                warnings.append(f"STATUS.md: executing while {name} is stale; confirm {current or 'the slice'} "
                                "does not rest on the stale part, or route back")
        for name in ("SPEC.md", "CURRENT_STATE.md", "ARCHITECTURE.md", "PLAN.md"):
            if artifacts.get(name) == "review-needed":
                warnings.append(f"STATUS.md: {name} is review-needed; reconcile the sections "
                                f"{current or 'the slice'} depends on before executing")

    # --- artifact-state contradictions
    plan_state = artifacts.get("PLAN.md")
    if plan_state == "not-started" and slices:
        errors.append(f"STATUS.md says PLAN.md is not-started but PLAN.md defines {len(slices)} slice(s)")
    if stage == "execute":
        for name in ("ARCHITECTURE.md", "PLAN.md"):
            if artifacts.get(name) == "not-started":
                errors.append(f"STATUS.md: stage is execute but {name} is not-started")
        if not any(s["status"] in {"ready", "in-progress", "blocked", "done"} for s in slices.values()):
            errors.append("PLAN.md: stage is execute but no slice is ready, in-progress, blocked or done")
    if stage == "shape":
        for name in ("SPEC.md", "CURRENT_STATE.md"):
            if artifacts.get(name) == "not-started":
                warnings.append(f"STATUS.md: stage is shape but {name} is not-started (grounding skipped?)")

    # --- stage exit gates (mechanical part only)
    if status == "stage-complete":
        needed = {
            "ground": ["SPEC.md", "CURRENT_STATE.md"],
            "shape": ["SPEC.md", "CURRENT_STATE.md", "ARCHITECTURE.md", "PLAN.md"],
            "execute": ["PLAN.md"],
        }.get(stage, [])
        for name in needed:
            if artifacts.get(name) in UNSETTLED:
                errors.append(f"STATUS.md: {stage} is stage-complete but {name} is {artifacts[name]}")
        if stage == "shape" and not any(s["status"] in {"ready", "in-progress"} for s in slices.values()):
            errors.append("PLAN.md: shape is stage-complete but no slice is ready")
    if status == "done":
        open_slices = [sid for sid, s in slices.items() if s["status"] not in {"done", "dropped"}]
        if open_slices:
            errors.append(f"STATUS.md: status is done but slices are not done/dropped: {', '.join(open_slices)}")

    for e in errors:
        print(f"ERROR: {e}")
    for w in warnings:
        print(f"WARN: {w}")
    if errors:
        return 1
    print(f"OK: {root} is structurally consistent ({len(slices)} slice(s), {len(warnings)} warning(s))")
    return 0


if __name__ == "__main__":
    sys.exit(main())
