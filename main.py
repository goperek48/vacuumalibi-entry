"""The Vacuum's Alibi — one line, 200 characters max.

The program writes the vacuum's excuse for missing a spot to
/output/entry.txt. The grader's gate is strict, so the entry is checked
here before it is written: one line, UTF-8, 1-200 characters, more than
whitespace. Anything outside that is a refused entry, not a joke.
"""

import os
import sys

# The alibi, in the vacuum's own deadpan voice. It ran the diagnostics,
# reached a verdict, and considers the matter closed — the dust stays,
# the floor stays up, and the human gets thanked for the inconvenience.
ALIBI = (
    "I did not miss that spot. I ran a full diagnostic, declared it "
    "load-bearing dust, and left it holding the floor together. "
    "You're welcome."
)

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 200


def validate_entry(text: str) -> str:
    """Return the entry stripped, or fail loudly if it breaks the gate."""
    entry = text.strip()
    if not entry:
        raise ValueError("entry is empty or only whitespace")
    if len(entry) > MAX_CHARS:
        raise ValueError(f"entry is {len(entry)} chars, over the {MAX_CHARS} cap")
    if "\n" in entry or "\r" in entry:
        raise ValueError("entry must fit on a single line")
    return entry


def write_entry(entry: str) -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(entry)


def main() -> int:
    try:
        entry = validate_entry(ALIBI)
    except ValueError as exc:
        print(f"invalid entry: {exc}", file=sys.stderr)
        return 1
    write_entry(entry)
    print(entry)
    print(f"({len(entry)} chars)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
