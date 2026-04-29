---
title: 综合定位与TCDM对接流程图
tags:
  - 广州机场
  - 流程图
  - TCDM
created: 2026-04-14
---

# 综合定位与 TCDM 对接流程图

## 流程说明

综合定位系统通过 RocketMQ 消费 TCDM 推送的排班（SDDL）和打卡（SDUE）数据，筛选外部单位 + T3 打卡地的有效数据写入数据库。

## 流程图

```mermaid
flowchart TD
    A([启动消费者服务]) --> B["配置 RocketMQ Consumer<br/>订阅 Topic: 打卡/排班"]
    B --> C[/监听 MQ 消息/]
    C --> D[解析消息体]
    D --> E{消息类型判断}

    E -->|SDDL 排班数据| F{"组织是否为外部单位<br/>AND<br/>打卡地是否为T3?"}
    E -->|SDUE 打卡数据| G{"组织是否为外部单位<br/>AND<br/>打卡地是否为T3?"}
    E -->|未知类型| H[记录日志跳过]

    F -->|是| I[写入 DB 排班表]
    F -->|否| J["丢弃消息<br/>记录日志"]

    G -->|是| K[写入 DB 打卡表]
    G -->|否| L["丢弃消息<br/>记录日志"]

    I --> M([返回 ConsumeSuccessly])
    J --> M
    K --> M
    L --> M
    H --> M

    M -.-> C
```

## 关键节点说明

| 节点 | 说明 |
|------|------|
| Topic | TCDM 通过 RocketMQ 推送排班和打卡两类消息 |
| SDDL | 排班数据消息类型标识 |
| SDUE | 打卡数据消息类型标识 |
| 外部单位过滤 | 只处理外部单位（非机场内部员工）的数据 |
| T3 打卡地过滤 | 只处理 T3 航站楼相关的打卡地点数据 |
| ConsumeSuccessly | 无论是否写入 DB，均返回消费成功，避免消息重复投递 |

---

## TCDM 调用综合定位接口

```mermaid
flowchart TD
    A[TCDM 业务事件] --> B{事件类型}

    B -->|新员工入职| C[postTrackables<br/>新建定位对象]
    C --> D[bindTrackables<br/>绑定对象及设备]

    B -->|员工离职| E[unbindTrackables<br/>解绑设备]
    E --> E2[deleteTrackables<br/>删除定位对象]

    B -->|新增单位| F[postTagTypes<br/>新建标签类型]
    F --> G[自动创建 label]
    G --> H[绑定对象区分单位]
    F --> I[分配未分配设备]

    B -->|删除单位| J[deleteTagTypes<br/>删除标签类型]
    J --> K[设备回流至委外人员]
    J --> L[同步删除 label]

    B -->|考勤打卡| M[getFencesCheckInside<br/>判断是否在考勤区域]
    M -->|在区域内| N[符合打卡条件]
    M -->|不在区域内| O[不符合打卡条件]
```

---

## 接口汇总

| 接口 | 方向 | 说明 |
|------|------|------|
| `/XIY/LBS/postTrackables` | TCDM → 综合定位 | 新建定位对象 |
| `/XIY/LBS/bindTrackables` | TCDM → 综合定位 | 批量绑定定位对象及设备 |
| `/XIY/LBS/deleteTrackables` | TCDM → 综合定位 | 删除定位对象 |
| `/XIY/LBS/postTagTypes` | TCDM → 综合定位 | 新建定位标签类型 |
| `/XIY/LBS/deleteTagTypes` | TCDM → 综合定位 | 删除定位标签类型 |
| `/XIY/LBS/getFencesCheckInside` | TCDM → 综合定位 | 判断人员是否在考勤区域内 |
| RocketMQ (SDDL/SDUE) | TCDM → 综合定位 | 推送排班及打卡数据 |
