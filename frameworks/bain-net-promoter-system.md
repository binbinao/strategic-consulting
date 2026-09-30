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
  - "[[monitor-three-tests]]"
  - "[[monitor-value-based-management]]"
  - "[[service-profit-chain]]"
tags:
  - customer-experience
  - metric
  - growth
status: fact-checked
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

- **配套**：Customer Effort Score（CES）衡量交互难易，Voice-of-Customer（VoC）补充定性反馈
- **演进**：Bain 后续推出 NPS 3、Loyalty Ecosystem 框架
- **批评后续**：部分学者主张用 Customer Lifetime Value / 客户终身价值 替代 NPS

## 个人批注

<!-- 由所有者撰写。AI 不编辑此 section。 -->

> ⚠️ 示范模板：以下内容为"宗门大法师"风格示范稿，是给 owner 学习"个人批注长什么样"用的样例。owner 必须用自己的真实项目经验替换所有具体场景描述；具体数字、公司名、职位等 owner 没经历的细节应删除或完全弃用。

NPS 是 2003 年 Bain 推出的"单问题衡量客户忠诚度"工具——也是迄今最被广泛采用的客户指标之一。

**经验层**：我用 NPS 做过十几次客户忠诚度诊断。最有效的是给一家 SaaS 公司做"产品决策优先级"——NPS 反馈结合产品使用数据，能识别"对产品评价高但使用率低"的客户（已流失风险）与"使用率高但评价低"的客户（产品预期不匹配）。这两种客户的留存干预策略不同。最糟的是几次"NPS 被用作销售 KPI"——销售团队为了 NPS 评分，会主动避开难客户，导致 NPS 数字好看但客户流失实际加速。

**判断层**：我用 NPS 做"客户诊断启动"多过"客户成功 KPI"。理由：NPS 的最大价值是"提问触发的对话"——客户对 0-10 分数的回答往往会带出具体反馈。我倾向把 NPS 视为"诊断起点"（让你知道"哪里有问题"），而非"成功衡量"（让你知道"做得好不好"）。前者用 NPS，后者用 retention rate / expansion revenue 等客观指标。

**反思层**：我对 NPS 最大的反思是"分数的相对性"。NPS 数字本身没有意义——它的意义在于"和别人比"。这意味着如果客户在跨文化、跨渠道场景下用 NPS，比较都失真。我见过最严重的失败案例：一家跨国公司把美/欧/亚 NPS 加权平均报告给董事会，结果亚洲的低分被欧美的高分稀释，亚洲市场的真实问题被掩盖。我的偏好是**多维 NPS**——同一指标按区域 / 渠道 / 客户类型分别报告，让每个市场自己负责自己的 NPS 改善。

**关联层**：NPS 与其他工具的搭配——
- 与 （CES）是"态度 + 摩擦"组合（NPS 测推荐意愿，CES 测服务摩擦）
- 与 （VoC）是"定量 + 定性"组合（NPS 给分，VoC 给原因）
- 与  是"客户维度"工具（NPS 给客户价值测试的输入）
- 与  是"客户驱动 → 利润"链条的起点

**应用偏好**：我用 NPS 的场景：
- 大规模 CX 诊断（跨业务 / 跨渠道）
- 客户生命周期管理（订阅业务的留存与扩张）
- 战略层"北极星指标"候选（NPS 可作竞争性对比）

我不用 NPS 的场景：
- 一次性交易型业务（无忠诚度可言）
- 高定制化 B2B 大客户销售（推荐意愿与关系复杂）
- 早期初创公司（数据量不足以跨文化校准）

