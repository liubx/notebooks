---
title: Fishbowl 对接方案
type: note
tags:
  - project/PN仓库项目
created: 2026-04-04
modified: 2026-04-04
---

# Fishbowl 对接方案

## 1. Fishbowl 是什么

Fishbowl 是一款本地部署（on-premise）的仓储管理系统（WMS），客户在多伦多仓库使用它管理库存、采购单、销售单等。它提供 REST API 用于第三方集成。

## 2. 对接目标

我们的定位系统（叉车 RFID + 激光雷达）负责仓库内的实时定位和出入库操作，Fishbowl 负责业务层面的库存管理。对接的核心目标是：

- 叉车入库完成 → 同步更新 Fishbowl 库存位置
- 叉车出库完成 → 同步更新 Fishbowl 出库状态
- 叉车移库完成 → 同步更新 Fishbowl 库位变更
- 从 Fishbowl 拉取待处理的出库单/入库单，作为叉车任务来源

## 3. Fishbowl REST API 概览

### 3.1 连接方式

- 基础 URL：`http://{FISHBOWL_SERVER}:{PORT}/api`（默认端口 2456）
- 认证：`POST /api/session` 获取 Bearer Token，后续请求带 `Authorization: Bearer <TOKEN>`
- 数据格式：JSON
- HTTP 方法：GET / POST / DELETE
- 分页：大部分列表接口返回 `totalCount`、`totalPages`、`pageNumber`、`pageSize`、`results`

### 3.2 核心 API 端点

| 模块 | 端点 | 方法 | 说明 |
|------|------|------|------|
| 认证 | `/api/session` | POST | 登录获取 Token |
| 零件/物料 | `/api/parts` | GET | 查询零件列表（分页） |
| 库存 | `/api/parts/inventory` | GET | 查询库存（按零件维度） |
| 产品 | `/api/products` | GET | 查询产品列表 |
| 采购单 | `/api/purchase-orders` | GET/POST | 查询/创建采购单 |
| 采购单操作 | `/api/purchase-orders/:id/issue` | POST | 签发采购单 |
| 采购单操作 | `/api/purchase-orders/:id/void` | POST | 作废采购单 |
| 采购单操作 | `/api/purchase-orders/:id/close-short` | POST | 短关采购单 |
| 销售单 | `/api/sales-orders/:id` | DELETE | 删除销售单 |
| 位置组 | `/api/location-groups` | GET | 查询仓库位置组 |
| 制造单 | `/api/manufacture-orders` | GET/POST | 制造工单管理 |
| 插件集成 | `/api/integrations/plugin-info` | GET/POST/DELETE | 第三方插件数据关联 |
| 数据导入 | `/api/import/:name` | POST | CSV/JSON 批量导入 |
| 数据查询 | `/api/data-query` | GET | 直接执行 SQL 查询 |

### 3.3 关键数据模型

**零件（Part）**：
```json
{
  "id": 29,
  "number": "FG2100",
  "description": "Extreme Mountain Bike",
  "type": "Inventory",
  "uom": { "id": 1, "name": "Each", "abbreviation": "ea" },
  "upc": "",
  "active": true,
  "hasBom": true,
  "hasTracking": true,
  "tracksSerialNumbers": true
}
```

**库存（Inventory）**：
```json
{
  "id": 28,
  "partNumber": "B201",
  "quantity": "242",
  "partDescription": "Premium Brake Cables",
  "uom": { "id": 1, "name": "Each", "abbreviation": "ea" }
}
```

**采购单（Purchase Order）**：包含 vendor、poItems（明细行）、locationGroup、状态流转（Bid Request → Issued → Picking → Fulfilled → Closed）等。

## 4. 对接方案

### 4.1 数据映射

| 我们的系统 | Fishbowl | 说明 |
|-----------|----------|------|
| 货物（Trackable） | Part / Product | 通过 RFID 标签关联到 Fishbowl 的零件编号 |
| 货位（Shelf，如 5-A15-13-1） | Location | Fishbowl 的 Location 需要与我们的货位编号建立映射 |
| 仓库 | Location Group | 一个仓库对应一个 Location Group |
| 入库操作 | Receive（采购单收货） | 入库完成后更新 Fishbowl 库存位置 |
| 出库操作 | Pick / Ship（销售单拣货/发货） | 出库完成后更新 Fishbowl 出库状态 |
| 移库操作 | Transfer Order / Move | 移库完成后更新 Fishbowl 库位 |

### 4.2 对接架构

```
┌─────────────────┐         ┌──────────────────┐         ┌─────────────────┐
│  叉车 Android    │  HTTP   │  我们的后端服务    │  HTTP   │  Fishbowl       │
│  (RFID+定位)     │ ──────→ │  (中间层)         │ ──────→ │  REST API       │
│                  │         │                   │         │  :2456          │
└─────────────────┘         └──────────────────┘         └─────────────────┘
```

建议在我们的后端服务中增加 Fishbowl 适配层，而不是让 Android 端直接调用 Fishbowl API。原因：
- Fishbowl 是本地部署，网络拓扑可能复杂
- 需要做数据转换和业务逻辑编排
- Token 管理和错误重试集中处理
- 可以做操作日志和审计

### 4.3 核心对接流程

#### 流程一：入库同步

```
叉车入库完成（CHECKIN → CHECKOUT）
  → 我们的后端收到入库请求
  → 调用 Fishbowl API：
    1. 查询 Part（通过 RFID → 零件编号映射）
    2. 通过 Import API 导入收货记录（Receiving）
       或通过 data-query 执行 SQL 更新库存位置
  → 返回结果给叉车端
```

#### 流程二：出库同步

```
叉车出库完成（CHECKOUT → CHECKEDOUT）
  → 我们的后端收到出库请求
  → 调用 Fishbowl API：
    1. 查询关联的 Sales Order / Pick
    2. 通过 Import API 更新拣货/发货状态
  → 返回结果给叉车端
```

#### 流程三：移库同步

```
叉车移库完成（CHECKOUT → CHECKOUT，位置变更）
  → 我们的后端收到移库请求
  → 调用 Fishbowl API：
    1. 通过 Import API 导入 Transfer Order
       或通过 data-query 更新库存位置
  → 返回结果给叉车端
```

#### 流程四：任务拉取

```
定时/触发拉取 Fishbowl 待处理单据
  → 调用 GET /api/purchase-orders?status=Issued（待收货的采购单）
  → 转换为我们系统的任务格式（Trackable + 状态 CHECKIN）
  → 叉车端 fetchTasks 时获取
```

### 4.4 Import API 的使用

Fishbowl 的 Import API 是最灵活的数据写入方式，支持 CSV 和 JSON 格式：

```bash
# JSON 格式导入示例
POST /api/import/Location-Transfer
Content-Type: application/json
Authorization: Bearer <TOKEN>

[
  ["Part Number", "From Location", "To Location", "Quantity", "Tracking"],
  ["B201", "5-A15-13-1", "5-B03-05-2", "1", "SN12345"]
]
```

常用的 Import 名称（需要确认客户 Fishbowl 版本支持哪些）：
- `Location-Transfer` — 库位转移
- `Inventory-Quantity` — 库存数量调整
- `Sales-Order-Details` — 销售单明细

### 4.5 Data Query API

Fishbowl 支持直接执行 SQL 查询，这是最强大但也最危险的接口：

```bash
GET /api/data-query
Content-Type: application/sql
Authorization: Bearer <TOKEN>

SELECT p.num, i.qty, l.name as location
FROM part p
JOIN inventory i ON p.id = i.partId
JOIN location l ON i.locationId = l.id
WHERE p.num = 'B201'
```

适合用于：
- 查询库存位置详情
- 验证数据一致性
- 获取 REST API 未直接暴露的数据

## 5. 需要跟客户确认的事项

### 5.1 环境信息
- [ ] Fishbowl 服务器地址和端口（默认 2456）
- [ ] Fishbowl 版本号（API 文档随版本变化，可在 `http://{server}:{port}/apidocs` 查看）
- [ ] 是否使用 HTTPS（需要证书配置）
- [ ] API 用户账号和权限（需要 Inventory、Parts、Purchase Orders 等模块权限）

### 5.2 业务映射
- [ ] 客户的 Location 编号规则是什么？如何与我们的货位编号（如 5-A15-13-1）对应？
- [ ] 客户的 Part Number 如何与我们的 RFID 标签关联？是否有条码/序列号对应关系？
- [ ] 客户使用哪些单据类型？（Purchase Order 收货、Sales Order 发货、Transfer Order 移库）
- [ ] 客户是否使用 Tracking（序列号追踪）？
- [ ] 出库是基于 Sales Order 还是其他单据？

### 5.3 技术细节
- [ ] Fishbowl 服务器是否在客户内网？我们的后端服务如何访问？（VPN / 公网映射 / 部署在同一网络）
- [ ] 是否需要实时同步还是可以批量同步？
- [ ] 数据冲突处理策略（如 Fishbowl 端手动修改了库存，如何与我们的系统保持一致）

## 6. 开发计划建议

### 第一阶段：基础对接（2-3 周）
1. 搭建 Fishbowl API 客户端（认证、基础 CRUD）
2. 实现 Location 映射（我们的货位 ↔ Fishbowl Location）
3. 实现 Part 映射（RFID 标签 ↔ Fishbowl Part Number）
4. 库存查询接口对接

### 第二阶段：业务流程对接（2-3 周）
1. 入库同步（收货 → Fishbowl 库存更新）
2. 出库同步（发货 → Fishbowl 状态更新）
3. 移库同步（Transfer → Fishbowl 位置更新）
4. 任务拉取（从 Fishbowl 获取待处理单据）

### 第三阶段：完善和测试（1-2 周）
1. 异常处理和重试机制
2. 数据一致性校验
3. 联调测试

## 7. 参考资料

- [Fishbowl REST API 文档](https://help.fishbowlinventory.com/advanced/s/apidocs/introduction.html)（在线版本，实际以客户服务器上的版本为准）
- [Fishbowl REST API - 连接说明](https://help.fishbowlinventory.com/advanced/s/apidocs/connecting.html)
- [Fishbowl REST API - 库存](https://help.fishbowlinventory.com/advanced/s/apidocs/inventory.html)
- [Fishbowl REST API - 采购单](https://help.fishbowlinventory.com/advanced/s/apidocs/purchaseorders.html)
- [Fishbowl REST API - 导入导出](https://help.fishbowlinventory.com/advanced/s/apidocs/importsandexports.html)
- [Fishbowl REST API - 数据查询](https://help.fishbowlinventory.com/advanced/s/apidocs/importsandexports.html)（data-query 端点）
- [Fishbowl REST API - 位置组](https://help.fishbowlinventory.com/advanced/s/apidocs/locationgroups.html)
- [Fishbowl REST API - 插件集成](https://help.fishbowlinventory.com/advanced/s/apidocs/integrations.html)

> 注意：Fishbowl 的 REST API 文档会随版本更新，客户服务器上可以通过 `http://{server}:{port}/apidocs` 访问与其版本匹配的完整文档。在线文档是示例版本，可能与客户实际版本有差异。
