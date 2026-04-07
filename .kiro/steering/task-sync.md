---
inclusion: fileMatch
fileMatchPattern: "**/1-任务.md"
---

# 任务同步规则

当添加或修改带有 `feishu_tasklist_guid` 的任务文件中的任务时，必须同步到飞书：

## 新增任务
1. 在本地任务文件中添加任务行
2. 立即调用飞书 API 创建对应任务（`lark-cli task tasks create`），放入对应的清单和分组
3. 用返回的飞书链接和 task_id 更新本地任务行
4. 如果任务行有嵌入图片（`![[xxx.png]]`），上传为飞书任务附件

## 修改任务
- 标题、截止日期、开始日期、负责人、状态等变更，同步更新飞书端
- 本地勾选完成 → 飞书标记完成
- 本地取消勾选 → 飞书重新打开

## 自定义字段同步（优先级 + 状态）

每个任务清单都有"优先级"和"状态"两个 single_select 自定义字段，同步时必须双向同步：

### 飞书 → 本地
- 优先级：高→🔺、中→⏫、低→🔼、无→不标记
- 状态：进行中→`#status/doing`、测试中→`#status/testing`、等待中→`#status/waiting`、已完成→`#status/done`
- 优先级 emoji 放在 `#task/` 标签之前
- 状态 tag 放在 `#project/xxx` 之后、`^task-` 之前

### 本地 → 飞书
- 🔺→高、⏫→中、🔼/🔽→低
- `#status/doing`→进行中、`#status/testing`→测试中、`#status/waiting`→等待中
- 已完成任务（`[x]`）自动设状态为"已完成"
- 未完成且无状态 tag 的任务默认设为"进行中"

### 各清单自定义字段 ID（每个清单不同！）
字段 ID 存储在各项目的 `0-总览.md` 飞书信息部分，同步前必须先读取确认。
如果字段 ID 不存在或不确定，先通过 API 查询：
```bash
lark-cli api GET /open-apis/task/v2/custom_fields \
  --params '{"resource_type":"tasklist","resource_id":"<tasklist_guid>","page_size":"50"}' --as user
```

## 时间补全
- 新建、修改、同步任务时，如果发现任务缺少开始日期（🛫）或截止日期（📅），主动估算并补上
- 估算依据：任务类型（BUG修复约1周、性能优化约2周、长期运维按实际情况）、创建日期、同类任务参考
- 本地补完后立即同步到飞书
- "待确认"分组的任务除外，不主动补时间

## 关键点
- 不要先写本地再"等用户说同步"，添加/修改的同时就完成飞书同步
- 同步失败不阻塞本地操作，标记 `#sync-error/feishu` 后继续
