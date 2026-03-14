# Notes Assistant 操作手册

基于 Kiro Skill + PARA + Zettelkasten 的 Obsidian 知识管理系统。无需安装任何依赖，AI 直接操作 Vault 文件。

## 工作原理

```
用户对话 → AI 自动激活 notes-assistant skill → AI 直接读写 Vault 文件
                                              → AI 调用 lark-mcp 同步飞书
```

所有业务逻辑以 Skill 形式存储在 `.kiro/skills/notes-assistant/` 下。当你提到笔记、记录、任务、项目等关键词时，skill 自动激活，无需手动引用。

## 文件结构

```
Vault/
├── .kiro/
│   ├── skills/
│   │   └── notes-assistant/
│   │       ├── SKILL.md                   # 核心工作流（结构、意图识别、任务、标签）
│   │       └── references/
│   │           ├── templates.md           # 9 种笔记模板
│   │           ├── sync-rules.md          # 飞书同步决策逻辑
│   │           ├── improvements.md        # 用户偏好记录
│   │           └── user-guide.md          # 本文件
│   └── settings/
│       └── mcp.json                       # lark-mcp 连接配置
├── 0-Daily/                               # 日常笔记 (YYYY/MM/YYYY-MM-DD.md)
├── 1-Projects/                            # 项目 (Work/ + Personal/)
├── 2-Areas/                               # 领域 (Work/ + Life/)
├── 3-Resources/                           # 资源 (Tech/ + Life/)
│   └── Tech/
│       ├── Knowledge-Cards/               # 知识卡片
│       ├── Code-Snippets/                 # 代码片段
│       ├── ADR/                           # 架构决策记录
│       └── Problem-Solving/               # 问题解决记录
├── 4-Archives/                            # 归档 (按年份)
└── Attachments/                           # 附件
```

## 快速开始

### 1. 初始化 Vault 结构

对 AI 说：「帮我初始化 PARA 文件夹结构」，AI 会创建上述所有目录。

### 2. 开始使用

直接用自然语言告诉 AI 你想做什么，skill 会自动激活。

## 功能说明

### 日常笔记

| 你说 | AI 做 |
|------|-------|
| 「记录一下今天学了 Docker」 | 创建/追加 `0-Daily/2026/03/2026-03-14.md`，写入学习板块 |
| 「今天开会讨论了新需求」 | 追加到工作板块的会议记录 |
| 「写下今天的心情」 | 追加到生活板块 |

日常笔记按 `0-Daily/YYYY/MM/YYYY-MM-DD.md` 组织，自动带前后日期导航链接。

### 项目管理

| 你说 | AI 做 |
|------|-------|
| 「创建一个工作项目：API 重构」 | 创建 `1-Projects/Work/API重构/README.md` |
| 「新建个人项目：读书计划」 | 创建 `1-Projects/Personal/读书计划/README.md` |
| 「归档 API 重构项目」 | 移动到 `4-Archives/2026/API重构/`，添加归档日期 |

### 会议记录

对 AI 说：「记录今天下午 3 点的技术评审会议，参与者有张三、李四」

AI 创建 `0-Daily/2026/03/2026-03-14-技术评审.md`，包含时间、参与者、议题、行动项等结构。

### 知识卡片

对 AI 说：「把刚才学的 Docker 网络知识提取为知识卡片」

AI 创建 `3-Resources/Tech/Knowledge-Cards/Docker网络.md`，并在源笔记中添加反向链接。

### 其他笔记类型

- 代码片段：「保存一个 Python 装饰器的代码片段」→ `3-Resources/Tech/Code-Snippets/`
- ADR：「记录一个技术决策：选择 PostgreSQL」→ `3-Resources/Tech/ADR/`
- 问题解决：「记录今天解决的 CORS 问题」→ `3-Resources/Tech/Problem-Solving/`

### 任务管理

任务使用 Obsidian checkbox 语法，支持元数据标注：

```markdown
- [ ] 完成 API 文档 📅 2026-03-20 @张三 #task/work #重要
- [ ] 买生日礼物 📅 2026-03-18 #task/personal
- [x] 已完成的任务
```

对 AI 说「查看任务概览」，生成任务中心，按今日/本周/重要紧急/工作/项目/个人分类展示。

任务自动分类规则：
1. `#task/personal` → 个人 | `#task/work` → 工作 | `#task/project/xxx` → 项目
2. 文件在 `1-Projects/` → 项目 | `2-Areas/Work/` → 工作 | `2-Areas/Life/` → 个人
3. 无标记 → 默认个人

### 周回顾 / 月回顾

| 你说 | AI 做 |
|------|-------|
| 「生成本周回顾」 | 创建 `0-Daily/2026/Week-11.md`，自动链接本周日常笔记 |
| 「生成 3 月回顾」 | 创建 `0-Daily/2026/2026-03-Review.md`，自动链接本月周回顾 |

### 飞书同步

需要先配置 lark-mcp（见下方配置说明）。

AI 会自动判断内容是否需要同步：
- 自动同步：工作任务、工作项目、技术决策、包含多个工作关键词的内容
- 自动不同步：私有标签、敏感信息、个人项目、生活领域内容
- 询问用户：学习笔记、特征不明确的内容

同步标签：
- `#sync/feishu` — 标记待同步
- `#synced/feishu` — 已同步
- `#sync-error/feishu` — 同步失败
- `#sync-conflict/feishu` — 冲突

## 配置飞书同步

编辑 `.kiro/settings/mcp.json`，填入飞书应用凭证并启用：

```json
{
  "mcpServers": {
    "lark-mcp": {
      "command": "npx",
      "args": ["-y", "@anthropic/lark-mcp"],
      "env": {
        "FEISHU_APP_ID": "你的飞书 App ID",
        "FEISHU_APP_SECRET": "你的飞书 App Secret"
      },
      "disabled": false,
      "autoApprove": []
    }
  }
}
```

需要 Node.js 环境（npx 命令）。

## 模板列表

所有模板定义在 `references/templates.md` 中，AI 创建笔记时自动使用：

| 模板 | 用途 |
|------|------|
| daily-note | 日常笔记（工作/学习/生活三板块） |
| project | 项目文档（目标、里程碑、任务、日志） |
| meeting | 会议记录（议题、讨论、决策、行动项） |
| knowledge-card | 知识卡片（核心概念、示例、关联） |
| code-snippet | 代码片段（场景、代码、说明） |
| tech-decision-record | 技术决策记录（背景、决策、后果、替代方案） |
| problem-solving | 问题解决（描述、环境、方案、根因） |
| weekly-review | 周回顾（工作/生活总结、下周计划） |
| monthly-review | 月回顾（目标达成、数据统计） |

## 自定义与扩展

- 修改 `SKILL.md` 可调整文件夹结构、意图识别、分类规则
- 修改 `references/sync-rules.md` 可调整同步判断逻辑和关键词
- 修改 `references/templates.md` 可调整模板内容
- `references/improvements.md` 会随使用逐步积累你的偏好
