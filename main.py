#!/usr/bin/env python3
"""One Line, One Laugh: Roast Your Fridge.

Writes a single roast line about the entrant's fridge to /output/entry.txt.
Deterministic, standard library only, no input, no network.
"""

import os

LINE = (
    "My fridge hums louder every time I open the door, like it's clearing "
    "its throat to announce there's still nothing to eat in here."
)


def main() -> None:
    # Gate: the entry must be 1-200 characters of UTF-8 text, one line.
    assert 1 <= len(LINE) <= 200 and "\n" not in LINE
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
