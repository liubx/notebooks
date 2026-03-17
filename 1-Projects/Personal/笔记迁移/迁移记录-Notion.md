---
title: 迁移记录-Notion
type: note
tags:
  - project/笔记迁移
created: 2026-03-16
modified: 2026-03-16
---

# 总览

- 来源：Notion 导出（6 个分类，80+ 个笔记）
- 原始文件保留在：`4-Archives/Notes/Notion/`
- 整理为代码片段：10 个
- 合并到知识卡片：2 个（招聘与面试记录、平台开发备忘）
- 合并到生活文档：2 个（加拿大信息、购房记录）
- 整理为归档索引：1 个（莱讯科技汇总）
- 合并到广州机场进度记录：1 个
- 碎片及无独立价值笔记（记录在本文件）：其余

# 技术相关（15 个）

## 整理为代码片段（10 个）

| 原始笔记 | 迁移到 |
|----------|--------|
| [[4-Archives/Notes/Notion/技术相关/SQL 相关语句]] + [[4-Archives/Notes/Notion/技术相关/MySQL]] | [[3-Resources/Tech/代码片段/SQL常用语句]] |
| [[4-Archives/Notes/Notion/技术相关/Linux相关指令]] + [[4-Archives/Notes/Notion/技术相关/端口转发]] + [[4-Archives/Notes/Notion/技术相关/监听捉包转发]] + [[4-Archives/Notes/Notion/技术相关/挂载nfs]] | [[3-Resources/Tech/代码片段/Linux运维命令]] |
| [[4-Archives/Notes/Notion/技术相关/Kubectl 相关指令]] | [[3-Resources/Tech/代码片段/Kubectl常用命令]] |
| [[4-Archives/Notes/Notion/技术相关/Nginx配置]] | [[3-Resources/Tech/代码片段/Nginx反向代理配置]] |
| [[4-Archives/Notes/Notion/技术相关/Git相关指令]] | [[3-Resources/Tech/代码片段/Git子模块管理]] |
| [[4-Archives/Notes/Notion/技术相关/Helm Minio]] | [[3-Resources/Tech/代码片段/Helm-MinIO部署]] |

## 碎片（5 个）

---

### [[4-Archives/Notes/Notion/技术相关/brew升级]]
已有 [[3-Resources/Tech/代码片段/macOS-Brew应用列表]]，内容重叠。
```bash
brew upgrade --cask android-studio pgadmin4 josm docker mqttx tencent-meeting elpass notion visual-studio-code google-chrome qgis wechat intellij-idea sunloginclient wechatwebdevtools iterm2 teamviewer logitech-options surge elpass microsoft-edge microsoft-word microsoft-excel microsoft-powerpoint monitorcontrol
```

---

### [[4-Archives/Notes/Notion/技术相关/导航相关]]
多楼层线段组件设计思路，已有 [[3-Resources/Tech/代码片段/MultiFloorLine组件]]。

---

### [[4-Archives/Notes/Notion/技术相关/Nextcloud]]
PostgreSQL 密码截图 + 系统密码 ncadmin/secret。

---

### [[4-Archives/Notes/Notion/技术相关/Ubuntu下vi输入i不进入insert插入模式]]
修改 `/etc/vim/vimrc.tiny`，将 `set compatible` 改为 `set nocompatible`。

---

### [[4-Archives/Notes/Notion/技术相关/后端修改建议]]
平台 API 设计文档，已合并到 [[3-Resources/Tech/知识卡片/平台开发备忘]]。

# 莱讯科技（30+ 个）

## 整理为代码片段（3 个）

| 原始笔记 | 迁移到 |
|----------|--------|
| [[4-Archives/Notes/Notion/莱讯科技/OpenClash]] | [[3-Resources/Tech/代码片段/OpenClash代理配置]] |
| [[4-Archives/Notes/Notion/莱讯科技/私有化部署方案]] | [[3-Resources/Tech/代码片段/私有化部署方案]] |
| [[4-Archives/Notes/Notion/莱讯科技/集群部署相关]] | [[3-Resources/Tech/代码片段/K8S集群部署配置]] |

## 合并到知识卡片（5 个）

| 原始笔记 | 迁移到 |
|----------|--------|
| [[4-Archives/Notes/Notion/莱讯科技/后端修改方案]] | [[3-Resources/Tech/知识卡片/平台开发备忘]] |
| [[4-Archives/Notes/Notion/莱讯科技/SAAS平台与业务对接问题]] | [[3-Resources/Tech/知识卡片/平台开发备忘]] |
| [[4-Archives/Notes/Notion/临时记录/博世&莱讯&南讯集成相关问题反馈]] | [[3-Resources/Tech/知识卡片/平台开发备忘]] |
| [[4-Archives/Notes/Notion/莱讯科技/参数描述库]] | [[3-Resources/Tech/知识卡片/平台开发备忘]] |
| [[4-Archives/Notes/Notion/莱讯科技/兼职面试问题]] | [[3-Resources/Tech/知识卡片/招聘与面试记录]] |

## 合并到 SQL 代码片段（3 个）

| 原始笔记 | 迁移到 |
|----------|--------|
| [[4-Archives/Notes/Notion/莱讯科技/DEVICE数据库修正]] | [[3-Resources/Tech/代码片段/SQL常用语句]]（设备类型初始化 SQL） |
| [[4-Archives/Notes/Notion/莱讯科技/有高度的 geom]] | [[3-Resources/Tech/代码片段/SQL常用语句]]（PostGIS 3D 几何操作） |
| [[4-Archives/Notes/Notion/莱讯科技/添加标签和基站类型]] | [[3-Resources/Tech/代码片段/SQL常用语句]]（设备类型初始化 SQL） |

## 归档索引（1 个）

年终总结（[[4-Archives/Notes/Notion/莱讯科技/2021年终总结]] / [[4-Archives/Notes/Notion/莱讯科技/2022年终总结]] / [[4-Archives/Notes/Notion/莱讯科技/2023年终总结]]）+ [[4-Archives/Notes/Notion/莱讯科技/年终总结述职]] → [[4-Archives/已完结项目/莱讯科技-年终总结汇总]]

## 碎片（18+ 个）

---

### [[4-Archives/Notes/Notion/莱讯科技/项目跟踪]]
项目列表索引页：二手车、冷库、长沙机场、中核、船只、兰州机场、武汉机场、Bossard、保定轮毂厂、Omlox seminar、广州机场、振华。已有对应 [[4-Archives/已完结项目]] 归档。

---

### [[4-Archives/Notes/Notion/莱讯科技/用户权限项目开发]]
超级管理员/公司管理员/普通用户的权限矩阵（公司、用户、项目三个维度），已合并到 [[3-Resources/Tech/知识卡片/平台开发备忘]]。

---

### [[4-Archives/Notes/Notion/莱讯科技/定位平台前端问题]]
FormSelect 未打开自动加载数据、表单显示不全、摄像头和基站添加位置。

---

### [[4-Archives/Notes/Notion/莱讯科技/导航开发]] JSON + 位置数据 JSON + 截图。

---

### [[4-Archives/Notes/Notion/莱讯科技/地图库楼层修改]]
楼层编号逻辑：`Math.floor(4/100) || Math.floor(4%100)`，4/400/401/410 层级判断。

---

### [[4-Archives/Notes/Notion/莱讯科技/红点电网项目遇到问题]]
1. 红点后台密码过期，无法登录查看
2. 电脑不正常关机后红点服务可能不能自动恢复

---

### [[4-Archives/Notes/Notion/莱讯科技/补全数据库，重新迁移]]
检查 geom 字段类型、补充 deleted 字段、确认 create_schema 一致、补充基站/标签类型 SQL、重新迁移四个数据库。

---

### [[4-Archives/Notes/Notion/莱讯科技/development邮件信息]]
SMTP: [development@reliablesense.cn](mailto:development@reliablesense.cn) / smtp.feishu.cn:465

---

### [[4-Archives/Notes/Notion/莱讯科技/Omlox 相关]]
Deep hub 上层应用公司：Bridge IT、德国通快。

---

### [[4-Archives/Notes/Notion/莱讯科技/旧数据库地址]]
Management(30993) / Device(30230) / Position(31596) / Map(32723)，均为 server.reliablesense.cn，admin/secret。

---

### [[4-Archives/Notes/Notion/莱讯科技/计算服务器硬盘容量]]
每天 ~13.8GB，每月 ~415GB，每年 ~5TB。

---

### [[4-Archives/Notes/Notion/莱讯科技/部署相关]]
position 配了 druid 连接池导致问题，去掉后恢复。

---

### [[4-Archives/Notes/Notion/莱讯科技/年终总结述职]]
员工述职记录（朱婷婷、杨嵘、陈子杰、陆东、王宗光、谢海飞、邓志斌），已索引到 [[4-Archives/已完结项目/莱讯科技-年终总结汇总]]。

---

### [[4-Archives/Notes/Notion/莱讯科技/创业 融资讲座]]
2022-04-08 讲座截图（10 张），无文字内容。

---

### [[4-Archives/Notes/Notion/莱讯科技/员工任务分配]] / [[4-Archives/Notes/Notion/莱讯科技/2019年OKR]] / [[4-Archives/Notes/Notion/莱讯科技/8月16日一周任务]] / [[4-Archives/Notes/Notion/莱讯科技/需要调整地理信息的储存坐标系]]
CSV 数据，历史任务跟踪表。

# 临时记录（17 个）

## 合并到知识卡片（5 个）

| 原始笔记 | 迁移到 |
|----------|--------|
| [[4-Archives/Notes/Notion/临时记录/产品经理面试流程]] | [[3-Resources/Tech/知识卡片/招聘与面试记录]]（产品经理面试流程） |
| [[4-Archives/Notes/Notion/临时记录/如何面试一个产品经理]] | [[3-Resources/Tech/知识卡片/招聘与面试记录]]（产品经理面试考察要点） |
| [[4-Archives/Notes/Notion/临时记录/面试]] | [[3-Resources/Tech/知识卡片/招聘与面试记录]]（前端面试问题） |
| [[4-Archives/Notes/Notion/临时记录/实施工程师]] | [[3-Resources/Tech/知识卡片/招聘与面试记录]]（实施工程师面试考察） |
| [[4-Archives/Notes/Notion/临时记录/博世&莱讯&南讯集成相关问题反馈]] | [[3-Resources/Tech/知识卡片/平台开发备忘]]（API 鉴权与集成对接） |

## 合并到广州机场项目（1 个）

| 原始笔记 | 迁移到 |
|----------|--------|
| [[4-Archives/Notes/Notion/临时记录/广州机场机场项目/硬件部分深化设计交底会]] | [[1-Projects/Work/广州机场/进度记录]]（硬件交底会记录） |

## 碎片（11 个）

---

### [[4-Archives/Notes/Notion/临时记录/购物清单]]
家庭购物清单，部分已购：摄像头 ✅、空气炸锅 ✅、小米音箱 ✅、花洒 ✅、药箱 ✅。待购：路由器、净水机、PS5、switch游戏、airpod pro2、ipad 10、4k屏幕等。

---

### [[4-Archives/Notes/Notion/临时记录/七叔连新路相关]]
家庭事务相关联系信息：[name] 身份证后六位 [id_suffix]，[name] 身份证后六位 [id_suffix]，手机 [phone]，地址：广东省广州市越秀区。

---

### [[4-Archives/Notes/Notion/临时记录/map-mobile 问题]]
移动端地图 bug 列表（13 项），含 3D/2D 切换、楼层切换、指北针、导航路线等问题。已修复 8 项，2 项无法修改，含测试 URL。

---

### [[4-Archives/Notes/Notion/临时记录/报价工时]]
功能报价工时表：室内室外三维地图操作 4人/天、地图定位对象显示 4人/天、定位对象列表 2人/天、地图弹窗 4人/天、轨迹显示 4人/天、接口要求 1人/天。

---

### [[4-Archives/Notes/Notion/临时记录/维护工作]]
维护项目列表：二手车、来邦、南方电网、麦钉（三个厂）、moko。

---

### [[4-Archives/Notes/Notion/临时记录/添加showMixEnviorment]]
前端组件 showMixEnvironment 参数添加清单：GeojsonEditor ☐、Cluster ✅、BitmapEditor ☐、Selection ☐、History ✅、MultiFloorLine ✅。

---

### [[4-Archives/Notes/Notion/临时记录/Bosch]]
博世项目备忘：安全策略、小程序使用。

---

### [[4-Archives/Notes/Notion/临时记录/Bossard]]
Bossard 项目沟通记录：分组功能疑问、POC/MVP 流程、购物车逻辑、数量标签、Android ID 变更问题（测试 ID: 8fab191d98a39550, 111f6297328fb754）。

---

### [[4-Archives/Notes/Notion/临时记录/Deephub]]
Deephub 集成步骤：location provider、fence、trackable 配置，导入办公室地图后可查看。

---

### [[4-Archives/Notes/Notion/临时记录/iris]]
空文件。

# 生活相关（9 个）

## 已迁移到 PARA 文档（2 个）

| 原始笔记 | 迁移到 |
|----------|--------|
| [[4-Archives/Notes/Notion/生活相关/加拿大相关]] | [[2-Areas/Life/加拿大信息]] |
| [[4-Archives/Notes/Notion/生活相关/中国购房]] | [[2-Areas/Life/购房记录]] |

## 碎片（7 个）

---

### [[4-Archives/Notes/Notion/生活相关/育儿相关]]
CSV 数据，含口吃问题、营养不足问题、寻麻疹相关、产后准备、产前准备等卡片，大部分为空白卡片标题。

---

### [[4-Archives/Notes/Notion/生活相关/家庭关系]]
两个子页面：
- 主要矛盾分析：带小孩价值观不一致（玩具、外出游玩、安全方面）、日常生活消费价值观不一致（买菜煮饭）、日常生活习惯不一致。
- 如何分析处理：分析出主要矛盾 → 分别处理主要矛盾（未完成）。

---

### [[4-Archives/Notes/Notion/生活相关/养鱼相关]]
两个参考链接：水草缸开缸全攻略（网易）、水草缸用自来水养草分析（人人焦点）。

---

### [[4-Archives/Notes/Notion/生活相关/家庭任务分配]]
CSV 数据，4 条任务：与 [name] 沟通、购买沙发、房屋合同（LB）、选择幼儿园（Hong），均未开始。

---

### [[4-Archives/Notes/Notion/生活相关/幼儿园]]
CSV 数据，广州市海珠区幼儿园调研：民办 4 所（石溪、乐森、探星、信孚星云）、公立 4 所（少年宫海富花园、雅致花园、穗花翠城、保利红棉）。

---

### [[4-Archives/Notes/Notion/生活相关/购房计划]]
CSV 数据，购房方案对比：茂林园 7 楼（市值 280W）、茂林园 4 楼（月租 2650）、市场价方案（首付 84w/月供 10402/30 年）、理想价方案（首付 50w/月供 9548/30 年）、家庭帮助方案（首付 100w/月供 9089/20 年），已合并核心数据到 [[2-Areas/Life/购房记录]]。

---

### [[4-Archives/Notes/Notion/生活相关/限制消费]]
CSV 数据，家庭财务管理协定：统一管理水电费/网费/银行卡/支付宝/微信，约束条件（不去高消费场所、不随意打车点外卖、非必须消费报备），福利（生活费、培训费、健身费赞助），有效期至稳定工作且还清 50% 债务。

# 学习相关（1 个）

## 碎片（1 个）

---

### [[4-Archives/Notes/Notion/学习相关]]
2018 年 CSV 数据，3 条学习任务（Speaking、Reading、Listen and Write），均已完成，无实质内容。

# 看书（1 个）

## 碎片（1 个）

---

### [[4-Archives/Notes/Notion/看书]]
两本待读书目：
- The Art of Doing Science and Engineering
- 万物根源