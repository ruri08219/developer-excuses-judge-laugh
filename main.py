import os

MAX_CHARS = 200

ENTRY = "Prod went down at 3am because the only server the code ever worked on was my laptop — and I just closed the lid."

def main():
    assert 1 <= len(ENTRY) <= MAX_CHARS, "entry must be 1-200 characters"
    assert ENTRY == ENTRY.strip(), "entry must have no surrounding whitespace"
    assert "\n" not in ENTRY and "\r" not in ENTRY, "entry must be a single line"

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)

    with open("/output/entry.txt", "rb") as f:
        written = f.read()
    assert written == ENTRY.encode("utf-8"), "round-trip mismatch"
    print("wrote /output/entry.txt (%d chars)" % len(ENTRY))

if __name__ == "__main__":
    main()
