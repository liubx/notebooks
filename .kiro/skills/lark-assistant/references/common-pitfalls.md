# lark-cli 常见踩坑记录

实际使用中遇到的问题和正确做法，避免重复犯错。

---

## 1. contact 命令用错

**错误**：`lark-cli contact +search --query "xxx"`
**正确**：`lark-cli contact +search-user --query "xxx"`

contact 的搜索命令是 `+search-user`，不是 `+search`。

## 2. task +create 不支持指定 section

`lark-cli task +create` 的 `--tasklist-id` 参数只能指定清单，无法指定分组（section）。

**需要指定 section 时**，用原生 API：

```bash
lark-cli task tasks create --as user --data '{
  "summary": "任务标题",
  "tasklists": [{
    "tasklist_guid": "清单GUID",
    "section_guid": "分组GUID"
  }]
}'
```

## 3. 对已完成任务调用 +complete 会报错

**错误信息**：`cannot set non-zero completed_at for a completed task`

飞书不允许对已完成的任务再次调用完成操作。调用前应先检查任务状态，或者捕获此错误直接跳过。

**正确做法**：
- 同步前先获取飞书端任务状态（`lark-cli task tasks get <guid> --as user`）
- 如果已完成，跳过 +complete 调用
- 如果需要修改完成时间，先将 completed_at 设为 0，再重新完成

## 4. +tasklist-task-add 不支持 section

`lark-cli task +tasklist-task-add` 只能把任务加到清单，不能指定分组。

**需要指定 section 时**，用原生 API `addTasklist`：

```bash
lark-cli api POST /open-apis/task/v2/tasks/<task_guid>/add_tasklist --as user --data '{
  "tasklist": {
    "tasklist_guid": "清单GUID",
    "section_guid": "分组GUID"
  }
}'
```

## 5. lark-cli api 裸调字段名必须精确

`lark-cli api` 的参数字段名必须与飞书官方文档完全一致。字段名错误会导致静默失败（exit 1，无输出），容易误判为 bug。

**正确做法**：不确定字段名时，先用 `lark-cli schema <resource>.<method>` 查看参数结构。

## 6. task +create 的 assignee 是 open_id

`--assignee` 参数需要传 `open_id`（如 `ou_xxx`），不是用户名。

**查找 open_id**：`lark-cli contact +search-user --query "姓名" --as user`

## 7. task tasks get 的 path 参数用 --params 传递

`lark-cli task tasks get` 不支持位置参数或 `--task_guid`，必须用 `--params`：

```bash
# 错误
lark-cli task tasks get c0f368a9-xxx --as user
lark-cli task tasks get --task_guid c0f368a9-xxx --as user

# 正确
lark-cli task tasks get --params '{"task_guid":"c0f368a9-xxx"}' --as user
```

所有 lark-cli 原生 API 的 path 参数都通过 `--params` JSON 传递。
