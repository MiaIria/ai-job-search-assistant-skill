#!/usr/bin/env python3
"""Score candidate-to-role fit with the 100-point rubric.

Usage:
    python scripts/score_fit.py --hard 24 --experience 32 --soft 21
"""

from __future__ import annotations

import argparse
import sys


MAX_SCORES = {
    "hard": 30,
    "experience": 40,
    "soft": 30,
}


def clamp_score(name: str, value: float) -> float:
    maximum = MAX_SCORES[name]
    if value < 0 or value > maximum:
        raise ValueError(f"{name} must be between 0 and {maximum}")
    return value


def band(total: float) -> str:
    if total >= 90:
        return "highly_recommended"
    if total >= 75:
        return "recommended"
    if total >= 60:
        return "possible"
    return "lower_priority"


def main() -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--hard", type=float, required=True, help="Hard requirements score, max 30")
    parser.add_argument(
        "--experience",
        type=float,
        required=True,
        help="Experience relevance score, max 40",
    )
    parser.add_argument("--soft", type=float, required=True, help="Soft fit score, max 30")
    args = parser.parse_args()

    hard = clamp_score("hard", args.hard)
    experience = clamp_score("experience", args.experience)
    soft = clamp_score("soft", args.soft)
    total = hard + experience + soft

    print(f"hard_requirements={hard:.1f}/30")
    print(f"experience_relevance={experience:.1f}/40")
    print(f"soft_fit={soft:.1f}/30")
    print(f"total={total:.1f}/100")
    print(f"band={band(total)}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
