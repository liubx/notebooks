---
inclusion: manual
---

# 飞书任务清单同步规则

## 分组映射

本地任务文件中的 `# 标题` 与飞书清单的 section 一一对应，通过 HTML 注释标记关联：

```markdown
# 分组名称
<!-- feishu_section: section-guid -->
```

### 分组类型

| 类型 | 说明 | 示例 |
|------|------|------|
| 飞书同步分组 | 有 `feishu_section` 注释，与飞书 section 对应 | `# BUG 修复`、`# 围栏功能` |
| 纯本地分组 | 无 `feishu_section` 注释，不参与同步 | `# 今日重点`、`# v2.7 上线` |
| 默认分组 | 注释中标注 `(默认分组)`，对应飞书清单的默认 section | `# 默认分组` |

### 规则

1. 飞书清单中每个自定义 section → 本地一个 `# 标题` + `feishu_section` 注释
2. 飞书默认分组 → 本地 `# 默认分组`，没有归入任何自定义 section 的任务放这里
3. 本地可以有不带 `feishu_section` 的纯本地分组，同步时跳过
4. 同步时根据任务的 `tasklists[].section_guid` 确定归属分组
5. 如果飞书新增了 section，本地也要新增对应的 `# 标题`
6. 分组顺序：纯本地分组在前，飞书同步分组在后，默认分组放最后

## 任务格式

```markdown
- [ ] 任务标题 [](飞书链接) 👤负责人 🛫 YYYY-MM-DD 📅 YYYY-MM-DD 优先级 #task/work #project/项目名 ^block-id
  可选的补充说明
```

### Tag 规则

- 所有飞书同步的工作任务必须带 `#task/work` tag（确保出现在日记任务查询中）
- 如果任务文件的 frontmatter 有 `project/xxx` tag，任务行也要带对应的 `#project/xxx`
- 如果任务文件属于 `2-Areas/Work/`（综合任务），用 `#type/xxx` 代替 `#project/xxx`

### 字段说明

| 字段 | 来源 | 说明 |
|------|------|------|
| 👤负责人 | members 中 role=assignee | 通过 open_id 查公司人员表转姓名 |
| 🛫 开始日期 | start.timestamp | 仅在飞书有设置开始时间时显示 |
| 📅 截止日期 | due.timestamp | 仅在飞书有设置截止日期时显示 |
| 优先级 | custom_fields 优先级 | ⏫ 紧急 / 🔼 高 / 🔽 低，无优先级字段则不显示 |
| [🔗] | task.url | 飞书任务详情链接 |
| ^block-id | 本地自定义 | Obsidian block reference，用于 wikilink 引用 |
| 补充说明 | task.description | 缩进两空格，简要摘录 |

## 权限与分组调整

飞书任务 API 只能操作调用者有权限的任务（创建者或成员）。

### 用户信息

- open_id: `ou_9be76f17d1adc319030bc8d0b883174e`（用于临时加入任务获取权限）

### 分组调整流程

需要移动任务到其他 section 时，按以下步骤操作：

1. 获取任务详情，检查 members 中是否包含用户（open_id）
2. 如果用户不在成员列表中：
   - 调用 `addMembers` 将用户加为 follower（临时获取权限）
   - 如果 addMembers 失败 → 跳过飞书端操作，只在本地文件归类，提示用户手动处理
3. 执行 `addTasklist`（加入目标 section）
4. 如果步骤 2 中临时加入了用户，调用 `removeMembers` 将用户移除
5. **绝对不要先 removeTasklist 再 addTasklist**，避免 add 失败导致任务脱离清单

### 降级策略

如果飞书端操作失败，在本地文件中正常归类，并在文件末尾用 callout 提示：

```markdown
> [!info] 飞书清单同步说明
> 以下任务因权限限制无法通过 API 操作，需在飞书客户端手动处理。
> 涉及任务：...
```

## 同步流程

1. 读取本地任务文件，提取已有任务的 guid（从飞书链接中解析）
2. 调用飞书 API 获取清单中所有未完成任务
3. 对比差异：
   - 飞书有、本地无 → 新增到对应分组
   - 飞书已完成、本地未勾选 → 标记为完成
   - 飞书分组变更 → 按「分组调整流程」操作飞书端，同时更新本地文件
4. 纯本地任务（无飞书链接）不受影响
5. 更新 frontmatter 中的 `modified` 日期
