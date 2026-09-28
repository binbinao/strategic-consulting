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

## 已完成方法论（首批 5 张）

- 麦肯锡 7S（McKinsey）
- BCG 增长矩阵（BCG）
- 波特五力（Michael Porter / Harvard）
- MECE / 议题树（行业通用 / McKinsey canonical）
- 贝恩净推荐值体系（Bain）

完整列表见 `docs/methodology-catalog.md`。