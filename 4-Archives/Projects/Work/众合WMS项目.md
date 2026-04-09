---
title: 众合WMS项目
type: archive
tags:
  - archive/项目
created: 2021-01-01
modified: 2021-12-31
---

# 众合WMS项目

UWB半自动库仓储管理系统，对接WCS系统，通过Android手环进行仓库作业指引。

## 系统介绍

系统是一个中间件，对接定位设备后端：
- 供上级WCS系统调用的接口
- 供下级Android手环设备调用
- 本地部署，无外网，远程支持困难
- 使用 Spring WebFlux 开发
- 代码仓库：https://github.com/reliablesense/WmsBackend

## 主要接口

1. 下发任务接口，调用设备后端发送message
2. 通过RabbitMQ上报当前位置（对接设备后端WebSocket，转换格式）
3. 通过RabbitMQ上报围栏出入时间
4. 任务确认接口
5. 服务器状态接口（供手环显示）
6. 转发UWB设备后端部分接口（围栏、定位标签相关）

## 代码维护要求

1. 检查代码潜在问题，保证长期运行
2. 重写输出日志，出问题时可追踪
3. 后续有接口调整

## 腕表与WCS通信协议

1. 腕表app与定位标签连接成功后，每隔5秒发送心跳包（含标签ID），10秒没收到则离线
2. 腕表app和定位标签绑定成功后，给WCS发送上线信息
3. WCS收到后返回确认，腕表才算正常连接，否则提示异常
4. 腕表和WCS之间有定时心跳，超时WCS主动下线该腕表
5. 增加WCS和腕表之间任务发送的确认信息
6. 腕表检测到标签连接异常时，主动给WCS下发下线指令
7. 标签ID通过指令包传递，不再写死在配置文件

## 已知问题

### WCS MQTT断连
UWB半自动库偶尔出现任务最后一步无法确认，原因是WCS与MQTT断开连接后没有重连，需重启WCS软件。

### 手环推送延迟
1. 出库时WMS推送信息到手表不顺利，只有一只手表能收到
2. 禁用定位移后仍推送信息，禁用功能失效
3. 定位移二维码打印放大后手表扫不了
4. 多个局反馈手环指令接收延迟、掉线

排查步骤：
1. 检查WCS是否成功调用了下发任务接口（查日志）
2. 检查下发任务的目标标签是否是当前手环绑定的标签
3. 检查下发任务时手环与蓝牙是否正常连接

### 现场问题反馈
- 云浮：其中一个标签出库入库时按钮没有变蓝色，可能定位不准
- 江门：有个标签经常充不上电

## 现场网络信息

- 192.168.40.10 / 255.255.255.0 / 192.168.40.254
- 10.150.229.223

## 电子墨水屏指令

```bash
# 入库
curl http://dev.wms.reliablesense.cn/EHCommon/ModularEink/EinkAPI/publishEink -X POST -d 'card_ids=3v1jaaMpR3a99m3myzhr4w&message=入库 \r\n从1号射频门到0001 数量1跺&type=0&time=0&voice=0&shake=1'

# 出库
curl http://dev.wms.reliablesense.cn/EHCommon/ModularEink/EinkAPI/publishEink -X POST -d 'card_ids=3v1jaaMpR3a99m3myzhr4w&message=出库 \r\n从0001到1号射频门 数量1跺&type=0&time=0&voice=0&shake=1'

# 盘点/拣选/移库 类似格式
```


## 地图样式 ID（Yuque 迁移）

| 元素 | ID |
|------|-----|
| 基站 | d85b2cc0-7165-45d6-8ea0-ccfa81044d76 |
| 房间 | 4cc4cc9a-878d-4f2e-840d-b4dcaf659b46 |
| 空库位 | 80807e4b-c610-4309-8d98-d157a1b3a837 |
| 可移动家具 | f77a31e2-1e0d-4d1f-8885-119c60488dae |
| 库位 | e1dd674a-f304-11ea-adc1-0242ac120002 |
| 绿墙 | 2262a85e-2205-4899-8bf7-756825de822d |
| 白墙 | bac7ffd9-0920-4161-b401-b9d337a49bbd |
| 墙-玻璃 | dac9290e-7d3c-4737-ad8f-7d59ac158073 |
| 门 | 25944d2d-eea6-4b93-aeed-19c74ee671ce |
| 桌子 | 49d168c6-c67f-4f15-af7a-e43055a1e91e |

墙 style 字段：
```json
{
  "color": "#FFFFFF",
  "height": 3,
  "base_height": 0
}
```
