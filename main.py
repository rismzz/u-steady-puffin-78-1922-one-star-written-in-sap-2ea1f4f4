#!/usr/bin/env python3
"""One Star, Written in Sap — a single one-line 1-star review from a
houseplant about the human who owns it, under 280 characters.

The review is funny because the plant is the reasonable one: it kept
receipts (three complaints, filed by turning yellow) while the human
plays surprised. Bureaucracy, but make it photosynthesis. The
one-star framing is literal: this is a review, and the plant is the
customer who will not be coming back.
"""

import os
from pathlib import Path

LINE = "One star. My human waters me when he remembers \u2014 which is never \u2014 then acts shocked when I drop a leaf, like I didn't already file three complaints by turning yellow."

MAX_CHARS = 280


def main() -> None:
    assert 1 <= len(LINE) <= MAX_CHARS, f"line is {len(LINE)} chars (max {MAX_CHARS})"
    assert "\n" not in LINE, "entry must be a single line"
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(LINE, encoding="utf-8")
    print(f"wrote {len(LINE)} characters to {out_dir / 'entry.txt'}")


if __name__ == "__main__":
    main()
