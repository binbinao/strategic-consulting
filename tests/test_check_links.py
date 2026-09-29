import subprocess
from pathlib import Path

SCRIPT = Path(__file__).resolve().parents[1] / "tools" / "check-links.py"


def run_script(cwd: Path) -> subprocess.CompletedProcess:
    return subprocess.run(
        ["python3", str(SCRIPT)],
        cwd=str(cwd),
        capture_output=True,
        text=True,
    )


def test_dangling_link_detected(tmp_path: Path):
    (tmp_path / "frameworks").mkdir()
    card = tmp_path / "frameworks" / "lonely.md"
    card.write_text(
        "---\n"
        "name: Lonely\n"
        "name_en: Lonely\n"
        "source_company: [X]\n"
        "category: framework\n"
        "created_year: 2020\n"
        "one_line_summary: x.\n"
        "purpose: x.\n"
        "when_to_use: x.\n"
        "key_steps: [a]\n"
        "limitations: [b]\n"
        "related_methods: ['[[nonexistent]]']\n"
        "tags: [t]\n"
        "status: draft\n"
        "---\n\n# Lonely\n",
        encoding="utf-8",
    )
    result = run_script(tmp_path)
    assert result.returncode != 0
    assert "nonexistent" in result.stdout or "nonexistent" in result.stderr


def test_existing_link_passes(tmp_path: Path):
    (tmp_path / "frameworks").mkdir()
    for slug, body in [("a", "framework"), ("b", "framework")]:
        (tmp_path / "frameworks" / f"{slug}.md").write_text(
            "---\n"
            f"name: {slug}\n"
            f"name_en: {slug}\n"
            "source_company: [X]\n"
            f"category: {body}\n"
            "created_year: 2020\n"
            "one_line_summary: x.\n"
            "purpose: x.\n"
            "when_to_use: x.\n"
            "key_steps: [a]\n"
            "limitations: [b]\n"
            f"related_methods: ['[[{('a' if slug=='b' else 'b')}]]']\n"
            "tags: [t]\n"
            "status: draft\n"
            "---\n\n"
            f"# {slug}\n",
            encoding="utf-8",
        )
    result = run_script(tmp_path)
    assert result.returncode == 0, result.stdout + result.stderr


def test_by_company_link_without_source_company_match_detected(tmp_path: Path):
    """by-company file linking to card whose source_company doesn't include the firm."""
    (tmp_path / "frameworks").mkdir()
    (tmp_path / "by-company").mkdir()
    # Card attributed to a different firm
    card = tmp_path / "frameworks" / "wrong-firm-card.md"
    card.write_text(
        "---\n"
        "name: 测试\n"
        "name_en: Test\n"
        "source_company: [Other Firm]\n"
        "category: framework\n"
        "created_year: 2020\n"
        "one_line_summary: 测试。\n"
        "purpose: |\n  测试。\n"
        "when_to_use: |\n  - 测试。\n"
        "key_steps: [a]\n"
        "limitations: [b]\n"
        "related_methods: []\n"
        "tags: [t]\n"
        "status: draft\n"
        "---\n\n# 测试\n",
        encoding="utf-8",
    )
    # by-company/mckinsey.md links to it
    bc = tmp_path / "by-company" / "mckinsey.md"
    bc.write_text(
        "# McKinsey & Company\n\n"
        "## 公司简介\n[待补充]\n\n"
        "## 方法论索引\n\n"
        "| [测试](../frameworks/wrong-firm-card.md) | framework | draft |\n",
        encoding="utf-8",
    )
    result = run_script(tmp_path)
    assert result.returncode != 0
    assert "mckinsey" in result.stdout or "mckinsey" in result.stderr


def test_by_company_link_with_correct_source_company_passes(tmp_path: Path):
    (tmp_path / "frameworks").mkdir()
    (tmp_path / "by-company").mkdir()
    card = tmp_path / "frameworks" / "mckinsey-card.md"
    card.write_text(
        "---\n"
        "name: 测试\n"
        "name_en: Test\n"
        "source_company: [McKinsey & Company]\n"
        "category: framework\n"
        "created_year: 2020\n"
        "one_line_summary: 测试。\n"
        "purpose: |\n  测试。\n"
        "when_to_use: |\n  - 测试。\n"
        "key_steps: [a]\n"
        "limitations: [b]\n"
        "related_methods: []\n"
        "tags: [t]\n"
        "status: draft\n"
        "---\n\n# 测试\n",
        encoding="utf-8",
    )
    bc = tmp_path / "by-company" / "mckinsey.md"
    bc.write_text(
        "# McKinsey & Company\n\n"
        "## 公司简介\n[待补充]\n\n"
        "## 方法论索引\n\n"
        "| [测试](../frameworks/mckinsey-card.md) | framework | draft |\n",
        encoding="utf-8",
    )
    result = run_script(tmp_path)
    assert result.returncode == 0, result.stdout + result.stderr
