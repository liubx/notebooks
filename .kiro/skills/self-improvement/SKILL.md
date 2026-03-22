---
name: self-improvement
description: "捕获学习、错误和纠正，实现持续改进。触发时机：(1) 命令或操作失败 (2) 用户纠正了错误 (3) 用户提出新功能需求 (4) 发现知识过时或不正确 (5) 发现更好的做法。"
---

# 自我改进 Skill

在工作过程中记录学习和错误，持续改进。重要的经验可以晋升为项目规则。

## 快速参考

| 场景 | 操作 |
|------|------|
| 命令/操作失败 | 记录到 `.learnings/ERRORS.md` |
| 用户纠正了你 | 记录到 `.learnings/LEARNINGS.md`，分类 `correction` |
| 用户想要新功能 | 记录到 `.learnings/FEATURE_REQUESTS.md` |
| API/工具调用失败 | 记录到 `.learnings/ERRORS.md` |
| 知识过时了 | 记录到 `.learnings/LEARNINGS.md`，分类 `knowledge_gap` |
| 发现更好的做法 | 记录到 `.learnings/LEARNINGS.md`，分类 `best_practice` |
| 经验普遍适用 | 晋升到 `.kiro/steering/` 或 `.kiro/rules/` |

## 日志格式

### 学习记录（LEARNINGS.md）

```markdown
## [LRN-YYYYMMDD-XXX] 分类

**记录时间**: YYYY-MM-DD
**优先级**: low | medium | high | critical
**状态**: pending | resolved | promoted
**领域**: obsidian | feishu | git | infra | docs | config | life

### 摘要
一句话描述学到了什么

### 详情
完整上下文：发生了什么，哪里错了，正确的是什么

### 晋升到
（如果已晋升）目标文件路径

---
```

### 错误记录（ERRORS.md）

```markdown
## [ERR-YYYYMMDD-XXX] 命令或工具名

**记录时间**: YYYY-MM-DD
**优先级**: high
**状态**: pending | resolved

### 摘要
简述什么失败了

### 错误信息
实际的错误输出

### 上下文
- 执行的命令/操作
- 使用的参数
- 环境信息

### 修复方法
如果已知，怎么解决

---
```

### 功能需求（FEATURE_REQUESTS.md）

```markdown
## [FEAT-YYYYMMDD-XXX] 功能名

**记录时间**: YYYY-MM-DD
**优先级**: medium
**状态**: pending

### 需求描述
用户想要做什么

### 背景
为什么需要，解决什么问题

---
```

## 晋升规则

当一条经验被验证为普遍适用时，晋升到项目级规则：

| 经验类型 | 晋升到 | 示例 |
|----------|--------|------|
| 行为规范 | `.kiro/rules/` | "修改前先检查文件状态" |
| 工作流程 | `.kiro/steering/` | "飞书迁移流程" |

## 检测触发词

**用户纠正**（→ correction）：
- "不对"、"错了"、"应该是..."、"不是这样"

**功能需求**（→ feature request）：
- "能不能..."、"我想要..."、"有没有办法..."

**知识盲区**（→ knowledge_gap）：
- 用户提供了你不知道的信息
- 文档或 API 行为与预期不符

**错误**（→ error）：
- 命令返回非零退出码
- 异常或报错信息
- 超时或连接失败
