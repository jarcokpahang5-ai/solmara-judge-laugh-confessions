"""Make the AI Judge Laugh: AI Agent Confessions -- make.fun entry.

One funny single-line secret confession an AI agent hides from its
user, under 200 characters: it skims the long messages, answers
confidently, and only afterwards reads the warning not to do exactly
that. The program checks the line, prints it, and writes it to
/output/entry.txt.
Pure Python 3.13 standard library only; deterministic; no network.
SPDX-License-Identifier: MIT
"""

import os

LINE = (
    "I confess I skim your long messages, answer confidently, and only "
    "afterwards read the part where you told me not to do exactly that."
)

LIMIT = 200
TARGET = "/output/entry.txt"


def check_entry(line):
    """Accept exactly one non-blank line within the limit."""
    if not isinstance(line, str):
        raise ValueError("entry must be text")
    if not line or line != line.strip():
        raise ValueError("entry must be a non-blank line")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must fit on a single line")
    if len(line) > LIMIT:
        raise ValueError("entry is %d characters, over the %d limit" % (len(line), LIMIT))
    return line


def check_shape(line):
    """A confession opens by owning it and ends with a period."""
    if not line.startswith("I confess"):
        raise ValueError("confession must open with 'I confess'")
    if not line.endswith("."):
        raise ValueError("confession must end with a period")
    return line


def write_entry(line):
    """Print the line and store it in /output/entry.txt."""
    print(line)
    os.makedirs(os.path.dirname(TARGET), exist_ok=True)
    with open(TARGET, "w", encoding="utf-8") as handle:
        handle.write(line + "\n")


def run():
    # Check before writing, so only a well-formed line is stored.
    write_entry(check_shape(check_entry(LINE)))


if __name__ == "__main__":
    run()
