# 学习记录

开发过程中捕获的纠正、洞察和知识盲区。

**分类**: correction（纠正） | insight（洞察） | knowledge_gap（知识盲区） | best_practice（最佳实践）
**领域**: obsidian | feishu | git | infra | docs | config | life
**状态**: pending（待处理） | resolved（已解决） | promoted（已晋升为规则）

## 状态说明

| 状态 | 含义 |
|------|------|
| `pending` | 尚未处理 |
| `resolved` | 已修复或已整合 |
| `promoted` | 已晋升到 `.kiro/steering/` 或 `.kiro/rules/` |

---


## [LRN-20260322-001] best_practice

**记录时间**: 2026-03-22
**优先级**: high
**状态**: promoted
**领域**: obsidian

### 摘要
Obsidian wikilink 不带 `.md` 后缀，不带别名

### 详情
Obsidian vault 中的 wikilink 格式为 `[[path/to/file]]`，不需要加 `.md` 后缀。这是用户明确要求的规范。

### 晋升到
`.kiro/rules/check-before-act.md`

---

## [LRN-20260322-002] correction

**记录时间**: 2026-03-22
**优先级**: high
**状态**: promoted
**领域**: git

### 摘要
`4-Archives/Notes/` 在 `.gitignore` 中，不要用 `git add -f`

### 详情
用户纠正：不要对 `.gitignore` 中的文件使用 `git add -f` 强制提交。这些文件被排除是有意为之的。

### 晋升到
`.kiro/rules/check-before-act.md`

---

## [LRN-20260322-003] best_practice

**记录时间**: 2026-03-22
**优先级**: medium
**状态**: resolved
**领域**: infra

### 摘要
Wikimedia Commons 下载图片需要设置 User-Agent，否则会被 429 限流

### 详情
直接用 curl 下载 Wikimedia 图片会遇到 429 Too Many Requests。需要设置浏览器 User-Agent header 才能正常下载。正确的 curl 命令：`curl -L -H "User-Agent: Mozilla/5.0" -o file.jpg "URL"`

---

## [LRN-20260322-004] best_practice

**记录时间**: 2026-03-22
**优先级**: medium
**状态**: resolved
**领域**: obsidian

### 摘要
修改文件前必须先读取当前状态，不依赖记忆

### 详情
用户经常在对话之间手动编辑文件。每次修改前都要用 readFile 或 git status 确认文件当前实际状态，不能依赖之前对话的上下文。

---

## [LRN-20260322-005] best_practice

**记录时间**: 2026-03-22
**优先级**: high
**状态**: pending
**领域**: config

### 摘要
新建 skill 直接在 `.kiro/skills/` 下创建，不用 `npx skills add`

### 详情
`npx skills add` 会下载整个 GitHub 仓库到 `.agents/skills/`，然后创建符号链接到 `.kiro/skills/`。下载的文件大部分是其他平台（OpenClaw/Claude Code/Copilot）的配置，对 Kiro 没用。正确做法是直接在 `.kiro/skills/<skill-name>/SKILL.md` 创建精简的中文版 skill 文件，只保留对 Kiro 有用的内容。

---
