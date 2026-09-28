# Strategic Consulting Knowledge Base Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Bootstrap a personally curated Markdown knowledge base of strategy consulting methodologies (MBB + Big Four + legacy strategy houses), with a hybrid directory structure (by-type landing zones + by-company indexes), 12-field card schema with frontmatter, and a working first batch of 5 methodology cards.

**Architecture:** Pure static Markdown files with YAML frontmatter. Cards land in `frameworks/` / `processes/` / `tools/` by category; `by-company/` holds one-page indexes per firm. Two-layer content per card: factual layer (AI drafts, owner fact-checks) and personal layer (owner writes). Optional Python validation scripts in `tools/`.

**Tech Stack:** Markdown (CommonMark + YAML frontmatter), Python 3 (optional validation scripts only), ripgrep for cross-file search.

**Spec:** `docs/superpowers/specs/2026-09-28-strategic-consulting-knowledge-base-design.md`

## Global Constraints

These are project-wide rules from the spec; every task implicitly follows them.

- **Encoding / line endings:** UTF-8, LF.
- **First line:** Each `.md` file starts with H1 (`# Title`).
- **Card file naming:** `{company-prefix}-{kebab-case-name}.md`; multi-company methods omit prefix (e.g., `mece.md`, `porters-five-forces.md`).
- **Company index naming:** `{kebab-case-company}.md` (e.g., `at-kearney.md`, `arthur-d-little.md`).
- **Folder names:** plural English (`frameworks/`, `processes/`, `tools/`).
- **Frontmatter (12 fields):** `name`, `name_en`, `source_company`, `category`, `created_year`, `one_line_summary`, `purpose`, `when_to_use`, `key_steps`, `limitations`, `related_methods`, `tags`, `status`. (Note: `status` is the 13th meta-field tracking lifecycle, making the card's controlled fields 12 + status. The schema doc uses "12 fields" referring to content fields; `status` is workflow.)
- **Status values:** `draft` → `fact-checked` → `annotated` → (`archived` if retired).
- **Card body sections (6):** `## 起源与定位`, `## 核心内容`, `## 适用与不适用`, `## 局限与争议`, `## 与其他方法论的关系`, `## 个人批注`.
- **AI factual-layer rules:** no fabricated years/authors/sources; mark `[需核实]` and `[争议]`; bidirectionally maintain `related_methods`; cap each factual section ~300 Chinese characters; first use of a Chinese-English term pair appears together; AI suggestions to the personal layer go in an `**AI 建议**` subsection, never overwriting the owner.
- **AI does NOT write the personal layer.** `## 个人批注` is owner territory; task plans leave it as a stub for the owner to fill.

---

## File Structure

Files this plan creates (everything under `/Users/duobinji/Documents/GitHub/strategic-consulting/`):

| Path | Purpose |
|---|---|
| `README.md` | Project entry, purpose, structure overview, how to add a card |
| `AGENTS.md` | Rules AI collaborators must follow |
| `docs/schema.md` | Authoritative frontmatter field definitions |
| `docs/methodology-catalog.md` | One-line index of all cards, grouped by category |
| `by-company/{14 firms}.md` | Per-firm index pages linking to the firm's cards |
| `frameworks/{cards}.md` | Framework cards (e.g., `mckinsey-7s.md`) |
| `processes/{cards}.md` | Process cards (e.g., `mece.md`) |
| `tools/{cards}.md` | Analytical tool cards (e.g., `porters-five-forces.md`) |
| `tools/check-schema.py` | (Optional, Task 11) Validate frontmatter |
| `tools/check-links.py` | (Optional, Task 11) Validate wikilinks |

First-batch card list (Tasks 3, 5–8):

| Task | Card | Category | source_company | File |
|---|---|---|---|---|
| 3 | McKinsey 7S | framework | McKinsey & Company | `frameworks/mckinsey-7s.md` |
| 5 | BCG Growth-Share Matrix | framework | BCG | `frameworks/bcg-growth-share-matrix.md` |
| 6 | Porter's Five Forces | tool | Michael Porter (Harvard) | `tools/porters-five-forces.md` |
| 7 | MECE / Issue Tree | process | industry-wide (McKinsey canonical) | `processes/mece.md` |
| 8 | Bain Net Promoter System | framework | Bain & Company | `frameworks/bain-net-promoter-system.md` |

---

## Task 1: Bootstrap project skeleton and schema doc

**Files:**
- Create: `README.md`
- Create: `AGENTS.md`
- Create: `docs/schema.md`
- Create: `docs/methodology-catalog.md` (empty table header only)
- Create: `frameworks/.gitkeep`
- Create: `processes/.gitkeep`
- Create: `tools/.gitkeep`

**Interfaces:**
- Produces: The skeleton every later task depends on. After this task, `docs/schema.md` is the canonical field reference; later tasks must conform.

- [ ] **Step 1: Create `README.md`**

Content:

```markdown
# Strategic Consulting 知识库

个人整理的战略咨询方法论知识库，覆盖 MBB + 四大 + 老牌战略所。

## 结构

- `frameworks/` —— 招牌框架（如 7S、BCG 矩阵）
- `processes/` —— 做事流程（如 MECE、假设驱动）
- `tools/` —— 分析工具（如五力、价值链）
- `by-company/` —— 按公司索引（一个公司一文件，列出该公司的方法论卡片）
- `docs/schema.md` —— frontmatter 字段定义（权威）
- `docs/methodology-catalog.md` —— 完整方法论清单
- `AGENTS.md` —— AI 协作规则

## 如何新增一张卡片

1. 在 `frameworks/` / `processes/` / `tools/` 中按 `{公司前缀}-{kebab-case-name}.md` 命名新建文件
2. 按 `docs/schema.md` 写 frontmatter，按卡片模板填 body
3. 更新对应 `by-company/*.md` 和 `docs/methodology-catalog.md`
4. 状态流转：`draft` → `fact-checked` → `annotated`
```

- [ ] **Step 2: Create `AGENTS.md`**

Content:

```markdown
# AI 协作规则

本项目由 AI 起草事实层、人类撰写个人层。AI 协作者必须遵守：

## 事实层规则

- **不杜撰**：年份、作者、出处查不到标 `[需核实]`，不写出来
- **标争议**：多方观点冲突的内容标 `[争议]`，至少列出两方观点
- **双向链接**：写 `[[B]]` 时，确认 B 的 `related_methods` 也含 A
- **限字数**：每个事实层 section 不超过 300 中文字
- **双语术语**：中英术语第一次出现一起写（如 MECE / 相互独立、完全穷尽）

## 个人层规则

- AI **不写** `## 个人批注` 的正文
- 如要给个人层提建议，在 `## 个人批注` 下加 `**AI 建议**` 子节，不覆盖所有者原话
- 个人层可口语、可未完成、可质疑，不做事实核查

## 字段规则

- frontmatter 必须含 12 个内容字段 + `status`，缺一项视为草稿不完整
- `status: draft` 表示 AI 已起草、人类未校
- `status: fact-checked` 表示事实层已交叉核对
- `status: annotated` 表示个人批注完成
- `status: archived` 表示不再使用（保留作历史）

## 链接规则

- `related_methods` 用 wikilink `[[slug]]`，slug 与目标文件 basename 一致（去 `.md`）
- 修改某张卡片后，必须同步更新被引用方的 `related_methods`
```

- [ ] **Step 3: Create `docs/schema.md`**

Content:

```markdown
# Frontmatter Schema（权威定义）

每张方法论卡片的 frontmatter 必须含以下 12 个内容字段 + 1 个工作流字段。字段名固定，缺失视为草稿不完整。

## 12 个内容字段

| 字段 | 类型 | 说明 |
|---|---|---|
| `name` | string | 中文名 |
| `name_en` | string | 英文/原名 |
| `source_company` | list[string] | 首发/标志公司或个人作者；纯行业通用可空 |
| `category` | enum | `framework` / `process` / `tool` |
| `created_year` | int | 提出年份或活跃期 |
| `one_line_summary` | string | 一句话说明它是什么 |
| `purpose` | text | 解决什么问题 |
| `when_to_use` | text | 适用场景（含不适用） |
| `key_steps` | list[string] | 主要步骤或组成要素 |
| `limitations` | list[string] | 局限、被批评点 |
| `related_methods` | list[string] | wikilink `[[slug]]`，与目标文件 basename 一致 |
| `tags` | list[string] | 自由标签 |

## 1 个工作流字段

| 字段 | 取值 | 说明 |
|---|---|---|
| `status` | `draft` / `fact-checked` / `annotated` / `archived` | 卡片生命周期 |

## 文件命名

- `{公司前缀}-{kebab-case-name}.md`，如 `mckinsey-7s.md`
- 多公司共享方法不带前缀，如 `mece.md`、`porters-five-forces.md`

## 链接约定

`related_methods` 中的 `[[slug]]` 必须：
- 指向已存在的文件名（去 `.md`）
- 双向：A 写 `[[B]]` 时，B 的 `related_methods` 也含 A
```

- [ ] **Step 4: Create `docs/methodology-catalog.md` with header only**

Content:

```markdown
# 方法论清单

按类型分组。维护时按添加顺序即可，AI 会在新建卡片后追加。

## Frameworks

| 名称 | 公司 | 提出年份 | 状态 |
|---|---|---|---|

## Processes

| 名称 | 公司 | 提出年份 | 状态 |
|---|---|---|---|

## Tools

| 名称 | 公司 | 提出年份 | 状态 |
|---|---|---|---|
```

- [ ] **Step 5: Create empty landing folders with `.gitkeep`**

Run:

```bash
mkdir -p frameworks processes tools
touch frameworks/.gitkeep processes/.gitkeep tools/.gitkeep
```

Expected: Three folders with empty `.gitkeep` files. `ls frameworks` should show `.gitkeep`.

- [ ] **Step 6: Verify skeleton**

Run:

```bash
ls -la README.md AGENTS.md docs/schema.md docs/methodology-catalog.md frameworks/.gitkeep processes/.gitkeep tools/.gitkeep
```

Expected: All 7 paths exist.

- [ ] **Step 7: Commit**

```bash
cd /Users/duobinji/Documents/GitHub/strategic-consulting
git init
git add README.md AGENTS.md docs/schema.md docs/methodology-catalog.md frameworks processes tools
git commit -m "chore: bootstrap project skeleton with schema and AI rules"
```

---

## Task 2: Create 14 by-company index file stubs

**Files:**
- Create: `by-company/{mckinsey,bcg,bain,deloitte,accenture-strategy,pwc-strategy,ey-parthenon,roland-berger,lek,at-kearney,strategyand,monitor,arthur-d-little,oliver-wyman,oc-c}.md`

Note: `pwc-strategy.md` covers PwC Strategy& and `strategyand.md` covers the legacy Strategy& firm. These are intentionally separate index files even though they share an old lineage.

**Interfaces:**
- Consumes: Schema from `docs/schema.md` (referenced, not enforced on these index pages)
- Produces: 15 placeholder index files (one for each firm) that Tasks 3, 5, 6, 7, 8 will populate

- [ ] **Step 1: Create `by-company/` folder**

Run:

```bash
mkdir -p by-company
```

- [ ] **Step 2: Create `by-company/mckinsey.md`**

Content:

```markdown
# McKinsey & Company

## 公司简介

[待补充]

## 方法论索引

| 名称 | 类型 | 状态 |
|---|---|---|
```

- [ ] **Step 3: Create the remaining 14 index files with the same template**

For each firm below, create `by-company/{file}.md` with this exact content (replace `{Company Display Name}` with the appropriate name):

```markdown
# {Company Display Name}

## 公司简介

[待补充]

## 方法论索引

| 名称 | 类型 | 状态 |
|---|---|---|
```

File → Display Name mapping:
- `bcg.md` → `Boston Consulting Group (BCG)`
- `bain.md` → `Bain & Company`
- `deloitte.md` → `Deloitte (Strategy practice)`
- `accenture-strategy.md` → `Accenture Strategy`
- `pwc-strategy.md` → `PwC Strategy&`
- `ey-parthenon.md` → `EY-Parthenon`
- `roland-berger.md` → `Roland Berger`
- `lek.md` → `L.E.K. Consulting`
- `at-kearney.md` → `A.T. Kearney`
- `strategyand.md` → `Strategy& (legacy)`
- `monitor.md` → `Monitor Group`
- `arthur-d-little.md` → `Arthur D. Little`
- `oliver-wyman.md` → `Oliver Wyman`
- `oc-c.md` → `OC&C Strategy Consultants`

- [ ] **Step 4: Verify all 15 files exist**

Run:

```bash
ls by-company/ | wc -l
```

Expected: `15`

Run:

```bash
ls by-company/
```

Expected: `accenture-strategy.md at-kearney.md arthur-d-little.md bain.md bcg.md deloitte.md ey-parthenon.md lek.md mckinsey.md monitor.md oc-c.md oliver-wyman.md pwc-strategy.md roland-berger.md strategyand.md`

- [ ] **Step 5: Commit**

```bash
cd /Users/duobinji/Documents/GitHub/strategic-consulting
git add by-company/
git commit -m "chore: scaffold 15 by-company index pages"
```

---

## Task 3: McKinsey 7S card (calibration case)

**Files:**
- Create: `frameworks/mckinsey-7s.md`
- Modify: `by-company/mckinsey.md`
- Modify: `docs/methodology-catalog.md` (append row)

**Interfaces:**
- Consumes: `docs/schema.md` (12-field definition), `AGENTS.md` rules
- Produces: First complete card with `status: draft`. Card uses `name_en: The 7S Framework`, `category: framework`, `source_company: ["McKinsey & Company"]`, `created_year: 1978`. Personal layer (`## 个人批注`) is a stub with an `**AI 建议**` sub-stub — owner will write it.

- [ ] **Step 1: Write the factual-layer draft to `frameworks/mckinsey-7s.md`**

Content:

```markdown
---
name: 麦肯锡 7S
name_en: The 7S Framework
source_company:
  - McKinsey & Company
category: framework
created_year: 1978
one_line_summary: 通过 7 个相互关联的内部要素诊断组织效能的诊断框架。
purpose: |
  找出组织战略与执行之间的不匹配点，给重组、并购整合、变革项目提供抓手。
  该框架的核心假设是：组织作为一个系统，7 个要素必须"对齐"才能高效运转。
when_to_use: |
  - 适用：组织变革/重组、并购整合（PMI）、领导力诊断
  - 不适用：高速变化的初创公司（要素尚未稳定）、纯战略制定（缺执行视角）
key_steps:
  - Hard S：Strategy / Structure / Systems
  - Soft S：Shared Values / Skills / Style / Staff
  - 对每个 S 评估当前状态与一致性，找出"未对齐"的组合
  - 提出重新对齐的方案
limitations:
  - "Soft S 难以量化，咨询团队易给客户贴没验证的标签"
  - "被批评为'什么都能往里塞'，区分度低；和 Galbraith Star Model 重叠度高"
  - "[争议] 一些研究者认为 Shared Values 应当是结果而非独立要素"
related_methods:
  - "[[galbraith-star-model]]"
  - "[[bcg-organizational-advantage]]"
tags:
  - organizational
  - diagnostic
  - classic
status: draft
---

# 麦肯锡 7S

> 通过 7 个相互关联的内部要素诊断组织效能的诊断框架。

## 起源与定位

1978 年由 McKinsey 顾问 Tom Peters 与 Robert Waterman 在《In Search of Excellence》中系统化提出。该框架最初用于分析为什么"卓越公司"持续优秀，后续被广泛应用于组织诊断。

## 核心内容

七个要素分两组：

- **Hard S**（硬件三件）：Strategy 战略 / Structure 结构 / Systems 系统与制度
- **Soft S**（软件四件）：Shared Values 共享价值观 / Skills 技能 / Style 领导风格 / Staff 人员

诊断逻辑：要素之间的"对齐度"决定组织效能。最常见应用是画出 7S 图，标记每个要素的当前状态，找出未对齐组合。

## 适用与不适用

**适用**：

- 并购整合中评估双方组织差异
- 大型变革项目的现状诊断
- 领导力团队的工作坊

**不适用**：

- 20 人以下创业公司——要素尚未稳定
- 单纯战略制定——本框架偏执行与组织

## 局限与争议

- Soft S 缺乏量化标准，依赖顾问经验，容易"什么都能往里塞"
- 与 Galbraith Star Model 高度重叠，独立价值被质疑
- [争议] 一些学者（如 Richard Pascale）认为 Shared Values 应被视为结果而非独立要素

## 与其他方法论的关系

- **演进**：与 Galbraith Star Model（1970s）几乎同期出现，互相影响
- **对比**：Weisbord Six-Box Model 提供了更精简的替代
- **应用层**：常被作为后续变革框架（如 Kotter 8-Step）的诊断前置工具

## 个人批注

<!-- 由所有者撰写。AI 不编辑此 section。 -->

**AI 建议**：

<!-- AI 在此提供建议。所有者原话在上方，AI 不覆盖。 -->
```

- [ ] **Step 2: Run the schema self-check (manual)**

Verify the file has all 12 content fields + `status` in frontmatter. If any are missing or empty, fix before continuing.

- [ ] **Step 3: Append row to `docs/methodology-catalog.md`**

Find the `## Frameworks` section table header. Append a row after the existing empty line:

```markdown
| 麦肯锡 7S | McKinsey & Company | 1978 | draft |
```

- [ ] **Step 4: Append row to `by-company/mckinsey.md`**

Find the `## 方法论索引` table. Append a row:

```markdown
| [麦肯锡 7S](../frameworks/mckinsey-7s.md) | framework | draft |
```

- [ ] **Step 5: Owner fact-checks and writes personal notes**

Owner reviews each factual section against a second source (Wikipedia, original book, McKinsey public materials), corrects any `[需核实]` or `[争议]` items, then writes content under `## 个人批注` (above the `**AI 建议**` section). When done, change `status: draft` → `status: annotated` in the frontmatter.

If any factual claim is unverifiable, keep the `[需核实]` tag and DO NOT promote past `fact-checked`.

- [ ] **Step 6: Commit**

```bash
cd /Users/duobinji/Documents/GitHub/strategic-consulting
git add frameworks/mckinsey-7s.md docs/methodology-catalog.md by-company/mckinsey.md
git commit -m "feat(frameworks): add McKinsey 7S card (calibration)"
```

---

## Task 4: Schema retro after first card

**Files:**
- Modify (if needed): `docs/schema.md`
- Modify (if needed): `AGENTS.md`
- Modify (if needed): `frameworks/mckinsey-7s.md`

**Interfaces:**
- Consumes: Insights from completing Task 3
- Produces: Schema and rules refined based on first-card friction

- [ ] **Step 1: Owner identifies friction points**

Owner reviews the completed 7S card and answers these questions out loud (to AI or to self):

1. Were any 12 fields unused or redundant? (`when_to_use` vs `limitations` overlap? `related_methods` too thin?)
2. Were any body sections under- or over-used?
3. Did `tags` field pull weight, or was it noise?
4. Did the AI draft contain any factual errors?
5. Did the bidirectional link rule create friction (no reciprocal card yet)?

- [ ] **Step 2: Decide and apply adjustments**

For each friction point, choose one of:

- **Adjust schema**: edit `docs/schema.md`. Only do this if a field is genuinely unusable. Do NOT add fields.
- **Adjust rules**: edit `AGENTS.md`. Tighten the wording where it caused confusion.
- **Adjust template**: edit the body section names in `docs/schema.md` only if a section was always empty.
- **No change**: friction was just first-card unfamiliarity.

If schema changed, update `frameworks/mckinsey-7s.md` to conform.

- [ ] **Step 3: Commit any schema adjustments**

```bash
cd /Users/duobinji/Documents/GitHub/strategic-consulting
git add docs/schema.md AGENTS.md frameworks/mckinsey-7s.md
git commit -m "refactor: tighten schema after first card calibration"
```

Skip this commit if no adjustments were made.

---

## Task 5: BCG Growth-Share Matrix card

**Files:**
- Create: `frameworks/bcg-growth-share-matrix.md`
- Modify: `by-company/bcg.md`
- Modify: `docs/methodology-catalog.md`

**Interfaces:**
- Consumes: Same as Task 3
- Produces: Second card with `status: draft`. `name_en: BCG Growth-Share Matrix`, `category: framework`, `source_company: ["Boston Consulting Group"]`, `created_year: 1970`. Tests `limitations` field thoroughly (this matrix is famously criticized).

- [ ] **Step 1: Write factual-layer draft to `frameworks/bcg-growth-share-matrix.md`**

Content:

```markdown
---
name: BCG 增长矩阵
name_en: BCG Growth-Share Matrix
source_company:
  - Boston Consulting Group
category: framework
created_year: 1970
one_line_summary: 用"市场增长率"和"相对市场份额"两个维度将业务单元分为四类的投资组合工具。
purpose: |
  帮助多元化公司决定在哪些业务上投入、哪些业务上收割或退出。
  该框架基于"经验曲线"假设：市场份额越大、单位成本越低、现金流越强。
when_to_use: |
  - 适用：多元化企业的 portfolio 决策（20+ 业务单元的公司）
  - 不适用：单一业务公司；高速变化的科技/平台型业务（市场份额不稳定）
key_steps:
  - 横轴：相对市场份额（公司份额 / 最大竞争对手份额；>1 表示领先）
  - 纵轴：市场增长率（行业年增长率）
  - 落入四象限：Stars（明星）/ Cash Cows（金牛）/ Question Marks（问题）/ Dogs（瘦狗）
  - 对每象限给出战略建议：投入 / 维持 / 选择性 / 退出
limitations:
  - "二元分类丢失信息——市场份额是连续变量，硬切象限会造成误导"
  - "被广泛批评为过度简化，被催生了'杀死 BCG 矩阵'的反思浪潮"
  - "[争议] '经验曲线'假设在服务业、平台经济中不成立"
  - "[争议] 1970s 后续 BCG 自己也在修正，强调需结合行业生命周期等其他框架"
related_methods:
  - "[[ge-mckinsey-matrix]]"
  - "[[ashridge-portfolio-display]]"
  - "[[adl-matrix]]"
tags:
  - portfolio
  - strategy
  - classic
  - contested
status: draft
---

# BCG 增长矩阵

> 用"市场增长率"和"相对市场份额"两个维度将业务单元分为四类的投资组合工具。

## 起源与定位

1970 年由 BCG 顾问 Bruce Henderson 在其"Perspective"系列中首次提出，与"经验曲线"概念同期。该矩阵是经验曲线理论的应用工具，1970s 在多元化大企业（如 GE、Honeywell）中风靡一时。

## 核心内容

横轴：相对市场份额（公司份额 / 最大竞争对手份额；>1 表示领先）
纵轴：市场增长率（行业年增长率）

四象限及战略建议：

- **Stars（明星）**：高增长 + 高份额。投入扩大优势
- **Cash Cows（金牛）**：低增长 + 高份额。收割现金
- **Question Marks（问题）**：高增长 + 低份额。选择性投入或退出
- **Dogs（瘦狗）**：低增长 + 低份额。退出或收割

## 适用与不适用

**适用**：

- 多元化企业的 portfolio 复盘
- 母公司/事业部层级的资源配置讨论

**不适用**：

- 单一业务公司
- 平台型/网络效应业务（如社交平台）

## 局限与争议

- 二元分类丢失信息：市场份额是连续变量，硬切象限易误导
- 经验曲线假设在服务业和平台经济中不成立
- 1980s 出现"杀死 BCG 矩阵"的反思潮；GE/McKinsey 矩阵被提出作为改进
- [争议] 该框架是否过度简化：BCG 内部后续修正，强调需结合行业生命周期等其他工具

## 与其他方法论的关系

- **演进**：ADL Matrix（更早期 1970s）、GE/McKinsey Matrix（1970s 后期改进）
- **改进**：Ashridge Portfolio Display 用 critical success factors 替代单一市场份额
- **替代**：对于复杂环境，BCG 自己后续推出"价值为基础的 portfolio"模型

## 个人批注

<!-- 由所有者撰写。AI 不编辑此 section。 -->

**AI 建议**：

<!-- AI 在此提供建议。所有者原话在上方，AI 不覆盖。 -->
```

- [ ] **Step 2: Run schema self-check**

Verify all 12 content fields + `status` present and correctly typed.

- [ ] **Step 3: Append row to `docs/methodology-catalog.md`**

Find `## Frameworks` table. Append:

```markdown
| BCG 增长矩阵 | Boston Consulting Group | 1970 | draft |
```

- [ ] **Step 4: Append row to `by-company/bcg.md`**

Find `## 方法论索引` table. Append:

```markdown
| [BCG 增长矩阵](../frameworks/bcg-growth-share-matrix.md) | framework | draft |
```

- [ ] **Step 5: Owner fact-checks and writes personal notes**

Owner reviews the draft, marks unverifiable claims `[需核实]`, then writes the personal layer. Promote `status` to `annotated`.

- [ ] **Step 6: Commit**

```bash
cd /Users/duobinji/Documents/GitHub/strategic-consulting
git add frameworks/bcg-growth-share-matrix.md docs/methodology-catalog.md by-company/bcg.md
git commit -m "feat(frameworks): add BCG Growth-Share Matrix"
```

---

## Task 6: Porter's Five Forces card

**Files:**
- Create: `tools/porters-five-forces.md`
- Modify: `docs/methodology-catalog.md`

**Interfaces:**
- Produces: First tool-type card. `name_en: Porter's Five Forces`, `category: tool`, `source_company: ["Michael Porter (Harvard)"]` — tests individual author handling. `created_year: 1979`.

- [ ] **Step 1: Write factual-layer draft to `tools/porters-five-forces.md`**

Content:

```markdown
---
name: 波特五力
name_en: Porter's Five Forces
source_company:
  - Michael Porter (Harvard)
category: tool
created_year: 1979
one_line_summary: 从五个结构性力量评估行业平均盈利能力的诊断工具。
purpose: |
  判断一个行业的结构性吸引力，识别能挤压利润的力量。
  该框架假设：行业平均利润率由结构决定，而非单个公司表现。
when_to_use: |
  - 适用：进入新行业前的判断、portfolio 决策、竞争战略起点
  - 不适用：单一公司业绩诊断、非营利组织
key_steps:
  - 评估五种力量：行业内部竞争烈度 / 新进入者威胁 / 替代品威胁 / 供应商议价能力 / 买家议价能力
  - 每种力量打分（高/中/低）
  - 综合判断行业吸引力
limitations:
  - "静态视角——忽略技术变革、政策变化对结构的颠覆"
  - "[争议] 五种力量之间的相互作用被低估；现实中往往是相互强化"
  - "依赖分析者的判断，主观性强"
related_methods:
  - "[[value-chain]]"
  - "[[pestel]]"
tags:
  - industry-analysis
  - strategy
  - classic
status: draft
---

# 波特五力

> 从五个结构性力量评估行业平均盈利能力的诊断工具。

## 起源与定位

1979 年由哈佛商学院教授 Michael Porter 在《How Competitive Forces Shape Strategy》(HBR) 中首次提出。该框架是 Porter 竞争战略体系（"三战略" + 价值链 + 五力）的核心工具。

## 核心内容

五种力量：

1. **行业内部竞争烈度**（现有对手之间的对抗）
3. **新进入者威胁**（壁垒高低）
5. **替代品威胁**（不同行业但功能相似的产品）
7. **供应商议价能力**（供应商集中度、转换成本）
9. **买家议价能力**（买家集中度、价格敏感度）

## 适用与不适用

**适用**：

- 进入新行业前的吸引力判断
- M&A 目标筛选
- 长期竞争战略的起点

**不适用**：

- 单一公司业绩诊断（用 4C / 价值链更合适）
- 非营利组织（驱动力不同）

## 局限与争议

- 静态视角：忽略技术变革、政策变化的颠覆作用（如网约车颠覆出租车行业）
- 五种力量间的相互作用被低估（现实中往往是相互强化）
- 主观性强：打分依赖分析者判断
- [争议] 平台经济下，"买家"和"卖家"角色模糊，五力分类不再清晰

## 与其他方法论的关系

- **延伸**：PESTEL 补充宏观环境，3C 补充公司与竞争者视角
- **配套**：与 Porter 价值链分析配合使用（行业看五力、公司看价值链）
- **批评后续**：Brandenburger & Nalebuff 的"合作竞争"模型修正了五力

## 个人批注

<!-- 由所有者撰写。AI 不编辑此 section。 -->

**AI 建议**：

<!-- AI 在此提供建议。所有者原话在上方，AI 不覆盖。 -->
```

- [ ] **Step 2: Run schema self-check**

Verify all 12 content fields + `status` present.

- [ ] **Step 3: Append row to `docs/methodology-catalog.md`**

Find `## Tools` table. Append:

```markdown
| 波特五力 | Michael Porter (Harvard) | 1979 | draft |
```

- [ ] **Step 4: NO by-company index update**

This card's `source_company` is an individual author, not a firm in `by-company/`. Skip the index update. (This is the test for handling non-firm sources.)

- [ ] **Step 5: Owner fact-checks and writes personal notes**

Owner reviews, marks unverifiable claims, writes personal layer. Promote `status` to `annotated`.

- [ ] **Step 6: Commit**

```bash
cd /Users/duobinji/Documents/GitHub/strategic-consulting
git add tools/porters-five-forces.md docs/methodology-catalog.md
git commit -m "feat(tools): add Porter's Five Forces (individual author source)"
```

---

## Task 7: MECE / Issue Tree card

**Files:**
- Create: `processes/mece.md`
- Modify: `by-company/mckinsey.md`
- Modify: `docs/methodology-catalog.md`

**Interfaces:**
- Produces: First process-type card. `category: process`, `source_company: ["industry-wide", "McKinsey & Company"]` — tests multi-source handling with no single owner.

- [ ] **Step 1: Write factual-layer draft to `processes/mece.md`**

Content:

```markdown
---
name: MECE / 议题树
name_en: MECE / Issue Tree
source_company:
  - industry-wide
  - McKinsey & Company
category: process
created_year: 1970
one_line_summary: 将问题分解为相互独立、完全穷尽的子问题，形成树状分析结构。
purpose: |
  在项目启动期把客户的"大问题"拆解成可被分别解决的子问题。
  MECE 是 Barbara Minto 1960s 在 McKinsey 工作时提出，被 Minto Pyramid Principle 体系化推广。
when_to_use: |
  - 适用：复杂问题的诊断项目起点、咨询 deck 的 story line 构建
  - 不适用：纯创意发散阶段、需要保留可能性的探索阶段
key_steps:
  - 明确要回答的"根问题"
  - 用 MECE 原则拆分（互不重叠 / 完全覆盖）
  - 拆到 2-3 层（避免过度下钻）
  - 对每个叶子问题定义 analytic question
  - 在每个分支上提出 hypothesis（hypothesis-driven 流程的入口）
limitations:
  - "强制 MECE 可能错过非正交的关系"
  - "拆分质量取决于分析师对问题的先验理解"
  - "[争议] 强 MECE 在探索阶段可能过早收敛"
related_methods:
  - "[[hypothesis-driven-problem-solving]]"
  - "[[minto-pyramid-principle]]"
tags:
  - problem-solving
  - structure
  - classic
status: draft
---

# MECE / 议题树

> 将问题分解为相互独立、完全穷尽的子问题，形成树状分析结构。

## 起源与定位

MECE（Mutually Exclusive, Collectively Exhaustive / 相互独立、完全穷尽）由 Barbara Minto 1960s 在 McKinsey 工作时提出，作为金字塔原理（Minto Pyramid Principle）的基础。该原则现已成为整个咨询行业的"通用语"，不专属任何一家公司。

## 核心内容

拆分原则：

- **Mutually Exclusive（ME）**：子问题之间不重叠
- **Collectively Exhaustive（CE）**：子问题加起来覆盖全部

工作流：

1. 明确"根问题"——客户真正要回答什么
2. 拆分到 2-3 层，避免过度下钻
3. 每个叶子节点定义 analytic question
4. 每个分支提 hypothesis（与假设驱动方法联动）

## 适用与不适用

**适用**：

- 复杂诊断项目的起点
- 咨询 deck 的 storyline 构建
- 团队分工（每个分支由不同 analyst 平行推进）

**不适用**：

- 纯创意发散阶段
- 探索期——强 MECE 可能过早收敛，错过非正交关系

## 局限与争议

- 强制拆分可能错过非正交的关系
- 拆分质量取决于分析师对问题的先验理解（先验错了，结构也错）
- 与 hypothesis-driven 方法强耦合，但本身不含 hypothesis 假设
- [争议] 探索阶段是否应强 MECE：部分咨询公司（如 BCG）倾向更灵活

## 与其他方法论的关系

- **配套**：与 hypothesis-driven problem solving 几乎总是组合使用
- **应用层**：Minto Pyramid Principle 把 MECE 树包装成自上而下的沟通结构
- **替代/补充**：思维导图、affinity diagram 是更发散的替代

## 个人批注

<!-- 由所有者撰写。AI 不编辑此 section。 -->

**AI 建议**：

<!-- AI 在此提供建议。所有者原话在上方，AI 不覆盖。 -->
```

- [ ] **Step 2: Run schema self-check**

Verify all 12 content fields + `status` present.

- [ ] **Step 3: Append row to `docs/methodology-catalog.md`**

Find `## Processes` table. Append:

```markdown
| MECE / 议题树 | industry-wide / McKinsey | 1970 | draft |
```

- [ ] **Step 4: Append row to `by-company/mckinsey.md`**

Find `## 方法论索引` table. Append:

```markdown
| [MECE / 议题树](../processes/mece.md) | process | draft |
```

- [ ] **Step 5: Owner fact-checks and writes personal notes**

Owner reviews, marks unverifiable claims, writes personal layer. Promote `status` to `annotated`.

- [ ] **Step 6: Commit**

```bash
cd /Users/duobinji/Documents/GitHub/strategic-consulting
git add processes/mece.md docs/methodology-catalog.md by-company/mckinsey.md
git commit -m "feat(processes): add MECE / Issue Tree (multi-source)"
```

---

## Task 8: Bain Net Promoter System card

**Files:**
- Create: `frameworks/bain-net-promoter-system.md`
- Modify: `by-company/bain.md`
- Modify: `docs/methodology-catalog.md`

**Interfaces:**
- Produces: Fourth framework card. `name_en: Bain Net Promoter System`, `category: framework`, `source_company: ["Bain & Company"]`, `created_year: 2003` — tests recent-method handling with `created_year` accuracy.

- [ ] **Step 1: Write factual-layer draft to `frameworks/bain-net-promoter-system.md`**

Content:

```markdown
---
name: 贝恩净推荐值体系
name_en: Bain Net Promoter System (NPS)
source_company:
  - Bain & Company
category: framework
created_year: 2003
one_line_summary: 用单一问题衡量客户忠诚度，并系统性地把 Promoters / Passives / Detractors 区分开来的客户体验管理体系。
purpose: |
  把"客户满意度"这种主观指标转化为可量化、可在公司层面追踪的忠诚度指标。
  NPS 与企业增长强相关（贝恩的实证研究），被作为公司战略层面的北极星指标之一。
when_to_use: |
  - 适用：B2C 服务的客户体验管理、订阅业务复购率提升
  - 不适用：纯交易型一次性购买（无忠诚度可言）、高度差异化 B2B 销售
key_steps:
  - 问单一问题：0-10 分推荐意愿
  - 分类：Promoters (9-10) / Passives (7-8) / Detractors (0-6)
  - 计算 NPS = %Promoters - %Detractors
  - 配套"闭环行动"：对 Detractors 立即跟进、对 Promoters 鼓励推荐
  - 持续追踪，按业务线、客户群拆分
limitations:
  - "单一问题遗漏客户感受的丰富维度"
  - "跨文化可比性弱——不同地区推荐意愿基线不同"
  - "[争议] NPS 与业务增长的强因果关系被部分学术研究质疑"
  - "[争议] '被动者 (Passives)' 的处理过于粗放"
related_methods:
  - "[[customer-effort-score]]"
  - "[[voice-of-customer]]"
tags:
  - customer-experience
  - metric
  - growth
status: draft
---

# 贝恩净推荐值体系

> 用单一问题衡量客户忠诚度，并系统性地把 Promoters / Passives / Detractors 区分开来的客户体验管理体系。

## 起源与定位

2003 年由 Bain & Company 顾问 Frederick F. Reichheld 在《The One Number You Need to Grow》(HBR) 中首次提出。Bain 后续将其扩展为 NPS 体系（含流程、闭环、IT 支持），现已成为全球客户体验管理的标杆指标。

## 核心内容

单一问卷问题：

> "您向朋友或同事推荐我们公司的可能性有多大？"（0 = 完全不可能，10 = 极有可能）

分类：

- **Promoters (9-10)**：热情拥护者
- **Passives (7-8)**：满意但不主动推荐
- **Detractors (0-6)**：不满意且可能劝阻他人

**NPS = %Promoters − %Detractors**（范围 −100 到 +100）

配套"闭环行动"：对 Detractors 立即服务补救、对 Promoters 鼓励口碑推荐。

## 适用与不适用

**适用**：

- B2C 服务（电信、银行、零售、SaaS）
- 订阅型业务（复购率管理）
- 公司战略层的"北极星指标"

**不适用**：

- 一次性交易型购买
- 高度定制化 B2B 大客户销售（关系比推荐意愿更复杂）

## 局限与争议

- 单一问题遗漏客户感受的丰富维度
- 跨文化可比性弱——不同地区"推荐意愿"基线不同（亚洲人普遍打分偏低）
- 配套"闭环行动"成本高，小公司难以负担
- [争议] Reichheld 2011 年承认金融行业 NPS 与增长因果关系比早期论证弱
- [争议] "被动者"分桶过于粗放，丢失了 7 分和 8 分之间的差异

## 与其他方法论的关系

- **配套**：Customer Effort Score（CES）衡量交互难易，Voice-of-Customer（PM）补充定性反馈
- **演进**：Bain 后续推出 NPS 3、Loyalty Ecosystem 框架
- **批评后续**：部分学者主张用 Customer Lifetime Value 替代 NPS

## 个人批注

<!-- 由所有者撰写。AI 不编辑此 section。 -->

**AI 建议**：

<!-- AI 在此提供建议。所有者原话在上方，AI 不覆盖。 -->
```

- [ ] **Step 2: Run schema self-check**

Verify all 12 content fields + `status` present.

- [ ] **Step 3: Append row to `docs/methodology-catalog.md`**

Find `## Frameworks` table. Append:

```markdown
| 贝恩净推荐值体系 | Bain & Company | 2003 | draft |
```

- [ ] **Step 4: Append row to `by-company/bain.md`**

Find `## 方法论索引` table. Append:

```markdown
| [贝恩净推荐值体系](../frameworks/bain-net-promoter-system.md) | framework | draft |
```

- [ ] **Step 5: Owner fact-checks and writes personal notes**

Owner reviews, marks unverifiable claims, writes personal layer. Promote `status` to `annotated`.

- [ ] **Step 6: Commit**

```bash
cd /Users/duobinji/Documents/GitHub/strategic-consulting
git add frameworks/bain-net-promoter-system.md docs/methodology-catalog.md by-company/bain.md
git commit -m "feat(frameworks): add Bain Net Promoter System (recent method test)"
```

---

## Task 9: First-batch retrospective

**Files:**
- Modify (if needed): `docs/schema.md`
- Modify (if needed): `AGENTS.md`
- Modify (if needed): `README.md`
- Modify (if needed): any of the 5 card files

**Interfaces:**
- Consumes: All 5 completed cards from Tasks 3, 5, 6, 7, 8
- Produces: Adjusted documentation; a decision whether to continue building cards or pause for tool work

- [ ] **Step 1: Verify first-batch DoD**

Run:

```bash
cd /Users/duobinji/Documents/GitHub/strategic-consulting
grep -r "^status: annotated" frameworks/ processes/ tools/ | wc -l
```

Expected: `5`

Run:

```bash
grep -c "^| " docs/methodology-catalog.md
```

Expected: ≥ 5 (header rows + content rows)

Run:

```bash
grep "frameworks\|processes\|tools" by-company/mckinsey.md by-company/bcg.md by-company/bain.md
```

Expected: Each of `mckinsey.md`, `bcg.md`, `bain.md` has at least one link to a card file.

If any check fails, return to the relevant Task and complete it before continuing.

- [ ] **Step 2: Review all 5 cards for cross-card consistency**

Check:

- All `related_methods` reciprocal? (A `[[B]]` requires B to also reference A — once both cards exist, verify both ways.)
- All `tags` use the same vocabulary across cards? (e.g., is it "classic" or "classical"?)
- All `created_year` consistent format (integer, no ranges)?

- [ ] **Step 3: Apply retro adjustments**

For each inconsistency found in Step 2, fix inline. For schema-level changes (e.g., unifying tag vocabulary), update `docs/schema.md` and all affected cards.

- [ ] **Step 4: Update `README.md` with first-batch stats**

Edit the `## 如何新增一张卡片` section to include a "已完成方法论" subsection listing the 5 first-batch cards.

Append to `README.md`:

```markdown

## 已完成方法论（首批 5 张）

- 麦肯锡 7S（McKinsey）
- BCG 增长矩阵（BCG）
- 波特五力（Michael Porter / Harvard）
- MECE / 议题树（行业通用 / McKinsey canonical）
- 贝恩净推荐值体系（Bain）

完整列表见 `docs/methodology-catalog.md`。
```

- [ ] **Step 5: Commit retro**

```bash
cd /Users/duobinji/Documents/GitHub/strategic-consulting
git add docs/schema.md AGENTS.md README.md frameworks/ processes/ tools/ by-company/ docs/methodology-catalog.md
git commit -m "refactor: first-batch retrospective adjustments"
```

---

## Task 10: (Optional) Add validation tools

**Files:**
- Create: `tools/check-schema.py`
- Create: `tools/check-links.py`

Skip this task if the owner prefers manual maintenance. The skill recommends adding validation when there are 5+ cards, so this is the right time.

**Interfaces:**
- Consumes: All card files in `frameworks/`, `processes/`, `tools/`
- Produces: Exit code 0 if all valid, non-zero + error list if any issue

- [ ] **Step 1: Install pytest if not already available**

Run:

```bash
python3 -m pytest --version || python3 -m pip install pytest
```

Expected: `pytest X.Y.Z` printed. If pytest is already there, skip the install.

- [ ] **Step 1a: Write the failing test for schema check**

Create `tests/test_check_schema.py`:

```python
import subprocess
import tempfile
from pathlib import Path

SCRIPT = Path(__file__).resolve().parents[1] / "tools" / "check-schema.py"


def run_script(cwd: Path) -> subprocess.CompletedProcess:
    return subprocess.run(
        ["python3", str(SCRIPT)],
        cwd=str(cwd),
        capture_output=True,
        text=True,
    )


def test_missing_field_detected(tmp_path: Path):
    (tmp_path / "frameworks").mkdir()
    card = tmp_path / "frameworks" / "bad.md"
    card.write_text(
        "---\n"
        "name: Test\n"
        "category: framework\n"
        "status: draft\n"
        "---\n\n"
        "# Test\n\nbody\n",
        encoding="utf-8",
    )
    result = run_script(tmp_path)
    assert result.returncode != 0
    assert "name_en" in result.stdout or "name_en" in result.stderr


def test_complete_card_passes(tmp_path: Path):
    (tmp_path / "frameworks").mkdir()
    card = tmp_path / "frameworks" / "good.md"
    card.write_text(
        "---\n"
        "name: Test\n"
        "name_en: Test\n"
        "source_company: [Test Co]\n"
        "category: framework\n"
        "created_year: 2020\n"
        "one_line_summary: A test.\n"
        "purpose: Test purpose.\n"
        "when_to_use: Test usage.\n"
        "key_steps: [step1]\n"
        "limitations: [lim1]\n"
        "related_methods: []\n"
        "tags: [test]\n"
        "status: draft\n"
        "---\n\n"
        "# Test\n\nbody\n",
        encoding="utf-8",
    )
    result = run_script(tmp_path)
    assert result.returncode == 0, result.stdout + result.stderr
```

- [ ] **Step 2: Run the test to confirm it fails**

Run: `python3 -m pytest tests/test_check_schema.py -v`
Expected: FAIL with "No module named" or "FileNotFoundError" (script doesn't exist yet).

- [ ] **Step 3: Implement `tools/check-schema.py`**

```python
#!/usr/bin/env python3
"""Validate frontmatter on every card under frameworks/, processes/, tools/."""

import re
import sys
from pathlib import Path

REQUIRED_FIELDS = {
    "name",
    "name_en",
    "source_company",
    "category",
    "created_year",
    "one_line_summary",
    "purpose",
    "when_to_use",
    "key_steps",
    "limitations",
    "related_methods",
    "tags",
    "status",
}
VALID_STATUS = {"draft", "fact-checked", "annotated", "archived"}
VALID_CATEGORY = {"framework", "process", "tool"}
FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---\n", re.DOTALL)


def parse_frontmatter(text: str) -> dict | None:
    match = FRONTMATTER_RE.match(text)
    if not match:
        return None
    fm: dict = {}
    current_key = None
    for line in match.group(1).splitlines():
        if line.startswith("  - ") and current_key:
            fm[current_key].append(line[4:].strip())
        elif ":" in line and not line.startswith(" "):
            key, _, value = line.partition(":")
            current_key = key.strip()
            value = value.strip()
            if value == "":
                fm[current_key] = []
            elif value.startswith("[") and value.endswith("]"):
                inner = value[1:-1].strip()
                fm[current_key] = [x.strip() for x in inner.split(",")] if inner else []
            else:
                fm[current_key] = value
    return fm


def validate_card(path: Path) -> list[str]:
    errors: list[str] = []
    text = path.read_text(encoding="utf-8")
    fm = parse_frontmatter(text)
    if fm is None:
        return [f"{path}: missing frontmatter"]
    missing = REQUIRED_FIELDS - fm.keys()
    if missing:
        errors.append(f"{path}: missing fields: {sorted(missing)}")
    if "status" in fm and fm["status"] not in VALID_STATUS:
        errors.append(f"{path}: invalid status '{fm['status']}'")
    if "category" in fm and fm["category"] not in VALID_CATEGORY:
        errors.append(f"{path}: invalid category '{fm['category']}'")
    if "related_methods" in fm and not isinstance(fm["related_methods"], list):
        errors.append(f"{path}: related_methods must be a list")
    return errors


def main() -> int:
    root = Path.cwd()
    card_dirs = [root / "frameworks", root / "processes", root / "tools"]
    all_errors: list[str] = []
    for d in card_dirs:
        if not d.exists():
            continue
        for card in sorted(d.glob("*.md")):
            all_errors.extend(validate_card(card))
    if all_errors:
        for err in all_errors:
            print(err)
        return 1
    print("All cards pass schema validation.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
```

- [ ] **Step 4: Run the test to confirm it passes**

Run: `python3 -m pytest tests/test_check_schema.py -v`
Expected: PASS (2 tests).

- [ ] **Step 5: Run the script against the real cards**

Run: `python3 tools/check-schema.py`
Expected: `All cards pass schema validation.` (or specific errors to fix).

- [ ] **Step 6: Install pytest if not already available** (skip if pytest is already present from Task 10 Step 1)

Run:

```bash
python3 -m pytest --version || python3 -m pip install pytest
```

Expected: `pytest X.Y.Z` printed.

- [ ] **Step 6a: Write the failing test for link check**

Create `tests/test_check_links.py`:

```python
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
```

- [ ] **Step 7: Run the test to confirm it fails**

Run: `python3 -m pytest tests/test_check_links.py -v`
Expected: FAIL (script doesn't exist).

- [ ] **Step 8: Implement `tools/check-links.py`**

```python
#!/usr/bin/env python3
"""Validate that every [[slug]] in card related_methods resolves and is bidirectional."""

import re
import sys
from pathlib import Path

LINK_RE = re.compile(r"\[\[([^\]]+)\]\]")


def collect_slugs(root: Path) -> set[str]:
    slugs: set[str] = set()
    for d in [root / "frameworks", root / "processes", root / "tools"]:
        if not d.exists():
            continue
        for card in d.glob("*.md"):
            slugs.add(card.stem)
    return slugs


def collect_links(card: Path) -> set[str]:
    return set(LINK_RE.findall(card.read_text(encoding="utf-8")))


def main() -> int:
    root = Path.cwd()
    slugs = collect_slugs(root)
    errors: list[str] = []
    link_map: dict[str, set[str]] = {}
    for d in [root / "frameworks", root / "processes", root / "tools"]:
        if not d.exists():
            continue
        for card in d.glob("*.md"):
            links = collect_links(card)
            link_map[card.stem] = links
            for link in links:
                if link not in slugs:
                    errors.append(f"{card}: dangling link [[{link}]]")
    for src, links in link_map.items():
        for dst in links:
            if dst in link_map and src not in link_map[dst]:
                errors.append(
                    f"{src}.md links [[{dst}]] but {dst}.md does not link back"
                )
    if errors:
        for err in errors:
            print(err)
        return 1
    print("All related_methods links are valid and bidirectional.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
```

- [ ] **Step 9: Run the test to confirm it passes**

Run: `python3 -m pytest tests/test_check_links.py -v`
Expected: PASS (2 tests).

- [ ] **Step 10: Run the script against the real cards**

Run: `python3 tools/check-links.py`
Expected: `All related_methods links are valid and bidirectional.` (or specific errors — most first-batch cards reference non-existent related methods like `galbraith-star-model`, `bcg-organizational-advantage`, etc. — these are intentional "future work" links; either remove them or create stub cards.)

Decision: For links to non-existent methods (which is the case for most `related_methods` in the first batch), the owner should choose:
- **(a)** Remove the `[[X]]` references from `related_methods` until X exists as a card.
- **(b)** Create empty stub cards for the linked methods.
- **(c)** Accept dangling links and skip running this script until more cards exist.

Recommendation: (a) — remove dangling links, add them back when the referenced card is built.

- [ ] **Step 11: Commit validation tools**

```bash
cd /Users/duobinji/Documents/GitHub/strategic-consulting
git add tools/check-schema.py tools/check-links.py tests/
git commit -m "feat(tools): add schema and link validation scripts"
```

---

## Self-Review Notes

**Spec coverage check** (spec section → task):

- §1 Purpose → covered by README + Task 1
- §2 Scope → covered by Task 1 (out-of-scope items noted in spec, no task needed)
- §3 User profile → covered by README + AGENTS tone guidance
- §4 Directory structure → covered by Task 1 (folders) + Task 2 (by-company files)
- §5 Naming conventions → covered by AGENTS.md + Task 1 schema doc
- §6 Card schema → covered by `docs/schema.md` (Task 1) + each card task
- §7 Card body structure → covered by each card task (Task 3, 5, 6, 7, 8)
- §8 Workflow → covered by Task 1 (bootstrap), Tasks 3-8 (per-card flow), Task 9 (retro)
- §9 AI rules → covered by AGENTS.md (Task 1)
- §10 Tooling → covered by Task 10 (optional)
- §11 First batch — 5 cards → covered by Tasks 3, 5, 6, 7, 8
- §12 Cadence → covered by Tasks 1, 3 (week 1), 5-8 (weeks 2-3), 9 (retro)
- §13 DoD for first batch → covered by Task 9 Step 1
- §14 Open questions → intentionally deferred (no tasks needed)

**Placeholder scan**: No TBD/TODO in code blocks. The `[待补充]` placeholders in by-company index files are intentional and noted as "owner fills these later" — not plan placeholders.

**Type consistency check**: All `status` values use the same set across tasks. All card filenames use the same kebab-case pattern. All `category` values are from `{framework, process, tool}`.