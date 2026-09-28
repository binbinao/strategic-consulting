# Strategic Consulting 知识库

> 个人整理的战略咨询方法论知识库，覆盖 MBB + 四大 + 老牌战略所的招牌框架、做事流程、分析工具。

策略咨询领域里，每家老牌咨询公司都有自己沉淀多年的"招牌方法"。但这些方法散落在教材、案例、咨询师的退休回忆录里，没有一个统一的中文索引。本项目按统一模板系统整理主流方法论，事实层用 AI 起草、个人层由所有者撰写，目标是建立一个可长期沉淀、可双向交叉引用、可独立扩展的个人方法论库。

## 目录

- [收录范围](#收录范围)
- [目录结构](#目录结构)
- [卡片格式](#卡片格式)
- [双层内容约定](#双层内容约定)
- [工作流](#工作流)
- [验证工具](#验证工具)
- [已收录方法论](#已收录方法论)
- [路线图](#路线图)
- [AI 协作](#ai-协作)
- [许可](#许可)

## 收录范围

| 范围 | 包含 |
|---|---|
| **公司** | McKinsey、BCG、Bain、Deloitte、Accenture Strategy、PwC Strategy&、EY-Parthenon、Roland Berger、L.E.K.、A.T. Kearney、Strategy&（legacy）、Monitor、Arthur D. Little、Oliver Wyman、OC&C（14 家） |
| **方法类型** | `framework`（招牌框架）、`process`（做事流程）、`tool`（分析工具）三类全覆盖 |
| **不收录** | 行业特定咨询 playbook（医疗、金融等）、运营/IT 咨询方法（Six Sigma、ITIL 等）、内部 firm 文化/求职内容 |

## 目录结构

```
strategic-consulting/
├── README.md                          # 本文件
├── AGENTS.md                          # AI 协作规则
├── docs/
│   ├── schema.md                      # frontmatter 字段定义（权威）
│   └── methodology-catalog.md         # 完整方法论清单
├── by-company/                        # 按公司索引（一个公司一文件）
│   ├── mckinsey.md
│   ├── bcg.md
│   └── ...                            # 共 15 个文件
├── frameworks/                        # 招牌框架（如 7S、BCG 矩阵）
├── processes/                         # 做事流程（如 MECE、假设驱动）
└── tools/                             # 分析工具（如五力、价值链）
```

按类型落地（卡片实际位置）+ 按公司索引（快速跳转某公司的全部方法）混合组织；多公司共享方法放类型目录、不带公司前缀。

## 卡片格式

每张方法论卡片是一个 `.md` 文件，含 YAML frontmatter + 6 个 H2 body section。完整字段定义见 [`docs/schema.md`](docs/schema.md)。

字段（12 个内容字段 + 1 个工作流字段）：

- **name**、**name_en**、**source_company**、**category**（framework/process/tool）、**created_year**
- **one_line_summary**、**purpose**、**when_to_use**
- **key_steps**、**limitations**、**related_methods**（wikilink）、**tags**
- **status**（draft / fact-checked / annotated / archived）

Body 6 个 section（中文）：起源与定位 / 核心内容 / 适用与不适用 / 局限与争议 / 与其他方法论的关系 / 个人批注

**正面示例**——节选自 `frameworks/mckinsey-7s.md`：

```yaml
---
name: 麦肯锡 7S
name_en: The 7S Framework
source_company: [McKinsey & Company]
category: framework
created_year: 1978
one_line_summary: 通过 7 个相互关联的内部要素诊断组织效能。
limitations:
  - "Soft S 难以量化，咨询团队易给客户贴没验证的标签"
  - "[争议] 一些研究者认为 Shared Values 应作为结果而非独立要素"
status: draft
---
```

## 双层内容约定

每张卡片严格分两层：

- **事实层**（AI 起草，所有者事实核查）：5 个 body section + frontmatter。规则写在 [`AGENTS.md`](AGENTS.md)，核心约束：年份/作者/出处查不到标 `[需核实]`；多方观点冲突标 `[争议]`；每个事实层 section ≤ 300 中文字。
- **个人层**（所有者撰写，AI 不写）：`## 个人批注` body。允许口语、未完成思考、案例映射、质疑，不做事实核查。

如果 AI 想给个人层提建议，放在 `**AI 建议**` 子节，不覆盖所有者原话。

## 工作流

新增一张卡片的流程：

1. 在 `frameworks/` / `processes/` / `tools/` 中按 `{公司前缀}-{kebab-case-name}.md` 命名新建文件（多公司共享方法不带前缀）
2. 按 `docs/schema.md` 写 frontmatter + 6 个 body section
3. 更新对应 `by-company/*.md` 索引 + `docs/methodology-catalog.md`
4. **AI 起草事实层** → status: `draft`
5. **所有者事实核查 + 撰写个人层** → status: `annotated`

状态流转：`draft` → `fact-checked` → `annotated` → `archived`（如不再使用）。单所有者工作流 happy path 是 `draft → annotated`；`fact-checked` 留给"先把事实层交叉核对、暂时不写个人批注"的中间态。

## 验证工具

项目自带两个 Python 校验脚本 + pytest 测试：

```bash
# 校验所有卡片的 frontmatter（12 字段、status/category 取值、list 类型、6 个 body section）
python3 tools/check-schema.py

# 校验 related_methods 的 wikilink 是否存在且双向
python3 tools/check-links.py

# 运行单元测试（7 个）
python3 -m pytest tests/ -v
```

`check-schema.py` 实现了一个轻量 YAML frontmatter 解析器（不依赖 PyYAML），故意保持可移植。如未来要严格 YAML 兼容，建议替换为 PyYAML。

## 已收录方法论

当前共 **21 张**：14 个 framework + 2 个 process + 5 个 tool，涵盖 MBB（McKinsey、BCG、Bain）主要招牌方法、Porter 竞争战略体系、四大工具类方法（详见完整清单 [`docs/methodology-catalog.md`](docs/methodology-catalog.md) 与 [`by-company/`](by-company/) 索引）。

**第三批新增（5 张 MBB 招牌 framework）**：

| 方法论 | 首发 | 提出年份 | 类型 |
|---|---|---|---|
| BCG 经验曲线 | Boston Consulting Group | 1968 | framework |
| 麦肯锡三horizons增长框架 | McKinsey & Company | 1999 | framework |
| 波特三战略 | Michael Porter (Harvard) | 1980 | framework |
| BCG 智能简化 | Boston Consulting Group | 2013 | framework |
| 贝恩可复制业务模型 | Bain & Company | 2005 | framework |

## 路线图

**前三批已交付**（共 21 张卡片，所有 `related_methods` 双向链接闭环），后续推进顺序自由：

1. **首批卡片的 fact-check + 个人批注**（所有者主导）—— 跑通 owner 端完整流程
2. **覆盖 MBB + 四大其他招牌方法**——前三批已铺底 BCG Experience Curve、Smart Simplicity、Porter Generic Strategies、Bain Repeatable Model 等；下一步可补 BCG / Bain 漏网方法（如 BCG Time-Based Competition）
3. **覆盖老牌战略所的招牌方法**——Roland Berger、Monitor、AT Kearney 等
4. **中文本土咨询方法**（远期）—— 君智、华与华、和君、华夏基石等是否单独一层？见 spec §14

**已明确延后的字段**（spec §14）：`case_examples`、`evolution_history`、单独的 `comparisons/` 目录。

## AI 协作

事实层由 AI 起草，所有者负责核查 + 写个人层。完整规则见 [`AGENTS.md`](AGENTS.md)，核心三条：

- AI 不写 `## 个人批注` 正文
- AI 起草时不杜撰年份/作者/出处（查不到标 `[需核实]`）
- `related_methods` 双向链接：写 `[[B]]` 时必须同步更新 B

## 许可

个人知识库项目，内容按"署名-非商业"使用。引用本仓库内容时，请保留卡片标题和原文链接。

---

整理不易，欢迎 Issue 提具体方法论补充建议（但需附原始出处，本项目不为未经验证的方法背书）。