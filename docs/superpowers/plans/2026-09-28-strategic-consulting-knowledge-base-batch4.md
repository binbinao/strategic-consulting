# Strategic Consulting Knowledge Base — Fourth Batch Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add 5 framework cards from "old strategy houses" (Monitor, Arthur D. Little, Booz/A.T. Kearney/PwC Strategy& lineage, A.T. Kearney, OC&C) to round out non-MBB coverage alongside the 21 cards delivered in batches 1-3.

**Architecture:** Same static Markdown + frontmatter pattern. Cards land in `frameworks/`. Net-new additions — no reciprocal links to close from prior batches (these are signature frameworks from firms previously underrepresented).

**Tech Stack:** Markdown (CommonMark + YAML frontmatter), Python 3 (validation scripts), git.

**Spec:** `docs/superpowers/specs/2026-09-28-strategic-consulting-knowledge-base-design.md` (unchanged)
**Previous plans:** see `docs/superpowers/plans/2026-09-28-strategic-consulting-knowledge-base{,-batch2,-batch3}.md`

## Global Constraints

Same as previous batches:

- UTF-8, LF line endings, H1 first line.
- 12 content fields + `status` in frontmatter.
- 6 body sections per card.
- Individual authors accepted in `source_company`.
- AI factual-layer rules: `[需核实]` for unverified facts, `[争议]` for contested claims, ~300 Chinese-character cap per factual section.
- AI does NOT write `## 个人批注` body content (owner work).
- Bilingual term-pair on first use.

## Files to create (5 framework cards)

| # | Card | Category | source_company | Approx. period |
|---|---|---|---|---|
| 1 | `frameworks/monitor-three-tests.md` | framework | Monitor Group | 1980s (Goold/Campbell) |
| 2 | `frameworks/adl-value-migration.md` | framework | Adrian Slywotzky (Arthur D. Little) | 1996 |
| 3 | `frameworks/booz-capabilities-driven-strategy.md` | framework | Booz Allen Hamilton + Wharton Mack Institute | 1990s-2000s |
| 4 | `frameworks/kearney-strategic-fitness.md` | framework | A.T. Kearney | 2000s |
| 5 | `frameworks/oc-c-where-to-play-how-to-win.md` | framework | OC&C Strategy Consultants | 2000s-2010s (popularized) |

## Files to modify

- `docs/methodology-catalog.md` — append 5 rows to Frameworks section (now 19 frameworks + 2 processes + 5 tools = 26 cards)
- `by-company/monitor.md` — append row for `monitor-three-tests`
- `by-company/arthur-d-little.md` — append row for `adl-value-migration`
- `by-company/strategyand.md` — append row for `booz-capabilities-driven-strategy`
- `by-company/at-kearney.md` — append row for `kearney-strategic-fitness`
- `by-company/oc-c.md` — append row for `oc-c-where-to-play-how-to-win`

## Out-of-scope

- Schema additions (case_examples, evolution_history) — still deferred per spec §14
- Owner fact-check + personal layer — owner work
- Reciprocal link work — these cards are net-new

---

## Task 1: 3 framework cards (Monitor Three Tests, ADL Value Migration, Booz Capabilities-Driven Strategy) + catalog/by-company updates

**Files (create):**
- `frameworks/monitor-three-tests.md`
- `frameworks/adl-value-migration.md`
- `frameworks/booz-capabilities-driven-strategy.md`

**Files (modify):**
- `docs/methodology-catalog.md` — append 3 rows to Frameworks
- `by-company/monitor.md` — append row for `monitor-three-tests`
- `by-company/arthur-d-little.md` — append row for `adl-value-migration`
- `by-company/strategyand.md` — append row for `booz-capabilities-driven-strategy`

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
  - `monitor-three-tests.md`: Michael Goold and Andrew Campbell, *Strategies and Styles* (1987) and *Designing Effective Organizations* — three tests: customer value test, competitive value test, feasibility test. Originally Monitor Group (acquired by Deloitte in 2013 as "Monitor Deloitte"). `source_company: ["Monitor Group"]`. `created_year: 1987`.
  - `adl-value-migration.md`: Adrian Slywotzky, *Value Migration* (1996, Harvard Business Review Press). The concept that value migrates between industry structures over time, often requiring companies to reinvent themselves. Slywotzky was at Arthur D. Little. `source_company: ["Adrian Slywotzky"]` (individual author) OR `["Arthur D. Little"]` (firm). Use individual author per the project convention for individual-first attribution. `created_year: 1996`.
  - `booz-capabilities-driven-strategy.md`: Booz Allen Hamilton / Wharton Mack Institute, capabilities-driven strategy work — focus on the few differentiating capabilities that drive competitive advantage. Co-developed across Booz Allen Hamilton (Booz & Company) and Wharton's Mack Institute. Note: Booz's strategy practice spun off as Booz & Company, then merged with PwC to form Strategy& in 2014. `source_company: ["Booz Allen Hamilton", "Wharton Mack Institute"]` (multi-source). `created_year: 2000` (round number for the firm work).

  For `related_methods` on each new card: populate naturally if there are clear conceptual connections to existing cards (e.g., `booz-capabilities-driven-strategy` could reference `[[value-chain]]` for activity-level decomposition). Don't fabricate links to non-existent cards.

- [ ] **Step 2: Implementer verifies**

  - `python3 tools/check-schema.py` passes
  - `python3 tools/check-links.py` passes
  - `python3 -m pytest tests/` — all 7 tests pass

- [ ] **Step 3: Commit**

  Single commit: `feat(frameworks): add 3 old-house signature cards (Monitor Three Tests, ADL Value Migration, Booz Capabilities-Driven Strategy)`.

---

## Task 2: 2 framework cards (Kearney Strategic Fitness, OC&C Where-to-Play/How-to-Win) + catalog/by-company updates

**Files (create):**
- `frameworks/kearney-strategic-fitness.md`
- `frameworks/oc-c-where-to-play-how-to-win.md`

**Files (modify):**
- `docs/methodology-catalog.md` — append 2 rows to Frameworks
- `by-company/at-kearney.md` — append row for `kearney-strategic-fitness`
- `by-company/oc-c.md` — append row for `oc-c-where-to-play-how-to-win`

**Interfaces:**
- Same as Task 1.

- [ ] **Step 1: Implementer writes both cards + modifications**

  Card-specific notes:
  - `kearney-strategic-fitness.md`: A.T. Kearney's "Strategic Fitness" framework — combines competitive position and operational efficiency into a single diagnostic. Used to assess strategic alignment. `source_company: ["A.T. Kearney"]`. `created_year: 2005` or so (the framework has been in use for some time; use `[需核实]` if uncertain of exact year).
  - `oc-c-where-to-play-how-to-win.md`: OC&C Strategy Consultants — "Where to Play / How to Win" framework for strategic choice clarity. While the phrases are common in strategy consulting, OC&C has used them as a signature methodology. `source_company: ["OC&C Strategy Consultants"]`. `created_year: 2005` (popularization period; use `[需核实]` if uncertain).

  Apply same template rules as Task 1.

- [ ] **Step 2: Implementer verifies**

  - `python3 tools/check-schema.py` passes
  - `python3 tools/check-links.py` passes
  - `python3 -m pytest tests/` — 7/7 pass

- [ ] **Step 3: Commit**

  Single commit: `feat(frameworks): add 2 old-house signature cards (Kearney Strategic Fitness, OC&C Where-to-Play/How-to-Win)`.

---

## Task 3: Cross-card consistency + final verification + README update

**Files:**
- Modify (if needed): any new card
- Modify (if needed): README "已收录方法论" + roadmap sections

**Interfaces:**
- Consumes: All 5 new cards + 21 existing cards
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
  - Tag vocabulary consistent (lowercase kebab-case)?
  - `created_year` integer format consistent?
  - `category` enum value correct?
  - Body section character counts under 300 cap?

- [ ] **Step 3: Apply trailing-newline fix**

  Add `\n` to any of the 5 new files that lack it (per the pattern from prior batches).

- [ ] **Step 4: Update README**

  Read `docs/methodology-catalog.md` (now 26 rows: 19 frameworks + 2 processes + 5 tools).

  Update `README.md` "已收录方法论" section:
  - Replace the "21 张" count with "26 张"
  - Add 5-row highlights table for batch-4 additions
  - Update roadmap: replace "进入第三批：覆盖 MBB + 四大其他招牌方法" with "第四批已交付：老牌战略所（Monitor / ADL / Booz / Kearney / OC&C）的招牌方法已收"

- [ ] **Step 5: Apply any fixes inline**

  If inconsistencies found in Step 2, fix them.

- [ ] **Step 6: Commit**

  - One commit for trailing newlines (mandatory)
  - One commit for README update (mandatory)
  - Optional commit for other consistency fixes

---

## Self-Review Notes

**Spec coverage**:
- §6 Schema → all 5 cards (Tasks 1, 2)
- §7 Body structure → all 5 cards (Tasks 1, 2)
- §9 AI rules → all 5 cards (Tasks 1, 2)
- §11 First batch 5 → 21 after batch 3 → 26 after batch 4

**Risks**:
- Implementer might write framework/method names without verification (Batch 1 lesson)
- "Capabilities-Driven Strategy" has contested attribution (Booz vs. Wharton Mack Institute vs. multiple co-authors) — needs careful `[需核实]` placement
- "Where to Play / How to Win" attribution to OC&C specifically is somewhat fuzzy (the phrases are common) — may need `[争议]`
- `created_year` for Kearney Strategic Fitness and OC&C Where-to-Play/How-to-Win may need `[需核实]`

**Type consistency**:
- `source_company` accepts multi-source list (Booz + Wharton)
- `source_company` accepts individual author (Slywotzky for ADL Value Migration)
- `category: framework` for all 5
- All `status: draft`

**Out-of-scope**:
- Schema additions still deferred
- Owner fact-check + personal layer still owner work