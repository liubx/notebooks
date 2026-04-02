# Bingxin's Vault 与 Yiyan's Vault 对比

两个 vault 从同一个基础分叉，共享 PARA + Zettelkasten 方法论和 Obsidian Tasks 插件体系，但针对不同使用场景做了差异化。

## 基本信息

| | Bingxin's Vault | Yiyan's Vault |
|---|---|---|
| 用途 | 个人工作+学习+生活 | 小孩成长记录+学习管理 |
| 路径 | `~/...Documents/Bingxin's Vault` | `~/...Documents/Yiyan's Vault` |
| 分叉点 | `b5d77c7` 整理孩子成长笔记 | 同左 |

## 目录结构差异

| 目录 | Bingxin | Yiyan |
|------|---------|-------|
| `1-Projects/` | `Work/` + `Personal/` | `Study/` + `Life/` |
| `2-Areas/` | `Work/` + `Life/` | `Life/` + `Study/`（多了学习领域） |
| `3-Resources/` | `Tech/`（知识卡片/代码片段/技术决策） | `Knowledge/` |
| 根目录特殊文件 | `任务总览.md` | `欢迎.md` + `任务总览.md` + `积分总表.md` |

## 任务体系差异

| | Bingxin | Yiyan |
|---|---|---|
| 任务类型 tag | `#task/work` `#task/study` `#task/personal` | `#task/study` `#task/life` |
| 额外 tag | `#type/xxx`（综合任务分类）`#status/xxx` | `#type/homework` `#type/daily` `#subject/数学` 等 |
| 日记任务布局 | 三栏：💼 工作 / 📖 学习 / 🏠 个人 | 两栏：📖 学习 / 🏠 生活 |
| 日记任务过滤 | 截止日期≤今天 或 开始日期≤今天 或 创建日期=今天 | 开始日期≤今天≤截止日期（严格范围内） |
| 任务分组 | 按 `#project/` → 项目名，`#type/` → 综合分类 | 按 `#project/` → 项目名 |
| 飞书同步 | ✅ 完整双向同步（lark-cli） | ❌ 无飞书同步（保留了旧的 lark-mcp 配置但未使用） |

## 日记模板差异

| | Bingxin | Yiyan |
|---|---|---|
| 工作/学习 section | `## 💼 工作` → `### 任务清单` / `### 工作进展` / `### 会议记录` / `### 问题记录` | `## 📖 学习` → `### 任务清单` / `### 作业情况` / `### 学习内容` / `### 阅读记录` |
| 学习 section | `## 📖 学习` → `### 任务清单` / `### 学习内容` / `### 技术笔记` / `### 阅读记录` | — |
| 生活 section | `## 🏠 个人` → `### 任务清单` / `### 个人事项` / `### 健康记录` / `### 心情感悟` | `## 🏠 生活` → `### 任务清单` / `### 个人事项` / `### 习惯养成` / `### 健康记录` |
| 每日固定任务 | 无 | 有（数学练习/读英语/阅读/练字/跳绳/收拾书包/收拾房间） |
| 明日收拾清单 | 无 | 有（根据课表生成） |

## Steering 规则差异

| 规则文件 | Bingxin | Yiyan |
|---------|---------|-------|
| `check-before-act.md` | ✅ 含关联 Vault 说明、Git 规则、日记规范 | ✅ 简化版（无关联 Vault） |
| `language.md` | ✅ 中文 | ✅ 中文（相同） |
| `command-timeout.md` | ✅ lark-cli 超时策略 | ❌ 不需要 |
| `feishu-migration.md` | ✅ 飞书文档迁移指南 | ❌ 已删除 |
| `project-report-template.md` | ✅ 飞书群汇报模板 | ❌ 不需要 |
| `task-sync.md` | ✅ 飞书任务同步规则 | ❌ 不需要 |
| `daily-note-rules.md` | ❌ 不需要 | ✅ 每日日记生成规则（课程表/作业/固定任务/收拾清单） |

## Skills 差异

| Skill | Bingxin | Yiyan |
|-------|---------|-------|
| `notes-assistant` | ✅ Work/Personal 分类 | ✅ Study/Life 分类 |
| `lark-assistant` + 全套 `lark-*` | ✅ 完整飞书工具链 | ❌ 不需要 |
| `agent-browser` | ✅ | ❌ |
| `planning-with-files` | ✅ | ✅（相同） |
| `obsidian-markdown` | ✅ | ✅（相同） |
| `find-skills` | ✅ | ✅（相同） |
| `self-improvement` | ✅ | ✅（相同） |
| `skill-creator` | ✅ | ✅（相同） |
| `json-canvas` | ✅ | ✅（相同） |

## notes-assistant 内部文件差异

| 文件 | 差异说明 |
|------|---------|
| `SKILL.md` | 路径映射（Work→Study, Personal→Life）、task tag（work→study, personal→life）、飞书工具引用不同 |
| `references/templates.md` | 日记模板结构不同（三栏 vs 两栏）、子标题不同（工作进展 vs 作业情况）、项目路径不同 |
| `references/sync-rules.md` | Bingxin 大幅扩展（飞书任务清单同步、自定义字段、附件、冲突处理），Yiyan 保留旧版简化版 |
| `references/user-guide.md` | 示例不同（API文档 vs 语文作业）、工具不同（lark-cli vs lark-mcp） |
| `references/improvements.md` | 相同 |
| `references/feishu-mcp.md` | Bingxin 已删除，Yiyan 已删除 |

## 共享的通用规则（同步时保持一致）

- filter 函数 `!!()` 包裹（防止 undefined）
- `sort by priority` / `sort by due` / `sort by start`
- `hide postpone button`
- `group by function task.heading` 第三层分组
- 项目总览 Dataview 自动化（相关笔记 + 项目日志含子项）
- Git 提交规则（不频繁提交）
- 日记写作规范（不重复创建已有任务）
- Wikilink 格式（不带 .md 后缀，不带别名）

## 同步原则

1. 通用改动（filter bug、sort、Dataview 模板）→ 双向同步
2. 飞书相关（lark-cli、任务同步、汇报模板）→ 仅 Bingxin
3. 分类适配（Work↔Study、Personal↔Life）→ 各自维护，不覆盖
4. Yiyan 独有（课程表、每日固定任务、积分）→ 仅 Yiyan
5. `.obsidian` 插件配置 → 保持一致（dataview、tasks）
