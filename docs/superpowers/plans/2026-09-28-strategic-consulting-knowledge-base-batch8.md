# Strategic Consulting Knowledge Base — Eighth Batch (Validator Strengthening) Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Strengthen the validation scripts (`tools/check-schema.py` + `tools/check-links.py`) so the AGENTS.md rules are enforced mechanically, not just reviewer-enforced.

**Architecture:** Pure Python work — extends existing scripts, adds pytest tests. No card content changes in this batch (existing-card fixes are a separate concern).

**Tech Stack:** Python 3, pytest.

**Spec:** `docs/superpowers/specs/2026-09-28-strategic-consulting-knowledge-base-design.md` (unchanged)
**Previous plans:** `docs/superpowers/plans/2026-09-28-strategic-consulting-knowledge-base{,-batch2,-batch3,-batch4,-batch5,-batch6,-batch7}.md`

## Global Constraints

- TDD discipline for each new validator (write failing test → implement → verify)
- Don't break existing 7 pytest tests
- All existing 33 cards must still pass after the new validators are added (otherwise existing-card fixes are needed — see Task 5)
- Match existing script style (`check-schema.py`, `check-links.py` use simple text parsing, no PyYAML dependency — keep that)

## Validator enhancements

### 1. 300-char-per-section check (in `tools/check-schema.py`)

Per AGENTS.md "每个事实层 section 不超过 300 中文字". The 5 factual sections (起源与定位 / 核心内容 / 适用与不适用 / 局限与争议 / 与其他方法论的关系) should each be ≤ 300 Chinese characters.

**NOT checked**: `## 个人批注` (owner territory, always empty placeholder)

**Counting**: Chinese characters = Unicode CJK Unified Ideographs range (U+4E00 to U+9FFF). English/punctuation not counted.

**Error format**: `"<path>: section <section> has <N> Chinese characters (>300 max)"`

### 2. `when_to_use` type enforcement (in `tools/check-schema.py`)

Per Batch 5 fix-round convention (now standard): `when_to_use` must be a string (block scalar `|`), NOT a YAML list.

**Error format**: `"<path>: when_to_use must be a string (block scalar), not a list"`

### 3. by-company reverse validation (in `tools/check-links.py`)

For each `by-company/*.md` entry's relative link to a card file, verify that the target card's `source_company` array includes a value that maps to the by-company file.

**Mapping table** (add to `check-links.py`):
| by-company file | expected canonical firm name(s) |
|---|---|
| `mckinsey.md` | `McKinsey & Company` |
| `bcg.md` | `Boston Consulting Group` |
| `bain.md` | `Bain & Company` |
| `deloitte.md` | `Deloitte` |
| `accenture-strategy.md` | `Accenture Strategy` |
| `pwc-strategy.md` | `PwC Strategy&` (also matches `Booz & Company` for legacy Booz→PwC lineage cards) |
| `ey-parthenon.md` | `EY-Parthenon` |
| `roland-berger.md` | `Roland Berger` |
| `lek.md` | `L.E.K. Consulting` |
| `at-kearney.md` | `A.T. Kearney` |
| `strategyand.md` | `Booz & Company` (legacy Booz lineage) |
| `monitor.md` | `Monitor Group` |
| `arthur-d-little.md` | `Arthur D. Little` |
| `oliver-wyman.md` | `Oliver Wyman` |
| `oc-c.md` | `OC&C Strategy Consultants` |

**Error format**: `"<by-company file>: <card filename> linked but source_company does not include <expected firm>"`

**Known edge case (current state)**: `frameworks/adl-value-migration.md` has `source_company: ["Adrian Slywotzky", "Mercer Management Consulting"]` but is indexed in `by-company/arthur-d-little.md`. This will fail the new validator. Task 5 will fix this drift.

---

## Files to modify

- `tools/check-schema.py` — add 2 new checks (300-char + when_to_use type)
- `tools/check-links.py` — add 1 new check (by-company reverse)
- `tests/test_check_schema.py` — add test cases for new schema checks
- `tests/test_check_links.py` — add test cases for new link check

## Files to potentially modify (Task 5)

If the new validators flag existing-card violations, fix them. Likely:
- `frameworks/adl-value-migration.md` — if `by-company/arthur-d-little.md` row gets flagged, remove the row (Slywotzky was at Mercer, not ADL)
- `frameworks/adl-matrix.md` — if its 起源与定位 or other sections exceed 300 chars, trim

(Plan will be updated at final review to enumerate specific fixes.)

---

## Task 1: 300-char-per-section check (TDD)

**Files (modify):**
- `tools/check-schema.py`
- `tests/test_check_schema.py`

- [ ] **Step 1: Write failing test**

  Add to `tests/test_check_schema.py`:

  ```python
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
  ```

- [ ] **Step 2: Run test to confirm it fails**

  Run: `python3 -m pytest tests/test_check_schema.py -v`

  Expected: FAIL with "function not defined" or AttributeError on the new check.

- [ ] **Step 3: Implement the 300-char check**

  In `tools/check-schema.py`, add to `validate_card()`:

  ```python
  MAX_FACTUAL_SECTION_CHARS = 300
  FACTUAL_SECTIONS = [
    "## 起源与定位",
    "## 核心内容",
    "## 适用与不适用",
    "## 局限与争议",
    "## 与其他方法论的关系",
  ]

  def _count_chinese_chars(text: str) -> int:
      return sum(1 for c in text if '\u4e00' <= c <= '\u9fff')

  def _section_body_length(card_text: str, section_heading: str) -> int:
      # Find the section heading, then count chinese chars until next ## heading or EOF
      idx = card_text.find(section_heading)
      if idx < 0:
          return 0
      start = idx + len(section_heading)
      # Find next ## heading
      next_heading = card_text.find("\n## ", start)
      if next_heading < 0:
          body = card_text[start:]
      else:
          body = card_text[start:next_heading]
      return _count_chinese_chars(body)

  # In validate_card(), after the body-section check:
  for section in FACTUAL_SECTIONS:
      n = _section_body_length(text, section)
      if n > MAX_FACTUAL_SECTION_CHARS:
          errors.append(f"{path}: section '{section.lstrip('# ').strip()}' has {n} Chinese characters (>300 max)")
  ```

- [ ] **Step 4: Run test to confirm it passes**

  Run: `python3 -m pytest tests/test_check_schema.py -v`

  Expected: PASS (3 new tests + 7 existing = 10 total).

- [ ] **Step 5: Run against real cards**

  Run: `python3 tools/check-schema.py`

  Expected: Either all 33 cards pass, OR some cards get flagged for being over-cap. If any flagged, document for Task 5 cleanup.

- [ ] **Step 6: Commit**

  Single commit: `feat(tools): enforce 300-char-per-factual-section limit in check-schema.py`.

---

## Task 2: `when_to_use` type enforcement (TDD)

**Files (modify):**
- `tools/check-schema.py`
- `tests/test_check_schema.py`

- [ ] **Step 1: Write failing test**

  Add to `tests/test_check_schema.py`:

  ```python
  def test_when_to_use_as_list_detected(tmp_path: Path):
      """when_to_use must be a string, not a list (Batch 5 lesson)."""
      (tmp_path / "frameworks").mkdir()
      card = tmp_path / "frameworks" / "badlist.md"
      card.write_text(
          "---\n"
          "name: 测试\n"
          "name_en: Test\n"
          "source_company: [测试]\n"
          "category: framework\n"
          "created_year: 2020\n"
          "one_line_summary: 测试。\n"
          "purpose: |\n  测试。\n"
          "when_to_use:\n"
          "  - 适用：a\n"
          "  - 不适用：b\n"
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
          "## 个人批注\n<!-- -->\n\n",
          encoding="utf-8",
      )
      result = run_script(tmp_path)
      assert result.returncode != 0
      assert "when_to_use" in result.stdout or "when_to_use" in result.stderr

  def test_when_to_use_as_block_scalar_passes(tmp_path: Path):
      """when_to_use as `|` block scalar is the canonical form."""
      (tmp_path / "frameworks").mkdir()
      card = tmp_path / "frameworks" / "good.md"
      card.write_text(
          "---\n"
          "name: 测试\n"
          "name_en: Test\n"
          "source_company: [测试]\n"
          "category: framework\n"
          "created_year: 2020\n"
          "one_line_summary: 测试。\n"
          "purpose: |\n  测试。\n"
          "when_to_use: |\n  - 适用：a\n  - 不适用：b\n"
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
          "## 个人批注\n<!-- -->\n\n",
          encoding="utf-8",
      )
      result = run_script(tmp_path)
      assert result.returncode == 0, result.stdout + result.stderr
  ```

- [ ] **Step 2: Run test to confirm it fails**

  Run: `python3 -m pytest tests/test_check_schema.py::test_when_to_use_as_list_detected -v`

  Expected: FAIL (function not implemented).

- [ ] **Step 3: Implement the when_to_use type check**

  In `tools/check-schema.py`, add to `validate_card()`:

  ```python
  if "when_to_use" in fm and not isinstance(fm["when_to_use"], str):
      errors.append(
          f"{path}: when_to_use must be a string (block scalar), "
          f"got {type(fm['when_to_use']).__name__}"
      )
  ```

- [ ] **Step 4: Run tests to confirm pass**

  Run: `python3 -m pytest tests/test_check_schema.py -v`

  Expected: PASS (5 new tests in schema file + 7 existing = 12 total, plus 2 new link tests in Task 3 = 14 total).

- [ ] **Step 5: Run against real cards**

  Run: `python3 tools/check-schema.py`

  Expected: All 33 cards pass (customer-effort-score.md was already fixed in batch 6).

- [ ] **Step 6: Commit**

  Single commit: `feat(tools): enforce when_to_use block-scalar type in check-schema.py`.

---

## Task 3: by-company reverse validation (TDD)

**Files (modify):**
- `tools/check-links.py`
- `tests/test_check_links.py`

- [ ] **Step 1: Write failing test**

  Add to `tests/test_check_links.py`:

  ```python
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
  ```

- [ ] **Step 2: Run test to confirm it fails**

  Run: `python3 -m pytest tests/test_check_links.py::test_by_company_link_without_source_company_match_detected -v`

  Expected: FAIL (check not implemented).

- [ ] **Step 3: Implement by-company reverse check**

  In `tools/check-links.py`, add a mapping and a new check function:

  ```python
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

  def check_by_company_index(root: Path) -> list[str]:
      """For each by-company row linking to a card, verify source_company match."""
      errors = []
      for bc_file, expected_firms in BY_COMPANY_FIRMS.items():
          bc_path = root / "by-company" / bc_file
          if not bc_path.exists():
              continue
          # Read frontmatter of each linked card
          for card_path, root_dir in [(root / "frameworks", "frameworks"),
                                       (root / "processes", "processes"),
                                       (root / "tools", "tools")]:
              if not card_path.exists():
                  continue
              # Find rows in by-company that reference cards
              bc_text = bc_path.read_text(encoding="utf-8")
              for link_match in re.finditer(r"\((?:\.\./)*(frameworks|processes|tools)/([^)]+)\.md\)", bc_text):
                  folder, slug = link_match.group(1), link_match.group(2)
                  target = root / folder / f"{slug}.md"
                  if not target.exists():
                      continue
                  target_text = target.read_text(encoding="utf-8")
                  target_fm = parse_frontmatter(target_text)  # reuse existing parser
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
  ```

  Wire this into `main()` (or equivalent entry point) of `check-links.py` — append errors to the output and exit with non-zero if any.

- [ ] **Step 4: Run tests to confirm pass**

  Run: `python3 -m pytest tests/test_check_links.py -v`

  Expected: PASS (4 tests in link file).

- [ ] **Step 5: Run against real by-company files**

  Run: `python3 tools/check-links.py`

  Expected: All 14 by-company files pass EXCEPT possibly `by-company/arthur-d-little.md` linking to `frameworks/adl-value-migration.md` (Slywotzky was at Mercer, not ADL — known edge case documented above).

- [ ] **Step 6: Commit**

  Single commit: `feat(tools): add by-company reverse validation in check-links.py`.

---

## Task 4: Apply existing-card fixes for any new validator violations

**Files (likely modify):**
- `by-company/arthur-d-little.md` — remove the ADL 价值迁移 row (Slywotzky was at Mercer, not ADL)
- `frameworks/adl-value-migration.md` — verify frontmatter is `[Adrian Slymer, Mercer Management Consulting]` (no change needed if so)
- Any cards flagged by the 300-char check (likely `frameworks/adl-matrix.md`, possibly others — check during Task 1 Step 5)
- `docs/methodology-catalog.md` — update ADL 价值迁移 row's `by-company` reference if needed (actually no — the catalog has a `company` column, not `by-company`)

- [ ] **Step 1: Run all 3 validators + pytest**

  Document the violations.

- [ ] **Step 2: Apply minimal fixes**

  For each violation, apply the smallest fix that resolves it. Don't refactor.

- [ ] **Step 3: Re-run validators + pytest**

  Confirm all 33 cards pass, all 7 + N new pytest tests pass.

- [ ] **Step 4: Commit**

  Single commit: `chore: fix existing-card violations surfaced by new validators`.

---

## Task 5: README update + cross-card consistency

- [ ] **Step 1: Update README validator section**

  Update README's "验证工具" section to reflect:
  - `check-schema.py` now also checks 300-char-per-section + when_to_use type
  - `check-links.py` now also checks by-company reverse validity

- [ ] **Step 2: Run all validators + pytest**

  Confirm all green.

- [ ] **Step 3: Commit**

  Single commit: `docs: update README to describe new validator checks`.

---

## Self-Review Notes

**Risks**:
- Some existing cards may fail new validators → Task 4 cleans up
- The by-company reverse check requires a careful mapping table; misconfiguring will produce false positives

**Type consistency**:
- `when_to_use` is always string (block scalar `|`) after this batch
- All 33 cards have valid `source_company` after Task 4 cleanup

**Out-of-scope**:
- PyYAML replacement of heuristic frontmatter parser — separate future task
- AGENTS.md updates — no changes needed (rules already exist, just enforced mechanically)
- Schema validator additions for any other AGENTS.md rules