# 错误记录

命令执行失败、API 报错、工具异常等。

---



## [ERR-20260407-001] 状态 tag 被错误插入到 wikilink 内部

**时间**: 2026-04-07
**严重性**: high
**领域**: obsidian, feishu

### 错误描述
同步脚本在任务行的 `^task-xxx` block ID 前插入 `#status/doing` 等 tag 时，没有检查插入位置是否在 `[[...]]` wikilink 内部，导致：

错误结果：`[[1-Projects/Work/广州机场/1-任务##status/doing ^task-alarm-unstable|↗️]]`
正确结果：`[[1-Projects/Work/广州机场/1-任务#^task-alarm-unstable|↗️]] ... #status/doing ^task-alarm-unstable`

### 影响
- 48 个任务行被破坏
- Obsidian 无法识别 `#status/xxx` 为 tag，导致每日任务视图中状态分组失效
- wikilink 的锚点也被破坏（`##status/doing` 不是有效锚点）

### 根因
脚本用正则 `re.search(r'\^task-', line)` 找到 block ID 位置后直接在前面插入，但没有判断该位置是否在 `[[...]]` 内部。任务行格式中 `^task-xxx` 出现两次：一次在 wikilink 内（`[[...#^task-xxx|↗️]]`），一次在行尾作为 block ID。

### 正确做法
插入 `#status/xxx` tag 时，必须确保插入位置在 `[[...]]` 外部：
1. 找到行尾的 `^task-xxx`（不在 `[[...]]` 内的那个）
2. 或者直接在 `#task/work` 或 `#project/xxx` tag 之后插入
3. 最安全的方式：在最后一个 `#project/xxx` tag 之后、行尾 `^task-xxx` 之前插入

```python
# 错误：直接在第一个 ^task- 前插入（可能在 wikilink 内）
m = re.search(r'\^task-', line)
line = line[:m.start()] + '#status/doing ' + line[m.start():]

# 正确：在行尾的 block ID 前插入（排除 wikilink 内的）
# 行尾 block ID 格式：空格 + ^task-xxx + 换行
m = re.search(r' (\^task-\S+)\s*$', line)
if m:
    line = line[:m.start()] + ' #status/doing ' + line[m.start()+1:]
```


## [ERR-20260407-002] 推送飞书状态时未同步写入本地 tag

**时间**: 2026-04-07
**严重性**: medium
**领域**: feishu, obsidian

### 错误描述
同步脚本在"本地→飞书"推送状态（如未完成任务默认设为"进行中"）时，只更新了飞书端，没有同时给本地任务行加上对应的 `#status/doing` tag。

### 影响
AI工作流的4个未完成任务推送了飞书"进行中"状态，但本地没有 `#status/doing`，导致每日任务视图中这些任务显示为"未开始"。

### 正确做法
推送飞书状态的同时，必须同步更新本地任务行的 status tag。双向同步应该是原子操作——本地和飞书保持一致。


## [ERR-20260407-003] 任务添加到错误的项目清单

**时间**: 2026-04-07
**严重性**: high
**领域**: feishu, task-management

### 错误描述
用户说"麦钉韩家村和李家豪，需要添加登录验证码"，当时打开的文件是 `平台更新v2-7/1-任务.md`，我直接把任务创建到了平台更新v2-7的飞书清单中，而实际上"麦钉"是一个独立项目（`1-Projects/Work/麦钉项目/`），任务应该放在麦钉项目的清单里。

### 影响
- 在错误的飞书清单中创建了任务，需要删除后重建
- 浪费了一个 task_id（t106034）

### 根因
1. 过度依赖当前打开的文件上下文，没有分析用户消息中的项目归属关键词
2. "麦钉"是明确的项目名称，应该先搜索是否有对应项目目录

### 正确做法
- 用户提到具体项目名称（如"麦钉"、"广州机场"等）时，先在 `1-Projects/Work/` 下搜索对应项目
- 不要仅凭当前打开的文件决定任务归属
- 如果不确定归属，先问用户确认

---

## [ERR-20260407-004] 飞书任务 API 路径错误：添加成员

**时间**: 2026-04-07
**严重性**: low
**领域**: feishu, api

### 错误描述
给任务添加负责人时，使用了错误的 API 路径：
- 错误：`POST /open-apis/task/v2/tasks/{task_guid}/members`（404）
- 正确：`POST /open-apis/task/v2/tasks/{task_guid}/add_members`

### 正确做法
飞书任务 v2 API 添加成员的正确路径是 `/add_members`，支持批量添加：
```bash
lark-cli api POST /open-apis/task/v2/tasks/<task_guid>/add_members \
  --data '{"members":[{"id":"ou_xxx","type":"user","role":"assignee"}]}' --as user
```


## [ERR-20260407-005] lark-cli task 原生 API 路径参数传递方式错误

**时间**: 2026-04-07
**严重性**: low
**领域**: lark-cli, task

### 错误描述
调用 `lark-cli task tasklists tasks` 时，使用了 `--tasklist_guid "xxx"` 的方式传递路径参数，报错 `unknown flag: --tasklist_guid`。

### 根因
lark-cli 原生 API 的路径参数（如 `tasklist_guid`）不是通过 `--flag` 传递的，而是作为位置参数直接跟在命令后面。

### 正确做法
路径参数需要通过 `--params` JSON 传递（与查询参数一起）：
```bash
# 正确
lark-cli task tasklists tasks --params '{"tasklist_guid":"xxx"}' --as user

# 错误
lark-cli task tasklists tasks --tasklist_guid xxx --as user
lark-cli task tasklists tasks "xxx" --as user
```


## [ERR-20260407-006] 任务被移到其他清单时误判为已删除

**时间**: 2026-04-07
**严重性**: medium
**领域**: feishu, task-sync

### 错误描述
同步服务器运维清单时，"建立内网镜像中心"(5f5820f8) 不在 `tasklists.tasks` 返回结果中，被误判为已删除并从本地移除。实际上该任务只是被移到了另一个飞书清单（`ea9de802`），任务本身仍然存在且未完成。

### 根因
`tasklists.tasks` API 只返回当前清单中的任务。如果任务被移到其他清单，就不会出现在原清单的返回结果中。同步逻辑没有区分"任务被删除"和"任务被移到其他清单"两种情况。

### 正确做法
当本地有的任务在清单 API 中找不到时，应该：
1. 先用 `tasks.get` 查询该任务的详情，确认任务是否还存在
2. 如果任务存在但不在当前清单中（`tasklists` 字段变了），说明是被移走了，不应删除
3. 只有当 `tasks.get` 返回 404 或任务确实被删除时，才从本地移除
