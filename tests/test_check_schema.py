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


def test_300_char_section_overflow_detected(tmp_path: Path):
    """300-char-per-section rule from AGENTS.md."""
    (tmp_path / "frameworks").mkdir()
    card = tmp_path / "frameworks" / "toolong.md"
    # Build a 核心内容 section with > 300 Chinese characters
    long_text = "一" * 305  # 305 Chinese chars
    card.write_text(
        "---\n"
        "name: 测试长\n"
        "name_en: Test Long\n"
        "source_company: [测试公司]\n"
        "category: framework\n"
        "created_year: 2020\n"
        "one_line_summary: 测试摘要。\n"
        "purpose: |\n  测试目的。\n"
        "when_to_use: |\n  - 测试。\n"
        "key_steps: [步骤]\n"
        "limitations: [限制]\n"
        "related_methods: []\n"
        "tags: [test]\n"
        "status: draft\n"
        "---\n\n"
        "# 测试长\n\n"
        "## 起源与定位\n短。\n\n"
        f"## 核心内容\n{long_text}\n\n"
        "## 适用与不适用\n短。\n\n"
        "## 局限与争议\n短。\n\n"
        "## 与其他方法论的关系\n短。\n\n"
        "## 个人批注\n<!-- 由所有者撰写 -->\n\n",
        encoding="utf-8",
    )
    result = run_script(tmp_path)
    assert result.returncode != 0
    assert "核心内容" in result.stdout or "核心内容" in result.stderr


def test_300_char_section_within_limit_passes(tmp_path: Path):
    """300-char-per-section limit is inclusive boundary."""
    (tmp_path / "frameworks").mkdir()
    card = tmp_path / "frameworks" / "ok.md"
    ok_text = "一" * 300  # exactly 300
    card.write_text(
        "---\n"
        "name: 测试\n"
        "name_en: Test\n"
        "source_company: [测试]\n"
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
        "---\n\n"
        "# 测试\n\n"
        "## 起源与定位\n短。\n\n"
        f"## 核心内容\n{ok_text}\n\n"
        "## 适用与不适用\n短。\n\n"
        "## 局限与争议\n短。\n\n"
        "## 与其他方法论的关系\n短。\n\n"
        "## 个人批注\n<!-- -->\n\n",
        encoding="utf-8",
    )
    result = run_script(tmp_path)
    assert result.returncode == 0, result.stdout + result.stderr


def test_personal_section_excluded_from_300_check(tmp_path: Path):
    """个人批注 is owner territory — never checked for length."""
    (tmp_path / "frameworks").mkdir()
    card = tmp_path / "frameworks" / "owner.md"
    long_text = "很" * 1000  # huge, in 个人批注
    card.write_text(
        "---\n"
        "name: 测试\n"
        "name_en: Test\n"
        "source_company: [测试]\n"
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
        "---\n\n"
        "# 测试\n\n"
        "## 起源与定位\n短。\n\n"
        "## 核心内容\n短。\n\n"
        "## 适用与不适用\n短。\n\n"
        "## 局限与争议\n短。\n\n"
        "## 与其他方法论的关系\n短。\n\n"
        f"## 个人批注\n{long_text}\n",
        encoding="utf-8",
    )
    result = run_script(tmp_path)
    assert result.returncode == 0, result.stdout + result.stderr
