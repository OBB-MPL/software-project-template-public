#!/usr/bin/env python3
"""Check tracked working-tree text files without third-party dependencies."""

from pathlib import Path
import re
import subprocess
import sys


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    result = subprocess.run(
        ["git", "ls-files", "-z"], cwd=root, check=True, capture_output=True
    )
    failures = []
    checked = 0
    conflict = re.compile(r"^(?:<{7}|={7}|>{7}|\|{7})(?:\s|$)")
    for raw_path in result.stdout.split(b"\0"):
        if not raw_path:
            continue
        relative = raw_path.decode("utf-8", errors="surrogateescape")
        path = root / relative
        if path.is_symlink() or not path.is_file():
            continue
        data = path.read_bytes()
        if b"\0" in data:
            continue
        try:
            content = data.decode("utf-8")
        except UnicodeDecodeError:
            continue
        checked += 1
        for number, line in enumerate(content.splitlines(), 1):
            if conflict.match(line):
                failures.append(f"{relative}:{number}: unresolved conflict marker")
            trimmed = line.rstrip(" \t")
            trailing = line[len(trimmed):]
            markdown_break = path.suffix.lower() == ".md" and trailing == "  " and trimmed
            if trailing and not markdown_break:
                failures.append(f"{relative}:{number}: trailing whitespace")
    if failures:
        print("\n".join(failures), file=sys.stderr)
        return 1
    print(f"Repository checks passed ({checked} text files).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
