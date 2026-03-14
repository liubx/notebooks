---
inclusion: manual
---

# Notes Assistant - 飞书同步规则

本文件定义了 Obsidian 笔记与飞书平台之间的同步决策逻辑。通过 lark-mcp 工具与飞书 API 交互。

## 同步决策逻辑

当用户创建或修改笔记时，按以下规则判断是否需要同步到飞书：

### 高置信度 - 不同步（自动判断）

以下情况直接判定为私有内容，不同步：

1. 包含 `#private` 标签
2. 包含敏感关键词: 密码、账号、身份证、银行卡、工资、薪资、隐私、私密、个人信息、家庭住址
3. 文件位于 `1-Projects/Personal/` 路径下
4. 包含 `#task/personal` 标签
5. 包含生活领域标签 `#area/生活`、`#area/健康`、`#area/财务`、`#area/家庭`、`#area/个人`
6. 包含个人项目关键词: 个人项目、买房、装修、家庭

### 高置信度 - 需要同步（自动判断）

以下情况直接判定为工作内容，需要同步：

1. 包含 `#task/work` 标签
2. 包含工作项目标签 `#project/xxx`（排除个人项目关键词）
3. 包含工作领域标签 `#area/xxx`（排除生活领域关键词）
4. 包含技术决策关键词: 技术决策、TDR、架构决策、决策记录
5. 包含 ≥2 个工作关键词

### 工作关键词列表

会议、团队、协作、项目、需求、开发、测试、上线、部署、评审、汇报、周报、月报、技术方案、架构、设计文档、接口文档、客户、产品、运营、市场

### 需要询问用户的情况

- 同时包含学习关键词和工作关键词 → 询问
- 仅包含学习关键词（学习、学了、学到、笔记、总结、心得、读书、阅读、看了、了解了）→ 询问
- 仅包含 1 个工作关键词 → 询问
- 无明确特征 → 询问

询问模板: "这个内容是否需要同步到飞书？"

## 同步标签约定

| 标签 | 含义 |
|------|------|
| `#sync/feishu` | 待同步到飞书 |
| `#sync/feishu-task` | 待同步任务 |
| `#sync/feishu-doc` | 待同步文档 |
| `#sync/feishu-wiki` | 待同步 Wiki |
| `#synced/feishu` | 已同步 |
| `#sync-error/feishu` | 同步失败 |
| `#sync-conflict/feishu` | 同步冲突 |

## 任务同步

### 同步到飞书
将 Obsidian 任务同步为飞书任务时：
- 任务内容 → 飞书任务标题
- `📅 日期` → 飞书截止日期
- `@负责人` → 飞书负责人
- `#重要`/`#紧急` → 飞书高优先级
- 完成状态 → 飞书任务状态

### 同步元数据
同步成功后，在任务行下方添加元数据：
```markdown
- [ ] 任务内容 #sync/feishu
  - feishu_task_id: xxx
  - feishu_url: https://...
  - last_sync: 2025-03-14T10:00:00
  - sync_status: synced
```

## 文档同步

### 同步到飞书
将 Obsidian 文档同步为飞书文档时：
- 提取 YAML front matter 后的第一个标题作为文档标题
- 转换 Markdown 为飞书格式（标题、列表、代码块、表格、链接、图片）
- 本地图片需上传到飞书后替换 URL

### 文档同步元数据
在 YAML front matter 中记录：
```yaml
feishu_sync:
  platform: feishu
  doc_type: doc
  feishu_doc_id: "xxx"
  feishu_url: "https://..."
  feishu_folder: "folder_path"
  last_sync: 2025-03-14T10:00:00
  sync_status: synced
```

## 项目级同步配置

每个项目可以有独立的同步配置文件 `.feishu-sync.json`：

```json
{
  "project_name": "项目名称",
  "feishu_tasklist_id": "飞书任务清单ID",
  "feishu_tasklist_url": "飞书任务清单URL",
  "sync_enabled": true,
  "sync_mode": "bidirectional",
  "grouping_mode": "custom",
  "custom_groups": [
    {"name": "开发", "feishu_group_id": "xxx"},
    {"name": "测试", "feishu_group_id": "yyy"}
  ],
  "default_group": "未分组",
  "field_mapping": {
    "title": "任务标题",
    "description": "任务描述",
    "due_date": "截止日期",
    "assignee": "负责人",
    "priority": "优先级",
    "status": "状态"
  }
}
```

同步模式:
- `bidirectional` — 双向同步
- `obsidian_to_feishu` — 仅推送到飞书
- `feishu_to_obsidian` — 仅从飞书拉取

## 冲突处理

当检测到本地和飞书都有修改时：
1. 标记为 `#sync-conflict/feishu`
2. 提示用户选择保留哪个版本
3. 冲突类型: 任务状态冲突、任务内容冲突、文档内容冲突

## 同步中心

当用户要求查看同步状态时，扫描 vault 中所有同步标签，生成 `飞书同步中心.md`，包含：
- 📊 同步统计（总数、待同步、已同步、失败、冲突，按任务/文档分类）
- ⏳ 待同步列表
- ✅ 已同步列表
- ❌ 同步失败列表
- ⚠️ 同步冲突列表

## MCP 工具调用

通过 lark-mcp 与飞书交互。可用操作：
- 创建/更新/获取飞书任务
- 创建/更新/获取飞书文档
- 上传图片到飞书
- 创建任务清单和分组

调用失败时自动重试（最多 3 次，指数退避）。
