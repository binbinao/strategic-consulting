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
