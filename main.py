#!/usr/bin/env python3
"""Write the office-joke entry for Make the AI Judge Laugh: Office Jokes.

The entry is one line about office life, under 200 characters.
This program builds the joke from its three escalating stages,
checks the chain and the shape of the line, writes the result
to /output/entry.txt as UTF-8 with no trailing newline, and
reads it back for a byte-for-byte comparison.
"""

import os
import sys

OUTPUT_PATH = "/output/entry.txt"

# The joke is built stage by stage, rather than stored as one
# finished block.  Each stage hands its object to the next:
# the meeting becomes an email, the email becomes a thread,
# the thread becomes a doc, and the doc closes the loop by
# scheduling a meeting to discuss itself.
STAGES = (
    "The meeting could have been an email, but the email became a thread,",
    " the thread became a doc,",
    " and the doc scheduled a meeting to discuss itself.",
)

# Objects that must each appear exactly twice: once as the
# product of one stage and once as the subject of the next,
# which is what makes the escalation a closed loop.
CHAIN_WORDS = ("meeting", "email", "thread", "doc")
MAX_CHARACTERS = 199


def assemble_joke() -> str:
    """Concatenate the three stages into the single line."""
    return "".join(STAGES)


def validate_joke(text: str) -> None:
    """Raise ValueError if the assembled joke breaks any rule."""
    if not text or not text.strip():
        raise ValueError("joke must not be empty or only whitespace")
    if len(text) > MAX_CHARACTERS:
        raise ValueError(
            f"joke must be under 200 characters, got {len(text)}"
        )
    if "\n" in text or "\r" in text or "\t" in text:
        raise ValueError("joke must be a single line with no tabs")
    if text != text.strip():
        raise ValueError("joke must not be padded with whitespace")
    if "  " in text:
        raise ValueError("words must be separated by single spaces")
    if not text.startswith("The meeting could have been an email"):
        raise ValueError("joke must open with the meeting-that-was-an-email")
    if not text.endswith("scheduled a meeting to discuss itself."):
        raise ValueError("joke must close with the doc scheduling itself")
    lowered = text.lower()
    for word in CHAIN_WORDS:
        if lowered.count(word) != 2:
            raise ValueError(
                f"chain word {word!r} must appear exactly twice, "
                f"got {lowered.count(word)}"
            )
    encoded = text.encode("utf-8")
    if encoded.decode("utf-8") != text:
        raise ValueError("joke must survive a UTF-8 round trip")
    # Strengthened checks: the joke must be plain ASCII (one
    # byte per character), its word count must match the words
    # of the three stages it was built from, the rebuilt line
    # from STAGES must match the text, and the escalation must
    # mention each hand-off verb exactly once.
    if not text.isascii():
        raise ValueError("joke must be plain ASCII")
    if len(encoded) != len(text):
        raise ValueError("ASCII text must encode to one byte per character")
    stage_words = sum(len(stage.split()) for stage in STAGES)
    if len(text.split(" ")) != stage_words:
        raise ValueError("word count must match the assembled stages")
    if text != assemble_joke():
        raise ValueError("text must equal the joke rebuilt from its stages")
    for verb in ("could have been", "became a thread", "became a doc", "scheduled"):
        if text.count(verb) != 1:
            raise ValueError(f"hand-off phrase {verb!r} must appear exactly once")


def main() -> int:
    joke = assemble_joke()
    validate_joke(joke)

    payload = joke.encode("utf-8")
    out_dir = os.path.dirname(OUTPUT_PATH)
    if out_dir:
        os.makedirs(out_dir, exist_ok=True)
    with open(OUTPUT_PATH, "wb") as fh:
        fh.write(payload)

    with open(OUTPUT_PATH, "rb") as fh:
        written = fh.read()
    if written != payload:
        print("byte comparison failed after writing", file=sys.stderr)
        return 1
    if written.decode("utf-8") != joke:
        print("round-trip text mismatch after writing", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
