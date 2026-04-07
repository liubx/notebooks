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

## 文档类型处理（2026-04-04 更新）

### Token 前缀与文档类型对应关系
- `doxcn` 前缀 → docx 新版文档（可直接 `docs +fetch` 读取）
- `doccn` 前缀 → doc 旧版文档（`docs +fetch` 不支持，需通过导出 API）
- `boxcn` 前缀 → file 上传附件

### 可直接读取内容（转 Markdown）
| 类型 | 工具 | 说明 |
|------|------|------|
| docx | `lark-cli docs +fetch --doc <token>` | 飞书新版文档，直接获取 Markdown |

### 通过导出 API 获取内容
| 类型 | 导出格式 | 说明 |
|------|---------|------|
| doc | 导出为 docx → pandoc 转 Markdown | 旧版文档，`docs +fetch` 不支持 |
| sheet | `sheets +export --file-extension xlsx` 或导出 API | 电子表格，也可用 `sheets +read` 读取内容 |

### 可直接下载原始文件
| 类型 | 工具 | 说明 |
|------|------|------|
| file | `lark-cli drive +download --file-token <token>` | 上传的附件（.docx/.pdf/.pptx/.xlsx/.zip 等） |

### 可读取数据（转 Markdown 表格或 CSV）
| 类型 | 工具 | 说明 |
|------|------|------|
| bitable | `lark-cli base +table-list` / `+field-list` / `+record-list` | 多维表格，可读取表结构和记录数据 |
| sheet | `lark-cli sheets +read` / `+info` | 电子表格，可读取单元格内容 |

### 无法导出（仅保留链接）
| 类型 | 说明 | 原因 |
|------|------|------|
| mindnote | 飞书思维导图（10 个） | 导出 API 不支持 mindnote 类型 |
| slides | 飞书幻灯片（2 个，已跳过） | 非本人文件，导出 API 也不支持 |

## doc 旧版文档导出流程（52 个）

doc 旧版文档（`doccn` 前缀）无法通过 `docs +fetch` 读取，但可以通过导出 API 导出为 docx 文件，再用 pandoc 转为 Markdown。

### 步骤
```bash
# 1. 创建导出任务
lark-cli api POST /open-apis/drive/v1/export_tasks \
  --data '{"file_extension":"docx","token":"<doc_token>","type":"doc"}' --as user

# 2. 查询任务状态（返回 file_token）
lark-cli api GET /open-apis/drive/v1/export_tasks/<ticket> \
  --params '{"token":"<doc_token>"}' --as user

# 3. 下载导出的 docx 文件
lark-cli api GET /open-apis/drive/v1/export_tasks/file/<file_token>/download \
  --output <输出路径>.docx --as user

# 4. 用 pandoc 转为 Markdown
pandoc <输出路径>.docx -t markdown -o <输出路径>.md
```

### 处理方式
- docx 文件保存到 `4-Archives/Notes/Feishu/Attachments/` 目录
- 同时用 pandoc 转为 Markdown，保存到对应的迁移目标路径
- Markdown 文件的 frontmatter 中标记 `feishu_type: doc` 和 `export_method: export-api+pandoc`

## file 附件下载流程

```bash
lark-cli drive +download --file-token <token> --output <输出路径> --as user
```

保存到 `4-Archives/Notes/Feishu/Attachments/` 目录，按原始文件夹结构组织。

## sheet 电子表格导出流程

```bash
# 方式一：Shortcut 导出
lark-cli sheets +export --spreadsheet-token <token> --file-extension xlsx --output-path <路径> --as user

# 方式二：读取内容转 Markdown
lark-cli sheets +read --spreadsheet-token <token> --as user
```

## bitable 多维表格导出流程

```bash
# 列出所有表
lark-cli base +table-list --base-token <token> --as user

# 列出字段
lark-cli base +field-list --base-token <token> --table-id <table_id> --as user

# 读取记录
lark-cli base +record-list --base-token <token> --table-id <table_id> --as user
```

读取后转为 Markdown 表格保存。

## 迁移目标路径

所有文件按飞书原始目录结构放置：

```
4-Archives/Notes/Feishu/
├── 云空间/                  # 按原始文件夹结构组织
│   ├── 根目录/
│   │   ├── 文档名.md        # docx/doc 转 Markdown
│   │   ├── Attachments/     # 该目录下文档的图片
│   │   ├── 表格名.xlsx      # sheet 导出
│   │   ├── 多维表格名.md    # bitable 导出为 Markdown
│   │   ├── 思维导图名.mm    # mindnote 手动下载
│   │   └── 附件名.docx      # file 直接下载
│   ├── 莱讯科技/
│   │   ├── 项目运维管理/
│   │   │   ├── 运维文档/
│   │   │   │   ├── 前端运维手册.md
│   │   │   │   ├── Attachments/    # 运维文档目录下的图片
│   │   │   │   └── 运维手册.docx   # file 下载的附件
│   │   │   └── ...
│   │   ├── 项目开发管理/
│   │   │   ├── 项目管理流程.mm     # mindnote 按原始位置放
│   │   │   └── ...
│   │   └── ...
│   └── ...
├── 知识库/                  # 按知识库树状结构组织
│   └── ...
└── 无法迁移/
    └── 链接索引.md          # slides 等无法导出的链接汇总
```

### 文件摆放规则
- docx/doc → 转 Markdown，放在飞书原始目录对应位置
- sheet → 导出 xlsx + 生成 Markdown 摘要，放在飞书原始目录
- bitable → 导出为 Markdown 表格，放在飞书原始目录
- file → 直接下载原始文件，放在飞书原始目录
- mindnote → 手动下载 .mm 文件，放在飞书原始目录
- 图片 → 放在文档同级的 `Attachments/` 子目录下

## 迁移后的文档格式

```markdown
---
title: 原始标题
source: feishu
feishu_token: "xxx"
feishu_type: docx/doc/sheet/bitable
feishu_url: "https://..."
export_method: direct/export-api+pandoc/sheets-read/base-record-list
migrated: YYYY-MM-DD
tags:
  - feishu-migration
---

# 原始标题

（文档内容）
```

## 文档图片处理流程

`docs +fetch` 返回的 Markdown 中，图片以 `<image token="boxcnXXX" width="N" height="N"/>` 格式存在。
需要额外步骤下载图片并替换引用。

### 图片处理步骤

```bash
# 1. 从 Markdown 中提取所有 image token
grep -oE 'token="[^"]+"' <文档>.md | sed 's/token="//;s/"//'

# 2. 逐个下载图片（自动检测扩展名）
lark-cli docs +media-download --token <image_token> --output <图片保存路径> --as user

# 3. 替换 Markdown 中的 image 标签为标准格式
# 将 <image token="boxcnXXX" width="N" height="N" align="center"/>
# 替换为 ![](Attachments/<文件名>.png)
```

### 图片保存位置

图片保存到文档同级的 `Attachments/` 目录下，文件名使用 token + 自动检测的扩展名：
```
4-Archives/Notes/Feishu/云空间/莱讯科技/项目运维管理/基础设施/
├── 系统架构图.md
└── Attachments/
    ├── Ccckbk2rCoBJ04xi6M3cNkQfnwc.png
    └── ...
```

Markdown 中引用图片使用相对路径：`![](Attachments/Ccckbk2rCoBJ04xi6M3cNkQfnwc.png)`

### 注意事项
- `docs +media-download` 会自动检测图片格式（png/jpg/gif 等）并添加正确扩展名
- 图片 token 以 `boxcn` 开头
- 部分旧文档的图片可能已过期无法下载，跳过即可
- doc 旧版文档通过导出 API 导出的 docx 文件中图片已内嵌，pandoc 转换时会自动提取

## 其他注意事项

- 飞书文档中的 @提及 会显示为用户 ID，无法自动转换为姓名
- 知识库节点可能有层级关系，迁移时保留为平铺结构，用 wikilink 关联
- 迁移完成后，原飞书文档不删除，保留作为备份
- doc 旧版文档通过导出 API + pandoc 转换，可能丢失部分格式
- mindnote 无法通过 API 导出，需手动在飞书界面导出为 FreeMind (.mm)
- slides 非本人文件，已跳过
