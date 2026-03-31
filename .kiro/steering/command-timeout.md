---
inclusion: always
---

# Shell 命令超时与重试策略

## 超时设置

所有 shell 命令（特别是 `lark-cli` 相关命令）执行时必须设置 `timeout` 参数：

- 普通命令（查询、搜索）：timeout = 30000（30秒）
- 发送消息、创建文档等写操作：timeout = 45000（45秒）
- 文件下载、批量操作：timeout = 60000（60秒）
- 绝对不要不设置 timeout

## 重试策略

如果命令超时或失败：

1. 第一次超时：用相同命令重试一次，保持相同 timeout
2. 第二次超时：尝试简化命令参数或拆分为更小的操作
3. 第三次失败：向用户报告问题，说明已尝试的方法，询问是否继续

## 常见卡住场景

- `lark-cli` 网络请求卡住 → 设置 timeout 后重试
- 大量数据查询 → 分页或限制数量
- 文件下载 → 检查 token 是否有效，重试

## 示例

```
executeBash: command="lark-cli im +messages-send ...", timeout=45000
executeBash: command="lark-cli contact +search-user ...", timeout=30000
executeBash: command="lark-cli docs +fetch ...", timeout=30000
```
