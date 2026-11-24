"""Write the entry line to /output/entry.txt.

Deterministic: the same bytes on every run. Standard library only.

The line is one sentence, 175 characters: a deadpan founder pitch for Pebble,
an app that lets you adopt, name, and emotionally support a single rock.
"""

import os

LINE = "Pebble is the world's first app that lets you adopt, name, and emotionally support a single rock in your garden, with daily check-ins and a grief counselor for when it erodes."


def main():
    # No trailing newline: the gate counts characters, and the entry is the
    # sentence exactly as pitched, nothing after it.
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
