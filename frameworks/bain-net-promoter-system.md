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

**AI 建议**：

<!-- 以下是 AI 在 fact-check 后提供的候选角度供所有者参考，非所有者原话。所有者可选用、修改、或完全弃用。 -->

- **应用角度**：NPS 本质是"用一句话替代 100 道问卷"。你遇到过 NPS 在哪个场景真的驱动了行为改变？哪个场景只是"高管 KPI 摆设"？
- **争议延伸**：本卡片提到 Reichheld 2011 年承认因果关系较弱。可参考 HBR 2011 年 Reichheld 的"Reichheld redux" 系列文章，以及 Keiningham/Cooil/等人 2011 年在 HBR 上的反驳。学术文献后续还有多轮辩论。
- **跨文化可比性**：本卡片提到"亚洲人普遍打分偏低"——这是 NPS 的真实痛点。如果你在中文场景下用 NPS，做过哪些跨文化调整？是用中位数代替均值，还是干脆换工具？
- **NPS vs. CES vs. VoC**：本卡片 `related_methods` 链到 `customer-effort-score`（CES）和 `voice-of-customer`（VoC）——这是 Bain 自家 NPS 的两个补充指标。如果你在做 CX 项目，NPS / CES / VoC 哪个是主指标？为什么？
- **被动者（Passives）问题**：本卡片提到 "被动者分桶过于粗放"——这是个 NPS 的著名短板。如果你处理 Passives 的实际信号，会拆成 7 / 8 还是直接用 "推荐意愿 ≥ 8"?
- **个人使用史**：你见过最糟 / 最佳的 NPS 实践案例是什么？是最糟被滥用（用于绩效考核员工导致刷分），还是最佳被用来真正诊断客户流失？
