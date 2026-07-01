#!/usr/bin/env python3
"""Check local Markdown links resolve inside the repository."""
from __future__ import annotations

from pathlib import Path
import re
import sys
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
LINK_RE = re.compile(r"(?<!!)\[[^\]]+\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)")


def is_external(href: str) -> bool:
    return (
        "://" in href
        or href.startswith("mailto:")
        or href.startswith("#")
        or href.startswith("tel:")
    )


def main() -> int:
    failures: list[str] = []
    for path in sorted(ROOT.rglob("*.md")):
        if any(part.startswith(".") and part != ".github" for part in path.relative_to(ROOT).parts):
            continue
        text = path.read_text(encoding="utf-8", errors="ignore")
        for match in LINK_RE.finditer(text):
            href = unquote(match.group(1)).split("#", 1)[0]
            if not href or is_external(href):
                continue
            target = (path.parent / href).resolve()
            try:
                target.relative_to(ROOT)
            except ValueError:
                failures.append(f"{path.relative_to(ROOT)} -> {href} escapes repository")
                continue
            if not target.exists():
                failures.append(f"{path.relative_to(ROOT)} -> {href} missing")

    if failures:
        print("Broken local Markdown links:")
        for failure in failures:
            print(f"- {failure}")
        return 1
    print("Local Markdown links OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
