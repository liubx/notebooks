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

## 常见问题

- `EADDRINUSE: address already in use 127.0.0.1:3000`：端口被占用，用 `lsof -ti:3000 | xargs kill -9` 释放
- `user_access_token is invalid or expired`：需要重新 OAuth 授权
- 权限不足（99991672）：去飞书开发者后台开通对应 API 权限
