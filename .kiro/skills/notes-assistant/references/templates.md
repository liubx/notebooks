# Note Templates

All templates for the notes-assistant skill. Replace `{{variable}}` with actual values when creating notes.

## Table of Contents
1. [Daily Note](#daily-note)
2. [Project](#project)
3. [Meeting](#meeting)
4. [Knowledge Card](#knowledge-card)
5. [Code Snippet](#code-snippet)
6. [Tech Decision Record](#tech-decision-record)
7. [Problem Solving](#problem-solving)
8. [Weekly Review](#weekly-review)
9. [Monthly Review](#monthly-review)

---

## Daily Note

Path: `0-Daily/YYYY/MM/YYYY-MM-DD.md`

Variables:
- `date`: YYYY-MM-DD
- `day_of_week`: 星期一~星期日
- `prev_date` / `next_date`: Adjacent dates

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

## 💼 工作

### 任务清单
\`\`\`tasks
filter by function \
  const t=moment("{{date}}"),d='day',{due:{moment:u},start:{moment:s},created:{moment:c},done:{moment:D}}=task,y=moment(t).subtract(1,d),b=m=>m?.isSameOrBefore(t,d),q=m=>m?.isSame(t,d); \
  return !!(!task.isDone?!u||b(u)||b(s)||q(c):q(D)||D?.isSame(y,d));
path does not include 4-Archives
tags include #task/work
hide toolbar
hide task count
hide created date
hide start date
hide done date
hide tags
hide backlink
hide edit button
hide postpone button
sort by priority
sort by due
sort by start
group by function \
  const p=task.tags.find(t=>t.startsWith("#project/")),y=task.tags.find(t=>t.startsWith("#type/")); \
  return p?"📁 "+p.replace("#project/","")+" [[1-Projects/Work/"+p.replace("#project/","")+"/1-任务|📋]]":y?"📂 "+y.replace("#type/","")+" [[2-Areas/Work/"+y.replace("#type/","")+"|📋]]":"📌 临时"
group by function task.heading?"📂 "+task.heading:""
\`\`\`

### 工作进展

### 会议记录

### 问题记录

## 📖 学习

### 任务清单
\`\`\`tasks
filter by function \
  const t=moment("{{date}}"),d='day',{due:{moment:u},start:{moment:s},created:{moment:c},done:{moment:D}}=task,y=moment(t).subtract(1,d),b=m=>m?.isSameOrBefore(t,d),q=m=>m?.isSame(t,d); \
  return !!(!task.isDone?!u||b(u)||b(s)||q(c):q(D)||D?.isSame(y,d));
path does not include 4-Archives
tags include #task/study
hide toolbar
hide task count
hide created date
hide start date
hide done date
hide tags
hide backlink
hide edit button
hide postpone button
sort by priority
sort by due
sort by start
group by function \
  const p=task.tags.find(t=>t.startsWith("#project/")); \
  return p?"📁 "+p.replace("#project/","")+" [[1-Projects/Personal/"+p.replace("#project/","")+"/1-任务|📋]]":"📌 临时"
group by function task.heading?"📂 "+task.heading:""
\`\`\`

### 学习内容

### 技术笔记

### 阅读记录

## 🏠 个人

### 任务清单
\`\`\`tasks
filter by function \
  const t=moment("{{date}}"),d='day',{due:{moment:u},start:{moment:s},created:{moment:c},done:{moment:D}}=task,y=moment(t).subtract(1,d),b=m=>m?.isSameOrBefore(t,d),q=m=>m?.isSame(t,d); \
  return !!(!task.isDone?!u||b(u)||b(s)||q(c):q(D)||D?.isSame(y,d));
path does not include 4-Archives
tags include #task/personal
hide toolbar
hide task count
hide created date
hide start date
hide done date
hide tags
hide backlink
hide edit button
hide postpone button
sort by priority
sort by due
sort by start
group by function \
  const p=task.tags.find(t=>t.startsWith("#project/")); \
  return p?"📁 "+p.replace("#project/","")+" [[1-Projects/Personal/"+p.replace("#project/","")+"/1-任务|📋]]":"📌 临时"
group by function task.heading?"📂 "+task.heading:""
\`\`\`

### 个人事项

### 健康记录

### 心情感悟
```

---

## Project

A project consists of two core files in a folder: `0-总览.md` (overview/index) and `1-任务.md` (task list). Other notes (meetings, designs, etc.) go in the same folder. No `#` level-1 header in files — Obsidian uses the filename as title.

### Project Overview

Path: `1-Projects/{Work|Personal}/{project_name}/0-总览.md`

Variables:
- `title`: Project title
- `category`: work or personal
- `start_date` / `due_date`: YYYY-MM-DD
- `project_name`: For tags and folder name
- `created` / `modified`: YYYY-MM-DD

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

# 项目概述

**项目目标**: 

**项目类型**: {{category}}

**时间线**:
- 开始日期: {{start_date}}
- 截止日期: {{due_date}}

# 任务总览

\`\`\`tasks
filter by function \
  const d='day',{done:{moment:D}}=task; \
  return !task.isDone||D?.isAfter(moment().subtract(7,d),d)||false;
path includes 1-Projects/{{Work|Personal}}/{{project_name}}
tags include #task/
hide toolbar
hide task count
hide created date
hide start date
hide done date
hide tags
hide backlink
hide edit button
group by function task.isDone ? "✅ 已完成" : "📋 进行中"
\`\`\`

# 相关笔记

# 项目日志

## {{created}}
- 项目创建
```

### Project Task List

Path: `1-Projects/{Work|Personal}/{project_name}/1-任务.md`

Variables:
- `title`: Project title
- `project_name`: For tags
- `created` / `modified`: YYYY-MM-DD

Tasks should include: a ↗️ backlink wikilink, due date (📅), created date (➕), tags (#task/work or #task/personal, #project/名称), and a block ID (^task-id) for embedding.

```markdown
---
title: {{title}}-任务
type: task-list
tags:
  - project/{{project_name}}
created: {{created}}
modified: {{modified}}
---

# {{section_name}}
- [ ] {{task_content}} [[1-Projects/{{Work|Personal}}/{{project_name}}/1-任务|↗️]] 📅 {{due_date}} ➕ {{created}} #task/{{category}} #project/{{project_name}} ^{{task_id}}
```

Other notes in the project can embed individual tasks:
```markdown
![[1-任务#^task-id]]
```

---

## Meeting

Path: `0-Daily/YYYY/MM/YYYY-MM-DD-{title}.md`

Variables:
- `title`: Meeting title
- `date` / `time`: Date and time
- `participants`: Comma-separated names
- `project_tag`: Related project tag (if any)
- `created`: YYYY-MM-DD

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

## 决策事项

## 行动项

- [ ] {{action_item}} 📅 {{due_date}} @{{assignee}}

## 下次会议

**时间**: 
**议题**: 
```

---

## Knowledge Card

Path: `3-Resources/Tech/知识卡片/{title}.md`

Variables:
- `title`: Descriptive title (e.g., "React Hooks 闭包陷阱")
- `main_tag`: Primary tech tag (e.g., `技术/前端/React`)
- `created`: YYYY-MM-DD
- `source`: Source note wikilink

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

## 参考资料
```

---

## Code Snippet

Path: `3-Resources/Tech/代码片段/{title}.md`

Variables:
- `title`: Descriptive title
- `language`: Programming language
- `language_tag`: Tag like `技术/Python`
- `created`: YYYY-MM-DD

````markdown
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

```{{language}}
{{code}}
```

## 说明

## 相关链接
````

---

## Tech Decision Record

Path: `3-Resources/Tech/技术决策/{NNNN}-{title}.md`

Variables:
- `title`: Decision title
- `number`: Sequential number (0001, 0002, ...)
- `status`: 提议 / 已接受 / 已废弃
- `date` / `created`: YYYY-MM-DD

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

# {{number}}-{{title}}

**状态**: {{status}}

**日期**: {{date}}

## 背景

## 决策内容

## 后果

### 正面影响

### 负面影响

### 风险

## 替代方案

### 方案 1

### 方案 2

## 相关决策
```

---

## Problem Solving

Path: `3-Resources/Tech/问题解决/{title}.md`

Variables:
- `title`: Problem description
- `tech_tag`: Related tech tag
- `created`: YYYY-MM-DD

````markdown
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

```
{{error_message}}
```

## 解决方案

## 根本原因

## 相关资源
````

---

## Weekly Review

Path: `0-Daily/YYYY/Week-WW.md`

Variables:
- `title`: e.g., "2025-W11 周回顾"
- `week`: ISO week number (01-53)
- `year`: Year
- `date_range`: e.g., "2025-03-10 ~ 2025-03-16"
- `daily_notes_links`: Auto-generated wikilink list for each day
- `created`: YYYY-MM-DD

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

---

## Monthly Review

Path: `0-Daily/YYYY/YYYY-MM-Review.md`

Variables:
- `title`: e.g., "2025-03 月回顾"
- `month`: Month (01-12)
- `year`: Year
- `weekly_reviews_links`: Auto-generated wikilink list
- `created`: YYYY-MM-DD

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
