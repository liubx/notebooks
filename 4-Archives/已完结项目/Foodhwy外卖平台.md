---
title: Foodhwy外卖平台
type: archived-project
status: 已完结
period: 2016-2019
company: Foodhwy
tags:
  - project/foodhwy
  - 已完结
created: 2026-03-16
modified: 2026-03-16
---

# 项目概述

加拿大华人外卖配送平台，基于 PHP/Laravel 后端 + React Native 移动端开发。

# 技术栈

- 后端：PHP / Laravel
- 前端：React Native（iOS/Android）
- 数据库：MySQL
- 支付：微信支付（App支付）
- 部署：DigitalOcean / 阿里云

# 服务器配置

- 测试站：https://foodhwy.net/
- 测试后台：http://foodhwy.net/admin
- 测试接口：http://php7.foodhwy.net/api
- 正式站点：https://wechat.foodhwy.com / https://foodhwy.passquan.com/
- 正式后台：https://wechat.foodhwy.com/admin/
- 正式接口：https://wechat.foodhwy.com/api/

# 本地开发环境

hosts 配置：
```
# project.foodhwy.com
127.0.0.1    foodhwy.com / foodhwy.net / phpmyadmin.foodhwy.com / phpredisadmin.foodhwy.com
```

# 角色权限体系

| 角色 | 常量 | 说明 |
|------|------|------|
| 匿名用户 | ROLE_ANONYMOUS = 0 | |
| 职员 | ROLE_STAFF = 10 | |
| 配送员 | ROLE_DELIVERER = 20 | |
| 店铺管理员 | ROLE_SHOP = 30 | |
| 部门管理员 | ROLE_SEGMENT = 35 | |
| 调度员 | ROLE_DISPATCH = 36 | |
| 地区负责人 | ROLE_AREA = 37 | |
| 平台管理员 | ROLE_BRAND = 40 | |
| 后台管理 | ROLE_SUPER = 60 | |

# 微信App支付流程

1. 服务器向 OTT 发支付请求，返回调起微信支付参数
2. App 拿到参数后加上 App Sign 发送给微信，调起微信支付
3. App 接受微信回调结果，显示支付成功或失败
4. 服务器通过 callback_url 接收支付结果，更新订单状态

# 排班系统

- 每个区域可配置排班时间段和每个时间段容许排班的数量
- 排班页面根据区域设定限制添加司机排班操作

# 调度数据接口

需要的数据：当前司机数量、进行中订单数量、已晚单数量、SA压力指数、平均晚单率、晚单总时长

---
*来源：Apple Notes 2019 年笔记迁移*


# 客服系统实施（Yuque 迁移）

选择 Kommunicate 作为客服系统。

## 整体流程

1. 用户/司机/商家在 App 中点击客服入口
2. 判断订单是否已分配会话 conversationId
3. 已分配则进入该会话，未分配则创建新会话
4. 发送请求关联会话和订单，下发订单卡片信息
5. 客服发送「邀请司机」时，推送给订单所分配司机

## 后端 API

```
POST /api/customer_service                        # 客户端
POST /api/hybrid/driver/customer_service/order    # 司机端
POST /api/hybrid/merchant/customer_service/order  # 商家端
GET  /api/customer_service                        # 获取会话
GET  /webhook/customer_service/forword            # Webhook
```

## 开发完成情况

### 后端 `feature/kommunicate`
- [x] 修改数据库，添加 conversation_id 字段到 order 表
- [x] 添加 startOrderConversation 接口
- [x] 添加 getOrderConversation 接口
- [x] 添加 Webhook 接收 Kommunicate 信息
- [x] 添加「邀请司机」推送逻辑

### 客户端
- [x] Android 端：我的页面通用客服入口 + 订单详情页客服入口
- [ ] iOS 端：待开发

### 司机端 `feature/kommunicate`
- [x] Android 端：设置页通用客服入口 + 订单详情页客服入口
- [x] iOS 端：设置页通用客服入口 + 订单详情页客服入口

### 商家端 `feature/kommunicate`
- [x] Android 端：设置页通用客服入口 + 订单详情页客服入口
- [x] iOS 端：设置页通用客服入口 + 订单详情页客服入口

## 遗留问题

- 商家端/司机端/客户端入口按钮图标和文案样式需要调整
- 用户 iOS 端 Kommunicate 接入待开发
- 推送功能需要测试（Webhook 接口填写到 Kommunicate 后台）
- 司机加入会话后只能看到之前的对话记录，不能发送消息和接收新消息

---
*来源：语雀 - LB个人知识库/Foodhwy/客服系统*
