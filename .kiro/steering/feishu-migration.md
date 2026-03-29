# 飞书文档迁移指南

将飞书云文档和知识库内容迁移到 Obsidian vault 中。

## 迁移范围

### 包含
- 用户能访问的所有飞书文档和知识库
- reliablesense.feishu.cn 域名下的内容

### 排除（第三方公开知识库）
- waytoagi.feishu.cn — AI 学习社区知识库
- docugenius.feishu.cn — 飞书排版打印插件文档
- bytedance.larkoffice.com — 飞书官方文档
- hsiaohsihsi.feishu.cn — 第三方模板库
- my.feishu.cn — 飞书个人模板库
- future-organization.feishu.cn — 第三方课程
- chao-hai.feishu.cn — 第三方知识库
- zhipu-ai.feishu.cn — 智谱 AI 文档
- feichuangtech.feishu.cn — 第三方插件文档
- m7zr8sy5wi.feishu.cn — 第三方知识库

判断方法：知识库 URL 中域名不是 `reliablesense.feishu.cn` 的都跳过。

## 文档类型处理

### 可读取内容（转 Markdown）
| 类型 | 工具 | 说明 |
|------|------|------|
| docx | `lark-cli docs +fetch --doc <token>` | 飞书新版文档，获取内容 |
| doc | `lark-cli docs +fetch --doc <token>` | 飞书旧版文档 |

### 无法直接读取内容（保留链接）
| 类型 | 说明 | 处理方式 |
|------|------|----------|
| file | 上传的附件（.docx/.pdf/.pptx 等） | 记录链接，后续通过导出任务+下载处理 |
| bitable | 多维表格 | 记录链接和标题 |
| sheet | 电子表格 | 记录链接和标题 |
| mindnote | 思维导图 | 记录链接和标题 |

### 文件下载流程
```bash
# lark-cli 原生支持
lark-cli drive +download --file-token <token> --output <输出路径>

# 或通过导出 API（lark-cli api 裸调）
lark-cli api POST /open-apis/drive/v1/export_tasks --data '{"file_extension":"pdf","token":"<token>","type":"docx"}'
```

## 迁移目标路径

```
4-Archives/Feishu/
├── 文档/                    # docx/doc 类型，转为 Markdown
├── 知识库/                  # 知识库节点，转为 Markdown
├── Attachments/            # 下载的附件文件
└── 迁移记录-飞书.md         # 迁移清单和状态
```

## 迁移记录格式

在 `1-Projects/Personal/笔记迁移/迁移记录-飞书.md` 中记录：

```markdown
---
title: 迁移记录-飞书
type: migration-log
source: feishu
created: YYYY-MM-DD
modified: YYYY-MM-DD
---

# 飞书文档迁移记录

## 统计
- 总文档数：N
- 已迁移：N（docx/doc 转 Markdown）
- 仅保留链接：N（bitable/sheet/mindnote/file）
- 跳过：N（第三方知识库）

## 文档（docx/doc）

| 标题 | Token | 类型 | 迁移到 | 状态 |
|------|-------|------|--------|------|
| xxx  | xxx   | docx | [[4-Archives/Feishu/文档/xxx]] | ✅ 已迁移 |

## 知识库

| 标题 | Node ID | Space | 迁移到 | 状态 |
|------|---------|-------|--------|------|
| xxx  | xxx     | xxx   | [[4-Archives/Feishu/知识库/xxx]] | ✅ 已迁移 |

## 无法迁移内容（保留链接）

| 标题 | Token | 类型 | 飞书链接 |
|------|-------|------|----------|
| xxx  | xxx   | bitable | https://... |

## 跳过的第三方内容

| 标题 | 来源 | 原因 |
|------|------|------|
| xxx  | waytoagi | 第三方公开知识库 |
```

## 迁移后的文档格式

```markdown
---
title: 原始标题
source: feishu
feishu_token: "xxx"
feishu_type: docx
feishu_url: "https://..."
migrated: YYYY-MM-DD
tags:
  - feishu-migration
---

# 原始标题

（文档内容）
```

## 注意事项

- 飞书文档中的 @提及 会显示为用户 ID，无法自动转换为姓名
- 飞书文档中的图片需要单独下载（通过素材临时下载链接）
- 知识库节点可能有层级关系，迁移时保留为平铺结构，用 wikilink 关联
- 迁移完成后，原飞书文档不删除，保留作为备份
