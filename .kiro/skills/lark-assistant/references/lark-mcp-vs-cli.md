# lark-cli vs lark-mcp vs lark-cli api 功能对比

> 更新日期：2026-03-29

## 三层工具架构

| 维度 | lark-cli（Shortcut + 原生 API） | lark-mcp（MCP Server） | lark-cli api（裸调 OpenAPI） |
|------|-------------------------------|----------------------|---------------------------|
| 调用方式 | Shell 命令 | MCP 协议，AI 直接调用 | Shell 命令 |
| 接口风格 | 高级封装 Shortcut + 原生 API | 原始 OpenAPI 1:1 映射 | 原始 OpenAPI，手动拼路径和参数 |
| 认证身份 | user / bot 灵活切换 | tenant_access_token（应用身份） | user / bot 灵活切换 |
| 文件上传/下载 | ✅ 原生支持 | ❌ 不支持 | ❌ 不支持（二进制流） |
| 文档编辑 | ✅ 追加/覆盖/替换/插入/删除 | ❌ 只能导入和读取 | ✅ 可以（需手动构造块操作） |
| 接口覆盖 | ~200（15 个业务域） | ~1000+（按 `-t` 配置启用） | 全部飞书 OpenAPI |
| 自动分页 | ✅ Shortcut 内置 | ❌ 需手动翻页 | ✅ `--page-all` |
| 适用场景 | 日常操作首选 | lark-cli 不覆盖的业务域 | 需要 user 身份 + lark-cli 没封装的 API |

## 调用优先级

```
1. lark-cli Shortcut     — 最优体验，自动分页/格式转换/Wiki 解析
2. lark-cli 原生 API     — Shortcut 不覆盖但 lark-cli 有注册的 resource.method
3. lark-cli api 裸调     — 需要 user 身份 + lark-cli 没注册的 API（如 wiki spaces list）
4. lark-mcp              — tenant 身份即可 + lark-cli 完全没覆盖的业务域
```

## 身份与权限差异（关键）

| 场景 | lark-cli | lark-mcp | lark-cli api |
|------|---------|---------|-------------|
| 用户个人资源（任务、日历、邮箱、云空间） | ✅ `--as user` | ❌ tenant 看不到 | ✅ `--as user` |
| 知识空间列表 | ❌ 没有 list 命令 | ❌ tenant 返回空 | ✅ `--as user` |
| 管理类操作（审批、人事、招聘） | ❌ 没有封装 | ✅ tenant 即可 | ✅ `--as bot` |
| 发消息（bot 身份） | ✅ `--as bot` | ✅ tenant 即可 | ✅ `--as bot` |
| 通讯录查询 | ✅ `+search-user` | ✅ tenant 即可 | ✅ 都行 |

## lark-cli api 裸调用法

```bash
# 基本格式
lark-cli api <METHOD> <PATH> [--as user|bot] [--params '{}'] [--data '{}']

# 示例：列出知识空间（需要 user 身份）
lark-cli api GET /open-apis/wiki/v2/spaces --as user --page-all

# 示例：获取知识空间子节点
lark-cli api GET /open-apis/wiki/v2/spaces/7065147197469458433/nodes --as user --page-all

# 示例：创建审批实例（bot 身份）
lark-cli api POST /open-apis/approval/v4/instances --as bot --data '{"approval_code":"xxx","form":"[...]"}'

# 示例：导出文档为 PDF
lark-cli api POST /open-apis/drive/v1/export_tasks --as user --data '{"file_extension":"pdf","token":"xxx","type":"docx"}'

# 查看参数结构（先 schema 再调用）
lark-cli schema wiki.spaces.list  # 如果 lark-cli 有注册
# 没注册的 API 需要查飞书开放平台文档
```

### lark-cli api 关键参数

| 参数 | 说明 |
|------|------|
| `--as user` | 用户身份（访问个人资源） |
| `--as bot` | 应用身份（管理类操作） |
| `--page-all` | 自动翻页获取全部数据 |
| `--page-size N` | 每页数量 |
| `--params '{}'` | URL 查询参数 |
| `--data '{}'` | 请求体 JSON |
| `--format json|table|csv` | 输出格式 |
| `-o <file>` | 二进制响应输出到文件 |

## 各工具独有能力

### lark-cli 独有
- 文件上传/下载（`drive +upload/+download`）
- 文档编辑（`docs +update`）
- 文档内图片插入/下载（`docs +media-insert/+media-download`）
- 数据聚合查询（`base +data-query`）
- 邮件回复/转发（`mail +reply/+forward`）
- 事件 WebSocket 监听（`event +subscribe`）
- 画板操作（`whiteboard-cli`）
- 时间推荐（`calendar +suggestion`）
- 记录历史（`base +record-history-list`）
- 附件上传到多维表格（`base +record-upload-attachment`）

### lark-cli api 独有场景
需要 user 身份 + lark-cli 没封装的 API：
- 知识空间列表（`GET /open-apis/wiki/v2/spaces`）
- 知识空间子节点列表（`GET /open-apis/wiki/v2/spaces/:id/nodes`）
- 知识空间创建/成员管理
- 文档导出任务（`POST /open-apis/drive/v1/export_tasks`）
- 文件版本管理

### lark-mcp 独有业务域
lark-cli 完全没有覆盖，且 tenant_access_token 可用：

| 业务域 | 工具前缀 | 说明 |
|--------|---------|------|
| 审批 | `approval.v4.*` | 审批定义、实例、任务 |
| 考勤 | `attendance.v1.*` | 考勤组、班次、打卡、排班 |
| 飞书人事 | `corehr.v1/v2.*` | 员工、部门、职级、合同、异动、离职 |
| 招聘 | `hire.v1.*` | 职位、投递、面试、Offer |
| 绩效 | `performance.v1/v2.*` | 绩效周期、评估、指标 |
| 薪酬 | `compensation/payroll.v1.*` | 薪资档案、发薪 |
| OKR | `okr.v1.*` | 目标管理 |
| 智能门禁 | `acs.v1.*` | 门禁设备、记录 |
| 词典 | `baike/lingo.v1.*` | 企业词典 |
| 卡片 | `cardkit.v1.*` | 卡片实体 |
| 搜索连接器 | `search.v2.*` | 自定义数据源 |
| AI 助手 | `aily.v1.*` | Aily 会话和技能 |
| 低代码 | `apaas.v1.*` | 飞书应用引擎 |
| 应用管理 | `application.v5/v6.*` | 应用信息、版本 |
| 翻译 | `translation.v1.*` | 文本翻译和语种识别 |
| OCR | `optical_char_recognition.v1.*` | 图片文字识别 |
| 语音识别 | `speech_to_text.v1.*` | 语音转文字 |

## 按业务域详细对比

### IM（即时通讯）
- 共有：发送/获取/回复消息、创建群、搜索群、群成员、表情回复、Pin
- lark-cli 独有：下载消息中的图片/文件
- lark-mcp 独有：群菜单、群标签页、群置顶、批量消息、消息流卡片

### 文档（Docs）
- 共有：获取内容、创建、导入、搜索
- lark-cli 独有：编辑文档、插入/下载图片、画板操作
- lark-mcp 独有：块级操作（创建/更新/删除块）、群公告操作

### 云空间（Drive）
- 共有：文件复制/移动/删除、元数据、评论、权限
- lark-cli 独有：文件上传/下载
- lark-mcp 独有：导出/导入任务、文件版本管理、素材临时下载链接
- lark-cli api 补充：导出任务（`POST /open-apis/drive/v1/export_tasks --as user`）

### 电子表格（Sheets）
- lark-cli 独有：读取/写入/追加单元格、导出
- lark-mcp 独有：浮动图片管理
- 共有：创建表格、查找单元格、筛选管理

### 多维表格（Base）
- 共有：表/字段/记录/视图 CRUD、仪表盘、自动化流程、角色
- lark-cli 独有：数据聚合查询、记录历史、附件上传
- lark-mcp 独有：（基本持平）

### 任务（Task）
- 共有：CRUD、成员、提醒、评论、清单、子任务
- lark-cli 独有：`+get-my-tasks` 搜索、`+complete`/`+reopen`
- lark-mcp 独有：自定义字段、分组、依赖、附件、动态订阅

### 日历（Calendar）
- 共有：日程 CRUD、忙闲查询、参会人管理
- lark-cli 独有：时间推荐（`+suggestion`）
- lark-mcp 独有：请假日程、Exchange 绑定

### 通讯录（Contact）
- 共有：搜索用户、获取用户信息
- lark-mcp 独有：部门 CRUD、用户组、职级/序列/职务、创建/删除用户

### 知识库（Wiki）
- lark-cli：只有 `get_node`（获取单个节点信息）
- lark-mcp（tenant）：空间列表返回空（需要应用被加为成员）
- lark-cli api（user）：✅ 空间列表、子节点列表、创建/移动/复制节点、成员管理

### 邮箱（Mail）
- 共有：发送/读取/搜索
- lark-cli 独有：回复/转发、草稿编辑、收信事件监听
- lark-mcp 独有：邮件组管理、公共邮箱管理

### 视频会议（VC）
- lark-cli 独有：搜索会议记录、获取纪要
- lark-mcp 独有：预约/管理会议、会议室管理、录制管理、会议报告

## 实测结论（2026-03-29）

| 测试场景 | 工具 | 结果 |
|---------|------|------|
| 列出知识空间 | lark-mcp（tenant） | ❌ 返回空（应用未加为空间成员） |
| 列出知识空间 | lark-cli api（user） | ✅ 返回 3 个空间 |
| 列出知识空间 | lark-cli | ❌ 没有 list 命令 |
| 任务分组（sections） | lark-cli api（user，无 scope） | ❌ 静默失败（exit 1，无输出） |
| 任务分组（sections） | lark-cli api（user，有 scope） | ✅ 正常返回 |
| 任务分组（sections） | lark-mcp（tenant，有 scope） | ✅ 正常返回 |
| 任务自定义字段 | lark-cli api（user，无 scope） | ❌ 静默失败 |
| 任务自定义字段 | lark-cli api（user，有 scope） | ✅ 正常返回 |
| 任务清单列表 | lark-cli api（user） | ✅ 正常返回 |
| 审批实例（dry-run） | lark-cli api（bot） | ✅ 请求构造正确 |

关键发现：
- lark-cli api 缺 user scope 时会静默失败（exit 1，无任何输出），容易误判为 bug
- 授权对应 scope 后 lark-cli api 完全正常
- lark-cli api 可以覆盖 lark-mcp 的所有功能，且额外支持 user 身份
- lark-mcp 的唯一优势是工具名自动发现（不用拼 API 路径），但功能上是 lark-cli api 的子集

最终决策：统一使用 lark-cli（Shortcut + 原生 API + api 裸调）+ lark-scripts.js（multipart 上传）。lark-mcp 保留配置但默认 disabled。
