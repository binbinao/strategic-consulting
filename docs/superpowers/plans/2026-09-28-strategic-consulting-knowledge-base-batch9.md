# Strategic Consulting Knowledge Base — Ninth Batch Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add 5 cards covering firm gaps and depth: L.E.K. first entry (the only in-scope firm with 0 cards), Monitor 2nd card, McKinsey 3rd card, plus 2 widely-attributed cross-firm tools.

**Architecture:** Same static Markdown + frontmatter pattern. 2 framework + 1 framework + 1 framework + 1 tool + 1 tool.

**Tech Stack:** Python 3 (now with strict validators from Batch 8).

**Spec:** `docs/superpowers/specs/2026-09-28-strategic-consulting-knowledge-base-design.md` (unchanged)
**Previous plans:** see `docs/superpowers/plans/2026-09-28-strategic-consulting-knowledge-base{,-batch2,-batch3,-batch4,-batch5,-batch6,-batch7,-batch8}.md`

## Global Constraints

- All Batch 8 validators apply mechanically — implementer MUST verify 300-char cap, `when_to_use` `|`-style block scalar, and by-company reverse validation for each new card
- TDD discipline via validators
- Batch 4 lesson: do NOT invent person names
- Batch 5 lesson: trailing newlines + `when_to_use` as `|`-style block scalar
- AGENTS.md "不杜撰" rule: do NOT fabricate framework/method origin claims

## Files to create (5 cards)

| # | Card | Category | source_company | Notes |
|---|---|---|---|---|
| 1 | `frameworks/lek-commercial-due-diligence.md` | framework | L.E.K. Consulting | First L.E.K. card (fills the L.E.K. gap) |
| 2 | `frameworks/monitor-value-based-management.md` | framework | Monitor Group | Monitor 2nd card |
| 3 | `frameworks/mckinsey-profitability-tree.md` | framework | McKinsey & Company | McKinsey 3rd card (distinctive diagnostic tool) |
| 4 | `tools/ansoff-matrix.md` | tool | Igor Ansoff (individual) | Industry tool, well-attributed |
| 5 | `tools/service-profit-chain.md` | self | James Heskett / HBR | Heskett/Sasser/Schlesinger 1994 (industry tool) |

## Files to modify

- `docs/methodology-catalog.md` — append 5 rows (3 frameworks + 2 tools; total 28 frameworks + 2 processes + 8 tools = 38 cards)
- `by-company/lek.md` — append row for `lek-commercial-due-diligence` (L.E.K. first entry)
- `by-company/mckinsey.md` — append row for `mckinsey-profitability-tree`
- (Monitor file already exists; no by-company update for value-based-management?)

Let me re-examine. Monitor is in by-company/monitor.md. Should `monitor-value-based-management` go there?

Yes, Monitor Group owns the framework.

- `by-company/monitor.md` — append row for `monitor-value-based-management`

For Ansoff Matrix and Service Profit Chain: both individual authors, no by-company update needed.

Final by-company updates:
- `by-company/lek.md` — append 1 row (first L.E.K. entry)
- `by-company/monitor.md` — append 1 row (Monitor 2nd)
- `by-company/mckinsey.md` — append 1 row (McKinsey 3rd)

No by-company update for Igor Ansoff (individual) or James Heskett (individual).

**SPECIAL NOTE for L.E.K.**: The `by-company/lek.md` file currently exists but has empty methodology index. First L.E.K. entry populates it.

## Out-of-scope

- Schema additions still deferred
- Owner fact-check + personal layer still owner work
- Reciprocal links added where defensible (per Batch 4/5/8 lessons)

---

## Task 1: 5 cards + catalog/by-company updates

**Files (create):**
- `frameworks/lek-commercial-due-diligence.md`
- `frameworks/monitor-value-based-management.md`
- `frameworks/mckinsey-profitability-tree.md`
- `tools/ansoff-matrix.md`
- `tools/service-profit-chain.md`

**Files (modify):**
- `docs/methodology-catalog.md` — append 5 rows
- `by-company/lek.md` — append 1 row (first entry)
- `by-company/monitor.md` — append 1 row (Monitor 2nd)
- `by-company/mckinsey.md` — append 1 row (McKinsey 3rd)

**Interfaces:**
- Consumes: existing `docs/schema.md`, `AGENTS.md`, prior-batch cards for style
- Produces: 5 cards at `status: draft`, plus catalog + by-company updates

- [ ] **Step 1: Implementer writes all 5 cards + modifications**

  Apply the established card template:
  - 12 content fields + `status: draft` in frontmatter
  - 6 body sections with substantive factual content (each section ~80-300 Chinese characters, validated by `check-schema.py`)
  - `## 个人批注` left as HTML-comment placeholder only
  - `**AI 建议**` left as HTML-comment placeholder only
  - `[需核实]` for unverified years/authors
  - `[争议]` for contested claims
  - Bilingual term pairs on first use
  - **`when_to_use` uses `|`-style block scalar** (validated by `check-schema.py`)
  - **Trailing newline on file**
  - Populate `related_methods` with reciprocal links to existing cards (validated by `check-links.py`)

  Card-specific notes:

  ### `lek-commercial-due-diligence.md`

  L.E.K. Consulting (founded 1983 London by three L.E.K. partners; firm name is the partners' initials + London). Distinctive in commercial due diligence (CDD) for private equity and corporate clients. L.E.K.'s CDD framework typically covers: market size and growth, competitive dynamics, customer analysis (segmentation, willingness-to-pay), operational benchmarks, management assessment.

  **Attribution caution**:
  - "L.E.K." is the firm name (3 founders). Don't claim "L.E.K." is a person's initials in a misleading way
  - Specific framework origin attribution is hard to source. Use cautious markers
  - Don't invent partner names

  Frontmatter:
  - `created_year: 1990` (round number for the period when CDD became L.E.K.'s distinctive offering) — mark `[需核实]`
  - `source_company: ["L.E.K. Consulting"]`
  - `category: framework`
  - Suggested `tags: [due-diligence, private-equity, growth]`

  ### `monitor-value-based-management.md`

  Monitor Group's Value-Based Management (VBM) framework. Monitor (founded 1981 by Mark Fuller and Michael Porter, acquired by Deloitte 2013 as "Monitor Deloitte"). VBM links corporate strategy to shareholder value creation through explicit identification of value drivers and KPIs. Distinctive in integrating financial and operational metrics.

  **Attribution caution**:
  - VBM as a concept has multiple contributors (Copeland, Koller, Murrin at McKinsey/Monitor also worked on this)
  - Monitor's specific VBM approach is differentiated from McKinsey's
  - Mark specific attribution as `[需核实]`

  Frontmatter:
  - `created_year: 1995` (round number; VBM work intensified 1990s) — mark `[需核实]`
  - `source_company: ["Monitor Group"]`
  - `category: framework`
  - Suggested `tags: [value, finance, strategy]`

  ### `mckinsey-profitability-tree.md`

  McKinsey's "Profitability Tree" (also called Margin Tree / Cost Tree) framework — diagnostic tool that decomposes a company's ROE/margin into its component drivers. Typically shows: revenue growth × price × volume × cost structure × capital efficiency. Used for identifying where to focus margin improvement.

  **Attribution caution**:
  - Profitability tree is widely used; not exclusive to McKinsey
  - McKinsey's specific formulation has internal publications
  - Mark McKinsey-specific contribution as `[需核实]`

  Frontmatter:
  - `created_year: 2000` (round number) — mark `[需核实]`
  - `source_company: ["McKinsey & Company"]`
  - `category: framework`
  - Suggested `tags: [diagnostic, finance, operational]`

  ### `ansoff-matrix.md`

  Igor Ansoff's "Ansoff Matrix" (1965 HBR article "Corporate Strategy"). 2x2 matrix of market × product: market penetration / market development / product development / diversification. Foundational growth strategy framework.

  **Attribution caution**:
  - Ansoff Matrix is well-attributed to Igor Ansoff (1965)
  - Specific card text should not claim any individual contributors beyond Ansoff
  - This is a foundational framework — body can be confident on the attribution

  Frontmatter:
  - `created_year: 1965`
  - `source_company: ["Igor Ansoff"]` (individual author)
  - `category: tool`
  - Suggested `tags: [growth, classic, matrix]`

  ### `service-profit-chain.md`

  Heskett/Sasser/Schlesinger's "Service Profit Chain" (1994 HBR article + book "The Service Profit Chain"). Links internal service quality → employee satisfaction → customer loyalty → revenue growth → profitability.

  **Attribution caution**:
  - Originally developed by Heskett, Sasser, Schlesinger (HBR / Harvard Business School)
  - Often associated with service industry consulting broadly
  - Don't attribute to ADL or other firms

  Frontmatter:
  - `created_year: 1994`
  - `source_company: ["James Heskett", "Leonard Berry", "Valarie Zeithaml"]` — or simpler: `["James Heskett"]` (lead author, individual per `first_name`)
  - `category: tool`
  - Suggested `tags: [service, growth, chain]`

  **For all 5 cards**:
  - **Do NOT invent person names** (Batch 4 lesson)
  - **Verify firm attribution** — L.E.K., Monitor Group, McKinsey are correct
  - **Populate `related_methods`** with reciprocal links to existing cards mentioned in body
  - Add reciprocal backlinks on those existing cards

  Possible reciprocal links:
  - L.E.K. CDD → could reference `[[value-chain]]` (analysis of company operations)
  - Monitor VBM → could reference `[[booz-capabilities-driven-strategy]]` (capability), `[[bain-net-promoter-system]]` (Bain's customer value work)
  - McKinsey Profitability Tree → could reference `[[bcg-experience-curve]]` (cost dynamics)
  - Ansoff Matrix → could reference `[[porters-five-forces]]` (industry view)
  - Service Profit Chain → could reference `[[bain-net-promoter-system]]` (customer loyalty), `[[customer-effort-score]]` (CES as customer satisfaction metric)

- [ ] **Step 2: Implementer verifies**

  - `python3 tools/check-schema.py` passes (validates 300-char cap, when_to_use type, schema fields, all 33+5=... cards)
  - `python3 tools/check-links.py` passes (validates related_methods bidirectional, by-company reverse)
  - `python3 -m pytest tests/` — all 14 tests pass

- [ ] **Step 3: Commit**

  Single commit: `feat(frameworks,tools): add 5 cross-firm cards (L.E.K. CDD, Monitor VBM, McKinsey Profitability Tree, Ansoff Matrix, Service Profit Chain)`.

---

## Task 2: Cross-card consistency + final verification + README update

- [ ] **Step 1: Run all validation**

  ```bash
  python3 tools/check-schema.py
  python3 tools/check-links.py
  python3 -m pytest tests/ -v
  ```

  All three must pass.

- [ ] **Step 2: Apply trailing newline fix if needed**

  Add `\n` to any of the 5 new files that lack it.

- [ ] **Step 3: Update README**

  Read `docs/methodology-catalog.md` (now 38 rows: 28 frameworks + 2 processes + 8 tools).

  Update `README.md`:
  - "已收录方法论" counts update to 38 张
  - Add 5-row highlights table for batch-9 additions
  - Update roadmap to reflect depth-filling is done

- [ ] **Step 4: Commit**

  - One commit for trailing newlines (mandatory if any file needed it)
  - One commit for README update (mandatory)

---

## Self-Review Notes

**Spec coverage**:
- §6 Schema → all 5 cards (Task 1)
- §7 Body structure → all 5 cards (Task 1)
- §9 AI rules → all 5 cards (Task 1)
- All 14 firms in spec §2 scope now have at least 1 card (L.E.K. filled gap)

**Risks**:
- Some firm attributions might be uncertain (L.E.K. specific CDD framework, McKinsey specific Profitability Tree formulation)
- Mark all attribution specifics with `[需核实]`
- All new cards subject to Batch 8 mechanical validators

**Type consistency**:
- 3 frameworks + 2 tools
- 4 with `source_company: [firm]`, 1 with individual author (Ansoff), 1 with individual author (Heskett)
- All `status: draft`
- `when_to_use` uses `|`-style block scalar

**Out-of-scope**:
- Schema additions still deferred
- Owner fact-check + personal layer still owner work