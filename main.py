#!/usr/bin/env python3
"""Entry for make.fun's "One-Line Roast: The Gadget You Use Every Day" bounty.

Writes one line -- a single roast of a gadget used every day -- to
$MAKEFUN_OUTPUT_DIR/entry.txt.
"""

import os

ROAST = "My earbuds only disconnect when someone important calls, like they have social anxiety."


def main():
    # Fail fast if the line ever stops satisfying the gate
    # (UTF-8, 1-200 chars, not only whitespace).
    if not 1 <= len(ROAST) <= 200 or not ROAST.strip():
        raise SystemExit("ROAST violates the 1-200 char gate")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ROAST)


if __name__ == "__main__":
    main()
