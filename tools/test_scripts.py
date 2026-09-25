#!/usr/bin/env python3
"""Smoke tests for the skills' runtime scripts (init_work.py, validate_work.py).

Run: python3 tools/test_scripts.py
"""
from __future__ import annotations

import subprocess
import sys
import tempfile
import textwrap
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILLS = ("ground", "shape", "execute", "state")
INIT = ROOT / "skills" / "ground" / "scripts" / "init_work.py"
INITS = [ROOT / "skills" / s / "scripts" / "init_work.py" for s in ("ground", "state")]
VALIDATORS = [ROOT / "skills" / s / "scripts" / "validate_work.py" for s in SKILLS]
VALIDATE = VALIDATORS[0]
CALIB = ROOT / "skills" / "execute" / "scripts" / "calibration.py"


def run(*args: str | Path, cwd: Path | None = None) -> subprocess.CompletedProcess:
    return subprocess.run([sys.executable, *map(str, args)], cwd=cwd, capture_output=True, text=True)


STATUS = """\
---
stage: {stage}
step: {step}
status: {status}
current_slice: {current}
updated: 2026-09-25
---

# Status

## Artifact state

- SPEC.md: {spec}
- CURRENT_STATE.md: {cs}
- ARCHITECTURE.md: {arch}
- PLAN.md: {plan}

## Open

- None recorded yet.

## Next

{next}
"""

SLICE = """\
## {sid} — Owner deletes their own comment

**Status:** {status}

**Behavior**
Given an owner, when they delete, then the comment is gone.

**Done when**
{boxes}

**Implementation notes**
{notes}
"""


def workspace(tmp: Path, *, stage="execute", step="implement", status="in-progress", current="S1",
              spec="complete", cs="complete", arch="complete", plan="draft",
              next_action="Make the non-owner 403 test pass in tests/comments.spec.ts, then check S1's second box.",
              slices: list[dict] | None = None, discovered="- [ ] D1 — something (found during S1; blocking: no)") -> Path:
    ws = tmp / "ws"
    ws.mkdir(exist_ok=True)
    (ws / "STATUS.md").write_text(STATUS.format(stage=stage, step=step, status=status, current=current, spec=spec,
                                                cs=cs, arch=arch, plan=plan, next=next_action))
    for name in ("SPEC.md", "CURRENT_STATE.md", "ARCHITECTURE.md"):
        (ws / name).write_text(f"# {name}\n")
    if slices is None:
        slices = [{"sid": "S1", "status": "in-progress", "boxes": "- [x] owner delete\n- [ ] non-owner 403"}]
    body = "".join(SLICE.format(notes=s.get("notes", ""), **{k: v for k, v in s.items() if k != "notes"}) + "\n" for s in slices)
    (ws / "PLAN.md").write_text(f"# Plan\n\n## Slices\n\n{body}## Discovered work\n\n{discovered}\n")
    return ws


class InitWork(unittest.TestCase):
    def test_creates_five_files_that_validate(self):
        with tempfile.TemporaryDirectory() as d:
            r = run(INIT, "PROJ-1", cwd=Path(d))
            self.assertEqual(r.returncode, 0, r.stderr)
            ws = Path(d) / ".work" / "PROJ-1"
            self.assertEqual(sorted(p.name for p in ws.iterdir()),
                             ["ARCHITECTURE.md", "CURRENT_STATE.md", "PLAN.md", "SPEC.md", "STATUS.md"])
            self.assertNotIn("{{DATE}}", (ws / "STATUS.md").read_text())
            v = run(VALIDATE, ws)
            self.assertEqual(v.returncode, 0, v.stdout)

    def test_never_overwrites(self):
        with tempfile.TemporaryDirectory() as d:
            run(INIT, "t", cwd=Path(d))
            spec = Path(d) / ".work" / "t" / "SPEC.md"
            spec.write_text("my work")
            r = run(INIT, "t", cwd=Path(d))
            self.assertEqual(r.returncode, 0)
            self.assertEqual(spec.read_text(), "my work")

    def test_partial_workspace_refused_then_filled(self):
        with tempfile.TemporaryDirectory() as d:
            run(INIT, "t", cwd=Path(d))
            ws = Path(d) / ".work" / "t"
            (ws / "PLAN.md").unlink()
            (ws / "SPEC.md").write_text("keep")
            r = run(INIT, "t", cwd=Path(d))
            self.assertEqual(r.returncode, 2)
            self.assertFalse((ws / "PLAN.md").exists())
            r = run(INIT, "t", "--fill-missing", cwd=Path(d))
            self.assertEqual(r.returncode, 0, r.stderr)
            self.assertTrue((ws / "PLAN.md").exists())
            self.assertEqual((ws / "SPEC.md").read_text(), "keep")

    def test_rejects_unsafe_task_id(self):
        with tempfile.TemporaryDirectory() as d:
            for bad in ("../x", "a/b", ".hidden", ""):
                self.assertNotEqual(run(INIT, bad, cwd=Path(d)).returncode, 0, bad)

    def test_state_copy_is_standalone(self):
        # state initializes from its own templates, so it installs without ground
        with tempfile.TemporaryDirectory() as d:
            r = run(INITS[1], "ADOPT-1", cwd=Path(d))
            self.assertEqual(r.returncode, 0, r.stderr)
            v = run(VALIDATORS[3], Path(d) / ".work" / "ADOPT-1")
            self.assertEqual(v.returncode, 0, v.stdout)

    def test_custom_root(self):
        with tempfile.TemporaryDirectory() as d:
            r = run(INIT, "t", "--root", "docs/tasks", cwd=Path(d))
            self.assertEqual(r.returncode, 0, r.stderr)
            self.assertTrue((Path(d) / "docs" / "tasks" / "t" / "STATUS.md").exists())


class ValidateWork(unittest.TestCase):
    def check(self, ws: Path, ok: bool, contains: str | None = None):
        r = run(VALIDATE, ws)
        self.assertEqual(r.returncode == 0, ok, r.stdout)
        if contains:
            self.assertIn(contains, r.stdout)
        return r

    def test_valid_execution_state(self):
        with tempfile.TemporaryDirectory() as d:
            self.check(workspace(Path(d)), True, "OK")

    def test_legacy_stage_name_warns(self):
        with tempfile.TemporaryDirectory() as d:
            self.check(workspace(Path(d), stage="execute-work"), True, "legacy stage 'execute-work'")

    def test_missing_file(self):
        with tempfile.TemporaryDirectory() as d:
            ws = workspace(Path(d))
            (ws / "CURRENT_STATE.md").unlink()
            self.check(ws, False, "missing")

    def test_unparseable_frontmatter(self):
        with tempfile.TemporaryDirectory() as d:
            ws = workspace(Path(d))
            (ws / "STATUS.md").write_text("# Status\nstage: ground\n")
            self.check(ws, False, "frontmatter")

    def test_unknown_values(self):
        with tempfile.TemporaryDirectory() as d:
            self.check(workspace(Path(d), stage="build-work"), False, "unknown stage")
        with tempfile.TemporaryDirectory() as d:
            self.check(workspace(Path(d), step="architecture"), False, "not valid for execute")
        with tempfile.TemporaryDirectory() as d:
            self.check(workspace(Path(d), status="paused"), False, "unknown status")
        with tempfile.TemporaryDirectory() as d:
            self.check(workspace(Path(d), arch="finished"), False, "unknown state")

    def test_duplicate_slice_ids(self):
        with tempfile.TemporaryDirectory() as d:
            s = {"sid": "S1", "status": "in-progress", "boxes": "- [ ] a"}
            self.check(workspace(Path(d), slices=[s, dict(s, status="ready")]), False, "duplicate slice id S1")

    def test_current_slice_must_exist(self):
        with tempfile.TemporaryDirectory() as d:
            ws = workspace(Path(d), current="S9", slices=[{"sid": "S1", "status": "ready", "boxes": "- [ ] a"}])
            self.check(ws, False, "S9 does not exist")

    def test_current_slice_status_incompatible_with_execution(self):
        with tempfile.TemporaryDirectory() as d:
            ws = workspace(Path(d), slices=[{"sid": "S1", "status": "not-ready", "boxes": "- [ ] a"}])
            self.check(ws, False, "expected ready or in-progress")

    def test_execution_requires_current_slice(self):
        with tempfile.TemporaryDirectory() as d:
            ws = workspace(Path(d), current="", slices=[{"sid": "S1", "status": "ready", "boxes": "- [ ] a"}])
            self.check(ws, False, "current_slice is empty")

    def test_one_in_progress_slice(self):
        with tempfile.TemporaryDirectory() as d:
            ws = workspace(Path(d), slices=[{"sid": "S1", "status": "in-progress", "boxes": "- [ ] a"},
                                            {"sid": "S2", "status": "in-progress", "boxes": "- [ ] b"}])
            self.check(ws, False, "more than one slice in-progress")

    def test_done_slice_with_unchecked_box(self):
        with tempfile.TemporaryDirectory() as d:
            ws = workspace(Path(d), slices=[{"sid": "S1", "status": "done", "boxes": "- [x] a\n- [ ] b"},
                                            {"sid": "S2", "status": "in-progress", "boxes": "- [ ] c"}], current="S2")
            self.check(ws, False, "unchecked")

    def test_ready_slice_needs_done_when(self):
        with tempfile.TemporaryDirectory() as d:
            ws = workspace(Path(d), slices=[{"sid": "S1", "status": "in-progress", "boxes": "(none yet)"}])
            self.check(ws, False, "no '**Done when**' checkboxes")

    def test_plan_not_started_but_has_slices(self):
        with tempfile.TemporaryDirectory() as d:
            ws = workspace(Path(d), stage="shape", step="slicing", current="", plan="not-started",
                           slices=[{"sid": "S1", "status": "candidate", "boxes": ""}])
            self.check(ws, False, "PLAN.md is not-started")

    def test_shape_stage_complete_requires_ready_slice(self):
        with tempfile.TemporaryDirectory() as d:
            ws = workspace(Path(d), stage="shape", step="handoff", status="stage-complete", current="",
                           slices=[{"sid": "S1", "status": "not-ready", "boxes": "- [ ] a"}])
            self.check(ws, False, "no slice is ready")

    def test_ground_stage_complete_requires_settled_artifacts(self):
        with tempfile.TemporaryDirectory() as d:
            ws = workspace(Path(d), stage="ground", step="handoff", status="stage-complete", current="",
                           cs="draft", arch="not-started", plan="not-started", slices=[])
            self.check(ws, False, "CURRENT_STATE.md is draft")

    def test_task_done_requires_all_slices_closed(self):
        with tempfile.TemporaryDirectory() as d:
            ws = workspace(Path(d), status="done", current="",
                           slices=[{"sid": "S1", "status": "done", "boxes": "- [x] a"},
                                   {"sid": "S2", "status": "ready", "boxes": "- [ ] b"}])
            self.check(ws, False, "not done/dropped: S2")

    def test_empty_next_is_error_vague_next_is_warning(self):
        with tempfile.TemporaryDirectory() as d:
            self.check(workspace(Path(d), next_action=""), False, "'## Next' is empty")
        with tempfile.TemporaryDirectory() as d:
            self.check(workspace(Path(d), next_action="Continue architecture."), True, "WARN")

    def test_done_with_estimate_but_no_actual_warns(self):
        with tempfile.TemporaryDirectory() as d:
            ws = workspace(Path(d), slices=[
                {"sid": "S1", "status": "done", "boxes": "- [x] a", "notes": "**Estimate:** 2h raw"},
                {"sid": "S2", "status": "in-progress", "boxes": "- [ ] b"}], current="S2")
            self.check(ws, True, "no Actual")

    def test_updated_must_be_iso_date(self):
        with tempfile.TemporaryDirectory() as d:
            ws = workspace(Path(d))
            s = ws / "STATUS.md"
            s.write_text(s.read_text().replace("updated: 2026-09-25", "updated: yesterday"))
            self.check(ws, False, "expected an ISO date")

    def test_stale_cursor_warnings(self):
        # all boxes checked but still in-progress
        with tempfile.TemporaryDirectory() as d:
            ws = workspace(Path(d), slices=[{"sid": "S1", "status": "in-progress", "boxes": "- [x] a\n- [x] b"}])
            self.check(ws, True, "every 'Done when' box is checked")
        # cursor says shaping while a slice is being executed
        with tempfile.TemporaryDirectory() as d:
            ws = workspace(Path(d), stage="shape", step="slicing", current="S1")
            self.check(ws, True, "the cursor or the slice state is stale")
        # executing on top of a stale architecture
        with tempfile.TemporaryDirectory() as d:
            self.check(workspace(Path(d), arch="stale"), True, "executing while ARCHITECTURE.md is stale")

    def test_review_needed_execution_prompts_reconciliation(self):
        with tempfile.TemporaryDirectory() as d:
            self.check(workspace(Path(d), arch="review-needed"), True,
                       "ARCHITECTURE.md is review-needed; reconcile the sections S1 depends on")

    def test_does_not_modify_files(self):
        with tempfile.TemporaryDirectory() as d:
            ws = workspace(Path(d), stage="nope")
            before = {p.name: p.read_bytes() for p in ws.iterdir()}
            run(VALIDATE, ws)
            self.assertEqual(before, {p.name: p.read_bytes() for p in ws.iterdir()})

    def test_shared_script_copies_identical(self):
        self.assertEqual(len({p.read_bytes() for p in VALIDATORS}), 1, "validate_work.py differs between skills")
        self.assertEqual(len({p.read_bytes() for p in INITS}), 1, "init_work.py differs between skills")


class Calibration(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.log = Path(self.tmp.name) / "nested" / "calibration.jsonl"

    def tearDown(self):
        self.tmp.cleanup()

    def append(self, slice_id="S1", est="8", act="10", *extra):
        return run(CALIB, "--file", self.log, "append", "--project", "shop", "--task", "ORD-12", "--slice", slice_id,
                   "--estimator", "claude-opus-5-5", "--estimate-hours", est, "--actual-hours", act, *extra)

    def test_append_creates_file_and_valid_record(self):
        r = self.append()
        self.assertEqual(r.returncode, 0, r.stderr)
        import json
        rec = json.loads(self.log.read_text().splitlines()[0])
        self.assertEqual(rec["schema"], 1)
        self.assertEqual(rec["velocity"], 0.8)
        self.assertEqual(rec["corrects"], False)
        self.assertEqual(oct(self.log.stat().st_mode & 0o777), "0o600")

    def test_duplicate_refused_correction_appended(self):
        self.append()
        r = self.append(act="12")
        self.assertEqual(r.returncode, 3)
        self.assertEqual(len(self.log.read_text().splitlines()), 1)
        r = self.append("S1", "8", "16", "--correction")
        self.assertEqual(r.returncode, 0, r.stderr)
        lines = self.log.read_text().splitlines()
        self.assertEqual(len(lines), 2)
        s = run(CALIB, "--file", self.log, "summary")
        self.assertIn("Records: 1", s.stdout)
        self.assertIn("median 0.50", s.stdout)

    def test_append_never_rewrites_existing_lines(self):
        self.log.parent.mkdir(parents=True)
        self.log.write_text("not json\n")
        self.assertEqual(self.append().returncode, 0)
        self.assertEqual(self.log.read_text().splitlines()[0], "not json")

    def test_rejects_invalid_input(self):
        self.assertNotEqual(self.append(act="0").returncode, 0)
        self.assertNotEqual(self.append(slice_id="slice-1").returncode, 0)
        self.assertFalse(self.log.exists())

    def test_summary_flags_insufficient_history_and_empty_log(self):
        s = run(CALIB, "--file", self.log, "summary")
        self.assertEqual(s.returncode, 0)
        self.assertIn("History: none", s.stdout)
        for i in range(3):
            self.append(f"S{i + 1}", "6", "10")
        s = run(CALIB, "--file", self.log, "summary", "--estimator", "claude-opus-5-5")
        self.assertIn("Records: 3", s.stdout)
        self.assertIn("insufficient", s.stdout)
        self.assertIn("1.67x", s.stdout)

    def test_summary_ignores_records_older_than_window(self):
        import json
        self.append("S1", "5", "10")
        old = json.loads(self.log.read_text())
        old.update(slice_id="S2", recorded_at="2020-01-01T00:00:00+00:00", velocity=0.1)
        with open(self.log, "a") as fh:
            fh.write(json.dumps(old) + "\n")
        s = run(CALIB, "--file", self.log, "summary")
        self.assertIn("Records: 1", s.stdout)

    def test_summary_treats_naive_recorded_at_as_utc(self):
        import json
        self.append("S1", "5", "10")
        rec = json.loads(self.log.read_text())
        rec.update(slice_id="S2", recorded_at="2099-01-01T00:00:00", velocity=0.5)
        with open(self.log, "a") as fh:
            fh.write(json.dumps(rec) + "\n")
        s = run(CALIB, "--file", self.log, "summary")
        self.assertEqual(s.returncode, 0, s.stderr)
        self.assertIn("Records: 2", s.stdout)

    def test_env_var_selects_file(self):
        import os
        env = dict(os.environ, DELIBERATE_DEV_CALIBRATION=str(self.log))
        r = subprocess.run([sys.executable, str(CALIB), "path"], capture_output=True, text=True, env=env)
        self.assertEqual(r.stdout.strip(), str(self.log))


if __name__ == "__main__":
    unittest.main(verbosity=1)
