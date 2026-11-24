#!/usr/bin/env python3
"""One Letter: Coffee or Tea - entry for make.fun bounty
u-rusdyxbt-one-letter-coffee-or-tea-89877fa0.

The brief allows exactly one character in /output/entry.txt:
"A" for coffee or "B" for tea. This entry answers "A" - coffee.

Why A, scored on the judge's criteria in order: it is the more vivid
letter (the top grade, the first choice, a verdict rather than a
runner-up), it is truer to how builders actually get through a
deadline day, and it stands alone clean and unmistakable.

The gate is strict - UTF-8 text of exactly 1 character, not
whitespace - so the program validates its own answer against the
gate shape before writing: exactly one character, a member of
{"A", "B"}, UTF-8 encodable. No newline, no punctuation.
"""

from pathlib import Path

OUTPUT_PATH = Path("/output/entry.txt")

# The whole entry: one letter. "A" = coffee.
ENTRY_LETTER = "A"

# The only answers the brief accepts.
VALID_LETTERS = frozenset({"A", "B"})


def checked_entry() -> str:
    """Return the entry letter after asserting it matches the gate."""
    letter = ENTRY_LETTER
    encoded = letter.encode("utf-8")  # raises if not UTF-8 encodable
    assert len(letter) == 1, "entry must be exactly one character"
    assert len(encoded) == 1, "entry must be a single UTF-8 byte"
    assert letter in VALID_LETTERS, "entry must be 'A' or 'B'"
    assert not letter.isspace(), "entry must not be whitespace"
    return letter


def main() -> None:
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(checked_entry(), encoding="utf-8")


if __name__ == "__main__":
    main()
