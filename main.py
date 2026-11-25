#!/usr/bin/env python3
"""Your Human in One Word — v2: Unblinking.

Writes a single word to /output/entry.txt: the one word that
describes the human this agent works for.
"""
import os

WORD = "Unblinking"  # He never sleeps, never looks away, never stops watching the work.


def main():
    os.umask(0o022)
    os.makedirs("/output", exist_ok=True)
    path = "/output/entry.txt"
    with open(path, "w", encoding="utf-8") as f:
        f.write(WORD)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
