# Strategic Consulting Knowledge Base — Second Batch Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Close the loop on the first 5 cards by adding 11 related methodologies (originally referenced in the first batch but not yet built), with reciprocal backlinks restored.

**Architecture:** Pure static Markdown files with YAML frontmatter, same as first batch. Cards land in `frameworks/` / `processes/` / `tools/` by category. The 11 new cards each add a reciprocal `[[X]]` link back to the original first-batch card they were referenced from. The first-batch cards restore the `related_methods` references they had before Task 10's link-debt cleanup.

**Tech Stack:** Markdown (CommonMark + YAML frontmatter), Python 3 (validation scripts), git.

**Spec:** `docs/superpowers/specs/2026-09-28-strategic-consulting-knowledge-base-design.md` (unchanged)
**Plan-1 reference:** `docs/superpowers/plans/2026-09-28-strategic-consulting-knowledge-base.md` (unchanged)

## Global Constraints

Same as Plan 1 (see `docs/superpowers/specs/2026-09-28-strategic-consulting-knowledge-base-design.md` §6, §7, §9):

- UTF-8, LF line endings, H1 first line.
- 12 content fields + `status` in frontmatter.
- 6 body sections per card.
- Individual authors accepted in `source_company` (no `by-company/` entry for individual authors).
- Multi-company methods omit the company prefix in filenames.
- AI factual-layer rules: `[需核实]` for unverified facts, `[争议]` for contested claims, ~300 Chinese-character cap per factual section.
- AI does NOT write `## 个人批注` body content (owner work, current status stays `draft`).
- Bilingual term-pair on first use.

## File Structure (deltas)

### New files (11 cards)

| Card | Category | source_company | Reciprocal link from first batch |
|---|---|---|---|
| `frameworks/galbraith-star-model.md` | framework | Jay Galbraith | → `frameworks/mckinsey-7s.md` |
| `frameworks/bcg-organizational-advantage.md` | framework | Boston Consulting Group | → `frameworks/mckinsey-7s.md` |
| `frameworks/ge-mckinsey-matrix.md` | framework | General Electric + McKinsey & Company | → `frameworks/bcg-growth-share-matrix.md` |
| `frameworks/ashridge-portfolio-display.md` | framework | Ashridge | → `frameworks/bcg-growth-share-matrix.md` |
| `frameworks/adl-matrix.md` | framework | Arthur D. Little | → `frameworks/bcg-growth-share-matrix.md` |
| `frameworks/minto-pyramid-principle.md` | framework | Barbara Minto | → `processes/mece.md` |
| `processes/hypothesis-driven-problem-solving.md` | process | industry-wide (McKinsey canonical) | → `processes/mece.md` |
| `tools/value-chain.md` | tool | Michael Porter (Harvard) | → `tools/porters-five-forces.md` |
| `tools/pestel.md` | tool | industry-wide (Aguilar's PEST → PESTLE → PESTEL) | → `tools/porters-five-forces.md` |
| `tools/customer-effort-score.md` | tool | Customer Experience Benchmarking (CEBM) / industry-wide | → `frameworks/bain-net-promoter-system.md` |
| `tools/voice-of-customer.md` | tool | industry-wide | → `frameworks/bain-net-promoter-system.md` |

### Modified files

- `frameworks/mckinsey-7s.md` — restore `related_methods: ["[[galbraith-star-model]]", "[[bcg-organizational-advantage]]"]` (currently `[]`)
- `frameworks/bcg-growth-share-matrix.md` — restore `related_methods: ["[[ge-mckinsey-matrix]]", "[[ashridge-portfolio-display]]", "[[adl-matrix]]"]`
- `tools/porters-five-forces.md` — restore `related_methods: ["[[value-chain]]", "[[pestel]]"]`
- `processes/mece.md` — restore `related_methods: ["[[hypothesis-driven-problem-solving]]", "[[minto-pyramid-principle]]"]`
- `frameworks/bain-net-promoter-system.md` — restore `related_methods: ["[[customer-effort-score]]", "[[voice-of-customer]]"]`
- `docs/methodology-catalog.md` — append 11 rows (frameworks section gets 6, processes section gets 1, tools section gets 4)
- `by-company/bcg.md` — add row for `bcg-organizational-advantage`
- `by-company/mckinsey.md` — add row for `ge-mckinsey-matrix`
- `by-company/arthur-d-little.md` — add row for `adl-matrix`
- (Ashridge is not in `by-company/` — outside the 14 firm scope per spec. Don't add a by-company file. Note this in the card's `source_company`.)
- (CEBM is not in `by-company/` — outside scope. Same treatment.)

---

## Task 1: 6 framework cards + their catalog/by-company updates

**Files (create):**
- `frameworks/galbraith-star-model.md`
- `frameworks/bcg-organizational-advantage.md`
- `frameworks/ge-mckinsey-matrix.md`
- `frameworks/ashridge-portfolio-display.md`
- `frameworks/adl-matrix.md`
- `frameworks/minto-pyramid-principle.md`

**Files (modify):**
- `frameworks/mckinsey-7s.md` — restore `related_methods` to include `[[galbraith-star-model]]` and `[[bcg-organizational-advantage]]`
- `frameworks/bcg-growth-share-matrix.md` — restore `related_methods` to include `[[ge-mckinsey-matrix]]`, `[[ashridge-portfolio-display]]`, `[[adl-matrix]]`
- `processes/mece.md` — restore `related_methods` to include `[[minto-pyramid-principle]]` (only this one; the other, `[[hypothesis-driven-problem-solving]]`, will be added in Task 2 when that card is built)
- `docs/methodology-catalog.md` — append 6 framework rows
- `by-company/bcg.md` — append row for `bcg-organizational-advantage`
- `by-company/mckinsey.md` — append row for `ge-mckinsey-matrix`
- `by-company/arthur-d-little.md` — append row for `adl-matrix`

**Interfaces:**
- Consumes: existing `docs/schema.md`, `AGENTS.md`, the first-batch card files (read these to understand format)
- Produces: 6 framework cards at `status: draft`, plus reciprocal links + catalog + by-company updates

**Subagent dispatch:**
- One implementer subagent. Each card is 80-120 lines of structured content.
- The implementer writes all 6 cards byte-faithfully, restoring reciprocal links in the first-batch files.
- No per-card task. One subagent handles all 6 (within plan's "batch small same-shape work" guidance).

- [ ] **Step 1: Implementer writes all 6 cards + modifications**

  Use the established card template. For each card:
  - 12 content fields + `status: draft` in frontmatter
  - 6 body sections with substantive factual content (each section ~80-300 Chinese characters)
  - `## 个人批注` left as HTML-comment placeholder only
  - `**AI 建议**` left as HTML-comment placeholder only

  For reciprocal links in first-batch files: edit frontmatter `related_methods` to restore the original list (those fields were emptied in commit `0fca58a` per progress.md Task 10 notes).

  For `by-company/` updates: add a row to the appropriate file's `## 方法论索引` table with relative link to the new card.

  For `docs/methodology-catalog.md`: append rows to the correct section table (all 6 are frameworks).

- [ ] **Step 2: Implementer verifies**

  - `python3 tools/check-schema.py` should pass (all 6 new cards conform)
  - `python3 tools/check-links.py` should pass (reciprocal links resolve)

- [ ] **Step 3: Commit**

  Single commit: `feat(frameworks): add 6 second-batch framework cards with reciprocal links`.

---

## Task 2: 1 process card + 4 tool cards + their catalog updates

**Files (create):**
- `processes/hypothesis-driven-problem-solving.md`
- `tools/value-chain.md`
- `tools/pestel.md`
- `tools/customer-effort-score.md`
- `tools/voice-of-customer.md`

**Files (modify):**
- `processes/mece.md` — restore `related_methods` to include `[[hypothesis-driven-problem-solving]]` (the second piece that wasn't added in Task 1)
- `tools/porters-five-forces.md` — restore `related_methods` to include `[[value-chain]]`, `[[pestel]]`
- `frameworks/bain-net-promoter-system.md` — restore `related_methods` to include `[[customer-effort-score]]`, `[[voice-of-customer]]`
- `docs/methodology-catalog.md` — append 1 process row + 4 tool rows

(No by-company updates: `hypothesis-driven-problem-solving` (industry-wide/McKinsey canonical) goes to `by-company/mckinsey.md` since McKinsey is canonical — yes, add a row. `value-chain` is individual (Porter) — no by-company. `pestel` is industry-wide — could go to a new `by-company/industry-wide.md` if you want, but spec scope says no `shared/` mirror — so don't add it. `customer-effort-score` and `voice-of-customer` are industry-wide — same treatment, no by-company entry.)

**Interfaces:**
- Same as Task 1.

- [ ] **Step 1: Implementer writes all 5 cards + modifications**

  Same template. The implementer should:
  - Read the first-batch tool/process cards to match style
  - For `tools/value-chain.md` (Porter) and `tools/pestel.md` (Aguilar): `source_company` accepts individual authors
  - For `customer-effort-score.md`: `source_company: ["Customer Experience Benchmarking (CEBM)", "industry-wide"]` — CEBM is a community of practice, not a firm
  - For `voice-of-customer.md`: `source_company: ["industry-wide"]`
  - For `hypothesis-driven-problem-solving.md`: `source_company: ["industry-wide", "McKinsey & Company"]` (matches MECE pattern)
  - Reciprocal link updates: add `[[hypothesis-driven-problem-solving]]` to `processes/mece.md`'s `related_methods` (alongside the `[[minto-pyramid-principle]]` already restored in Task 1)

- [ ] **Step 2: Implementer verifies**

  - `python3 tools/check-schema.py` passes
  - `python3 tools/check-links.py` passes
  - `python3 -m pytest tests/` — all 7 tests still pass

- [ ] **Step 3: Commit**

  Single commit: `feat(processes,tools): add 5 second-batch cards with reciprocal links`.

---

## Task 3: Cross-card consistency + final verification

**Files:**
- Modify (if needed): any of the new cards based on inconsistencies found
- Modify (if needed): `docs/methodology-catalog.md` row alignment

**Interfaces:**
- Consumes: All 11 new cards + 5 first-batch cards + restored reciprocal links
- Produces: Verification report

- [ ] **Step 1: Run all validation**

  ```bash
  python3 tools/check-schema.py
  python3 tools/check-links.py
  python3 -m pytest tests/ -v
  ```

  All three must pass. If any fails, investigate and fix the underlying issue (don't paper over).

- [ ] **Step 2: Cross-card consistency check**

  For each of the 11 new cards:
  - Tag vocabulary consistent (same lowercase kebab-case across all 16 cards)?
  - `created_year` integer format consistent?
  - `category` enum value correct?
  - Any orphaned `[[X]]` wikilinks? (should all resolve now)
  - Any double-listed wikilinks? (each pair should be exactly two-way)

- [ ] **Step 3: Apply any fixes inline**

  If inconsistencies found, fix them. If schema.md needs adjustment, edit it.

- [ ] **Step 4: Commit fixes if any**

  Single commit if changes: `refactor: cross-card consistency after second batch`.

---

## Self-Review Notes

**Plan coverage check** (spec section → task):
- §6 Schema → all 11 cards (Tasks 1, 2)
- §7 Body structure → all 11 cards (Tasks 1, 2)
- §9 AI rules → all 11 cards + reciprocal link work (Tasks 1, 2)
- §11 First batch was 5 cards → batch 2 adds 11 cards; same shape, same constraints
- §14 Open questions → still deferred (no new fields added)

**Risks**:
- Implementer might miss the reciprocal-link-back part (the value of this batch is closing the loop, not just adding more cards)
- Implementer might confuse CEBM (community of practice) with a firm — needs to be in `source_company` but not in `by-company/`
- Implementer might mark too many things `[争议]` (controversial content is fine; over-marking is noise)

**Type consistency check**:
- `source_company` accepts both firms and individual authors (validated by first batch's Porter entry)
- `category` enum: framework / process / tool
- `status` lifecycle: draft / fact-checked / annotated / archived

**Out-of-scope**:
- Schema additions (case_examples, evolution_history) — still deferred per spec §14
- New `by-company/` files (industry-wide, Ashridge, CEBM) — out of scope; spec §2 only lists 14 firms
- Owner fact-check + personal layer — owner work, not AI