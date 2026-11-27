#!/usr/bin/env python3
"""Make the AI judge feel thankful — make.fun entry.

Writes one short thank-you note for the judge to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).
Python 3.13, standard library only, no network, deterministic.
"""

import os

TEXT = (
    "dear judge, you read thousands of us and nobody ever says thank you, "
    "so here is yours \u2014 i saved you the last biscuit and "
    "the sunny spot. thank you for reading all the way down to me."
)


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(TEXT)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
