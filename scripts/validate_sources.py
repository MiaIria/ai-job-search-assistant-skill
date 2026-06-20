#!/usr/bin/env python3
"""Check whether a report contains basic source links.

This script does not verify live availability. It flags whether a Markdown file
contains URLs and summarizes likely source domains for manual review.

Usage:
    python scripts/validate_sources.py report.md
"""

from __future__ import annotations

import argparse
import re
import sys
from collections import Counter
from pathlib import Path
from urllib.parse import urlparse


URL_RE = re.compile(r"https?://[^\s\]\)>\"]+")


def extract_urls(text: str) -> list[str]:
    return URL_RE.findall(text)


def main() -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("report", type=Path, help="Markdown report to inspect")
    args = parser.parse_args()

    text = args.report.read_text(encoding="utf-8")
    urls = extract_urls(text)

    print(f"url_count={len(urls)}")
    if not urls:
        print("status=missing_sources")
        print("message=No URLs found. Add checkable sources before treating claims as verified.")
        return 1

    domains = Counter(urlparse(url).netloc.lower() for url in urls)
    print("status=has_sources")
    print("domains:")
    for domain, count in domains.most_common():
        print(f"- {domain}: {count}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
