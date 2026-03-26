---
name: notes-assistant
description: AI-driven Obsidian knowledge management assistant using PARA + Zettelkasten methodology. Helps create and manage daily notes, project docs, meeting notes, knowledge cards, code snippets, tech decision records, problem-solving records, weekly/monthly reviews, and task management. Handles Feishu (Lark) sync decisions and operations via MCP. Use this skill whenever the user mentions 笔记, 记录, 日常, 日记, 知识管理, 任务, 待办, todo, 会议, 项目, 归档, 回顾, 总结, 飞书同步, 知识卡片, 代码片段, 技术决策, 问题解决, PARA, Zettelkasten, daily note, weekly review, monthly review, or wants to organize notes in Obsidian — even if they don't explicitly say "notes assistant".
---

# Notes Assistant

AI-driven Obsidian knowledge management using PARA + Zettelkasten. You operate directly on the user's Obsidian vault — reading, creating, and editing Markdown files. No scripts or middleware needed.

## Core Principles

1. **Conversation-driven**: Users describe what they want in natural language; you figure out the intent, pick the right template, and create/edit files directly.
2. **Smart defaults**: Auto-detect content type, storage path, and tags from context. Ask only when genuinely uncertain.
3. **PARA structure**: Projects / Areas / Resources / Archives — everything has a home.
4. **Zettelkasten knowledge**: Atomic knowledge cards with bidirectional links form a growing knowledge network.
5. **Feishu sync awareness**: Automatically judge whether content is work-related and needs syncing. See `references/sync-rules.md` for the full decision logic.

## Vault Structure

```
Vault/
├── 0-Daily/              # Daily notes (YYYY/MM/YYYY-MM-DD.md)
│   ├── YYYY/MM/          # Daily notes by year/month
│   ├── Weekly-Reviews/   # or YYYY/Week-WW.md
│   └── Monthly-Reviews/  # or YYYY/YYYY-MM-Review.md
├── 1-Projects/           # Active projects
│   ├── Work/             # Work projects
│   │   └── {项目名}/
│   │       ├── 0-总览.md     # Project overview (index page)
│   │       ├── 1-任务.md     # Task list (single source of truth)
│   │       └── *.md          # Meeting notes, design docs, etc.
│   └── Personal/         # Personal projects
│       └── {项目名}/
│           ├── 0-总览.md
│           ├── 1-任务.md
│           └── *.md
├── 2-Areas/              # Ongoing responsibilities
│   ├── Work/             # Tech management, team collaboration
│   └── Life/             # Health, finance, family
├── 3-Resources/          # Reference knowledge
│   └── Tech/
│       ├── 知识卡片/
│       ├── 代码片段/
│       ├── 技术决策/
│       └── 问题解决/
├── 4-Archives/           # Completed projects (by year)
├── Attachments/          # Images, PDFs, etc.
└── Templates/            # Note templates
```

## Intent Recognition

When the user sends a message, identify the intent from keywords and context:

| Intent | Keywords | Action |
|--------|----------|--------|
| Daily note | 记录、今天、日常、工作、学习、生活、笔记 | Create/append daily note |
| Project | 项目、新项目、project | Create project folder + README |
| Meeting | 会议、开会、讨论、meeting | Create meeting note |
| Knowledge card | 知识卡片、知识点、概念、原理 | Create knowledge card |
| Code snippet | 代码、snippet、代码片段 | Create code snippet |
| Tech decision | 技术决策、架构决策 | Create tech decision record |
| Problem solving | 问题、解决、bug、错误 | Create problem-solving record |
| Task | 添加任务、待办、todo、任务 | Create/update/query tasks |
| Feishu sync | 同步、飞书、feishu | Trigger sync (see references/sync-rules.md) |
| Review | 回顾、总结、review | Generate weekly/monthly review |
| Archive | 归档、archive | Archive completed project |
| Search | 查找、搜索、查询 | Search vault content |
| Improvement | 记住、偏好、以后、习惯 | Record user preference (see references/improvements.md) |

## Note Creation Rules

For each note type, determine the path and apply the corresponding template from `references/templates.md`.

### Paths by Type

| Type | Path Pattern |
|------|-------------|
| Daily note | `0-Daily/YYYY/MM/YYYY-MM-DD.md` |
| Project (work) | `1-Projects/Work/{name}/0-总览.md` + `1-Projects/Work/{name}/1-任务.md` |
| Project (personal) | `1-Projects/Personal/{name}/0-总览.md` + `1-Projects/Personal/{name}/1-任务.md` |
| Meeting | `0-Daily/YYYY/MM/YYYY-MM-DD-{title}.md` |
| 知识卡片 | `3-Resources/Tech/知识卡片/{title}.md` |
| 代码片段 | `3-Resources/Tech/代码片段/{title}.md` |
| 技术决策 | `3-Resources/Tech/技术决策/{NNNN}-{title}.md` |
| 问题解决 | `3-Resources/Tech/问题解决/{title}.md` |
| Weekly review | `0-Daily/YYYY/Week-WW.md` |
| Monthly review | `0-Daily/YYYY/YYYY-MM-Review.md` |

### Key Behaviors

- **Daily note exists?** Append to the relevant section (工作/学习/生活) instead of creating a new file.
- **Daily note navigation**: Fill `prev` and `next` links pointing to adjacent dates.
- **Auto-tagging**: Add `#project/{name}` for project content, `#area/{name}` for area content.
- **Templates**: Read `references/templates.md` for the full template of each note type. Fill in variables like `{{date}}`, `{{title}}`, etc.

## Task Management

Tasks are managed using the Obsidian Tasks plugin. Each project has a dedicated `1-任务.md` as the single source of truth for all tasks.

### Task Syntax
```markdown
- [ ] Task content [[1-Projects/Work/项目名/1-任务|↗️]] 📅 2026-03-20 ➕ 2026-03-14 #task/work #project/项目名 ^task-id
- [x] Completed task [[1-Projects/Work/项目名/1-任务|↗️]] ✅ 2026-03-14
```

Emoji meanings:
- `📅` due date
- `➕` created date
- `⏳` scheduled date
- `🛫` start date
- `✅` done date (auto-added on completion)
- `^task-id` block ID for embedding individual tasks
- `[[path/to/1-任务|↗️]]` backlink to the task's source file (placed after task description, before emoji dates)

### ↗️ Backlink Convention
Every task (both completed and uncompleted) must include a `[[path/to/1-任务|↗️]]` wikilink placed after the task description text and before the emoji dates. This serves as a compact backlink to the task's source file, replacing the verbose built-in `backlink` display.

Format: `- [ ] 任务描述 [[full/path/to/1-任务|↗️]] 🛫 ... 📅 ... ➕ ...`

Important: Project names (folder names, tags, wikilink paths) must NEVER contain `.` — Obsidian interprets `.` as file extensions in wikilinks and as sub-tag separators in tags. Always replace `.` with `-` (e.g., `平台更新v2-7` not `平台更新v2.7`). The `title` field in frontmatter can keep the original name with `.` for display purposes.

### Task Date Rules
- When user starts working on a task, add `🛫` start date
- When user completes a task, if no `🛫` start date exists, set it to the same date as `✅` done date
- This ensures every completed task has a start date, making daily note queries accurate for historical review
- Tasks live in `1-任务.md` inside each project folder (single source of truth)
- Other notes in the project can embed tasks using block references: `![[1-任务#^task-id]]`
- The project `0-总览.md` embeds the full task list: `![[1-任务]]`
- When referencing project task lists from outside the project folder (e.g. daily notes), use full paths with display aliases: `[[1-Projects/Work/麦钉项目/1-任务|麦钉项目任务清单]]`

### Task Types & Where to Put Them
1. **Project tasks** → `1-任务.md` in the project folder. Has a clear end goal.
2. **Area tasks** → In the corresponding Area note. Ongoing responsibilities, no end date.
3. **Temporary tasks** → In the daily note's relevant section (e.g. 🏠 生活 > 个人事项). Small, same-day or near-term tasks. Tag with `#task/personal` or `#task/work`, default due date is today.

### Daily Note Task Display
Daily notes use a single Tasks plugin query block in the `📋 任务` section. Temporary tasks (buy something, reply an email) go in the relevant daily note section (e.g. 🏠 生活 > 个人事项), with default due date set to the current day and `#task/personal` tag.

Daily note sections use emoji headers: `📋 任务`, `💼 工作`, `📖 学习`, `🏠 生活`.

The query block rules:
- Filter: tasks due before tomorrow, scheduled today, or created today
- Hide: created date, tags, backlink, edit button
- Group level 1 by `#task/work` → "💼 工作", `#task/personal` → "🏠 个人", else → "📌 其他"
- Group level 2 by `#project/` tag → "项目：{name} 📋" (with wikilink to project's 1-任务.md), else → "临时"

Wikilinks in daily notes should use full paths with display aliases, e.g. `[[1-Projects/Work/麦钉项目/1-任务|麦钉项目任务清单]]`.

```markdown
## 📋 任务
\`\`\`tasks
filter by function \
  const today = '{{date}}'; \
  const yesterday = '{{date_minus_1}}'; \
  const tomorrow = '{{date_plus_1}}'; \
  const due = task.due?.format('YYYY-MM-DD'); \
  const done = task.done?.format('YYYY-MM-DD'); \
  const created = task.created?.format('YYYY-MM-DD'); \
  const start = task.start?.format('YYYY-MM-DD'); \
  const isDone = task.isDone; \
  if (!isDone && due && due < tomorrow) return true; \
  if (!isDone && !due) return true; \
  if (done === today || done === yesterday) return true; \
  if (created === today) return true; \
  if (start === today) return true; \
  return false;
path does not include 4-Archives
tags include #task/
hide toolbar
hide created date
hide start date
hide done date
hide tags
hide backlink
hide edit button
hide task count
group by function task.tags.includes("#task/work") ? "💼 工作" : task.tags.includes("#task/personal") ? "🏠 个人" : "📌 其他"
group by function \
  const p=task.tags.find(t=>t.startsWith("#project/")),y=task.tags.find(t=>t.startsWith("#type/")),w=task.tags.includes("#task/work")?"Work":"Personal"; \
  return p?"📁 "+p.replace("#project/","")+" [[1-Projects/"+w+"/"+p.replace("#project/","")+"/1-任务|📋]]":y?"📂 "+y.replace("#type/","")+" [[2-Areas/Work/"+y.replace("#type/","")+"|📋]]":"📌 临时"
\`\`\`
```

### Task Classification Priority
1. `#task/personal` → Personal
2. `#task/work` → Work
3. `#task/project/{name}` or `#project/{name}` → Project
4. File in `1-Projects/` → Project (name from path)
5. File in `2-Areas/Work/` → Work
6. File in `2-Areas/Life/` → Personal
7. Default → Personal

### Task Center
When asked for task overview, scan all `.md` files for tasks and generate `任务中心.md` with:
- Statistics (total, completed, in-progress, today, this week, important/urgent)
- Today's tasks, this week's tasks, important/urgent tasks
- Grouped by: work tasks, project tasks (by project), personal tasks

## Knowledge Extraction

When analyzing notes, look for knowledge indicators:
- Keywords: 学习了、理解了、发现、总结、原理、最佳实践、技巧、经验
- Contains code blocks → likely technical content
- Structured lists → organized knowledge
- Length > 100 chars → substantive content

Suggest extracting valuable knowledge points into cards. Add backlinks between source note and card.

## Reviews

### Weekly Review
- Collect all daily notes from Monday–Sunday of that week
- Generate links to each day's note
- Sections: work summary, life summary, next week plan

### Monthly Review
- Collect all weekly reviews from that month
- Sections: work summary, life summary, statistics, next month plan

## Project Archiving

When archiving a project:
1. Move folder from `1-Projects/{Work|Personal}/{name}` to `4-Archives/YYYY/{name}`
2. Add `archived_date: YYYY-MM-DD` to `0-总览.md` front matter
3. Preserve all content, links, and tags unchanged

## Feishu Sync

Sync decisions and operations are detailed in `references/sync-rules.md`. The key idea:
- Work content (project tags, work area tags, meeting keywords) → auto-sync
- Private content (personal tags, life areas, sensitive info) → never sync
- Uncertain → ask the user

Use lark-mcp tools for actual Feishu API calls (tasks, docs, wiki). See `references/feishu-mcp.md` for connection setup, tool list, OAuth login, and troubleshooting.

## User Preferences & Self-Improvement

Track user corrections and preferences in `references/improvements.md`. When a user says things like "以后不要问我这个" or "记住我的偏好", record it. Apply recorded preferences in future interactions.

## Tag System

| Category | Format | Examples |
|----------|--------|---------|
| Topic | `#技术/子类` | `#技术/前端/React`, `#工作`, `#生活`, `#学习` |
| Status | `#状态` | `#进行中`, `#已完成`, `#待办` |
| Priority | `#优先级` | `#重要`, `#紧急` |
| Project | `#project/名称` | `#project/电商系统` |
| Area | `#area/名称` | `#area/技术管理`, `#area/健康` |
| Task type | `#task/类型` | `#task/work`, `#task/personal`, `#task/project/名称` |
| Sync | `#sync/目标` | `#sync/feishu`, `#synced/feishu`, `#sync-error/feishu` |

## Reference Files

Read these when you need detailed information:

- **`references/templates.md`** — Full templates for all 9 note types. Read when creating any note.
- **`references/sync-rules.md`** — Feishu sync decision logic, tag conventions, conflict handling, MCP usage. Read when handling sync-related requests.
- **`references/improvements.md`** — User preferences and improvement history. Read at the start of each conversation and when the user provides feedback about your behavior.
- **`references/user-guide.md`** — User-facing operation manual with examples. Read when the user asks how to use the system.
- **`references/feishu-mcp.md`** — lark-mcp connection setup, tool list, OAuth login, permissions, and troubleshooting. Read when calling Feishu APIs or debugging MCP issues.
