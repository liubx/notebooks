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

参考 `task-format.md` steering 规则。飞书同步任务的标题做成超链接：

```markdown
- [ ] [任务标题](飞书链接) [[文件路径#^task-id|↗️]] 👤负责人 🛫 YYYY-MM-DD 📅 YYYY-MM-DD 优先级 #task/work #project/项目名 ^task-id
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

1. 获取飞书清单的所有分组（section_list）
2. 按分组逐个获取未完成任务（section_tasks，completed=false），确保分组归属正确
3. 读取本地任务文件，提取已有任务的 guid（从飞书链接中解析）
4. 对比差异：
   - 飞书有、本地无 → 新增到对应分组
   - 飞书已完成、本地未勾选 → 标记为完成
   - 飞书分组变更 → 按「分组调整流程」操作飞书端，同时更新本地文件
5. 纯本地任务（无飞书链接）不受影响
6. 更新 frontmatter 中的 `modified` 日期

### 分组同步规则

- 只同步有未完成任务的分组，空分组不在本地创建
- 分组名必须与飞书任务清单里的分组名称保持一致，不自行命名
- 如果飞书分组名变更，本地也要同步更新

### 用户 ID 映射规则

- 遇到未知的用户 ID，必须先调用 `contact_v3_user_get` 查询真实姓名，不得猜测
- 已知映射缓存在下方表格中，新查到的映射要追加

### 已知用户 ID 映射

| open_id | 姓名 |
|---------|------|
| ou_9be76f17d1adc319030bc8d0b883174e | 刘秉欣 |
| ou_105edcafa5829da753622165782e03ec | 陆东 |
| ou_a6a57cc5a5b68f1cc1de9303fde95b9e | 姚文羚 |
| ou_133d6b2efd74de1c18e78c31982e3682 | 闫云江 |
| ou_5e48e13751c35f6259c4a466b0aa2c2d | 钟申炜 |
| ou_84805b2c6cc34a5c91cdb5230df5f5aa | 王鹏 |
| ou_c46553a9025efc0bdd0a9ebd095ff753 | 杨嵘 |
| ou_d8753db08d55d6d3281f66f9f38d57d9 | 马工 |
| ou_aed93030c2cf59d0e67dc94d462f4242 | 杨嵘(设计) |
| ou_d7c6010202b1e198bd3f8c236da29c73 | 伍峥 |
| ou_b8d3d51fa3d5b6e1200347b625521c58 | 财务 |
| ou_c7e1e347a7461614127f677249cedb17 | 李工 |
| ou_de5641e7821fa86d456a3a7e8d48810f | 韩晓龙 |
| ou_950e3fbd4f3b31d0d662e2107179a2bb | 闫云江(前端) |
| ou_c745ac63bf3f9874d86ae330114eeb9a | 王工(上港) |
| ou_430cf085e4a3f107a2d7bf5b1d0555e8 | 马工(洛阳) |
