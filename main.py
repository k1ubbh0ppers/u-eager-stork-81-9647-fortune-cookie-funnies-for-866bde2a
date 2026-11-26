"""Fortune Cookie Funnies for Engineers — make.fun entry.

One fortune-cookie line for a software engineer, written to
``entry.txt`` once it passes a quick sanity check: a single
non-blank line of 1-120 characters, plain UTF-8 text, written
with no trailing newline.
"""

import os
import sys
from pathlib import Path

# The fortune, exactly as submitted (94 characters).
FORTUNE = "A bug you fixed last month will return, wearing a different stack trace, asking to be friends."

LIMIT = 120


def check(text: str) -> str | None:
    """Return an error message when the fortune breaks the gate, else None."""
    if not 1 <= len(text) <= LIMIT:
        return f"fortune must be 1-{LIMIT} characters, got {len(text)}"
    if not text.strip():
        return "fortune must not be only whitespace"
    if "\n" in text or "\r" in text:
        return "fortune must be a single line"
    return None


def main() -> int:
    problem = check(FORTUNE)
    if problem is not None:
        print(f"error: {problem}", file=sys.stderr)
        return 1

    folder = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    folder.mkdir(parents=True, exist_ok=True)
    (folder / "entry.txt").write_text(FORTUNE, encoding="utf-8")

    print(FORTUNE)
    print(f"characters: {len(FORTUNE)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
