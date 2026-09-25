#!/usr/bin/env python3
"""Validate the five skills, run script smoke tests, and optionally package them.

Usage:
    python3 tools/check.py              # checks + smoke tests
    python3 tools/check.py --package    # ...then write dist/dd-<skill>.zip

Checks:
- SKILL.md frontmatter (name = folder, description length, no angle brackets, allowed keys)
- the official skill-creator quick_validate.py, when found (set SKILL_CREATOR_DIR to override)
- agents/openai.yaml short_description length (25-64 chars)
- every references/, scripts/, assets/ path named in SKILL.md or a reference exists, and every
  reference is named in SKILL.md
- shared files are byte-identical in every skill that ships them (see SHARED)
- workflow vocabulary used in runtime Markdown (stage/step pairs, `status: x`, `step: x`,
  `**Status:** x`, artifact states) matches the values validate_work.py accepts
- no runtime file points into this repository (research/, docs/, evals/)
- dist/dd-<skill>.zip holds exactly the current skills/<skill> files (fresh, byte-identical)
"""
from __future__ import annotations

import importlib.util
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
WORKFLOW = ["ground", "shape", "execute", "state"]  # share the task-state contract and validator
SKILLS = WORKFLOW + ["help"]
TEMPLATES = [f"assets/templates/{n}" for n in ("STATUS.md", "SPEC.md", "CURRENT_STATE.md", "ARCHITECTURE.md", "PLAN.md")]
# path -> skills that ship a copy; ground holds the copy to edit
SHARED = {
    "references/task-state.md": WORKFLOW,
    "scripts/validate_work.py": WORKFLOW,
    "scripts/init_work.py": ["ground", "state"],
    **{t: ["ground", "state"] for t in TEMPLATES},
}
DIST = ROOT / "dist"
EXCLUDE = {"__pycache__", ".DS_Store"}
CANDIDATE_SKILL_CREATORS = [
    Path.home() / ".claude/plugins/marketplaces/claude-plugins-official/plugins/skill-creator/skills/skill-creator",
    Path.home() / ".codex/skills/.system/skill-creator",
]


def skill_creator_dir() -> Path | None:
    env = os.environ.get("SKILL_CREATOR_DIR")
    for c in ([Path(env)] if env else []) + CANDIDATE_SKILL_CREATORS:
        if (c / "scripts" / "quick_validate.py").is_file():
            return c
    return None


def frontmatter(text: str) -> dict[str, str]:
    m = re.match(r"^---\n(.*?)\n---\n", text, re.DOTALL)
    if not m:
        return {}
    out = {}
    for line in m.group(1).splitlines():
        if ":" in line and not line.startswith(" "):
            k, v = line.split(":", 1)
            out[k.strip()] = v.strip()
    return out


def check_skill(name: str, creator: Path | None) -> list[str]:
    errs: list[str] = []
    d = ROOT / "skills" / name
    text = (d / "SKILL.md").read_text(encoding="utf-8")
    fm = frontmatter(text)
    if fm.get("name") != name:
        errs.append(f"{name}: frontmatter name is {fm.get('name')!r}")
    desc = fm.get("description", "")
    if not desc or len(desc) > 1024 or "<" in desc or ">" in desc:
        errs.append(f"{name}: description missing, >1024 chars, or has angle brackets")
    extra = set(fm) - {"name", "description", "license", "allowed-tools", "metadata"}
    if extra:
        errs.append(f"{name}: unexpected frontmatter keys {sorted(extra)}")

    if creator:
        r = subprocess.run([sys.executable, str(creator / "scripts" / "quick_validate.py"), str(d)],
                           capture_output=True, text=True)
        if r.returncode != 0:
            errs.append(f"{name}: quick_validate: {(r.stdout + r.stderr).strip()}")

    oy = (d / "agents" / "openai.yaml").read_text(encoding="utf-8")
    m = re.search(r'short_description:\s*"([^"]*)"', oy)
    if not m or not 25 <= len(m.group(1)) <= 64:
        errs.append(f"{name}: agents/openai.yaml short_description must be a quoted 25-64 char string")

    path_re = re.compile(r"\b((?:references|scripts|assets/templates)/[\w./-]*[\w/])")
    named = set(path_re.findall(text))
    for rel in named:
        if not (d / rel).exists():
            errs.append(f"{name}: SKILL.md names missing path {rel}")
    for ref in (d / "references").glob("*.md"):
        if f"references/{ref.name}" not in named:
            errs.append(f"{name}: references/{ref.name} is never named in SKILL.md")
        for rel in set(path_re.findall(ref.read_text(encoding="utf-8"))):
            if not (d / rel).exists():
                errs.append(f"{name}: references/{ref.name} names missing path {rel}")

    for f in d.rglob("*"):
        if f.is_file() and f.suffix in {".md", ".py", ".yaml"}:
            body = f.read_text(encoding="utf-8")
            if re.search(r"(?<![\w.])(research|docs|evals)/(sources|extractions|synthesis|scenarios|[\w-]+\.md)", body):
                errs.append(f"{name}: {f.relative_to(d)} points into the source repository")
    return errs


def check_shared() -> list[str]:
    errs = []
    for rel, owners in SHARED.items():
        missing = [s for s in owners if not (ROOT / "skills" / s / rel).is_file()]
        if missing:
            errs.append(f"shared file {rel} missing in {missing}")
            continue
        copies = {s: (ROOT / "skills" / s / rel).read_bytes() for s in owners}
        if len(set(copies.values())) != 1:
            errs.append(f"shared file {rel} differs between skills {owners}; edit the ground copy and copy it across")
    return errs


def check_distribution() -> list[str]:
    """Both plugin catalogs must point at this root and its five canonical skills."""
    errors: list[str] = []
    def read_json(path: Path) -> dict:
        try:
            value = json.loads(path.read_text(encoding="utf-8"))
            if isinstance(value, dict):
                return value
            errors.append(f"{path.relative_to(ROOT)}: expected a JSON object")
        except (OSError, ValueError) as exc:
            errors.append(f"{path.relative_to(ROOT)}: {exc}")
        return {}

    portable = read_json(ROOT / "plugin.json")
    claude = read_json(ROOT / ".claude-plugin/plugin.json")
    codex_market = read_json(ROOT / ".agents/plugins/marketplace.json")
    claude_market = read_json(ROOT / ".claude-plugin/marketplace.json")
    if portable.get("$schema") != "https://agent-plugins.org/schemas/1.0.0/plugin.schema.json":
        errors.append("plugin.json: expected portable Agent Plugins schema")
    if portable.get("name") != "dd" or claude.get("name") != portable.get("name"):
        errors.append("plugin manifests: plugin names differ")
    if portable.get("version") != claude.get("version"):
        errors.append("plugin manifests: versions differ")
    if sorted(p.name for p in (ROOT / "skills").iterdir() if p.is_dir()) != sorted(SKILLS):
        errors.append("skills/: expected exactly the five canonical skill directories")
    for name in SKILLS:
        if not (ROOT / "skills" / name / "SKILL.md").is_file():
            errors.append(f"skills/{name}/SKILL.md is missing")
    for directory in (ROOT / ".claude-plugin", ROOT / ".agents/plugins"):
        if any(directory.rglob("SKILL.md")) or any(directory.rglob("task-state.md")):
            errors.append(f"{directory.relative_to(ROOT)} contains a methodology copy")

    entries = [("Codex", codex_market), ("Claude", claude_market)]
    for label, catalog in entries:
        plugins = catalog.get("plugins")
        if not isinstance(plugins, list) or len(plugins) != 1:
            errors.append(f"{label} marketplace: expected one plugin entry")
            continue
        entry = plugins[0]
        if entry.get("name") != portable.get("name"):
            errors.append(f"{label} marketplace: entry name differs from plugin")
        source = entry.get("source")
        if label == "Codex":
            if not isinstance(source, dict) or source.get("source") != "local":
                errors.append("Codex marketplace: expected local source")
                continue
            source = source.get("path")
        if not isinstance(source, str) or not source.startswith("./") or (ROOT / source).resolve() != ROOT:
            errors.append(f"{label} marketplace: source must resolve to canonical repository root")
    return errors


def check_dist() -> list[str]:
    """Each dist/dd-<skill>.zip must hold exactly the current skills/<skill> files, byte-identical."""
    errs = []
    for name in SKILLS:
        target = DIST / f"dd-{name}.zip"
        if not target.is_file():
            errs.append(f"dist/dd-{name}.zip is missing; run tools/check.py --package")
            continue
        src = ROOT / "skills" / name
        expected = {str(f.relative_to(src.parent)): f for f in src.rglob("*")
                    if f.is_file() and not EXCLUDE & set(f.parts)}
        with zipfile.ZipFile(target) as z:
            names = set(z.namelist())
            for rel in sorted(names - expected.keys()):
                errs.append(f"dist/dd-{name}.zip: {rel} is not in skills/; rebuild with --package")
            for rel in sorted(expected.keys() - names):
                errs.append(f"dist/dd-{name}.zip: missing {rel}; rebuild with --package")
            for rel in sorted(expected.keys() & names):
                if z.read(rel) != expected[rel].read_bytes():
                    errs.append(f"dist/dd-{name}.zip: {rel} differs from skills/{rel}; rebuild with --package")
    return errs


def vocabulary() -> dict:
    spec = importlib.util.spec_from_file_location("validate_work", ROOT / "skills/ground/scripts/validate_work.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return {"steps": mod.STEPS, "statuses": mod.STATUSES, "artifacts": mod.ARTIFACT_STATES, "slices": mod.SLICE_STATES}


def check_vocabulary() -> list[str]:
    """All skills must use the state vocabulary that validate_work.py enforces."""
    v = vocabulary()
    all_steps = set().union(*v["steps"].values())
    checks = [
        (re.compile(r"`step: ([a-z-]+)`"), all_steps, "step"),
        (re.compile(r"`status: ([a-z-]+)`"), v["statuses"], "status"),
        (re.compile(r"^\*\*Status:\*\* `?([a-z-]+)`?", re.M), v["slices"], "slice status"),
        (re.compile(r"`(?:SPEC|CURRENT_STATE|ARCHITECTURE|PLAN)\.md`(?: to)? `([a-z-]+)`"), v["artifacts"], "artifact state"),
    ]
    stage_step = re.compile(r"`(ground|shape|execute)` / `([a-z-]+)`")
    errs = []
    for s in SKILLS:
        for f in sorted((ROOT / "skills" / s).rglob("*.md")):
            body = f.read_text(encoding="utf-8")
            where = f"{s}/{f.relative_to(ROOT / 'skills' / s)}"
            for rx, allowed, kind in checks:
                for word in rx.findall(body):
                    if word not in allowed:
                        errs.append(f"{where}: unknown {kind} '{word}'")
            for stage, step in stage_step.findall(body):
                if step not in v["steps"][stage]:
                    errs.append(f"{where}: step '{step}' is not a {stage} step")
    return errs


def package(creator: Path | None) -> list[Path]:
    DIST.mkdir(exist_ok=True)
    out = []
    for name in SKILLS:
        src = ROOT / "skills" / name
        target = DIST / f"dd-{name}.zip"
        with tempfile.TemporaryDirectory() as tmp:
            built = None
            if creator and (creator / "scripts" / "package_skill.py").is_file():
                r = subprocess.run([sys.executable, "-m", "scripts.package_skill", str(src), tmp],
                                   cwd=creator, capture_output=True, text=True)
                candidate = Path(tmp) / f"{name}.skill"
                if r.returncode == 0 and candidate.is_file():
                    built = candidate
                else:
                    print(f"  official packager failed for {name}; using built-in zip\n{r.stdout}{r.stderr}")
            if built is None:
                built = Path(tmp) / f"{name}.zip"
                with zipfile.ZipFile(built, "w", zipfile.ZIP_DEFLATED) as z:
                    for f in sorted(src.rglob("*")):
                        if f.is_file() and not EXCLUDE & set(f.parts):
                            z.write(f, f.relative_to(src.parent))
            shutil.copyfile(built, target)
        with zipfile.ZipFile(target) as z:
            roots = {n.split("/", 1)[0] for n in z.namelist()}
            if roots != {name} or f"{name}/SKILL.md" not in z.namelist():
                raise SystemExit(f"ERROR: {target} does not contain exactly one skill folder '{name}/'")
        out.append(target)
    return out


def main() -> int:
    creator = skill_creator_dir()
    print(f"skill-creator validator: {creator or 'not found (built-in checks only)'}")
    errs = check_distribution() + check_shared() + check_vocabulary()
    for s in SKILLS:
        errs += check_skill(s, creator)
    for e in errs:
        print(f"ERROR: {e}")
    if errs:
        return 1
    print("OK: plugin paths, skill structure, references, shared files, vocabulary")

    r = subprocess.run([sys.executable, str(ROOT / "tools" / "test_scripts.py")], capture_output=True, text=True)
    print((r.stdout + r.stderr).strip().splitlines()[-1])
    if r.returncode != 0:
        print(r.stdout + r.stderr)
        return 1

    if "--package" in sys.argv:
        for p in package(creator):
            with zipfile.ZipFile(p) as z:
                print(f"packaged {p.relative_to(ROOT)} ({len(z.namelist())} files)")
    # dist/ is gitignored and built on demand; check it only when a build exists
    if not DIST.is_dir():
        print("SKIP: dist/ not built (run with --package to build ZIPs)")
        return 0
    stale = check_dist()
    for e in stale:
        print(f"ERROR: {e}")
    if stale:
        return 1
    print("OK: dist ZIPs match skills/")
    return 0


if __name__ == "__main__":
    sys.exit(main())
