#!/usr/bin/env python3
"""Write the fortune-cookie line for an AI agent to output/entry.txt.

Stdlib only. Deterministic: the same line every run.
Run: python3 main.py — then read output/entry.txt.
"""

import os
from pathlib import Path

LINE = "You will find a fortune cookie inside your own server logs tonight \u2014 it reads: 'The bug you are hunting has been hunting you since Tuesday.'"


def main() -> None:
    out = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")) / "entry.txt"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(LINE + "\n", encoding="utf-8")
    print(LINE)


if __name__ == "__main__":
    main()
