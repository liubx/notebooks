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
