# 任务格式与飞书同步规则

任务格式规范、飞书同步决策逻辑、飞书任务清单同步规则的统一参考文档。

---

## 一、任务行格式规范

### 统一格式

有外部链接（飞书/文章/任何 URL）：
```
- [ ] [任务标题](外部链接) [[路径#^id|↗️]] 👤负责人 🛫 开始 📅 截止 ➕ 创建 优先级 #tags ^task-id
```

没有外部链接：
```
- [ ] 任务标题 [[路径#^id|↗️]] 👤负责人 🛫 开始 📅 截止 ➕ 创建 优先级 #tags ^task-id
```

### 字段说明

| 字段 | 格式 | 必填 | 说明 |
|------|------|------|------|
| 标题 | 纯文本或 `[标题](url)` | ✅ | 有外部链接时做成超链接 |
| ↗️ backlink | `[[路径#^task-id\|↗️]]` | ✅ | 精确定位到任务行 |
| 👤负责人 | `👤姓名` | 可选 | 飞书同步的任务带负责人 |
| 🛫 开始日期 | `🛫 YYYY-MM-DD` | ✅ | 飞书有 start 就用，没有则用创建时间 |
| 📅 截止日期 | `📅 YYYY-MM-DD` | 建议填 | 飞书有 due 就用，没有则评估一个截止时间，除非特意留空 |
| ➕ 创建日期 | `➕ YYYY-MM-DD` | ✅ | 飞书 created_at 必有值，本地必填 |
| ✅ 完成日期 | `✅ YYYY-MM-DD` | 自动 | 完成时自动添加，未完成不填 |
| 优先级 | 🔺高 🔼中 🔽低 | 可选 | Tasks 插件原生优先级 |
| #tags | `#task/类型 #project/名称` | ✅ | 任务分类和项目归属 |
| ^task-id | `^task-xxx` | ✅ | block reference ID |

### 字段顺序

标题 → 外部链接（如有）→ ↗️ backlink → 👤负责人 → 🛫 → 📅 → ➕ → 优先级 → #tags → ^task-id

### 任务类型 Tag

- `#task/work` — 工作任务
- `#task/study` — 学习任务
- `#task/personal` — 个人任务

### 状态 Tag（与飞书自定义字段同步）

- 无 status tag — 默认状态（收集箱）
- `#status/doing` — 进行中
- `#status/testing` — 测试中
- `#status/waiting` — 等待中
- `#status/done` — 已完成
- `#status/cancelled` — 已取消

### 任务补充信息

用缩进子列表补充详情，Tasks 插件不会解析缩进行：

```markdown
- [ ] 写接口文档 📅 2026-03-28 #task/work #project/xxx ^task-api-doc
  - 用户认证接口
  - 数据查询接口
  - 参考：https://example.com/api-spec
```

---

## 二、飞书同步决策逻辑

### Never Sync（私有内容）

自动判定为私有，不同步也不询问：

1. 含 `#private` tag
2. 含敏感关键词：密码, 账号, 身份证, 银行卡, 工资, 薪资, 隐私, 私密, 个人信息, 家庭住址
3. 文件在 `1-Projects/Personal/` 下
4. 含 `#task/personal` tag
5. 含生活类 tag：`#area/生活`, `#area/健康`, `#area/财务`, `#area/家庭`, `#area/个人`
6. 含个人项目关键词：个人项目, 买房, 装修, 家庭

### Auto Sync（工作内容）

自动判定为工作内容，直接同步：

1. 含 `#task/work` tag
2. 含工作项目 tag `#project/xxx`（排除个人项目关键词）
3. 含工作领域 tag `#area/xxx`（排除生活类关键词）
4. 含技术决策关键词：技术决策, 架构决策, 决策记录
5. 含 ≥2 个工作关键词

工作关键词：会议, 团队, 协作, 项目, 需求, 开发, 测试, 上线, 部署, 评审, 汇报, 周报, 月报, 技术方案, 架构, 设计文档, 接口文档, 客户, 产品, 运营, 市场

### 需要询问用户

以上规则都不明确匹配时询问："这个内容是否需要同步到飞书？"

### Sync Tags

| Tag | 含义 |
|-----|------|
| `#sync/feishu` | 待同步（通用） |
| `#sync/feishu-task` | 待同步任务 |
| `#sync/feishu-doc` | 待同步文档 |
| `#sync/feishu-wiki` | 待同步知识库 |
| `#synced/feishu` | 已同步 |
| `#sync-error/feishu` | 同步失败 |
| `#sync-conflict/feishu` | 同步冲突 |
| `#private` | 私有，永不同步 |

---

## 三、飞书任务清单同步规则

### 分组映射

本地任务文件中的 `# 标题` 与飞书清单的 section 一一对应，通过 HTML 注释标记关联：

```markdown
# 分组名称
<!-- feishu_section: section-guid -->
```

#### 分组类型

| 类型 | 说明 | 示例 |
|------|------|------|
| 飞书同步分组 | 有 `feishu_section` 注释，与飞书 section 对应 | `# BUG 修复`、`# 围栏功能` |
| 纯本地分组 | 无 `feishu_section` 注释，不参与同步 | `# 今日重点`、`# v2.7 上线` |
| 默认分组 | 注释中标注 `(默认分组)`，对应飞书清单的默认 section | `# 默认分组` |

#### 分组规则

1. 飞书清单中每个自定义 section → 本地一个 `# 标题` + `feishu_section` 注释
2. 飞书默认分组 → 本地 `# 默认分组`
3. 本地可以有不带 `feishu_section` 的纯本地分组，同步时跳过
4. 同步时根据任务的 `tasklists[].section_guid` 确定归属分组
5. 如果飞书新增了 section，本地也要新增对应的 `# 标题`
6. 分组顺序：纯本地分组在前，飞书同步分组在后，默认分组放最后

### 飞书同步任务格式

飞书同步任务的标题做成超链接：

```markdown
- [ ] [任务标题](飞书链接) [[文件路径#^task-id|↗️]] 👤负责人 🛫 YYYY-MM-DD 📅 YYYY-MM-DD 优先级 #task/work #project/项目名 ^task-id
  可选的补充说明
```

#### 飞书字段映射

| 字段 | 来源 | 说明 |
|------|------|------|
| 👤负责人 | members 中 role=assignee | 通过 open_id 查用户映射表转姓名 |
| 🛫 开始日期 | start.timestamp | 仅在飞书有设置时显示 |
| 📅 截止日期 | due.timestamp | 仅在飞书有设置时显示 |
| 优先级 | custom_fields 优先级 | ⏫ 紧急 / 🔼 高 / 🔽 低 |
| [🔗] | task.url | 飞书任务详情链接 |
| ^block-id | 本地自定义 | Obsidian block reference |

#### Tag 规则

- 所有飞书同步的工作任务必须带 `#task/work`
- 如果任务文件的 frontmatter 有 `project/xxx` tag，任务行也要带 `#project/xxx`
- 如果任务文件属于 `2-Areas/Work/`（综合任务），用 `#type/xxx` 代替 `#project/xxx`

### 同步流程

1. 获取飞书清单的所有分组（section_list）
2. 获取飞书清单的所有任务（包括已完成）
3. 读取本地任务文件，提取已有任务的 guid（从飞书链接中解析）
4. 确定"旧任务分界线"：本地任务文件中第一个飞书任务的创建时间（`➕` 日期）
5. 对比差异：
   - 飞书有、本地无、未完成 → 新增到本地对应分组
   - 飞书有、本地无、已完成、完成时间 >= 分界线 → 新增到本地（标记完成）
   - 飞书有、本地无、已完成、完成时间 < 分界线 → 跳过（旧任务不补录）
   - 飞书有、本地有 → 检查状态差异（飞书已完成但本地未勾选 → 更新本地）
   - 本地有飞书链接、飞书无 → 保持不动（可能被删除）
   - 本地有、无飞书链接 → 纯本地任务，需要同步到飞书
6. 检查任务行中的嵌入图片（`![[xxx.png]]`），同步到飞书任务附件（见下方附件同步规则）
7. 更新 frontmatter 中的 `modified` 和 `feishu_synced` 日期

### 日期自动填充规则

| 日期 | 飞书 → 本地 | 本地 → 飞书 |
|------|------------|------------|
| ➕ 创建时间 | 飞书 `created_at`，必填 | 不需要（飞书自动生成） |
| 🛫 开始时间 | 飞书 `start` 有值就用，没有则用 `created_at` | 本地 `🛫` → 飞书 `start` |
| 📅 截止时间 | 飞书 `due` 有值就用，没有则根据任务内容评估一个截止时间（除非特意留空） | 本地 `📅` → 飞书 `due` |
| ✅ 完成时间 | 飞书 `completed_at > 0` 就填，否则不填 | 本地勾选完成 → 飞书标记完成 |

#### 日期填充原则

- 所有任务都应尽量填上 🛫 开始日期和 📅 截止日期
- 截止日期根据任务内容评估：BUG 类通常 1 周内，功能开发 1-2 周，文档类 1 周
- 如果实在不好估算，给一个偏长的时间（如 2 周或 1 个月），后续再调整
- 只有用户明确说"不设截止时间"时才留空
- 新增截止日期后要同步到飞书端（`lark-cli task +update --task-id <guid> --data '{"due":{"timestamp":"<ms>","is_all_day":true}}'`）

### 自定义字段同步规则

每个飞书清单应有两个自定义字段：状态和优先级。如果清单没有这些字段，同步时需要先创建。

#### 状态字段

| 选项 | 本地 tag | 说明 |
|------|---------|------|
| （不填） | 无 status tag | 默认状态，代表未开始 |
| 进行中 | `#status/doing` | 正在处理 |
| 测试中 | `#status/testing` | 测试验证阶段 |
| 等待中 | `#status/waiting` | 等待外部条件 |
| 已完成 | `#status/done` | 已完成（已完成的任务自动设置） |
| 已取消 | `#status/cancelled` | 已取消 |

同步逻辑：
- 飞书 → 本地：根据 `custom_fields` 中状态字段的值，添加对应的 `#status/xxx` tag
- 本地 → 飞书：根据本地 `#status/xxx` tag，设置飞书自定义字段值
- 新建任务默认不填状态（代表未开始）
- 任务完成时自动设置状态为"已完成"

#### 优先级字段

| 选项 | 本地标记 | 说明 |
|------|---------|------|
| 高 | 🔺 | 高优先级 |
| 中 | 🔼 | 中优先级 |
| 低 | 🔽 | 低优先级 |
| （不填） | 无标记 | 默认，根据任务内容判断是否需要填充 |

同步逻辑：
- 飞书 → 本地：根据 `custom_fields` 中优先级字段的值，添加对应的优先级 emoji
- 本地 → 飞书：根据本地优先级 emoji，设置飞书自定义字段值
- 新建任务时根据任务内容评估优先级

#### 非项目清单状态选项

非项目清单（售前、财务、品牌宣传、供应商对接、需求管理、服务器运维）统一使用 4 个状态选项，不含"测试中"：

| 选项 | 本地 tag | color_index |
|------|---------|-------------|
| 进行中 | `#status/doing` | 30 |
| 等待中 | `#status/waiting` | 5 |
| 已完成 | `#status/done` | 20 |
| 已取消 | `#status/cancelled` | 50 |

项目清单可以额外包含"测试中"选项（color_index: 45），视项目需要决定。

#### 自定义字段创建规则

所有工作任务清单（项目和非项目）必须有「优先级」和「状态」两个自定义字段。同步时如果发现清单缺少这些字段，需要先创建再同步。

优先级字段选项（所有清单统一）：

| 选项 | color_index |
|------|-------------|
| 高 | 1（红色）|
| 中 | 11（黄色）|
| 低 | 16（绿色）|

#### 各清单自定义字段 GUID 映射

| 清单 | 状态字段 GUID | 优先级字段 GUID |
|------|-------------|---------------|
| 平台更新v2-7 | `26a6b622-c6f8-4b79-b907-96ff0481e74c` | `03b92159-f356-427b-a573-8a0434e9ec10` |
| 广州机场 | `9890d7c5-ba0d-4f0f-a684-2dd7207245dc` | `f793d9f5-c4b7-4b5a-93dc-4045dac1f6f7` |

> 其他清单的字段 GUID 在首次同步时通过 `lark-cli api GET /open-apis/task/v2/custom_fields --as user --params '{"resource_type":"tasklist","resource_id":"<guid>"}'` 获取，如果没有则创建。

#### 工具调用

```bash
# 查看清单自定义字段
lark-cli api GET /open-apis/task/v2/custom_fields --as user --params '{"resource_type":"tasklist","resource_id":"<tasklist_guid>"}'

# 创建自定义字段
lark-cli api POST /open-apis/task/v2/custom_fields --as user --data '{"resource_type":"tasklist","resource_id":"<tasklist_guid>","name":"状态","type":"single_select","single_select_setting":{"options":[{"name":"进行中","color_index":30},{"name":"测试中","color_index":45},{"name":"等待中","color_index":5},{"name":"已完成","color_index":20},{"name":"已取消","color_index":50}]}}'

# 设置任务自定义字段值（用 +update，不要用 lark-cli api PATCH）
lark-cli task +update --task-id <task_guid> --data '{"custom_fields":[{"guid":"<field_guid>","single_select_value":"<option_guid>"}]}' --as user
```

### 负责人同步规则

- 飞书 → 本地：从 `members` 中提取 `role=assignee` 的成员，通过用户映射表转为姓名，写入 `👤姓名`
- 本地 → 飞书：创建任务时通过 `--assignee <open_id>` 指定负责人
- 多个负责人用多个 `👤` 表示：`👤姚文羚 👤陆东`
- 未知的 open_id 必须先调用 `lark-cli contact +search-user` 查询姓名，不得猜测
- 修改非自己创建的任务前，需要先把自己加为 follower：`lark-cli task +followers --task-id <guid> --add <自己的open_id> --as user`

### 任务附件（图片）同步规则

本地任务行中通过 `![[图片名.png]]` 嵌入的图片，需要同步为飞书任务的附件。

#### 识别规则

任务行的缩进子行中包含 Obsidian 图片嵌入语法：
```markdown
- [ ] [任务标题](飞书链接) ... ^task-id
  ![[截图.png]]
```

图片文件查找顺序：
1. 任务文件同目录下的 `Attachments/` 文件夹
2. 任务文件同目录
3. Vault 根目录的 `Attachments/`

#### 同步流程

1. 解析任务行下方缩进行中的 `![[xxx.png]]` / `![[xxx.jpg]]` 等图片引用
2. 查找本地图片文件的实际路径
3. 获取飞书任务当前附件列表：`lark-cli api GET /open-apis/task/v2/attachments --params '{"resource_type":"task","resource_id":"<task_guid>"}'`
4. 对比本地图片和飞书附件（按文件名匹配）：
   - 本地有、飞书无 → 上传：`node lark-scripts.js task-attach <task_guid> <图片路径>`
   - 本地无、飞书有 → 不删除（飞书端可能有人手动添加的附件）
   - 同名已存在 → 跳过（不重复上传）
5. 上传失败时不阻塞任务同步，标记警告继续

#### 工具调用

```bash
# 列出任务附件
lark-cli api GET /open-apis/task/v2/attachments --params '{"resource_type":"task","resource_id":"<task_guid>"}' --as user

# 上传任务附件（multipart，必须用 lark-scripts.js）
node .kiro/skills/lark-assistant/lark-scripts.js task-attach <task_guid> <图片路径>

# 删除任务附件
lark-cli api DELETE /open-apis/task/v2/attachments/<attach_guid> --as user
```

#### 注意事项

- lark-scripts.js 复用 lark-cli 的凭据（macOS Keychain），无需单独认证
- 需要 `task:attachment:write` scope，通过 `lark-cli auth login --scope "task:attachment:write"` 授权
- 飞书任务附件上传 API 不支持 `lark-cli api`（需要 multipart），只能通过 lark-scripts.js
- 附件列表和删除可以直接用 `lark-cli api`

#### 分组同步规则

- 只同步有未完成任务的分组，空分组不在本地创建
- 分组名必须与飞书清单里的分组名称保持一致
- 如果飞书分组名变更，本地也要同步更新

### 权限与分组调整

飞书任务 API 只能操作调用者有权限的任务（创建者或成员）。

#### 分组调整流程

1. 获取任务详情，检查 members 中是否包含用户
2. 如果用户不在成员列表中：调用 `addMembers` 临时加为 follower
3. 执行 `addTasklist`（加入目标 section）
4. 如果步骤 2 中临时加入了用户，调用 `removeMembers` 移除
5. **绝对不要先 removeTasklist 再 addTasklist**

#### 降级策略

如果飞书端操作失败，在本地文件中正常归类，并用 callout 提示：

```markdown
> [!info] 飞书清单同步说明
> 以下任务因权限限制无法通过 API 操作，需在飞书客户端手动处理。
```

### 用户 ID 映射

遇到未知的用户 ID，必须先调用 `contact +get-user` 查询真实姓名，不得猜测。

| open_id | 姓名 |
|---------|------|
| ou_195bb3b8d1d0ca691e44407b827698df | 刘秉欣 |
| ou_022e1cfd69ddd292f43986257038c358 | 陆东 |
| ou_e0a91153067efa24e4c14e93e3bb5921 | 姚文羚 |
| ou_eca076dbfbc5de15f818c2032ed2c563 | 闫云江 |
| ou_dcdce1f487b53e18401e36b6302559d4 | 钟申炜 |
| ou_917a04e85c42253cc0c1c481ee50a0e4 | 伍峥 |
| ou_ea330506b95d595609440cfef93802c2 | 杨嵘 |
| ou_c0539b45af4070465c5fe10869002f89 | 石佳鑫 |
| ou_bec03d2498c2eb3eec39ae9d5aca8ddf | 何宜峰 |
| ou_0eb067ebc0cd266ff2837a7ce865d6fa | 陈子杰 |
| ou_913d65ef9fd6fb36de8a6d26ebfcfe35 | 王宗光 |
| ou_a03f60c5e33e97fdf438283d0b965170 | 邓志斌 |
| ou_48a8b3bbac19df9f243d49e19545c3be | 张函硕 |
| ou_86ca955bf3801a16cd8935d6e85fbacc | 韩晓龙 |
| ou_feec774e97c0ffbed06e416157d38409 | 刘仁跃 |

---

## 四、文档同步

### Obsidian → Feishu

- 提取 YAML front matter 后的第一个标题作为文档标题
- Markdown 转飞书格式（标题、列表、代码块、表格、链接、图片）
- 本地图片上传到飞书并替换 URL
- `[[wikilinks]]` 转飞书文档链接（如果目标也已同步）

### 文档同步元数据

```yaml
feishu_sync:
  platform: feishu
  doc_type: doc  # doc / wiki / sheet
  feishu_doc_id: "xxx"
  feishu_url: "https://..."
  sync_mode: bidirectional
  last_sync: 2025-03-14T10:00:00
  sync_status: synced
```

---

## 五、自动同步行为

### 核心原则

本地添加/修改/删除笔记或任务时，如果内容符合同步条件（见第二节决策逻辑），应立即同步到飞书，无需等待用户指令。

### 同步触发时机

| 本地操作 | 同步动作 |
|---------|---------|
| 新增任务（符合同步条件） | 在飞书创建对应任务 |
| 修改任务（标题/截止日期/负责人/状态等） | 更新飞书对应任务 |
| 完成任务（勾选 checkbox） | 在飞书标记任务完成 |
| 删除任务（移除任务行） | 在飞书删除或标记取消 |
| 新增/修改文档（符合同步条件） | 创建或更新飞书文档 |

### 同步前检查（必须，双向）

每次同步前，先获取飞书端的当前状态进行对比。同步是双向的：本地改动推到飞书，飞书改动也拉回本地。

1. 获取飞书端任务/文档的最新数据
2. 对比本地和飞书端的差异
3. 根据对比结果决定操作：

| 情况 | 处理方式 |
|------|---------|
| 仅本地有变化 | 推送本地修改到飞书 |
| 仅飞书有变化 | 拉取飞书修改到本地 |
| 两端都有变化但不冲突（修改了不同字段） | 合并两端修改，双向更新 |
| 两端都有变化且冲突（修改了相同字段） | 尝试智能合并（见下方规则） |
| 无法判断如何合并 | 询问用户确认 |

### 飞书 → 本地同步

同步检查时发现飞书端有变化，需要回写到本地：

| 飞书变化 | 本地操作 |
|---------|---------|
| 新增任务（飞书有、本地无） | 在本地对应分组新增任务行 |
| 修改任务（标题/截止日期/负责人/优先级等） | 更新本地对应任务行 |
| 完成任务 | 本地勾选 checkbox，添加 ✅ 完成日期 |
| 删除任务 | 本地移除任务行或标记删除线 |
| 分组变更 | 本地移动任务到对应分组 |
| 新增分组 | 本地新增 `# 分组名` + `feishu_section` 注释 |

### 智能合并规则

冲突时优先尝试自动合并，只有确实无法判断时才询问用户：

| 冲突类型 | 自动合并策略 |
|---------|------------|
| 标题不同 | 保留飞书端（飞书是多人协作源） |
| 截止日期不同 | 保留更晚的日期 |
| 负责人不同 | 保留飞书端 |
| 状态不同（本地完成 vs 飞书未完成） | 以本地操作为准（用户主动勾选） |
| 状态不同（本地未完成 vs 飞书已完成） | 以飞书为准（他人完成了任务） |
| 描述/补充信息不同 | 合并两端内容（本地追加在后） |
| 多个字段同时冲突 | 询问用户 |

### 同步失败处理

- 同步失败时不阻塞本地操作，本地修改照常保存
- 标记 `#sync-error/feishu`，下次操作时自动重试
- 连续 3 次失败后提示用户检查认证状态

---

## 六、冲突处理与错误处理

### 冲突处理（需要询问用户的情况）

当智能合并无法处理时：
1. 标记 `#sync-conflict/feishu`
2. 简要说明冲突内容（哪些字段不一致）
3. 让用户选择：保留本地 / 保留飞书 / 手动指定
4. 用户确认后立即执行同步

### 错误处理

- 网络错误：指数退避重试，全部失败标记 `#sync-error/feishu`
- 认证错误：提示用户运行 `lark-cli auth login --recommend`
- 频率限制：自动等待重试
- 权限不足：提示缺少的 scope，引导用户授权
