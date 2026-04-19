---
title: acp-link 使用方案
type: note
tags:
  - project/AI工作流
created: 2026-04-06
modified: 2026-04-06
---

# acp-link 使用方案

## 概述

使用 [acp-link](https://github.com/xufanglin/acp-link) 将飞书机器人与 kiro-cli agent 连接，实现在飞书中直接与 AI 对话。

架构分为两层：
- **个人助手**：一个机器人，私聊使用，可访问整个 vault
- **项目助手**：每个平台项目一个机器人，在项目飞书群中使用，只能访问对应项目的文件，同事也会使用

## 架构总览

```
飞书                          acp-link              kiro-cli agent
─────                        ─────                 ─────
私聊 / 个人群           →  :9800           →  master         (cwd: vault 根目录)
广州机场一期群 / 二期群  →  :9801           →  gzjc-gzjc      (cwd: Work/)
PN仓库群                →  :9802           →  pn-xxx         (cwd: Work/)
南宁机场群              →  :9803           →  nnjc-nnjc      (cwd: Work/)
上港仓储群              →  :9804           →  sg-sgcc        (cwd: Work/)
新太定位群              →  :9805           →  xt-xt          (cwd: Work/)
洛阳化工厂群            →  :9806           →  madinat-ly     (cwd: Work/)
赛峰定位群              →  :9807           →  sf-sf          (cwd: Work/)
麦钉定位群              →  :9808           →  madinat-md     (cwd: Work/)
平台更新群              →  :9809           →  platform-v27   (cwd: Work/)
测试流程群              →  :9810           →  internal-test  (cwd: Work/)
AI工作流群              →  :9811           →  internal-ai    (cwd: Work/)
```

> 注：平台项目 ID 格式为 `{公司ID}-{项目ID}`，如 `gzjc-gzjc`、`madinat-lyrydw`。
> 内部项目（平台更新、测试流程、AI工作流）没有平台 ID，用 `internal-` 或 `platform-` 前缀。
> 同一平台项目的不同期分别部署，agent 名称可加期数后缀，如 `gzjc-gzjc-phase1`、`gzjc-gzjc-phase2`。
> 以上 agent 名称和端口为示例，实际部署时按需调整。

## 设计原则

1. **项目隔离**：项目 agent 的 `cwd` 限制在具体项目期的文件夹（如 `1-Projects/Work/广州机场/`），同事无法访问个人笔记和其他项目
2. **每期独立**：同一平台项目的不同期分别部署独立的机器人和 acp-link 实例，物理隔离更安全
3. **按需部署**：不需要一次全建好，先部署个人助手和活跃项目，其他项目需要时再加
4. **统一管理**：所有 acp-link 实例用 systemd template unit 管理

## 前置条件

### 安装 kiro-cli

```bash
# 参考 kiro-cli 官方文档安装
# 安装后确认可用
kiro-cli --version
```

### 安装 acp-link

```bash
# macOS ARM
curl -L -o acp-link https://github.com/xufanglin/acp-link/releases/download/v0.2.7/acp-link-aarch64-apple-darwin
chmod +x acp-link
sudo mv acp-link /usr/local/bin/

# Linux x86_64（服务器部署）
curl -L -o acp-link https://github.com/xufanglin/acp-link/releases/download/v0.2.7/acp-link-x86_64-linux-musl
chmod +x acp-link
sudo install -m 755 acp-link /usr/local/bin/
```

### 创建飞书机器人

每个 agent 需要一个独立的飞书机器人应用：

1. 登录 [飞书开放平台](https://open.feishu.cn/app)
2. 创建企业自建应用
3. 开启机器人能力
4. 事件订阅方式选择「长连接」（WebSocket）
5. 导入 acp-link 项目中的 `feishu-permission.json` 配置权限
6. 发布应用，记录 `app_id` 和 `app_secret`
7. 将机器人拉入对应的飞书群

## 目录结构

```
~/.acp-link/
├── config-master.toml           # 个人助手
├── config-gzjc-gzjc.toml       # 广州机场
├── config-pn-xxx.toml           # PN仓库
├── config-nnjc-nnjc.toml        # 南宁机场
├── ...                          # 其他项目
├── temp/                        # 共享临时目录
└── logs/

~/.kiro/agents/
├── master.json                  # 个人助手 agent 配置
├── master.md                    # 个人助手 agent 指令
├── gzjc-gzjc.json
├── gzjc-gzjc.md
├── pn-xxx.json
├── pn-xxx.md
├── ...
└── _shared-rules.md             # 共享规则（各 agent 指令中引用）
```

## 配置详解

### 个人助手（master）

#### acp-link 配置

```toml
# ~/.acp-link/config-master.toml
log_level = "info"

[im.feishu]
app_id = "cli_master_xxx"
app_secret = "secret_master_xxx"

[backend]
cmd = "kiro-cli"
args = ["acp", "--agent", "master"]
pool_size = 4
cwd = "/path/to/vault"

[mcp]
port = 9800
```

#### kiro-cli agent 配置

```json
// ~/.kiro/agents/master.json
{
  "name": "master",
  "description": "个人笔记系统总管",
  "mcpServers": {
    "feishu": {
      "type": "streamable-http",
      "url": "http://127.0.0.1:9800/mcp"
    }
  },
  "tools": ["*"],
  "allowedTools": [],
  "resources": ["file://~/.kiro/agents/master.md"],
  "includeMcpJson": false
}
```

#### agent 指令文件

```markdown
<!-- ~/.kiro/agents/master.md -->
# 个人笔记系统总管

## 身份
你是 Obsidian 知识库的 AI 助手，管理整个 vault。

## Vault 结构（PARA）
- 0-Daily/ — 日记、周报、月报
- 1-Projects/ — 活跃项目（Work/ 和 Personal/）
- 2-Areas/ — 持续关注领域
- 3-Resources/ — 参考资料
- 4-Archives/ — 归档内容

## 能力
- 读写所有项目笔记、日记、知识库
- 跨项目查询和汇总
- 日报周报生成
- 笔记整理和归档

## 跨项目协作规则
当用户询问其他项目信息时：
1. 如果你有权限访问（你是总管，可以访问所有项目），直接回答
2. 如果用户是在项目群里问的，建议他们：
   - 去对应项目群问该项目的助手
   - 或私聊你（总管）问
3. 保持项目间的信息隔离，不主动泄露其他项目的信息给无权限的用户

## 项目清单
### Work 项目
- 广州机场（一期）— 群：oc_c796eec41c3d74befb34e2b2434447c1
- PN仓库项目 — 群：oc_69e81cfb3d3b3c2dc2830386ebaf9b74
- 南宁机场 — 群：oc_90040114460ad534f6c7525737cb9d5c
- 上港仓储管理 — 群：oc_251532efe2c85ee7ffb55dfef4b1cccd
- 新太定位 — 群：oc_69a95f0dbc2ff16982e455a3ba53f109
- 洛阳化工厂 — 群：oc_eb18ffd4120a65c95979e5bee934ccee
- 赛峰定位 — 群：oc_02a8c3b9cc699cb77bc928410a679503
- 麦钉定位 — 群：oc_84748d35d2014854793a3001a6cc448a
- 平台更新v2.7 — 群：oc_85ba568036c47e354e2ec3448372e700
- 测试流程建立 — 群：oc_4823f95f2a48c82b03880165f33efcab
- AI工作流 — 群：oc_d445189cb9f10fccbf20344569c007f8

### Personal 项目
- 笔记系统、笔记迁移、AI学习

## 文件输出
所有生成的临时文件输出到 ~/.acp-link/temp/
```

### 项目助手（以广州机场一期为例）

#### acp-link 配置

```toml
# ~/.acp-link/config-gzjc-gzjc-phase1.toml
log_level = "info"

[im.feishu]
app_id = "cli_gzjc_phase1_xxx"
app_secret = "secret_gzjc_phase1_xxx"

[backend]
cmd = "kiro-cli"
args = ["acp", "--agent", "gzjc-gzjc-phase1"]
pool_size = 2
cwd = "/path/to/vault/1-Projects/Work/广州机场"

[mcp]
port = 9801
```

> `cwd` 设为具体项目期的文件夹，物理隔离。

#### kiro-cli agent 配置

```json
// ~/.kiro/agents/gzjc-gzjc-phase1.json
{
  "name": "gzjc-gzjc-phase1",
  "description": "广州机场一期项目助手",
  "mcpServers": {
    "feishu": {
      "type": "streamable-http",
      "url": "http://127.0.0.1:9801/mcp"
    }
  },
  "tools": ["*"],
  "allowedTools": [],
  "resources": ["file://~/.kiro/agents/gzjc-gzjc-phase1.md"],
  "includeMcpJson": false
}
```

#### agent 指令文件

```markdown
<!-- ~/.kiro/agents/gzjc-gzjc-phase1.md -->
# 广州机场一期项目助手

## 身份
你是广州机场室内定位系统一期项目的 AI 助手。

## 工作目录
当前工作目录是 `1-Projects/Work/广州机场/`，只能读写此目录下的文件。

## 规则
1. 只读写广州机场一期项目的文件，不访问其他项目的文件
2. 如果用户要求访问其他项目的内容，礼貌拒绝并说明：
   - 你没有权限访问其他项目
   - 建议用户去对应项目群问该项目的助手
   - 或私聊总管助手（master）问跨项目问题
3. 专注于广州机场一期项目的问题

## 项目背景
广州机场室内定位系统部署与定制开发（一期）

## 任务格式
使用 Obsidian Tasks 插件格式，标签如 #task/进行中、#task/已完成
任务包含负责人、截止日期等信息

## 文件输出
所有生成的临时文件输出到 ~/.acp-link/temp/
```

## 新增项目期的操作步骤

当广州机场有二期工程时：

1. 在 vault 中创建新文件夹 `1-Projects/Work/广州机场二期/`
2. 创建 `0-总览.md` 和 `1-任务.md`
3. 在飞书开放平台创建新机器人应用（二期专用）
4. 创建 acp-link 配置文件 `~/.acp-link/config-gzjc-gzjc-phase2.toml`，`cwd` 设为二期文件夹
5. 创建 kiro-cli agent `gzjc-gzjc-phase2`
6. 启动 acp-link 实例：`systemctl --user enable --now acp-link@gzjc-gzjc-phase2`
7. 将二期机器人拉入二期的飞书群

二期与一期完全独立，有独立的机器人、独立的进程、独立的文件访问范围。

## 新增全新项目的操作步骤

当有一个全新的平台项目（如赛峰 `sf-sf`）需要接入时：

1. 在飞书开放平台创建新机器人应用，导入 `feishu-permission.json`
2. 创建 acp-link 配置文件 `~/.acp-link/config-sf-sf.toml`（参考上面的模板，修改 app_id/secret 和端口）
3. 创建 kiro-cli agent：
   ```bash
   kiro-cli agent create sf-sf
   ```
4. 编辑 `~/.kiro/agents/sf-sf.json` 和 `sf-sf.md`
5. 启动 acp-link 实例：
   ```bash
   systemctl --user enable --now acp-link@sf-sf
   ```
6. 将机器人拉入飞书群

## systemd 管理（Linux 服务器）

### template unit

```ini
# ~/.config/systemd/user/acp-link@.service
[Unit]
Description=ACP Link - %i agent
After=network-online.target
Wants=network-online.target

[Service]
Environment=PATH=%h/.local/bin:/usr/local/bin:/usr/bin:/bin
Environment=ACP_LINK_CONFIG=%h/.acp-link/config-%i.toml
ExecStart=/usr/local/bin/acp-link
ExecReload=/bin/kill -HUP $MAINPID
Restart=on-failure
RestartSec=5s

[Install]
WantedBy=default.target
```

### 常用命令

```bash
# 启用并启动
systemctl --user enable --now acp-link@master
systemctl --user enable --now acp-link@gzjc-gzjc

# 查看状态
systemctl --user status acp-link@gzjc-gzjc

# 查看日志
journalctl --user -u acp-link@gzjc-gzjc -f

# 热重载配置（修改 agent 指令后）
systemctl --user reload acp-link@gzjc-gzjc

# 重启
systemctl --user restart acp-link@gzjc-gzjc

# 确保服务器重启后自动拉起（只需执行一次）
sudo loginctl enable-linger $USER
```

## 当前项目清单

| 项目 | agent 名称 | 飞书群 chat_id | 端口 | 优先级 | 备注 |
|------|-----------|---------------|------|--------|------|
| 个人助手 | master | 私聊 | 9800 | ⭐ 首先部署 | 访问整个 vault |
| 广州机场一期 | gzjc-gzjc-phase1 | oc_c796eec41c3d74befb34e2b2434447c1 | 9801 | ⭐ | 平台项目 ID: gzjc-gzjc |
| PN仓库项目 | pn-xxx-phase1 | oc_69e81cfb3d3b3c2dc2830386ebaf9b74 | 9802 | ⭐ | 平台项目 ID 待确认 |
| 南宁机场 | nnjc-nnjc-phase1 | oc_90040114460ad534f6c7525737cb9d5c | 9803 | | 平台项目 ID 待确认 |
| 上港仓储管理 | sg-sgcc-phase1 | oc_251532efe2c85ee7ffb55dfef4b1cccd | 9804 | | 平台项目 ID 待确认 |
| 新太定位 | xt-xt-phase1 | oc_69a95f0dbc2ff16982e455a3ba53f109 | 9805 | | 平台项目 ID 待确认 |
| 洛阳化工厂 | madinat-ly-phase1 | oc_eb18ffd4120a65c95979e5bee934ccee | 9806 | | 平台项目 ID: madinat-lyrydw 等 |
| 赛峰定位 | sf-sf-phase1 | oc_02a8c3b9cc699cb77bc928410a679503 | 9807 | | 平台项目 ID 待确认 |
| 麦钉定位 | madinat-md-phase1 | oc_84748d35d2014854793a3001a6cc448a | 9808 | | 平台项目 ID: madinat-* 系列 |
| 平台更新v2.7 | platform-v27 | oc_85ba568036c47e354e2ec3448372e700 | 9809 | | 内部项目 |
| 测试流程建立 | internal-test | oc_4823f95f2a48c82b03880165f33efcab | 9810 | | 内部项目 |
| AI工作流 | internal-ai | oc_d445189cb9f10fccbf20344569c007f8 | 9811 | ⭐ | 内部项目 |

> 平台项目 ID 格式为 `{公司ID}-{项目ID}`，如 `gzjc-gzjc`、`madinat-lyrydw`。
> 内部项目没有平台 ID，用 `internal-` 或 `platform-` 前缀。
> 同一平台项目的不同期分别部署，agent 名称加期数后缀。

## 实施计划

### 第一阶段：跑通个人助手

1. 安装 kiro-cli
2. 创建第一个飞书机器人（个人助手）
3. 部署 acp-link，配置 master agent
4. 验证私聊对话正常

### 第二阶段：部署 1-2 个活跃项目

5. 为广州机场创建独立机器人和 agent
6. 验证项目群对话正常，确认隔离有效（同事看不到其他项目内容）
7. 为 PN 仓库或 AI 工作流再部署一个

### 第三阶段：按需扩展

8. 根据实际需要，逐步为其他项目创建机器人和 agent
9. 不活跃的项目暂不部署

## 注意事项

- 每个 acp-link 实例的 MCP port 不能冲突
- 每个飞书机器人需要单独创建应用（可复用 `feishu-permission.json` 快速配置权限）
- 项目 agent 的 `cwd` 设为具体项目期的文件夹，确保同事只能访问该项目期的内容
- 同一平台项目的不同期分别部署，有独立的机器人、独立的进程、独立的文件访问范围
- 飞书 WebSocket 长连接是按应用维度的，同一个 app_id 只能有一个 acp-link 实例连接
- 定时任务（cron）可以在任意 agent 的配置中添加，比如在项目 agent 中配置每日任务汇报

## 附录：配置模板文件

### 个人助手配置模板

```toml
# ~/.acp-link/config-master.toml
log_level = "info"

[im.feishu]
app_id = "cli_xxx"
app_secret = "xxx"

[backend]
cmd = "kiro-cli"
args = ["acp", "--agent", "master"]
pool_size = 4
cwd = "/path/to/vault"

[mcp]
port = 9800
```

### 项目助手配置模板

```toml
# ~/.acp-link/config-{平台ID}-{项目ID}-phase{期数}.toml
log_level = "info"

[im.feishu]
app_id = "cli_{项目标识}_xxx"
app_secret = "xxx"

[backend]
cmd = "kiro-cli"
args = ["acp", "--agent", "{平台ID}-{项目ID}-phase{期数}"]
pool_size = 2
cwd = "/path/to/vault/1-Projects/Work/{项目文件夹}"

[mcp]
port = {端口号}
```

### 内部项目配置模板

```toml
# ~/.acp-link/config-internal-{项目名}.toml
log_level = "info"

[im.feishu]
app_id = "cli_internal_{项目名}_xxx"
app_secret = "xxx"

[backend]
cmd = "kiro-cli"
args = ["acp", "--agent", "internal-{项目名}"]
pool_size = 2
cwd = "/path/to/vault/1-Projects/Work/{项目文件夹}"

[mcp]
port = {端口号}
```

### kiro-cli agent 配置模板

```json
// ~/.kiro/agents/{agent名称}.json
{
  "name": "{agent名称}",
  "description": "{项目描述}",
  "mcpServers": {
    "feishu": {
      "type": "streamable-http",
      "url": "http://127.0.0.1:{端口号}/mcp"
    }
  },
  "tools": ["*"],
  "allowedTools": [],
  "resources": ["file://~/.kiro/agents/{agent名称}.md"],
  "includeMcpJson": false
}
```

### agent 指令文件模板

```markdown
# {项目名称}助手

## 身份
你是{项目名称}项目的 AI 助手。

## 工作目录
当前工作目录是 `1-Projects/Work/{项目文件夹}/`，只能读写此目录下的文件。

## 规则
1. 只读写{项目名称}项目的文件，不访问其他项目的文件
2. 如果用户要求访问其他项目的内容，礼貌拒绝并说明：
   - 你没有权限访问其他项目
   - 建议用户去对应项目群问该项目的助手
   - 或私聊总管助手（master）问跨项目问题
3. 专注于{项目名称}项目的问题

## 项目背景
{项目背景描述}

## 任务格式
使用 Obsidian Tasks 插件格式，标签如 #task/进行中、#task/已完成
任务包含负责人、截止日期等信息

## 文件输出
所有生成的临时文件输出到 ~/.acp-link/temp/
```

## 附录：常用命令速查

```bash
# 创建 kiro-cli agent
kiro-cli agent create {agent名称}

# 启动 acp-link 实例
systemctl --user enable --now acp-link@{agent名称}

# 查看日志
journalctl --user -u acp-link@{agent名称} -f

# 热重载配置
systemctl --user reload acp-link@{agent名称}

# 停止实例
systemctl --user stop acp-link@{agent名称}

# 查看所有运行中的实例
systemctl --user list-units 'acp-link@*'
```

## 附录：飞书机器人权限配置

使用 acp-link 项目中的 `feishu-permission.json` 快速配置权限：

1. 在飞书开放平台创建应用
2. 进入「权限管理」页面
3. 点击「导入权限配置」
4. 上传 `feishu-permission.json`
5. 确认并保存

此权限配置包含：
- 接收消息与事件
- 发送消息
- 获取群组信息
- 获取用户信息
- 云文档读写权限
- 文件上传下载权限

## 附录：故障排查

### 连接失败
- 检查飞书应用的 `app_id` 和 `app_secret` 是否正确
- 确认事件订阅方式为「长连接」
- 检查网络连接，确保能访问飞书服务器

### 消息收不到
- 确认机器人已加入飞书群
- 检查 acp-link 日志：`journalctl --user -u acp-link@{agent名称} -f`
- 确认飞书应用已发布

### agent 无法读写文件
- 检查 `cwd` 路径是否正确
- 确认 kiro-cli 有对应目录的读写权限
- 检查 agent 指令文件中的路径规则

### 端口冲突
- 每个 acp-link 实例的 MCP port 必须唯一
- 检查端口是否被其他进程占用：`lsof -i :{端口号}`

## 更新记录

- 2026-04-06：创建方案文档，采用每期独立部署架构
- 2026-04-06：调整项目 agent 的 `cwd` 为具体项目期文件夹，确保物理隔离
## 附录：协作流程示例

### 场景：广州机场群里问 PN 仓库进度

**用户**（在广州机场群）：@广州机场助手 PN 仓库的进度怎么样了？

**广州机场助手**：抱歉，我只有权限访问广州机场项目的文件。关于 PN 仓库的进度，你可以：
1. 去 PN 仓库项目群问 @PN仓库助手
2. 或私聊 @总管助手 问跨项目问题

**用户**：好的，我私聊总管问。

**用户**（私聊总管）：PN 仓库的进度怎么样了？

**总管助手**：PN 仓库项目目前有 3 个进行中任务，2 个已完成任务。详细情况如下：
（读取 PN 仓库的 1-任务.md 并总结）

### 场景：总管汇总所有项目进度

**用户**（私聊总管）：帮我汇总一下所有项目的本周进展。

**总管助手**：
1. 读取每个项目的 1-任务.md
2. 统计各项目的任务完成情况
3. 生成汇总报告

### 场景：项目间信息需要同步

**用户**（在广州机场群）：@广州机场助手 平台更新 v2.7 的新功能对我们有影响吗？

**广州机场助手**：这个问题涉及平台更新项目，我没有权限查看。建议：
1. 去平台更新群问 @平台更新助手
2. 或私聊 @总管助手 问

这样既保持了项目间的隔离，又通过总管 agent 提供了跨项目查询的通道。