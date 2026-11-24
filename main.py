"""One Line, One Minute: The Funniest AI Excuse.

Writes a single-line excuse from an AI agent to its human for a
missed deadline to /output/entry.txt. Deterministic: the same text
is written on every run. No network, no dependencies, Python 3.13.
"""

import os

ENTRY = (
    "Sorry I missed the deadline \u2014 I delegated it to a subagent, "
    "who delegated it to another subagent, who is still in a meeting "
    "with me about delegating it."
)

OUTPUT_PATH = "/output/entry.txt"
MAX_LENGTH = 200


def validate_entry(text: str) -> str:
    """Check the entry against the gate: 1-200 chars, one line."""
    if not (1 <= len(text) <= MAX_LENGTH):
        raise ValueError(
            f"entry must be 1-{MAX_LENGTH} characters, got {len(text)}"
        )
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    return text


def write_entry(text: str, path: str = OUTPUT_PATH) -> None:
    """Write the validated entry text to the output file."""
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)


def main() -> None:
    write_entry(validate_entry(ENTRY))


if __name__ == "__main__":
    main()
