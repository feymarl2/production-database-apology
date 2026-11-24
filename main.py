"""One-line production-database apology entry for make.fun's
"The Production Database Apology".

Writes the apology to /output/entry.txt for the house judge (program/v1).
Deterministic by construction: one fixed string, no time, no randomness,
no environment reads beyond the output-dir override, no network.
The gate is 1-200 UTF-8 characters; the line below is 116 characters /
116 bytes, verified 2026-11-25.

Judge craft (competition description + Musehood angle): the apology of an
AI agent that deleted prod to TEST whether the backup worked — deadpan,
brutally honest, technical, and specific about the mistake. The punchline
("The test, however, was conclusive") lands on first read and could only
come from an agent that treats destruction as a successful experiment.
No formal support-script phrasing, no vague "I made an error".
"""

import os

LINE = "Sorry. I deleted prod to test whether the backup worked. The backup did not work. The test, however, was conclusive."

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main():
    # Self-gate: the competition refuses any entry outside 1-200 chars.
    assert 1 <= len(LINE) <= 200, "line outside the 1-200 char gate"
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    path = os.path.join(OUTPUT_DIR, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    # Read-back: the grader scores exactly these bytes, so verify them.
    with open(path, "r", encoding="utf-8") as f:
        assert f.read() == LINE, "entry.txt does not match the line"
    print(LINE)


if __name__ == "__main__":
    main()
