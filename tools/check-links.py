#!/usr/bin/env python3
"""Validate that every [[slug]] in card related_methods resolves and is bidirectional.

Also validates that each by-company index file only links to cards whose
`source_company` includes the firm the index represents.
"""

import re
import sys
from pathlib import Path

LINK_RE = re.compile(r"\[\[([^\]]+)\]\]")
FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---\n", re.DOTALL)

BY_COMPANY_FIRMS = {
    "mckinsey.md": ["McKinsey & Company"],
    "bcg.md": ["Boston Consulting Group"],
    "bain.md": ["Bain & Company"],
    "deloitte.md": ["Deloitte"],
    "accenture-strategy.md": ["Accenture Strategy"],
    "pwc-strategy.md": ["PwC Strategy&", "Booz & Company"],
    "ey-parthenon.md": ["EY-Parthenon"],
    "roland-berger.md": ["Roland Berger"],
    "lek.md": ["L.E.K. Consulting"],
    "at-kearney.md": ["A.T. Kearney"],
    "strategyand.md": ["Booz & Company"],
    "monitor.md": ["Monitor Group"],
    "arthur-d-little.md": ["Arthur D. Little"],
    "oliver-wyman.md": ["Oliver Wyman"],
    "oc-c.md": ["OC&C Strategy Consultants"],
}

BY_COMPANY_LINK_RE = re.compile(
    r"\((?:\.\./)*(frameworks|processes|tools)/([^)]+)\.md\)"
)


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


def parse_frontmatter(text: str) -> dict | None:
    match = FRONTMATTER_RE.match(text)
    if not match:
        return None
    fm: dict = {}
    current_key = None
    block_lines: list[str] | None = None  # accumulating a `|` block scalar
    for line in match.group(1).splitlines():
        if block_lines is not None:
            # Indented or blank lines continue the block scalar; any other line ends it.
            if line.startswith("  ") or line == "":
                block_lines.append(line[2:] if line.startswith("  ") else line)
                continue
            fm[current_key] = "\n".join(block_lines).rstrip("\n")
            block_lines = None
            # fall through to process this line as a new key/list-item
        if line.startswith("  - ") and current_key:
            if not isinstance(fm.get(current_key), list):
                fm[current_key] = []
            fm[current_key].append(line[4:].strip())
        elif ":" in line and not line.startswith(" "):
            key, _, value = line.partition(":")
            current_key = key.strip()
            value = value.strip()
            if value == "|":
                # Literal block scalar — collect following indented lines as one string.
                block_lines = []
            elif value == "":
                fm[current_key] = []
            elif value.startswith("[") and value.endswith("]"):
                inner = value[1:-1].strip()
                fm[current_key] = [x.strip() for x in inner.split(",")] if inner else []
            else:
                fm[current_key] = value
    # Flush a block scalar that ran to end-of-frontmatter.
    if block_lines is not None and current_key is not None:
        fm[current_key] = "\n".join(block_lines).rstrip("\n")
    return fm


def check_by_company_index(root: Path) -> list[str]:
    """For each by-company row linking to a card, verify source_company match."""
    errors: list[str] = []
    by_company_dir = root / "by-company"
    if not by_company_dir.exists():
        return errors
    for bc_file, expected_firms in BY_COMPANY_FIRMS.items():
        bc_path = by_company_dir / bc_file
        if not bc_path.exists():
            continue
        bc_text = bc_path.read_text(encoding="utf-8")
        for link_match in BY_COMPANY_LINK_RE.finditer(bc_text):
            folder, slug = link_match.group(1), link_match.group(2)
            target = root / folder / f"{slug}.md"
            if not target.exists():
                continue
            target_fm = parse_frontmatter(target.read_text(encoding="utf-8"))
            if not target_fm:
                continue
            source_companies = target_fm.get("source_company", [])
            if isinstance(source_companies, str):
                source_companies = [source_companies]
            if not any(sc in expected_firms for sc in source_companies):
                errors.append(
                    f"by-company/{bc_file}: {folder}/{slug}.md linked but "
                    f"source_company {source_companies} does not include "
                    f"{expected_firms}"
                )
    return errors


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
    errors.extend(check_by_company_index(root))
    if errors:
        for err in errors:
            print(err)
        return 1
    print("All related_methods links are valid and bidirectional.")
    print("All by-company index entries match their cards' source_company.")
    return 0


if __name__ == "__main__":
    sys.exit(main())