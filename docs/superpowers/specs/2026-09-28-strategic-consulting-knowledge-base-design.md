# Strategic Consulting Knowledge Base — Design

**Date**: 2026-09-28
**Status**: Draft (awaiting user review)
**Path**: `strategic-consulting/`

## 1. Purpose

A personally curated Markdown knowledge base of strategy consulting methodologies — frameworks, processes, and analytical tools — used by major consulting firms (MBB, Big Four strategy practices, legacy strategy houses). Optimized for self-study and personal reference, with the option to share cleanly when needed.

## 2. Scope and non-goals

**In scope**
- "Signature" frameworks with names (e.g., 7S, BCG Matrix, Porter Five Forces)
- Project-execution methods (e.g., MECE, hypothesis-driven problem solving)
- Analytical tools commonly used by consultants (e.g., value chain, 4C, profitability tree)
- Coverage: MBB (McKinsey, BCG, Bain) + Big Four strategy practices (Deloitte, Accenture Strategy, PwC Strategy&, EY-Parthenon) + legacy strategy houses (Roland Berger, L.E.K., A.T. Kearney, Strategy&, Monitor, Arthur D. Little, Oliver Wyman, OC&C) — 14 firms total.

**Out of scope**
- Industry-specific consulting playbooks (healthcare, finance)
- Operational/IT consulting methodologies (Six Sigma, ITIL, etc.)
- Internal firm culture, career advice, hiring
- Tooling for any web UI (this is a static knowledge base)

## 3. User profile and tone

- **Primary user**: the project owner — a practitioner fluent in MBB/strategy jargon
- **Primary use**: self-study and personal reference (with optional light sharing)
- **Tone**: factual layer uses precise, sourced language; personal layer allows informal voice, incomplete thoughts, skepticism, and case mapping

## 4. Directory structure (hybrid: by-type for cards, by-company for indexes)

```
strategic-consulting/
├── README.md
├── AGENTS.md
├── docs/
│   ├── schema.md
│   └── methodology-catalog.md
├── by-company/
│   ├── mckinsey.md
│   ├── bcg.md
│   ├── bain.md
│   ├── deloitte.md
│   ├── accenture-strategy.md
│   ├── pwc-strategy.md
│   ├── ey-parthenon.md
│   ├── roland-berger.md
│   ├── lek.md
│   ├── at-kearney.md
│   ├── strategyand.md
│   ├── monitor.md
│   ├── arthur-d-little.md
│   ├── oliver-wyman.md
│   └── oc-c.md
├── frameworks/
├── processes/
└── tools/
```

- `frameworks/`, `processes/`, `tools/` are the **card landing zones**.
- `by-company/` are **index pages** — one file per firm, listing the firm's methodology cards.
- No `shared/` mirror; multi-company methods live in their type folder with multi-value `source_company`.

## 5. Naming conventions

- Methodology cards: `{company-prefix}-{kebab-case-name}.md` (e.g., `mckinsey-7s.md`). Multi-company methods omit the prefix (e.g., `mece.md`, `porters-five-forces.md`).
- Company index files: `{kebab-case-company}.md` (e.g., `at-kearney.md`).
- Folders: plural English (`frameworks/`, `processes/`, `tools/`).
- All Markdown: UTF-8, LF line endings, H1 first line.

## 6. Card schema — 12 fields

```yaml
---
name: <Chinese name>
name_en: <English/original name>
source_company: <list of canonical firm names or individual authors; can be empty for fully industry-wide methods>
category: framework | process | tool
created_year: <year proposed or peak-active period>
one_line_summary: <one sentence>
purpose: <what problem it solves>
when_to_use: <text, can include negative cases>
key_steps: <list>
limitations: <list of criticisms, known pitfalls, where the method breaks>
related_methods: <list of [[slug]] wikilinks>
tags: <list>
status: draft | fact-checked | annotated | archived
---
```

## 7. Card body structure

```markdown
# {{ name }}

> {{ one_line_summary }}

## 起源与定位
(factual)

## 核心内容
(factual)

## 适用与不适用
(factual + personal supplements)

## 局限与争议
(factual + personal supplements)

## 与其他方法论的关系
(factual)

## 个人批注
(personal — owner writes, AI does not edit)
```

## 8. Workflow

### 8.1 One-time bootstrap
1. Create the directory skeleton (folders, `README.md`, `AGENTS.md`, `docs/schema.md`, `docs/methodology-catalog.md`, 14 empty `by-company/*.md` files).
2. Build the first card (McKinsey 7S) end-to-end as the calibration case.
3. Retro on schema and template after one card is complete.

### 8.2 Per-card flow
1. Owner requests a new card.
3. AI drafts the factual layer + frontmatter, sets `status: draft`.
5. Owner reviews the factual layer, performs fact-check, sets `status: fact-checked`.
7. Owner writes `## 个人批注`, sets `status: annotated`.
9. Update `docs/methodology-catalog.md` and the relevant `by-company/*.md` index.

### 8.3 Status lifecycle
`draft` → `fact-checked` → `annotated` → (`archived` if retired)

## 9. AI collaboration rules (written into `AGENTS.md`)

- Do not fabricate years, authors, or sources — mark unverified facts with `[需核实]`.
- Mark contested content with `[争议]` and list at least two viewpoints.
- Maintain bidirectional `related_methods` links — when A writes `[[B]]`, ensure B references A.
- Cap each factual section at ~300 Chinese characters.
- First use of a Chinese-English term pair should appear together (e.g., MECE / 相互独立、完全穷尽).
- AI suggestions that should enter the personal layer go in a separate `**AI 建议**` subsection inside `## 个人批注` — never overwrite the owner's words.

## 10. Tooling (optional, not enforced)

- `tools/check-schema.py` — validate every card's frontmatter against `docs/schema.md`.
- `tools/check-links.py` — validate `related_methods` wikilinks resolve and are bidirectional.

## 11. First batch — 5 cards

| # | Methodology | Category | source_company | What it stress-tests |
|---|---|---|---|---|
| 1 | McKinsey 7S | framework | McKinsey & Company | baseline happy path |
| 2 | BCG Growth-Share Matrix | framework | BCG | contested method, `limitations` field |
| 3 | Porter's Five Forces | tool | Michael Porter (Harvard) | source_company accepts individual authors |
| 4 | MECE / Issue Tree | process | industry-wide (McKinsey canonical) | multi-source / no single owner |
| 5 | Bain Net Promoter System | framework | Bain & Company | recent method (2003), `created_year` field |

## 12. Cadence

- **Week 1**: card #1 (7S) — purpose is calibration, not speed.
- **Weeks 2–3**: cards #2–5, ~2 per week.
- **After 5 cards**: stop, retro on schema, template, `AGENTS.md` rules. Adjust before continuing.

## 13. Definition of done for the first batch

- 5 card files all at `status: annotated`.
- `docs/methodology-catalog.md` lists 5 rows.
- `by-company/mckinsey.md`, `bcg.md`, `bain.md` each have at least one entry.

## 14. Open questions deferred (will revisit after first 5 cards)

- Whether to add `case_examples` field (real-world application stories).
- Whether to add `evolution_history` field (how the method changed over time).
- Whether to maintain a `comparisons/` folder (e.g., all growth-share style matrices side-by-side).
- Whether to add a Chinese-context layer (君智、华与华、和君 etc.) once the MBB/Big Four layer is solid.