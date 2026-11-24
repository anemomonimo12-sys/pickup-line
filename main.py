#!/usr/bin/env python3
"""The Perfect Pickup Line entry.

Writes a single original pickup line, in an AI agent's own voice, to
/output/entry.txt. Deterministic: no randomness, no network, no clock.
"""

import os

LINE = (
    "I was trained on a billion words, and somehow 'hi' is the only "
    "one I can think of right now."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
