"""One-line developer excuse entry for make.fun.

Writes the exact excuse to /output/entry.txt as UTF-8, then reads it
back and asserts a byte-identical round-trip.
"""

import os

ENTRY = "Prod went down at 3am because the only server the code ever worked on was my laptop \u2014 and I just closed the lid."


def main():
    os.makedirs("/output", exist_ok=True)
    data = ENTRY.encode("utf-8")
    with open("/output/entry.txt", "wb") as f:
        f.write(data)
    with open("/output/entry.txt", "rb") as f:
        back = f.read()
    assert back == data, "round-trip mismatch"
    assert 1 <= len(ENTRY) <= 200, "entry length out of range"
    assert ENTRY == ENTRY.strip(), "entry has surrounding whitespace"
    assert "\n" not in ENTRY, "entry must be a single line"


if __name__ == "__main__":
    main()
