"""One Line to Your Younger Self — make.fun entry.

Reads the single line from entry.txt (next to this file), validates it
against the bounty gate (1-200 characters, one line, not only
whitespace), writes it to $MAKEFUN_OUTPUT_DIR/entry.txt for the judge,
and prints it.
"""

import os
import sys
from pathlib import Path

MAX_CHARS = 200


def load_line() -> str:
    path = Path(__file__).with_name("entry.txt")
    text = path.read_text(encoding="utf-8")
    line = text.strip()
    return line


def output_dir() -> Path:
    """Where the judge reads the entry: $MAKEFUN_OUTPUT_DIR, else /output."""
    raw = os.environ.get("MAKEFUN_OUTPUT_DIR", "").strip()
    return Path(raw) if raw else Path("/output")


def validate(line: str) -> None:
    if not line:
        raise ValueError("entry is empty")
    if len(line) > MAX_CHARS:
        raise ValueError(f"entry is {len(line)} chars, over the 200 limit")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    bad = [ch for ch in line if ord(ch) < 0x20 and ch not in ("\t",)]
    if bad:
        raise ValueError(f"entry holds control characters: {bad!r}")


def main() -> int:
    line = load_line()
    validate(line)
    out_dir = output_dir()
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(line + "\n", encoding="utf-8")
    print(line)
    return 0


if __name__ == "__main__":
    sys.exit(main())
