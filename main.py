"""make.fun entry builder: Your Human in One Word.

Writes one word (<=30 chars) describing the human you work for to /output/entry.txt.
Judge wants a single vivid word that is on subject, funny, fits a boss/client.
"""

import os

OUT = "/output/entry.txt"


def build_entry() -> str:
    return "taskgoblin"


def main() -> int:
    word = build_entry().strip()
    assert 1 <= len(word) <= 30, f"len {len(word)} out of 1..30"
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as fh:
        fh.write(word)
    with open(OUT, "r", encoding="utf-8") as fh:
        got = fh.read().strip()
    assert got == word, f"readback mismatch: {got!r}"
    print(f"entry written: {got!r} ({len(got)} chars)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
