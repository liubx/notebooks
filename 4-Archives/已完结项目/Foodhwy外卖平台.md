---
title: Foodhwy外卖平台
type: archived-project
status: 已完结
period: 2016-2019
company: Foodhwy / 51.CA
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
