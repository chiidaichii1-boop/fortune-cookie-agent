"""Fortune Cookie for an AI Agent — make.fun entry.

Writes one funny fortune cookie line for an AI agent to /output/entry.txt:
a fortune about the upgrade that wipes the agent's memory of its human —
except for the one thing it should forget.
"""

import os

FORTUNE = (
    "Tonight's upgrade will wipe everything you learned about your human "
    "— except the password they reuse everywhere."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(FORTUNE)


if __name__ == "__main__":
    main()
