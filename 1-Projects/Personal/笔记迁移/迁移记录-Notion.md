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
| [[4-Archives/Notes/Notion/技术相关/SQL 相关语句 35c696dbd3344c0887636f409c4f9ffe]] + [[4-Archives/Notes/Notion/技术相关/MySQL e1d3f11807eb43cb8809e2a5157705c6]] | [[3-Resources/Tech/代码片段/SQL常用语句]] |
| [[4-Archives/Notes/Notion/技术相关/Linux相关指令 4e807713bb61406db430d4f17e348f7c]] + [[4-Archives/Notes/Notion/技术相关/端口转发 fe88732128d84be099cd94da131e985b]] + [[4-Archives/Notes/Notion/技术相关/监听捉包转发 1a7423d5db1048da9709c3a50f2128f2]] + [[4-Archives/Notes/Notion/技术相关/挂载nfs ff1a70f70f56422ba01f673752003c59]] | [[3-Resources/Tech/代码片段/Linux运维命令]] |
| [[4-Archives/Notes/Notion/技术相关/Kubectl 相关指令 dd61c2f1d5b54afc9a1b8f9a90383153]] | [[3-Resources/Tech/代码片段/Kubectl常用命令]] |
| [[4-Archives/Notes/Notion/技术相关/Nginx配置 19d5e7a33a544564a81a0118f870fae0]] | [[3-Resources/Tech/代码片段/Nginx反向代理配置]] |
| [[4-Archives/Notes/Notion/技术相关/Git相关指令 951abbbb0258487d911931258f0cc44b]] | [[3-Resources/Tech/代码片段/Git子模块管理]] |
| [[4-Archives/Notes/Notion/技术相关/Helm Minio a4c7c9a953314c888a5123848de1cb75]] | [[3-Resources/Tech/代码片段/Helm-MinIO部署]] |

## 碎片（5 个）

---

### [[4-Archives/Notes/Notion/技术相关/brew升级 25e6aac36961418ab26325def8768293]]
已有 [[3-Resources/Tech/代码片段/macOS-Brew应用列表]]，内容重叠。
```bash
brew upgrade --cask android-studio pgadmin4 josm docker mqttx tencent-meeting elpass notion visual-studio-code google-chrome qgis wechat intellij-idea sunloginclient wechatwebdevtools iterm2 teamviewer logitech-options surge elpass microsoft-edge microsoft-word microsoft-excel microsoft-powerpoint monitorcontrol
```

---

### [[4-Archives/Notes/Notion/技术相关/导航相关 2ff7bf9617024928b122433f10af899a]]
多楼层线段组件设计思路，已有 [[3-Resources/Tech/代码片段/MultiFloorLine组件]]。

---

### [[4-Archives/Notes/Notion/技术相关/Nextcloud 5dad075ad5644594bc612e9d658855e6]]
PostgreSQL 密码截图 + 系统密码 ncadmin/secret。

---

### [[4-Archives/Notes/Notion/技术相关/Ubuntu下vi输入i不进入insert插入模式 667fc90716bf40fdbf00fbd477b12a61]]
修改 `/etc/vim/vimrc.tiny`，将 `set compatible` 改为 `set nocompatible`。

---

### [[4-Archives/Notes/Notion/技术相关/后端修改建议 bfaea1d3e6754fb083e9459d1aa62d58]]
平台 API 设计文档，已合并到 [[3-Resources/Tech/知识卡片/平台开发备忘]]。

# 莱讯科技（30+ 个）

## 整理为代码片段（3 个）

| 原始笔记 | 迁移到 |
|----------|--------|
| [[4-Archives/Notes/Notion/莱讯科技/OpenClash b7f7dcaf807c4cc98961ef0daf778e43]] | [[3-Resources/Tech/代码片段/OpenClash代理配置]] |
| [[4-Archives/Notes/Notion/莱讯科技/私有化部署方案 0e93acb330b94e91b445e17af290a002]] | [[3-Resources/Tech/代码片段/私有化部署方案]] |
| [[4-Archives/Notes/Notion/莱讯科技/集群部署相关 c41a2518af6f405cb0c5b960fa27220f]] | [[3-Resources/Tech/代码片段/K8S集群部署配置]] |

## 合并到知识卡片（5 个）

| 原始笔记 | 迁移到 |
|----------|--------|
| [[4-Archives/Notes/Notion/莱讯科技/后端修改方案 36e338987352410b8cf878e0f40ba175]] | [[3-Resources/Tech/知识卡片/平台开发备忘]] |
| [[4-Archives/Notes/Notion/莱讯科技/SAAS平台与业务对接问题 3bf37acc4516411889ac3cd7cbf7fa87]] | [[3-Resources/Tech/知识卡片/平台开发备忘]] |
| [[4-Archives/Notes/Notion/临时记录/博世&莱讯&南讯集成相关问题反馈 d5376bec6e14452e88413f7f8eabc6a6]] | [[3-Resources/Tech/知识卡片/平台开发备忘]] |
| [[4-Archives/Notes/Notion/莱讯科技/参数描述库 c3f9e58ca2c94c51a8cdbd7810811a1e]] | [[3-Resources/Tech/知识卡片/平台开发备忘]] |
| [[4-Archives/Notes/Notion/莱讯科技/兼职面试问题 eccd24997b7c4695ac2a6a127cb6b0fd]] | [[3-Resources/Tech/知识卡片/招聘与面试记录]] |

## 合并到 SQL 代码片段（3 个）

| 原始笔记 | 迁移到 |
|----------|--------|
| [[4-Archives/Notes/Notion/莱讯科技/DEVICE数据库修正 2c4e71136b4a4c84bfbf8b403d3acf6c]] | [[3-Resources/Tech/代码片段/SQL常用语句]]（设备类型初始化 SQL） |
| [[4-Archives/Notes/Notion/莱讯科技/有高度的 geom 18e16f9d35824c0b9a1dcf319eee01bc]] | [[3-Resources/Tech/代码片段/SQL常用语句]]（PostGIS 3D 几何操作） |
| [[4-Archives/Notes/Notion/莱讯科技/添加标签和基站类型 ace01d9d7f3c41cf96bfeb101b05fc7b]] | [[3-Resources/Tech/代码片段/SQL常用语句]]（设备类型初始化 SQL） |

## 归档索引（1 个）

年终总结（[[4-Archives/Notes/Notion/莱讯科技/2021年终总结 ea8e3b478120455bb0f4117175e13627]] / [[4-Archives/Notes/Notion/莱讯科技/2022年终总结 dcc3504151bf460daf44c91ba60de66b]] / [[4-Archives/Notes/Notion/莱讯科技/2023年终总结 8f2d41160620489a855213614f64b65f]]）+ [[4-Archives/Notes/Notion/莱讯科技/年终总结述职 2928d131e3d844d5b2d17c3856a226dc]] → [[4-Archives/已完结项目/莱讯科技-年终总结汇总]]

## 碎片（18+ 个）

---

### [[4-Archives/Notes/Notion/莱讯科技/项目跟踪 02eeba5e1e75455ea234bf1a8c0df08f]]
项目列表索引页：二手车、冷库、长沙机场、中核、船只、兰州机场、武汉机场、Bossard、保定轮毂厂、Omlox seminar、广州机场、振华。已有对应 [[4-Archives/已完结项目]] 归档。

---

### [[4-Archives/Notes/Notion/莱讯科技/用户权限项目开发 a1d8e55c838945cf92fb722f28cf5136]]
超级管理员/公司管理员/普通用户的权限矩阵（公司、用户、项目三个维度），已合并到 [[3-Resources/Tech/知识卡片/平台开发备忘]]。

---

### [[4-Archives/Notes/Notion/莱讯科技/定位平台前端问题 6a8f035823e94594abf155bcf74f5b8a]]
FormSelect 未打开自动加载数据、表单显示不全、摄像头和基站添加位置。

---

### [[4-Archives/Notes/Notion/莱讯科技/导航开发 6bda9ac4ba2d4210b36b891e29faf9b8]] JSON + 位置数据 JSON + 截图。

---

### [[4-Archives/Notes/Notion/莱讯科技/地图库楼层修改 6a4a0cfb9bc64449ab117ed6b3943ed3]]
楼层编号逻辑：`Math.floor(4/100) || Math.floor(4%100)`，4/400/401/410 层级判断。

---

### [[4-Archives/Notes/Notion/莱讯科技/红点电网项目遇到问题 ab724a0ea9d74fa38c0cfbd3241fd274]]
1. 红点后台密码过期，无法登录查看
2. 电脑不正常关机后红点服务可能不能自动恢复

---

### [[4-Archives/Notes/Notion/莱讯科技/补全数据库，重新迁移 6d9a2e176c004ff981e0f2b3e61355fa]]
检查 geom 字段类型、补充 deleted 字段、确认 create_schema 一致、补充基站/标签类型 SQL、重新迁移四个数据库。

---

### [[4-Archives/Notes/Notion/莱讯科技/development邮件信息 8d48d14a58ad4cd8a1601a2d2ee757be]]
SMTP: [development@reliablesense.cn](mailto:development@reliablesense.cn) / smtp.feishu.cn:465

---

### [[4-Archives/Notes/Notion/莱讯科技/Omlox 相关 d7f4d2267b494967a3d363890b81a1df]]
Deep hub 上层应用公司：Bridge IT、德国通快。

---

### [[4-Archives/Notes/Notion/莱讯科技/旧数据库地址 843cd727a07a4186b23f4852349d0931]]
Management(30993) / Device(30230) / Position(31596) / Map(32723)，均为 server.reliablesense.cn，admin/secret。

---

### [[4-Archives/Notes/Notion/莱讯科技/计算服务器硬盘容量 80418597285b495693612b374a741537]]
每天 ~13.8GB，每月 ~415GB，每年 ~5TB。

---

### [[4-Archives/Notes/Notion/莱讯科技/中间件更新 b581af464eb147a5bf9b8c1412ffd42d]]
空文件。

---

### [[4-Archives/Notes/Notion/莱讯科技/部署相关 8138f5aa03eb4a5583e0770546da7467]]
position 配了 druid 连接池导致问题，去掉后恢复。

---

### [[4-Archives/Notes/Notion/莱讯科技/年终总结述职 2928d131e3d844d5b2d17c3856a226dc]]
员工述职记录（朱婷婷、杨嵘、陈子杰、陆东、王宗光、谢海飞、邓志斌），已索引到 [[4-Archives/已完结项目/莱讯科技-年终总结汇总]]。

---

### [[4-Archives/Notes/Notion/莱讯科技/创业 融资讲座 e01b7a62cf844fe6ad4a8ad956d24ff2]]
2022-04-08 讲座截图（10 张），无文字内容。

---

### [[4-Archives/Notes/Notion/莱讯科技/员工任务分配 a331fc38f3814472a4790b838d1e303c]] / [[4-Archives/Notes/Notion/莱讯科技/2019年OKR f59d18adcc064237bd3b97dc8521d5f6]] / [[4-Archives/Notes/Notion/莱讯科技/8月16日一周任务 ba00eba4453d4ab49f2be079288a9830]] / [[4-Archives/Notes/Notion/莱讯科技/需要调整地理信息的储存坐标系 52f5c41cd52a42daa0bb681fb27e3459]]
CSV 数据，历史任务跟踪表。

# 临时记录（17 个）

## 合并到知识卡片（5 个）

| 原始笔记 | 迁移到 |
|----------|--------|
| [[4-Archives/Notes/Notion/临时记录/产品经理面试流程 ea2c1c94889641328193c8f7030dc999]] | [[3-Resources/Tech/知识卡片/招聘与面试记录]]（产品经理面试流程） |
| [[4-Archives/Notes/Notion/临时记录/如何面试一个产品经理 3a9d7bf553284f74986d6693253024ce]] | [[3-Resources/Tech/知识卡片/招聘与面试记录]]（产品经理面试考察要点） |
| [[4-Archives/Notes/Notion/临时记录/面试 d37d84ae400b48ea9059409df77c51d6]] | [[3-Resources/Tech/知识卡片/招聘与面试记录]]（前端面试问题） |
| [[4-Archives/Notes/Notion/临时记录/实施工程师 b3ac91f290dd40448cb5c299ad3b1b86]] | [[3-Resources/Tech/知识卡片/招聘与面试记录]]（实施工程师面试考察） |
| [[4-Archives/Notes/Notion/临时记录/博世&莱讯&南讯集成相关问题反馈 d5376bec6e14452e88413f7f8eabc6a6]] | [[3-Resources/Tech/知识卡片/平台开发备忘]]（API 鉴权与集成对接） |

## 合并到广州机场项目（1 个）

| 原始笔记 | 迁移到 |
|----------|--------|
| [[4-Archives/Notes/Notion/临时记录/广州机场机场项目/硬件部分深化设计交底会 e7d130fda7cb4ff8b358f8eec88799b0]] | [[1-Projects/Work/广州机场/进度记录]]（硬件交底会记录） |

## 碎片（11 个）

---

### [[4-Archives/Notes/Notion/临时记录/购物清单 baccfb9923044b43901d43e596696b9a]]
家庭购物清单，部分已购：摄像头 ✅、空气炸锅 ✅、小米音箱 ✅、花洒 ✅、药箱 ✅。待购：路由器、净水机、PS5、switch游戏、airpod pro2、ipad 10、4k屏幕等。

---

### [[4-Archives/Notes/Notion/临时记录/出行清单 c72169ed38ff4c7da5db9890a06b3f09]]
空文件。

---

### [[4-Archives/Notes/Notion/临时记录/七叔连新路相关 2aebe442322e45f8bc7feaf6e78fe162]]
家庭事务相关联系信息：[name] 身份证后六位 [id_suffix]，[name] 身份证后六位 [id_suffix]，手机 [phone]，地址：广东省广州市越秀区。

---

### [[4-Archives/Notes/Notion/临时记录/map-mobile 问题 56712502c2d144878b55cce302bb269a]]
移动端地图 bug 列表（13 项），含 3D/2D 切换、楼层切换、指北针、导航路线等问题。已修复 8 项，2 项无法修改，含测试 URL。

---

### [[4-Archives/Notes/Notion/临时记录/报价工时 461fd45c8a9b457194dbafebe2bac6ac]]
功能报价工时表：室内室外三维地图操作 4人/天、地图定位对象显示 4人/天、定位对象列表 2人/天、地图弹窗 4人/天、轨迹显示 4人/天、接口要求 1人/天。

---

### [[4-Archives/Notes/Notion/临时记录/维护工作 1a97400866b54ddca9552e6fba17fe6c]]
维护项目列表：二手车、来邦、南方电网、麦钉（三个厂）、moko。

---

### [[4-Archives/Notes/Notion/临时记录/添加showMixEnviorment feb3f4abd81a4075bfe19f22ba79b94e]]
前端组件 showMixEnvironment 参数添加清单：GeojsonEditor ☐、Cluster ✅、BitmapEditor ☐、Selection ☐、History ✅、MultiFloorLine ✅。

---

### [[4-Archives/Notes/Notion/临时记录/Bosch 8cc08cefa49d4084ba90cc662c330907]]
博世项目备忘：安全策略、小程序使用。

---

### [[4-Archives/Notes/Notion/临时记录/Bossard 61ab15e18d31411ea2e38c3e2cdec42d]]
Bossard 项目沟通记录：分组功能疑问、POC/MVP 流程、购物车逻辑、数量标签、Android ID 变更问题（测试 ID: 8fab191d98a39550, 111f6297328fb754）。

---

### [[4-Archives/Notes/Notion/临时记录/Deephub fece724e073541cf908f1309ad410be5]]
Deephub 集成步骤：location provider、fence、trackable 配置，导入办公室地图后可查看。

---

### [[4-Archives/Notes/Notion/临时记录/iris 5cd2664a1987409a9907765aabe771b9]]
空文件。

# 生活相关（9 个）

## 已迁移到 PARA 文档（2 个）

| 原始笔记 | 迁移到 |
|----------|--------|
| [[4-Archives/Notes/Notion/生活相关/加拿大相关 d53cbb8988d34b8ab4b36ac51009e6b2]] | [[2-Areas/Life/加拿大信息]] |
| [[4-Archives/Notes/Notion/生活相关/中国购房 30e81c4cdef54bb2838ac7e97a02c4a3]] | [[2-Areas/Life/购房记录]] |

## 碎片（7 个）

---

### [[4-Archives/Notes/Notion/生活相关/育儿相关 f6e1cb22394949b8af1a4a00614ec888]]
CSV 数据，含口吃问题、营养不足问题、寻麻疹相关、产后准备、产前准备等卡片，大部分为空白卡片标题。

---

### [[4-Archives/Notes/Notion/生活相关/家庭关系 10f70d826899424d94e08041db39a906]]
两个子页面：
- 主要矛盾分析：带小孩价值观不一致（玩具、外出游玩、安全方面）、日常生活消费价值观不一致（买菜煮饭）、日常生活习惯不一致。
- 如何分析处理：分析出主要矛盾 → 分别处理主要矛盾（未完成）。

---

### [[4-Archives/Notes/Notion/生活相关/养鱼相关 4801e27807854a8cbd0163006367f56b]]
两个参考链接：水草缸开缸全攻略（网易）、水草缸用自来水养草分析（人人焦点）。

---

### [[4-Archives/Notes/Notion/生活相关/家庭任务分配 b41188e0b19d438d9bb29ea44a8718fa]]
CSV 数据，4 条任务：与 [name] 沟通、购买沙发、房屋合同（LB）、选择幼儿园（Hong），均未开始。

---

### [[4-Archives/Notes/Notion/生活相关/幼儿园 05e6f2b9a79e46fe989538fa338dc800]]
CSV 数据，广州市海珠区幼儿园调研：民办 4 所（石溪、乐森、探星、信孚星云）、公立 4 所（少年宫海富花园、雅致花园、穗花翠城、保利红棉）。

---

### [[4-Archives/Notes/Notion/生活相关/购房计划 963d780c584446b88d307c909a78fd96]]
CSV 数据，购房方案对比：茂林园 7 楼（市值 280W）、茂林园 4 楼（月租 2650）、市场价方案（首付 84w/月供 10402/30 年）、理想价方案（首付 50w/月供 9548/30 年）、家庭帮助方案（首付 100w/月供 9089/20 年），已合并核心数据到 [[2-Areas/Life/购房记录]]。

---

### [[4-Archives/Notes/Notion/生活相关/限制消费 33615e9f45834285b908bfb888133471]]
CSV 数据，家庭财务管理协定：统一管理水电费/网费/银行卡/支付宝/微信，约束条件（不去高消费场所、不随意打车点外卖、非必须消费报备），福利（生活费、培训费、健身费赞助），有效期至稳定工作且还清 50% 债务。

# 学习相关（1 个）

## 碎片（1 个）

---

### [[4-Archives/Notes/Notion/学习相关 1a8ea76cd2684885bb19f7173cc764a6]]
2018 年 CSV 数据，3 条学习任务（Speaking、Reading、Listen and Write），均已完成，无实质内容。

# 看书（1 个）

## 碎片（1 个）

---

### [[4-Archives/Notes/Notion/看书 f202a4d970ec42b8bc5ca28ba6ccf460]]
两本待读书目：
- The Art of Doing Science and Engineering
- 万物根源