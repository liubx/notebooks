---
name: lark-assistant
version: 1.1.0
description: "飞书全能助手：统一调度 lark-cli 和 lark-scripts.js，覆盖飞书全部业务域。当用户提到飞书、Lark、任务、文档、日历、消息、邮件、审批、招聘、人事、考勤、OKR、绩效、薪酬、门禁、词典、搜索等飞书相关功能时使用。优先使用 lark-cli Shortcut（高级封装），其次 lark-cli 原生 API，再次 lark-cli api 裸调任意 OpenAPI，最后 lark-scripts.js 处理 multipart 上传。"
metadata:
  requires:
    bins: ["lark-cli"]
---

# 飞书全能助手（Lark Assistant）

## 调用优先级（核心规则）

```
1. lark-cli Shortcut     — 最优体验，自动分页/格式转换/Wiki 解析
2. lark-cli 原生 API     — Shortcut 不覆盖但 lark-cli 有注册的 resource.method
3. lark-cli api 裸调     — 任意飞书 OpenAPI，支持 user/bot 身份，自动分页
4. lark-scripts.js       — multipart 文件上传（任务附件），唯一不可替代场景
```

### 为什么不用 lark-mcp？

经实测验证，`lark-cli api` 可以调用任意飞书 OpenAPI（包括审批、人事、招聘等），且支持 user/bot 身份切换。lark-mcp 只有 tenant 身份，功能上是 lark-cli api 的子集。lark-mcp 配置保留在 `mcp.json` 中但默认 disabled，需要时可启用。

## lark-cli 优先的业务域

这些域 lark-cli 有高级封装 Shortcut：

| 业务域 | lark-cli skill | 关键优势 |
|--------|---------------|----------|
| 任务 | lark-task | `+get-my-tasks` 搜索、`+complete`/`+reopen` |
| 文档 | lark-doc | `+fetch` 返回 Markdown、`+update` 编辑、`+media-insert` 插图 |
| 云空间 | lark-drive | `+upload`/`+download` 文件传输、`+add-comment` 评论 |
| 电子表格 | lark-sheets | `+read`/`+write`/`+append`/`+find`/`+export` |
| 多维表格 | lark-base | `+data-query` 聚合分析、`+record-*`、`+workflow-*` |
| 即时通讯 | lark-im | `+messages-send`/`+messages-search`/`+messages-resources-download` |
| 日历 | lark-calendar | `+agenda`/`+create`/`+freebusy`/`+suggestion` |
| 通讯录 | lark-contact | `+search-user`/`+get-user` |
| 知识库 | lark-wiki | `wiki spaces get_node` |
| 邮箱 | lark-mail | `+send`/`+reply`/`+forward`/`+triage`/`+watch` |
| 视频会议 | lark-vc | `+search`/`+notes` |
| 妙记 | lark-minutes | `minutes get` |
| 事件订阅 | lark-event | `+subscribe`（WebSocket） |
| 画板 | lark-whiteboard | whiteboard-cli + `+whiteboard-update` |

## lark-cli api 裸调的场景

lark-cli 没有 Shortcut 或原生 API 封装时，用 `lark-cli api` 裸调：

```bash
# 基本格式
lark-cli api <METHOD> <PATH> [--as user|bot] [--params '{}'] [--data '{}'] [--page-all]

# 知识空间列表
lark-cli api GET /open-apis/wiki/v2/spaces --as user --page-all

# 知识空间子节点
lark-cli api GET /open-apis/wiki/v2/spaces/<space_id>/nodes --as user --page-all

# 任务自定义字段
lark-cli api GET /open-apis/task/v2/custom_fields --as user

# 任务分组
lark-cli api GET /open-apis/task/v2/sections --as user --params '{"resource_type":"my_tasks"}'

# 审批实例
lark-cli api GET /open-apis/approval/v4/instances --as bot --params '{"approval_code":"xxx"}'

# 导出文档为 PDF
lark-cli api POST /open-apis/drive/v1/export_tasks --as user --data '{"file_extension":"pdf","token":"xxx","type":"docx"}'
```

### 关键参数

| 参数 | 说明 |
|------|------|
| `--as user` | 用户身份（个人资源：任务、日历、邮箱、知识空间等） |
| `--as bot` | 应用身份（管理类操作：审批、人事、通讯录管理等） |
| `--page-all` | 自动翻页获取全部数据 |
| `--params '{}'` | URL 查询参数 |
| `--data '{}'` | 请求体 JSON |
| `-o <file>` | 二进制响应输出到文件 |

### 调用前必查文档

`lark-cli api` 裸调时，参数字段名必须与飞书官方文档完全一致（如 `tasklist_guid` 而非 `tasklist`）。不确定时，先用 `lark-openapi-explorer` skill 查阅官方文档：

1. 从 `https://open.feishu.cn/llms.txt` 定位模块
2. 从模块文档定位具体 API
3. 获取完整参数规范后再调用

字段名错误会导致 lark-cli api 静默失败（exit 1，无输出），容易误判为 bug。

## 补充工具：lark-scripts.js

`lark-cli api` 不支持 multipart/form-data（文件上传），通过 `lark-scripts.js` 补充。

唯一必须使用的场景：任务附件上传。

Token 来源：直接读取 lark-cli 的加密存储（macOS Keychain master key + AES-256-GCM 解密），无需单独认证。前提是已通过 `lark-cli auth login` 完成授权且 scope 包含 `task:attachment:write`。

```bash
FT=.kiro/skills/lark-assistant/lark-scripts.js

node $FT task-attach <task_guid> <文件路径>       # 上传任务附件
node $FT task-download <attach_guid> <输出路径>   # 下载任务附件（备用）
```

### Token 读取机制

1. 从 `~/.lark-cli/config.json` 读取 appId 和 userOpenId
2. 从 macOS Keychain 读取 master key（service=`lark-cli`, account=`master.key`）
3. 解密 `~/Library/Application Support/lark-cli/<appId>_<userOpenId>.enc`（AES-256-GCM）
4. 从解密后的 JSON 中提取 `accessToken`
5. token 过期时自动触发 `lark-cli auth status --verify` 刷新

## 工具选择速查

| 操作 | 工具 | 说明 |
|------|------|------|
| 日常任务/文档/IM/日历 | lark-cli Shortcut | 最优体验 |
| 上传/下载文件 | `lark-cli drive +upload/+download` | 原生支持 |
| 知识空间列表/节点 | `lark-cli api --as user` | lark-cli 没封装 |
| 任务自定义字段/分组/依赖 | `lark-cli api --as user` | lark-cli 没封装 |
| 审批/人事/招聘/考勤 | `lark-cli api --as bot` | lark-cli 没封装 |
| 上传任务附件 | `lark-scripts.js task-attach` | multipart，唯一方式 |

## 前置依赖

```bash
lark-cli config show             # 查看配置
lark-cli auth login --recommend  # token 过期时重新登录
```

详见 `.kiro/skills/lark-shared/SKILL.md`。

## 参考文档

- 各 lark-cli skill 详细文档：`.kiro/skills/lark-*/SKILL.md`
- 工具对比和实测记录：`.kiro/skills/lark-assistant/references/lark-mcp-vs-cli.md`
- lark-cli 认证和权限：`.kiro/skills/lark-shared/SKILL.md`
- lark-scripts.js 源码：`.kiro/skills/lark-assistant/lark-scripts.js`
