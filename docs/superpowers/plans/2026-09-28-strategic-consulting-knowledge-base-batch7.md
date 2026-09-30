# Strategic Consulting Knowledge Base — Seventh Batch (Polish) Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Apply focused polish fixes surfaced in prior-batch reviews. Single batch, low-risk changes.

**Architecture:** Targeted edits to existing files. No new cards. No schema changes.

**Tech Stack:** Markdown, git.

**Spec:** `docs/superpowers/specs/2026-09-28-strategic-consulting-knowledge-base-design.md` (unchanged)
**Previous plans:** `docs/superpowers/plans/2026-09-28-strategic-consulting-knowledge-base{,-batch2,-batch3,-batch4,-batch5,-batch6}.md`

## Global Constraints

- Minimum-diff principle: only edit what's listed below
- Don't refactor unrelated content
- Don't change `## 个人批注` (owner territory)
- Match established card style (already-converged conventions from prior batches)

## Polish items (from prior-batch final reviews)

| # | Issue | File | Fix |
|---|---|---|---|
| 1 | Catalog row for ADL Value Migration says `Adrian Slywotzky`; README highlights table says `Adrian Slywotzky（Mercer Management Consulting）` — drift between surfaces | `docs/methodology-catalog.md` | Update catalog cell to `Adrian Slywotzky（Mercer Management Consulting）` to match README highlights. Frontmatter on the card already has multi-source `[Adrian Slywotzky, Mercer Management Consulting]`. |
| 2 | "14 家公司" wording in README is incorrect — by-company actually has 15 files (PwC Strategy& and Strategy& legacy are split). Catalog and spec both use 14 conceptual firms. | `README.md` | Note: keep "14 家公司（conception）" wording but add a clarifying note in the 收录范围 row that there are 15 by-company files (the 14 conceptual firms + the PwC/Strategy& legacy split). Easier: leave spec at 14 conceptual firms, accept the 14 vs 15 file mismatch as a known artifact. **Decision**: Update line 24 from "（14 家）" to "（14 家 / 15 个 by-company 文件，因为 PwC Strategy& 与 Strategy& legacy 分列）" |
| 3 | README batch-5 description says "3 张老牌战略所招牌方法 + 1 张工具" — wording off; should just be "3 张" | `README.md` line 120 | Fix wording to "**第五批新增（3 张老牌战略所招牌方法）**：" |
| 4 | README batch-6 description says "Big Four first entry" — verify clarity, may need small polish | `README.md` | Verify after fix #3 |
| 5 | "Booz & Company / PwC Strategy&" formatting in catalog row vs README: catalog uses slash " / " — consistent now | none | (verification only, no edit) |

## Files to modify

- `docs/methodology-catalog.md` — update row for `adl-value-migration` to reflect Mercer attribution
- `README.md` — wording fixes on 2 lines

## Files to verify (no edits expected, just confirm consistency)

- `frameworks/mckinsey-three-horizons.md` — confirm "三horizons" naming (deferred to owner fact-check)
- `frameworks/adl-value-migration.md` — frontmatter already has multi-source

---

## Task 1: Polish fixes + cross-card consistency verification

**Files (modify):**
- `docs/methodology-catalog.md` (1 row update)
- `README.md` (2 wording fixes)

- [ ] **Step 1: Apply catalog fix**

  In `docs/methodology-catalog.md`, find the row:
  ```
  | ADL 价值迁移 | Adrian Slywotzky | 1996 | draft |
  ```
  Change the company column to:
  ```
  | ADL 价值迁移 | Adrian Slywotzky（Mercer Management Consulting） | 1996 | draft |
  ```

- [ ] **Step 2: Apply README fix 1**

  In `README.md`, find line 24 (the 收录范围 row) which currently says "(14 家)" inline:
  ```
  | **公司** | McKinsey、BCG、Bain、Deloitte、Accenture Strategy、PwC Strategy&、EY-Parthenon、Roland Berger、L.E.K.、A.T. Kearney、Strategy&（legacy）、Monitor、Arthur D. Little、Oliver Wyman、OC&C（14 家） |
  ```

  Change the parenthetical to clarify the file count:
  ```
  | **公司** | McKinsey、BCG、Bain、Deloitte、Accenture Strategy、PwC Strategy&、EY-Parthenon、Roland Berger、L.E.K.、A.T. Kearney、Strategy&（legacy）、Monitor、Arthur D. Little、Oliver Wyman、OC&C（14 家 / 15 个 by-company 文件，因 PwC Strategy& 与 Strategy& legacy 分列） |
  ```

- [ ] **Step 3: Apply README fix 2**

  In `README.md`, find line ~120:
  ```
  **第五批新增（3 张老牌战略所招牌方法 + 1 张工具）**：
  ```
  Change to:
  ```
  **第五批新增（3 张老牌战略所招牌方法）**：
  ```

- [ ] **Step 4: Verify and commit**

  Run validation scripts (should still pass — pure text changes):
  ```bash
  python3 tools/check-schema.py
  python3 tools/check-links.py
  python3 -m pytest tests/
  ```

  Commit (single commit: `docs: polish catalog/headmatter alignment + README wording fixes`)

- [ ] **Step 5: Self-review**

  - Did I apply all 3 text fixes (catalog row + 2 README wording)?
  - Do all 3 validators still pass?
  - Is the commit message descriptive?

---

## Self-Review Notes

**Scope**: Pure documentation polish. No new content, no schema changes, no card content changes.

**Risks**:
- Very low. Pure text edits. Worst case: README table formatting breaks (verify visually).

**Type consistency**:
- Catalog and README should both now have ADL Value Migration attributed to "Adrian Slywotzky（Mercer Management Consulting）"
- This matches the frontmatter `source_company: ["Adrian Slywotzky", "Mercer Management Consulting"]` on the card

**Out-of-scope (deferred)**:
- "三horizons" naming — owner fact-check time concern
- Bilingual term gaps in batch 6 cards — minor fillers
- `[争议]` one-sided markers — matches existing convention across all 29 cards