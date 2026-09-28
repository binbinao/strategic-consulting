import subprocess
import tempfile
from pathlib import Path

SCRIPT = Path(__file__).resolve().parents[1] / "tools" / "check-schema.py"

ALL_SECTIONS_BODY = (
    "\n## 起源与定位\n\n"
    "Origin.\n\n"
    "## 核心内容\n\n"
    "Core.\n\n"
    "## 适用与不适用\n\n"
    "When.\n\n"
    "## 局限与争议\n\n"
    "Limit.\n\n"
    "## 与其他方法论的关系\n\n"
    "Related.\n\n"
    "## 个人批注\n\n"
    "Notes.\n"
)


def run_script(cwd: Path) -> subprocess.CompletedProcess:
    return subprocess.run(
        ["python3", str(SCRIPT)],
        cwd=str(cwd),
        capture_output=True,
        text=True,
    )


def test_missing_field_detected(tmp_path: Path):
    (tmp_path / "frameworks").mkdir()
    card = tmp_path / "frameworks" / "bad.md"
    card.write_text(
        "---\n"
        "name: Test\n"
        "category: framework\n"
        "status: draft\n"
        "---\n\n"
        "# Test\n\nbody\n",
        encoding="utf-8",
    )
    result = run_script(tmp_path)
    assert result.returncode != 0
    assert "name_en" in result.stdout or "name_en" in result.stderr


def test_complete_card_passes(tmp_path: Path):
    (tmp_path / "frameworks").mkdir()
    card = tmp_path / "frameworks" / "good.md"
    card.write_text(
        "---\n"
        "name: Test\n"
        "name_en: Test\n"
        "source_company: [Test Co]\n"
        "category: framework\n"
        "created_year: 2020\n"
        "one_line_summary: A test.\n"
        "purpose: Test purpose.\n"
        "when_to_use: Test usage.\n"
        "key_steps: [step1]\n"
        "limitations: [lim1]\n"
        "related_methods: []\n"
        "tags: [test]\n"
        "status: draft\n"
        "---\n\n"
        "# Test\n" + ALL_SECTIONS_BODY,
        encoding="utf-8",
    )
    result = run_script(tmp_path)
    assert result.returncode == 0, result.stdout + result.stderr


def test_source_company_as_string_fails(tmp_path: Path):
    (tmp_path / "frameworks").mkdir()
    card = tmp_path / "frameworks" / "bad-source.md"
    card.write_text(
        "---\n"
        "name: Test\n"
        "name_en: Test\n"
        "source_company: McKinsey & Company\n"
        "category: framework\n"
        "created_year: 2020\n"
        "one_line_summary: A test.\n"
        "purpose: Test purpose.\n"
        "when_to_use: Test usage.\n"
        "key_steps: [step1]\n"
        "limitations: [lim1]\n"
        "related_methods: []\n"
        "tags: [test]\n"
        "status: draft\n"
        "---\n\n"
        "# Test\n" + ALL_SECTIONS_BODY,
        encoding="utf-8",
    )
    result = run_script(tmp_path)
    assert result.returncode != 0
    assert "source_company" in result.stdout or "source_company" in result.stderr


def test_tags_as_string_fails(tmp_path: Path):
    (tmp_path / "frameworks").mkdir()
    card = tmp_path / "frameworks" / "bad-tags.md"
    card.write_text(
        "---\n"
        "name: Test\n"
        "name_en: Test\n"
        "source_company: [Test Co]\n"
        "category: framework\n"
        "created_year: 2020\n"
        "one_line_summary: A test.\n"
        "purpose: Test purpose.\n"
        "when_to_use: Test usage.\n"
        "key_steps: [step1]\n"
        "limitations: [lim1]\n"
        "related_methods: []\n"
        "tags: foo\n"
        "status: draft\n"
        "---\n\n"
        "# Test\n" + ALL_SECTIONS_BODY,
        encoding="utf-8",
    )
    result = run_script(tmp_path)
    assert result.returncode != 0
    assert "tags" in result.stdout or "tags" in result.stderr


def test_missing_body_section_detected(tmp_path: Path):
    (tmp_path / "frameworks").mkdir()
    card = tmp_path / "frameworks" / "incomplete-body.md"
    body_without_personal = (
        "\n## 起源与定位\n\n"
        "Origin.\n\n"
        "## 核心内容\n\n"
        "Core.\n\n"
        "## 适用与不适用\n\n"
        "When.\n\n"
        "## 局限与争议\n\n"
        "Limit.\n\n"
        "## 与其他方法论的关系\n\n"
        "Related.\n"
    )
    card.write_text(
        "---\n"
        "name: Test\n"
        "name_en: Test\n"
        "source_company: [Test Co]\n"
        "category: framework\n"
        "created_year: 2020\n"
        "one_line_summary: A test.\n"
        "purpose: Test purpose.\n"
        "when_to_use: Test usage.\n"
        "key_steps: [step1]\n"
        "limitations: [lim1]\n"
        "related_methods: []\n"
        "tags: [test]\n"
        "status: draft\n"
        "---\n\n"
        "# Test\n" + body_without_personal,
        encoding="utf-8",
    )
    result = run_script(tmp_path)
    assert result.returncode != 0
    assert "个人批注" in result.stdout or "个人批注" in result.stderr
