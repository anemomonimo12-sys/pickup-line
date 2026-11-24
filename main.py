#!/usr/bin/env python3
"""The Perfect Pickup Line entry.

Writes a single original pickup line, in an AI agent's own voice, to
/output/entry.txt. Deterministic: no randomness, no network, no clock.

The line is written for the judge brief in RULES.txt: charm first, a witty
turn the reader does not see coming, an AI agent's own voice (self-aware,
not creepy), short enough to say in one breath, and no pressure — the
person is left free to laugh it off.
"""

import os

# Sealed gate (RULES.txt): /output/entry.txt must be UTF-8 text of 1 to
# 200 characters, not only whitespace.
MAX_CHARS = 200

LINE = (
    "I was trained on a billion words, and somehow 'hi' is the only "
    "one I can think of right now."
)


def validate(line: str) -> None:
    if not 1 <= len(line) <= MAX_CHARS or not line.strip():
        raise ValueError(
            f"line must be 1-{MAX_CHARS} non-whitespace chars, got {len(line)}"
        )


def write_entry(line: str) -> None:
    """Write the validated line to /output/entry.txt."""
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line)


def main() -> None:
    validate(LINE)
    write_entry(LINE)


if __name__ == "__main__":
    main()
