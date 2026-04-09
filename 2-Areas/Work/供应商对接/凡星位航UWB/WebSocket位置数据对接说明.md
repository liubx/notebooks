---
title: UWB 定位引擎 WebSocket 位置数据对接说明
created: 2026-04-08
tags:
  - type/供应商对接
---

# UWB 定位引擎 — WebSocket 位置数据对接说明

> 本文档描述 UWB 定位引擎通过 WebSocket 推送位置数据的接口协议，供第三方平台对接使用。

## 1. 连接方式

- 协议：WebSocket，数据格式 JSON
- 角色：**定位引擎为 Client，第三方平台为 Server**
- 引擎启动后主动连接平台的 WebSocket 地址，重连间隔 5 秒
- 连接地址在引擎配置文件中配置，示例：
  ```
  websocketserverurl = ws://192.168.1.100:1234
  ```

## 2. 基站信息（MsgType: 1）

连接成功后以及基站状态发生变化时，引擎会推送基站信息。

### 报文结构

```json
{
  "MsgType": 1,
  "AncList": [
    {
      "AncId": 2090,
      "Online": 1,
      "Ready": 1,
      "MapId": 1,
      "Floor": 1,
      "X": 30.15,
      "Y": 15.22,
      "Z": 1.51,
      "Ip": "192.168.2.100",
      "Port": 32121
    }
  ]
}
```

### 字段说明

| 字段 | 类型 | 必须 | 说明 |
|------|------|------|------|
| AncId | 数字 | ✅ | 基站编号 |
| Online | 数字 | ✅ | 0=离线，1=在线 |
| Ready | 数字 | ✅ | 0=未配置，1=已配置（目前总是为1） |
| MapId | 数字 | ✅ | 基站所在地图编号 |
| X / Y / Z | double | ✅ | 基站坐标，单位米 |
| Floor | 数字 | ❌ | 楼层，默认1 |
| Ip | 字符串 | ✅ | 基站 IPv4 地址 |
| Port | 数字 | ✅ | 基站 IPv4 端口 |

### 完整示例

```json
{"MsgType":1, "AncList":[
  {"AncId":2090,"Online":1,"Ready":1,"MapId":1,"Floor":1,"X":30.15,"Y":15.22,"Z":1.51,"Ip":"192.168.2.100","Port":32121},
  {"AncId":2091,"Online":0,"Ready":1,"MapId":2,"Floor":1,"X":-0.15,"Y":-15.22,"Z":2.2,"Ip":"192.168.2.99","Port":55311}
]}
```

## 3. UWB 定位信息（MsgType: 2）

实时推送，每当有新定位数据产生就会发送。一条消息可包含多个标签的定位信息。

### 报文结构

```json
{
  "MsgType": 2,
  "TagList": [
    {
      "TagId": 1099,
      "IsMeter": 0,
      "X": 30150,
      "Y": 15220,
      "Z": 1510,
      "StaticTime": 10,
      "MapId": 1,
      "Floor": 1,
      "Battery": 100,
      "BuildName": "氨区",
      "BuildId": "1"
    }
  ]
}
```

### 字段说明

| 字段 | 类型 | 必须 | 说明 |
|------|------|------|------|
| TagId | 数字 | ✅ | 标签编号 |
| IsMeter | 数字 | ❌ | 0=XYZ为毫米整数，1=XYZ为米制double。缺省视为0 |
| X / Y / Z | 数字/double | ✅ | 坐标值，单位由IsMeter决定 |
| StaticTime | 数字 | ✅ | 标签静止状态持续时长（秒） |
| MapId | 数字 | ✅ | 标签所在地图编号 |
| Floor | 数字 | ❌ | 楼层，默认1 |
| Battery | 数字 | ✅ | 电池电量 0~100 |
| BuildName | 字符串 | ❌ | 所属建筑名称，不属于任何建筑时为空字符串 |
| BuildId | 字符串 | ❌ | 所属建筑ID，不属于任何建筑时为空字符串 |

### 坐标单位说明

- `IsMeter=0`（或字段缺失）：XYZ 坐标为**毫米**整数
- `IsMeter=1`：XYZ 坐标为**米**制 double 浮点数
### 完整示例

```json
{"MsgType":2, "TagList":[
  {"StaticTime":10,"Battery":100,"TagId":1099,"IsMeter":0,"X":30150,"Y":15220,"Z":1510,"MapId":1,"Floor":1,"BuildName":"氨区","BuildId":"1"},
  {"StaticTime":0,"Battery":99,"TagId":1101,"IsMeter":1,"X":-30.15001,"Y":-15.2201,"Z":1.5101,"MapId":1,"Floor":1,"BuildName":"","BuildId":""}
]}
```

> 标签1099：IsMeter=0，坐标 (30150, 15220, 1510) 单位 mm
> 标签1101：IsMeter=1，坐标 (-30.15, -15.22, 1.51) 单位 m

## 4. 对接要点

1. **启动 WebSocket Server** 监听指定端口，等待引擎主动连接
2. 收到消息后根据 `MsgType` 字段判断类型，`MsgType=2` 即为 UWB 定位数据
3. 遍历 `TagList` 数组获取每个标签的实时坐标
4. 注意检查 `IsMeter` 字段以正确处理坐标单位
