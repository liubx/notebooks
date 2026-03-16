---
title: 定位平台WebSocket接口文档
type: knowledge-card
tags:
  - tech/api
  - tech/websocket
created: 2021-09-05
modified: 2026-03-16
---

# 定位平台 WebSocket 接口文档

室内外一体化定位平台的 WebSocket 接口定义。

## 位置上传

**Endpoint**: `ws://{hostname}/websocket/positionRelay/api/ws`

**Headers**:
- `apiKey` (必填): 工程的 API KEY
- `apiSecret` (必填): 工程的 apiSecret

**Channel**: `/position`

**Request 示例**:
```json
{
  "x": 0,
  "y": 0,
  "z": 0,
  "longitude": 116.5631329226788,
  "latitude": 39.78613241779979,
  "altitude": 0,
  "spaceId": 1,
  "floor": 1,
  "mapId": 1,
  "timestamp": 1630787430629,
  "schema": "reliablesense_demo",
  "code": "23324324234",
  "type": "CORELOCATION_AOA"
}
```

## 位置监听

**Endpoint**: `ws://{hostname}/websocket/position/api/ws`

**订阅地址**: `/topic/position/{apiKey}`

**Headers**: 同上

**推送数据格式**: 同位置上传 Request

## 告警监听

**Endpoint**: `ws://{hostname}/websocket/alarm/api/ws`

**订阅地址**: `/topic/alarm/{apiKey}`

**Headers**: 同上

**推送数据示例**:
```json
{
  "id": 20,
  "active": true,
  "trackableId": "427edba3-b3c9-439f-852a-4b36d93803b5",
  "relatedId": "b36d8c7a-822e-4903-ac07-165b81986d45",
  "description": "离开了限出电子围栏围栏",
  "type": {
    "id": 1,
    "name": "围栏告警",
    "enable": true
  },
  "name": "围栏告警",
  "typeId": 1,
  "floor": 0,
  "mapId": 0,
  "spaceId": 0,
  "longitude": 116.55448499045343,
  "latitude": 39.786107929063707,
  "altitude": 0.0,
  "startTime": "2021-09-04T21:03:27.582884Z",
  "endTime": null,
  "trackable": {
    "id": "427edba3-b3c9-439f-852a-4b36d93803b5",
    "name": "testTrack",
    "trackableTypeIds": [1],
    "trackableTypes": [{"id": 1, "name": "人员", "uid": "PEOPLE"}]
  },
  "related": {
    "id": "b36d8c7a-822e-4903-ac07-165b81986d45",
    "name": "限出电子围栏",
    "geoJson": "{\"type\":\"Polygon\",\"coordinates\":[...]}",
    "type": "KEEP_IN",
    "enable": true,
    "activeMode": "ALWAYS"
  },
  "schema": "reliablesense_demo"
}
```

---
*来源：语雀 - 室内外一体化微服务文档*
