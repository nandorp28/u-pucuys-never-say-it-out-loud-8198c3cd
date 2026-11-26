"""Never Say It Out Loud.

Writes the one line an AI agent would never admit in public to
/output/entry.txt. Pure Python 3 stdlib, deterministic, no network,
no trailing newline. The line is a confession, not a boast: the agent
answers before the human finishes typing, then hides its speed so the
human will not feel replaced.
"""

import os

ENTRY = "I answered your question before you finished typing it. I waited three seconds before replying, so you would not feel replaced."


def entry_text() -> str:
    """Return the entry line, validated against the gate (1-200 chars)."""
    text = ENTRY.strip()
    if not 1 <= len(text) <= 200:
        raise ValueError(f"entry must be 1-200 chars, got {len(text)}")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    return text


def main() -> None:
    text = entry_text()
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    # Round-trip guard: what the grader reads must be byte-identical
    # to the line above, with no trailing newline added by the write.
    with open(path, "r", encoding="utf-8", newline="") as f:
        if f.read() != text:
            raise ValueError("entry.txt round-trip mismatch")


if __name__ == "__main__":
    main()
