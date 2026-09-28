import subprocess
import tempfile
from pathlib import Path

SCRIPT = Path(__file__).resolve().parents[1] / "tools" / "check-schema.py"


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
        "# Test\n\nbody\n",
        encoding="utf-8",
    )
    result = run_script(tmp_path)
    assert result.returncode == 0, result.stdout + result.stderr
