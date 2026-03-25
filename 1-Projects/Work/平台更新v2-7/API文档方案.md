---
title: API文档方案
type: reference
tags:
  - project/平台更新v2-7
created: 2026-03-24
modified: 2026-03-24
---

# API 文档整理方案

## 方案概述

使用 OpenAPI 3.0 规范维护 API 文档，分模块管理，支持多种格式输出和 OEM 定制交付。

## 技术选型

| 工具 | 用途 | 费用 |
|------|------|------|
| OpenAPI 3.0 YAML | 文档源文件格式 | 免费（规范） |
| `@redocly/cli` | 校验、合并、预览、生成 HTML | 免费开源 |
| Swagger UI | 在线调试页面 | 免费开源 |
| widdershins | 导出 Markdown | 免费开源 |
| Pandoc | Markdown → Word/PDF | 免费开源 |

## 项目结构

```
api-docs/
├── api.yaml                         # 标准版（完整，含 management）
├── api-external.yaml                # 对外版（不含 management）
├── api-oem-gzjc-gzjc.yaml          # OEM: 广州机场
├── api-oem-madinat-xmc.yaml        # OEM: 麦钉-洗煤厂
│
├── paths/                           # 通用接口模块
│   ├── device/
│   │   ├── tags.yaml                # /api/tags
│   │   └── anchors.yaml            # /api/anchors
│   ├── position/
│   │   ├── trackables.yaml          # /api/trackables
│   │   └── positions.yaml           # /api/positions
│   ├── map/
│   │   └── maps.yaml               # /api/maps
│   └── management/
│       └── users.yaml               # /api/management/users（内部）
│
├── paths/oem-gzjc-gzjc/            # 广州机场覆盖的路由
│   └── device/
│       └── tags.yaml
├── paths/oem-madinat-xmc/          # 麦钉覆盖的路由
│   └── position/
│       └── trackables.yaml
│
├── components/                      # 通用数据模型
│   └── schemas/
│       ├── Tag.yaml
│       ├── Anchor.yaml
│       ├── Trackable.yaml
│       ├── Position.yaml
│       └── Map.yaml
│
├── components/oem-gzjc-gzjc/       # 广州机场覆盖的 schema
│   └── schemas/
│       └── Tag.yaml
├── components/oem-madinat-xmc/      # 麦钉覆盖的 schema
│   └── schemas/
│       └── Trackable.yaml
│
├── swagger-ui/                      # Swagger UI 部署文件
│   └── index.html
│
└── redocly.yaml                     # Redocly CLI 配置
```

## 接口模块划分

| 模块 | 路由 | 说明 | 对外提供 |
|------|------|------|----------|
| management | /api/management/* | 用户管理、角色管理等 | ❌ 仅内部 |
| device | /api/tags, /api/anchors | 标签、基站设备管理 | ✅ |
| position | /api/trackables, /api/positions | 定位对象、位置数据 | ✅ |
| map | /api/maps | 地图管理 | ✅ |

## 授权方式

| 方式 | 类型 | 用途 | 覆盖模块 |
|------|------|------|----------|
| Bearer JWT | `http/bearer` | 内部系统 | 全部（含 management） |
| API Key | `apiKey/header` | 对外开放 | device / position / map |

在 `api.yaml` 中定义：

```yaml
components:
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer
      bearerFormat: JWT
      description: 内部系统使用，登录后获取 Token
    ApiKeyAuth:
      type: apiKey
      in: header
      name: X-API-Key
      description: 对外接口使用，在管理后台申请
```

## 主文件说明

### api.yaml — 标准完整版

包含所有模块（含 management），使用 Bearer JWT 授权，内部开发和调试用。

### api-external.yaml — 对外版

不含 management 模块，使用 API Key 授权，交付给客户的通用版本。

### api-oem-xxx.yaml — OEM 定制版

基于对外版，品牌信息替换为客户信息。有定制的路由/schema 引用 OEM 覆盖文件，其余引用通用模块。

## OEM 定制规则

- 有覆盖的路由 → 引用 `paths/oem-xxx/` 下的文件
- 有覆盖的 schema → 引用 `components/oem-xxx/` 下的文件
- 没有覆盖的 → 引用通用的 `paths/` 和 `components/`
- 不需要的接口 → 不写

### 新增 OEM 项目步骤

1. 复制一个现有 OEM 主文件，修改 `info` 中的品牌信息
2. 有定制的路由 → 在 `paths/oem-xxx/` 下建覆盖文件
3. 有定制的 schema → 在 `components/oem-xxx/` 下建覆盖文件
4. 没有定制的 → 不用动，自动用通用版

## 常用命令

```bash
# 本地预览文档
npx @redocly/cli preview-docs api.yaml

# 校验格式
npx @redocly/cli lint api.yaml

# 多文件合并成单文件
npx @redocly/cli bundle api.yaml -o dist/api-bundled.yaml

# 生成 Redoc HTML（好看，交付用）
npx @redocly/cli build-docs api.yaml -o dist/doc-standard.html
npx @redocly/cli build-docs api-external.yaml -o dist/doc-external.html
npx @redocly/cli build-docs api-oem-gzjc-gzjc.yaml -o dist/doc-gzjc.html

# 导出 Markdown
npx widdershins dist/api-bundled.yaml -o dist/api-doc.md

# Markdown 转 Word
pandoc dist/api-doc.md -o dist/api-doc.docx
```

## 输出格式对照

| 格式 | 工具链 | 用途 |
|------|--------|------|
| Swagger UI HTML | Swagger UI | 开发在线调试 |
| Redoc HTML | `@redocly/cli build-docs` | 交付客户（好看） |
| Markdown | widdershins | 内部存档 / Obsidian |
| Word (.docx) | widdershins + Pandoc | 正式文档交付 |

## 线上部署

Swagger UI 部署为静态文件，nginx 托管：

```
/var/www/api-docs/
├── index.html    # Swagger UI 页面
└── api.yaml      # OpenAPI 文件（bundle 后的单文件）
```

或使用 Docker：

```bash
docker run -d -p 8080:8080 \
  -e SWAGGER_JSON=/api/api.yaml \
  -v /path/to/api.yaml:/api/api.yaml \
  swaggerapi/swagger-ui
```

## Swagger UI 预设授权（仅开发环境）

在 `swagger-ui/index.html` 中可预设调试用的 Token：

```javascript
onComplete: function() {
  ui.preauthorizeApiKey('ApiKeyAuth', 'dev-api-key');
  ui.preauthorizeApiKey('BearerAuth', 'dev-jwt-token');
}
```

> ⚠️ 预设密钥仅限内部开发环境，不要提交到公开仓库或交付给客户。

## 部分交付

按需选择模块生成文档：

- 对外通用 → `api-external.yaml`（不含 management）
- OEM 客户 → `api-oem-xxx.yaml`（定制品牌 + 定制接口）
- 导出 Word 时可选择性合并 Markdown 文件

## 依赖安装

```bash
# Node.js（必须）
# 已有则跳过

# Pandoc（导出 Word 时需要）
brew install pandoc

# 其他工具通过 npx 直接运行，无需安装
```
