---
inclusion: manual
---

# 飞书 MCP 连接指南

当需要连接飞书（读写文档、知识库、对话、任务等）时，按以下步骤操作。

## 前置条件

- 飞书开发者后台已创建应用，获取 App ID 和 App Secret
- 应用安全设置中已配置重定向 URL：`http://localhost:3000/callback`
  - 配置地址：https://open.feishu.cn/app/<APP_ID>/safe
- 应用已开通所需的 API 权限（文档、知识库、消息等）

## MCP 配置

在 MCP 客户端的配置文件中添加 lark-mcp：

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

## OAuth 登录流程

lark-mcp 使用 OAuth 用户授权，token 会过期需要重新授权。

### 方式一：通过 MCP 调用触发（推荐）

1. 直接调用任意飞书 MCP 工具
2. 如果 token 过期，返回的错误信息中包含授权 URL
3. 在浏览器打开该 URL 完成授权
4. 再次调用即可成功

### 方式二：终端手动登录

⚠️ 注意：终端 login 和 MCP server 共用 3000 端口，不能同时运行。需要先停用 MCP 中的 lark-mcp 再执行登录。

1. 停用 MCP 客户端中的 lark-mcp 连接
2. 终端执行：
   ```bash
   npx -y @larksuiteoapi/lark-mcp login -a <APP_ID> -s <APP_SECRET>
   ```
3. 浏览器打开输出的授权 URL，完成飞书授权
4. 看到 `✅ Successfully logged in` 后，关闭终端进程
5. 重新启用 MCP 客户端中的 lark-mcp

## 工具权限配置

lark-mcp 通过 `-t` 参数控制启用哪些 API 工具。不指定时使用 `preset.default` 默认集合。

### 查看可用工具

完整工具列表见：https://github.com/larksuite/lark-openapi-mcp/blob/main/docs/reference/tool-presets/tools-zh.md

工具名称格式为 `{业务域}.{版本}.{资源}.{操作}`，例如：
- `docx.v1.document.rawContent` — 获取文档纯文本
- `docs.v1.content.get` — 获取云文档 Markdown 内容
- `drive.v1.exportTask.create` — 创建导出任务
- `drive.v1.media.batchGetTmpDownloadUrl` — 获取素材临时下载链接

### 配置方式

在 `-t` 参数中用逗号分隔列出需要的工具：

```json
"-t", "task.v2.task.create,docx.v1.document.rawContent,docs.v1.content.get,drive.v1.exportTask.create"
```

也可以使用预设：
- `preset.default` — 默认工具集
- 具体工具名 — 按需添加

### 飞书开发者后台权限

工具对应的 API 需要在飞书开发者后台开通权限，否则调用会返回 99991672 错误。

配置地址：`https://open.feishu.cn/app/<APP_ID>/security`

常用权限分组：
- 文档：`docx:document`, `docx:document:readonly`
- 云空间：`drive:drive`, `drive:drive:readonly`, `drive:file:readonly`
- 知识库：`wiki:wiki`, `wiki:wiki:readonly`
- 任务：`task:task`, `task:task:readonly`
- 消息：`im:message`, `im:message:readonly`
- 通讯录：`contact:user.base:readonly`, `contact:department.base:readonly`

### 当前配置的工具

```
task.v2.task.create, task.v2.task.patch, task.v2.task.addMembers,
task.v2.task.addReminders, docx.v1.document.rawContent,
docx.builtin.import, docx.builtin.search,
wiki.v2.space.getNode, wiki.v1.node.search,
im.v1.chat.create, im.v1.chat.list, im.v1.chat.search,
im.v1.chatMembers.get, im.v1.message.create, im.v1.message.list,
contact.v3.user.batchGetId, contact.v3.user.get, contact.v3.user.search,
contact.v3.department.list, contact.v3.contact.me
```

### 待添加的工具（文档迁移用）

```
docs.v1.content.get                        — 获取云文档 Markdown 内容
drive.v1.exportTask.create                 — 创建导出任务（docx/sheet/bitable → Word/Excel/PDF）
drive.v1.exportTask.get                    — 查询导出任务结果
drive.v1.media.batchGetTmpDownloadUrl      — 获取素材临时下载链接
drive.v1.file.list                         — 获取文件夹中的文件清单
drive.v1.meta.batchQuery                   — 获取文件元数据
```

## 常见问题

- `EADDRINUSE: address already in use 127.0.0.1:3000`：端口被占用，用 `lsof -ti:3000 | xargs kill -9` 释放
- `user_access_token is invalid or expired`：需要重新 OAuth 授权
- 权限不足（99991672）：去飞书开发者后台开通对应 API 权限，配置地址见上方
