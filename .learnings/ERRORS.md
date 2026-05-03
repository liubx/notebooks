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

### 补充场景：drive files copy 的 file_token 也是路径参数
```bash
# 正确 — file_token 放在 --params 里
lark-cli drive files copy --params '{"file_token":"xxx"}' --data '{"name":"名称","type":"docx","folder_token":"fldXXX"}' --as user

# 错误 — 作为 flag
lark-cli drive files copy --file_token xxx --data '...' --as user
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

### 补充确认（2026-05-01）
- 飞书 OpenAPI 的 wiki scope 列表中没有 `wiki:node:delete`，只有 create/read/retrieve/update/copy/move
- `DELETE /open-apis/wiki/v2/spaces/{space_id}/nodes/{node_token}` 路径虽然能接收请求（要求 `obj_type` body 参数），但 lark-cli 在 DELETE + `--data` 时路径参数解析异常（报 `node not found`），且即使修复也可能因缺少 scope 而失败
- 结论：**飞书 OpenAPI 不支持删除知识库节点**，只能在网页端手动操作


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


## [ERR-20260501-001] file 类型可以通过 drive copy + move_docs_to_wiki 加入知识库

**时间**: 2026-05-01
**严重性**: medium
**领域**: feishu, wiki, api

### 错误描述
之前认为 file 类型（.docx/.xlsx/.pptx/.zip/.pdf/.png/.svg/.jpeg 等上传附件）无法加入知识库，因为 `wiki create node` API 不支持 `obj_type: file`（返回 131002 param err）。

### 根因
`wiki create node` API 确实不支持 file 类型。但 `move_docs_to_wiki` API 支持 file 类型。

### 正确做法
用两步操作把 file 类型文件加入知识库（不动原件）：
1. `drive files copy` — 复制一份副本到临时位置
2. `move_docs_to_wiki` — 把副本移入知识库节点

```bash
# 步骤1：复制副本
lark-cli api POST /open-apis/drive/v1/files/{原件token}/copy \
  --data '{"type":"file","folder_token":"{临时目录}","name":"{文件名}"}' --as user

# 步骤2：把副本移入知识库
lark-cli api POST /open-apis/wiki/v2/spaces/{space_id}/nodes/move_docs_to_wiki \
  --data '{"parent_wiki_token":"{知识库节点}","obj_type":"file","obj_token":"{副本token}"}' --as user
```

注意：这里 move_docs_to_wiki 移的是副本，不是原件，所以不违反"不动原件"的原则。


## [ERR-20260501-002] macOS 默认 bash 3.x 不支持 declare -A 关联数组

**时间**: 2026-05-01
**严重性**: low
**领域**: bash, macos, shell

### 错误描述
在 macOS 上执行包含 `declare -A` 的 bash 脚本时报错 `declare: -A: invalid option`，导致脚本中所有关联数组操作失败。

### 根因
macOS 默认的 `/bin/bash` 是 3.2 版本（因 GPLv3 许可证问题未更新），而关联数组（`declare -A`）是 bash 4.0+ 的特性。

### 正确做法
1. 不要在脚本中使用 `declare -A`，改用普通数组或逐个变量
2. 或者使用 `#!/usr/bin/env bash` 并确保 PATH 中有 bash 4+（如 Homebrew 安装的 `/opt/homebrew/bin/bash`）
3. 对于批量操作，直接逐个调用命令更可靠


## [ERR-20260501-001] docs +update 写入知识库文档报 CreateDescendant forbidden (1770032)

**时间**: 2026-05-01
**严重性**: medium
**领域**: feishu, docs, wiki, api

### 错误描述
使用 `docs +update --mode overwrite` 向知识库中通过 `wiki create node` 创建的空 docx 文档写入 markdown 内容时，部分文档报错 `CreateDescendant failed: forbidden`（errorCode: 1770032）。同样的操作对其他文档成功，说明不是权限问题，而是内容相关。

### 根因
可能是 markdown 内容中包含了飞书 API 不支持的特殊格式或字符（如特殊的 HTML 标签、过长的代码块、特殊 Unicode 字符等），导致创建文档块时被拒绝。

### 正确做法
1. 检查失败文档的 markdown 内容，排查特殊字符或格式
2. 去掉 `<mention-user>`、`<reminder>`、`<text color>` 等飞书特有标签后重试
3. 如果内容过长或包含超大表格（如 31 列的甘特图），尝试简化后写入
4. 如果内容过长，尝试分段写入（先写一部分，再 append）

### 补充场景
- `<mention-user>` 和 `<reminder>` 标签会导致 `CreateDescendant forbidden`（1770032），去掉后成功
- 包含大量 `<lark-table>` 的超长文档（2600+ 行，31 列甘特图表格）会导致 `field validation failed`（99992402），可能是表格列数或总块数超限


## [ERR-20260501-002] move_docs_to_wiki 会在云空间原位留下 shortcut，需要清理

**时间**: 2026-05-01
**严重性**: low
**领域**: feishu, wiki, drive, api

### 错误描述
使用 `drive copy` + `move_docs_to_wiki` 将文件副本移入知识库后，云空间原位会自动生成一个 shortcut（快捷方式），指向知识库中的新节点。百度水厂项目产生了 48 个 shortcut。

### 根因
`move_docs_to_wiki` 的设计行为：将文件从云空间移入知识库时，会在原位留下 shortcut 以保持引用不断。

### 正确做法
`move_docs_to_wiki` 完成后，立即删除云空间中产生的 shortcut：
```bash
# shortcut 可以通过 drive files delete API 删除
lark-cli api DELETE /open-apis/drive/v1/files/{shortcut_token} --params '{"type":"shortcut"}' --as user
```

迁移步骤中应该加入清理 shortcut 的步骤：
1. `drive copy` 复制副本到临时位置
2. `move_docs_to_wiki` 移入知识库
3. 列出临时位置的 shortcut（`type=shortcut`）
4. 逐个删除 shortcut


## [ERR-20260501-003] docs +update 不支持 sub-page-list 标签

**时间**: 2026-05-01
**严重性**: low
**领域**: feishu, docs, api

### 错误描述
通过 `docs +update --markdown` 写入包含 `<sub-page-list wiki-token="xxx"/>` 的内容时，标签被当作不支持的 HTML 标签移除，warning: `unsupported HTML tag removed: sub-page-list`。

### 根因
`docs +update` 的 markdown 解析器不支持 `<sub-page-list>` 这个飞书特有的组件标签。虽然 `docs +fetch` 能读取到这个标签，但写入时不支持。

### 正确做法
`<sub-page-list>` 只能在飞书网页端手动添加（在文档中输入 `/子页面列表` 或 `/sub-page-list`）。API 无法写入此组件。


## [ERR-20260501-004] lark-cli schema drive.files.copy 实际执行了 copy 操作

**时间**: 2026-05-01
**严重性**: medium
**领域**: lark-cli, drive, api

### 错误描述
执行 `lark-cli schema drive.files.copy` 期望查看 API 参数结构，但实际返回了 `{"code":0,"data":{"task_id":"xxx"},"msg":"success"}`，说明它实际执行了 copy 操作而不是显示 schema。

### 根因
`lark-cli schema` 对某些 API 可能不支持或行为异常。`drive.files.copy` 可能被解析为实际的 API 调用。

### 正确做法
对于已知的 API（如 drive files copy、wiki move_docs_to_wiki），直接参考错误记录中已有的正确用法，不需要再查 schema。


## [ERR-20260502-001] 迁移脚本分类逻辑 bug：重复创建同名分类节点

**时间**: 2026-05-02
**严重性**: high
**领域**: feishu, wiki, migration-script

### 错误描述
`migrate_project.py` 的分类逻辑对每个子目录路径都创建新的分类节点，没有缓存已创建的分类名。导致武汉机场迁移时创建了 20+ 个重复的"接口对接"节点和 2 个重复的"会议纪要"节点。

### 根因
```python
# bug 代码：每次都创建新节点
for p in sorted(groups.keys()):
    if p != '根目录':
        cat_name = p.strip('/').split('/')[0]
        # 没有检查 cat_name 是否已创建过
        nt, ot = create_node(root_nt, cat_name)
        category_map[p] = nt
```

### 正确做法
用 dict 缓存已创建的分类名，同名分类只创建一次：
```python
created_categories = {}
for p in sorted(groups.keys()):
    if p != '根目录':
        cat_name = p.strip('/').split('/')[0]
        if cat_name not in created_categories:
            nt, ot = create_node(root_nt, cat_name)
            created_categories[cat_name] = nt
        category_map[p] = created_categories[cat_name]
```


## [ERR-20260502-002] lark-cli wiki 子命令用法错误

**时间**: 2026-05-02
**严重性**: low
**领域**: lark-cli, wiki

### 错误描述
执行 `lark-cli wiki create_space_node --space-id xxx` 报错 `unknown flag: --space-id`。`create_space_node` 不是有效的 wiki 子命令。

### 根因
lark-cli wiki 的可用子命令是：`+node-create`、`members`、`nodes`、`spaces`。创建知识库节点应该用 `wiki +node-create` shortcut 或原生 API。

### 正确做法
```bash
# 方式一：使用 shortcut
lark-cli wiki +node-create --space-id <space_id> --title '标题' --obj-type docx --as user

# 方式二：使用原生 API
lark-cli api POST /open-apis/wiki/v2/spaces/<space_id>/nodes \
  --data '{"obj_type":"docx","parent_node_token":"","title":"标题"}' --as user
```


## [ERR-20260503-001] bash 脚本中 $(pwd) 路径含单引号导致 python3 -c 解析失败

**时间**: 2026-05-03
**严重性**: medium
**领域**: bash, python, shell

### 错误描述
迁移脚本中用 `TMPFILE="$(pwd)/api_result_tmp.json"` 生成临时文件路径，但工作目录 `Bingxin's Vault` 包含单引号，导致 `python3 -c` 内联代码中 `open('/Users/.../Bingxin's Vault/...')` 的字符串被单引号截断，报 `SyntaxError: unterminated string literal`。

### 根因
`$(pwd)` 展开后路径含单引号，嵌入到 Python 单引号字符串中会导致字符串提前终止。

### 正确做法
1. 临时文件放到 `/tmp` 目录（不含特殊字符）：`TMPFILE="/tmp/xxx.json"`
2. 或者用 Python 的 `sys.argv` 传递路径，避免在 `-c` 字符串中硬编码路径
3. 永远不要假设工作目录路径不含特殊字符


## [ERR-20260503-002] lark-cli docs +update @file 必须使用相对路径

**时间**: 2026-05-03
**严重性**: low
**领域**: lark-cli, docs

### 错误描述
执行 `lark-cli docs +update --markdown @/tmp/shanghai_bosch.md` 时报错 `--file must be a relative path within the current directory`。

### 根因
lark-cli 的 `@file` 语法要求文件路径必须是当前工作目录下的相对路径，不支持绝对路径或当前目录外的路径。

### 正确做法
```bash
# 正确：使用相对路径（文件在当前工作目录下）
lark-cli docs +update --doc xxx --markdown @scripts/file.md --as user

# 错误：使用绝对路径
lark-cli docs +update --doc xxx --markdown @/tmp/file.md --as user
```


## [ERR-20260503-003] docs +update 无法写入 mention-doc 标签

**时间**: 2026-05-03
**严重性**: high
**领域**: feishu, docs, api

### 错误描述
使用 `docs +update --mode append` 写入包含 `<mention-doc token="xxx" type="docx">文件名</mention-doc>` 的 markdown 内容时，API 返回 `errorCode=4000515, open api resource Not found`。纯文本内容可以正常写入，但 mention-doc 标签无法通过 API 创建。

### 根因
`<mention-doc>` 是飞书文档中的特殊块类型（文档引用/链接），docx API 的 `create descendant` 接口不支持通过 markdown 创建这种块。这些 mention-doc 块在迁移时是通过 `move_docs_to_wiki` 等操作自动生成的，不是通过 docs API 写入的。

### 正确做法
1. **不要删除包含 mention-doc 的文档内容**——一旦删除就无法通过 API 恢复
2. 对于需要修改格式的目录页，只能做局部修改（删除描述行、纯文本摘要），不能重写整个文档
3. 如果需要重建 mention-doc 列表，只能在飞书网页端手动操作
4. `docs +fetch` 能读取 mention-doc，但 `docs +update` 不能写入——这是单向的


### 补充场景（replace_all 也无法修改含 mention-doc 的行）
`replace_all` 模式替换含 mention-doc 行中的文本时，也会报 `errorCode=4000515`。因为替换操作需要重建整个块，而重建时 mention-doc 元素无法通过 API 创建。结论：**任何需要重建含 mention-doc 块的操作都会失败**，只能删除纯文本行或追加纯文本内容。


## [ERR-20260503-004] doc 旧版文档 drive copy 后 move_docs_to_wiki 报 131005 document not found

**时间**: 2026-05-03
**严重性**: medium
**领域**: feishu, wiki, drive, doc

### 错误描述
对 doc 旧版文档（`doccn` 前缀）执行 `drive files copy` 成功获得新 token，但随后执行 `move_docs_to_wiki` 时报 `131005 document not found by token`。即使等待后重试也一样失败。docx 和 file 类型不受影响。

### 根因
`drive files copy` 对 doc 旧版文档的 copy 行为可能不同于 docx——copy 可能返回了 token 但实际文档未完全创建，或者 doc 类型的副本不被 `move_docs_to_wiki` 识别。

### 正确做法
doc 旧版文档不要通过 `drive copy` + `move_docs_to_wiki` 迁移到知识库。替代方案：
1. 这些文档已经通过导出 API + pandoc 转为本地 md 文件，本地有完整内容
2. 在知识库目录页中标记为"仅本地"，提供原始飞书链接
3. 或者在知识库中创建新的 docx 节点，手动写入内容


### 补充场景（2026-05-03 标签贴膜设计成功写入 mention-doc）

`docs +update --mode overwrite` 可以成功写入 mention-doc 标签，前提是：
1. 使用 `obj_token`（不是 node_token）
2. type 设为 `file`（API 会自动转为 `docx` 显示，但不影响功能）
3. 内容格式简单（纯列表，无复杂嵌套）

之前失败的场景可能是因为 mention-doc 的 token 无效（如使用了 node_token 而非 obj_token），或者内容中混合了其他不支持的标签。**结论：mention-doc 写入是可行的，关键是使用正确的 obj_token。**
