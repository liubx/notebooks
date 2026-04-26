---
title: "AESB总线业务联调方案"
source: feishu
feishu_token: "FM2hdCBaqo3humx0p1ccd8a9nKc"
feishu_type: docx
feishu_url: "https://reliablesense.feishu.cn/docx/FM2hdCBaqo3humx0p1ccd8a9nKc"
migrated: 2026-03-24
tags:
  - feishu-migration
---








**AESB总线** {align="center"}
**业务联调测试方案** {align="center"}




**工程名称：**<text underline="true">广州白云国际机场三期扩建工程T3航站楼及货运区民航弱电系统工程（二标段）</text>
**施工单位：**<text underline="true">民航成都电子技术有限责任公司</text>
**编制人：**<text underline="true">**                                    **</text>
**审核人（项目经理）：**<text underline="true">**                        **</text>
**审批人（技术负责人）：**<text underline="true">**                      **</text>
**日期： **

**目录** {align="center"}
1. 文档信息3
1.1. 文档基本信息3
1.2. 文档修订信息3
2. 概述4
2.1. 测试目的4
2.2. 测试范围及说明4
3. 参与人员及职责6
4. 测试环境8
4.1. 总体说明8
4.2. 测试环境条件清单8
5. 测试场景及流程8
5.1. 测试场景8
5.1.1. 生产业务8
5.1.2. 能力中台21
5.1.3. 服务业务24
5.1.4. 交通业务28
5.1.5. 安防业务34
5.1.6. 运维业务36
5.1.7. 商业业务37
5.1.8. 集团业务38
5.2. 测试流程39
5.2.1. API接口联调测试流程39
5.2.2. MQ接口联调测试流程41
6. 测试结论42
6.1. 测试问题42
6.2. 解决措施43
6.3. 测试结果44
7. 附件44
7.1. 测试记录表（单独提供）44
7.2. 测试过程截图（附简单文字说明）44
# 文档信息
## 文档基本信息
本文档由企业服务总线EASB编制，用于AESB总线平台联调测试工作，未经公司书面许可，不能以任何理由复制、使用或泄漏本文件的全部或部分内容。
## 文档修订信息

<lark-table rows="10" cols="5" column-widths="106,122,105,161,278">

  <lark-tr>
    <lark-td>
      标题
    </lark-td>
    <lark-td colspan="4">
      AESB总线业务联调测试方案
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      项目名称
    </lark-td>
    <lark-td colspan="4">
      广州白云国际机场三期扩建工程T3航站楼及货运区民航弱电系统工程（二标段）
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      类别
    </lark-td>
    <lark-td colspan="4">
      规范文档 □设计方案 □实施文档 □
      配置文档 □测试文档 ■需求分析 □
      其    他 □
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      摘要
    </lark-td>
    <lark-td colspan="4">
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      当前版本
    </lark-td>
    <lark-td colspan="4">
      1.0
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      文档作者
    </lark-td>
    <lark-td colspan="4">
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      版本号
    </lark-td>
    <lark-td>
      日期
    </lark-td>
    <lark-td>
      修改人
    </lark-td>
    <lark-td>
      审阅人
    </lark-td>
    <lark-td>
      摘要
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
    </lark-td>
    <lark-td>
    </lark-td>
    <lark-td>
    </lark-td>
    <lark-td>
    </lark-td>
    <lark-td>
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
    </lark-td>
    <lark-td>
    </lark-td>
    <lark-td>
    </lark-td>
    <lark-td>
    </lark-td>
    <lark-td>
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
    </lark-td>
    <lark-td>
    </lark-td>
    <lark-td>
    </lark-td>
    <lark-td>
    </lark-td>
    <lark-td>
    </lark-td>
  </lark-tr>
</lark-table>

---


# 概述
## 测试目的
在测试环境验证云计算平台AESB总线服务为应用系统提供的API接口、MQ接口数据调用的服务功能。
## 测试范围及说明
AESB总线与其他业务系统存在接口调用的场景（登录认证、组织/用户数据同步）

<lark-table rows="61" cols="8" column-widths="55,209,86,93,98,92,95,89">

  <lark-tr>
    <lark-td rowspan="2">
      **序号** {align="center"}
    </lark-td>
    <lark-td rowspan="2">
      **系统名称**
    </lark-td>
    <lark-td rowspan="2">
      **系统架构** {align="center"}
    </lark-td>
    <lark-td colspan="2">
      **API接口集成** {align="center"}
    </lark-td>
    <lark-td colspan="2">
      **MQ接口集成** {align="center"}
    </lark-td>
    <lark-td rowspan="2">
      **接入总线** {align="center"}
      **情况** {align="center"}
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      **是否集成** {align="center"}
    </lark-td>
    <lark-td>
      **集成协议** {align="center"}
    </lark-td>
    <lark-td>
      **是否集成** {align="center"}
    </lark-td>
    <lark-td>
      **集成协议** {align="center"}
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      1 {align="center"}
    </lark-td>
    <lark-td>
      <text bgcolor="yellow">机场地理信息系统</text>
    </lark-td>
    <lark-td>
      B/S {align="center"}
    </lark-td>
    <lark-td>
      是 {align="center"}
    </lark-td>
    <lark-td>
      HTTP {align="center"}
    </lark-td>
    <lark-td>
      否 {align="center"}
    </lark-td>
    <lark-td>
      / {align="center"}
    </lark-td>
    <lark-td>
      已接入
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      2 {align="center"}
    </lark-td>
    <lark-td>
      <text bgcolor="yellow">高精度综合定位系统</text>
    </lark-td>
    <lark-td>
      B/S {align="center"}
    </lark-td>
    <lark-td>
      是 {align="center"}
    </lark-td>
    <lark-td>
      HTTP {align="center"}
    </lark-td>
    <lark-td>
      是 {align="center"}
    </lark-td>
    <lark-td>
      RocketMQ {align="center"}
    </lark-td>
    <lark-td>
      待接入
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      3 {align="center"}
    </lark-td>
    <lark-td>
      <text bgcolor="yellow">物联网平台</text>
    </lark-td>
    <lark-td>
      B/S {align="center"}
    </lark-td>
    <lark-td>
      是 {align="center"}
    </lark-td>
    <lark-td>
      HTTP {align="center"}
    </lark-td>
    <lark-td>
      是 {align="center"}
    </lark-td>
    <lark-td>
      RocketMQ {align="center"}
    </lark-td>
    <lark-td>
      已接入
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      4 {align="center"}
    </lark-td>
    <lark-td>
      <text bgcolor="yellow">旅客服务平台</text>
    </lark-td>
    <lark-td>
      B/S {align="center"}
    </lark-td>
    <lark-td>
      是 {align="center"}
    </lark-td>
    <lark-td>
      HTTP {align="center"}
    </lark-td>
    <lark-td>
      否 {align="center"}
    </lark-td>
    <lark-td>
      / {align="center"}
    </lark-td>
    <lark-td>
      已接入
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      5 {align="center"}
    </lark-td>
    <lark-td>
      <text bgcolor="yellow">离港系统（电子告知书）</text>
    </lark-td>
    <lark-td>
      B/S {align="center"}
    </lark-td>
    <lark-td>
      是 {align="center"}
    </lark-td>
    <lark-td>
      HTTP {align="center"}
    </lark-td>
    <lark-td>
      否 {align="center"}
    </lark-td>
    <lark-td>
      / {align="center"}
    </lark-td>
    <lark-td>
      已接入
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      6 {align="center"}
    </lark-td>
    <lark-td>
      全场设备及能源管理系统
    </lark-td>
    <lark-td>
      B/S {align="center"}
    </lark-td>
    <lark-td>
      是 {align="center"}
    </lark-td>
    <lark-td>
      HTTP {align="center"}
    </lark-td>
    <lark-td>
      否 {align="center"}
    </lark-td>
    <lark-td>
      / {align="center"}
    </lark-td>
    <lark-td>
      已接入
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      7 {align="center"}
    </lark-td>
    <lark-td>
      <text bgcolor="yellow">机场运行信息集成系统</text>
    </lark-td>
    <lark-td>
      B/S {align="center"}
    </lark-td>
    <lark-td>
      否 {align="center"}
    </lark-td>
    <lark-td>
      / {align="center"}
    </lark-td>
    <lark-td>
      是 {align="center"}
    </lark-td>
    <lark-td>
      RocketMQ {align="center"}
    </lark-td>
    <lark-td>
      已接入
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      8 {align="center"}
    </lark-td>
    <lark-td>
      <text bgcolor="yellow">公共广播系统</text>
    </lark-td>
    <lark-td>
      B/S {align="center"}
    </lark-td>
    <lark-td>
      是 {align="center"}
    </lark-td>
    <lark-td>
      HTTP {align="center"}
    </lark-td>
    <lark-td>
      否 {align="center"}
    </lark-td>
    <lark-td>
      / {align="center"}
    </lark-td>
    <lark-td>
      已接入
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      9 {align="center"}
    </lark-td>
    <lark-td>
      <text bgcolor="yellow">航班信息显示系统</text>
    </lark-td>
    <lark-td>
      B/S {align="center"}
    </lark-td>
    <lark-td>
      是 {align="center"}
    </lark-td>
    <lark-td>
      HTTP {align="center"}
    </lark-td>
    <lark-td>
      是 {align="center"}
    </lark-td>
    <lark-td>
      RocketMQ {align="center"}
    </lark-td>
    <lark-td>
      已接入
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      10 {align="center"}
    </lark-td>
    <lark-td>
      <text bgcolor="yellow">AI中台安全算法</text>
    </lark-td>
    <lark-td>
      API 架构 {align="center"}
    </lark-td>
    <lark-td>
      是 {align="center"}
    </lark-td>
    <lark-td>
      HTTP {align="center"}
    </lark-td>
    <lark-td>
      否 {align="center"}
    </lark-td>
    <lark-td>
      / {align="center"}
    </lark-td>
    <lark-td>
      已接入
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      11 {align="center"}
    </lark-td>
    <lark-td>
      <text bgcolor="yellow">统一身份认证中心</text>
    </lark-td>
    <lark-td>
      B/S {align="center"}
    </lark-td>
    <lark-td>
      是 {align="center"}
    </lark-td>
    <lark-td>
      HTTP {align="center"}
    </lark-td>
    <lark-td>
      否 {align="center"}
    </lark-td>
    <lark-td>
      / {align="center"}
    </lark-td>
    <lark-td>
      已接入
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      12 {align="center"}
    </lark-td>
    <lark-td>
      <text bgcolor="yellow">安检信息管理系统</text>
    </lark-td>
    <lark-td>
      B/S {align="center"}
    </lark-td>
    <lark-td>
      否 {align="center"}
    </lark-td>
    <lark-td>
      / {align="center"}
    </lark-td>
    <lark-td>
      是 {align="center"}
    </lark-td>
    <lark-td>
      RocketMQ {align="center"}
    </lark-td>
    <lark-td>
      进行中
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      13 {align="center"}
    </lark-td>
    <lark-td>
      <text bgcolor="yellow">地服运行管理应用</text>
    </lark-td>
    <lark-td>
      B/S {align="center"}
    </lark-td>
    <lark-td>
      否 {align="center"}
    </lark-td>
    <lark-td>
      / {align="center"}
    </lark-td>
    <lark-td>
      是 {align="center"}
    </lark-td>
    <lark-td>
      RocketMQ {align="center"}
    </lark-td>
    <lark-td>
      进行中
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      14 {align="center"}
    </lark-td>
    <lark-td>
      <text bgcolor="yellow">行李全流程跟踪系统</text>
    </lark-td>
    <lark-td>
      B/S {align="center"}
    </lark-td>
    <lark-td>
      否 {align="center"}
    </lark-td>
    <lark-td>
      / {align="center"}
    </lark-td>
    <lark-td>
      是 {align="center"}
    </lark-td>
    <lark-td>
      RocketMQ {align="center"}
    </lark-td>
    <lark-td>
      进行中
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      15 {align="center"}
    </lark-td>
    <lark-td>
      <text bgcolor="yellow">行李处理系统</text>
    </lark-td>
    <lark-td>
      B/S {align="center"}
    </lark-td>
    <lark-td>
      否 {align="center"}
    </lark-td>
    <lark-td>
      / {align="center"}
    </lark-td>
    <lark-td>
      是 {align="center"}
    </lark-td>
    <lark-td>
      RocketMQ {align="center"}
    </lark-td>
    <lark-td>
      进行中
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      16 {align="center"}
    </lark-td>
    <lark-td>
      道口综合管理系统
    </lark-td>
    <lark-td>
      B/S {align="center"}
    </lark-td>
    <lark-td>
      否 {align="center"}
    </lark-td>
    <lark-td>
      / {align="center"}
    </lark-td>
    <lark-td>
      是 {align="center"}
    </lark-td>
    <lark-td>
      RocketMQ {align="center"}
    </lark-td>
    <lark-td>
      进行中
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      17 {align="center"}
    </lark-td>
    <lark-td>
      跑道异物检测系统
    </lark-td>
    <lark-td>
      B/S {align="center"}
    </lark-td>
    <lark-td>
      是 {align="center"}
    </lark-td>
    <lark-td>
      HTTP {align="center"}
    </lark-td>
    <lark-td>
      是 {align="center"}
    </lark-td>
    <lark-td>
      RocketMQ {align="center"}
    </lark-td>
    <lark-td>
      进行中
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      18 {align="center"}
    </lark-td>
    <lark-td>
      大场景拼接及跑道防入侵系统
    </lark-td>
    <lark-td>
      B/S {align="center"}
    </lark-td>
    <lark-td>
      是 {align="center"}
    </lark-td>
    <lark-td>
      HTTP {align="center"}
    </lark-td>
    <lark-td>
      是 {align="center"}
    </lark-td>
    <lark-td>
      RocketMQ {align="center"}
    </lark-td>
    <lark-td>
      进行中
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      19 {align="center"}
    </lark-td>
    <lark-td>
      <text bgcolor="yellow">机场协同决策系统</text>
    </lark-td>
    <lark-td>
      B/S {align="center"}
    </lark-td>
    <lark-td>
      否 {align="center"}
    </lark-td>
    <lark-td>
      / {align="center"}
    </lark-td>
    <lark-td>
      是 {align="center"}
    </lark-td>
    <lark-td>
      RocketMQ {align="center"}
    </lark-td>
    <lark-td>
      待接入
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      20 {align="center"}
    </lark-td>
    <lark-td>
      <text bgcolor="yellow">航空安保一体化平台</text>
    </lark-td>
    <lark-td>
      B/S {align="center"}
    </lark-td>
    <lark-td>
      是 {align="center"}
    </lark-td>
    <lark-td>
      HTTP {align="center"}
    </lark-td>
    <lark-td>
      是 {align="center"}
    </lark-td>
    <lark-td>
      RocketMQ {align="center"}
    </lark-td>
    <lark-td>
      待接入
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      21 {align="center"}
    </lark-td>
    <lark-td>
      <text bgcolor="yellow">T3门禁系统</text>
    </lark-td>
    <lark-td>
      B/S {align="center"}
    </lark-td>
    <lark-td>
      是 {align="center"}
    </lark-td>
    <lark-td>
      HTTP {align="center"}
    </lark-td>
    <lark-td>
      是 {align="center"}
    </lark-td>
    <lark-td>
      RocketMQ {align="center"}
    </lark-td>
    <lark-td>
      待接入
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      22 {align="center"}
    </lark-td>
    <lark-td>
      安检分层系统
    </lark-td>
    <lark-td>
      B/S {align="center"}
    </lark-td>
    <lark-td>
      否 {align="center"}
    </lark-td>
    <lark-td>
      / {align="center"}
    </lark-td>
    <lark-td>
      是 {align="center"}
    </lark-td>
    <lark-td>
      RocketMQ {align="center"}
    </lark-td>
    <lark-td>
      待接入
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      23 {align="center"}
    </lark-td>
    <lark-td>
      综合交通运行管理系统
    </lark-td>
    <lark-td>
      B/S {align="center"}
    </lark-td>
    <lark-td>
      否 {align="center"}
    </lark-td>
    <lark-td>
      / {align="center"}
    </lark-td>
    <lark-td>
      是 {align="center"}
    </lark-td>
    <lark-td>
      RocketMQ {align="center"}
    </lark-td>
    <lark-td>
      待接入
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      24 {align="center"}
    </lark-td>
    <lark-td>
      T3交通中心停车场管理系统
    </lark-td>
    <lark-td>
      B/S {align="center"}
    </lark-td>
    <lark-td>
      是 {align="center"}
    </lark-td>
    <lark-td>
      HTTP {align="center"}
    </lark-td>
    <lark-td>
      否 {align="center"}
    </lark-td>
    <lark-td>
      / {align="center"}
    </lark-td>
    <lark-td>
      待接入
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      25 {align="center"}
    </lark-td>
    <lark-td>
      动环系统
    </lark-td>
    <lark-td>
      B/S {align="center"}
    </lark-td>
    <lark-td>
      是 {align="center"}
    </lark-td>
    <lark-td>
      HTTP {align="center"}
    </lark-td>
    <lark-td>
      否 {align="center"}
    </lark-td>
    <lark-td>
      / {align="center"}
    </lark-td>
    <lark-td>
      待接入
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      26 {align="center"}
    </lark-td>
    <lark-td>
      <text bgcolor="yellow">大运控航班保障信息应用</text>
    </lark-td>
    <lark-td>
      B/S {align="center"}
    </lark-td>
    <lark-td>
      否 {align="center"}
    </lark-td>
    <lark-td>
      / {align="center"}
    </lark-td>
    <lark-td>
      是 {align="center"}
    </lark-td>
    <lark-td>
      RocketMQ {align="center"}
    </lark-td>
    <lark-td>
      待接入
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      27 {align="center"}
    </lark-td>
    <lark-td>
      视频监控系统
    </lark-td>
    <lark-td>
      B/S {align="center"}
    </lark-td>
    <lark-td>
      是 {align="center"}
    </lark-td>
    <lark-td>
      HTTP {align="center"}
    </lark-td>
    <lark-td>
      否 {align="center"}
    </lark-td>
    <lark-td>
      / {align="center"}
    </lark-td>
    <lark-td>
      待接入
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      28 {align="center"}
    </lark-td>
    <lark-td>
      <text bgcolor="yellow">货运服务总线</text>
    </lark-td>
    <lark-td>
      B/S {align="center"}
    </lark-td>
    <lark-td>
      是 {align="center"}
    </lark-td>
    <lark-td>
      HTTP {align="center"}
    </lark-td>
    <lark-td>
      是 {align="center"}
    </lark-td>
    <lark-td>
      TongHTP {align="center"}
    </lark-td>
    <lark-td>
      待接入
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      29 {align="center"}
    </lark-td>
    <lark-td>
      飞行区下穿通道综合管理平台
    </lark-td>
    <lark-td>
      B/S {align="center"}
    </lark-td>
    <lark-td>
      是 {align="center"}
    </lark-td>
    <lark-td>
      HTTP {align="center"}
    </lark-td>
    <lark-td>
      否 {align="center"}
    </lark-td>
    <lark-td>
      / {align="center"}
    </lark-td>
    <lark-td>
      待接入
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      30 {align="center"}
    </lark-td>
    <lark-td>
      驱鸟及低慢管控系统
    </lark-td>
    <lark-td>
      B/S {align="center"}
    </lark-td>
    <lark-td>
      否 {align="center"}
    </lark-td>
    <lark-td>
      / {align="center"}
    </lark-td>
    <lark-td>
      是 {align="center"}
    </lark-td>
    <lark-td>
      RocketMQ {align="center"}
    </lark-td>
    <lark-td>
      待接入
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      31 {align="center"}
    </lark-td>
    <lark-td>
      T1T2门禁
    </lark-td>
    <lark-td>
      B/S {align="center"}
    </lark-td>
    <lark-td>
      否 {align="center"}
    </lark-td>
    <lark-td>
      / {align="center"}
    </lark-td>
    <lark-td>
      是 {align="center"}
    </lark-td>
    <lark-td>
      RocketMQ {align="center"}
    </lark-td>
    <lark-td>
      待接入
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      32 {align="center"}
    </lark-td>
    <lark-td>
      <text bgcolor="yellow">T3泊位引导系统</text>
    </lark-td>
    <lark-td>
      B/S {align="center"}
    </lark-td>
    <lark-td>
      否 {align="center"}
    </lark-td>
    <lark-td>
      / {align="center"}
    </lark-td>
    <lark-td>
      是 {align="center"}
    </lark-td>
    <lark-td>
      RocketMQ {align="center"}
    </lark-td>
    <lark-td>
      待接入
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      33 {align="center"}
    </lark-td>
    <lark-td>
      T3智能调度
    </lark-td>
    <lark-td>
      B/S {align="center"}
    </lark-td>
    <lark-td>
      是 {align="center"}
    </lark-td>
    <lark-td>
      HTTP {align="center"}
    </lark-td>
    <lark-td>
      是 {align="center"}
    </lark-td>
    <lark-td>
      RabbitMQ {align="center"}
    </lark-td>
    <lark-td>
      待接入
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      34 {align="center"}
    </lark-td>
    <lark-td>
      <text bgcolor="yellow">应急管理系统</text>
    </lark-td>
    <lark-td>
      B/S {align="center"}
    </lark-td>
    <lark-td>
    </lark-td>
    <lark-td>
    </lark-td>
    <lark-td>
    </lark-td>
    <lark-td>
    </lark-td>
    <lark-td>
      待接入
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      35 {align="center"}
    </lark-td>
    <lark-td>
      <text bgcolor="yellow">围界入侵报警系统</text>
    </lark-td>
    <lark-td>
      B/S {align="center"}
    </lark-td>
    <lark-td>
    </lark-td>
    <lark-td>
    </lark-td>
    <lark-td>
    </lark-td>
    <lark-td>
    </lark-td>
    <lark-td>
      待接入
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      36 {align="center"}
    </lark-td>
    <lark-td>
      数字孪生系统
    </lark-td>
    <lark-td>
      B/S {align="center"}
    </lark-td>
    <lark-td>
    </lark-td>
    <lark-td>
    </lark-td>
    <lark-td>
    </lark-td>
    <lark-td>
    </lark-td>
    <lark-td>
      待接入
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      37 {align="center"}
    </lark-td>
    <lark-td>
      地勤航班生产运用系统
    </lark-td>
    <lark-td>
      B/S {align="center"}
    </lark-td>
    <lark-td>
      否 {align="center"}
    </lark-td>
    <lark-td>
      / {align="center"}
    </lark-td>
    <lark-td>
      是 {align="center"}
    </lark-td>
    <lark-td>
    </lark-td>
    <lark-td>
      待接入
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      38 {align="center"}
    </lark-td>
    <lark-td>
      <text bgcolor="yellow">证件管理系统</text>
    </lark-td>
    <lark-td>
      B/S {align="center"}
    </lark-td>
    <lark-td>
      是 {align="center"}
    </lark-td>
    <lark-td>
      HTTP {align="center"}
    </lark-td>
    <lark-td>
      否 {align="center"}
    </lark-td>
    <lark-td>
      / {align="center"}
    </lark-td>
    <lark-td>
      待接入
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      39 {align="center"}
    </lark-td>
    <lark-td>
      车辆注册数据服务
    </lark-td>
    <lark-td>
      B/S {align="center"}
    </lark-td>
    <lark-td>
      是 {align="center"}
    </lark-td>
    <lark-td>
      HTTP {align="center"}
    </lark-td>
    <lark-td>
      否 {align="center"}
    </lark-td>
    <lark-td>
      / {align="center"}
    </lark-td>
    <lark-td>
      待接入
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      40 {align="center"}
    </lark-td>
    <lark-td>
      T2安保监控整体管理平台
    </lark-td>
    <lark-td>
      B/S {align="center"}
    </lark-td>
    <lark-td>
    </lark-td>
    <lark-td>
    </lark-td>
    <lark-td>
    </lark-td>
    <lark-td>
    </lark-td>
    <lark-td>
      待接入
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      41 {align="center"}
    </lark-td>
    <lark-td>
      T3PISS系统
    </lark-td>
    <lark-td>
      B/S {align="center"}
    </lark-td>
    <lark-td>
    </lark-td>
    <lark-td>
    </lark-td>
    <lark-td>
    </lark-td>
    <lark-td>
    </lark-td>
    <lark-td>
      待接入
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      42 {align="center"}
    </lark-td>
    <lark-td>
      第一航站区智慧能源管理系统
    </lark-td>
    <lark-td>
      B/S {align="center"}
    </lark-td>
    <lark-td>
    </lark-td>
    <lark-td>
    </lark-td>
    <lark-td>
    </lark-td>
    <lark-td>
    </lark-td>
    <lark-td>
      待接入
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      43 {align="center"}
    </lark-td>
    <lark-td>
      集团SMS安全管理系统
    </lark-td>
    <lark-td>
      B/S {align="center"}
    </lark-td>
    <lark-td>
    </lark-td>
    <lark-td>
    </lark-td>
    <lark-td>
    </lark-td>
    <lark-td>
    </lark-td>
    <lark-td>
      待接入
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      44 {align="center"}
    </lark-td>
    <lark-td>
      回音壁系统
    </lark-td>
    <lark-td>
      B/S {align="center"}
    </lark-td>
    <lark-td>
    </lark-td>
    <lark-td>
    </lark-td>
    <lark-td>
    </lark-td>
    <lark-td>
    </lark-td>
    <lark-td>
      待接入
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      45 {align="center"}
    </lark-td>
    <lark-td>
      空港设备好运平台
    </lark-td>
    <lark-td>
      B/S {align="center"}
    </lark-td>
    <lark-td>
    </lark-td>
    <lark-td>
    </lark-td>
    <lark-td>
    </lark-td>
    <lark-td>
    </lark-td>
    <lark-td>
      待接入
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      46 {align="center"}
    </lark-td>
    <lark-td>
      广告媒体综合管理系统
    </lark-td>
    <lark-td>
      B/S {align="center"}
    </lark-td>
    <lark-td>
    </lark-td>
    <lark-td>
    </lark-td>
    <lark-td>
    </lark-td>
    <lark-td>
    </lark-td>
    <lark-td>
      待接入
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      47 {align="center"}
    </lark-td>
    <lark-td>
      商业管理系统
    </lark-td>
    <lark-td>
      B/S {align="center"}
    </lark-td>
    <lark-td>
    </lark-td>
    <lark-td>
    </lark-td>
    <lark-td>
    </lark-td>
    <lark-td>
    </lark-td>
    <lark-td>
      待接入
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      48 {align="center"}
    </lark-td>
    <lark-td>
      业财系统
    </lark-td>
    <lark-td>
      B/S {align="center"}
    </lark-td>
    <lark-td>
    </lark-td>
    <lark-td>
    </lark-td>
    <lark-td>
    </lark-td>
    <lark-td>
    </lark-td>
    <lark-td>
      待接入
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      49 {align="center"}
    </lark-td>
    <lark-td>
      限制性物品管理系统
    </lark-td>
    <lark-td>
      B/S {align="center"}
    </lark-td>
    <lark-td>
    </lark-td>
    <lark-td>
    </lark-td>
    <lark-td>
    </lark-td>
    <lark-td>
    </lark-td>
    <lark-td>
      待接入
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      50 {align="center"}
    </lark-td>
    <lark-td>
      净空管理系统
    </lark-td>
    <lark-td>
      B/S {align="center"}
    </lark-td>
    <lark-td>
    </lark-td>
    <lark-td>
    </lark-td>
    <lark-td>
    </lark-td>
    <lark-td>
    </lark-td>
    <lark-td>
      待接入
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      51 {align="center"}
    </lark-td>
    <lark-td>
      气象信息
    </lark-td>
    <lark-td>
      B/S {align="center"}
    </lark-td>
    <lark-td>
    </lark-td>
    <lark-td>
    </lark-td>
    <lark-td>
    </lark-td>
    <lark-td>
    </lark-td>
    <lark-td>
      待接入
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      52 {align="center"}
    </lark-td>
    <lark-td>
      T3电瓶车管理系统
    </lark-td>
    <lark-td>
      B/S {align="center"}
    </lark-td>
    <lark-td>
    </lark-td>
    <lark-td>
    </lark-td>
    <lark-td>
    </lark-td>
    <lark-td>
    </lark-td>
    <lark-td>
      待接入
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      53 {align="center"}
    </lark-td>
    <lark-td>
      ADSB系统
    </lark-td>
    <lark-td>
      B/S {align="center"}
    </lark-td>
    <lark-td>
    </lark-td>
    <lark-td>
    </lark-td>
    <lark-td>
    </lark-td>
    <lark-td>
    </lark-td>
    <lark-td>
      待接入
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      54 {align="center"}
    </lark-td>
    <lark-td>
      场监系统
    </lark-td>
    <lark-td>
      B/S {align="center"}
    </lark-td>
    <lark-td>
    </lark-td>
    <lark-td>
    </lark-td>
    <lark-td>
    </lark-td>
    <lark-td>
    </lark-td>
    <lark-td>
      待接入
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      55 {align="center"}
    </lark-td>
    <lark-td>
      车辆管理系统
    </lark-td>
    <lark-td>
      B/S {align="center"}
    </lark-td>
    <lark-td>
    </lark-td>
    <lark-td>
    </lark-td>
    <lark-td>
    </lark-td>
    <lark-td>
    </lark-td>
    <lark-td>
      待接入
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      56 {align="center"}
    </lark-td>
    <lark-td>
      电子进程单系统
    </lark-td>
    <lark-td>
      B/S {align="center"}
    </lark-td>
    <lark-td>
    </lark-td>
    <lark-td>
    </lark-td>
    <lark-td>
    </lark-td>
    <lark-td>
    </lark-td>
    <lark-td>
      待接入
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      57 {align="center"}
    </lark-td>
    <lark-td>
      AMDB系统
    </lark-td>
    <lark-td>
      B/S {align="center"}
    </lark-td>
    <lark-td>
    </lark-td>
    <lark-td>
    </lark-td>
    <lark-td>
    </lark-td>
    <lark-td>
    </lark-td>
    <lark-td>
      待接入
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      58 {align="center"}
    </lark-td>
    <lark-td>
      廊桥控制系统
    </lark-td>
    <lark-td>
      B/S {align="center"}
    </lark-td>
    <lark-td>
    </lark-td>
    <lark-td>
    </lark-td>
    <lark-td>
    </lark-td>
    <lark-td>
    </lark-td>
    <lark-td>
      待接入
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      59 {align="center"}
    </lark-td>
    <lark-td>
      空港设备云桥系统
    </lark-td>
    <lark-td>
      B/S {align="center"}
    </lark-td>
    <lark-td>
    </lark-td>
    <lark-td>
    </lark-td>
    <lark-td>
    </lark-td>
    <lark-td>
    </lark-td>
    <lark-td>
      待接入
    </lark-td>
  </lark-tr>
</lark-table>

#### 测试时间及地点
对接测试时间：2025-03-17~2025-05-15
联调时间：2025-04-23~2025-06-15
测试地点：广州白云机场AOC大楼
# 参与人员及职责
（本系统）

<lark-table rows="2" cols="5" column-widths="59,139,311,106,141">

  <lark-tr>
    <lark-td>
      **序号** {align="center"}
    </lark-td>
    <lark-td>
      **系统** {align="center"}
    </lark-td>
    <lark-td>
      **职责及功能描述** {align="center"}
    </lark-td>
    <lark-td>
      **测试人员** {align="center"}
    </lark-td>
    <lark-td>
      **联系电话** {align="center"}
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      1 {align="center"}
    </lark-td>
    <lark-td>
      AESB总线 {align="center"}
    </lark-td>
    <lark-td>
      与业务系统对接并联调测试 {align="center"}
    </lark-td>
    <lark-td>
      杨神刚 {align="center"}
    </lark-td>
    <lark-td>
      15274834504 {align="center"}
    </lark-td>
  </lark-tr>
</lark-table>



（第三方业务系统）

<lark-table rows="60" cols="5" column-widths="61,240,222,115,146">

  <lark-tr>
    <lark-td>
      **序号** {align="center"}
    </lark-td>
    <lark-td>
      **系统名称** {align="center"}
    </lark-td>
    <lark-td>
      **职责及功能描述** {align="center"}
    </lark-td>
    <lark-td>
      **测试人员** {align="center"}
    </lark-td>
    <lark-td>
      **联系电话** {align="center"}
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      1
    </lark-td>
    <lark-td>
      机场地理信息系统
    </lark-td>
    <lark-td>
      与总线对接并联调测试
    </lark-td>
    <lark-td>
      田志民
    </lark-td>
    <lark-td>
      18753635202
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      2
    </lark-td>
    <lark-td>
      高精度综合定位系统
    </lark-td>
    <lark-td>
      与总线对接并联调测试
    </lark-td>
    <lark-td>
      陈子杰
    </lark-td>
    <lark-td>
      13809059768
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      3
    </lark-td>
    <lark-td>
      物联网平台
    </lark-td>
    <lark-td>
      与总线对接并联调测试
    </lark-td>
    <lark-td>
      唐欣然
    </lark-td>
    <lark-td>
      18617200035
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      4
    </lark-td>
    <lark-td>
      旅客服务平台
    </lark-td>
    <lark-td>
      与总线对接并联调测试
    </lark-td>
    <lark-td>
      俞泰盛
    </lark-td>
    <lark-td>
      13724011923
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      5
    </lark-td>
    <lark-td>
      电子告知书系统
    </lark-td>
    <lark-td>
      与总线对接并联调测试
    </lark-td>
    <lark-td>
      俞泰盛
    </lark-td>
    <lark-td>
      13724011923
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      6
    </lark-td>
    <lark-td>
      全场设备及能源管理系统
    </lark-td>
    <lark-td>
      与总线对接并联调测试
    </lark-td>
    <lark-td>
      李奕盛
    </lark-td>
    <lark-td>
      18675617663
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      7
    </lark-td>
    <lark-td>
      机场运行信息集成系统
    </lark-td>
    <lark-td>
      与总线对接并联调测试
    </lark-td>
    <lark-td>
      郑迪文
    </lark-td>
    <lark-td>
      18628074819
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      8
    </lark-td>
    <lark-td>
      广播系统-基础广播
    </lark-td>
    <lark-td>
      与总线对接并联调测试
    </lark-td>
    <lark-td>
      黄明闯
    </lark-td>
    <lark-td>
      13824474415
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      9
    </lark-td>
    <lark-td>
      航班信息显示系统
    </lark-td>
    <lark-td>
      与总线对接并联调测试
    </lark-td>
    <lark-td>
      叶景
    </lark-td>
    <lark-td>
      13751878553
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      10
    </lark-td>
    <lark-td>
      AI中台安全算法
    </lark-td>
    <lark-td>
      与总线对接并联调测试
    </lark-td>
    <lark-td>
      孔令栋
    </lark-td>
    <lark-td>
      15822601343
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      11
    </lark-td>
    <lark-td>
      统一身份认证中心
    </lark-td>
    <lark-td>
      与总线对接并联调测试
    </lark-td>
    <lark-td>
      沈剑棠
    </lark-td>
    <lark-td>
      13168347709
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      12
    </lark-td>
    <lark-td>
      安检信息管理系统
    </lark-td>
    <lark-td>
      与总线对接并联调测试
    </lark-td>
    <lark-td>
      胡安锦
    </lark-td>
    <lark-td>
      18030199556
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      13
    </lark-td>
    <lark-td>
      地服运行管理应用
    </lark-td>
    <lark-td>
      与总线对接并联调测试
    </lark-td>
    <lark-td>
      张晓辉
    </lark-td>
    <lark-td>
      18613058800
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      14
    </lark-td>
    <lark-td>
      行李全流程跟踪系统
    </lark-td>
    <lark-td>
      与总线对接并联调测试
    </lark-td>
    <lark-td>
      黄泽鹏
    </lark-td>
    <lark-td>
      13828431914
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      15
    </lark-td>
    <lark-td>
      行李处理系统
    </lark-td>
    <lark-td>
      与总线对接并联调测试
    </lark-td>
    <lark-td>
      冯建新
    </lark-td>
    <lark-td>
      18017589900
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      16
    </lark-td>
    <lark-td>
      道口综合管理系统
    </lark-td>
    <lark-td>
      与总线对接并联调测试
    </lark-td>
    <lark-td>
      孙瀚
    </lark-td>
    <lark-td>
      17706918889
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      17
    </lark-td>
    <lark-td>
      跑道异物检测系统
    </lark-td>
    <lark-td>
      与总线对接并联调测试
    </lark-td>
    <lark-td>
      邓平
    </lark-td>
    <lark-td>
      15528024966
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      18
    </lark-td>
    <lark-td>
      大场景拼接及跑道防入侵系统
    </lark-td>
    <lark-td>
      与总线对接并联调测试
    </lark-td>
    <lark-td>
      刘彦峰
    </lark-td>
    <lark-td>
      18522078357
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      19
    </lark-td>
    <lark-td>
      机场协同决策系统
    </lark-td>
    <lark-td>
      与总线对接并联调测试
    </lark-td>
    <lark-td>
      郑迪文
    </lark-td>
    <lark-td>
      18628074819
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      20
    </lark-td>
    <lark-td>
      航空安保一体化平台
    </lark-td>
    <lark-td>
      与总线对接并联调测试
    </lark-td>
    <lark-td>
      陈家法
    </lark-td>
    <lark-td>
      18675512823
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      21
    </lark-td>
    <lark-td>
      T3门禁系统
    </lark-td>
    <lark-td>
      与总线对接并联调测试
    </lark-td>
    <lark-td>
      陈家法
    </lark-td>
    <lark-td>
      18675512823
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      22
    </lark-td>
    <lark-td>
      安检分层系统
    </lark-td>
    <lark-td>
      与总线对接并联调测试
    </lark-td>
    <lark-td>
      康春飞
    </lark-td>
    <lark-td>
      18910264852
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      23
    </lark-td>
    <lark-td>
      综合交通运行管理系统
    </lark-td>
    <lark-td>
      与总线对接并联调测试
    </lark-td>
    <lark-td>
      杨海胜
    </lark-td>
    <lark-td>
      1801135794
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      24
    </lark-td>
    <lark-td>
      T3交通中心停车场管理系统
    </lark-td>
    <lark-td>
      与总线对接并联调测试
    </lark-td>
    <lark-td>
      杨海彬
    </lark-td>
    <lark-td>
      13760614155
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      25
    </lark-td>
    <lark-td>
      动环系统
    </lark-td>
    <lark-td>
      与总线对接并联调测试
    </lark-td>
    <lark-td>
      黄善政
    </lark-td>
    <lark-td>
      15766068388
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      26
    </lark-td>
    <lark-td>
      大运控航班保障信息应用
    </lark-td>
    <lark-td>
      与总线对接并联调测试
    </lark-td>
    <lark-td>
      冯兴悦
    </lark-td>
    <lark-td>
      13632102508
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      27
    </lark-td>
    <lark-td>
      视频监控系统
    </lark-td>
    <lark-td>
      与总线对接并联调测试
    </lark-td>
    <lark-td>
      张涛
    </lark-td>
    <lark-td>
      18100195534
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      28
    </lark-td>
    <lark-td>
      货运服务总线
    </lark-td>
    <lark-td>
      与总线对接并联调测试
    </lark-td>
    <lark-td>
      柴景艳
    </lark-td>
    <lark-td>
      13718491731
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      29
    </lark-td>
    <lark-td>
      飞行区下穿通道综合管理平台
    </lark-td>
    <lark-td>
      与总线对接并联调测试
    </lark-td>
    <lark-td>
      孙鑫
    </lark-td>
    <lark-td>
      17610961132
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      30
    </lark-td>
    <lark-td>
      驱鸟及低慢管控系统
    </lark-td>
    <lark-td>
      与总线对接并联调测试
    </lark-td>
    <lark-td>
      雷锐
    </lark-td>
    <lark-td>
      13810962859
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      31
    </lark-td>
    <lark-td>
      T1T2门禁
    </lark-td>
    <lark-td>
      与总线对接并联调测试
    </lark-td>
    <lark-td>
      胡勇
    </lark-td>
    <lark-td>
      13488898930
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      32
    </lark-td>
    <lark-td>
      应急管理系统
    </lark-td>
    <lark-td>
      与总线对接并联调测试
    </lark-td>
    <lark-td>
      冯兴悦
    </lark-td>
    <lark-td>
      13632102508
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      33
    </lark-td>
    <lark-td>
      围界入侵报警系统
    </lark-td>
    <lark-td>
      与总线对接并联调测试
    </lark-td>
    <lark-td>
      陈家法
    </lark-td>
    <lark-td>
      18675512823
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      34
    </lark-td>
    <lark-td>
      数字孪生系统
    </lark-td>
    <lark-td>
      与总线对接并联调测试
    </lark-td>
    <lark-td>
      常远达
    </lark-td>
    <lark-td>
      13321100113
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      35
    </lark-td>
    <lark-td>
      地勤航班生产运用系统
    </lark-td>
    <lark-td>
      与总线对接并联调测试
    </lark-td>
    <lark-td>
      杜天宝
    </lark-td>
    <lark-td>
      13416261332
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      36
    </lark-td>
    <lark-td>
      证件管理系统
    </lark-td>
    <lark-td>
      与总线对接并联调测试
    </lark-td>
    <lark-td>
      韩明文
    </lark-td>
    <lark-td>
      15071176503
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      37
    </lark-td>
    <lark-td>
      车辆注册数据服务
    </lark-td>
    <lark-td>
      与总线对接并联调测试
    </lark-td>
    <lark-td>
      韩明文
    </lark-td>
    <lark-td>
      15071176503
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      38
    </lark-td>
    <lark-td>
      T2安保监控整体管理平台
    </lark-td>
    <lark-td>
      与总线对接并联调测试
    </lark-td>
    <lark-td>
      陈家法
    </lark-td>
    <lark-td>
      18675512823
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      39
    </lark-td>
    <lark-td>
      T3智能调度
    </lark-td>
    <lark-td>
      与总线对接并联调测试
    </lark-td>
    <lark-td>
      伦家俊
    </lark-td>
    <lark-td>
      18565440729
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      40
    </lark-td>
    <lark-td>
      T3PISS系统
    </lark-td>
    <lark-td>
      与总线对接并联调测试
    </lark-td>
    <lark-td>
      李舰
    </lark-td>
    <lark-td>
      13828441680
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      41
    </lark-td>
    <lark-td>
      第一航站区智慧能源管理系统
    </lark-td>
    <lark-td>
      与总线对接并联调测试
    </lark-td>
    <lark-td>
      伦家俊
    </lark-td>
    <lark-td>
      18565440729
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      42
    </lark-td>
    <lark-td>
      集团SMS安全管理系统
    </lark-td>
    <lark-td>
      与总线对接并联调测试
    </lark-td>
    <lark-td>
      黄灏成
    </lark-td>
    <lark-td>
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      43
    </lark-td>
    <lark-td>
      回音壁系统
    </lark-td>
    <lark-td>
      与总线对接并联调测试
    </lark-td>
    <lark-td>
      马忠星
    </lark-td>
    <lark-td>
      18520605027
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      44
    </lark-td>
    <lark-td>
      空港设备好运平台
    </lark-td>
    <lark-td>
      与总线对接并联调测试
    </lark-td>
    <lark-td>
      沈凡书
    </lark-td>
    <lark-td>
      16676784547
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      45
    </lark-td>
    <lark-td>
      广告媒体综合管理系统
    </lark-td>
    <lark-td>
      与总线对接并联调测试
    </lark-td>
    <lark-td>
      周逸耿
    </lark-td>
    <lark-td>
      13828435457
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      46
    </lark-td>
    <lark-td>
      商业管理系统
    </lark-td>
    <lark-td>
      与总线对接并联调测试
    </lark-td>
    <lark-td>
      徐鹏
    </lark-td>
    <lark-td>
      13560150996
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      47
    </lark-td>
    <lark-td>
      业财系统
    </lark-td>
    <lark-td>
      与总线对接并联调测试
    </lark-td>
    <lark-td>
    </lark-td>
    <lark-td>
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      48
    </lark-td>
    <lark-td>
      限制性物品管理系统
    </lark-td>
    <lark-td>
      与总线对接并联调测试
    </lark-td>
    <lark-td>
    </lark-td>
    <lark-td>
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      49
    </lark-td>
    <lark-td>
      净空管理系统
    </lark-td>
    <lark-td>
      与总线对接并联调测试
    </lark-td>
    <lark-td>
    </lark-td>
    <lark-td>
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      50
    </lark-td>
    <lark-td>
      气象信息
    </lark-td>
    <lark-td>
      与总线对接并联调测试
    </lark-td>
    <lark-td>
    </lark-td>
    <lark-td>
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      51
    </lark-td>
    <lark-td>
      T3电瓶车管理系统
    </lark-td>
    <lark-td>
      与总线对接并联调测试
    </lark-td>
    <lark-td>
    </lark-td>
    <lark-td>
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      52
    </lark-td>
    <lark-td>
      ADSB系统
    </lark-td>
    <lark-td>
      与总线对接并联调测试
    </lark-td>
    <lark-td>
    </lark-td>
    <lark-td>
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      53
    </lark-td>
    <lark-td>
      场监系统
    </lark-td>
    <lark-td>
      与总线对接并联调测试
    </lark-td>
    <lark-td>
    </lark-td>
    <lark-td>
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      54
    </lark-td>
    <lark-td>
      车辆管理系统
    </lark-td>
    <lark-td>
      与总线对接并联调测试
    </lark-td>
    <lark-td>
    </lark-td>
    <lark-td>
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      55
    </lark-td>
    <lark-td>
      电子进程单系统
    </lark-td>
    <lark-td>
      与总线对接并联调测试
    </lark-td>
    <lark-td>
    </lark-td>
    <lark-td>
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      56
    </lark-td>
    <lark-td>
      AMDB系统
    </lark-td>
    <lark-td>
      与总线对接并联调测试
    </lark-td>
    <lark-td>
    </lark-td>
    <lark-td>
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      57
    </lark-td>
    <lark-td>
      廊桥控制系统
    </lark-td>
    <lark-td>
      与总线对接并联调测试
    </lark-td>
    <lark-td>
    </lark-td>
    <lark-td>
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      58
    </lark-td>
    <lark-td>
      空港设备云桥系统
    </lark-td>
    <lark-td>
      与总线对接并联调测试
    </lark-td>
    <lark-td>
    </lark-td>
    <lark-td>
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      59
    </lark-td>
    <lark-td>
      T3泊位引导系统
    </lark-td>
    <lark-td>
      与总线对接并联调测试
    </lark-td>
    <lark-td>
      郑煜畅
    </lark-td>
    <lark-td>
      15902027149
    </lark-td>
  </lark-tr>
</lark-table>


# 测试环境
## 总体说明
本次测试基于与本次测试环境（至少包括：系统部署、接口开发、服务器环境、网络环境等）均完成、正常或具备的条件下进行，如有未完成、不正常、不具备的条件应做好记录，后续完善后重新补充测试并出具测试报告。
## 测试环境条件清单

<lark-table rows="2" cols="8" column-widths="41,110,113,108,127,104,75,76">

  <lark-tr>
    <lark-td>
      序号 {align="center"}
    </lark-td>
    <lark-td>
      系统 {align="center"}
    </lark-td>
    <lark-td>
      系统部署 {align="center"}
    </lark-td>
    <lark-td>
      接口开发 {align="center"}
    </lark-td>
    <lark-td>
      服务器环境 {align="center"}
    </lark-td>
    <lark-td>
      网络环境 {align="center"}
    </lark-td>
    <lark-td>
      时钟 {align="center"}
    </lark-td>
    <lark-td>
      备注 {align="center"}
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      1 {align="center"}
    </lark-td>
    <lark-td>
      AESB {align="center"}
    </lark-td>
    <lark-td>
      已完成 {align="center"}
    </lark-td>
    <lark-td>
      已完成 {align="center"}
    </lark-td>
    <lark-td>
      已完成 {align="center"}
    </lark-td>
    <lark-td>
      正常 {align="center"}
    </lark-td>
    <lark-td>
      正常 {align="center"}
    </lark-td>
    <lark-td>
    </lark-td>
  </lark-tr>
</lark-table>

# 测试场景及流程
## 测试场景
广州机场三期扩建工程信息工程以统一的云安全体系为策略，基于信息弱电基础配套设施，建设IaaS（Infrastructure as a Service基础设施即服务）、PaaS（Platform-As-A-Service，平台即服务），以AESB总线为业务系统的串接，以智能数据中心的数据提供管理服务为体现，实现了本次建设的8大主题业务系统应用：生产业务、能力中台、服务业务、交通业务、安防业务、运维业务、商业业务、集团业务。
本次测试以AESB总线平台为桥梁，实现各业务系统之间的数据互通。
### 生产业务
#### <text bgcolor="yellow">机场运行信息集成系统（二标）</text>
生产方：信息集成系统主要负责机场航班信息的管理，并提供统一的、标准的、完整的航班数据服务，提供的数据包括航班基础数据、航班计划、航班动态数据。信息集成系统通过AESB的MQ接口方式提供数据服务。
接口信息如下：

<lark-table rows="160" cols="4" column-widths="146,155,344,166">

  <lark-tr>
    <lark-td>
      系统名称
    </lark-td>
    <lark-td colspan="2">
      接口事件信息 {align="center"}
    </lark-td>
    <lark-td>
      下游系统
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td rowspan="159">
      航班信息集成系统
    </lark-td>
    <lark-td rowspan="37">
      航班动态事件
    </lark-td>
    <lark-td>
      航班动态增加事件说明（DFIE）
    </lark-td>
    <lark-td rowspan="159">
      航班信息显示系统、安检信息系统、广播系统、登机桥系统、泊位系统、地面服务管理系统、ACDM系统、综合交通管理平台、视频节点采集、旅客流向分析、物流行李系统、货站管理系统、、体验系统综合能源管理平台、应急救援、智能数据中心、机场全景监视系统、旅客运行与服务管理平台、呼叫中心、贵宾管理系统、ACDM系统-收费结算、航班保障节点识别系统
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      动态删除事件说明（DFDE）
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      航班动态信息请求事件（RQDF）
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      动态航班整表同步事件（DFDL）
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      航班衔接变更事件（AFID）
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      航班共享变更事件（SFLG）
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      航班航线变更事件（AIRL）
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      航班号变更事件（HBTT）
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      航班前站起飞事件（ONRE）
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      航班到达本站事件（ARRE）
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      航班本站起飞事件（DEPE）
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      航班到达下一站事件（NXTE）
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      航班开始值机事件（CKIE）
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      航班截止值机事件（CKOE）
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      航班开始登机事件（BORE）
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      航班过站登机事件（TBRE）
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      航班催促登机事件（LBDE）
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      航班结束登机事件（POKE）
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      航班延误事件（DLYE）
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      航班取消事件（CANE）
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      航班返航事件（RTNE）
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      航班滑回事件（BAKE）
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      航班备降事件（ALTE）
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      航班更换飞机事件（CFCE）
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      航班VIP事件（VIP）
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      航班登机门动态信息更新事件（GTLS）
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      航班行李滑槽口动态信息更新事件（CHLS）
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      航班行李提取转盘动态信息更新事件（BLLS）
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      航班值机柜台动态信息更新事件（CKLS）
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      航班机位动态信息更新事件（STLS）
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      航班计划时间事件（FPTT）
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      航班预计时间事件（FETT）
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      航班实际时间事件（FRTT）
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      航班航站楼变更事件（TRML）
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      航班任务变更事件（FLTK）
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      航班属性变更事件（FATT）
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      航班调时事件（FATE）
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td rowspan="2">
      航班班期事件
    </lark-td>
    <lark-td>
      航班班期信息请求事件（RQPF）
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      航班班期响应事件（PFDL）
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td rowspan="118">
      基础数据事件
    </lark-td>
    <lark-td>
      异常原因增加事件（ARIE）
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      异常原因变更事件（ARUE）
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      异常原因删除事件（ARDE）
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      异常原因基础请求事件（RQAR）
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      异常原因整表数据同步事件（ARDL）
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      航空公司增加事件（AWIE）
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      航空公司变更事件（AWUE）
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      航空公司删除事件（AWDE）
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      航空公司基础请求事件（RQAW）
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      航空公司整表数据同步事件（AWDL）
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      航空分公司增加事件（SAIE）
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      航空分公司变更事件（SAUE）
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      航空分公司删除事件（SADE）
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      航空分公司基础请求事件（RQSA）
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      航空分公司整表数据同步事件（SADL）
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      机型增加事件（CTIE）
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      机型变更事件（CTUE）
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      机型删除事件（CTDE）
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      机型基础请求事件（RQCT）
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      机型整表数据同步事件（CTDL）
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      飞机增加事件（CFIE）
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      飞机变更事件（CFUE）
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      飞机删除事件（CFDE）
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      飞机基础请求事件（RQCF）
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      飞机整表数据同步事件（CFDL）
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      机场增加事件（APIE）
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      机场变更事件（APUE）
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      机场删除事件（APDE）
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      机场基础请求事件（RQAP）
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      机场整表数据同步事件（APDL）
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      飞行任务增加事件（FTIE）
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      飞行任务变更事件（FTUE）
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      飞行任务删除事件（FTDE）
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      飞行任务基础请求事件（RQFT）
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      飞行任务整表数据同步事件（FTDL）
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      航班状态基础请求事件（RQFS）
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      航班状态整表数据同步事件（FSDL）
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      柜台类型增加事件（CLIE）
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      柜台类型变更事件（CLUE）
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      柜台类型删除事件（CLDE）
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      柜台类型基础请求事件(RQCL)
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      柜台类型整表数据同步事件（CLDL）
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      航站楼增加事件（TMIE）
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      航站楼变更事件（TMUE）
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      航站楼删除事件（TMDE）
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      航站楼基础请求事件（RQTM）
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      航站楼整表数据同步事件（TMDL）
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      登机门增加事件（GTIE）
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      登机门变更事件（GTUE）
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      登机门删除事件（GTDE）
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      登机门基础请求事件（RQGT）
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      登机门整表数据同步事件（GTDL）
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      行李提取转盘增加事件（BLIE）
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      行李提取转盘变更事件（BLUE）
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      行李提取转盘删除事件（BLDE）
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      行李提取转盘基础请求事件（RQBL）
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      行李提取转盘整表数据同步事件（BLDL）
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      值机岛/区域信息增加事件（CAIE）
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      值机岛/区域信息变更事件（CAUE）
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      值机岛/区域信息删除事件（CADE）
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      值机岛/区域信息基础请求事件（RQCA）
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      值机岛/区域信息整表数据同步事件（CADL）
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      值机柜台信息增加事件（CCIE）
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      值机柜台信息变更事件（CCUE）
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      值机柜台信息删除事件（CCDE）
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      值机柜台信息基础请求事件（RQCC）
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      值机柜台信息整表数据同步事件（CCDL）
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      机位信息增加事件（STIE）
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      机位信息变更事件（STUE）
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      机位信息删除事件（STDE）
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      机位信息基础请求事件（RQST）
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      机位信息整表数据同步事件（STDL）
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      指廊信息增加事件（COIE）
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      指廊信息变更事件（COUE）
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      指廊信息删除事件（CODE）
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      指廊信息基础请求事件（RQCO）
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      指廊信息整表数据同步事件（CODL）
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      登机桥信息增加事件（BGIE）
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      登机桥信息变更事件（BGUE）
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      登机桥信息删除事件（BGDE）
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      登机桥信息基础请求事件（RQBG）
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      登机桥信息整表数据同步事件（BGDL）
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      到达口信息增加事件（EOIE）
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      到达口信息变更事件（EOUE）
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      到达口信息删除事件（EODE）
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      到达口信息基础请求事件（RQEO）
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      到达口信息整表数据同步事件（EODL）
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      航班代理增加事件（AGIE）
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      航班代理变更事件（AGUE）
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      航班代理删除事件（AGDE）
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      航班代理基础请求事件（RQAG）
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      航班代理整表数据同步事件（AGDL）
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      机位不可用增加事件（BSIE）
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      机位不可用更新事件（BSUE）
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      机位不可用删除事件（BSDE）
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      机位不可用请求事件（RQBS）
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      机位不可用整表事件（BSDL）
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      登机口不可用增加事件（GTNAIE）
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      登机口不可用更新事件（GTNAUE）
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      登机口不可用删除事件（GTNADE）
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      登机口不可用请求事件（RQGTNA）
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      登机口不可用整表事件（GTNADL）
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      行李提取转盘不可用增加事件（BLNAIE）
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      行李提取转盘不可用更新事件（BLNAUE）
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      行李提取转盘不可用删除事件（BLNADE）
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      行李提取转盘不可用请求事件（RQBLNA）
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      行李提取转盘不可用整表事件（BLNADL）
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      值机柜台不可用增加事件（CCNAIE）
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      值机柜台不可用更新事件（CCNAUE）
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      值机柜台不可用删除事件（CCNADE）
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      值机柜台不可用请求事件（RQCCNA）
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      值机柜台不可用整表事件（CCNADL）
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      航班标签增加事件（BAIE）
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      跑道增加事件（RWIE）
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      跑道变更事件（RWUE）
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      跑道删除事件（RWDE）
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      跑道基础请求事件（RQRW）
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      跑道整表数据同步事件（RWDL）
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td rowspan="2">
      航班计划事件
    </lark-td>
    <lark-td>
      航班计划整表同步事件（FPDL）
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      航班计划请求消息（RQFP）
    </lark-td>
  </lark-tr>
</lark-table>

消费方：可获取T3离港系统、行李系统的数据。

<lark-table rows="11" cols="3" column-widths="126,385,200">

  <lark-tr>
    <lark-td>
      系统名称
    </lark-td>
    <lark-td>
      接口事件
    </lark-td>
    <lark-td>
      下游系统
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td rowspan="6">
      T3离港
    </lark-td>
    <lark-td>
      值机结束事件（DCSCKCI）
    </lark-td>
    <lark-td rowspan="7">
      信息集成系统
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      登机开放事件（DCSBDOP）
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      登机结束事件（DCSBDCL）
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      催促登机事件（DCSLCTM）
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      过站登机事件（DCSTSBD）
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      本站登机事件（DCSLCBD）
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      行李系统
    </lark-td>
    <lark-td>
      滑槽分配变更事件（CHLS）
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td rowspan="2">
      ACDM系统
    </lark-td>
    <lark-td>
      目标保障完成时间整表事件(ACDL）
    </lark-td>
    <lark-td>
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      目标保障完成时间事件（TODT）
    </lark-td>
    <lark-td>
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
    </lark-td>
    <lark-td>
      航班保障节点动态更新事件（TPUE）
    </lark-td>
    <lark-td>
    </lark-td>
  </lark-tr>
</lark-table>


#### <text bgcolor="yellow">大运控协同管理平台（三标）</text>
#### 协同决策系统 A-CDM（三标）
生产方：协同决策系统（A-CDM）是以数据为核心，以系统为支撑，以制度为前提的航班保，障进程管理系统。系统通过航空器和航班保障信息的收集与整合，打破航班保障过程中各业务单位之间的信息壁垒，实现航班保障进程关键时间节点的精准预测和透明管理。
协同决策系统通过AESB的MQ接口方式提供数据服务。
接口信息如下：

<lark-table rows="4" cols="3" column-widths="126,385,200">

  <lark-tr>
    <lark-td>
      系统名称
    </lark-td>
    <lark-td>
      接口事件
    </lark-td>
    <lark-td>
      下游系统
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td rowspan="3">
      ACDM
    </lark-td>
    <lark-td>
      航班保障节点动态更新事件（TPUE）
    </lark-td>
    <lark-td rowspan="3">
      信息集成系统
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      目标保障完成时间整表事件(ACDL）
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      目标保障完成时间事件（TODT）
    </lark-td>
  </lark-tr>
</lark-table>

消费方：可获取信息集成系统/大运控平台、地服系统、航空安保一体化系统的数据。

<lark-table rows="4" cols="3" column-widths="138,378,200">

  <lark-tr>
    <lark-td>
      系统名称
    </lark-td>
    <lark-td>
      接口事件
    </lark-td>
    <lark-td>
      下游系统
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td rowspan="3">
      信息集成系统
    </lark-td>
    <lark-td>
      航班动态信息变更
    </lark-td>
    <lark-td rowspan="3">
      ACDM系统
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      航班保障节点变更
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      空管航班进程事件
    </lark-td>
  </lark-tr>
</lark-table>


#### 自动广播系统（二标）
生产方：自动广播系统在总线平台使用MQ的接口形式消费航班类接口数据，不主动提供数据。
消费方：可获取XX系统的数据。

#### 航班信息显示系统（二标）
生产方：航班信息显示系统，是指候机楼内，显示始发、到达或转港飞机的班次、时间、机号、地点等信息的系统装置。
航班信息显示系统提供的数据将通过AESB总线MQ接口形式发布，所有接入系统均需要按照AESB规范进行数据的接入。

<lark-table rows="2" cols="4" column-widths="184,105,230,269">

  <lark-tr>
    <lark-td>
      系统名称 {align="center"}
    </lark-td>
    <lark-td colspan="2">
      接口事件 {align="center"}
    </lark-td>
    <lark-td>
      下游系统 {align="center"}
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      航班信息显示系统
    </lark-td>
    <lark-td>
      行李数据
    </lark-td>
    <lark-td>
      首末件行李数luggage
    </lark-td>
    <lark-td>
      地服运行系统、智能数据中心
    </lark-td>
  </lark-tr>
</lark-table>

消费方：可获取XX系统的数据。

#### <text bgcolor="yellow">应急指挥系统（三标）</text>
应急救援系统是指在机场发生紧急情况时，能够立即启动各种资源和机制，协调各方力量，进行紧急救援和处置的系统。其目的是为了在最短的时间内，采取最合适的救援措施，减少人员伤亡和财产损失，保障机场运营和航空安全。
应急救援系统提供的数据将通过AESB总线MQ接口形式发布，所有接入系统均需要按照AESB规范进行数据的接入。

<lark-table rows="17" cols="4" column-widths="140,117,375,139">

  <lark-tr>
    <lark-td>
      系统名称 {align="center"}
    </lark-td>
    <lark-td colspan="2">
      接口事件 {align="center"}
    </lark-td>
    <lark-td>
      下游系统 {align="center"}
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td rowspan="16">
      应急救援系统
    </lark-td>
    <lark-td rowspan="5">
      应急类
    </lark-td>
    <lark-td>
      应急事件信息（MQ-EMS-001）
    </lark-td>
    <lark-td rowspan="16">
      智能数据中心 {align="center"}
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      应急总指挥（MQ-EMS-002）
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      应急现场指挥成员（MQ-EMS-003）
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      应急航班信息（MQ-EMS-004）
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      应急事件参与人（MQ-EMS-005）
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td rowspan="6">
      物资类
    </lark-td>
    <lark-td>
      物资分类（MQ-EMS-006）
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      物资类型（MQ-EMS-007）
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      仓库（MQ-EMS-008）
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      物资供应商（MQ-EMS-009）
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      应急物资（MQ-EMS-010
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      物资出库记录（MQ-EMS-011）
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td rowspan="2">
      人员类
    </lark-td>
    <lark-td>
      人员队伍（MQ-EMS-012）
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      队伍成员（MQ-EMS-013）
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td rowspan="3">
      采购类 {align="center"}
    </lark-td>
    <lark-td>
      合同（MQ-EMS-014）
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      采购（MQ-EMS-015）
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      采购明细（MQ-EMS-016）
    </lark-td>
  </lark-tr>
</lark-table>

#### <text bgcolor="yellow">地服运行管理系统（三标）</text>
地服运行管理系统提供的数据将通过AESB总线MQ接口形式发布，所有接入系统均需要按照AESB规范进行数据的接入。
接口信息如下：

<lark-table rows="9" cols="4" column-widths="119,83,430,140">

  <lark-tr>
    <lark-td>
      系统名称
    </lark-td>
    <lark-td colspan="2">
      接口事件
    </lark-td>
    <lark-td>
      下游系统
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td rowspan="8">
      地服运行管理系统
    </lark-td>
    <lark-td rowspan="8">
      地服保障事件
    </lark-td>
    <lark-td>
      航班保障节点动态更新事件（DPUE）
    </lark-td>
    <lark-td rowspan="8">
      航空收费系统、A-CDM、空侧运行管理系统、智能数据中心
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      航班保障节点动态整表请求事件（RQDP）
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      航班保障节点动态整表事件（DPDL）
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      航班保障节点基础信息增加事件（BDIE）
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      航班保障节点基础信息变更事件（BDUE）
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      航班保障节点基础信息删除事件（BDDE）
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      航班保障节点基础信息请求消息（RQBD）
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      航班保障节点基础信息整表同步（BDDL）
    </lark-td>
  </lark-tr>
</lark-table>


#### 离港系统（电子告知书）（二标）

#### 安检信息管理系统（二标）
安检信息系统提供的数据将通过AESB总线MQ接口形式发布，所有接入系统均需要按照AESB规范进行数据的接入。
接口信息如下：


<lark-table rows="2" cols="4" column-widths="156,119,293,205">

  <lark-tr>
    <lark-td>
      系统名称 {align="center"}
    </lark-td>
    <lark-td colspan="2">
      接口事件 {align="center"}
    </lark-td>
    <lark-td>
      下游系统 {align="center"}
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      安检信息系统
    </lark-td>
    <lark-td>
      旅客事件
    </lark-td>
    <lark-td>
      旅客开包事件（SCIMS-LKKB）
    </lark-td>
    <lark-td>
      航班信息显示系统、智能数据中心
    </lark-td>
  </lark-tr>
</lark-table>


#### 行李处理系统（范德兰德）
行李分拣系统提供的数据将通过AESB总线MQ接口形式发布，所有接入系统均需要按照AESB规范进行数据的接入。
接口信息如下：

<lark-table rows="5" cols="4" column-widths="109,101,341,220">

  <lark-tr>
    <lark-td>
      系统名称
    </lark-td>
    <lark-td colspan="2">
      接口事件 {align="center"}
    </lark-td>
    <lark-td>
      下游系统 {align="center"}
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td rowspan="4">
      行李分拣系统
    </lark-td>
    <lark-td rowspan="4">
      资源数据
    </lark-td>
    <lark-td>
      资源整体表（MQ-BAGGAGE-001）
    </lark-td>
    <lark-td rowspan="4">
      航班信息显示系统、智能数据中心
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      资源新增数据（MQ-BAGGAGE-002）
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      资源删除数据（MQ-BAGGAGE-003）
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      资源更新数据（MQ-BAGGAGE-004）
    </lark-td>
  </lark-tr>
</lark-table>


#### <text bgcolor="yellow">机场地理信息系统（三标）</text>
工程地理信息系统提供的数据将通过AESB总线API的接口形式发布，所有接入系统均需要按照AESB规范进行数据的接入。
接口信息如下：

<lark-table rows="5" cols="4" column-widths="140,138,373,121">

  <lark-tr>
    <lark-td>
      系统名称 {align="center"}
    </lark-td>
    <lark-td colspan="2">
      接口事件 {align="center"}
    </lark-td>
    <lark-td>
      下游系统 {align="center"}
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td rowspan="4">
      工程地理信息系统
    </lark-td>
    <lark-td rowspan="2">
      地图服务
    </lark-td>
    <lark-td>
      二维地图服务（API-MAP-2D）
    </lark-td>
    <lark-td rowspan="4">
      智能数据中心、贵宾系统、商业管理平台、物联网平台、智能停车管理系统、旅客体验系统、旅客流向分析及服务调度系统、机坪车辆管理系统、地服运行系统、航班信息显示系统、商业管理平台
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      三维地图服务（API-MAP-DATA）
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td rowspan="2">
      空间数据服务
    </lark-td>
    <lark-td>
      空间数据服务（API-MAP-3D）
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      空间分析服务（API-MAP-analysis）
    </lark-td>
  </lark-tr>
</lark-table>



#### <text bgcolor="yellow">行李全流程跟踪系统（三标）</text>

#### T3泊位引导系统
泊位引导系统提供的数据将通过AESB总线MQ接口形式发布，所有接入系统均需要按照AESB规范进行数据的接入。
接口信息如下：

<lark-table rows="4" cols="4" column-widths="97,102,343,229">

  <lark-tr>
    <lark-td>
      系统名称
    </lark-td>
    <lark-td colspan="2">
      接口事件
    </lark-td>
    <lark-td>
      下游系统
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td rowspan="3">
      泊位引导系统
    </lark-td>
    <lark-td rowspan="2">
      挡轮数据
    </lark-td>
    <lark-td>
      上挡轮更新数据（MQ-DGS-001）
    </lark-td>
    <lark-td rowspan="3">
      地服运行系统、智能数据中心
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      下挡轮更新数据（MQ-DGS-002）
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      机位数据
    </lark-td>
    <lark-td>
      机位状态更新数据（MQ-DGS-003）
    </lark-td>
  </lark-tr>
</lark-table>


#### <text bgcolor="yellow">航站楼协同决策管理系统（三标）</text>

### 中台业务
#### <text bgcolor="yellow">物联网平台（三标）</text>
物联网平台提供的数据将通过AESB总线MQ和API的接口形式发布，所有接入系统均需要按照AESB规范进行数据的接入。
接口信息如下：

<lark-table rows="4" cols="4" column-widths="125,145,353,149">

  <lark-tr>
    <lark-td>
      系统名称
    </lark-td>
    <lark-td colspan="2">
      接口事件 {align="center"}
    </lark-td>
    <lark-td>
      下游系统 {align="center"}
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td rowspan="3">
      物联网平台
    </lark-td>
    <lark-td rowspan="2">
      位置数据MQ
    </lark-td>
    <lark-td>
      Lora位置数据（MQ-UNIIOT-001）
    </lark-td>
    <lark-td rowspan="3">
      智能数据中心、地服运行系统、设备设施管理系统
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      UW位置数据（MQ-UNIIOT-002）
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      设备数据API
    </lark-td>
    <lark-td>
      基础数据（API-UNIIOT-001）
    </lark-td>
  </lark-tr>
</lark-table>


#### AI中台（集团）

#### <text bgcolor="yellow">高精度综合定位系统（三标）</text>
高精度定位系统提供的数据将通过AESB总线API的接口形式发布，所有接入系统均需要按照AESB规范进行数据的接入。
接口信息如下：

<lark-table rows="19" cols="4" column-widths="98,138,374,163">

  <lark-tr>
    <lark-td>
      系统名称 {align="center"}
    </lark-td>
    <lark-td colspan="2">
      接口事件 {align="center"}
    </lark-td>
    <lark-td>
      下游系统 {align="center"}
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td rowspan="13">
      高精度定位系统
    </lark-td>
    <lark-td rowspan="4">
      告警数据
    </lark-td>
    <lark-td>
      处理告警（API-LBS-001）
    </lark-td>
    <lark-td rowspan="17">
      商业管理平台、物联网平台、智能数据中心 、TCDM管理平台
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      近7天告警统计（API-LBS-002）
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      告警信息（时间）（API-LBS-003）
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      告警信息（条数）（API-LBS-004）
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td rowspan="2">
      场景数据
    </lark-td>
    <lark-td>
      反向场景信息（API-LBS-005）
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      场景列表（API-LBS-006）
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td rowspan="4">
      位置数据
    </lark-td>
    <lark-td>
      定位信息（场景）（API-LBS-007）
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      定位信息（人员）（API-LBS-008）
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      历史轨迹（设备）（API-LBS-009）
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      Beacon位置数据（API-LBS-010）
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td rowspan="3">
      统计数据
    </lark-td>
    <lark-td>
      基础数据（API-LBS-011）
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      导航次数统计（API-LBS-012）
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      地图搜索统计（API-LBS-013）
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td rowspan="4">
    </lark-td>
    <lark-td rowspan="4">
      定位对象
    </lark-td>
    <lark-td>
      获取定位对象列表(API-LBS-014)
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      获取定位对象详情(API-LBS-015)
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      修改定位对象(API-LBS-016)
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      定位对象绑定解绑(API-LBS-017)
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
    </lark-td>
    <lark-td>
      手推车 {align="center"}
    </lark-td>
    <lark-td>
      手推车告警接口
    </lark-td>
    <lark-td>
    </lark-td>
  </lark-tr>
</lark-table>



#### 旅客服务平台（二标）
#### 统一身份认证中心（集团）


### 货运业务
#### 货运服务总线（四标）

#### 机坪车辆管理系统
机坪车辆管理系统提供的数据将通过AESB总线MQ的接口形式发布，所有接入系统均需要按照AESB规范进行数据的接入。
接口信息如下：

<lark-table rows="7" cols="4" column-widths="167,134,372,99">

  <lark-tr>
    <lark-td>
      系统名称 {align="center"}
    </lark-td>
    <lark-td colspan="2">
      接口事件 {align="center"}
    </lark-td>
    <lark-td>
      下游系统 {align="center"}
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td rowspan="6">
      车辆管理系统
    </lark-td>
    <lark-td rowspan="3">
      车辆数据MQ
    </lark-td>
    <lark-td>
      车辆上线（MQ-UNICAR-001）
    </lark-td>
    <lark-td rowspan="6">
      机场全景系统、空侧运行管理系统、智能数据中心
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      车辆下线（MQ-UNICAR-002）
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      车辆位置（MQ-UNICAR-003）
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      部门数据API
    </lark-td>
    <lark-td>
      部门数据（API-UNICAR-001）
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td rowspan="2">
      车辆数据API
    </lark-td>
    <lark-td>
      车辆基础数据（API-UNICAR-002）
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      车辆类型数据（API-UNICAR-003）
    </lark-td>
  </lark-tr>
</lark-table>


#### 呼叫中心
呼叫中心提供的数据将通过AESB总线API的接口形式发布，所有接入系统均需要按照AESB规范进行数据的接入。
接口信息如下：

<lark-table rows="7" cols="4" column-widths="98,98,335,242">

  <lark-tr>
    <lark-td>
      系统名称 {align="center"}
    </lark-td>
    <lark-td colspan="2">
      接口事件 {align="center"}
    </lark-td>
    <lark-td>
      下游系统 {align="center"}
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td rowspan="6">
      呼叫中心
    </lark-td>
    <lark-td rowspan="3">
      呼叫事件
    </lark-td>
    <lark-td>
      呼叫记录查询（CCS-API-001）
    </lark-td>
    <lark-td rowspan="6">
      智能数据中心 {align="center"}
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      转接记录（CCS-API-002）
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      状态监控（CCS-API-003）
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      查询事件
    </lark-td>
    <lark-td>
      质检查询（CCS-API-005）
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td rowspan="2">
      统计事件
    </lark-td>
    <lark-td>
      话务统计（CCS-API-004）
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      自助服务统计（CCS-API-006）
    </lark-td>
  </lark-tr>
</lark-table>


#### 旅客体验系统
旅客体验系统提供的数据将通过AESB总线API的接口形式发布，所有接入系统均需要按照AESB规范进行数据的接入。
接口信息如下：

<lark-table rows="4" cols="4" column-widths="149,110,339,173">

  <lark-tr>
    <lark-td>
      系统名称 {align="center"}
    </lark-td>
    <lark-td colspan="2">
      接口事件 {align="center"}
    </lark-td>
    <lark-td>
      下游系统 {align="center"}
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td rowspan="3">
      旅客体验系统
    </lark-td>
    <lark-td rowspan="3">
      投诉事件
    </lark-td>
    <lark-td>
      投诉（API-QMS-001）
    </lark-td>
    <lark-td rowspan="3">
      智能数据中心、呼叫中心
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      投诉撤销（API-QMS-002）
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      投诉建议数据（API-QMS-003）
    </lark-td>
  </lark-tr>
</lark-table>



#### 贵宾管理系统
贵宾管理系统提供的数据将通过AESB总线API的接口形式发布，所有接入系统均需要按照AESB规范进行数据的接入。
接口信息如下：

<lark-table rows="5" cols="4" column-widths="145,107,349,170">

  <lark-tr>
    <lark-td>
      系统名称 {align="center"}
    </lark-td>
    <lark-td colspan="2">
      接口事件 {align="center"}
    </lark-td>
    <lark-td>
      下游系统 {align="center"}
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td rowspan="4">
      贵宾系统
    </lark-td>
    <lark-td>
      会员信息
    </lark-td>
    <lark-td>
      会员信息（API-VSMS-001）
    </lark-td>
    <lark-td rowspan="4">
      智能数据中心、呼叫中心
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td rowspan="3">
      服务信息
    </lark-td>
    <lark-td>
      服务预约（API-VSMS-002）
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      服务取消（API-VSMS-003）
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      服务状态查询（API-VSMS-004）
    </lark-td>
  </lark-tr>
</lark-table>


#### 服务质量执行测量系统
服务质量执行测量系统提供的数据将通过AESB总线API的接口形式发布，所有接入系统均需要按照AESB规范进行数据的接入。
接口信息如下：

<lark-table rows="4" cols="4" column-widths="116,127,311,218">

  <lark-tr>
    <lark-td>
      系统名称 {align="center"}
    </lark-td>
    <lark-td colspan="2">
      接口事件 {align="center"}
    </lark-td>
    <lark-td>
      下游系统 {align="center"}
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td rowspan="3">
      服务质量执行测量系统
    </lark-td>
    <lark-td rowspan="3">
      投诉事件
    </lark-td>
    <lark-td>
      投诉（API-QMS-001）
    </lark-td>
    <lark-td rowspan="3">
      智能数据中心、呼叫中心
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      投诉撤销（API-QMS-002）
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      投诉建议数据（API-QMS-003）
    </lark-td>
  </lark-tr>
</lark-table>



#### 机场客户管理系统
机场客户管理系统在总线平台使用MQ的接口形式消费员工管理系统的员工数据更新提醒数据，不主动提供数据。

#### 旅客流向分析与服务调度系统
旅客流向分析与服务调度系统提供的数据将通过AESB总线MQ的接口形式发布，所有接入系统均需要按照AESB规范进行数据的接入。
接口信息如下：

<lark-table rows="5" cols="4" column-widths="98,94,358,222">

  <lark-tr>
    <lark-td>
      系统名称 {align="center"}
    </lark-td>
    <lark-td colspan="2">
      接口事件 {align="center"}
    </lark-td>
    <lark-td>
      下游系统 {align="center"}
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td rowspan="4">
      旅客流向分析及服务调度系统
    </lark-td>
    <lark-td rowspan="4">
      旅客服务
    </lark-td>
    <lark-td>
      旅客建议数据（MQ-TAMS-PAD）
    </lark-td>
    <lark-td rowspan="4">
      旅客运行管理系统、旅客体验系统、综合交通管理平台、智能数据中心
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      旅客流量数据（MQ-TAMS-PTV）
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      旅客人数数据（MQ-TAMS-PTN）
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      异常行为数据（MQ-TAMS-NAA）
    </lark-td>
  </lark-tr>
</lark-table>


#### 旅客运行及服务管理平台
旅客运行及服务管理平台提供的数据将通过AESB总线API的接口形式发布，所有接入系统均需要按照AESB规范进行数据的接入。
接口信息如下：


#### 机场门户
机场门户网站在总线平台使用API的接口形式调用综合交通管理平台的数据，不主动提供数据。
### 交通业务
#### 智能停车场管理系统
智能停车场管理系统提供的数据将通过AESB总线API的接口形式发布，所有接入系统均需要按照AESB规范进行数据的接入。
接口信息如下：





<lark-table rows="17" cols="4" column-widths="104,51,512,105">

  <lark-tr>
    <lark-td>
      系统名称 {align="center"}
    </lark-td>
    <lark-td colspan="2">
      接口事件 {align="center"}
    </lark-td>
    <lark-td>
      下游系统 {align="center"}
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td rowspan="16">
      智能停车场管理系统
    </lark-td>
    <lark-td rowspan="16">
      信信息查询API
    </lark-td>
    <lark-td>
      获取车场当前剩余车位数（API-VEHICLE-009）
    </lark-td>
    <lark-td rowspan="16">
      智能数据中心、综合交通管理平台、旅客体验系统、贵宾管理系统
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      查询车辆停放位置（API-VEHICLE-015）
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      预约下发（API-VEHICLE-016）
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      获取车位进出车辆上报（寻车/诱导系统）（API-VEHICLE-011）
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      获取停车场收费信息（API-VEHICLE-005）
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      获取停车场统计信息（API-VEHICLE-004）
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      获取通行车辆信息（API-VEHICLE-002）
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      获取停车场统计数据（API-VEHICLE-019）
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      获取收费明细信息（API-VEHICLE-010）
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      获取车辆入场信息（API-VEHICLE-007）
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      获取车辆出场信息（API-VEHICLE-008）
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      获取停车场个楼层车位停车情况（API-VEHICLE-006）
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      获取车位空余信息（API-VEHICLE-003）
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      获取停车场车位信息（API-VEHICLE-001）
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      获取停车场实时数据（API-VEHICLE-018）
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      获取停车场基本信息（API-VEHICLE-017）
    </lark-td>
  </lark-tr>
</lark-table>



#### 出租车蓄车场管理系统
出租车蓄车场管理系统提供的数据将通过AESB总线API的接口形式发布，所有接入系统均需要按照AESB规范进行数据的接入。
接口信息如下：

<lark-table rows="24" cols="4" column-widths="98,113,305,256">

  <lark-tr>
    <lark-td>
      系统名称
    </lark-td>
    <lark-td colspan="2">
      接口事件
    </lark-td>
    <lark-td>
      下游系统
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td rowspan="23">
      出租车蓄车场管理系统
    </lark-td>
    <lark-td>
      登录事件
    </lark-td>
    <lark-td>
      登录（获取token）
    </lark-td>
    <lark-td rowspan="23">
      智能数据中心、综合交通管理平台
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td rowspan="2">
      授权事件
    </lark-td>
    <lark-td>
      蓄车池、上客区实时车辆数据
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      蓄车池/上客区/大巴车场车辆授权
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td rowspan="2">
      司机信息
    </lark-td>
    <lark-td>
      获取司机签到信息列表
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      获取司机列表消息
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td rowspan="4">
      流量信息
    </lark-td>
    <lark-td>
      获取补贴车小时流量
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      获取补贴车日流量
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      获取蓄车场/上客区小时进出流量
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      获取蓄车场/上客区日进出流量
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td rowspan="10">
      列表信息
    </lark-td>
    <lark-td>
      获取上客区列表
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      获取操作日志列表数据
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      获取短途补贴列表信息
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      获取调度信息列表
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      获取蓄车池列表
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      获取黑名单列表详情
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      获取车辆列表信息
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      获取出租车公司列表信息
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      获取旅客排队分析
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      获取意见反馈列表数据
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      订阅消息
    </lark-td>
    <lark-td>
      设置订阅进出车消息接口
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      设备状态
    </lark-td>
    <lark-td>
      获取设备状态
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td rowspan="2">
      进出记录
    </lark-td>
    <lark-td>
      获取上客区进出记录
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      获取蓄车池进出记录
    </lark-td>
  </lark-tr>
</lark-table>


#### 大巴车站管理系统
大巴车站管理系统提供的数据将通过AESB总线API的接口形式发布，所有接入系统均需要按照AESB规范进行数据的接入。
接口信息如下：

<lark-table rows="16" cols="4" column-widths="165,74,401,132">

  <lark-tr>
    <lark-td>
      系统名称 {align="center"}
    </lark-td>
    <lark-td colspan="2">
      接口事件 {align="center"}
    </lark-td>
    <lark-td>
      下游系统 {align="center"}
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td rowspan="15">
      大巴车站管理系统
    </lark-td>
    <lark-td rowspan="15">
      信息查询
    </lark-td>
    <lark-td>
      出票信息（API-BSMS-001）
    </lark-td>
    <lark-td rowspan="15">
      智能数据中心、综合交通管理平台、旅客体验系统、智能停车场管理系统、自动广播
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      查询线上购票信息（API-BSMS-002）
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      查询报班信息（API-BSMS-003）
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      查询发班单信息（API-BSMS-004）
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      查询在线购票付款信息（API-BSMS-005）
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      查询在线退票退款信息（API-BSMS-006）
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      票价信息（API-BSMS-007）
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      查询班次信息（API-BSMS-008）
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      查询运输企业信息（API-BSMS-009）
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      司机信息（API-BSMS-010）
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      查询出站单信息（API-BSMS-011）
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      查询线路信息（API-BSMS-012）
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      查询站点信息（API-BSMS-013）
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      查询车辆信息（API-BSMS-014）
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      站点线路信息（API-BSMS-015）
    </lark-td>
  </lark-tr>
</lark-table>


#### 货运安检信息系统
货运安检信息系统提供的数据将通过AESB总线MQ的接口形式发布，所有接入系统均需要按照AESB规范进行数据的接入。
接口信息如下：

<lark-table rows="4" cols="4" column-widths="123,99,411,139">

  <lark-tr>
    <lark-td>
      系统名称
    </lark-td>
    <lark-td colspan="2">
      接口事件 {align="center"}
    </lark-td>
    <lark-td>
      下游系统
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td rowspan="3">
      货运安检信息系统
    </lark-td>
    <lark-td rowspan="3">
      运单数据
    </lark-td>
    <lark-td>
      运单承运数据（MQ-ALP-CYB）
    </lark-td>
    <lark-td rowspan="3">
      智能数据中心
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      运单基础数据（MQ-ALP-AWBINFO）
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      运单操作节点数据（MQ-ALP-AWBSTATUS）
    </lark-td>
  </lark-tr>
</lark-table>



#### 货代管理系统
货代管理系统在总线平台使用MQ的接口形式消费航班类接口数据，不主动提供数据。

#### 货站管理系统
货站管理系统在总线平台使用MQ的接口形式消费航班类接口数据，不主动提供数据。

#### 物流信息平台
物流信息平台在总线平台使用MQ的接口形式消费航班类接口数据，不主动提供数据。

#### 综合交通管理平台
综合交通管理平台提供的数据将通过AESB总线API的接口形式发布，所有接入系统均需要按照AESB规范进行数据的接入。
接口信息如下：


<lark-table rows="34" cols="4" column-widths="123,88,453,108">

  <lark-tr>
    <lark-td>
      系统名称
    </lark-td>
    <lark-td colspan="2">
      接口事件
    </lark-td>
    <lark-td>
      下游系统
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td rowspan="33">
      综合交通管理平台
    </lark-td>
    <lark-td rowspan="2">
      航班
    </lark-td>
    <lark-td>
      获取航班动态（itmsFlightDynamic）
    </lark-td>
    <lark-td rowspan="33">
      智能数据中心、旅客体验系统、旅客流向分析及服务调度系统、媒体发布系统、安全保卫管理平台、自动广播 {align="center"}
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      航班客流量预测（itmsFlightProphet）
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td rowspan="4">
      机场大巴
    </lark-td>
    <lark-td>
      机场大巴线路（itmsAirportBusLine）
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      机场大巴站点（itmsAirportBusStation）
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      机场大巴班次（itmsAirportBusShift）
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      机场大巴客流量预测（itmsAirportBusProphet）
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td rowspan="4">
      长途汽车
    </lark-td>
    <lark-td>
      长途汽车线路（itmsCoachLine）
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      长途汽车站点（itmsCoachStation）
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      长途汽车班次（itmsAirportBusShift）
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      长途汽车客流量预测（itmsCoachProphet）
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td rowspan="4">
      出租车
    </lark-td>
    <lark-td>
      出租车机场范围内车辆资源服务（itmsTaxiResource））
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      出租车机场排队情况服务（itmsTaxiQueue）
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      出租车机场范围内订单时间段数量统计服务（itmsTaxiOrderPeriod）
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      出租车机场范围内OD区域数量统计服务（itmsTaxiOrderRegion）
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td rowspan="4">
      网约车
    </lark-td>
    <lark-td>
      网约车机场范围内车辆资源服务（itmsRideHailingResource）
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      网约车机场排队情况服务（itmsRideHailingQueue）
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      网约车机场范围内订单时间段数量统计服务（itmsRideHailingOrderPeriod）
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      网约车机场范围内OD区域数量统计服务（itmsRideHailingOrderRegion）
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td rowspan="2">
      公交车
    </lark-td>
    <lark-td>
      公交车线路数据（itmsBusLines）
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      公交车站点（itmsBusStations）
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td rowspan="5">
      地铁
    </lark-td>
    <lark-td>
      地铁线路（itmsMetroLine）
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      地铁站点（itmsMetroStation）
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      地铁实时班次（itmsMetroShift）
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      地铁站点客流量（itmsMetroStationFlow）
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      地铁线路客流量（itmsMetroLineFlow）
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td rowspan="4">
      停车场
    </lark-td>
    <lark-td>
      停车场信息（itmsParkingLot）
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      停车场区域信息（itmsParkingLotArea）
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      停车场实时车位数量（itmsParkingLotDynSpace）
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      停车场数据回传接口（itmsParkingLotRetrieval）
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td rowspan="3">
      路网
    </lark-td>
    <lark-td>
      道路基础信息（itmsRoadBase）
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      道路流量信息（itmsRoadFlow）
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      道路拥挤信息（itmsRoadCongestion）
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      统计
    </lark-td>
    <lark-td>
      旅客分流统计信息（itmsStatisticsPassengerSplit）
    </lark-td>
  </lark-tr>
</lark-table>


#### 交通信息发布及查询系统
交通信息发布及查询系统在总线平台使用MQ的接口形式消费航班类接口数据，不主动提供数据。

### 安防业务
#### 航空安保一体化平台（一标）
安全保卫综合管理平台提供的数据将通过AESB总线API的接口形式发布，所有接入系统均需要按照AESB规范进行数据的接入。
接口信息如下：

<lark-table rows="3" cols="4" column-widths="143,106,259,263">

  <lark-tr>
    <lark-td>
      系统名称 {align="center"}
    </lark-td>
    <lark-td colspan="2">
      接口事件 {align="center"}
    </lark-td>
    <lark-td>
      下游系统 {align="center"}
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td rowspan="2">
      安全保卫综合管理平台
    </lark-td>
    <lark-td rowspan="2">
      分析数据
    </lark-td>
    <lark-td>
      视频分析报警数据（MQ-PSIM-001）
    </lark-td>
    <lark-td rowspan="2">
      旅客流向分析及服务调度系统、全景监控系统、综合交通管理平台、智能数据中心
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      客流分析统计数据（MQ-PSIM-002）
    </lark-td>
  </lark-tr>
</lark-table>



#### T3门禁系统（一标）
#### 证件管理系统（一标）
#### 交通智能卡口工程及航站区监控系统
交通智能卡口工程及航站区监控系统提供的数据将通过AESB总线API和MQ的接口形式发布，所有接入系统均需要按照AESB规范进行数据的接入。
接口信息如下：

<lark-table rows="3" cols="4" column-widths="147,104,236,285">

  <lark-tr>
    <lark-td>
      系统名称
    </lark-td>
    <lark-td colspan="2">
      接口事件 {align="center"}
    </lark-td>
    <lark-td>
      下游系统
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td rowspan="2">
      交通智能卡口工程及航站区监控系统
    </lark-td>
    <lark-td>
      卡口资源
    </lark-td>
    <lark-td>
      分页获取卡口资源（API-Hiktpc-001）
    </lark-td>
    <lark-td rowspan="2">
      贵宾管理系统、综合交通管理平台、智能数据中心
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      过车
    </lark-td>
    <lark-td>
      过车数据（MQ-Hiktpc-001）
    </lark-td>
  </lark-tr>
</lark-table>


#### 围界入侵报警系统（中航弱电）
围界报警监控提供的数据将通过AESB总线MQ的接口形式发布，所有接入系统均需要按照AESB规范进行数据的接入。
接口信息如下：

<lark-table rows="3" cols="3" column-widths="116,318,338">

  <lark-tr>
    <lark-td>
      系统名称
    </lark-td>
    <lark-td>
      接口事件
    </lark-td>
    <lark-td>
      下游系统
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td rowspan="2">
      围界报警监控系统
    </lark-td>
    <lark-td>
      报警数据（MQ-PSS-001）
    </lark-td>
    <lark-td rowspan="2">
      空侧运行管理系统、智能数据中心
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      故障数据（MQ-PSS-002）
    </lark-td>
  </lark-tr>
</lark-table>


#### 飞行区道口管理系统
飞行区道口管理系统在总线平台使用API的接口形式调用车辆管理系统的车辆位置接口数据，不主动提供数据。

### 运维业务
#### 动环监控系统
动环监控系统提供的数据将通过AESB总线MQ的接口形式发布，所有接入系统均需要按照AESB规范进行数据的接入。
接口信息如下：

<lark-table rows="6" cols="4" column-widths="113,109,347,203">

  <lark-tr>
    <lark-td>
      系统名称
    </lark-td>
    <lark-td colspan="2">
      接口事件 {align="center"}
    </lark-td>
    <lark-td>
      下游系统
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td rowspan="5">
      动环监控系统
    </lark-td>
    <lark-td rowspan="2">
      告警事件MQ
    </lark-td>
    <lark-td>
      设备实时告警（MQ-PROB-001）
    </lark-td>
    <lark-td rowspan="5">
      综合能源管理平台、智能数据中心
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      设备实时告警恢复（MQ-PROB-002）
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td rowspan="3">
      设备事件API
    </lark-td>
    <lark-td>
      设备列表（API-PROB-001）
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      设备测点数据（API-PROB-002）
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      设备告警（API-PROB-003）
    </lark-td>
  </lark-tr>
</lark-table>


#### 综合能源管理平台
综合能源管理平台提供的数据将通过AESB总线API的接口形式发布，所有接入系统均需要按照AESB规范进行数据的接入。
接口信息如下：

<lark-table rows="2" cols="4" column-widths="178,104,232,259">

  <lark-tr>
    <lark-td>
      系统名称
    </lark-td>
    <lark-td colspan="2">
      接口事件 {align="center"}
    </lark-td>
    <lark-td>
      下游系统
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      综合能源管理平台
    </lark-td>
    <lark-td>
      闸机信息
    </lark-td>
    <lark-td>
      获取闸机状态（API-CEMP-001）
    </lark-td>
    <lark-td>
      智能数据中心、A-CDM
    </lark-td>
  </lark-tr>
</lark-table>


#### 设备设施管理系统
设备设施管理系统在总线平台使用API的接口形式调用动环监控系统的数据，不主动提供数据。


### 商业业务
#### 商业管理平台
商业管理平台提供的数据将通过AESB总线API和MQ的接口形式发布，所有接入系统均需要按照AESB规范进行数据的接入。
接口信息如下：

<lark-table rows="10" cols="4" column-widths="147,109,222,294">

  <lark-tr>
    <lark-td>
      系统名称
    </lark-td>
    <lark-td colspan="2">
      接口事件 {align="center"}
    </lark-td>
    <lark-td>
      下游系统
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td rowspan="9">
      商业管理系统
    </lark-td>
    <lark-td>
      登录事件
    </lark-td>
    <lark-td>
      登录授权token
    </lark-td>
    <lark-td rowspan="9">
      智能数据中心、旅客体验系统、企业资源计划
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      合同
    </lark-td>
    <lark-td>
      查询获取租赁合同信息
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td rowspan="2">
      商铺
    </lark-td>
    <lark-td>
      商铺信息
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      商铺信息添加修改事件SIAM
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td rowspan="4">
      活动政策
    </lark-td>
    <lark-td>
      消费满减政策查询接口
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      礼券兑换活动列表查询接口
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      会员折扣政策查询接口
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      积分抵现政策查询接口
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      订单
    </lark-td>
    <lark-td>
      订单信息添加修改事件OIAM
    </lark-td>
  </lark-tr>
</lark-table>


### 集团业务
#### 员工管理系统
提供的数据将通过AESB总线API和MQ的接口形式发布，所有接入系统均需要按照AESB规范进行数据的接入。
接口信息如下：

<lark-table rows="10" cols="4" column-widths="98,103,453,117">

  <lark-tr>
    <lark-td>
      系统名称 {align="center"}
    </lark-td>
    <lark-td colspan="2">
      接口事件 {align="center"}
    </lark-td>
    <lark-td>
      下游系统 {align="center"}
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td rowspan="9">
      员工管理系统
    </lark-td>
    <lark-td rowspan="4">
      员工信息
    </lark-td>
    <lark-td>
      员工通行记录同步（API-EMPLOYEE-PASS-RECORD-001）
    </lark-td>
    <lark-td rowspan="9">
      物流信息平台、门户网站、智能数据中
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      员工通行信息同步（API-EMPLOYEE-ACCESS-INFO-001）
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      员工基础信息（API-EMPLOYEE-BASIC-INFO-001）
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      员工数据更新提醒（MQ-ASMS-EIU-001）
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td rowspan="3">
      证件信息
    </lark-td>
    <lark-td>
      驾驶证信息（API-EMPLOYEE-DRIVING-LICENSE-001）
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      行驶证信息（API-EMPLOYEE-VEHICLE-DRIVING-LICENSE-001）
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      通行证信息（API-EMPLOYEE-PASS-LICENSE-001）
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td rowspan="2">
      附件
    </lark-td>
    <lark-td>
      获取附件列表（API-GET-DOC-LIST-001）
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      附件下载（API-DOWNLOAD-DOC-001）
    </lark-td>
  </lark-tr>
</lark-table>


#### 企业资源计划
企业资源计划在总线平台使用API的接口形式调用商业管理平台和财务系统的数据，不主动提供数据。

## 测试流程
### API接口联调测试流程
API接口业务流程图如下：
![](Attachments/MK7eb7iqAoEdBHxgYubcxNhHnpg.png)

①上游ISV将API接口发布至APIC；
②下游ISV通过SDK或者API调试工具调用APIC已经发布的API接口；
③APIC将ISV的请求转发至上游ISV的接口服务器；
④上游ISV的接口服务器将请求结果返回给APIC；
⑤APIC将请求结果返回给下游ISV；
联合上下游系统，确认业务系统调用的API接口返回的数据内容、格式是否正确，如数据格式或者内容有误，反馈结果给业务系统整改。

API接口联调测试流程如下：

<lark-table rows="4" cols="6" column-widths="44,86,129,118,265,136">

  <lark-tr>
    <lark-td>
      **序号**
    </lark-td>
    <lark-td>
      **流程**
    </lark-td>
    <lark-td>
      **测试项目**
    </lark-td>
    <lark-td>
      **具体操作流程**
    </lark-td>
    <lark-td>
      **预期实现效果**
    </lark-td>
    <lark-td>
      **完成情况（预期效果+测试情况）**
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      1
    </lark-td>
    <lark-td>
      连通性测试
    </lark-td>
    <lark-td>
      测试AEBS与业务系统网络连通性
    </lark-td>
    <lark-td>
      AESB总线与业务系统在服务器互ping地址
    </lark-td>
    <lark-td>
      有数据返回！网络连通性正常！
    </lark-td>
    <lark-td>
      网络连通性正常！
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      2
    </lark-td>
    <lark-td>
      测试API接口
    </lark-td>
    <lark-td>
      下游系统按照上游系统提供的IDD文档进行API接口测试调用
    </lark-td>
    <lark-td>
      ①Postman等调测工具进行调测；
      ②服务器使用总线提供的SDK调用API进行调测；
    </lark-td>
    <lark-td>
      **正常情况：**
      状态码200，返回数据（部分接口返回空数据为正常现象，需ISV自行调整后端返回内容）！
      **错误情况：**
      状态码401，认证参数错误！
      状态码404，请求路径有误！
      状态码500，内部服务错误！
      状态码502，后端接口不可用！
    </lark-td>
    <lark-td>
      状态码200，正常返回数据！
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      3
    </lark-td>
    <lark-td>
      反馈结果给上游系统
    </lark-td>
    <lark-td>
      /
    </lark-td>
    <lark-td>
      /
    </lark-td>
    <lark-td>
      数据格式与内容均符合要求！
    </lark-td>
    <lark-td>
      数据格式与内容均符合要求！如不满足预期，联系上游系统整改后重复第一步骤
    </lark-td>
  </lark-tr>
</lark-table>


### MQ接口联调测试流程
MQ接口业务流程图如下：
![](Attachments/PExxbxmN3ov5f2xdmDbcuWRkn9f.png)

①上游ISV将消息传输到MQS(Rocket MQ)的消息队列；
②下游ISV订阅上游ISV的消息队列，消费消息数据。

通过AESB总线MQ实例-消息服务MQS-消息查询-指定topic可以按时间维度查询消息内容、tag、生产消费时间，生产者和消费者的消费状态等。
MQ接口联调测试流程如下：

<lark-table rows="4" cols="6" column-widths="44,82,154,104,260,135">

  <lark-tr>
    <lark-td>
      **序号**
    </lark-td>
    <lark-td>
      **流程**
    </lark-td>
    <lark-td>
      **测试项目**
    </lark-td>
    <lark-td>
      **具体操作流程**
    </lark-td>
    <lark-td>
      **预期实现效果**
    </lark-td>
    <lark-td>
      **完成情况（预期效果+测试情况）**
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      1
    </lark-td>
    <lark-td>
      连通性测试
    </lark-td>
    <lark-td>
      测试AEBS与业务系统网络连通性
    </lark-td>
    <lark-td>
      AESB总线与业务系统在服务器互ping地址
    </lark-td>
    <lark-td>
      有数据返回！网络连通性正常！
    </lark-td>
    <lark-td>
      网络连通性正常！
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      2
    </lark-td>
    <lark-td>
      测试消息收发状态
    </lark-td>
    <lark-td>
      上游业务系统按照IDD接口文档中每个事件发送消息至指定topic
    </lark-td>
    <lark-td>
      由拥有topic的ISV发送消息到topic，通过总线的消息轨迹（前提是业务系统程序中开启消息轨迹）或者下游系统的程序回显查看消费状态
    </lark-td>
    <lark-td>
      **正常情况：**
      收发消息正常，内容格式无误，总线消息轨迹中回显生产者和消费者！(需上下游业务系统开启消息轨迹！)
      **错误情况：**
      消费失败！网络波动或地址有误！
      下游系统程序无回显，topic/消费组等参数填写有误！
    </lark-td>
    <lark-td>
      业务系统正常收发数据，且数据内容无误！
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      3
    </lark-td>
    <lark-td>
      反馈结果给上游系统
    </lark-td>
    <lark-td>
      /
    </lark-td>
    <lark-td>
      /
    </lark-td>
    <lark-td>
      数据格式与内容均符合要求！
    </lark-td>
    <lark-td>
      数据格式与内容均符合要求！如不满足预期，联系上游系统整改后重复第一步骤
    </lark-td>
  </lark-tr>
</lark-table>


# 测试结论
## 测试问题

<lark-table rows="11" cols="3" column-widths="116,458,199">

  <lark-tr>
    <lark-td>
      序号
    </lark-td>
    <lark-td>
      测试问题
    </lark-td>
    <lark-td>
      当前状态 {align="center"}
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      1
    </lark-td>
    <lark-td>
      GIS工程地理信息系统API接口测试响应较长
    </lark-td>
    <lark-td>
      已解决 {align="center"}
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      2
    </lark-td>
    <lark-td>
      商业管理平台对接总线提示秘钥无法解析
    </lark-td>
    <lark-td>
      已解决 {align="center"}
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      3
    </lark-td>
    <lark-td>
      综合能源管理平台无法消费登机桥的消息
    </lark-td>
    <lark-td>
      已解决 {align="center"}
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      4
    </lark-td>
    <lark-td>
      综合能源管理平台无法在总线回显消息轨迹
    </lark-td>
    <lark-td>
      已解决 {align="center"}
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      5
    </lark-td>
    <lark-td>
      自动广播系统消费消息时延较长
    </lark-td>
    <lark-td>
      已解决 {align="center"}
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      6
    </lark-td>
    <lark-td>
      空侧运行管理系统、ACDM等无法消费多条消息
    </lark-td>
    <lark-td>
      已解决 {align="center"}
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      7
    </lark-td>
    <lark-td>
      高杆灯监控系统接入无响应
    </lark-td>
    <lark-td>
      已解决 {align="center"}
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      8
    </lark-td>
    <lark-td>
      泊位引导系统应用程序版本过高，无法连接平台
    </lark-td>
    <lark-td>
      已解决 {align="center"}
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      9
    </lark-td>
    <lark-td>
      总线平台概率性无法消费IMF航班动态消息接口
    </lark-td>
    <lark-td>
      调整中 {align="center"}
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      10
    </lark-td>
    <lark-td>
      航显系统回复能够成功消费但无法收到消息
    </lark-td>
    <lark-td>
      调整中 {align="center"}
    </lark-td>
  </lark-tr>
</lark-table>


## 解决措施

<lark-table rows="11" cols="3" column-widths="92,330,331">

  <lark-tr>
    <lark-td>
      序号 {align="center"}
    </lark-td>
    <lark-td>
      问题 {align="center"}
    </lark-td>
    <lark-td>
      解决措施 {align="center"}
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      1
    </lark-td>
    <lark-td>
      GIS工程地理信息系统API接口测试响应较长
    </lark-td>
    <lark-td>
      打开总线APIC公网出口，使用GIS的EIP代理接口，测试时延较低
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      2
    </lark-td>
    <lark-td>
      商业管理平台对接总线提示秘钥无法解析
    </lark-td>
    <lark-td>
      使用总线提供的DEMO对接测试，调整程序后可连接总线发送消息
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      3
    </lark-td>
    <lark-td>
      综合能源管理平台无法消费登机桥的消息
    </lark-td>
    <lark-td>
      填写参数有误，修改后正常消费；
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      4
    </lark-td>
    <lark-td>
      综合能源管理平台无法在总线回显消息轨迹
    </lark-td>
    <lark-td>
      程序中缺失参数，补充后正常回显
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      5
    </lark-td>
    <lark-td>
      自动广播系统消费消息时延较长
    </lark-td>
    <lark-td>
      建议使用内网地址连接后有明显改善
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      6
    </lark-td>
    <lark-td>
      空侧运行管理系统、ACDM等无法消费多条消息
    </lark-td>
    <lark-td>
      建议一个消费组对应一个topic，方便管理，正常消费全部消息；
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      7
    </lark-td>
    <lark-td>
      高杆灯监控系统接入无响应
    </lark-td>
    <lark-td>
      调整消息队列客户端版本
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      8
    </lark-td>
    <lark-td>
      泊位引导系统应用程序版本过高，无法连接平台
    </lark-td>
    <lark-td>
      下调Java版本，使用Java8连接平台
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      9
    </lark-td>
    <lark-td>
      总线平台概率性无法消费IMF航班动态消息接口
    </lark-td>
    <lark-td>
      更新总线平台版本，修复已知性问题，并提供回显给IMF平台
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      10
    </lark-td>
    <lark-td>
      航显系统回复能够成功消费但无法收到消息
    </lark-td>
    <lark-td>
      新建消费组，建立订阅关系后重试消费
    </lark-td>
  </lark-tr>
</lark-table>

## 测试结果
整体测试结果待所有接口测试完毕后补充。

# 附件
## 测试记录表（单独提供）
## 测试过程截图（附简单文字说明）
安全保卫综合管理平台接口测试截图：
![](Attachments/QjRrbZB21oH8xXxJXcncydndnQd.png)


车辆管理系统接口测试截图：
![](Attachments/VKO2bj9LEov9TXx8RARcIrvOn3b.png)


![](Attachments/C2VJbZetzoiHRTxWFVqcyXrpnbg.png)

![](Attachments/Gb5tbO0M9oZO94xqaKQcaxXjn7d.png)


出租车蓄车场管理系统接口测试截图：
<grid cols="4">
  <column width="25">
    ![](Attachments/ViBgbTx27o9ur0xOR3JcpUMRnMc.png)

  </column>
  <column width="25">
    ![](Attachments/Imb9b4B2Xo3slbxbt6LcF2lCnxq.png)

  </column>
  <column width="25">
    ![](Attachments/NGqbbeK1No5bNJx3V7xcob3VnJg.png)

  </column>
  <column width="25">
    ![](Attachments/DeETbm5RbozwogxisC6cguKonCf.png)

  </column>
</grid>

<grid cols="4">
  <column width="25">
    ![](Attachments/PDONbLo6QoSiMZxLn06cRvnenzf.png)

  </column>
  <column width="25">
    ![](Attachments/WE61bzTnuogZnUxC8VjcqNJFnRe.png)

  </column>
  <column width="25">
    ![](Attachments/CvjcbWQMIoyjpgxKqnycIrApnjN.png)

  </column>
  <column width="25">
    ![](Attachments/MfJubV9tMoQOAOxKCsncz1Ttnvc.png)

  </column>
</grid>

<grid cols="4">
  <column width="25">
    ![](Attachments/CJaZb6nj6oh71XxWJzMc8xEEn1b.png)

  </column>
  <column width="25">
    ![](Attachments/YUuXbwGDjoZPWfx9fKdc7GbDnUd.png)

  </column>
  <column width="25">
    ![](Attachments/Utyub9j4Co6KIxxuXQccwigQnpg.png)

  </column>
  <column width="25">
    ![](Attachments/KXvpbHvJGoIU3OxmIjncOdJUn8g.png)

  </column>
</grid>

<grid cols="4">
  <column width="25">
    ![](Attachments/AwWrbNDBJoi0aexfH5KcMkLynRd.png)

  </column>
  <column width="25">
    ![](Attachments/Hdb6bzZ7OoJbZPxqSKdcarOWnUf.png)

  </column>
  <column width="25">
    ![](Attachments/QDufbfnmJopJIFxZ4DYc9sfWnsd.png)

  </column>
  <column width="25">
    ![](Attachments/COFtbvPaAomunQxVDZkc2ojZnk7.png)

  </column>
</grid>

<grid cols="4">
  <column width="25">
    ![](Attachments/Qlnab8ebUoeSv7xp54lchV0Tn4e.png)

  </column>
  <column width="25">
    ![](Attachments/OmOFbXXIeoli4dxeOzecxU8znub.png)

  </column>
  <column width="25">
    ![](Attachments/U4KrboQPUoZoODx2fMecBzysnMg.png)

  </column>
  <column width="25">
    ![](Attachments/IKxDbEgrZopX2WxY98icIGDCn1c.png)

  </column>
</grid>

![](Attachments/Qb1sbZTgnoMarmxTbWZcFfLtn9f.png)


大巴车站管理系统接口测试截图：
![](Attachments/DJD4bnVvwo2bqUxlK0pcxxmPnwI.png)

<grid cols="4">
  <column width="25">
    ![](Attachments/S2E4baLIZoqvVqxU22YcK9Thnxe.png)

  </column>
  <column width="25">
    ![](Attachments/Nb7KbLYO8o4wa4xQ0lUcWUdPnj1.png)

  </column>
  <column width="25">
    ![](Attachments/M3eQbEfTbobJBWxoMJTcl3R4n8f.png)

  </column>
  <column width="25">
    ![](Attachments/Tr8TbPjuioB2YjxriAuc5VMKnfh.png)

  </column>
</grid>

<grid cols="4">
  <column width="25">
    ![](Attachments/OL2WbKfDGotZ6Fx7u1DclJsLn4g.png)

  </column>
  <column width="25">
    ![](Attachments/DwCObQ7aaoee2ixLem6crzvZndg.png)

  </column>
  <column width="25">
    ![](Attachments/O8kcbEZODoZ5i5xqPM1c2y0rn4M.png)

  </column>
  <column width="25">
    ![](Attachments/Pf3fbMUUzoWPZJx8eOWcdtrxnYb.png)

  </column>
</grid>

<grid cols="4">
  <column width="25">
    ![](Attachments/N1wRbrgaDo78AyxGpyvcDQkGnUd.png)

  </column>
  <column width="25">
    ![](Attachments/VoxHbkrcVo9yp5xK1OncDwovnzf.png)

  </column>
  <column width="25">
    ![](Attachments/DmaDbVcezoUFYRxifsjcJX2Tnlg.png)

  </column>
  <column width="25">
    ![](Attachments/QEm4bn75Yo7ZZFxtU8AcD68On2e.png)

  </column>
</grid>

<grid cols="2">
  <column width="50">
    ![](Attachments/Z6uyb3OdAoztTxxPvi8cbVdNnzM.png)

  </column>
  <column width="50">
    ![](Attachments/ITNubJP1Hoxv8WxDmRIcLMv6nqg.png)

  </column>
</grid>


动环监控系统接口测试截图：
<grid cols="4">
  <column width="25">
    ![](Attachments/MlyJb71SgoZMr7xnLtQcq2cXnvh.png)

  </column>
  <column width="25">
    ![](Attachments/Tf42bl3fGorm5OxHPONcXEwxnGb.png)

  </column>
  <column width="25">
    ![](Attachments/SIabbSdv5o0fA7xmmgvcsqjQnPd.png)

  </column>
  <column width="25">
    ![](Attachments/EVcSbeDVZoH6iGxOD2rcvzb5nA6.png)

  </column>
</grid>

![](Attachments/MgzXbnSlSoa7qAxtd4ecr0gbnOd.png)


航班节点采集系统接口测试截图：
<grid cols="2">
  <column width="50">
    ![](Attachments/X3ktbODzaovL2rxjhYjcmUUMnvh.png)

  </column>
  <column width="50">
    ![](Attachments/VjTkbjV1corZ9TxqU5YcNP0fnLe.png)

  </column>
</grid>

呼叫中心系统接口测试截图：
<grid cols="4">
  <column width="25">
    ![](Attachments/RtWrb7M0JoXFOrxpmvYcoZm1nvb.png)

  </column>
  <column width="25">
    ![](Attachments/EhEfb4mA4ojq9Kx5m84cXMIJnSc.png)

  </column>
  <column width="25">
    ![](Attachments/Slogbfbe0oPxCTxeCTocUdUDn7j.png)

  </column>
  <column width="25">
    ![](Attachments/UPvCbyHknouHLYxCd69cshX8nVf.png)

  </column>
</grid>

![](Attachments/OXNsbeIlQo9R3Qx15jSc15R6nIg.png)

![](Attachments/IzmWbwrE3o6QFDx8K4ycVSfenQe.png)









空侧运行管理系统接口测试截图：
<grid cols="4">
  <column width="25">
    ![](Attachments/W0TabAJKKoRSI4x6YV2cqM4Jn1d.png)

  </column>
  <column width="25">
    ![](Attachments/AloPbIuzCo578oxrSddc68bUnOb.png)

  </column>
  <column width="25">
    ![](Attachments/HwEHbD5dKoajtBxPfxTcEKnpn6f.png)

  </column>
  <column width="25">
    ![](Attachments/T0mAb8aiXo3F6mxiLJ3cno8enWf.png)

  </column>
</grid>

<grid cols="2">
  <column width="50">
    ![](Attachments/SQdEbj9xXoSOmexCyMsclVP6nCf.png)

  </column>
  <column width="50">
    ![](Attachments/Wfo1bvNCMo6wmuxPWrCc6VCnnUe.png)

  </column>
</grid>


旅客流向分析及服务调度系统接口测试截图：
<grid cols="4">
  <column width="25">
    ![](Attachments/Io1qbLZLLo1jrxxfafgc7sI5nNB.png)

  </column>
  <column width="25">
    ![](Attachments/ZiRxbLBiyoHHa1xegS7c1f9UnTe.png)

  </column>
  <column width="25">
    ![](Attachments/VBieb9uFcooSHYxLojicQSU1nEd.png)

  </column>
  <column width="25">
    ![](Attachments/RI8wbDfoeoEzrzxmNx0cJpuQnfc.png)

  </column>
</grid>





旅客运行管理系统接口测试截图：
<grid cols="4">
  <column width="25">
    ![](Attachments/CSbQbHFWyoCRc9xQaXbcOhQ2nDe.png)

  </column>
  <column width="25">
    ![](Attachments/IWCubnxgqoeDmCxzVeIckhsVny9.png)

  </column>
  <column width="25">
    ![](Attachments/J7rxbxeeQo3E4kxH9evcEJbPnCd.png)

  </column>
  <column width="25">
    ![](Attachments/We5BbxVf3oNJDbxzAsRcqnQ3nIc.png)

  </column>
</grid>

<grid cols="4">
  <column width="25">
    ![](Attachments/AFkdbuBgno8QuAxYojYcg2PGnpe.png)

  </column>
  <column width="25">
    ![](Attachments/WZAQbnMEPohbzYxjkv3chODMn5d.png)

  </column>
  <column width="25">
    ![](Attachments/L6MQbIp9koaI3hxSAqGcXmxEnxm.png)

  </column>
  <column width="25">
    ![](Attachments/YR1ebJhsuoVRENxDi3xczzifnFb.png)

  </column>
</grid>

![](Attachments/KgJmbtso2oIT7SxhJdrcxZu3nQh.png)





商业管理平台接口测试截图（部分API接口暂时无法测通，商业管理平台后端调整中）：
<grid cols="3">
  <column width="33">
    ![](Attachments/DiATbWHb4o3WYex0ZRDcAB26nYf.png)

  </column>
  <column width="33">
    ![](Attachments/Q3JBb1Ll2ogeuux6aFFcU4wcn3c.png)

  </column>
  <column width="33">
    ![](Attachments/DRItb3YasoYwCOxJA27cCPSdn6f.png)

  </column>
</grid>


<grid cols="2">
  <column width="50">
    ![](Attachments/Ky0Kbl49poqfhoxYHqrczvAVnBh.png)

  </column>
  <column width="50">
    ![](Attachments/Txnpba1Zjod39SxdBAOcuzn6nHg.png)

  </column>
</grid>



物联网平台接口测试截图：
![](Attachments/E3AGbHohJovgK2xcOlBcADLRnQP.png)

应急救援系统接口测试截图：
<grid cols="4">
  <column width="25">
    ![](Attachments/MaG1bobAaosUwWx0FHLcIs7vnQh.png)

  </column>
  <column width="25">
    ![](Attachments/As4HbcdxwoxWsVxcCDsciId8n7g.png)

  </column>
  <column width="25">
    ![](Attachments/OY0YbV4OkorDgyxFS7HcSHZdnxg.png)

  </column>
  <column width="25">
    ![](Attachments/IEelbKmZHo55RhxALXXcXGvZnAg.png)

  </column>
</grid>

<grid cols="4">
  <column width="25">
    ![](Attachments/LFmCbGpztojg2Ax58GKcuFANn2g.png)

  </column>
  <column width="25">
    ![](Attachments/MfDzbHRDoo59JgxtuCkcKbGbnqh.png)

  </column>
  <column width="25">
    ![](Attachments/DlBgbIIDUo8wKZxytSwc4RamnFf.png)

  </column>
  <column width="25">
    ![](Attachments/VqaEbFEreorgAWx0K87c3OMMnEb.png)

  </column>
</grid>

![](Attachments/En4ybHD0YohAfzx71d7cRdnunDe.png)






员工管理系统接口测试截图：
<grid cols="4">
  <column width="25">
    ![](Attachments/C8gbbRz4donj61xp9t1cEsWgn9g.png)

  </column>
  <column width="25">
    ![](Attachments/SDytb6MznomZCRxqxcuc6VKknib.png)

  </column>
  <column width="25">
    ![](Attachments/IBylbvgmmoz13Lxe6AQcWEz4nSd.png)

  </column>
  <column width="25">
    ![](Attachments/IoJ6b4Kd4oNfNRx9st6cOcUznKf.png)

  </column>
</grid>

<grid cols="4">
  <column width="25">
    ![](Attachments/XVY5biLuVoZMFBxJTgOc6eAanKh.png)

  </column>
  <column width="25">
    ![](Attachments/V4eyb2v0toIeoLxHmkicjHJVnSh.png)

  </column>
  <column width="25">
    ![](Attachments/FOtPbZgXXomaYUxwfvLcTgAundc.png)

  </column>
  <column width="25">
    ![](Attachments/CY5PbQAYco9WwdxN0Tscrn6hnrf.png)

  </column>
</grid>





智能卡口系统接口测试截图：
![](Attachments/KyyzbOEy7o0NnPxdD0DcsWHbn0f.png)


智能停车场系统接口测试截图：
<grid cols="4">
  <column width="25">
    ![](Attachments/FrjMbuJdWow3GgxeszUcJR15n2M.jpg)

  </column>
  <column width="25">
    ![](Attachments/KMA5bhpQGoNEcIx8074cN3hEnXg.png)

  </column>
  <column width="25">
    ![](Attachments/TyPDbyX9loTWrxx3CTOcO0d0n1b.png)

  </column>
  <column width="25">
    ![](Attachments/MQzHbQd7CoGT29xQZkAcAmtOn0b.jpg)

  </column>
</grid>

<grid cols="4">
  <column width="25">
    ![](Attachments/TWmgbT05DoXsQWxsSaxcgNWBn8g.png)

  </column>
  <column width="25">
    ![](Attachments/WT57bLnXbotSNVx9Aqcc2zTbn3d.png)

  </column>
  <column width="25">
    ![](Attachments/Dj67b5oMooywT9x0Ct1cS5Zkn8f.png)

  </column>
  <column width="25">
    ![](Attachments/SGdobKecNosYRWxhghIcsKD6n24.png)

  </column>
</grid>

<grid cols="4">
  <column width="25">
    ![](Attachments/YB7Lb7t22okapBxdfokcwSJLnwq.png)

  </column>
  <column width="25">
    ![](Attachments/ZtZYbQNWVofqK1xcMNkc7MAFn4s.png)

  </column>
  <column width="25">
    ![](Attachments/WOfpbRMD1ozLorxI9XEc4TF0n4e.png)

  </column>
  <column width="25">
    ![](Attachments/B61Ib879Pot6aaxs8eRcyYcQnWd.png)

  </column>
</grid>

<grid cols="4">
  <column width="25">
    ![](Attachments/Uhe5bjweuoMNPMxQHR9cyOOvndd.png)

  </column>
  <column width="25">
    ![](Attachments/QUnIbcmSroCB1sxGbR1cy4OQnlg.png)

  </column>
  <column width="25">
    ![](Attachments/QHudbFEGZoJ0XExn5P3c0YPZnAR.png)

  </column>
  <column width="25">
    ![](Attachments/H9pkbkPq0oid5xxQX45cNEe2ngh.png)

  </column>
</grid>

<grid cols="3">
  <column width="33">
    ![](Attachments/AySqbqkaioDavSx6BLocOozOnZg.png)

  </column>
  <column width="33">
    ![](Attachments/ATtAbNbCfopcIWxQEjec3nDnnYf.png)

  </column>
  <column width="33">
    ![](Attachments/Q4ZmbR7V8oO3ltxaf9GcGotgnAo.png)

  </column>
</grid>







综合交通管理平台接口测试截图：
<grid cols="4">
  <column width="25">
    ![](Attachments/XdilbmYXgodAHJx7Y45cRbOCn4c.png)

  </column>
  <column width="25">
    ![](Attachments/WZrGbpSygomT63xg9ilc0bvknwc.png)

  </column>
  <column width="25">
    ![](Attachments/BMdUbJW7fo49kZxDrM2cQLKun63.png)

  </column>
  <column width="25">
    ![](Attachments/VLTcb9OH8odIDMx9HtycXn46nrf.png)

  </column>
</grid>

<grid cols="4">
  <column width="25">
    ![](Attachments/LZE0bwzePoCqonxzp70cHhDunTg.png)

  </column>
  <column width="25">
    ![](Attachments/GLJUb3fmYo5PJ5xl58TcM6QonNh.png)

  </column>
  <column width="25">
    ![](Attachments/KKGlbjbJAoarHWxN8OPcHcr4nEh.png)

  </column>
  <column width="25">
    ![](Attachments/TpNzbmednof8GixS09TcW5T5n7g.png)

  </column>
</grid>

<grid cols="4">
  <column width="25">
    ![](Attachments/RxJtbx6cmo4zqFxCuMAcxDV8nUe.png)

  </column>
  <column width="25">
    ![](Attachments/MOTsbq4nHorjeCxTuBFcDRNinId.png)

  </column>
  <column width="25">
    ![](Attachments/B9GGb7HPaoRBAYxpHlLcEFtInEe.png)

  </column>
  <column width="25">
    ![](Attachments/RC2Ubom7Bo3ruGxTpt7cMVelnP8.png)

  </column>
</grid>

<grid cols="4">
  <column width="25">
    ![](Attachments/DOo7b4K66oIB5Px9Y3CcxXx7n4d.png)

  </column>
  <column width="25">
    ![](Attachments/WBqObZlozoLvR8x9ZgPcTMs4nNy.png)

  </column>
  <column width="25">
    ![](Attachments/Rk4CbRbwpo6a6CxzpXIcuIovnk5.png)

  </column>
  <column width="25">
    ![](Attachments/GEeVbSyJSoVJiPxRBVHckJnKnVd.png)

  </column>
</grid>

<grid cols="4">
  <column width="25">
    ![](Attachments/VKV2bAalsobCvnxfVvocyYZGn2X.png)

  </column>
  <column width="25">
    ![](Attachments/BwZBbJv4TovgMixUnjec5kJJnhg.png)

  </column>
  <column width="25">
    ![](Attachments/OWOebN3USooAylx5CxMcXiQankb.png)

  </column>
  <column width="25">
    ![](Attachments/UakibrptcoBNhKxH8QAcAz01naf.png)

  </column>
</grid>

<grid cols="4">
  <column width="25">
    ![](Attachments/DNjJbPyyto0ufNxwc9vcmGXznte.png)

  </column>
  <column width="25">
    ![](Attachments/T1bdbLjlEoMpLpxNZPJc8oW5nxc.png)

  </column>
  <column width="25">
    ![](Attachments/VbG4b8QL6o0jecxopRYc8CL7nBe.png)

  </column>
  <column width="25">
    ![](Attachments/U9AtbjA31oajCrx57kCc8ESJnaf.png)

  </column>
</grid>

<grid cols="4">
  <column width="25">
    ![](Attachments/VEIFbRD9gox6PRxXFtmct0x2nsc.png)

  </column>
  <column width="25">
    ![](Attachments/Ho1TbWQHqoziiPxqIOPcUw9Lnue.png)

  </column>
  <column width="25">
    ![](Attachments/FCvnbvOFboCWPNxsoSvcULULnWc.png)

  </column>
  <column width="25">
    ![](Attachments/CMt5ba6SCo0U2NxI9l4cyCPlnYA.png)

  </column>
</grid>

<grid cols="4">
  <column width="25">
    ![](Attachments/Ao0gbIDP2o5jiaxpM7JcQQBxneg.png)

  </column>
  <column width="25">
    ![](Attachments/SDrCbmm83oDTk5xx8aUcbnawnSg.png)

  </column>
  <column width="25">
    ![](Attachments/UQtub1pH7oCNMCxD3LQcLVDHnpe.png)

  </column>
  <column width="25">
    ![](Attachments/DzptbbstCoJdH5xKmzpcAVHEnHf.png)

  </column>
</grid>

![](Attachments/TbF3bB2EqoSYKWxb2ZccDU5fnXc.png)

综合能源管理平台接口测试截图：
![](Attachments/CPhnbCBEzolEiExVp6qcwgQVn0e.png)







协同决策系统接口测试截图：
<grid cols="3">
  <column width="33">
    ![](Attachments/DstCb471zoLNvCxUasCcJXwEndh.png)

  </column>
  <column width="33">
    ![](Attachments/JWElbfFZYox1sIxMInscB4Q7nJd.png)

  </column>
  <column width="33">
    ![](Attachments/NyC5bgBd7odyXwxlk0tcDNRgnwc.png)

  </column>
</grid>




工程地理信息系统接口测试截图：
![](Attachments/X8uNbYnd4oouKQxZUqEcBWTonyg.png)

![](Attachments/ML6Zbf1CRoEtSMx5L5wcb4ecnff.png)


IMF航班接口调试截图：
<grid cols="4">
  <column width="25">
    ![](Attachments/J89qbPJs2o0yRtxXcQnc5Jyen1c.png)

  </column>
  <column width="25">
    ![](Attachments/RpEZbBN6QoS4p2x1yewcur08n1b.png)

  </column>
  <column width="25">
    ![](Attachments/RTfPb1sMiogUs3xWc53c2S7Enae.png)

  </column>
  <column width="25">
    ![](Attachments/OFMxbzr1KoZ6kqx0zCEc4buGnmb.png)

  </column>
</grid>

<grid cols="4">
  <column width="25">
    ![](Attachments/EgIxbi02HoqpIRxubhzcT2dqnid.png)

  </column>
  <column width="25">
    ![](Attachments/OXlEbGD11omw0GxfgYYc6G8qn4d.png)

  </column>
  <column width="25">
    ![](Attachments/TVYabbqgPo9pHTxzPCDcMRclnSh.png)

  </column>
  <column width="25">
    ![](Attachments/JTGVbQuNaon2FAxz6sscaWH4n3e.png)

  </column>
</grid>

![](Attachments/HAeFbjxjzosu3oxJgZSc64bQnjh.png)

![](Attachments/QpRebV135oBZwtxPj2ycNqb4nVs.png)

<grid cols="2">
  <column width="50">
    ![](Attachments/XoNTbFKqboT4JTx0WDkctYWlnca.png)

  </column>
  <column width="50">
    ![](Attachments/VX8xbamwooLxh2x15h7cjjvHn4d.png)

  </column>
</grid>

<grid cols="4">
  <column width="25">
    ![](Attachments/MsBjb6sl9onxz3x7sRNc3SfDnDh.png)

  </column>
  <column width="25">
    ![](Attachments/CjLMbivgOoktNBx0gfOcOMB7n7c.png)

  </column>
  <column width="25">
    ![](Attachments/DJbjb4lBJo1ZnBxxok6cz6eInTd.png)

  </column>
  <column width="25">
    ![](Attachments/MuAYbGOr8oQ14Ixujs9cb7jBnpf.png)

  </column>
</grid>

<grid cols="2">
  <column width="50">
    ![](Attachments/QMT8b43WEo8QiAxoqlFcBs9Jn7f.png)

  </column>
  <column width="50">
    ![](Attachments/KL7ubbdSKopnWyxZa7TczcHAnrh.png)

  </column>
</grid>


地服运行系统接口测试截图：
![](Attachments/GWHnb0WWnozDl5xBf0ncztP8nie.png)

![](Attachments/FDdkb8dq4oTxjSxuhq6cXeZWn3c.jpg)

登机桥系统接口测试截图：
<grid cols="4">
  <column width="25">
    ![](Attachments/VI8hbrqjooiNlqxgMT5cBNq3nSh.png)

  </column>
  <column width="25">
    ![](Attachments/Mkm1b6Vbnow5oRx5T4Dc1v2cnxc.png)

  </column>
  <column width="25">
    ![](Attachments/WrOybTNYQor8xNxPSCNcwgIfnyd.png)

  </column>
  <column width="25">
    ![](Attachments/Ln3EbYcp5oirxSxEgEic7tf6nZc.png)

  </column>
</grid>

服务质量执行测量系统接口测试截图（同贵宾系统、旅客体验系统接口类似，部分接口因算法问题暂时无法进行测试）：
![](Attachments/KsrebLZOsoLDzRx9GnSck1Nfn0e.png)

贵宾系统接口测试截图（部分接口因算法问题暂时无法进行测试）：
![](Attachments/AzzQbSit7oYzHbxb9gVcuI9Nnsc.png)

旅客体验系统接口测试截图（部分接口因算法问题暂时无法进行测试）：
![](Attachments/S03qbPwhVophNGxV38Xcn3VVnDd.png)

旅客安检系统接口测试截图：
<grid cols="2">
  <column width="50">
    ![](Attachments/DVr9b2BKRofzVnxPQfKcW9Ukngb.jpg)

  </column>
  <column width="50">
    ![](Attachments/TiIwbB6wooMAjKxmUDQcoeEtnZe.jpg)

  </column>
</grid>


智能数据中心接口测试截图：
![](Attachments/LinKb7TSVobVnUxieo0ccszCndf.jpg)

