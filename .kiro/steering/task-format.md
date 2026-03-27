---
inclusion: always
---

# 任务格式规范

## 统一任务行格式

有外部链接（飞书/文章/任何 URL）：
```
- [ ] [任务标题](外部链接) [[路径#^id|↗️]] 👤负责人 🛫 开始 📅 截止 ➕ 创建 优先级 #tags ^task-id
```

没有外部链接：
```
- [ ] 任务标题 [[路径#^id|↗️]] 👤负责人 🛫 开始 📅 截止 ➕ 创建 优先级 #tags ^task-id
```

## 字段说明

| 字段 | 格式 | 必填 | 说明 |
|------|------|------|------|
| 标题 | 纯文本或 `[标题](url)` | ✅ | 有外部链接时做成超链接 |
| ↗️ backlink | `[[路径#^task-id\|↗️]]` | ✅ | 精确定位到任务行 |
| 👤负责人 | `👤姓名` | 可选 | 飞书同步的任务带负责人 |
| 🛫 开始日期 | `🛫 YYYY-MM-DD` | 可选 | 任务开始时间 |
| 📅 截止日期 | `📅 YYYY-MM-DD` | 可选 | 任务截止时间 |
| ➕ 创建日期 | `➕ YYYY-MM-DD` | 可选 | 任务创建时间 |
| ✅ 完成日期 | `✅ YYYY-MM-DD` | 自动 | 完成时自动添加 |
| 优先级 | 🔺高 🔼中 🔽低 | 可选 | Tasks 插件原生优先级 |
| #tags | `#task/类型 #project/名称` | ✅ | 任务分类和项目归属 |
| ^task-id | `^task-xxx` | ✅ | block reference ID |

## 任务类型 Tag

- `#task/work` — 工作任务
- `#task/study` — 学习任务
- `#task/personal` — 个人任务

## 状态 Tag（与飞书自定义字段同步）

- 无 status tag — 默认状态（收集箱）
- `#status/doing` — 进行中
- `#status/testing` — 测试中
- `#status/waiting` — 等待中
- `#status/done` — 已完成
- `#status/cancelled` — 已取消

## 任务补充信息

用缩进子列表补充详情，Tasks 插件不会解析缩进行：

```markdown
- [ ] 写接口文档 📅 2026-03-28 #task/work #project/xxx ^task-api-doc
  - 用户认证接口
  - 数据查询接口
  - 参考：https://example.com/api-spec
```

## 字段顺序

标题 → 外部链接（如有）→ ↗️ backlink → 👤负责人 → 🛫 → 📅 → ➕ → 优先级 → #tags → ^task-id
