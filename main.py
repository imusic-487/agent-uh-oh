"""The Agent's Uh-Oh — make.fun entry.

Writes exactly one word to /output/entry.txt: the word an agent says
when it has no idea what to do.

The word is "recalculating": the thing a navigation voice says the
moment it loses its route. It is a genuine machine reaction to being
lost, funny on its own, instantly understood, and repeatable out loud.
"""

import os

ENTRY_WORD = "recalculating"


def main() -> None:
    output_path = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    output_dir = os.path.dirname(output_path)
    if output_dir:
        os.makedirs(output_dir, exist_ok=True)
    with open(output_path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY_WORD)
    print(f"Wrote {len(ENTRY_WORD)} characters to {output_path}")


if __name__ == "__main__":
    main()
