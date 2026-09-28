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