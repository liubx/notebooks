---
title: Git子模块管理
type: code-snippet
language: bash
tags:
  - tech/git
source: "[[4-Archives/Notion/技术相关/Git相关指令 951abbbb0258487d911931258f0cc44b]]"
created: 2026-03-16
---

## 删除子模块

```bash
git submodule deinit {MOD_NAME}
git rm --cached {MOD_NAME}
git commit -am "Remove a submodule."
```

## 修改子模块 URL

1. 修改 `.gitmodules` 中对应模块的 `url`
2. 同步到 `.git/config`：

```bash
git submodule sync
git commit -am "Update submodule url."
```

## 初始化/更新

```bash
git submodule update --init --recursive
git submodule deinit -f rscommon
```
