---
title: 酒店App项目
type: archive
tags:
  - archive/项目
created: 2021-01-01
modified: 2021-12-31
---

# 酒店App项目

酒店定位App，提供完整注册登录系统，用户绑定定位对象，蓝牙AOA定位。

## 需求设计

### 用户系统
- 数据表 user：用户名、密码、性别、手机号、证件类型（身份证/护照）、证件号码
- ID 使用平台生成的 trackableId

### 管理后台接口（验证走平台）
1. 业务后端给所有返回 trackable 对象的接口补充用户字段（除密码外）
2. 密码修改接口 POST /api/trackables/password
3. 增删改查通过平台 /trackable 接口实现

### App接口（验证在业务后端独立实现）
1. 注册接口 POST /api/trackables/registration（不需要验证）
2. 登录接口 POST /api/trackables/sessions（不需要验证）
3. 密码修改接口 /api/trackables/password（需token验证）
4. 注销接口 DELETE /api/trackables/sessions（需token验证）

## App端修改清单

1. 注册页面去掉手机
2. 注册成功后自动登录，弹框提醒补充信息
3. Token持久化，启动时通过 /api/trackables/userinfo 检查有效性
4. Token失效则登出
5. 登录后检查 replacePassword 字段，为 true 则提示修改密码
6. 修改密码后不需要重新登录，结果返回新 token
7. 密码统一经过 SHA1 加密
8. 性别选择框：male→男性 / female→女性
9. 证件类型选择框：idcard→身份证 / passport→护照
10. 接入蓝牙库，登录后开始广播（设备唯一ID转换为0~65535数字）

## 设备绑定逻辑

1. 绑定接口 POST /api/trackables/bind，参数 { mobile: ios/android, address: `43544d41${hex}` }
2. 注册或登录后检查用户 tag 字段，如果 modules 里有匹配地址则跳过
3. 否则调用绑定接口，失败则弹窗重试或联系管理员

## BUG记录

1. nickName 保存成功但更新后没有显示
2. 信息页标题应显示用户名
3. 证件类型选择身份证应提交 cardId，护照提交 passport
4. 证件号输入框应允许英文字母，按类型校验格式
5. 性别提交值：male / female
6. 手机格式校验
7. 注册自动登录后提示修改密码，修改后又提示补充信息
8. 重置密码后第一次登录没提示修改密码，第二次才提示

## 工时估算

### PC端
- 消息：后端7人/天 + 前端7人/天 + 测试5人/天 = 19人/天
- 健康：后端7人/天 + 前端7人/天 + 测试5人/天 = 19人/天

### App端
- 消息：App 7人/天 + 测试5人/天 = 12人/天
- 健康：App 10人/天 + 测试5人/天 = 15人/天
- 注册登录：后端7人/天 + App 7人/天 + 测试5人/天 = 19人/天
- 导航偏好：后端7人/天 + App 5人/天 + 测试3人/天 = 15人/天
- 配对：后端1人/天 + App 1人/天 + 测试2人/天 = 4人/天
