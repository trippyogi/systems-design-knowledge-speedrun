#!/usr/bin/env python3
"""Create a new ADR file from the template."""
from pathlib import Path
import argparse
import re

ROOT = Path(__file__).resolve().parents[1]
ADR_DIR = ROOT / "docs" / "adr"
TEMPLATE = ROOT / "docs" / "templates" / "adr-template.md"


def slugify(title: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", title.lower()).strip("-")
    return slug or "decision"


def main() -> int:
    parser = argparse.ArgumentParser(description="Create a new ADR file from the template.")
    parser.add_argument("title", nargs="+", help="ADR title, e.g. 'Choose cache-aside for redirects'")
    args = parser.parse_args()

    title = " ".join(args.title).strip()
    ADR_DIR.mkdir(parents=True, exist_ok=True)
    existing = sorted(ADR_DIR.glob("*.md"))
    next_num = len(existing) + 1
    path = ADR_DIR / f"{next_num:04d}-{slugify(title)}.md"
    content = TEMPLATE.read_text(encoding="utf-8").replace("ADR NNNN: Title", f"ADR {next_num:04d}: {title}")
    path.write_text(content, encoding="utf-8")
    print(path.relative_to(ROOT))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
