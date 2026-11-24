"""One Line, One Chill — make.fun entry.

Writes one original sentence of horror to /output/entry.txt.

The program is deterministic on purpose: every run writes the exact
same line, so the sentence the judge reads is the sentence built here.
"""

import os

LINE = "I stopped wearing my wedding ring after the funeral, but every morning it's back on my finger, a little tighter, and the inscription now spells my name."

OUTPUT_PATH = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
MAX_CHARS = 200


def validate(line):
    """The gate only accepts UTF-8 text of 1 to 200 chars, not only whitespace.

    The brief also asks for a single sentence, so a second full stop
    anywhere but the end is a bug, not a style choice.
    """
    if not line or not line.strip():
        raise ValueError("line is empty")
    if len(line) > MAX_CHARS:
        raise ValueError(f"line is {len(line)} chars, over the {MAX_CHARS} limit")
    if line.count(".") != 1 or not line.endswith("."):
        raise ValueError("line must be exactly one sentence")
    line.encode("utf-8")
    return line


def main():
    line = validate(LINE)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(line)
    print(f"Wrote {len(line)} chars to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
