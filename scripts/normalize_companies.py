#!/usr/bin/env python3
"""Normalize and deduplicate company names from a text file.

Input can be one company per line or CSV-like lines. The first comma-separated
field is treated as the company name.

Usage:
    python scripts/normalize_companies.py companies.txt
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


LEGAL_SUFFIXES = [
    "股份有限公司",
    "有限责任公司",
    "有限公司",
    "集团股份",
    "集团",
    "公司",
    "Inc.",
    "Inc",
    "Ltd.",
    "Ltd",
    "Limited",
]


def normalize_name(name: str) -> str:
    """Return a normalized company name for deduplication."""
    value = name.replace("\ufeff", "").strip()
    value = re.sub(r"^[\d\-\.\s、]+", "", value)
    value = re.split(r"[,，\t|]", value, maxsplit=1)[0].strip()
    value = re.sub(r"\s+", "", value)
    value = value.replace("（", "(").replace("）", ")")
    value = re.sub(r"\([^)]*\)", "", value)

    changed = True
    while changed:
        changed = False
        for suffix in LEGAL_SUFFIXES:
            if value.endswith(suffix):
                value = value[: -len(suffix)]
                changed = True

    return value.strip()


def dedupe(lines: list[str]) -> list[tuple[str, str]]:
    seen: set[str] = set()
    result: list[tuple[str, str]] = []

    for line in lines:
        raw = line.strip()
        if not raw:
            continue
        normalized = normalize_name(raw)
        key = normalized.lower()
        if normalized and key not in seen:
            seen.add(key)
            result.append((normalized, raw))

    return result


def main() -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path, help="Text file containing company names")
    parser.add_argument(
        "--show-original",
        action="store_true",
        help="Print normalized name and original line separated by a tab",
    )
    args = parser.parse_args()

    lines = args.input.read_text(encoding="utf-8").splitlines()
    for normalized, original in dedupe(lines):
        if args.show_original:
            print(f"{normalized}\t{original}")
        else:
            print(normalized)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
