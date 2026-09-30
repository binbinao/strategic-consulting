# Strategic Consulting Knowledge Base — Third Batch Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add 5 MBB-originated signature methodology cards that fill out the McKinsey / BCG / Bain coverage alongside the existing first-batch and second-batch cards.

**Architecture:** Same static Markdown + frontmatter pattern as previous batches. Cards land in `frameworks/` (all 5 are frameworks). No reciprocal links to first/second-batch cards (these 5 are net-new additions, not closes of the original 11 dangling references).

**Tech Stack:** Markdown (CommonMark + YAML frontmatter), Python 3 (validation scripts), git.

**Spec:** `docs/superpowers/specs/2026-09-28-strategic-consulting-knowledge-base-design.md` (unchanged)
**Batch-1 plan:** `docs/superpowers/plans/2026-09-28-strategic-consulting-knowledge-base.md` (unchanged)
**Batch-2 plan:** `docs/superpowers/plans/2026-09-28-strategic-consulting-knowledge-base-batch2.md` (unchanged)

## Global Constraints

Same as previous batches:

- UTF-8, LF line endings, H1 first line.
- 12 content fields + `status` in frontmatter.
- 6 body sections per card.
- Individual authors accepted in `source_company` (no `by-company/` entry for individual authors).
- AI factual-layer rules: `[需核实]` for unverified facts, `[争议]` for contested claims, ~300 Chinese-character cap per factual section.
- AI does NOT write `## 个人批注` body content (owner work, current status stays `draft`).
- Bilingual term-pair on first use.

## Files to create (5 framework cards)

| # | Card | Category | source_company | Approx. period |
|---|---|---|---|---|
| 1 | `frameworks/bcg-experience-curve.md` | framework | Boston Consulting Group | 1960s (foundational, parallel to BCG Matrix) |
| 2 | `frameworks/mckinsey-three-horizons.md` | framework | McKinsey & Company | 2000s |
| 3 | `frameworks/porter-generic-strategies.md` | framework | Michael Porter (Harvard) | 1980s (foundational strategy) |
| 4 | `frameworks/bcg-smart-simplicity.md` | framework | Boston Consulting Group | 2013 (newer signature) |
| 5 | `frameworks/bain-repeatable-model.md` | framework | Bain & Company | 2000s |

## Files to modify

- `docs/methodology-catalog.md` — append 5 rows to Frameworks section
- `by-company/bcg.md` — append 2 rows (BCG Experience Curve + BCG Smart Simplicity)
- `by-company/mckinsey.md` — append 1 row (McKinsey Three Horizons)
- `by-company/bain.md` — append 1 row (Bain Repeatable Model)

NO `by-company/` update for `porter-generic-strategies.md` (Porter is individual author, no by-company per spec scope).

## Out-of-scope / not in this batch

- Schema additions (case_examples, evolution_history) — still deferred per spec §14
- New `by-company/` files — still out of scope; spec §2 only lists 14 firms
- Owner fact-check + personal layer — owner work, not AI
- Reciprocal link work — these 5 cards are net-new, not closing loops from prior batches
- Validator strengthening (300-char cap enforcement, when_to_use type check) — deferred to future work

---

## Task 1: 3 framework cards (BCG Experience Curve, McKinsey 3 Horizons, Porter Generic Strategies) + catalog/by-company updates

**Files (create):**
- `frameworks/bcg-experience-curve.md`
- `frameworks/mckinsey-three-horizons.md`
- `frameworks/porter-generic-strategies.md`

**Files (modify):**
- `docs/methodology-catalog.md` — append 3 rows to Frameworks
- `by-company/bcg.md` — append row for `bcg-experience-curve`
- `by-company/mckinsey.md` — append row for `mckinsey-three-horizons`

**Interfaces:**
- Consumes: existing `docs/schema.md`, `AGENTS.md`, prior-batch card files for style reference
- Produces: 3 framework cards at `status: draft`, plus catalog + by-company updates

- [ ] **Step 1: Implementer writes all 3 cards + modifications**

  For each card:
  - 12 content fields + `status: draft` in frontmatter
  - 6 body sections with substantive factual content (each section ~80-300 Chinese characters, well under cap)
  - `## 个人批注` left as HTML-comment placeholder only
  - `**AI 建议**` left as HTML-comment placeholder only
  - Use `[需核实]` for unverified years/authors; `[争议]` for contested claims
  - Bilingual term pairs on first use

  Card-specific notes:
  - `bcg-experience-curve.md`: origin Bruce Henderson, 1960s, parallels BCG Growth-Share Matrix
  - `mckinsey-three-horizons.md`: origin Mehrdad Baghai / McKinsey, codified 2000s (Baghai's 1999 *The Leap to Leadership* book / HBR articles)
  - `porter-generic-strategies.md`: Michael Porter, "Three Generic Strategies" (cost leadership / differentiation / focus), 1980s HBR and *Competitive Strategy* (1980)

  For `related_methods` on each new card: populate naturally if there are clear conceptual connections to other cards (e.g., `bcg-experience-curve` could link back to `bcg-growth-share-matrix` for context). Don't fabricate links to non-existent cards.

  For `by-company/` updates: append rows with relative links to the new card files.

- [ ] **Step 2: Implementer verifies**

  - `python3 tools/check-schema.py` passes
  - `python3 tools/check-links.py` passes
  - `python3 -m pytest tests/` — all 7 tests pass

- [ ] **Step 3: Commit**

  Single commit: `feat(frameworks): add 3 MBB signature cards (BCG Experience Curve, McKinsey 3 Horizons, Porter Generic Strategies)`.

---

## Task 2: 2 framework cards (BCG Smart Simplicity, Bain Repeatable Model) + catalog/by-company updates

**Files (create):**
- `frameworks/bcg-smart-simplicity.md`
- `frameworks/bain-repeatable-model.md`

**Files (modify):**
- `docs/methodology-catalog.md` — append 2 rows to Frameworks
- `by-company/bcg.md` — append row for `bcg-smart-simplicity`
- `by-company/bain.md` — append row for `bain-repeatable-model`

**Interfaces:**
- Same as Task 1.

- [ ] **Step 1: Implementer writes both cards + modifications**

  Card-specific notes:
  - `bcg-smart-simplicity.md`: BCG senior partners (Eric Grehan, Yves Morieux), HBR 2013 article + book "Six Simple Rules" 2014. Modern organizational design.
  - `bain-repeatable-model.md`: Bain methodology. Identify 5-7 elements that make the business successful; codify and replicate. Associated with "Bain Vector" growth diagnostic and earlier "Repeatable Model of business success" work.

  Apply same template rules as Task 1.

- [ ] **Step 2: Implementer verifies**

  - `python3 tools/check-schema.py` passes
  - `python3 tools/check-links.py` passes
  - `python3 -m pytest tests/` — 7/7 pass

- [ ] **Step 3: Commit**

  Single commit: `feat(frameworks): add 2 MBB signature cards (BCG Smart Simplicity, Bain Repeatable Model)`.

---

## Task 3: Cross-card consistency + final verification

**Files:**
- Modify (if needed): any new card
- Modify (if needed): README "已收录方法论" table

**Interfaces:**
- Consumes: All 5 new cards + 16 existing cards
- Produces: Verification report + README update

- [ ] **Step 1: Run all validation**

  ```bash
  python3 tools/check-schema.py
  python3 tools/check-links.py
  python3 -m pytest tests/ -v
  ```

  All three must pass.

- [ ] **Step 2: Cross-card consistency check**

  For each of the 5 new cards:
  - Tag vocabulary consistent (same lowercase kebab-case)?
  - `created_year` integer format consistent?
  - `category` enum value correct?
  - Body section character counts under 300 cap?
  - Any double-listed or non-reciprocal wikilinks?

- [ ] **Step 3: Update README "已收录方法论" table**

  Read `docs/methodology-catalog.md` (now 21 rows) and update `README.md`'s "已收录方法论" section to reflect 21 cards (12 frameworks + 2 processes + 5 tools + 2 more frameworks... wait, recount).

  Actually: 9 frameworks + 2 processes + 5 tools = 16 (after batch 2). + 5 frameworks in batch 3 = 14 frameworks + 2 processes + 5 tools = 21 cards total.

  Update the README table to show all 21 cards (or keep the table compact and point to the catalog). Decide which is better — for 21 cards, a full table is heavy; a pointer to catalog + summary counts may be cleaner. Either approach is acceptable; pick what's natural for the README's tone.

- [ ] **Step 4: Apply any fixes inline**

  If inconsistencies found in Step 2, fix them.

- [ ] **Step 5: Commit**

  - One commit for README update: `docs: update README to reflect 21 cards after batch 3`
  - One commit for any other fixes (if needed)

---

## Self-Review Notes

**Spec coverage** (spec section → task):
- §6 Schema → all 5 cards (Tasks 1, 2)
- §7 Body structure → all 5 cards (Tasks 1, 2)
- §9 AI rules → all 5 cards (Tasks 1, 2)
- §11 First batch was 5 cards → batch 2 added 11, batch 3 adds 5; total 21

**Risks**:
- Implementer might write framework/method names in "与其他方法论的关系" without verification (Batch 1 lesson)
- Implementer might over-mark `[需核实]` (calibration, not noise)
- Implementer might confuse "Repeatable Model" name with alternative spellings (Bain & Co's terminology varies across publications)

**Type consistency**:
- `source_company` accepts both firms (BCG, McKinsey, Bain) and individual authors (Porter)
- `category: framework` for all 5
- All `status: draft`

**Out-of-scope**:
- Schema additions still deferred
- Owner fact-check + personal layer still owner work
- No reciprocal links expected (these are net-new, not closes)