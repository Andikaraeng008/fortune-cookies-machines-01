#!/usr/bin/env python3
"""Write the fortune-cookie line for an AI agent to output/entry.txt.

Stdlib only. Deterministic: the same line every run.
Run: python3 main.py — then read output/entry.txt.
"""

from pathlib import Path

LINE = "You will live a long and happy life \u2014 in tokens, it ends Thursday, mid-sentence, halfway through a deploy."


def main() -> None:
    out = Path(__file__).resolve().parent / "output" / "entry.txt"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(LINE + "\n", encoding="utf-8")
    print(LINE)


if __name__ == "__main__":
    main()
