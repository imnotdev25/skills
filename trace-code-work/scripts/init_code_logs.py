#!/usr/bin/env python3
"""Create missing daily trace-code-work logs without overwriting existing logs."""

from __future__ import annotations

import argparse
from datetime import date
from pathlib import Path


LOG_NAMES = ("DECISIONS.md", "FLOW.md", "EXPLORE.md", "QUIZ.md")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, required=True, help="Project root")
    parser.add_argument("--date", default=date.today().isoformat(), help="YYYY-MM-DD")
    return parser.parse_args()


def validate_date(value: str) -> str:
    try:
        return date.fromisoformat(value).isoformat()
    except ValueError as error:
        raise SystemExit(f"Invalid --date {value!r}; expected YYYY-MM-DD") from error


def initialize(root: Path, log_date: str) -> tuple[Path, list[Path], list[Path]]:
    project_root = root.expanduser().resolve()
    if not project_root.is_dir():
        raise SystemExit(f"Project root is not a directory: {project_root}")

    assets = Path(__file__).resolve().parent.parent / "assets"
    target = project_root / "code-logs" / log_date
    target.mkdir(parents=True, exist_ok=True)
    created: list[Path] = []
    preserved: list[Path] = []

    for name in LOG_NAMES:
        destination = target / name
        if destination.exists():
            preserved.append(destination)
            continue
        template = assets / name
        if not template.is_file():
            raise SystemExit(f"Missing template: {template}")
        destination.write_text(
            template.read_text(encoding="utf-8").replace("{{DATE}}", log_date),
            encoding="utf-8",
        )
        created.append(destination)

    return target, created, preserved


def main() -> None:
    args = parse_args()
    target, created, preserved = initialize(args.root, validate_date(args.date))
    print(f"Log directory: {target}")
    for path in created:
        print(f"created: {path.name}")
    for path in preserved:
        print(f"preserved: {path.name}")


if __name__ == "__main__":
    main()
