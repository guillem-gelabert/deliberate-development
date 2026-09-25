#!/usr/bin/env python3
"""Append-only estimate-vs-actual log for deliberate-development (schema 1).

Log file, first match wins:
    --file PATH
    $DELIBERATE_DEV_CALIBRATION
    ~/.deliberate-development/calibration.jsonl

Commands:
    calibration.py path
    calibration.py append --project P --task T --slice S1 --estimator E \\
                          --estimate-hours 8 --actual-hours 12.5 \\
                          [--calibrated-hours 13] [--novel] [--includes TEXT] [--note TEXT] [--correction]
    calibration.py summary [--estimator E] [--project P] [--months 6]

append writes one JSON line and never rewrites or deletes existing lines. A second
record for the same (project, task, slice) is refused unless --correction is given;
summary then uses the latest record for that key. summary only does arithmetic on
recorded numbers: it does not produce an estimate.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import statistics
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

SCHEMA = 1
MIN_HISTORY = 6  # Spolsky: assume the worst until about six tasks are recorded
DEFAULT = Path.home() / ".deliberate-development" / "calibration.jsonl"


def log_path(arg: str | None) -> Path:
    if arg:
        return Path(arg).expanduser()
    env = os.environ.get("DELIBERATE_DEV_CALIBRATION")
    return Path(env).expanduser() if env else DEFAULT


def read(path: Path) -> tuple[list[dict], int]:
    """Valid schema-1 records and the number of unreadable lines."""
    if not path.exists():
        return [], 0
    records, bad = [], 0
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        try:
            r = json.loads(line)
            if r.get("schema") != SCHEMA or not all(k in r for k in ("project", "task_id", "slice_id", "velocity")):
                raise ValueError
            records.append(r)
        except (ValueError, AttributeError):
            bad += 1
    return records, bad


def key(r: dict) -> tuple[str, str, str]:
    return r["project"], r["task_id"], r["slice_id"]


def positive(value: str) -> float:
    v = float(value)
    if not v > 0:
        raise argparse.ArgumentTypeError("must be > 0")
    return v


def nonempty(value: str) -> str:
    if not value.strip():
        raise argparse.ArgumentTypeError("must not be empty")
    return value.strip()


def slice_id(value: str) -> str:
    if not re.fullmatch(r"S\d+", value):
        raise argparse.ArgumentTypeError("slice id must look like S1, S2, ...")
    return value


def cmd_append(a: argparse.Namespace, path: Path) -> int:
    records, bad = read(path)
    k = (a.project, a.task, a.slice)
    if any(key(r) == k for r in records) and not a.correction:
        print(f"ERROR: {path} already has a record for {'/'.join(k)}; pass --correction to supersede it", file=sys.stderr)
        return 3
    record = {
        "schema": SCHEMA,
        "recorded_at": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
        "project": a.project,
        "task_id": a.task,
        "slice_id": a.slice,
        "estimator": a.estimator,
        "estimate_hours": a.estimate_hours,
        "calibrated_hours": a.calibrated_hours,
        "actual_hours": a.actual_hours,
        "velocity": round(a.estimate_hours / a.actual_hours, 3),
        "novel": a.novel,
        "includes": a.includes,
        "note": a.note,
        "corrects": a.correction,
    }
    path.parent.mkdir(mode=0o700, parents=True, exist_ok=True)
    line = json.dumps(record, ensure_ascii=False) + "\n"
    fd = os.open(path, os.O_WRONLY | os.O_APPEND | os.O_CREAT, 0o600)
    try:
        os.write(fd, line.encode("utf-8"))
    finally:
        os.close(fd)
    if bad:
        print(f"WARN: {path} has {bad} unreadable line(s); left untouched", file=sys.stderr)
    print(f"Appended to {path}: {'/'.join(k)} velocity {record['velocity']}")
    return 0


def cmd_summary(a: argparse.Namespace, path: Path) -> int:
    records, bad = read(path)
    latest: dict[tuple, dict] = {}
    for r in records:  # file order is append order; later records supersede earlier ones
        latest[key(r)] = r
    cutoff = datetime.now(timezone.utc) - timedelta(days=round(a.months * 30.44))
    rows = []
    for r in latest.values():
        try:
            when = datetime.fromisoformat(r["recorded_at"])
        except (KeyError, ValueError, TypeError):
            continue
        if when.tzinfo is None:  # hand-added record without an offset: treat as UTC
            when = when.replace(tzinfo=timezone.utc)
        if when < cutoff:
            continue
        if a.estimator and r.get("estimator") != a.estimator:
            continue
        if a.project and r.get("project") != a.project:
            continue
        rows.append(r)

    scope = ", ".join(f"{n}={v}" for n, v in (("estimator", a.estimator), ("project", a.project)) if v) or "all estimators"
    print(f"Log: {path}")
    print(f"Window: last {a.months:g} months; filter: {scope}")
    if bad:
        print(f"WARN: {bad} unreadable line(s) ignored")
    if not a.estimator:
        estimators = sorted({r.get("estimator", "?") for r in rows})
        if len(estimators) > 1:
            print(f"WARN: mixes estimators {estimators}; velocity is personal, pass --estimator")
    n = len(rows)
    print(f"Records: {n}")
    if n == 0:
        print("History: none. Assume the worst: give a pessimistic range and say there is no history.")
        return 0
    v = sorted(r["velocity"] for r in rows)
    print(f"Velocity (estimate/actual): min {v[0]:.2f}  median {statistics.median(v):.2f}  max {v[-1]:.2f}")
    print(f"Implied factor on raw estimates (1/median): {1 / statistics.median(v):.2f}x")
    novel = [r["velocity"] for r in rows if r.get("novel")]
    if novel:
        print(f"Novel-work records: {len(novel)}, median velocity {statistics.median(novel):.2f}")
    if n < MIN_HISTORY:
        print(f"History: insufficient ({n} < {MIN_HISTORY}). Treat the factor as weak and lean pessimistic.")
    return 0


def main() -> int:
    p = argparse.ArgumentParser(description="Append-only estimate-vs-actual log (schema 1).")
    p.add_argument("--file", help="log file (default: $DELIBERATE_DEV_CALIBRATION or ~/.deliberate-development/calibration.jsonl)")
    sub = p.add_subparsers(dest="cmd", required=True)
    sub.add_parser("path", help="print the resolved log path")
    ap = sub.add_parser("append", help="append one completed slice")
    ap.add_argument("--project", required=True, type=nonempty)
    ap.add_argument("--task", required=True, type=nonempty)
    ap.add_argument("--slice", required=True, type=slice_id)
    ap.add_argument("--estimator", required=True, type=nonempty, help="who produced the estimate (person or model id)")
    ap.add_argument("--estimate-hours", required=True, type=positive, help="raw estimate before calibration")
    ap.add_argument("--actual-hours", required=True, type=positive, help="measured elapsed time; never invented")
    ap.add_argument("--calibrated-hours", type=positive)
    ap.add_argument("--novel", action="store_true", help="slice involved work new to the estimator")
    ap.add_argument("--includes", type=nonempty, help="what the actual includes (bug fixes, interruptions)")
    ap.add_argument("--note", type=nonempty)
    ap.add_argument("--correction", action="store_true", help="supersede an existing record for the same slice")
    sp = sub.add_parser("summary", help="velocity statistics from recorded history")
    sp.add_argument("--estimator")
    sp.add_argument("--project")
    sp.add_argument("--months", type=positive, default=6.0)
    for sp_ in (ap, sp):  # allow --file after the subcommand too
        sp_.add_argument("--file", dest="file_sub", help=argparse.SUPPRESS)
    a = p.parse_args()
    path = log_path(getattr(a, "file_sub", None) or a.file)
    if a.cmd == "path":
        print(path)
        return 0
    return cmd_append(a, path) if a.cmd == "append" else cmd_summary(a, path)


if __name__ == "__main__":
    sys.exit(main())
