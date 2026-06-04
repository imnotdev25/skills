#!/usr/bin/env python3
"""
wsh — workspace hygiene CLI.

Enforces:
  - single workspace root (cwd)
  - BaseName_DD_MM_YYYY.ext naming
  - scripts under scripts/, retired files under archive/
  - no deletions; archive instead

Usage:
  python scripts/wsh.py new <base> <ext> [--kind script|data|output|root] [--root .]
  python scripts/wsh.py archive <path> [--root .]
  python scripts/wsh.py rename <path> <new_base> [--root .]
  python scripts/wsh.py audit [--root .]
"""
from __future__ import annotations

import argparse
import re
import shutil
import sys
from datetime import date
from pathlib import Path

DATE_RE = re.compile(r"_(\d{2})_(\d{2})_(\d{4})$")
SCRIPT_EXTS = {".py", ".sh", ".js", ".ts", ".tsx", ".jsx", ".mjs", ".cjs",
               ".zig", ".rs", ".go", ".rb", ".pl", ".lua", ".applescript",
               ".ps1", ".bat", ".fish", ".zsh"}
KIND_DIR = {"script": "scripts", "data": "data", "output": "outputs", "root": ""}
ARCHIVE = "archive"
PROTECTED_DIRS = {"archive", ".git", ".venv", "venv", "node_modules",
                  "__pycache__", ".mypy_cache", ".pytest_cache", ".ruff_cache",
                  ".idea", ".vscode"}


def today_suffix() -> str:
    d = date.today()
    return f"{d.day:02d}_{d.month:02d}_{d.year:04d}"


def split_base_date(stem: str) -> tuple[str, str | None]:
    """Return (base, date_suffix_or_None) for a filename stem."""
    m = DATE_RE.search(stem)
    if not m:
        return stem, None
    return stem[: m.start()], m.group(0)[1:]


def ensure_dated(stem: str) -> str:
    base, suffix = split_base_date(stem)
    return f"{base}_{suffix}" if suffix else f"{base}_{today_suffix()}"


def kind_for(path: Path) -> str:
    if path.suffix.lower() in SCRIPT_EXTS:
        return "script"
    return "root"


def cmd_new(args: argparse.Namespace) -> int:
    root = Path(args.root).resolve()
    ext = args.ext if args.ext.startswith(".") else f".{args.ext}"
    kind = args.kind or ("script" if ext.lower() in SCRIPT_EXTS else "root")
    subdir = KIND_DIR[kind]
    target_dir = root / subdir if subdir else root
    target_dir.mkdir(parents=True, exist_ok=True)
    fname = f"{args.base}_{today_suffix()}{ext}"
    path = target_dir / fname
    if path.exists():
        print(f"exists: {path}", file=sys.stderr)
        return 1
    path.touch()
    print(path)
    return 0


def cmd_archive(args: argparse.Namespace) -> int:
    root = Path(args.root).resolve()
    src = Path(args.path).resolve()
    if not src.exists():
        print(f"not found: {src}", file=sys.stderr)
        return 1
    try:
        rel = src.relative_to(root)
    except ValueError:
        print(f"refusing: {src} is outside root {root}", file=sys.stderr)
        return 1
    if rel.parts and rel.parts[0] == ARCHIVE:
        print(f"already archived: {src}", file=sys.stderr)
        return 0
    dest = root / ARCHIVE / rel
    dest.parent.mkdir(parents=True, exist_ok=True)
    if dest.exists():
        # append a disambiguator
        i = 2
        while True:
            cand = dest.with_name(f"{dest.stem}__{i}{dest.suffix}")
            if not cand.exists():
                dest = cand
                break
            i += 1
    shutil.move(str(src), str(dest))
    print(dest)
    return 0


def cmd_rename(args: argparse.Namespace) -> int:
    src = Path(args.path).resolve()
    if not src.exists():
        print(f"not found: {src}", file=sys.stderr)
        return 1
    _, suffix = split_base_date(src.stem)
    suffix = suffix or today_suffix()
    new_name = f"{args.new_base}_{suffix}{src.suffix}"
    dest = src.with_name(new_name)
    if dest.exists():
        print(f"exists: {dest}", file=sys.stderr)
        return 1
    src.rename(dest)
    print(dest)
    return 0


def iter_files(root: Path):
    for p in root.rglob("*"):
        if not p.is_file():
            continue
        if any(part in PROTECTED_DIRS for part in p.relative_to(root).parts):
            continue
        if p.name.startswith("."):
            continue
        yield p


def cmd_audit(args: argparse.Namespace) -> int:
    root = Path(args.root).resolve()
    violations: list[tuple[str, Path, str]] = []
    for p in iter_files(root):
        rel = p.relative_to(root)
        parts = rel.parts
        # rule: scripts must live in scripts/
        if p.suffix.lower() in SCRIPT_EXTS and (not parts or parts[0] != "scripts"):
            violations.append(("script_outside_scripts_dir", p,
                               f"move to {root / 'scripts' / p.name}"))
        # rule: misc files at root that look like outputs
        # rule: date suffix required
        _, suffix = split_base_date(p.stem)
        if suffix is None:
            violations.append(("missing_date_suffix", p,
                               f"rename to *_{today_suffix()}{p.suffix}"))
    if not violations:
        print("clean ✓")
        return 0
    for kind, path, hint in violations:
        print(f"{kind}\t{path}\t→ {hint}")
    print(f"\n{len(violations)} violation(s)")
    return 1


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(prog="wsh", description="Workspace hygiene CLI")
    p.add_argument("--root", default=".", help="workspace root (default: cwd)")
    sub = p.add_subparsers(dest="cmd", required=True)

    s_new = sub.add_parser("new", help="create a properly-dated file")
    s_new.add_argument("base")
    s_new.add_argument("ext")
    s_new.add_argument("--kind", choices=list(KIND_DIR.keys()))
    s_new.set_defaults(func=cmd_new)

    s_arc = sub.add_parser("archive", help="move a file under archive/")
    s_arc.add_argument("path")
    s_arc.set_defaults(func=cmd_archive)

    s_ren = sub.add_parser("rename", help="rename keeping date suffix")
    s_ren.add_argument("path")
    s_ren.add_argument("new_base")
    s_ren.set_defaults(func=cmd_rename)

    s_aud = sub.add_parser("audit", help="report rule violations")
    s_aud.set_defaults(func=cmd_audit)

    return p


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
