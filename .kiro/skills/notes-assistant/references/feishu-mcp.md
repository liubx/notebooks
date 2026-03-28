# 飞书 MCP 连接与配置

## MCP 配置

lark-mcp 使用 OAuth 用户授权（`--oauth --token-mode user_access_token`）。

配置示例：

```json
{
  "lark-mcp": {
    "command": "npx",
    "args": [
      "-y",
      "@larksuiteoapi/lark-mcp",
      "mcp",
      "-a", "<APP_ID>",
      "-s", "<APP_SECRET>",
      "--oauth",
      "--token-mode", "user_access_token"
    ],
    "disabled": false,
    "autoApprove": []
  }
}
```

## 工具配置

通过 `-t` 参数控制启用哪些 API 工具，不指定时使用 `preset.default`。

工具名称格式：`{业务域}.{版本}.{资源}.{操作}`，MCP 调用时下划线替换点号（如 `mcp_lark_mcp_docx_v1_document_rawContent`）。

完整工具列表：https://github.com/larksuite/lark-openapi-mcp/blob/main/docs/reference/tool-presets/tools-zh.md

### 当前已配置的工具

- 任务：`task.v2.task.create` / `patch` / `addMembers` / `addReminders`
- 文档：`docx.v1.document.rawContent`（纯文本）、`docx.builtin.import`（Markdown 导入）、`docx.builtin.search`
- 知识库：`wiki.v2.space.getNode`、`wiki.v2.space.list`、`wiki.v2.spaceNode.list`、`wiki.v1.node.search`
- 消息：`im.v1.message.create` / `list`、`im.v1.chat.list` / `search` / `create`、`im.v1.chatMembers.get`
- 通讯录：`contact.v3.user.get` / `search` / `batchGetId`、`contact.v3.department.list`、`contact.v3.contact.me`

### 待添加的工具（文档迁移用）

- `docs.v1.content.get` — 获取云文档 Markdown 内容
- `drive.v1.exportTask.create` — 创建导出任务
- `drive.v1.exportTask.get` — 查询导出任务结果
- `drive.v1.media.batchGetTmpDownloadUrl` — 获取素材临时下载链接
- `drive.v1.file.list` — 获取文件夹中的文件清单
- `drive.v1.meta.batchQuery` — 获取文件元数据

## OAuth 登录

token 过期时有两种处理方式：

1. 直接调用任意飞书工具，返回的错误信息中包含授权 URL → 浏览器打开完成授权 → 重试
2. 终端手动登录（需先停用 MCP 中的 lark-mcp，因为共用 3000 端口）：
   ```bash
   npx -y @larksuiteoapi/lark-mcp login -a <APP_ID> -s <APP_SECRET>
   ```
   授权完成后关闭终端进程，重新启用 lark-mcp。

## 权限配置

工具对应的 API 需要在飞书开发者后台开通权限（`https://open.feishu.cn/app/<APP_ID>/security`），否则返回 99991672 错误。

常用权限分组：
- 文档：`docx:document`, `docx:document:readonly`
- 云空间：`drive:drive`, `drive:drive:readonly`, `drive:file:readonly`
- 知识库：`wiki:wiki`, `wiki:wiki:readonly`
- 任务：`task:task`, `task:task:readonly`
- 消息：`im:message`, `im:message:readonly`
- 通讯录：`contact:user.base:readonly`, `contact:department.base:readonly`

## 常见问题

- `EADDRINUSE 127.0.0.1:3000`：端口被占用，`lsof -ti:3000 | xargs kill -9`
- `user_access_token is invalid or expired`：重新 OAuth 授权
- 权限不足（99991672）：去飞书开发者后台开通对应 API 权限

## 补充工具：feishu-tools.js

lark-mcp 基于 JSON API，无法处理二进制文件操作（multipart 上传、二进制流下载）。`.kiro/skills/notes-assistant/feishu-tools.js` 补充了这些能力。

### 能力对比

| 操作 | lark-mcp | feishu-tools.js | 原因 |
|------|----------|-----------------|------|
| 上传文件到云空间 | ❌ | ✅ `upload` | multipart 上传 |
| 下载云空间文件 | ❌ | ✅ `download` | 二进制流下载 |
| 上传任务附件 | ❌ | ✅ `task-attach` | multipart 上传 |
| 下载任务附件 | ❌ | ✅ `task-download` | 临时 URL + 二进制下载 |
| 读取文档内容 | ✅ rawContent | — | JSON 响应 |
| 任务 CRUD | ✅ | — | JSON 响应 |
| 知识库操作 | ✅ | — | JSON 响应 |

### 用法

```bash
# 以下命令中 FT 为脚本路径简写
# FT=.kiro/skills/notes-assistant/feishu-tools.js

# OAuth 认证（获取/刷新 token，自动打开浏览器授权）
node .kiro/skills/notes-assistant/feishu-tools.js auth

# 上传文件到飞书云空间
node .kiro/skills/notes-assistant/feishu-tools.js upload <本地文件路径> [目标文件夹token]

# 下载飞书云空间文件（file 类型，如 .xlsx/.docx/.pdf）
node .kiro/skills/notes-assistant/feishu-tools.js download <file_token> <输出路径>

# 上传本地文件作为飞书任务附件
node .kiro/skills/notes-assistant/feishu-tools.js task-attach <task_guid> <本地文件路径>

# 下载飞书任务附件到本地
node .kiro/skills/notes-assistant/feishu-tools.js task-download <attachment_guid> <输出路径>
```

### Token 管理

- Token 保存在 `.kiro/skills/notes-assistant/feishu-token.json`，有效期 2 小时
- 脚本会自动检查过期，过期时提示重新运行 `auth`
- OAuth scope：`task:attachment:write task:task drive:drive`
- 与 lark-mcp 共用同一个飞书应用（APP_ID/APP_SECRET）

### 使用场景

1. **任务附件同步**：Obsidian 任务中的图片/文件 ↔ 飞书任务附件
   - 上传：`node .kiro/skills/notes-assistant/feishu-tools.js task-attach <guid> <图片路径>`
   - 下载：先用 lark-mcp 获取附件列表，再用 `task-download` 下载
2. **飞书迁移**：下载知识库中的 file 类型节点（.docx/.xlsx/.pdf 等）
   - 用 lark-mcp 获取文件列表和 token，再用 `download` 下载
3. **文件上传**：将本地文件上传到飞书云空间备份

### 限制

- 飞书原生文档（docx/sheet/bitable）不能直接下载，需用 lark-mcp 的 `rawContent` 获取文本，或通过导出 API 转换
- 任务描述中的图片无法通过 API 嵌入（客户端私有能力），只能作为附件上传
- `rich_description`（v1 API）仅支持文本、`[text](url)` 链接和 `<a>url</a>` 超链接，不支持图片
