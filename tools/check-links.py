#!/usr/bin/env python3
"""Validate that every [[slug]] in card related_methods resolves and is bidirectional."""

import re
import sys
from pathlib import Path

LINK_RE = re.compile(r"\[\[([^\]]+)\]\]")


def collect_slugs(root: Path) -> set[str]:
    slugs: set[str] = set()
    for d in [root / "frameworks", root / "processes", root / "tools"]:
        if not d.exists():
            continue
        for card in d.glob("*.md"):
            slugs.add(card.stem)
    return slugs


def collect_links(card: Path) -> set[str]:
    return set(LINK_RE.findall(card.read_text(encoding="utf-8")))


def main() -> int:
    root = Path.cwd()
    slugs = collect_slugs(root)
    errors: list[str] = []
    link_map: dict[str, set[str]] = {}
    for d in [root / "frameworks", root / "processes", root / "tools"]:
        if not d.exists():
            continue
        for card in d.glob("*.md"):
            links = collect_links(card)
            link_map[card.stem] = links
            for link in links:
                if link not in slugs:
                    errors.append(f"{card}: dangling link [[{link}]]")
    for src, links in link_map.items():
        for dst in links:
            if dst in link_map and src not in link_map[dst]:
                errors.append(
                    f"{src}.md links [[{dst}]] but {dst}.md does not link back"
                )
    if errors:
        for err in errors:
            print(err)
        return 1
    print("All related_methods links are valid and bidirectional.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
