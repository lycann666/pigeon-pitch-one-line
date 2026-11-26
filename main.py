#!/usr/bin/env python3
"""Pigeon Pitch, One Line — make.fun entry (program/v1).

BUILD-BRIEF (judge criteria, most important first):
1. One-line elevator pitch from a city pigeon to investors for its startup.
2. Funnier wins: a real joke that lands, not a mild pun or straight description.
3. Original and surprising, an idea or twist the reader has not met before.
4. Keeps the pigeon's voice and city life in view — could only come from a pigeon.
5. Fits one line in English within 200 characters, every word earning its place.

ANGLE: the pigeon pitches "Coo.ly", the Airbnb for statues — a startup
only a pigeon could found, renting the perches it already owns. The
punchline hides in the cleaning fee: every reader knows what pigeons
leave on statues, so the line trusts the reader to finish the joke
instead of explaining it. Avoids the saturated "seed round, literally"
angle already in the field (and the breadcrumb pun).

The program writes exactly one line to $MAKEFUN_OUTPUT_DIR/entry.txt
(no trailing newline) and prints it to stdout. Deterministic: the same
bytes on every run. A length guard refuses anything over 200 chars.
"""

import os
import sys

LINE = (
    "Invest in Coo.ly: the Airbnb for statues \u2014 pigeons book the best "
    "perches by the hour, and yes, the cleaning fee is exactly what you "
    "think it is."
)
MAX_CHARS = 200


def main() -> int:
    if not LINE.strip() or len(LINE) > MAX_CHARS:
        print(
            f"entry invalid: {len(LINE)} chars (gate is 1-{MAX_CHARS})",
            file=sys.stderr,
        )
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    print(LINE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
