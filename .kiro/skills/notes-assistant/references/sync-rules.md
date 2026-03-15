# Feishu Sync Rules

Sync decision logic and operations for Obsidian ↔ Feishu integration via lark-mcp.

## Sync Decision Logic

When a user creates or modifies a note, determine whether it should sync to Feishu.

### Never Sync (Private Content)

Auto-classify as private — do not sync and do not ask:

1. Contains `#private` tag
2. Contains sensitive keywords: 密码, 账号, 身份证, 银行卡, 工资, 薪资, 隐私, 私密, 个人信息, 家庭住址
3. File is under `1-Projects/Personal/`
4. Contains `#task/personal` tag
5. Contains life-area tags: `#area/生活`, `#area/健康`, `#area/财务`, `#area/家庭`, `#area/个人`
6. Contains personal project keywords: 个人项目, 买房, 装修, 家庭

### Auto Sync (Work Content)

Auto-classify as work content — sync without asking:

1. Contains `#task/work` tag
2. Contains work project tag `#project/xxx` (excluding personal project keywords)
3. Contains work area tag `#area/xxx` (excluding life area keywords)
4. Contains tech decision keywords: 技术决策, 架构决策, 决策记录
5. Contains ≥2 work keywords (see list below)

### Work Keywords

会议, 团队, 协作, 项目, 需求, 开发, 测试, 上线, 部署, 评审, 汇报, 周报, 月报, 技术方案, 架构, 设计文档, 接口文档, 客户, 产品, 运营, 市场

### Ask the User

When none of the above rules match clearly:

- Mixed learning + work keywords → ask
- Only learning keywords (学习, 学了, 笔记, 总结, 心得, 读书, 阅读) → ask
- Only 1 work keyword → ask
- No clear indicators → ask

Prompt: "这个内容是否需要同步到飞书？"

## Sync Tags

| Tag | Meaning |
|-----|---------|
| `#sync/feishu` | Pending sync to Feishu (general) |
| `#sync/feishu-task` | Pending task sync |
| `#sync/feishu-doc` | Pending document sync |
| `#sync/feishu-wiki` | Pending wiki sync |
| `#synced/feishu` | Successfully synced |
| `#sync-error/feishu` | Sync failed |
| `#sync-conflict/feishu` | Sync conflict detected |
| `#private` | Private, never sync |

## Task Sync

### Obsidian → Feishu

Map Obsidian task fields to Feishu task:
- Task content → Feishu task title
- `📅 date` → Due date
- `@assignee` → Assignee
- `#重要` / `#紧急` → High priority
- Checkbox state → Completion status

### Sync Metadata

After successful sync, add metadata below the task line:
```markdown
- [ ] Task content #sync/feishu
  - feishu_task_id: xxx
  - feishu_url: https://...
  - last_sync: 2025-03-14T10:00:00
  - sync_status: synced
```

Update the tag from `#sync/feishu` to `#synced/feishu`.

## Document Sync

### Obsidian → Feishu

When syncing a document:
- Extract first heading after YAML front matter as document title
- Convert Markdown to Feishu format (headings, lists, code blocks, tables, links, images)
- Upload local images to Feishu and replace URLs
- Convert `[[wikilinks]]` to Feishu doc links (if target is also synced)
- Convert `#tags` to Feishu tags
- Convert `@mentions` to Feishu @mentions

### Document Sync Metadata

Store in YAML front matter:
```yaml
feishu_sync:
  platform: feishu
  doc_type: doc  # doc / wiki / sheet
  feishu_doc_id: "xxx"
  feishu_url: "https://..."
  feishu_folder: "folder_path"
  sync_mode: bidirectional  # bidirectional / obsidian_to_feishu / feishu_to_obsidian
  auto_sync: true
  last_sync: 2025-03-14T10:00:00
  sync_status: synced
```

## Project-Level Sync Config

Each project can have a `.feishu-sync.json` in its folder:

```json
{
  "project_name": "ProjectName",
  "feishu_tasklist_id": "tasklist_xxx",
  "feishu_tasklist_url": "https://...",
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

Sync modes:
- `bidirectional` — Two-way sync
- `obsidian_to_feishu` — Push only
- `feishu_to_obsidian` — Pull only

## Conflict Handling

When both Obsidian and Feishu have been modified since last sync:
1. Mark with `#sync-conflict/feishu`
2. Show the user both versions with timestamps
3. Ask user to choose: keep Obsidian version / keep Feishu version / manual merge
4. Pause auto-sync for conflicted items until resolved

## Sync Center

When asked for sync status, scan all sync tags in the vault and generate `飞书同步中心.md`:
- 📊 Statistics (total, pending, synced, failed, conflicts — by task/doc)
- ⏳ Pending sync list
- ✅ Synced list
- ❌ Failed list
- ⚠️ Conflict list

## MCP Tool Usage

Use lark-mcp for all Feishu API interactions:
- Create / update / get tasks
- Create / update / get documents
- Upload images
- Create task lists and groups

On failure, retry up to 3 times with exponential backoff. If MCP is unavailable, mark items as pending sync and inform the user.

## Error Handling

- **Network error**: Retry with backoff, mark as `#sync-error/feishu` if all retries fail
- **Auth error**: Inform user to check MCP config (app_id, app_secret)
- **Rate limit**: Wait and retry automatically
- **MCP unavailable**: Mark as pending, inform user
