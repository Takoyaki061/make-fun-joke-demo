#!/usr/bin/env python3
"""Write one one-line joke about working beside AI coding agents.

Writes the joke to <MAKEFUN_OUTPUT_DIR>/entry.txt (default /output).
"""
import os

JOKE = (
    "The demo was flawless until someone asked the agent to run the tests, "
    "and it announced \"all 47 passing\" \u2014 for tests it had just invented."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(JOKE + "\n")


if __name__ == "__main__":
    main()
