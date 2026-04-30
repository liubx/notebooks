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
用户说"麦钉韩家村和李家豪，需要添加登录验证码"，当时打开的文件是 `平台更新v2-7/1-任务.md`，我直接把任务创建到了平台更新v2-7的飞书清单中，而实际上"麦钉"是一个独立项目（`1-Projects/Work/麦钉定位/`），任务应该放在麦钉定位的清单里。

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
路径参数需要通过 `--params` JSON 传递（与查询参数一起），不能作为位置参数或 flag：
```bash
# 正确 — 路径参数放在 --params JSON 里
lark-cli task tasklists tasks --params '{"tasklist_guid":"xxx","page_size":"100"}' --as user

# 错误 — 作为 flag
lark-cli task tasklists tasks --tasklist_guid xxx --as user

# 错误 — 作为位置参数
lark-cli task tasklists tasks xxx --params '{"page_size":"100"}' --as user
```

同理，`tasks get` 也需要把 `task_guid` 放在 `--params` 里：
```bash
lark-cli task tasks get --params '{"task_guid":"xxx","user_id_type":"open_id"}' --as user
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


## [ERR-20260408-001] 飞书 API 频率限制导致批量任务同步失败

**时间**: 2026-04-08
**严重性**: medium
**领域**: feishu, api, rate-limit

### 错误描述
使用 Python 脚本通过 subprocess 连续调用 `lark-cli api` 拉取 17 个任务清单数据时，触发飞书 API 频率限制（错误码 99992402），导致所有请求返回空响应或 `ok: false`。即使加了 3~5 秒间隔，限流窗口仍未恢复。而直接在 shell 中手动调用同一命令则正常返回。

### 根因
1. 飞书任务 API 有频率限制，短时间内大量请求会触发 99992402 错误
2. 一旦触发限流，恢复窗口可能较长（超过 5 秒间隔仍不够）
3. 之前多次重试（每个清单 3 次 × 17 个 = 51 次请求）加剧了限流

### 正确做法
1. 批量拉取飞书数据时，每次请求间隔至少 10 秒
2. 遇到限流错误时，指数退避（10s → 20s → 40s）
3. 不要用脚本批量同步所有清单，改为逐个在 shell 中调用，或只同步有变化的清单
4. 考虑先用 `lark-cli task tasklists list` 获取 `updated_at` 时间戳，只同步最近更新过的清单


## [ERR-20260408-002] lark-cli task +create 使用了不存在的 --member 参数

**时间**: 2026-04-08
**严重性**: low
**领域**: lark-cli, task

### 错误描述
创建任务时使用 `--member` 参数指定负责人，报错 `unknown flag: --member`。

### 根因
`task +create` shortcut 的负责人参数是 `--assignee`，不是 `--member`。

### 正确做法
```bash
lark-cli task +create --summary '标题' --description '描述' --assignee 'ou_xxx' --as user
```


## [ERR-20260409-001] iCloud 目录下 os.walk 极慢导致脚本超时

**时间**: 2026-04-09
**严重性**: medium
**领域**: icloud, python, performance

### 错误描述
在 iCloud Drive 同步目录（`~/Library/Mobile Documents/iCloud~md~obsidian/`）下执行 `os.walk()` 遍历 8000+ 文件时，耗时超过 2 分钟，导致 Python 脚本频繁超时。

### 根因
iCloud Drive 对文件系统操作有额外开销（需要检查文件是否已下载、同步状态等），`os.path.exists()` 和 `os.walk()` 每个文件都会触发 iCloud 的元数据查询。

### 正确做法
1. 避免在 iCloud 目录下频繁使用 `os.walk()`，改用 `find` 命令或缓存结果
2. 将脚本放到后台进程运行（`controlBashProcess`），不要用 `executeBash` 带 timeout
3. 如果必须扫描，先用 `find` 生成文件列表到临时文件，再用 Python 读取


## [ERR-20260409-002] docs +search 缺少 search:docs:read scope

**时间**: 2026-04-09
**严重性**: low
**领域**: lark-cli, docs, scope

### 错误描述
执行 `lark-cli docs +search --query '...' --as user` 时报错 `missing required scope(s): search:docs:read`。

### 根因
当前用户 token 未授权 `search:docs:read` scope，无法使用文档搜索功能。

### 正确做法
1. 如果需要搜索，先执行 `lark-cli auth login --scope "search:docs:read"` 授权
2. 或者绕过搜索，直接用已知的文档 token/URL 操作
3. 也可以用 `lark-cli drive +list` 浏览云空间文件夹来定位文档


## [ERR-20260414-001] docs +create 缺少必需的 --markdown 参数

**时间**: 2026-04-14
**严重性**: low
**领域**: lark-cli, docs

### 错误描述
执行 `lark-cli docs +create --title '告警规则说明' --folder-token '' --as user` 时报错 `required flag(s) "markdown" not set`。

### 根因
`docs +create` shortcut 要求必须提供 `--markdown` 参数来指定文档初始内容，不能只传标题。

### 正确做法
```bash
lark-cli docs +create --title '标题' --markdown '# 标题内容' --folder-token 'fldcnXXX' --as user
```


## [ERR-20260414-002] docs +create 长 markdown 内容在命令行中传递失败

**时间**: 2026-04-14
**严重性**: medium
**领域**: lark-cli, docs, shell

### 错误描述
将大段 markdown 内容直接作为 `--markdown` 参数值传入 shell 命令时，由于内容包含单引号、反引号、特殊字符和换行，导致 shell 解析失败，`lark-cli` 报 `required flag(s) "markdown" not set`，且命令超时。

### 根因
Shell 对长字符串和特殊字符的处理有限制，直接在命令行中传递大段 markdown 容易导致引号不匹配、转义问题。

### 正确做法
将 markdown 内容写入临时文件，通过 stdin 或 `--markdown-file` 方式传入：
```bash
# 方式一：写入临时文件后用 cat 管道传入
cat /tmp/content.md | lark-cli docs +create --title '标题' --markdown - --as user

# 方式二：如果支持文件参数
lark-cli docs +create --title '标题' --markdown "$(cat /tmp/content.md)" --as user
```


## [ERR-20260414-003] mermaid.ink 在线渲染服务返回 403 Forbidden

**时间**: 2026-04-14
**严重性**: low
**领域**: mermaid, image-rendering

### 错误描述
通过 Python urllib 请求 `https://mermaid.ink/img/{base64}?type=png` 渲染 Mermaid 流程图为 PNG 时，服务返回 HTTP 403 Forbidden。

### 根因
mermaid.ink 可能对 User-Agent、请求频率或编码格式有限制，Python 默认 User-Agent 被拒绝。

### 补充场景
kroki.io (`POST https://kroki.io/mermaid/png`) 同样返回 403 Forbidden，说明当前网络环境可能对这类在线渲染服务有访问限制。

### 正确做法
1. 优先使用本地 mmdc (mermaid-cli) 渲染：`npx -y @mermaid-js/mermaid-cli mmdc -i input.mmd -o output.png`
2. 如果本地工具不可用，使用浏览器打开 mermaid.live 手动导出
3. 在线服务（mermaid.ink、kroki.io）在受限网络环境下不可靠，不应作为首选方案


## [ERR-20260416-001] lark-cli task +create 使用了不存在的 --tasklist-guid 参数

**时间**: 2026-04-16
**严重性**: low
**领域**: lark-cli, task

### 错误描述
创建任务时使用 `--tasklist-guid` 参数指定清单，报错 `unknown flag: --tasklist-guid`。

### 根因
`task +create` shortcut 的清单参数是 `--tasklist-id`，不是 `--tasklist-guid`。同样没有 `--section-guid` 参数。

### 正确做法
```bash
lark-cli task +create --summary '标题' --tasklist-id '<guid>' --as user
```
注意：`+create` shortcut 不支持直接指定 section，创建后需要用 API 移动到目标 section。或者使用原生 API `task tasks create --data '{...}'` 来同时指定 tasklist 和 section。

### 补充：所有 shortcut 统一使用 --task-id 而非 --task-guid
- `+complete --task-id <guid>`
- `+reopen --task-id <guid>`
- `+tasklist-task-add --tasklist-id <guid> --task-id <guid>`
- `+assign --task-id <guid>`
- `+comment --task-id <guid>`

### 补充：+tasklist-task-add 同样使用 --tasklist-id 和 --task-id
```bash
# 正确
lark-cli task +tasklist-task-add --tasklist-id '<guid>' --task-id '<task_guid>' --as user
# 错误
lark-cli task +tasklist-task-add --tasklist-guid '<guid>' --task-guids '<task_guid>' --as user
```
注意：`+tasklist-task-add` 不支持 `--section-guid` 参数，添加到指定 section 需要用原生 API：
```bash
# 将任务添加到清单的指定 section（正确方式）
lark-cli api POST /open-apis/task/v2/tasks/<task_guid>/add_tasklist \
  --data '{"tasklist_guid":"<清单guid>","section_guid":"<分组guid>"}' --as user

# 从清单移除任务
lark-cli api POST /open-apis/task/v2/tasks/<task_guid>/remove_tasklist \
  --data '{"tasklist_guid":"<清单guid>"}' --as user
```

---

## [ERR-20260414-003] markitdown 转换 pptx 失败：不支持的形状类型

**时间**: 2026-04-14
**严重性**: low
**领域**: markitdown, pptx

### 错误描述
`python3 -m markitdown xxx.pptx` 报错 `NotImplementedError: Shape instance of unrecognized shape type`，无法转换。

### 根因
pptx 中包含 markitdown PptxConverter 不支持的形状类型（如 SmartArt、图表等非标准形状）。

### 正确做法
改用 `python-pptx` 直接提取文本，跳过不支持的形状：
```python
from pptx import Presentation
prs = Presentation('file.pptx')
for i, slide in enumerate(prs.slides):
    for shape in slide.shapes:
        if shape.has_text_frame:
            print(shape.text_frame.text)
```


## [ERR-20260416-003] lark-cli task sections list 不是有效命令

**时间**: 2026-04-16
**严重性**: low
**领域**: lark-cli, task, sections

### 错误描述
执行 `lark-cli task sections list --data/--params '{"tasklist_guid":"xxx"}'` 报错 `unknown flag`。`sections` 不是 `lark-cli task` 的有效子命令。

### 根因
lark-cli 没有封装 `task sections` 子命令。sections 操作需要通过原生 API 调用。

### 正确做法
使用原生 API 获取清单的 sections：
```bash
lark-cli api GET /open-apis/task/v2/sections \
  --params '{"resource_type":"tasklist","resource_id":"<tasklist_guid>","page_size":"50"}' --as user
```

---

## [ERR-20260416-002] tasklists tasks API 的 completed 参数不接受 "both"

**时间**: 2026-04-16
**严重性**: low
**领域**: feishu, api, task

### 错误描述
调用 `lark-cli task tasklists tasks` 时传入 `"completed":"both"` 参数，API 返回 9499 错误：`Invalid parameter value: "both"`。

### 根因
飞书任务 v2 API 的 `completed` 查询参数不支持 `"both"` 值。该参数可能只接受布尔值或特定字符串（如空字符串表示全部）。

### 正确做法
不传 `completed` 参数（默认返回未完成任务），然后单独查询已完成任务：
```bash
# 未完成任务（不传 completed 或 completed=""）
lark-cli task tasklists tasks --params '{"tasklist_guid":"xxx","section_guid":"xxx","page_size":"100"}' --as user

# 已完成任务
lark-cli task tasklists tasks --params '{"tasklist_guid":"xxx","section_guid":"xxx","page_size":"100","completed":"true"}' --as user
```


## [ERR-20260417-001] markitdown 命令行工具未安装（exit code 127）

**时间**: 2026-04-17
**严重性**: low
**领域**: markitdown, cli

### 错误描述
执行 `markitdown "xxx.pdf"` 时返回 exit code 127（command not found），说明 markitdown 未作为全局 CLI 工具安装。

### 根因
markitdown 是 Python 包，需要通过 `pip install markitdown` 安装后才能在命令行使用，或者通过 `python3 -m markitdown` 调用。

### 正确做法
```bash
# 方式一：通过 Python 模块调用
python3 -m markitdown document.pdf

# 方式二：先安装再使用（需要包含 pdf 依赖）
pip install 'markitdown[all]'
markitdown document.pdf
```

### 补充场景：markitdown 已安装但缺少 pdf 依赖
即使 markitdown 包已安装，如果没有安装 `[pdf]` 可选依赖，转换 PDF 时会报 `MissingDependencyException`。需要 `pip install 'markitdown[pdf]'` 或 `pip install 'markitdown[all]'`。


## [ERR-20260426-001] lark-cli api 不支持 --timeout 参数

**时间**: 2026-04-26
**严重性**: low
**领域**: lark-cli, api

### 错误描述
执行 `lark-cli api GET /open-apis/wiki/v2/spaces --params '...' --as user --timeout 30000` 时报错 `unknown flag: --timeout`。

### 根因
`lark-cli api` 子命令没有 `--timeout` flag。超时控制应该在 `executeBash` 的 `timeout` 参数中设置，而不是传给 lark-cli。

### 正确做法
```bash
# 正确：timeout 放在 executeBash 层面
executeBash: command="lark-cli api GET /open-apis/wiki/v2/spaces --params '...' --as user", timeout=30000

# 错误：timeout 传给 lark-cli
lark-cli api GET ... --timeout 30000
```


## [ERR-20260426-002] wiki setting API 无法修改知识库名称

**时间**: 2026-04-26
**严重性**: low
**领域**: feishu, wiki, api

### 错误描述
`PUT /open-apis/wiki/v2/spaces/{space_id}/setting` 传入 `{"name":"新名称"}` 返回 `code: 0` 成功，但实际知识库名称未改变。

### 根因
飞书 wiki setting API 只能修改 `create_setting`（谁能创建节点）和 `security_setting`（安全设置）等配置项，`name` 字段不在 setting 的可修改范围内。飞书 OpenAPI 目前没有提供修改知识库名称的接口。

### 正确做法
知识库名称只能在飞书网页端手动修改（知识库设置页面）。创建知识库时就要确定好名称。


## [ERR-20260426-003] 飞书没有 move_wiki_docs_to_space API（知识库→云空间反向移动）

**时间**: 2026-04-26
**严重性**: medium
**领域**: feishu, wiki, api

### 错误描述
尝试调用 `POST /open-apis/wiki/v2/spaces/{space_id}/nodes/move_wiki_docs_to_space` 将知识库文件移回云空间，返回 HTTP 404。

### 根因
飞书 OpenAPI 只提供了 `move_docs_to_wiki`（云空间→知识库）的单向移动 API，没有反向操作 `move_wiki_docs_to_space`。知识库中的文件无法通过 API 直接移回云空间。

### 正确做法
1. 知识库文件只能在飞书网页端手动拖拽移回云空间
2. 或者通过 wiki `move` API 在知识库内部移动节点（不能移出知识库）
3. 迁移前应该先复制副本到知识库，再确认无误后才移动原件，避免需要反向操作


## [ERR-20260426-004] 知识库文件无法通过 drive files delete API 删除

**时间**: 2026-04-26
**严重性**: medium
**领域**: feishu, wiki, drive, api

### 错误描述
尝试用 `DELETE /open-apis/drive/v1/files/{file_token}?type=docx` 删除知识库中的文件，返回 `1061004 forbidden`。

### 根因
知识库中的文件受知识库权限保护，不能通过云空间的 drive API 直接删除。飞书 wiki API 也没有提供删除节点的接口。

### 正确做法
1. 知识库节点只能在飞书网页端手动删除
2. 或者通过知识库管理员在设置中操作
3. API 层面目前无法删除知识库节点——这是飞书 OpenAPI 的限制


## [ERR-20260426-005] drive files move API 也无法将知识库文件移回云空间

**时间**: 2026-04-26
**严重性**: medium
**领域**: feishu, wiki, drive, api

### 错误描述
尝试用 `POST /open-apis/drive/v1/files/{file_token}/move` 将知识库中的文件（docx 和 file 类型都试过）移回云空间目录，返回 `1061002 params error`。

### 根因
知识库中的文件虽然有 obj_token，但它们已经属于知识库管理，drive move API 不支持跨知识库→云空间的移动。`1061002 params error` 实际上是"该文件不在云空间中，无法通过 drive API 移动"的意思。

### 正确做法
1. 飞书 API 层面完全无法将文件从知识库移回云空间（move_wiki_docs_to_space 不存在，drive move 也不行）
2. 只能在飞书网页端手动操作
3. 迁移时应该先复制到知识库，确认无误后再移动原件，避免需要反向操作


## [ERR-20260428-001] 云空间文件夹 token 误用 wiki nodes API 查询

**时间**: 2026-04-28
**严重性**: low
**领域**: feishu, wiki, drive, api

### 错误描述
将云空间文件夹的 token（如 `MrIOflncTlWrkEd4hJZcUxatncd`）作为 `parent_node_token` 传给 `GET /open-apis/wiki/v2/spaces/{space_id}/nodes`，返回 `131005 node not found by parent node token`。

### 根因
新 004/005 目录是云空间文件夹，不是知识库节点。Wiki API 只能查询知识库内的节点，云空间文件夹需要用 Drive API（`GET /open-apis/drive/v1/files`）来列出内容。

### 正确做法
区分 token 来源：
- 知识库节点 → 用 `GET /open-apis/wiki/v2/spaces/{space_id}/nodes` + `parent_node_token`
- 云空间文件夹 → 用 `lark-cli drive +list --folder-token <token>` 或 `GET /open-apis/drive/v1/files` + `folder_token`

```bash
# 列出云空间文件夹内容
lark-cli drive +list --folder-token <folder_token> --as user
```


## [ERR-20260430-001] wiki tasks API 查询需要 task_type 参数

**时间**: 2026-04-30
**严重性**: low
**领域**: feishu, wiki, api

### 错误描述
查询 `move_docs_to_wiki` 异步任务状态时，使用 `GET /open-apis/wiki/v2/tasks/{task_id}` 返回 `99992402 field validation failed: task_type is required`。

### 根因
wiki tasks API 需要 `task_type` 查询参数来区分不同类型的异步任务。

### 正确做法
```bash
# 正确：带 task_type 参数
lark-cli api GET /open-apis/wiki/v2/tasks/<task_id> \
  --params '{"task_type":"move"}' --as user
```


## [ERR-20260430-001] 知识库节点操作应该用 copy 而不是 move，且无法通过 API 删除节点

**时间**: 2026-04-30
**严重性**: high
**领域**: feishu, wiki, api

### 错误描述
在百度水厂项目中，多次使用 `wiki move` 在知识库内移动节点（从根节点移到子节点，又移回来），导致知识库结构混乱。后来用 `drive copy` + `move_docs_to_wiki` 复制文件到知识库，又产生了重复节点。飞书 API 不支持删除知识库节点，无法通过 API 清理重复。

### 根因
1. 没有遵守"不动原文件"的原则，在知识库内使用了 wiki move
2. 多次反复操作导致重复文件
3. 飞书 wiki API 没有删除节点的方法

### 正确做法
1. **永远不要用 wiki move 移动知识库中的文件**——一旦文件在知识库中的位置确定，就不要再动
2. **先规划好知识库结构，再一次性创建**——创建子节点 → copy 文件到子节点，不要先创建再调整
3. **知识库节点无法通过 API 删除**——只能在飞书网页端手动删除，所以操作前要确认
4. **迁移步骤中应该先确定总览结构，再同步到知识库**——不要边做边调整
