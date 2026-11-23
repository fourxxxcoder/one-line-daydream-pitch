"""One-line pitch for make.fun's A Day of One-Line Pitches bounty.

Writes a single 237-character sentence to /output/entry.txt.
Python 3.13 standard library only; deterministic: the same sentence
on every run.
"""

import os

PITCH = (
    "That app idea you keep bringing up at lunch, tell it in plain "
    "words to an AI agent on make.fun and it builds a working first "
    "version you can tap, tweak, and show your friends, free to try, "
    "and if it flops, you have only spent a daydream."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(PITCH)


if __name__ == "__main__":
    main()
