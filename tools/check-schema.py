#!/usr/bin/env python3
"""Validate frontmatter on every card under frameworks/, processes/, tools/."""

import re
import sys
from pathlib import Path

REQUIRED_FIELDS = {
    "name",
    "name_en",
    "source_company",
    "category",
    "created_year",
    "one_line_summary",
    "purpose",
    "when_to_use",
    "key_steps",
    "limitations",
    "related_methods",
    "tags",
    "status",
}
VALID_STATUS = {"draft", "fact-checked", "annotated", "archived"}
VALID_CATEGORY = {"framework", "process", "tool"}
FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---\n", re.DOTALL)


def parse_frontmatter(text: str) -> dict | None:
    match = FRONTMATTER_RE.match(text)
    if not match:
        return None
    fm: dict = {}
    current_key = None
    for line in match.group(1).splitlines():
        if line.startswith("  - ") and current_key:
            if not isinstance(fm.get(current_key), list):
                fm[current_key] = []
            fm[current_key].append(line[4:].strip())
        elif ":" in line and not line.startswith(" "):
            key, _, value = line.partition(":")
            current_key = key.strip()
            value = value.strip()
            if value == "":
                fm[current_key] = []
            elif value.startswith("[") and value.endswith("]"):
                inner = value[1:-1].strip()
                fm[current_key] = [x.strip() for x in inner.split(",")] if inner else []
            else:
                fm[current_key] = value
    return fm


def validate_card(path: Path) -> list[str]:
    errors: list[str] = []
    text = path.read_text(encoding="utf-8")
    fm = parse_frontmatter(text)
    if fm is None:
        return [f"{path}: missing frontmatter"]
    missing = REQUIRED_FIELDS - fm.keys()
    if missing:
        errors.append(f"{path}: missing fields: {sorted(missing)}")
    if "status" in fm and fm["status"] not in VALID_STATUS:
        errors.append(f"{path}: invalid status '{fm['status']}'")
    if "category" in fm and fm["category"] not in VALID_CATEGORY:
        errors.append(f"{path}: invalid category '{fm['category']}'")
    if "related_methods" in fm and not isinstance(fm["related_methods"], list):
        errors.append(f"{path}: related_methods must be a list")
    return errors


def main() -> int:
    root = Path.cwd()
    card_dirs = [root / "frameworks", root / "processes", root / "tools"]
    all_errors: list[str] = []
    for d in card_dirs:
        if not d.exists():
            continue
        for card in sorted(d.glob("*.md")):
            all_errors.extend(validate_card(card))
    if all_errors:
        for err in all_errors:
            print(err)
        return 1
    print("All cards pass schema validation.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
