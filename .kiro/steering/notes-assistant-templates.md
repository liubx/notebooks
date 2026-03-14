---
inclusion: manual
---

# Notes Assistant - 笔记模板

创建笔记时，使用以下模板。将 `{{变量}}` 替换为实际值。

## 日常笔记模板 (daily-note)

```markdown
---
date: {{date}}
day_of_week: {{day_of_week}}
tags:
  - daily
prev: "[[{{prev_date}}]]"
next: "[[{{next_date}}]]"
---

# {{date}} {{day_of_week}}

## 工作板块

### 今日任务
- [ ] 

### 会议记录

### 工作进展

### 问题记录

## 学习板块

### 学习内容

### 技术笔记

### 阅读记录

## 生活板块

### 个人事项

### 健康记录

### 心情感悟
```

变量说明:
- `date`: 日期 YYYY-MM-DD
- `day_of_week`: 星期几（周一~周日）
- `prev_date`: 前一天日期
- `next_date`: 后一天日期

## 项目模板 (project)

```markdown
---
title: {{title}}
type: project
category: {{category}}
status: 进行中
start_date: {{start_date}}
due_date: {{due_date}}
tags:
  - project/{{project_name}}
created: {{created}}
modified: {{modified}}
---

# {{title}}

## 项目概述

**项目目标**: 

**项目类型**: {{category}}

**时间线**:
- 开始日期: {{start_date}}
- 截止日期: {{due_date}}

## 里程碑

- [ ] 里程碑 1
- [ ] 里程碑 2
- [ ] 里程碑 3

## 任务列表

### 待办任务
- [ ] 

### 进行中
- [ ] 

### 已完成
- [x] 

## 相关资源

- 

## 项目日志

### {{created}}
- 项目创建
```

变量说明:
- `title`: 项目标题
- `category`: work 或 personal
- `start_date` / `due_date`: YYYY-MM-DD
- `project_name`: 项目名（用于标签和文件夹名）
- `created` / `modified`: YYYY-MM-DD

## 会议记录模板 (meeting)

```markdown
---
title: {{title}}
type: meeting
date: {{date}}
time: {{time}}
tags:
  - meeting
  - {{project_tag}}
created: {{created}}
---

# {{title}}

**会议时间**: {{date}} {{time}}

**参与者**: {{participants}}

## 会议议题

1. 

## 讨论内容

### 议题 1

### 议题 2

## 决策事项

- [ ] 

## 行动项

- [ ] {{action_item}} 📅 {{due_date}} @{{assignee}}

## 下次会议

**时间**: 
**议题**: 
```

## 知识卡片模板 (knowledge-card)

```markdown
---
title: {{title}}
type: knowledge-card
tags:
  - {{main_tag}}
created: {{created}}
source: "[[{{source}}]]"
related:
  - 
---

# {{title}}

## 核心概念

## 详细说明

## 示例

## 相关知识

- 

## 参考资料

- 
```

## 代码片段模板 (code-snippet)

```markdown
---
title: {{title}}
type: code-snippet
language: {{language}}
tags:
  - code-snippet
  - {{language_tag}}
created: {{created}}
---

# {{title}}

**语言**: {{language}}

## 使用场景

## 代码

​```{{language}}
{{code}}
​```

## 说明

## 相关链接

- 
```

## 技术决策记录模板 (tech-decision-record)

```markdown
---
title: {{title}}
type: tech-decision-record
number: {{number}}
status: {{status}}
date: {{date}}
tags:
  - tech-decision-record
  - 技术/架构
created: {{created}}
---

# TDR-{{number}}: {{title}}

**状态**: {{status}}

**日期**: {{date}}

## 背景

描述需要做出决策的背景和问题。

## 决策内容

描述我们决定采用的方案。

## 后果

### 正面影响

### 负面影响

### 风险

## 替代方案

### 方案 1

### 方案 2

## 相关决策

- 
```

状态值: 提议 / 已接受 / 已废弃

## 问题解决模板 (problem-solving)

```markdown
---
title: {{title}}
type: problem-solving
tags:
  - problem-solving
  - {{tech_tag}}
created: {{created}}
---

# {{title}}

## 问题描述

## 问题环境

- 操作系统: 
- 软件版本: 
- 相关配置: 

## 错误信息

​```
{{error_message}}
​```

## 解决方案

## 根本原因

## 相关资源

- 
```

## 周回顾模板 (weekly-review)

```markdown
---
title: {{title}}
type: weekly-review
week: {{week}}
year: {{year}}
date_range: {{date_range}}
tags:
  - review
  - weekly
created: {{created}}
---

# {{title}}

**周次**: {{year}}-W{{week}}

**日期范围**: {{date_range}}

## 工作总结

### 本周完成项目

### 技术学习

### 工作反思

## 生活总结

### 个人事项

### 健康状况

### 生活感悟

## 本周日常笔记

{{daily_notes_links}}

## 下周计划

### 工作计划

### 个人计划
```

变量说明:
- `title`: 如 "2025-W11 周回顾"
- `week`: ISO 周数 (01-53)
- `year`: 年份
- `date_range`: 如 "2025-03-10 ~ 2025-03-16"
- `daily_notes_links`: 自动生成的日常笔记 wikilink 列表

## 月回顾模板 (monthly-review)

```markdown
---
title: {{title}}
type: monthly-review
month: {{month}}
year: {{year}}
tags:
  - review
  - monthly
created: {{created}}
---

# {{title}}

**年月**: {{year}}-{{month}}

## 工作总结

### 本月目标达成

### 重要项目

### 技术成长

## 生活总结

### 个人目标

### 重要事件

### 下月计划

## 本月周回顾

{{weekly_reviews_links}}

## 数据统计

- 完成任务数: 
- 创建笔记数: 
- 学习时长: 
```

变量说明:
- `title`: 如 "2025-03 月回顾"
- `month`: 月份 (01-12)
- `weekly_reviews_links`: 自动生成的周回顾 wikilink 列表
