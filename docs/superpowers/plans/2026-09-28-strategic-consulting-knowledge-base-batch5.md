# Strategic Consulting Knowledge Base — Fifth Batch Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add 3 cards from Roland Berger and Oliver Wyman to complete coverage of "old strategy houses" alongside the 26 cards delivered in batches 1-4.

**Architecture:** Same static Markdown + frontmatter pattern. 2 frameworks + 1 tool.

**Tech Stack:** Markdown, Python 3 (validation scripts), git.

**Spec:** `docs/superpowers/specs/2026-09-28-strategic-consulting-knowledge-base-design.md` (unchanged)
**Previous plans:** see `docs/superpowers/plans/2026-09-28-strategic-consulting-knowledge-base{,-batch2,-batch3,-batch4}.md`

## Global Constraints

Same as previous batches:

- UTF-8, LF line endings, H1 first line.
- 12 content fields + `status` in frontmatter.
- 6 body sections per card.
- AI factual-layer rules: `[需核实]` for unverified facts, `[争议]` for contested claims, ~300 Chinese-character cap per factual section.
- AI does NOT write `## 个人批注` body content (owner work).
- Bilingual term-pair on first use.

## Files to create (3 cards)

| # | Card | Category | source_company | Notes |
|---|---|---|---|---|
| 1 | `frameworks/roland-berger-premium-strategy.md` | framework | Roland Berger | Premium/luxury positioning work |
| 2 | `tools/oliver-wyman-risk-based-pricing.md` | tool | Oliver Wyman | Risk-based pricing for insurance/banking |
| 3 | `frameworks/oliver-wyman-enterprise-risk-management.md` | framework | Oliver Wyman | ERM strategic framework |

## Files to modify

- `docs/methodology-catalog.md` — append 3 rows (2 frameworks + 1 tool; total 29 cards = 21 frameworks + 2 processes + 6 tools)
- `by-company/roland-berger.md` — append row for `roland-berger-premium-strategy`
- `by-company/oliver-wyman.md` — append 2 rows for the OW cards

## Out-of-scope

- Schema additions still deferred per spec §14
- Owner fact-check + personal layer still owner work
- Reciprocal links expected to be added where defensible (per Batch 4 lesson)

---

## Task 1: 3 framework/tool cards + catalog/by-company updates

**Files (create):**
- `frameworks/roland-berger-premium-strategy.md`
- `tools/oliver-wyman-risk-based-pricing.md`
- `frameworks/oliver-wyman-enterprise-risk-management.md`

**Files (modify):**
- `docs/methodology-catalog.md` — append 3 rows
- `by-company/roland-berger.md` — append 1 row
- `by-company/oliver-wyman.md` — append 2 rows

**Interfaces:**
- Consumes: existing `docs/schema.md`, `AGENTS.md`, prior-batch cards for style
- Produces: 3 cards at `status: draft`, plus catalog + by-company updates

- [ ] **Step 1: Implementer writes all 3 cards + modifications**

  Apply the established card template:
  - 12 content fields + `status: draft` in frontmatter
  - 6 body sections with substantive factual content (each section ~80-300 Chinese characters, well under cap)
  - `## 个人批注` left as HTML-comment placeholder only
  - `**AI 建议**` left as HTML-comment placeholder only
  - `[需核实]` for unverified years/authors
  - `[争议]` for contested claims
  - Bilingual term pairs on first use

  Card-specific notes:

  - `roland-berger-premium-strategy.md`: Roland Berger (founded 1967 Munich). Distinctive RB work centers on premium/luxury positioning, especially for European luxury, automotive, and industrial clients. RB's published IP is less formal than MBB; their "premium" work includes strategic positioning for high-end brands. Mark specific RB origin claims as `[需核实]` since the firm has limited distinctive public framework IP. `created_year: 2005` (round number for the period when RB's premium work was prominent). `source_company: ["Roland Berger"]`.

  - `oliver-wyman-risk-based-pricing.md`: Oliver Wyman (founded 1984, acquired by Marsh & McLennan). Distinctive OW work in risk-based pricing for insurance, banking, and asset management. Combines actuarial modeling with customer segmentation to set prices that reflect risk levels. Mark attribution as `[需核实]` since OW's specific risk-based pricing methodology has limited public documentation. `created_year: 2010` (round number for the period when risk-based pricing became prominent in financial services). `source_company: ["Oliver Wyman"]`.

  - `oliver-wyman-enterprise-risk-management.md`: Oliver Wyman's Enterprise Risk Management (ERM) framework, integrating strategic, financial, operational, and reputational risk perspectives. OW has been a major force in ERM consulting. Mark specific origin as `[需核实]`; the framework is well-known in the industry but OW's specific version has limited public documentation. `created_year: 2005` (round number). `source_company: ["Oliver Wyman"]`.

  **For all 3 cards**:
  - **Do NOT invent person names** (Batch 4 Task 1 lesson)
  - **Verify firm attribution** — Roland Berger and Oliver Wyman are correct
  - **Populate `related_methods`** with reciprocal links to existing cards mentioned in body (Batch 4 Task 1 lesson)
  - Add reciprocal backlinks on those existing cards (modify their `related_methods` frontmatter)

  Possible reciprocal links:
  - RB Premium Strategy → could link to `[[porter-generic-strategies]]` (differentiation concept), `[[bcg-growth-share-matrix]]` (premium positions are typically Stars)
  - OW Risk-Based Pricing → could link to `[[value-chain]]` (operational analysis), `[[pestel]]` (industry risk factors)
  - OW ERM Framework → could link to `[[porters-five-forces]]` (industry risk), `[[pestel]]` (external risks)

  Apply same template rules as prior batches.

- [ ] **Step 2: Implementer verifies**

  - `python3 tools/check-schema.py` passes
  - `python3 tools/check-links.py` passes
  - `python3 -m pytest tests/` — all 7 tests pass

- [ ] **Step 3: Commit**

  Single commit: `feat(frameworks,tools): add 3 cards completing old-house coverage (RB Premium Strategy, OW Risk-Based Pricing, OW ERM Framework)`.

---

## Task 2: Cross-card consistency + final verification + README update

**Files:**
- Modify (if needed): any new card
- Modify (if needed): README "已收录方法论" + roadmap sections

**Interfaces:**
- Consumes: All 3 new cards + 26 existing cards
- Produces: Verification report + README update

- [ ] **Step 1: Run all validation**

  ```bash
  python3 tools/check-schema.py
  python3 tools/check-links.py
  python3 -m pytest tests/ -v
  ```

  All three must pass.

- [ ] **Step 2: Cross-card consistency check**

  For each of the 3 new cards:
  - Tag vocabulary consistent (lowercase kebab-case)?
  - `created_year` integer format consistent?
  - `category` enum value correct?
  - Body section character counts under 300 cap?

- [ ] **Step 3: Apply trailing-newline fix**

  Add `\n` to any of the 3 new files that lack it.

- [ ] **Step 4: Update README**

  Read `docs/methodology-catalog.md` (now 29 rows: 21 frameworks + 2 processes + 6 tools).

  Update `README.md`:
  - "已收录方法论" counts update to 29 张
  - Add batch-5 highlights row
  - Roadmap item 3 (老牌战略所) → mark complete
  - Roadmap item 4 → if any of these methods is missing, mention it; otherwise point to next batch direction (Big Four entry)

- [ ] **Step 5: Apply any fixes inline**

  If inconsistencies found in Step 2, fix them.

- [ ] **Step 6: Commit**

  - One commit for trailing newlines (mandatory)
  - One commit for README update (mandatory)
  - Optional commit for other consistency fixes

---

## Self-Review Notes

**Spec coverage**:
- §6 Schema → all 3 cards (Task 1)
- §7 Body structure → all 3 cards (Task 1)
- §9 AI rules → all 3 cards (Task 1)
- §11 Batch count: 5 → 26 → 29

**Risks**:
- Roland Berger and Oliver Wyman have less distinctive public framework IP than MBB/Monitor/ADL/Booz — implementer must avoid fabricating origin claims
- RB and OW's specific framework naming may not be well-documented; use cautious `[需核实]` markers
- Year choices for these cards are round-numbered (2005, 2010) due to attribution uncertainty

**Type consistency**:
- 2 framework + 1 tool
- `source_company` accepts firms (no individual authors in this batch)
- All `status: draft`

**Out-of-scope**:
- Schema additions still deferred
- Owner fact-check + personal layer still owner work