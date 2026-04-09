---
inclusion: fileMatch
fileMatchPattern: "**/1-任务.md"
---

# 飞书任务同步流程

当添加或修改带有 `feishu_tasklist_guid` 的任务文件中的任务时，必须同步到飞书。
不要先写本地再"等用户说同步"，添加/修改的同时就完成飞书同步。
同步失败不阻塞本地操作，标记 `#sync-error/feishu` 后继续。

## 核心原则：保证本地与飞书一致

同步的目标是让本地 Obsidian 和飞书任务保持一致。具体含义：
- 飞书是权威数据源，拉取时以飞书为准覆盖本地
- 本地新增/修改后必须立即推送到飞书，不存在"仅本地"的中间状态
- 任务的所有同步字段（标题、状态、日期、负责人、优先级、描述、所属清单/分组）双端必须一致
- 如果发现不一致，以最后修改方为准；无法判断时以飞书为准

---

## 零、同步范围

### 清单范围

只同步"数据映射总表"（第六节）中标记 ✅ 的清单，包括：
- 所有进行中项目的任务清单（`1-Projects/Work/*/1-任务.md`）
- 所有综合任务清单（`2-Areas/Work/飞书任务/*.md`）

不同步的清单：
- 未开始项目（区域功能开发、三维地图开发、赛峰项目等）
- 归档项目（天河机场等）
- 用户明确排除的清单

### 任务范围

每个清单内，同步以下任务：
- 所有未完成任务（`completed_at` 为空）
- 最近 30 天内完成的任务（`completed_at` 在近 30 天内）

超过 30 天的已完成任务：
- 拉取时：如果本地已有则保留不动，如果本地没有则不拉取
- 推送时：不主动推送变更

### 同步字段

每个任务必须同步以下字段，保证双端一致：

| 字段 | 飞书来源 | 本地标记 | 说明 |
|------|---------|---------|------|
| 标题 | summary | 任务文本 | 必须一致 |
| 完成状态 | completed_at | `[x]`/`[ ]` + ✅日期 | 必须一致 |
| 开始日期 | start.timestamp | 🛫 YYYY-MM-DD | 项目任务必填，综合任务可选 |
| 截止日期 | due.timestamp | 📅 YYYY-MM-DD | 项目任务必填，综合任务可选 |
| 负责人 | members (assignee) | 👤姓名 | 必须一致，follower 不同步 |
| 优先级 | 自定义字段 | 🔺/⏫/🔼/无 | 可为空，但必须确认查过飞书 |
| 状态 | 自定义字段 | #status/doing 等 | 可为空，未完成任务无状态时不强制补 |
| 描述 | description | 缩进子内容 | 必须一致 |
| 所属清单 | tasklist | 文件归属 | 任务在哪个清单决定写入哪个文件 |
| 所属分组 | section | ## 标题 | 任务在哪个 section 决定放在哪个标题下 |
| 飞书链接 | guid + task_id | `[标题](applink)` | 同步后必须有 |

时间补全规则：
- 项目任务（`1-Projects/Work/*/1-任务.md`）和服务器运维：缺少时间时根据内容估算并补全，补完后同步到飞书
- 其他综合任务清单：时间可选，不强制补全

优先级和状态：
- 可以为空（飞书端确实没设的情况），但必须是"确认过飞书端没设"而非"忘了查"
- 拉取时如果飞书有值则必须同步到本地，飞书无值则本地也不标记

---

## 一、拉取同步（飞书 → Obsidian）

触发：用户说"同步飞书任务"、"拉取XX项目任务"、"更新任务"等。

### 1. 准备阶段

```
1) 读取目标任务文件的 frontmatter，获取 feishu_tasklist_guid
2) 读取对应项目的 0-总览.md，获取自定义字段 ID（优先级字段 ID、状态字段 ID 及各选项 ID）
3) 如果 0-总览.md 中没有自定义字段 ID，先查询并补充：
   lark-cli api GET /open-apis/task/v2/custom_fields \
     --params '{"resource_type":"tasklist","resource_id":"<tasklist_guid>","page_size":"50"}' \
     --as user --timeout 30000
4) 读取人员映射表：2-Areas/Work/公司人员.md
```

### 2. 获取飞书数据

```bash
# 获取清单下所有 section
lark-cli task sections list --data '{"tasklist_guid":"<guid>"}' --as user

# 获取每个 section 下的任务列表（包含已完成任务）
lark-cli task tasklists tasks --tasklist_guid <guid> \
  --params '{"section_guid":"<section_guid>","page_size":"100","completed":"both"}' --as user

# 获取每个任务的详情（负责人、描述、自定义字段等）
lark-cli task tasks get --task_guid <task_guid> \
  --params '{"user_id_type":"open_id"}' --as user
```

所有命令必须设置 timeout=30000。

### 3. 过滤任务

```
对于获取到的每个任务：
  - 未完成（completed_at 为空）→ 纳入同步
  - 已完成且 completed_at 在近 30 天内 → 纳入同步
  - 已完成且 completed_at 超过 30 天 → 跳过（本地已有则保留不动）
```

### 4. 数据转换规则

#### 任务行格式

```
- [ ] [任务标题](飞书applink) [[文件路径#^block-id|↗️]] 👤负责人 🛫 开始日期 📅 截止日期 优先级emoji ➕ 创建日期 #task/work #project/项目名 #status/状态 ^block-id
  描述内容（如果有，缩进两空格）
```

#### 字段顺序（严格遵守）

任务标题 → `[](飞书链接)` → `[[自引用]]` → 👤负责人(可多个) → 🛫开始日期 → 📅截止日期 → 优先级emoji → ➕创建日期 → ✅完成日期(仅已完成) → #task/work → #project/xxx → #status/xxx → ^block-id

#### 飞书链接格式

```
https://applink.feishu.cn/client/todo/detail?guid={guid}&suite_entity_num={task_id}
```

- 链接放在任务标题文字后面，用 `[任务标题](url)` 格式
- 同步时通过 URL 中的 guid 参数匹配任务

#### 自引用链接

```
[[1-Projects/Work/项目名/1-任务#^block-id|↗️]]
```

- 放在飞书链接后面，用于 Obsidian 内部跳转

#### 优先级映射

| 飞书自定义字段值 | Obsidian emoji | Tasks 插件级别 |
|----------------|---------------|--------------|
| 高 | 🔺 | Highest |
| 中 | ⏫ | High |
| 低 | 🔼 | Medium |
| 无 | 不标记 | Normal |

#### 状态映射

| 飞书自定义字段值 | Obsidian tag |
|----------------|-------------|
| 进行中 | #status/doing |
| 测试中 | #status/testing |
| 等待中 | #status/waiting |
| 已完成 | #status/done |
| 已取消 | #status/cancelled |

#### 人员映射

- 从 `2-Areas/Work/公司人员.md` 查 open_id → 姓名
- 多个负责人用空格分隔：`👤张三 👤李四`
- 只同步 assignee（role="assignee"），follower 不同步

#### Section 映射

- 飞书 section name → Obsidian `## Section名称` 二级标题
- section 下方加 HTML 注释标记：`<!-- feishu_section: <section_guid> (section名称) -->`
- "默认分组" section 放在文件最后

### 5. 匹配与更新逻辑

```
对于飞书返回的每个任务（已通过第 3 步过滤）：
  1) 在本地文件中搜索包含该任务 guid 的行
  2) 如果找到（已有任务）：
     - 逐字段对比：标题、完成状态、开始日期、截止日期、负责人、优先级、状态、描述
     - 有变化的字段以飞书为准更新本地
     - 飞书已完成但本地未完成 → 改为 [x]，加 ✅ 日期，#status/xxx → #status/done
     - 飞书未完成但本地已完成 → 改为 [ ]，去掉 ✅，恢复飞书端的状态 tag
     - 负责人变化 → 更新 👤 列表
     - 描述变化 → 更新缩进子内容
  3) 如果未找到（新任务）：
     - 生成 block-id（格式：^task-简短英文描述）
     - 按飞书的 section 归属，追加到对应 section 末尾
     - 所有同步字段都要写入
  4) 本地有飞书链接但飞书端已删除的任务 → 标记 ~~已从飞书删除~~
  5) 任务在飞书端移动了 section → 本地也移动到对应 section 下

对于本地文件中的 section：
  1) 飞书有新 section → 在文件中创建新的二级标题 + feishu_section 注释
  2) 飞书 section 改名 → 更新标题和注释
  3) 保持 section 在飞书中的排列顺序
```

### 6. 更新 frontmatter

```yaml
modified: 当天日期
feishu_synced: 当天日期
```

---

## 二、推送同步（Obsidian → 飞书）

触发：用户说"推送任务到飞书"、"创建飞书任务"、在本地新增/修改任务等。

### 1. 新增任务

```
1) 在本地文件对应 section 下写入任务行（暂无飞书链接）
2) 创建飞书任务（包含所有字段）：
   lark-cli task tasks create --data '{
     "summary": "任务标题",
     "due": {"timestamp": "秒级时间戳", "is_all_day": true},
     "start": {"timestamp": "秒级时间戳", "is_all_day": true},
     "members": [{"id": "ou_xxx", "type": "user", "role": "assignee"}],
     "description": "描述内容（如果有）",
     "tasklist_guid": "<清单guid>",
     "section_guid": "<分组guid>"
   }' --as user --timeout 45000

   简单任务也可用 shortcut：
   lark-cli task +create \
     --summary "任务标题" \
     --tasklist-guid <清单guid> \
     --section-guid <分组guid> \
     --as user --timeout 45000

3) 从返回结果提取 guid 和 task_id（suite_entity_num 字段）
4) 生成飞书 applink：
   https://applink.feishu.cn/client/todo/detail?guid={guid}&suite_entity_num={task_id}
5) 更新本地任务行，补上 [任务标题](applink) 和 [[自引用]]
6) 设置自定义字段（优先级和状态，如果有值）：
   lark-cli task tasks patch --task_guid <guid> --data '{
     "task": {"custom_fields": [
       {"guid": "<优先级字段ID>", "single_select_value": "<选项ID>"},
       {"guid": "<状态字段ID>", "single_select_value": "<选项ID>"}
     ]},
     "update_fields": ["custom_fields"]
   }' --as user --timeout 30000
7) 如果是项目任务且缺少时间，根据内容估算补全，补完后同步到飞书
```

### 2. 修改已有任务

```
1) 识别变更内容（标题、日期、负责人、状态、优先级、描述）
2) 更新本地文件
3) 同步到飞书：
   lark-cli task tasks patch --task_guid <guid> --data '{
     "task": {变更字段},
     "update_fields": ["变更的字段名"]
   }' --as user --timeout 30000
```

#### 常见变更的 patch 字段

| 变更 | update_fields | data.task 内容 |
|------|--------------|---------------|
| 标题 | `["summary"]` | `{"summary": "新标题"}` |
| 截止日期 | `["due"]` | `{"due": {"timestamp": "秒级时间戳", "is_all_day": true}}` |
| 开始日期 | `["start"]` | `{"start": {"timestamp": "秒级时间戳", "is_all_day": true}}` |
| 描述 | `["description"]` | `{"description": "新描述内容"}` |
| 优先级 | `["custom_fields"]` | `{"custom_fields": [{"guid": "字段ID", "single_select_value": "选项ID"}]}` |
| 状态 | `["custom_fields"]` | `{"custom_fields": [{"guid": "字段ID", "single_select_value": "选项ID"}]}` |

#### 负责人变更

```bash
# 添加负责人
lark-cli task members add --task_guid <guid> \
  --data '{"members": [{"id": "ou_xxx", "type": "user", "role": "assignee"}]}' --as user

# 移除负责人
lark-cli task members remove --task_guid <guid> \
  --data '{"members": [{"id": "ou_xxx", "type": "user", "role": "assignee"}]}' --as user
```

#### 任务移动（清单/分组变更）

如果任务需要从一个清单或分组移到另一个：
```bash
# 从原清单移除
lark-cli task tasklists remove_task --tasklist_guid <原清单guid> \
  --data '{"task_guid":"<task_guid>"}' --as user

# 添加到新清单的指定分组
lark-cli task +tasklist-task-add --tasklist-guid <新清单guid> \
  --task-guids <task_guid> --section-guid <新分组guid> --as user
```
本地同步：将任务行从原文件/section 移到目标文件/section。

### 3. 完成/重新打开任务

```bash
# 完成任务
lark-cli task +complete --task-guid <guid> --as user --timeout 30000
# 本地：[ ] → [x]，加 ✅ 日期，#status/xxx → #status/done

# 重新打开
lark-cli task +reopen --task-guid <guid> --as user --timeout 30000
# 本地：[x] → [ ]，去掉 ✅ 日期，恢复之前的 #status/xxx
```

---

## 三、时间补全规则

### 必须补全的文件

- `1-Projects/Work/*/1-任务.md` — 所有项目任务
- `2-Areas/Work/服务器运维/1-任务.md` — 服务器运维

### 不强制补全的文件

- 需求管理、供应商对接、售前项目支持、品牌宣传、财务工作等综合任务清单

### 补全逻辑

```
如果任务缺少 🛫 或 📅：
  1) 根据任务类型和内容估算合理时间
  2) 参考同 section 内其他任务的时间范围
  3) 开始日期默认为创建日期或当天
  4) 截止日期根据任务复杂度估算（简单 3-5 天，中等 1-2 周，复杂 2-4 周）
  5) 本地补完后立即同步到飞书
```

---

## 四、同步检查清单（每次必检）

每次新建、修改、同步任务后，逐项检查：

| 字段 | 本地标记 | 要求 |
|------|---------|------|
| 飞书链接 | `[标题](applink)` | 必须有（新建后立即补） |
| 自引用 | `[[path#^id\|↗️]]` | 必须有 |
| 负责人 | 👤姓名 | 必须与飞书一致 |
| 开始日期 | 🛫 YYYY-MM-DD | 项目任务+服务器运维必填，其他可选 |
| 截止日期 | 📅 YYYY-MM-DD | 项目任务+服务器运维必填，其他可选 |
| 优先级 | 🔺/⏫/🔼/无 | 必须确认查过飞书（可为空） |
| 状态 | #status/doing 等/无 | 必须确认查过飞书（可为空） |
| 描述 | 缩进子内容 | 必须与飞书一致（无描述则无子内容） |
| 所属分组 | ## 标题下 | 必须与飞书 section 一致 |
| block-id | ^task-xxx | 必须有 |
| #task/work | tag | 必须有 |
| #project/xxx | tag | 必须有 |

---

## 五、自定义字段 ID 查询与存储

### 查询命令

```bash
lark-cli api GET /open-apis/task/v2/custom_fields \
  --params '{"resource_type":"tasklist","resource_id":"<tasklist_guid>","page_size":"50"}' \
  --as user --timeout 30000
```

### 存储位置

在项目 `0-总览.md` 的"飞书信息"部分，格式：

```markdown
## 飞书信息

- 任务清单：项目名（`<tasklist_guid>`）→ [[1-任务]]
- 项目群组：项目名（`<chat_id>`）
- 自定义字段：
  - 状态：`<field_guid>`（进行中=`<option_id>`、等待中=`<option_id>`、已完成=`<option_id>`、已取消=`<option_id>`、测试中=`<option_id>`）
  - 优先级：`<field_guid>`（高=`<option_id>`、中=`<option_id>`、低=`<option_id>`）
```

### 已知清单字段 ID

同步前先读 0-总览.md 确认，不要硬编码。如果缺失，查询后写回 0-总览.md。

---

## 六、数据映射总表

### 任务清单 → Obsidian 文件

| 分类 | 飞书清单 | Obsidian 文件 | 同步 |
|------|---------|-------------|------|
| 进行中项目 | AI工作流 | `1-Projects/Work/AI工作流/1-任务.md` | ✅ |
| 进行中项目 | 平台更新v2.7 | `1-Projects/Work/平台更新v2-7/1-任务.md` | ✅ |
| 进行中项目 | 广州机场 | `1-Projects/Work/广州机场/1-任务.md` | ✅ |
| 进行中项目 | 上港仓储管理 | `1-Projects/Work/上港仓储管理/1-任务.md` | ✅ |
| 进行中项目 | 新太项目 | `1-Projects/Work/新太项目/1-任务.md` | ✅ |
| 进行中项目 | 南宁机场项目 | `1-Projects/Work/南宁机场/1-任务.md` | ✅ |
| 进行中项目 | PN仓库项目 | `1-Projects/Work/PN仓库项目/1-任务.md` | ✅ |
| 综合任务 | 售前工作 | `2-Areas/Work/飞书任务/售前工作.md` | ✅ |
| 综合任务 | 服务器运维 | `2-Areas/Work/飞书任务/服务器运维.md` | ✅ |
| 综合任务 | 需求管理 | `2-Areas/Work/飞书任务/需求管理.md` | ✅ |
| 综合任务 | 营销宣传 | `2-Areas/Work/飞书任务/营销宣传.md` | ✅ |
| 综合任务 | 财务工作 | `2-Areas/Work/飞书任务/财务工作.md` | ✅ |
| 综合任务 | 设备测试 | `2-Areas/Work/飞书任务/设备测试.md` | ✅ |
| 未开始项目 | 区域功能开发等 | 暂不同步 | ❌ |
| 归档项目 | 天河机场等 | 不同步 | ❌ |

### 人员映射

存储在 `2-Areas/Work/公司人员.md`，通过 open_id 查姓名。

---

## 七、错误处理

| 场景 | 处理 |
|------|------|
| API 超时 | 相同命令重试一次（timeout 不变）→ 简化参数重试 → 报告用户 |
| 权限不足 | 按 lark-shared 规则处理，提示用户授权 |
| 任务不存在 | 可能已被飞书端删除，本地标记 ~~已从飞书删除~~ |
| 字段 ID 不匹配 | 重新查询自定义字段，更新 0-总览.md |
| 同步失败 | 本地任务行加 `#sync-error/feishu`，不阻塞其他操作 |

---

## 八、时间戳转换

飞书 API 使用秒级 Unix 时间戳，且 `is_all_day: true` 时时间戳为当天 00:00:00 UTC+8。

```
日期 → 时间戳：date -j -f "%Y-%m-%d" "2026-04-09" "+%s"
时间戳 → 日期：date -r 1775836800 "+%Y-%m-%d"
```

注意：macOS 的 date 命令语法与 Linux 不同，用 `-j -f` 格式。
