# Strategic Consulting Knowledge Base — Sixth Batch Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** First-entry cards for the 4 Big Four strategy practices (Deloitte, Accenture Strategy, PwC Strategy&, EY-Parthenon), completing the 14-firm coverage specified in spec §2.

**Architecture:** Same static Markdown + frontmatter pattern. All 4 are frameworks.

**Tech Stack:** Markdown, Python 3 (validation scripts), git.

**Spec:** `docs/superpowers/specs/2026-09-28-strategic-consulting-knowledge-base-design.md` (unchanged)
**Previous plans:** see `docs/superpowers/plans/2026-09-28-strategic-consulting-knowledge-base{,-batch2,-batch3,-batch4,-batch5}.md`

## Global Constraints

Same as previous batches:

- UTF-8, LF line endings, H1 first line.
- 12 content fields + `status` in frontmatter.
- 6 body sections per card.
- AI factual-layer rules: `[需核实]` for unverified facts, `[争议]` for contested claims, ~300 Chinese-character cap per factual section.
- AI does NOT write `## 个人批注` body content (owner work).
- Bilingual term-pair on first use.
- **Use `|`-style block scalar for `when_to_use`** (not YAML list — Batch 5 fix-round lesson).
- **Trailing newlines required** on all .md files (Batch 5 fix-round lesson).

## Files to create (4 framework cards)

| # | Card | Category | source_company | Notes |
|---|---|---|---|---|
| 1 | `frameworks/pwc-fit-for-growth.md` | framework | PwC Strategy& | Fit-for-Growth (Booz lineage) |
| 2 | `frameworks/ey-parthenon-multi-sided-platform.md` | framework | EY-Parthenon | Multi-Sided Platform strategy |
| 3 | `frameworks/deloitte-business-chemistry.md` | framework | Deloitte | Business Chemistry (Human Capital) |
| 4 | `frameworks/accenture-industry-x.md` | framework | Accenture Strategy | Industry X framework |

## Files to modify

- `docs/methodology-catalog.md` — append 4 rows to Frameworks section (now 25 frameworks + 2 processes + 6 tools = 33 cards)
- `by-company/pwc-strategy.md` — append row for `pwc-fit-for-growth`
- `by-company/ey-parthenon.md` — append row for `ey-parthenon-multi-sided-platform`
- `by-company/deloitte.md` — append row for `deloitte-business-chemistry`
- `by-company/accenture-strategy.md` — append row for `accenture-industry-x`

## Out-of-scope

- Schema additions still deferred per spec §14
- Owner fact-check + personal layer still owner work
- Reciprocal links expected to be added where defensible (per Batch 4/5 lessons)

---

## Task 1: 4 framework cards + catalog/by-company updates

**Files (create):**
- `frameworks/pwc-fit-for-growth.md`
- `frameworks/ey-parthenon-multi-sided-platform.md`
- `frameworks/deloitte-business-chemistry.md`
- `frameworks/accenture-industry-x.md`

**Files (modify):**
- `docs/methodology-catalog.md` — append 4 rows to Frameworks
- `by-company/pwc-strategy.md` — append 1 row
- `by-company/ey-parthenon.md` — append 1 row
- `by-company/deloitte.md` — append 1 row
- `by-company/accenture-strategy.md` — append 1 row

**Interfaces:**
- Consumes: existing `docs/schema.md`, `AGENTS.md`, prior-batch cards for style
- Produces: 4 cards at `status: draft`, plus catalog + by-company updates

- [ ] **Step 1: Implementer writes all 4 cards + modifications**

  Apply the established card template:
  - 12 content fields + `status: draft` in frontmatter
  - 6 body sections with substantive factual content (each section ~80-300 Chinese characters, well under cap)
  - `## 个人批注` left as HTML-comment placeholder only
  - `**AI 建议**` left as HTML-comment placeholder only
  - `[需核实]` for unverified years/authors
  - `[争议]` for contested claims
  - Bilingual term pairs on first use
  - **`when_to_use` uses `|`-style block scalar** (not YAML list)
  - **Trailing newline on each file**

  Card-specific notes:

  - `pwc-fit-for-growth.md`: PwC Strategy&'s signature "Fit-for-Growth" framework. Origin: Booz Allen Hamilton, then Booz & Company (2008 spin-off), then Strategy& (2014 PwC acquisition). Work led by Strategy& partners. Focus: a company should be optimized for growth (not size), with three core moves — invest selectively, fix the basics, cut the rest. `source_company: ["PwC Strategy&"]` OR `["Booz & Company", "PwC Strategy&"]` (multi-source to acknowledge lineage). `created_year: 2008` (Booz & Company spin-off, when Fit-for-Growth work intensified) — mark `[需核实]` if uncertain. `tags: [strategy, growth, restructuring]`.

  - `ey-parthenon-multi-sided-platform.md`: EY-Parthenon's "Multi-Sided Platform" strategy. Parthenon Group (founded 1991, acquired by EY in 2014) was an early advocate of platform thinking in strategy consulting. Platform strategies connect two or more distinct user groups, creating network effects. `source_company: ["EY-Parthenon"]` OR `["Parthenon Group", "EY-Parthenon"]` (multi-source). `created_year: 2010` (round number for the period when Parthenon published platform work) — mark `[需核实]` if uncertain. `tags: [platform, strategy, growth]`.

  - `deloitte-business-chemistry.md`: Deloitte's "Business Chemistry" framework — a personality/teamwork diagnostic derived from Deloitte's Human Capital practice. Two-by-two matrix: Analytics, Visionaries, Integrators, Catalysts (or similar). Used to improve team dynamics, leadership, communication. `source_company: ["Deloitte"]`. `created_year: 2014` (Deloitte published the Business Chemistry book) — mark `[需核实]` if uncertain. `tags: [team, leadership, human-capital]`.

  - `accenture-industry-x.md`: Accenture Strategy's "Industry X" framework for digital manufacturing/operations transformation. Combines digital tech with operational excellence. Accenture has used Industry X as a flagship offering for industrial clients. `source_company: ["Accenture Strategy"]`. `created_year: 2017` (Accenture's Industry X launch) — mark `[需核实]` if uncertain. `tags: [digital, operations, industrial]`.

  **For all 4 cards**:
  - **Do NOT invent person names** (Batch 4 Task 1 lesson)
  - **Verify firm attribution** — these 4 firms are correct
  - **Populate `related_methods`** with reciprocal links to existing cards mentioned in body
  - Add reciprocal backlinks on those existing cards
  - Mark attribution/year claims as `[需核实]` since Big Four strategy practices' specific framework origins are less well-documented than MBB

  Possible reciprocal links:
  - `pwc-fit-for-growth` → could reference `[[booz-capabilities-driven-strategy]]` (Booz lineage), `[[bcg-growth-share-matrix]]` (portfolio resource allocation)
  - `ey-parthenon-multi-sided-platform` → could reference `[[porters-five-forces]]` (industry structure)
  - `deloitte-business-chemistry` → could reference `[[galbraith-star-model]]` (org design), `[[bcg-organizational-advantage]]` (org capability)
  - `accenture-industry-x` → could reference `[[value-chain]]` (operations), `[[bcg-experience-curve]]` (cost dynamics)

  Apply same template rules as prior batches.

- [ ] **Step 2: Implementer verifies**

  - `python3 tools/check-schema.py` passes
  - `python3 tools/check-links.py` passes
  - `python3 -m pytest tests/` — all 7 tests pass
  - **Verify trailing newlines** on all 4 new files
  - **Verify `when_to_use`** uses `|`-style block scalar on all 4 new files

- [ ] **Step 3: Commit**

  Single commit: `feat(frameworks): add 4 Big Four first-entry cards (Strategy& Fit-for-Growth, EY-Parthenon Multi-Sided Platform, Deloitte Business Chemistry, Accenture Industry X)`.

---

## Task 2: Cross-card consistency + final verification + README update

**Files:**
- Modify (if needed): any new card
- Modify: README "已收录方法论" + roadmap sections

**Interfaces:**
- Consumes: All 4 new cards + 29 existing cards
- Produces: Verification report + README update

- [ ] **Step 1: Run all validation**

  ```bash
  python3 tools/check-schema.py
  python3 tools/check-links.py
  python3 -m pytest tests/ -v
  ```

  All three must pass.

- [ ] **Step 2: Cross-card consistency check**

  For each of the 4 new cards:
  - Tag vocabulary consistent (lowercase kebab-case)?
  - `created_year` integer format consistent?
  - `category: framework`?
  - Body section character counts under 300 cap?
  - `when_to_use` uses `|`-style block scalar?
  - All files end with `\n`?

- [ ] **Step 3: Update README**

  Read `docs/methodology-catalog.md` (now 33 rows: 25 frameworks + 2 processes + 6 tools).

  Update `README.md`:
  - "已收录方法论" counts update to 33 张
  - Add 4-row highlights table for batch-6 additions
  - Roadmap item 4 (Big Four first entry) → mark complete
  - Next-step direction: cross-firm consolidation, or polish, or wait

- [ ] **Step 4: Apply any fixes inline**

  If inconsistencies found in Step 2, fix them.

- [ ] **Step 5: Commit**

  - One commit for README update (mandatory)
  - Optional commit for other consistency fixes

---

## Self-Review Notes

**Spec coverage**:
- §6 Schema → all 4 cards (Task 1)
- §7 Body structure → all 4 cards (Task 1)
- §9 AI rules → all 4 cards (Task 1)
- §11 14-firm coverage: after batch 6, all 14 firms in spec §2 have at least 1 card

**Risks**:
- Big Four strategy practices have less distinctive public framework IP than MBB/老牌所
- Some frameworks (Business Chemistry, Industry X) have specific origins that may need `[需核实]`
- Year choices for these cards are round-numbered (2008, 2010, 2014, 2017) due to attribution uncertainty

**Type consistency**:
- All 4 are framework
- `source_company` accepts firms (no individual authors in this batch)
- All `status: draft`
- `when_to_use` uses `|`-style block scalar (Batch 5 lesson)

**Out-of-scope**:
- Schema additions still deferred
- Owner fact-check + personal layer still owner work