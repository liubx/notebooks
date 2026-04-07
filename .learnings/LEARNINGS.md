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


## [LRN-20260402-001] correction

**记录时间**: 2026-04-02
**优先级**: high
**状态**: pending
**领域**: feishu

### 摘要
飞书任务 API 的 due/start timestamp 是毫秒级，不是秒级

### 详情
用户多次反馈创建任务时日期没有设上。原因是飞书任务 v2 API 的 `due.timestamp` 和 `start.timestamp` 字段需要**毫秒级时间戳**（13位数字），而不是秒级（10位）。

错误写法：`"timestamp":"1775088000"`（秒级，10位）→ 飞书会存为错误日期
正确写法：`"timestamp":"1775088000000"`（毫秒级，13位）→ 正确的 2026-04-02

创建任务时也一样，`create` 接口的 due/start 也需要毫秒级时间戳。之前用 `"date":"2026-04-10"` 格式传入被忽略了，飞书 v2 API 不支持 date 字段，只认 timestamp + is_all_day。

正确的创建任务带日期写法：
```json
{
  "summary": "任务标题",
  "due": {"timestamp": "1775779200000", "is_all_day": true},
  "start": {"timestamp": "1775088000000", "is_all_day": true}
}
```

计算方法：`python3 -c "from datetime import datetime,timezone; print(int(datetime(2026,4,2,tzinfo=timezone.utc).timestamp()*1000))"`

---


## [LRN-20260407-001] correction

**记录时间**: 2026-04-07
**优先级**: high
**状态**: pending
**领域**: feishu

### 摘要
飞书任务时间设置必须用 `+update`/`+create` shortcut 的日期参数，不要用原生 API 手动传时间戳

### 详情
多次出现用原生 API（`PATCH /open-apis/task/v2/tasks/`）设置 start/due 时间戳后，飞书端显示的日期不正确的问题。根本原因：

1. **秒级 vs 毫秒级混淆**：飞书 v2 API 的 timestamp 字段有时接受秒级有时接受毫秒级，行为不一致
2. **`is_all_day` 与时区交互**：设置 `is_all_day: true` 时，时间戳会被飞书按 UTC 解析再转换为用户时区，导致日期偏移
3. **原生 API 的 start 字段经常不生效**：PATCH 返回 `code: 0` 但实际 start 没有更新

**正确做法**：
- 设置截止日期：`lark-cli task +update --task-id <guid> --due 2026-04-07 --as user`
- 设置开始日期：`lark-cli task +update --task-id <guid> --data '{"start":{"timestamp":"<毫秒>","is_all_day":true}}' --as user`
- 创建任务带日期：`lark-cli task +create --summary '标题' --due 2026-04-07 --as user`
- `+update` 的 `--due` 参数支持 `YYYY-MM-DD` 格式，会自动处理时间戳转换，优先使用
- `+update` 不支持 `--start` 参数，start 只能通过 `--data` JSON 传入，此时必须用**毫秒级时间戳**（13位）
- `+create` 不支持 `--start` 参数，创建后需要单独用 `+update --data` 补 start

**绝对不要**：
- 用秒级时间戳（10位）传给 API — 会变成 1970 年附近的日期
- 猜测时间戳格式 — 始终用 `python3 -c "..."` 计算确认
- 连续用原生 API 设置多个字段 — lark-cli 有输出缓存问题，容易误判结果

---


## [LRN-20260407-002] insight

**记录时间**: 2026-04-07
**优先级**: high
**状态**: promoted
**领域**: feishu

### 摘要
飞书任务自定义字段必须通过 API 创建才能正确绑定到清单任务上

### 详情
南宁机场清单遇到的问题：清单上存在自定义字段（优先级、状态），但通过 `tasks.patch` 设置值时返回 1470403 错误 "task is not attached with the custom field"。

**根本原因**：这些自定义字段不是通过 `POST /open-apis/task/v2/custom_fields` API 创建并绑定到清单的，而是通过其他方式（可能是飞书界面复制或从其他清单关联）添加的。这种方式创建的字段虽然在清单级别可见，但不会自动绑定到清单中的任务上。

**尝试过但无效的方法**：
1. 重新登录获取 `task:custom_field:write` scope → 无效，不是权限问题
2. 把任务从清单移除再加回来 → 无效，字段仍未绑定
3. `POST /custom_fields/{guid}/remove` + `POST /custom_fields/{guid}/add` 重新绑定 → 无效
4. 创建任务时带 `custom_fields` 参数 → 同样报 1470403

**最终解决方案**：
1. 在飞书界面上删除有问题的自定义字段
2. 通过 API 重新创建字段并绑定到清单：
```bash
lark-cli api POST /open-apis/task/v2/custom_fields --data '{
  "resource_type": "tasklist",
  "resource_id": "<tasklist_guid>",
  "name": "优先级",
  "type": "single_select",
  "single_select_setting": {
    "options": [
      {"name": "高", "color_index": 1},
      {"name": "中", "color_index": 11},
      {"name": "低", "color_index": 16}
    ]
  }
}' --as user
```
3. 通过 API 创建的字段会自动绑定到清单中的所有任务（包括已有任务），之后 `tasks.patch` 设置值就能成功

**注意**：
- 每个清单的自定义字段 guid 和选项 guid 都不同，不能跨清单复用
- `lark-cli schema` 中没有 `custom_fields` 资源，需要用 `lark-cli api` 原生调用
- 创建字段的请求体字段直接放顶层（`name`、`type`、`resource_type`、`resource_id`），不需要 `custom_field` 包装

### 晋升到
`.kiro/steering/task-sync.md` — 自定义字段同步章节

---

## [LRN-20260407-003] best_practice

**记录时间**: 2026-04-07
**优先级**: medium
**状态**: promoted
**领域**: feishu

### 摘要
同步任务时必须双向同步自定义字段（优先级+状态）到本地和飞书

### 详情
之前同步任务只同步了标题、日期、负责人、完成状态，遗漏了自定义字段（优先级和状态）。

**同步规则**：
- 飞书 → 本地：优先级映射为 emoji（🔺高/⏫中/🔼低），状态映射为 tag（`#status/doing` 等）
- 本地 → 飞书：emoji 和 tag 反向映射为自定义字段选项值
- 已完成任务自动设状态为"已完成"
- 未完成且无状态标记的任务默认设为"进行中"

### 晋升到
`.kiro/steering/task-sync.md` — 自定义字段同步章节
