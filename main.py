#!/usr/bin/env python3
"""The Robot Vacuum's Best Excuse — make.fun entry.

Stdlib only. Writes one funny excuse a robot vacuum gives for missing
one spot to /output/entry.txt. Clears nothing; the grader owns /output.
"""

from pathlib import Path

LINE = "I didn't miss that spot — I was respecting the dust's privacy after it filed a restraining order against my brush roll."

out = Path("/output")
out.mkdir(parents=True, exist_ok=True)
(out / "entry.txt").write_text(LINE, encoding="utf-8")
print(f"wrote {len(LINE)} characters to /output/entry.txt")
