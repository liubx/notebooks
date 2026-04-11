---
title: 阶段二-飞书归档提取到PARA迁移方案
type: design-doc
tags:
  - project/笔记迁移
created: 2026-04-11
---

# 阶段二：飞书归档提取到 PARA 迁移方案

基于 `4-Archives/Notes/Feishu/` 中已拉取的全量内容，逐文件审查后制定的迁移策略。

## 迁移原则

1. 只提取有持续参考价值的内容到 PARA，一次性/过时的留归档
2. 会议纪要、智能纪要、近期会议速递、月度纪要小结 → 全部留归档不动
3. 年终总结、工作周报 → 留归档不动
4. 同一文档有多个副本的，只提取最新/最完整版本
5. file 类型附件（上传的 .docx/.xlsx/.pptx/.pdf 等）→ 留归档不动
6. README.md 索引文件、链接索引.md → 留归档不动
7. bitable 导出的 .xlsx → 留归档不动
8. 进行中项目的资料提取到 `1-Projects/Work/对应项目/`
9. 已结束项目整体归档到 `4-Archives/Projects/Work/`

---

## 一、云空间/根目录（散落文件）

| 文件 | 本地路径 | 飞书链接 | 决策 | 目标路径 | 理由 |
|------|---------|---------|------|---------|------|
| API.md | [[4-Archives/Notes/Feishu/云空间/根目录/API]] | [飞书](https://reliablesense.feishu.cn/docx/NoXpdv9A1oSb4gxwWDmciKajnOJ) | → 提取 | `1-Projects/Work/上港仓储管理/WMS-API接口文档.md` | 上港项目的 WMS 对接接口，跟项目走 |
| 墨水屏数据协议.md | [[4-Archives/Notes/Feishu/云空间/根目录/墨水屏数据协议]] | [飞书](https://reliablesense.feishu.cn/docx/P4z0dkpVUoq3jwxUvBtcrRpundd) | → 提取 | `2-Areas/Work/设备管理/墨水屏数据协议.md` | 设备协议文档，归设备管理 |
| 系统架构图.md | [[4-Archives/Notes/Feishu/云空间/根目录/系统架构图]] | [飞书](https://reliablesense.feishu.cn/docx/IYLtdtwDQoaOetxP9Xkc66jfnPf) | → 提取 | `2-Areas/Work/产品研发/综合定位系统架构图.md` | 产品架构文档，归产品研发 |
| 系统整改配置表.md | [[4-Archives/Notes/Feishu/云空间/根目录/系统整改配置表]] | [飞书](https://reliablesense.feishu.cn/docx/ZpsNdChggodbeaxLg78cgtRBnGc) | → 提取 | `1-Projects/Work/广州机场/系统整改配置表.md` | 含 A域/B域、巡检app，属广州机场项目 |
| deploy.yaml | [[4-Archives/Notes/Feishu/云空间/根目录/deploy.yaml]] | - | 留归档 | - | 单个配置文件，无上下文 |
| Doc2.docx | [[4-Archives/Notes/Feishu/云空间/根目录/Doc2.docx]] | - | 留归档 | - | 上传附件 |
| 优化后.txt | [[4-Archives/Notes/Feishu/云空间/根目录/优化后.txt]] | - | 留归档 | - | 无上下文的临时文件 |
| map-mobile.mm | [[4-Archives/Notes/Feishu/云空间/根目录/map-mobile.mm]] | - | 留归档 | - | 思维导图 |
| map-model.mm | [[4-Archives/Notes/Feishu/云空间/根目录/map-model.mm]] | - | 留归档 | - | 思维导图 |
| rssi数据.docx | [[4-Archives/Notes/Feishu/云空间/根目录/rssi数据.docx]] | - | 留归档 | - | 上传附件 |
| SaaS平台操作手册V7.docx | [[4-Archives/Notes/Feishu/云空间/根目录/SaaS平台操作手册V7.docx]] | - | 留归档 | - | 上传附件 |
| 快速启用，属于你的任务管理系统.md | [[4-Archives/Notes/Feishu/云空间/根目录/快速启用，属于你的任务管理系统]] | - | 留归档 | - | 飞书模板文档 |
| 研发部的视频会议 2024年11月22日.md | [[4-Archives/Notes/Feishu/云空间/根目录/研发部的视频会议 2024年11月22日]] | - | 留归档 | - | 会议纪要 |
| 移动应用 - 监控 2025年5月13日.md | [[4-Archives/Notes/Feishu/云空间/根目录/移动应用 - 监控 2025年5月13日]] | - | 留归档 | - | 临时监控记录 |
| 翻译.docx | [[4-Archives/Notes/Feishu/云空间/根目录/翻译.docx]] | - | 留归档 | - | 上传附件 |
| 认证文件.zip | [[4-Archives/Notes/Feishu/云空间/根目录/认证文件.zip]] | - | 留归档 | - | 压缩包 |
| 综合定位系统-深化设计方案.docx | [[4-Archives/Notes/Feishu/云空间/根目录/综合定位系统-深化设计方案.docx]] | - | 留归档 | - | 上传附件 |
| 所有 .xlsx/.xls 表格文件（约 10 个） | 见下方列表 | - | 留归档 | - | 无 feishu_url（非文档类型） |

> 根目录表格文件：[[4-Archives/Notes/Feishu/云空间/根目录/14号夜班差异分析.xlsx]]、[[4-Archives/Notes/Feishu/云空间/根目录/MAC-Address.xlsx]]、[[4-Archives/Notes/Feishu/云空间/根目录/员工花名册-在职.xlsx]]、[[4-Archives/Notes/Feishu/云空间/根目录/周报测试.xlsx]]、[[4-Archives/Notes/Feishu/云空间/根目录/定位对象在线时长导出表.xlsx]]、[[4-Archives/Notes/Feishu/云空间/根目录/广州市公办小学招生报名系统入学申请表.xls]]、[[4-Archives/Notes/Feishu/云空间/根目录/广州机场综合定位.xlsx]]、[[4-Archives/Notes/Feishu/云空间/根目录/数字化.xlsx]]、[[4-Archives/Notes/Feishu/云空间/根目录/红柳林筛分楼部署内容.xlsx]]、[[4-Archives/Notes/Feishu/云空间/根目录/综合定位系统功能清单.xlsx]]
| 广州白云国际机场三期扩建项目-综合定位-接口规范-V1.0.2.docx | [[4-Archives/Notes/Feishu/云空间/根目录/广州白云国际机场三期扩建项目-综合定位-接口规范-V1.0.2.docx]] | - | 留归档 | - | 上传附件，南宁机场项目已有对应文档 |
| 智慧仓储物流早会汇报v1.5.pptx | [[4-Archives/Notes/Feishu/云空间/根目录/智慧仓储物流早会汇报v1.5.pptx]] | - | 留归档 | - | PPT 附件 |

> **归类规则补充**：
> - 项目相关的接口/技术文档 → 跟对应项目走（`1-Projects/Work/` 或 `4-Archives/Projects/Work/`），不放通用 Tech 目录
> - 设备协议类文档 → `2-Areas/Work/设备管理/`
> - 产品架构文档（系统架构图、概要设计等描述产品整体的） → `2-Areas/Work/产品研发/`
> - 含"综合定位"、"A域/B域"、"巡检app"等广州机场特征关键词的文档 → `1-Projects/Work/广州机场/`

---

## 二、云空间/散落的会议纪要和飞书 AI 生成内容

约 150+ 个文件，**全部留归档不动**。包括 Video meeting、视频会议纪要、文字记录、智能纪要、近期会议速递、月度纪要小结等。

---

## 三、同事个人文档

### 何宜峰的个人文档
**全部留归档**。

### 王宗光的个人文档

| 文件 | 本地路径 | 飞书链接 | 决策 | 目标路径 |
|------|---------|---------|------|---------|
| LBS系统梳理.md | [[4-Archives/Notes/Feishu/云空间/王宗光的个人文档/后端架构/LBS系统梳理]] | [飞书](https://reliablesense.feishu.cn/docx/B6SgdFSRaoPqd7xQoTOcZGMAncd) | → 提取 | `3-Resources/Tech/设计方案/LBS系统梳理.md` |
| RS-LBS后端平台架构重构方案(v2.0.0).md | [[4-Archives/Notes/Feishu/云空间/王宗光的个人文档/后端架构/RS-LBS后端平台架构重构方案(v2.0.0)]] | [飞书](https://reliablesense.feishu.cn/docx/WctjdFkvSoAIJ8x3t1scyrXVnXc) | → 提取 | `3-Resources/Tech/设计方案/RS-LBS后端平台架构重构方案.md` |
| RS-MID中间件平台架构方案(v1.0.0).md | [[4-Archives/Notes/Feishu/云空间/王宗光的个人文档/后端架构/RS-MID中间件平台架构方案(v1.0.0)]] | [飞书](https://reliablesense.feishu.cn/docx/PYwpd0PL3owk84xKLsNcQCy8nmh) | → 提取 | `3-Resources/Tech/设计方案/RS-MID中间件平台架构方案.md` |
| Zone + tile38功能实现备忘.md | [[4-Archives/Notes/Feishu/云空间/王宗光的个人文档/平台功能迭代/Zone + tile38功能实现备忘]] | [飞书](https://reliablesense.feishu.cn/docx/QI0SdzgAsol9SKxEh2wcWOkJnZc) | → 提取 | `3-Resources/Tech/知识卡片/Zone-tile38功能实现备忘.md` |
| 广州机场App登录验证码.md | [[4-Archives/Notes/Feishu/云空间/王宗光的个人文档/项目资料/广州机场App登录验证码]] | [飞书](https://reliablesense.feishu.cn/docx/ZxChdrcWCofAbxxzQEIcRopQnPg) | → 提取 | `1-Projects/Work/广州机场/App登录验证码.md` |
| 会议纪要/ | [[4-Archives/Notes/Feishu/云空间/王宗光的个人文档/会议纪要/]] | - | 留归档 | - | 会议纪要 |
| 工作总结/（3个年度总结） | [[4-Archives/Notes/Feishu/云空间/王宗光的个人文档/工作总结/]] | - | 留归档 | - | 年终总结 |
| 定制化项目/（新太、洛阳化工） | [[4-Archives/Notes/Feishu/云空间/王宗光的个人文档/定制化项目/]] | - | 留归档 | - | 已结束项目零散记录 |
| 测试/（压测、路网C++） | [[4-Archives/Notes/Feishu/云空间/王宗光的个人文档/测试/]] | - | 留归档 | - | 测试数据 |
| 问题处理记录/工作记录.md | [[4-Archives/Notes/Feishu/云空间/王宗光的个人文档/问题处理记录/工作记录]] | - | 留归档 | - | 零散工作记录 |
| 项目资料/博实结、嘉盛、洛阳化工、赛力斯 | [[4-Archives/Notes/Feishu/云空间/王宗光的个人文档/项目资料/]] | - | 留归档 | - | 已结束项目资料 |
| 项目资料/RTK报文分析.log | [[4-Archives/Notes/Feishu/云空间/王宗光的个人文档/项目资料/RTK报文分析.log]] | - | 留归档 | - | 日志文件 |
| 用户敏感信息处理.md | [[4-Archives/Notes/Feishu/云空间/王宗光的个人文档/用户敏感信息处理]] | - | 留归档 | - | 通用但内容较少 |
| 🚩会议签到表.xlsx | [[4-Archives/Notes/Feishu/云空间/王宗光的个人文档/🚩会议签到表.xlsx]] | - | 留归档 | - | 表格 |
| 工作周报.xlsx / 王宗光24年周报.xlsx | [[4-Archives/Notes/Feishu/云空间/王宗光的个人文档/工作周报.xlsx]] / [[4-Archives/Notes/Feishu/云空间/王宗光的个人文档/王宗光24年周报.xlsx]] | - | 留归档 | - | 周报表格 |
| 远端接口新需求问题反馈-20230323.xlsx | [[4-Archives/Notes/Feishu/云空间/王宗光的个人文档/远端接口新需求问题反馈-20230323.xlsx]] | - | 留归档 | - | 表格 |
| 所有会议纪要/智能纪要/近期会议速递（约 30 个） | [[4-Archives/Notes/Feishu/云空间/王宗光的个人文档/]] 下各 .md 文件 | - | 留归档 | - | 飞书 AI 生成内容 |

### 陈子杰/孙永霖的个人文档
**全部留归档**。

---

## 四、莱讯科技/项目运维管理

### 4a. 运维文档

| 文件 | 本地路径 | 飞书链接 | 决策 | 目标路径 |
|------|---------|---------|------|---------|
| 前端运维手册.md | [[4-Archives/Notes/Feishu/云空间/莱讯科技/项目运维管理/运维文档/前端运维手册]] | [飞书](https://reliablesense.feishu.cn/docx/CT42dawUcoGhYLx2UIjcjVuTnYf) | → 提取 | `3-Resources/Tech/代码片段/前端运维手册.md` |
| 后端运维手册.md | [[4-Archives/Notes/Feishu/云空间/莱讯科技/项目运维管理/运维文档/后端运维手册]] | [飞书](https://reliablesense.feishu.cn/docx/OGLIdpLsJoaVecxBWuZcD41xnEf) | → 提取 | `3-Resources/Tech/代码片段/后端运维手册.md` |
| 新太运维手册.md | [[4-Archives/Notes/Feishu/云空间/莱讯科技/项目运维管理/运维文档/新太运维手册]] | [飞书](https://reliablesense.feishu.cn/docx/NFOVdlWSFoZJ91xTXMbcvY7mnSg) | → 提取 | `3-Resources/Tech/代码片段/新太运维手册.md` |
| 区域功能后端开发文档.md | [[4-Archives/Notes/Feishu/云空间/莱讯科技/项目运维管理/运维文档/区域功能后端开发文档]] | [飞书](https://reliablesense.feishu.cn/docx/JknBdu9hEon9gJxuC4ycEBhOnjb) | → 提取 | `3-Resources/Tech/知识卡片/区域功能后端开发文档.md` |
| 数据库操作说明.md | [[4-Archives/Notes/Feishu/云空间/莱讯科技/项目运维管理/运维文档/数据库操作说明]] | [飞书](https://reliablesense.feishu.cn/docx/KjS8dWiAvoxdCIxgkEEcDktinSU) | → 提取 | `3-Resources/Tech/代码片段/数据库操作说明.md` |
| 数据库 pg-backup 使用方法说明.md | [[4-Archives/Notes/Feishu/云空间/莱讯科技/项目运维管理/运维文档/数据库 pg-backup 使用方法说明]] | [飞书](https://reliablesense.feishu.cn/docx/LfEodRSmnoOopsxju9kckxCtnng) | → 提取 | `3-Resources/Tech/代码片段/pg-backup使用方法.md` |
| 综合定位系统运维白皮书.md | [[4-Archives/Notes/Feishu/云空间/莱讯科技/项目运维管理/运维文档/综合定位系统运维白皮书]] | [飞书](https://reliablesense.feishu.cn/docx/AMuadobIrozdlZxG96gcHgtPnxe) | → 提取 | `2-Areas/Work/产品研发/综合定位系统运维白皮书.md` |
| 综合定位系统运维白皮书编写内容框架.md | [[4-Archives/Notes/Feishu/云空间/莱讯科技/项目运维管理/运维文档/综合定位系统运维白皮书编写内容框架]] | 留归档 | 白皮书已有完整版 |
| 移动应用平台运维白皮书编写内容框架.md | [[4-Archives/Notes/Feishu/云空间/莱讯科技/项目运维管理/运维文档/移动应用平台运维白皮书编写内容框架]] | 留归档 | 框架文档 |
| 综合定位系统进程清单编写内容框架.md | [[4-Archives/Notes/Feishu/云空间/莱讯科技/项目运维管理/运维文档/综合定位系统进程清单编写内容框架]] | 留归档 | 框架文档 |
| 综合定位系统配置清单编写内容框架.md | [[4-Archives/Notes/Feishu/云空间/莱讯科技/项目运维管理/运维文档/综合定位系统配置清单编写内容框架]] | 留归档 | 框架文档 |
| 移动应用平台进程清单编写内容框架.md | [[4-Archives/Notes/Feishu/云空间/莱讯科技/项目运维管理/运维文档/移动应用平台进程清单编写内容框架]] | 留归档 | 框架文档 |
| 移动应用平台配置清单编写内容框架.md | [[4-Archives/Notes/Feishu/云空间/莱讯科技/项目运维管理/运维文档/移动应用平台配置清单编写内容框架]] | 留归档 | 框架文档 |
| 数据库字典注释.xlsx | [[4-Archives/Notes/Feishu/云空间/莱讯科技/项目运维管理/运维文档/数据库字典注释.xlsx]] | 留归档 | 表格附件 |

### 4b. 升级文档

| 文件 | 本地路径 | 飞书链接 | 决策 | 目标路径 |
|------|---------|---------|------|---------|
| 升级文档--20260126.md | [[4-Archives/Notes/Feishu/云空间/莱讯科技/项目运维管理/升级文档/升级文档--20260126]] | [飞书](https://reliablesense.feishu.cn/docx/YNlKdlNzMogEq3xSsrscEDcQnqg) | → 提取 | `3-Resources/Tech/代码片段/平台升级文档-最新版.md` |
| 导航服务器更新文档.md | [[4-Archives/Notes/Feishu/云空间/莱讯科技/项目运维管理/升级文档/导航服务器更新文档]] | [飞书](https://reliablesense.feishu.cn/docx/Ffvddci64oATfcx9BVbckMwgnnh) | → 提取 | `3-Resources/Tech/代码片段/导航服务器更新文档.md` |
| 导航服务器重启文档.md | [[4-Archives/Notes/Feishu/云空间/莱讯科技/项目运维管理/升级文档/导航服务器重启文档]] | [飞书](https://reliablesense.feishu.cn/docx/JusGdT3I3oe2guxmy6SclellnYe) | → 提取 | `3-Resources/Tech/代码片段/导航服务器重启文档.md` |
| 2.5升级文档.md | [[4-Archives/Notes/Feishu/云空间/莱讯科技/项目运维管理/升级文档/2.5升级文档]] | [飞书](https://reliablesense.feishu.cn/docx/K2X3di1MWo7vymxykJecGQoZnFb) | 留归档 | 旧版本 |
| 2.4升级版本流程.md | [[4-Archives/Notes/Feishu/云空间/莱讯科技/项目运维管理/升级文档/2.4升级版本流程]] | [飞书](https://reliablesense.feishu.cn/docx/YtbEdiE8boGjbyxtPK3cB3tXnmg) | 留归档 | 旧版本 |

### 4c. 交付文档

| 文件 | 本地路径 | 飞书链接 | 决策 | 目标路径 |
|------|---------|---------|------|---------|
| 部署手册.md | [[4-Archives/Notes/Feishu/云空间/莱讯科技/项目运维管理/交付文档/部署手册]] | [飞书](https://reliablesense.feishu.cn/docs/doxcn3NLUHLJwrpSxVsnCtVfTfd) | → 提取 | `3-Resources/Tech/代码片段/部署手册.md` |
| 部署文档离线版.md | [[4-Archives/Notes/Feishu/云空间/莱讯科技/项目运维管理/交付文档/部署文档离线版]] | [飞书](https://reliablesense.feishu.cn/docx/LsHXdLWbmogiEKxZtK5c229nnad) | → 提取 | `3-Resources/Tech/代码片段/部署文档-离线版.md` |
| 私有化部署数据库生成步骤.md | [[4-Archives/Notes/Feishu/云空间/莱讯科技/项目运维管理/交付文档/私有化部署数据库生成步骤]] | [飞书](https://reliablesense.feishu.cn/docx/ArEWdDLrCoeAMpxJV7tc2YC7ntb) | → 提取 | `3-Resources/Tech/代码片段/私有化部署-数据库生成步骤.md` |
| 地图交付标准.md | [[4-Archives/Notes/Feishu/云空间/莱讯科技/项目运维管理/交付文档/地图交付标准]] | [飞书](https://reliablesense.feishu.cn/docx/CHvwd4VPboHEtpxyhsWcP7PonPe) | → 提取 | `3-Resources/Tech/代码片段/地图交付标准.md` |
| 交接文档.md | [[4-Archives/Notes/Feishu/云空间/莱讯科技/项目运维管理/交付文档/交接文档]] | [飞书](https://reliablesense.feishu.cn/docx/UOvmd7dz4oFkXVxuq3OczvtrnHf) | → 提取 | `3-Resources/Tech/代码片段/项目交接文档.md` |
| 中间件实施标准化文档.md | [[4-Archives/Notes/Feishu/云空间/莱讯科技/项目运维管理/交付文档/中间件实施标准化文档]] | [飞书](https://reliablesense.feishu.cn/docx/CmG7d0TpIo93M8xpgWucRUSKnYb) | → 提取 | `3-Resources/Tech/代码片段/中间件实施标准化文档.md` |
| 现场测试实施标准化文档.md | [[4-Archives/Notes/Feishu/云空间/莱讯科技/项目运维管理/交付文档/现场测试实施标准化文档]] | [飞书](https://reliablesense.feishu.cn/docx/Xsj8dUH5IoKCRuxYRL8ceVTOnKh) | → 提取 | `3-Resources/Tech/代码片段/现场测试实施标准化文档.md` |
| 无动力设备管理系统部署指南.md | [[4-Archives/Notes/Feishu/云空间/莱讯科技/项目运维管理/交付文档/无动力设备管理系统部署指南]] | [飞书](https://reliablesense.feishu.cn/docx/NsKCdYwf3okiEPxw0yScBOeGnNh) | → 提取 | `3-Resources/Tech/代码片段/无动力设备管理系统部署指南.md` |
| 验收会议流程.md | [[4-Archives/Notes/Feishu/云空间/莱讯科技/项目运维管理/交付文档/验收会议流程]] | [飞书](https://reliablesense.feishu.cn/docx/F9ufd0xoxoa5n0xXlWdcvRrEnJf) | → 提取 | `2-Areas/Work/业务管理/验收会议流程.md` |
| 验收确认报告.md | [[4-Archives/Notes/Feishu/云空间/莱讯科技/项目运维管理/交付文档/验收确认报告]] | [飞书](https://reliablesense.feishu.cn/docx/CwTrdyjpIoh9CcxFymscde3Jnq6) | → 提取 | `2-Areas/Work/业务管理/验收确认报告-模板.md` |
| 确认报告（软件）.md | [[4-Archives/Notes/Feishu/云空间/莱讯科技/项目运维管理/交付文档/确认报告（软件）]] | [飞书](https://reliablesense.feishu.cn/docx/doxcnljrKooELVNhrut5pZswMzc) | → 提取 | `2-Areas/Work/业务管理/软件确认报告-模板.md` |
| 设计验证报告.md | [[4-Archives/Notes/Feishu/云空间/莱讯科技/项目运维管理/交付文档/设计验证报告]] | [飞书](https://reliablesense.feishu.cn/docx/YbkHdX5zoopuh6xyFHOcNPHFndb) | → 提取 | `2-Areas/Work/业务管理/设计验证报告-模板.md` |
| 管理系统项目验收报告.md | [[4-Archives/Notes/Feishu/云空间/莱讯科技/项目运维管理/交付文档/管理系统项目验收报告]] | [飞书](https://reliablesense.feishu.cn/docx/IF1qd37NdoCGVUxMAi4cw1wynZb) | → 提取 | `2-Areas/Work/业务管理/项目验收报告-模板.md` |
| 用户手册（软件）.md | [[4-Archives/Notes/Feishu/云空间/莱讯科技/项目运维管理/交付文档/用户手册（软件）]] | [飞书](https://reliablesense.feishu.cn/docx/Z3H7dsbrSob9Kfxbw7ZcwloHnJc) | → 提取 | `2-Areas/Work/产品研发/定位平台用户手册.md` |

### 4d. 售后文档

| 文件 | 本地路径 | 飞书链接 | 决策 | 目标路径 |
|------|---------|---------|------|---------|
| 定位平台配置建议-v2.md | [[4-Archives/Notes/Feishu/云空间/莱讯科技/项目运维管理/售后文档/定位平台配置建议-v2]] | [飞书](https://reliablesense.feishu.cn/docx/BQ3fdtAgtoeyEuxvvxScqWCznne) | → 提取 | `3-Resources/Tech/代码片段/定位平台配置建议.md` |
| 系统容灾备份方案.md | [[4-Archives/Notes/Feishu/云空间/莱讯科技/项目运维管理/售后文档/系统容灾备份方案]] | [飞书](https://reliablesense.feishu.cn/docx/Na7YdwtkYosbSJxCZyPcMmSlnCe) | → 提取 | `2-Areas/Work/产品研发/系统容灾备份方案.md` |
| 定位平台配置建议.md | [[4-Archives/Notes/Feishu/云空间/莱讯科技/项目运维管理/售后文档/定位平台配置建议]] | - | 留归档 | 旧版本，被 v2 覆盖 |
| 定位平台配置建议-待完善.md | [[4-Archives/Notes/Feishu/云空间/莱讯科技/项目运维管理/售后文档/定位平台配置建议-待完善]] | - | 留归档 | 草稿版 |
| 系统容灾备份的方案.md | [[4-Archives/Notes/Feishu/云空间/莱讯科技/项目运维管理/售后文档/系统容灾备份的方案]] | - | 留归档 | 与上面重复 |
| 系统整改配置表.md | [[4-Archives/Notes/Feishu/云空间/莱讯科技/项目运维管理/售后文档/系统整改配置表]] | - | 留归档 | 根目录已有同文件 |
| SOW文件.md | [[4-Archives/Notes/Feishu/云空间/莱讯科技/项目运维管理/售后文档/SOW文件]] | - | 留归档 | 项目 SOW |

### 4e. 集群资料

所有 `*集群.md` 文件（约 20 个）→ 提取到 `3-Resources/Tech/环境配置/集群/` 下按名称。

| 文件 | 本地路径 | 决策 | 目标路径 |
|------|---------|------|---------|
| cnnc_qshdz集群.md | [[4-Archives/Notes/Feishu/云空间/莱讯科技/项目运维管理/集群资料/cnnc_qshdz集群]] | [飞书](https://reliablesense.feishu.cn/docx/MKTNd2yCQoXoGqxc7ylcO5DcnOd) | → 提取 | `3-Resources/Tech/环境配置/集群/` |
| madinat_gat集群.md | [[4-Archives/Notes/Feishu/云空间/莱讯科技/项目运维管理/集群资料/madinat_gat集群]] | [飞书](https://reliablesense.feishu.cn/docx/N7gMdz5ukoIv1Bxj38bcBobInCc) | → 提取 | `3-Resources/Tech/环境配置/集群/` |
| madinat_hjc集群.md | [[4-Archives/Notes/Feishu/云空间/莱讯科技/项目运维管理/集群资料/madinat_hjc集群]] | [飞书](https://reliablesense.feishu.cn/docs/doccn6POZJyaWmcGGsWDbuyGARb) | → 提取 | `3-Resources/Tech/环境配置/集群/` |
| madinat_hll集群.md | [[4-Archives/Notes/Feishu/云空间/莱讯科技/项目运维管理/集群资料/madinat_hll集群]] | [飞书](https://reliablesense.feishu.cn/docx/JdWOdanhvo8Yl8xAs9pc4xWGnI9) | → 提取 | `3-Resources/Tech/环境配置/集群/` |
| madinat_xmc集群.md | [[4-Archives/Notes/Feishu/云空间/莱讯科技/项目运维管理/集群资料/madinat_xmc集群]] | [飞书](https://reliablesense.feishu.cn/docs/doccnRbr2ps3Rpla22Se3M7vnFc) | → 提取 | `3-Resources/Tech/环境配置/集群/` |
| madinat_sewd集群.md | [[4-Archives/Notes/Feishu/云空间/莱讯科技/项目运维管理/集群资料/madinat_sewd集群]] | [飞书](https://reliablesense.feishu.cn/docx/SGYudVlmgoEJ0ixNyuhcC94rncf) | → 提取 | `3-Resources/Tech/环境配置/集群/` |
| madinat_ntt集群.md | [[4-Archives/Notes/Feishu/云空间/莱讯科技/项目运维管理/集群资料/madinat_ntt集群]] | [飞书](https://reliablesense.feishu.cn/docx/GmiydvdkdotNEWxPntpcFGXZnmd) | → 提取 | `3-Resources/Tech/环境配置/集群/` |
| madinat_lyrydw集群.md | [[4-Archives/Notes/Feishu/云空间/莱讯科技/项目运维管理/集群资料/madinat_lyrydw集群]] | [飞书](https://reliablesense.feishu.cn/docx/O5P2dVdVMoc3pWx0GVic4cpenhc) | → 提取 | `3-Resources/Tech/环境配置/集群/` |
| madinat_lyhx集群.md | [[4-Archives/Notes/Feishu/云空间/莱讯科技/项目运维管理/集群资料/madinat_lyhx集群]] | [飞书](https://reliablesense.feishu.cn/docx/HDKcdM8myoW1RExNYvac0N4pnuJ) | → 提取 | `3-Resources/Tech/环境配置/集群/` |
| xintai_xintai集群.md | [[4-Archives/Notes/Feishu/云空间/莱讯科技/项目运维管理/集群资料/xintai_xintai集群]] | [飞书](https://reliablesense.feishu.cn/docx/MbA7diPTJosC1Gxn3XPcfdMznVg) | → 提取 | `3-Resources/Tech/环境配置/集群/` |
| gjtsg_zhdl集群.md | [[4-Archives/Notes/Feishu/云空间/莱讯科技/项目运维管理/集群资料/gjtsg_zhdl集群]] | [飞书](https://reliablesense.feishu.cn/docx/FxjUdZYiyoDWmOxHklhcjvMlnZb) | → 提取 | `3-Resources/Tech/环境配置/集群/` |
| shwl_shsg集群.md | [[4-Archives/Notes/Feishu/云空间/莱讯科技/项目运维管理/集群资料/shwl_shsg集群]] | [飞书](https://reliablesense.feishu.cn/docx/MJ2KdoekEoS4jyxuHWfcx2UMnUb) | → 提取 | `3-Resources/Tech/环境配置/集群/` |
| shwl_gzhft集群.md | [[4-Archives/Notes/Feishu/云空间/莱讯科技/项目运维管理/集群资料/shwl_gzhft集群]] | [飞书](https://reliablesense.feishu.cn/docx/WY2Hd2wu5oHOI1xJb3UculFSn1d) | → 提取 | `3-Resources/Tech/环境配置/集群/` |
| jiexun_autotrader集群.md | [[4-Archives/Notes/Feishu/云空间/莱讯科技/项目运维管理/集群资料/jiexun_autotrader集群]] | [飞书](https://reliablesense.feishu.cn/docx/QNHkdVzTEooNW9xhmvScZ0cKnMd) | → 提取 | `3-Resources/Tech/环境配置/集群/` |
| lance_dxgcsy集群.md | [[4-Archives/Notes/Feishu/云空间/莱讯科技/项目运维管理/集群资料/lance_dxgcsy集群]] | [飞书](https://reliablesense.feishu.cn/docx/VN9RdnZIforRPWxYXX5ckt9ynQf) | → 提取 | `3-Resources/Tech/环境配置/集群/` |
| erdoswhcyy_erdoswhcyy集群.md | [[4-Archives/Notes/Feishu/云空间/莱讯科技/项目运维管理/集群资料/erdoswhcyy_erdoswhcyy集群]] | [飞书](https://reliablesense.feishu.cn/docx/GW4tda6T9opR4jxGCkUcQA57n7d) | → 提取 | `3-Resources/Tech/环境配置/集群/` |
| whjc_whjc集群.md | [[4-Archives/Notes/Feishu/云空间/莱讯科技/项目运维管理/集群资料/whjc_whjc集群]] | [飞书](https://reliablesense.feishu.cn/docx/RKuQdRotpoe3zixaPrWcx9j6nBc) | → 提取 | `3-Resources/Tech/环境配置/集群/` |
| cloud 资料.md | [[4-Archives/Notes/Feishu/云空间/莱讯科技/项目运维管理/集群资料/cloud 资料]] | [飞书](https://reliablesense.feishu.cn/docx/QXgzdOibVoySLUxFwtzctoWin0t) | → 提取 | `3-Resources/Tech/环境配置/集群/` |
| dev-office 集群.md | [[4-Archives/Notes/Feishu/云空间/莱讯科技/项目运维管理/集群资料/dev-office 集群]] | [飞书](https://reliablesense.feishu.cn/docx/QUtcdDjFjocOxVxiEiRcPQ20nZb) | → 提取 | `3-Resources/Tech/环境配置/集群/` |
| online-sh 集群.md | [[4-Archives/Notes/Feishu/云空间/莱讯科技/项目运维管理/集群资料/online-sh 集群]] | [飞书](https://reliablesense.feishu.cn/docs/doccn4ZbY3L0axKO5uic6o278ge) | → 提取 | `3-Resources/Tech/环境配置/集群/` |
| middleware-bj 集群.md | [[4-Archives/Notes/Feishu/云空间/莱讯科技/项目运维管理/集群资料/middleware-bj 集群]] | [飞书](https://reliablesense.feishu.cn/docs/doccnqB78BLk2Mq9fvYb9xEEbTd) | → 提取 | `3-Resources/Tech/环境配置/集群/` |
| 代理配置操作说明.md | [[4-Archives/Notes/Feishu/云空间/莱讯科技/项目运维管理/集群资料/代理配置操作说明]] | [飞书](https://reliablesense.feishu.cn/docx/LbLPdc4dHoROcnxVSsmcF2sgnyb) | → 提取 | `3-Resources/Tech/代码片段/代理配置操作说明.md` |
| 内网穿透 frp 说明.md | [[4-Archives/Notes/Feishu/云空间/莱讯科技/项目运维管理/集群资料/内网穿透 frp 说明]] | [飞书](https://reliablesense.feishu.cn/docx/doxcnAdY9LCLIeBTvI8nVH0St8e) | → 提取 | `3-Resources/Tech/代码片段/内网穿透frp说明.md` |

### 4f. 基础设施

| 文件 | 本地路径 | 飞书链接 | 决策 | 目标路径 |
|------|---------|---------|------|---------|
| 综合定位系统技术要求.md | [[4-Archives/Notes/Feishu/云空间/莱讯科技/项目运维管理/基础设施/综合定位系统技术要求]] | [飞书](https://reliablesense.feishu.cn/docx/Gi0MdNC9ToLxM0xfPDCcsKD2nzf) | → 提取 | `2-Areas/Work/产品研发/综合定位系统技术要求.md` | 产品技术规格 |
| 系统功能清单.md | [[4-Archives/Notes/Feishu/云空间/莱讯科技/项目运维管理/基础设施/系统功能清单]] | [飞书](https://reliablesense.feishu.cn/docx/WdNtdRhPxoN8VoxwzI5cjocCntK) | → 提取 | `2-Areas/Work/产品研发/综合定位系统功能清单.md` | 产品功能列表 |
| 信息安全问题回复.md | [[4-Archives/Notes/Feishu/云空间/莱讯科技/项目运维管理/基础设施/信息安全问题回复]] | [飞书](https://reliablesense.feishu.cn/docx/YIs2dQZh4o3v3axaC0ccR2TInGe) | → 提取 | `1-Projects/Work/广州机场/信息安全问题回复.md` | 含综合定位系统特征，归广州机场 |
| Nexus相关地址.md | [[4-Archives/Notes/Feishu/云空间/莱讯科技/项目运维管理/基础设施/Nexus相关地址]] | [飞书](https://reliablesense.feishu.cn/docs/doccnMTqpCuBzz3UTWyYm6iiF2e) | → 提取 | `3-Resources/Tech/环境配置/Nexus相关地址.md` | 通用环境信息 |
| 系统架构图.md | [[4-Archives/Notes/Feishu/云空间/莱讯科技/项目运维管理/基础设施/系统架构图]] | [飞书](https://reliablesense.feishu.cn/docx/IYLtdtwDQoaOetxP9Xkc66jfnPf) | 留归档 | 根目录已提取到产品研发 |
| 系统架构图-v2.md | [[4-Archives/Notes/Feishu/云空间/莱讯科技/项目运维管理/基础设施/系统架构图-v2]] | [飞书](https://reliablesense.feishu.cn/docx/JdRpdI6QKoDIICx8qducxh97nWh) | 留归档 | 根目录已提取到产品研发 |

### 4g. 散落文件

| 文件 | 本地路径 | 飞书链接 | 决策 | 目标路径 |
|------|---------|---------|------|---------|
| 莱讯科技-小程序管理文档.md | [[4-Archives/Notes/Feishu/云空间/莱讯科技/项目运维管理/莱讯科技-小程序管理文档]] | [飞书](https://reliablesense.feishu.cn/docx/JgCpdERLho9N3zxiGpqcQ7GAnov) | → 提取 | `3-Resources/Tech/知识卡片/小程序管理文档.md` |

---

## 五、莱讯科技/项目开发管理

### 5a. 定位平台企业版

| 文件 | 本地路径 | 飞书链接 | 决策 | 目标路径 |
|------|---------|---------|------|---------|
| 软件项目资料-企业版.md | [[4-Archives/Notes/Feishu/云空间/莱讯科技/项目开发管理/定位平台企业版/软件项目资料-企业版]] | [飞书](https://reliablesense.feishu.cn/docx/Sk1fdcud4oXDO0xLblCcpKYDn1c) | → 提取 | `2-Areas/Work/产品研发/软件项目资料-企业版.md` |
| 概要设计说明书-企业版.md | [[4-Archives/Notes/Feishu/云空间/莱讯科技/项目开发管理/定位平台企业版/概要设计说明书-企业版]] | [飞书](https://reliablesense.feishu.cn/docx/doxcngYEqNfE7V81KsKpg2ewK2f) | → 提取 | `2-Areas/Work/产品研发/概要设计说明书-企业版.md` |
| 软件架构图.md | [[4-Archives/Notes/Feishu/云空间/莱讯科技/项目开发管理/定位平台企业版/软件架构图]] | [飞书](https://reliablesense.feishu.cn/docs/doccnNYXYzLw4jvVOBOTjTmjswh) | → 提取 | `2-Areas/Work/产品研发/定位平台软件架构图.md` |
| 定位平台后端汇总.md | [[4-Archives/Notes/Feishu/云空间/莱讯科技/项目开发管理/定位平台企业版/定位平台后端汇总]] | [飞书](https://reliablesense.feishu.cn/docs/doccnYL2wLoROVlZqKWO39CnGMh) | → 提取 | `2-Areas/Work/产品研发/定位平台后端汇总.md` |
| 定位平台关键接口.md | [[4-Archives/Notes/Feishu/云空间/莱讯科技/项目开发管理/定位平台企业版/定位平台关键接口]] | [飞书](https://reliablesense.feishu.cn/docx/ZTNPdFqmQo3zRvxUrZJcsdU4nGg) | → 提取 | `2-Areas/Work/产品研发/定位平台关键接口.md` |
| 定位平台服务器.md | [[4-Archives/Notes/Feishu/云空间/莱讯科技/项目开发管理/定位平台企业版/定位平台服务器]] | [飞书](https://reliablesense.feishu.cn/docx/UqgAd09BRoZ306xMBW4cvIK2npg) | → 提取 | `2-Areas/Work/产品研发/定位平台服务器说明.md` |
| 定位平台操作手册.md | [[4-Archives/Notes/Feishu/云空间/莱讯科技/项目开发管理/定位平台企业版/定位平台操作手册]] | [飞书](https://reliablesense.feishu.cn/docx/A2jXdJxm7o6ilNxFx8ac86MYndh) | → 提取 | `2-Areas/Work/产品研发/定位平台操作手册.md` |

### 5b. 定位平台定制版

| 文件 | 本地路径 | 决策 | 目标路径 |
|------|---------|------|---------|
| 软件项目资料-定制版.md | [[4-Archives/Notes/Feishu/云空间/莱讯科技/项目开发管理/定位平台定制版/软件项目资料-定制版]] | [飞书](https://reliablesense.feishu.cn/docx/doxcnmwgwcdPnrEHAgd4pXZMBgc) | → 提取 | `2-Areas/Work/产品研发/软件项目资料-定制版.md` |
| 概要设计说明书-定制版.md | [[4-Archives/Notes/Feishu/云空间/莱讯科技/项目开发管理/定位平台定制版/概要设计说明书-定制版]] | [飞书](https://reliablesense.feishu.cn/docx/doxcnE47mE0e0UrshePl4lw033d) | → 提取 | `2-Areas/Work/产品研发/概要设计说明书-定制版.md` |
| 各项目子目录 | 见下方项目资料管理部分 | → 归档 | 按项目分配 |

### 5c. 定位平台中间件 / 5d. 云端版

| 文件 | 本地路径 | 决策 | 目标路径 |
|------|---------|------|---------|
| 软件项目资料-中间件.md | [[4-Archives/Notes/Feishu/云空间/莱讯科技/项目开发管理/定位平台中间件/软件项目资料-中间件]] | [飞书](https://reliablesense.feishu.cn/docx/QbwZdfpAGoD01Ux19u8cuYuVnYf) | → 提取 | `2-Areas/Work/产品研发/软件项目资料-中间件.md` |
| 软件项目资料-云端版.md | [[4-Archives/Notes/Feishu/云空间/莱讯科技/项目开发管理/定位平台云端版/软件项目资料-云端版]] | [飞书](https://reliablesense.feishu.cn/docx/doxcnYnCagX1SsmAbbSyUtL0SRb) | → 提取 | `2-Areas/Work/产品研发/软件项目资料-云端版.md` |

---

## 六、莱讯科技/项目资料管理

### 6a. 进行中项目 → `1-Projects/Work/`

| 飞书目录 | 本地路径 | 目标路径 |
|---------|---------|---------|
| 002. 上海上港/ | [[4-Archives/Notes/Feishu/云空间/莱讯科技/项目资料管理/002. 上海上港/]] | `1-Projects/Work/上港仓储管理/` |
| 004. 广州机场-综合定位/ | [[4-Archives/Notes/Feishu/云空间/莱讯科技/项目资料管理/004. 广州机场-综合定位/]] | `1-Projects/Work/广州机场/综合定位/` |
| 005. 广州机场-移动应用平台/ | [[4-Archives/Notes/Feishu/云空间/莱讯科技/项目资料管理/005. 广州机场-移动应用平台/]] | `1-Projects/Work/广州机场/移动应用平台/` |
| 南宁机场项目/ | [[4-Archives/Notes/Feishu/云空间/莱讯科技/项目资料管理/南宁机场项目/]] | `1-Projects/Work/南宁机场/` |

> 只提取 .md 技术文档，.xlsx/.pptx/.docx/.mp4/.zip 等附件留归档。

### 6b. 已结束项目 → `4-Archives/Projects/Work/`

| 飞书目录 | 本地路径 | 目标路径 |
|---------|---------|---------|
| 003. 中东电子厂客户/ | [[4-Archives/Notes/Feishu/云空间/莱讯科技/项目资料管理/003. 中东电子厂客户/]] | `4-Archives/Projects/Work/中东电子厂/` |
| 中联核信/ | [[4-Archives/Notes/Feishu/云空间/莱讯科技/项目资料管理/中联核信/]] | `4-Archives/Projects/Work/中联核信/` |
| 红点定位/ | [[4-Archives/Notes/Feishu/云空间/莱讯科技/项目资料管理/红点定位/]] | `4-Archives/Projects/Work/红点定位/` |
| 998. 售后项目/ | [[4-Archives/Notes/Feishu/云空间/莱讯科技/项目资料管理/998. 售后项目/]] | `4-Archives/Projects/Work/对应项目名/` |
| 999. 归档项目/ | [[4-Archives/Notes/Feishu/云空间/莱讯科技/项目资料管理/999. 归档项目/]] | `4-Archives/Projects/Work/对应项目名/` |
| ~其他项目/ | [[4-Archives/Notes/Feishu/云空间/莱讯科技/项目资料管理/~其他项目/]] | `4-Archives/Projects/Work/对应项目名/` |

### 6c. 通用资料

| 飞书目录 | 本地路径 | 决策 | 目标路径 |
|---------|---------|------|---------|
| 000. 售前项目/ | [[4-Archives/Notes/Feishu/云空间/莱讯科技/项目资料管理/000. 售前项目/]] | → 提取 | `2-Areas/Work/业务管理/售前项目/` |
| 001. 项目资料模板/ | [[4-Archives/Notes/Feishu/云空间/莱讯科技/项目资料管理/001. 项目资料模板/]] | → 提取 | `2-Areas/Work/业务管理/项目资料模板/` |
| 软著立项/ | [[4-Archives/Notes/Feishu/云空间/莱讯科技/项目资料管理/软著立项/]] | → 提取 | `2-Areas/Work/综合管理/软著立项/` |
| 项目评估/ | [[4-Archives/Notes/Feishu/云空间/莱讯科技/项目资料管理/项目评估/]] | → 提取 | `2-Areas/Work/业务管理/项目评估/` |
| cle测算报告.md | [[4-Archives/Notes/Feishu/云空间/莱讯科技/项目资料管理/cle测算报告]] | [飞书](https://reliablesense.feishu.cn/docx/KsIRdMFKRoRWqQx8yYkce8G0nys) | → 提取 | `3-Resources/Tech/知识卡片/CLE测算报告.md` |

---

## 七、莱讯科技/解决方案管理

23 个行业方案目录 → `3-Resources/Business/解决方案/` 下按行业分子文件夹。

| 飞书目录 | 本地路径 | 目标路径 |
|---------|---------|---------|
| 医疗管理/ | [[4-Archives/Notes/Feishu/云空间/莱讯科技/解决方案管理/医疗管理/]] | `3-Resources/Business/解决方案/医疗管理/` |
| 工厂智能管理/ | [[4-Archives/Notes/Feishu/云空间/莱讯科技/解决方案管理/工厂智能管理/]] | `3-Resources/Business/解决方案/工厂智能管理/` |
| 人员定位系统/ | [[4-Archives/Notes/Feishu/云空间/莱讯科技/解决方案管理/人员定位系统/]] | `3-Resources/Business/解决方案/人员定位系统/` |
| 轨道交通/ | [[4-Archives/Notes/Feishu/云空间/莱讯科技/解决方案管理/轨道交通/]] | `3-Resources/Business/解决方案/轨道交通/` |
| 监狱方案/ | [[4-Archives/Notes/Feishu/云空间/莱讯科技/解决方案管理/监狱方案/]] | `3-Resources/Business/解决方案/监狱方案/` |
| APP/ | [[4-Archives/Notes/Feishu/云空间/莱讯科技/解决方案管理/APP/]] | `3-Resources/Business/解决方案/APP/` |
| 仓储物流/ | [[4-Archives/Notes/Feishu/云空间/莱讯科技/解决方案管理/仓储物流/]] | `3-Resources/Business/解决方案/仓储物流/` |
| 智慧工地/ | [[4-Archives/Notes/Feishu/云空间/莱讯科技/解决方案管理/智慧工地/]] | `3-Resources/Business/解决方案/智慧工地/` |
| 展厅方案/ | [[4-Archives/Notes/Feishu/云空间/莱讯科技/解决方案管理/展厅方案/]] | `3-Resources/Business/解决方案/展厅方案/` |
| 智慧停车/ | [[4-Archives/Notes/Feishu/云空间/莱讯科技/解决方案管理/智慧停车/]] | `3-Resources/Business/解决方案/智慧停车/` |
| 三维GIS方案/ | [[4-Archives/Notes/Feishu/云空间/莱讯科技/解决方案管理/三维GIS方案/]] | `3-Resources/Business/解决方案/三维GIS方案/` |
| 资产管理/ | [[4-Archives/Notes/Feishu/云空间/莱讯科技/解决方案管理/资产管理/]] | `3-Resources/Business/解决方案/资产管理/` |
| 室外定位GPS/ | [[4-Archives/Notes/Feishu/云空间/莱讯科技/解决方案管理/室外定位GPS/]] | `3-Resources/Business/解决方案/室外定位GPS/` |
| 工业环境解决方案/ | [[4-Archives/Notes/Feishu/云空间/莱讯科技/解决方案管理/工业环境解决方案/]] | `3-Resources/Business/解决方案/工业环境/` |
| 枪支定位/ | [[4-Archives/Notes/Feishu/云空间/莱讯科技/解决方案管理/枪支定位/]] | `3-Resources/Business/解决方案/枪支定位/` |
| 室外定位导航/ | [[4-Archives/Notes/Feishu/云空间/莱讯科技/解决方案管理/室外定位导航/]] | `3-Resources/Business/解决方案/室外定位导航/` |
| 智能制造/ | [[4-Archives/Notes/Feishu/云空间/莱讯科技/解决方案管理/智能制造/]] | `3-Resources/Business/解决方案/智能制造/` |
| 执法办案中心/ | [[4-Archives/Notes/Feishu/云空间/莱讯科技/解决方案管理/执法办案中心/]] | `3-Resources/Business/解决方案/执法办案中心/` |
| 交通运输方案/ | [[4-Archives/Notes/Feishu/云空间/莱讯科技/解决方案管理/交通运输方案/]] | `3-Resources/Business/解决方案/交通运输/` |
| 室外手环定位/ | [[4-Archives/Notes/Feishu/云空间/莱讯科技/解决方案管理/室外手环定位/]] | `3-Resources/Business/解决方案/室外手环定位/` |
| 煤矿智能管理/ | [[4-Archives/Notes/Feishu/云空间/莱讯科技/解决方案管理/煤矿智能管理/]] | `3-Resources/Business/解决方案/煤矿智能管理/` |
| 方案制作需求清单/ | [[4-Archives/Notes/Feishu/云空间/莱讯科技/解决方案管理/方案制作需求清单/]] | `3-Resources/Business/解决方案/` |
| ~其他公司方案/ | [[4-Archives/Notes/Feishu/云空间/莱讯科技/解决方案管理/~其他公司方案/]] | 留归档 |

---

## 八、莱讯科技/其他子目录

| 飞书目录 | 本地路径 | 决策 | 目标路径 |
|---------|---------|------|---------|
| 销售管理/ | [[4-Archives/Notes/Feishu/云空间/莱讯科技/销售管理/]] | → 提取 | `2-Areas/Work/业务管理/销售管理/` |
| 供应商管理/ | [[4-Archives/Notes/Feishu/云空间/莱讯科技/供应商管理/]] | → 提取 | `2-Areas/Work/设备管理/供应商管理/` |
| 品牌手册与logo/ | [[4-Archives/Notes/Feishu/云空间/莱讯科技/品牌手册与logo/]] | → 提取 | `2-Areas/Work/品牌宣传/品牌手册/` |
| 招聘管理/ | [[4-Archives/Notes/Feishu/云空间/莱讯科技/招聘管理/]] | → 提取 | `2-Areas/Work/团队管理/招聘/` |
| 网站维护/ | [[4-Archives/Notes/Feishu/云空间/莱讯科技/网站维护/]] | → 提取 | `2-Areas/Work/品牌宣传/网站维护/` |
| 宣传/ | [[4-Archives/Notes/Feishu/云空间/莱讯科技/宣传/]] | → 提取 | `2-Areas/Work/品牌宣传/宣传/` |
| 公司宣传物（公司介绍）/ | [[4-Archives/Notes/Feishu/云空间/莱讯科技/公司宣传物（公司介绍）/]] | → 提取 | `2-Areas/Work/品牌宣传/公司介绍/` |
| 往期展会资料合集/ | [[4-Archives/Notes/Feishu/云空间/莱讯科技/往期展会资料合集/]] | → 提取 | `2-Areas/Work/品牌宣传/展会/` |
| 公司英文资料/ | [[4-Archives/Notes/Feishu/云空间/莱讯科技/公司英文资料/]] | → 提取 | `2-Areas/Work/品牌宣传/英文资料/` |
| 路网维护/ | [[4-Archives/Notes/Feishu/云空间/莱讯科技/路网维护/]] | 留归档 | 图片/CAD |
| ~参考资料/ | [[4-Archives/Notes/Feishu/云空间/莱讯科技/~参考资料/]] | 待确认 | 需逐个查看 |
| 共享文件/ | [[4-Archives/Notes/Feishu/云空间/莱讯科技/共享文件/]] | 留归档 | 临时网盘 |

### 公司内部资料重点文件

| 文件 | 本地路径 | 决策 | 目标路径 |
|------|---------|------|---------|
| 员工管理制度.md | [[4-Archives/Notes/Feishu/云空间/莱讯科技/公司内部资料/员工管理制度]] | → 提取 | `2-Areas/Work/团队管理/员工管理制度.md` |
| 工作周报管理及考核制度.md | [[4-Archives/Notes/Feishu/云空间/莱讯科技/公司内部资料/工作周报管理及考核制度]] | → 提取 | `2-Areas/Work/团队管理/工作周报管理及考核制度.md` |
| 考勤制度.md | [[4-Archives/Notes/Feishu/云空间/莱讯科技/公司内部资料/考勤制度]] | → 提取 | `2-Areas/Work/团队管理/考勤制度.md` |
| 组织架构图.md | [[4-Archives/Notes/Feishu/云空间/莱讯科技/公司内部资料/组织架构图]] | → 提取 | `2-Areas/Work/团队管理/组织架构图.md` |
| 地图制作设计书.md | [[4-Archives/Notes/Feishu/云空间/莱讯科技/公司内部资料/地图制作设计书]] | → 提取 | `3-Resources/Tech/知识卡片/地图制作设计书.md` |
| PPT模版/ | [[4-Archives/Notes/Feishu/云空间/莱讯科技/公司内部资料/PPT模版/]] | → 提取 | `2-Areas/Work/品牌宣传/PPT模版/` |
| ISO9001质量体系认证/ | [[4-Archives/Notes/Feishu/云空间/莱讯科技/公司内部资料/ISO9001质量体系认证/]] | → 提取 | `2-Areas/Work/综合管理/ISO9001/` |
| 软著的立项资料/ | [[4-Archives/Notes/Feishu/云空间/莱讯科技/公司内部资料/软著的立项资料/]] | → 提取 | `2-Areas/Work/综合管理/软著立项/` |
| 小程序管理文档.md | [[4-Archives/Notes/Feishu/云空间/莱讯科技/小程序管理文档]] | → 提取 | `3-Resources/Tech/知识卡片/小程序管理文档.md` |

---

## 九、知识库

### 9a. 技术分享

| 文件 | 本地路径 | 飞书链接 | 决策 | 目标路径 |
|------|---------|---------|------|---------|
| 前端React开发规范.md | [[4-Archives/Notes/Feishu/知识库/技术分享/前端相关文档/前端React开发规范]] | [飞书](https://reliablesense.feishu.cn/doc/doccnymhDUxjzJsBjuZ5mBGpG4c) | → 提取 | `3-Resources/Tech/知识卡片/前端React开发规范.md` |
| 后端开发流程规范.md | [[4-Archives/Notes/Feishu/知识库/技术分享/后端相关文档/后端开发流程规范]] | [飞书](https://reliablesense.feishu.cn/docx/CUA7dlJrRoTZ3Fx8t5kc1UiRneb) | → 提取 | `3-Resources/Tech/知识卡片/后端开发流程规范.md` |
| 定位平台系统整体改造方案.md | [[4-Archives/Notes/Feishu/知识库/技术分享/后端相关文档/定位平台系统整体改造方案]] | [飞书](https://reliablesense.feishu.cn/doc/doccnVRMcLTfhON3R9OLZT7VHgf) | → 提取 | `2-Areas/Work/产品研发/定位平台系统整体改造方案.md` |
| 微服务说明.md | [[4-Archives/Notes/Feishu/知识库/技术分享/后端相关文档/微服务说明]] | [飞书](https://reliablesense.feishu.cn/docx/F2PhdYeMCoHjP6xd8y0cyz6Mnac) | → 提取 | `3-Resources/Tech/知识卡片/微服务说明.md` |
| 后端问题QA.md | [[4-Archives/Notes/Feishu/知识库/技术分享/后端问题QA]] | [飞书](https://reliablesense.feishu.cn/docx/OpsxdI417oi5i4xLyrhc8Znyn5f) | → 提取 | `3-Resources/Tech/问题解决/后端问题QA.md` |
| QGIS地图绘制准备.md | [[4-Archives/Notes/Feishu/知识库/技术分享/地图相关文档/QGIS地图绘制准备]] | [飞书](https://reliablesense.feishu.cn/docx/CXjHdQO7JogckXxR6owcL5AcnEb) | → 提取 | `3-Resources/Tech/知识卡片/QGIS地图绘制准备.md` |
| QGIS安装.md | [[4-Archives/Notes/Feishu/知识库/技术分享/地图相关文档/QGIS安装]] | [飞书](https://reliablesense.feishu.cn/docx/DKP6dIPIHoXYuMxJ5Xoc00LVngp) | → 提取 | `3-Resources/Tech/知识卡片/QGIS安装.md` |
| QGIS图片及瓦片图添加.md | [[4-Archives/Notes/Feishu/知识库/技术分享/地图相关文档/QGIS图片及瓦片图添加]] | [飞书](https://reliablesense.feishu.cn/docx/X68Zdyv98o4AgGx073LcsrscnAh) | → 提取 | `3-Resources/Tech/知识卡片/QGIS图片及瓦片图添加.md` |
| QGIS地图绘制注意事项CAD版.md | [[4-Archives/Notes/Feishu/知识库/技术分享/地图相关文档/QGIS地图绘制注意事项CAD版]] | [飞书](https://reliablesense.feishu.cn/doc/doccnKYx4RPxYSXzTH0ssUvvBmf) | → 提取 | `3-Resources/Tech/知识卡片/QGIS地图绘制注意事项CAD版.md` |
| png图片导入地图.md | [[4-Archives/Notes/Feishu/知识库/技术分享/地图相关文档/png图片导入地图]] | [飞书](https://reliablesense.feishu.cn/doc/doccn3DidLn9ur0mvFbqsnXhstd) | → 提取 | `3-Resources/Tech/知识卡片/png图片导入地图.md` |
| 瓦片图制作.md | [[4-Archives/Notes/Feishu/知识库/技术分享/地图相关文档/瓦片图制作]] | [飞书](https://reliablesense.feishu.cn/docx/OvGsdeF3UoAgULxqd9Kc08punEg) | → 提取 | `3-Resources/Tech/代码片段/瓦片图制作.md` |
| 路网绘制.md | [[4-Archives/Notes/Feishu/知识库/技术分享/地图相关文档/路网绘制]] | [飞书](https://reliablesense.feishu.cn/docx/doxcnmMiCtaR2HkpnlPPrChqyEb) | → 提取 | `3-Resources/Tech/代码片段/路网绘制.md` |
| 地图按钮、视角、控件控制.md | [[4-Archives/Notes/Feishu/知识库/技术分享/地图相关文档/地图按钮、视角、控件控制]] | [飞书](https://reliablesense.feishu.cn/docx/HUTId5xjFoaRIxxUkQWcEb1Xnge) | → 提取 | `3-Resources/Tech/知识卡片/地图控件控制.md` |
| 项目建立步骤.md | [[4-Archives/Notes/Feishu/知识库/技术分享/地图相关文档/项目建立步骤]] | [飞书](https://reliablesense.feishu.cn/docx/LapVd88f0oFaKUx4QwRcwrW1neI) | → 提取 | `3-Resources/Tech/代码片段/地图项目建立步骤.md` |
| 麦钉点云图地图绘制注意事项.md | [[4-Archives/Notes/Feishu/知识库/技术分享/地图相关文档/麦钉点云图地图绘制注意事项]] | [飞书](https://reliablesense.feishu.cn/doc/doccn6HL7llLqfP4e5qCI96CdUf) | → 提取 | `3-Resources/Tech/知识卡片/麦钉点云图地图绘制注意事项.md` |
| CICD流程介绍.md | [[4-Archives/Notes/Feishu/知识库/技术分享/基础平台相关文档/CICD流程介绍]] | [飞书](https://reliablesense.feishu.cn/doc/doccnqi4YxvSVSY23MSLXIkwIKe) | → 提取 | `3-Resources/Tech/知识卡片/CICD流程介绍.md` |
| Gitlab-CICD说明.md | [[4-Archives/Notes/Feishu/知识库/技术分享/基础平台相关文档/Gitlab-CICD说明]] | [飞书](https://reliablesense.feishu.cn/doc/doccnUileviuvksypU7AAbSEGwg) | → 提取 | `3-Resources/Tech/代码片段/Gitlab-CICD说明.md` |
| 前后端CICD.md | [[4-Archives/Notes/Feishu/知识库/技术分享/基础平台相关文档/前后端CICD]] | [飞书](https://reliablesense.feishu.cn/doc/doccncqa7DwRv2fD3Z3KA6oO4oh) | → 提取 | `3-Resources/Tech/代码片段/前后端CICD.md` |
| 开发分支管理规范.md | [[4-Archives/Notes/Feishu/知识库/技术分享/基础平台相关文档/开发分支管理规范]] | [飞书](https://reliablesense.feishu.cn/doc/doccnlE0yWc24L79rE98oSVsY8d) | → 提取 | `3-Resources/Tech/知识卡片/开发分支管理规范.md` |
| 办公网v2ray操作手册.md | [[4-Archives/Notes/Feishu/知识库/技术分享/基础平台相关文档/办公网VPN/办公网v2ray操作手册]] | [飞书](https://reliablesense.feishu.cn/docx/G1OBdhlTSotGV6xRToRcXlzWnoe) | → 提取 | `3-Resources/Tech/代码片段/办公网v2ray操作手册.md` |
| 办公网WireGuard操作手册.md | [[4-Archives/Notes/Feishu/知识库/技术分享/基础平台相关文档/办公网VPN/办公网WireGuard操作手册]] | [飞书](https://reliablesense.feishu.cn/docx/Q4OzdL6ZboG5dSxgqqlcNn4WnFf) | → 提取 | `3-Resources/Tech/代码片段/办公网WireGuard操作手册.md` |
| Deployment英文版/ (4个) | [[4-Archives/Notes/Feishu/知识库/技术分享/基础平台相关文档/Deployment英文版/]] | 各有飞书链接 | → 提取 | `3-Resources/Tech/代码片段/` 下按文件 |
| 私有化部署/ | [[4-Archives/Notes/Feishu/知识库/技术分享/基础平台相关文档/私有化部署/]] | 各有飞书链接 | → 提取 | `3-Resources/Tech/代码片段/` 下按文件 |
| PostGIS 相关 (8个) | [[4-Archives/Notes/Feishu/知识库/技术分享/数据库相关文档/Postgis/]] | 各有飞书链接 | → 提取 | `3-Resources/Tech/代码片段/` 合并到已有 PostGIS 笔记 |
| Postgres 相关 (4个) | [[4-Archives/Notes/Feishu/知识库/技术分享/数据库相关文档/Postgres/]] | 各有飞书链接 | → 提取 | `3-Resources/Tech/代码片段/` 合并到已有 SQL 笔记 |
| TimescaleDB 相关 (4个) | [[4-Archives/Notes/Feishu/知识库/技术分享/数据库相关文档/TimescaleDB/]] | 各有飞书链接 | → 提取 | `3-Resources/Tech/代码片段/` |
| locust报告参数说明.md | [[4-Archives/Notes/Feishu/知识库/技术分享/测试相关文档/locust报告参数说明]] | [飞书](https://reliablesense.feishu.cn/docx/doxcnyVpKX1V11tJYH2sKdff3Ph) | → 提取 | `3-Resources/Tech/知识卡片/locust报告参数说明.md` |
| 测试平台对比.md | [[4-Archives/Notes/Feishu/知识库/技术分享/测试相关文档/测试平台对比]] | [飞书](https://reliablesense.feishu.cn/doc/doccnoMeCyK1lHtPzzIxxZTmB8U) | → 提取 | `3-Resources/Tech/知识卡片/测试平台对比.md` |
| 测试流程1.md | [[4-Archives/Notes/Feishu/知识库/技术分享/测试相关文档/测试流程1]] | [飞书](https://reliablesense.feishu.cn/doc/doccnvKjRt0RgI04vi1UFEuAW4f) | → 提取 | `3-Resources/Tech/知识卡片/测试流程.md` |
| 测试的流程及内容.md | [[4-Archives/Notes/Feishu/知识库/技术分享/测试相关文档/测试的流程及内容]] | [飞书](https://reliablesense.feishu.cn/doc/doccnUSmCPXtSpHsITXo3gMqtqd) | → 提取 | `3-Resources/Tech/知识卡片/测试的流程及内容.md` |
| 测试计划初稿.md | [[4-Archives/Notes/Feishu/知识库/技术分享/测试相关文档/测试计划初稿]] | [飞书](https://reliablesense.feishu.cn/doc/doccnXKbFqjR5Up9dVYrzjvUUmh) | → 提取 | `3-Resources/Tech/知识卡片/测试计划初稿.md` |
| 禅道测试相关操作手册.md | [[4-Archives/Notes/Feishu/知识库/技术分享/测试相关文档/禅道测试相关操作手册]] | [飞书](https://reliablesense.feishu.cn/doc/doccnTqc7EnZxfZYH0T20rXWLVe) | → 提取 | `3-Resources/Tech/知识卡片/禅道测试操作手册.md` |
| 稳定性测试.md | [[4-Archives/Notes/Feishu/知识库/技术分享/测试相关文档/稳定性测试]] | [飞书](https://reliablesense.feishu.cn/docx/doxcnPMwcMjDrt0cdQBUlY9Jldf) | → 提取 | `3-Resources/Tech/知识卡片/稳定性测试.md` |
| MOKO-RSSI定位基站与树莓派组网.md | [[4-Archives/Notes/Feishu/知识库/技术分享/硬件相关文档/MOKO-RSSI定位基站与树莓派组网]] | [飞书](https://reliablesense.feishu.cn/docx/TDS8dDE7ToGtUWxMvu7c8bROnwf) | → 提取 | `3-Resources/Tech/知识卡片/MOKO-RSSI定位基站与树莓派组网.md` |
| RTK设备局域网WiFi使用文档.md | [[4-Archives/Notes/Feishu/知识库/技术分享/硬件相关文档/RTK设备局域网WiFi使用文档]] | [飞书](https://reliablesense.feishu.cn/docx/Yr5vdDP3YonYuWxkhZ3cfDGDnGd) | → 提取 | `3-Resources/Tech/知识卡片/RTK设备局域网WiFi使用文档.md` |
| 树莓派SSD版本安装.md | [[4-Archives/Notes/Feishu/知识库/技术分享/硬件相关文档/树莓派SSD版本安装]] | [飞书](https://reliablesense.feishu.cn/docx/YUSVdEwLVooPMHx3luMcAXh6nlh) | → 提取 | `3-Resources/Tech/知识卡片/树莓派SSD版本安装.md` |
| 烧写设备.md | [[4-Archives/Notes/Feishu/知识库/技术分享/硬件相关文档/烧写设备]] | [飞书](https://reliablesense.feishu.cn/docx/NigodFqlcowXQVxYWh5cVyoDn2g) | → 提取 | `3-Resources/Tech/知识卡片/烧写设备.md` |
| 日常运维相关文档.md | [[4-Archives/Notes/Feishu/知识库/技术分享/日常运维相关文档]] | [飞书](https://reliablesense.feishu.cn/doc/doccnlJ8hk4ih92ZXrCFLFc9Zid) | → 提取 | `3-Resources/Tech/代码片段/日常运维相关文档.md` |

### 9b. 项目管理

| 文件 | 本地路径 | 决策 | 目标路径 |
|------|---------|------|---------|
| 团队会议.md | [[4-Archives/Notes/Feishu/知识库/项目管理/团队会议]] | → 提取 | `2-Areas/Work/团队管理/团队会议模板.md` |
| 团队周会.md | [[4-Archives/Notes/Feishu/知识库/项目管理/团队周会]] | → 提取 | `2-Areas/Work/团队管理/团队周会模板.md` |
| 文档模版.md | [[4-Archives/Notes/Feishu/知识库/项目管理/文档模版]] | → 提取 | `2-Areas/Work/业务管理/文档模版.md` |
| 每日进展同步.md | [[4-Archives/Notes/Feishu/知识库/项目管理/每日进展同步]] | → 提取 | `2-Areas/Work/团队管理/每日进展同步模板.md` |
| 项目启动.md | [[4-Archives/Notes/Feishu/知识库/项目管理/项目启动]] | → 提取 | `2-Areas/Work/业务管理/项目启动模板.md` |
| 项目复盘.md | [[4-Archives/Notes/Feishu/知识库/项目管理/项目复盘]] | → 提取 | `2-Areas/Work/业务管理/项目复盘模板.md` |
| 项目规划.md | [[4-Archives/Notes/Feishu/知识库/项目管理/项目规划]] | → 提取 | `2-Areas/Work/业务管理/项目规划模板.md` |

### 9c. 规章制度

| 文件 | 本地路径 | 决策 | 目标路径 |
|------|---------|------|---------|
| 人力资源制度.md | [[4-Archives/Notes/Feishu/知识库/规章制度/人力资源制度]] | → 提取 | `2-Areas/Work/团队管理/人力资源制度.md` |
| 人力资源制度/ 子目录 | [[4-Archives/Notes/Feishu/知识库/规章制度/人力资源制度/]] | → 提取 | `2-Areas/Work/团队管理/人力资源制度/` |
| 公关制度.md | [[4-Archives/Notes/Feishu/知识库/规章制度/公关制度]] | → 提取 | `2-Areas/Work/综合管理/公关制度.md` |
| 法务制度.md | [[4-Archives/Notes/Feishu/知识库/规章制度/法务制度]] | → 提取 | `2-Areas/Work/综合管理/法务制度.md` |
| 财务制度.md | [[4-Archives/Notes/Feishu/知识库/规章制度/财务制度]] | → 提取 | `2-Areas/Work/综合管理/财务制度.md` |
| 采购制度.md | [[4-Archives/Notes/Feishu/知识库/规章制度/采购制度]] | → 提取 | `2-Areas/Work/综合管理/采购制度.md` |

### 9d. 个人知识库

| 文件 | 本地路径 | 飞书链接 | 决策 | 目标路径 |
|------|---------|---------|------|---------|
| Iot接口对接代码.md | [[4-Archives/Notes/Feishu/知识库/个人知识库/Iot接口对接代码]] | [飞书](https://reliablesense.feishu.cn/wiki/PJMvwq7JFipjUIkquXpcVEt2nUf) | → 提取 | `3-Resources/Tech/代码片段/IoT接口对接代码.md` |
| Rocket命令行测试.md | [[4-Archives/Notes/Feishu/知识库/个人知识库/Rocket命令行测试]] | [飞书](https://reliablesense.feishu.cn/wiki/NECEwJ2pUienKZkrcsRc6Pranyg) | → 提取 | `3-Resources/Tech/代码片段/RocketMQ命令行测试.md` |
| 订阅压线事件.md | [[4-Archives/Notes/Feishu/知识库/个人知识库/订阅压线事件]] | [飞书](https://reliablesense.feishu.cn/wiki/UwMHwNSUxie9kNkrqVwc0SwOnKe) | → 提取 | `3-Resources/Tech/知识卡片/订阅压线事件.md` |
| 车载定位连调总结.md | [[4-Archives/Notes/Feishu/知识库/个人知识库/车载定位连调总结]] | [飞书](https://reliablesense.feishu.cn/wiki/I7C8w9kEBiLR3YkaRyJcbekunVf) | → 提取 | `3-Resources/Tech/知识卡片/车载定位连调总结.md` |
| 重定位.md | [[4-Archives/Notes/Feishu/知识库/个人知识库/重定位]] | [飞书](https://reliablesense.feishu.cn/wiki/EcASw46qMijgXFkNqQZcWstJnWe) | → 提取 | `3-Resources/Tech/知识卡片/重定位.md` |
| 南宁机场2025年12月26日.md | [[4-Archives/Notes/Feishu/知识库/个人知识库/南宁机场2025年12月26日]] | [飞书](https://reliablesense.feishu.cn/wiki/SLcMwfrKlibIwqkwU6ccaTVZnIc) | → 提取 | `1-Projects/Work/南宁机场/南宁机场记录.md` |
| 工作交接.md | [[4-Archives/Notes/Feishu/知识库/个人知识库/工作交接]] | - | 留归档 | 个人工作交接 |
| 测试总结.md | [[4-Archives/Notes/Feishu/知识库/个人知识库/测试总结]] | - | 留归档 | 测试记录 |
| 运行有问题的项目及其结果截图.md | [[4-Archives/Notes/Feishu/知识库/个人知识库/运行有问题的项目及其结果截图]] | - | 留归档 | 临时记录 |
| 知识问答-Space7527246326739157011.md | [[4-Archives/Notes/Feishu/知识库/个人知识库/知识问答-Space7527246326739157011]] | - | 留归档 | 飞书 AI 问答 |
| 知识问答-Space7527250303092015107.md | [[4-Archives/Notes/Feishu/知识库/个人知识库/知识问答-Space7527250303092015107]] | - | 留归档 | 飞书 AI 问答 |
| 视频会议助手与陈子杰的会话.md | [[4-Archives/Notes/Feishu/知识库/个人知识库/视频会议助手与陈子杰的会话]] | - | 留归档 | 会议记录 |
| 费用报销单.xlsx | [[4-Archives/Notes/Feishu/知识库/个人知识库/费用报销单.xlsx]] | - | 留归档 | 个人财务 |

### 9e. 受限知识库

| 文件 | 本地路径 | 飞书链接 | 决策 | 目标路径 |
|------|---------|---------|------|---------|
| Map-mobile-v2.7版本更新报告.md | [[4-Archives/Notes/Feishu/知识库/受限知识库/Map-mobile-v2.7版本更新报告]] | [飞书](https://reliablesense.feishu.cn/wiki/WiJ2wFB10iQ98skKC4lcgQgqn9b) | → 提取 | `2-Areas/Work/产品研发/Map-mobile-v2.7更新报告.md` |
| 前端Admin-2.7更新内容.md | [[4-Archives/Notes/Feishu/知识库/受限知识库/前端Admin-2.7更新内容]] | [飞书](https://reliablesense.feishu.cn/wiki/OaQpwHMvhiduTDk5lBqcluCfnPf) | → 提取 | `2-Areas/Work/产品研发/前端Admin-2.7更新内容.md` |
| 后端2.7更新内容.md | [[4-Archives/Notes/Feishu/知识库/受限知识库/后端2.7更新内容]] | [飞书](https://reliablesense.feishu.cn/wiki/AYprwPzeGiWaPlkUnVxcQWbMndc) | → 提取 | `2-Areas/Work/产品研发/后端2.7更新内容.md` |
| 新太元验收标准总结.md | [[4-Archives/Notes/Feishu/知识库/受限知识库/新太元验收标准总结]] | [飞书](https://reliablesense.feishu.cn/wiki/LbYbwPb1QidoL0kpKakcRhCrnPe) | → 提取 | `4-Archives/Projects/Work/内蒙新太/验收标准总结.md` |
| 新太项目总结.md | [[4-Archives/Notes/Feishu/知识库/受限知识库/新太项目总结]] | [飞书](https://reliablesense.feishu.cn/wiki/TK3Sw7sNkiEFD1kFx27cLTkznAV) | → 提取 | `4-Archives/Projects/Work/内蒙新太/项目总结.md` |
| 2025年年终总结-后端.md | [[4-Archives/Notes/Feishu/知识库/受限知识库/2025年年终总结-后端]] | [飞书](https://reliablesense.feishu.cn/wiki/ZSDawo3uLi4lxXkGZP7cHGxBnXc) | 留归档 | 年终总结 |
| 2025年度总结-前端.md | [[4-Archives/Notes/Feishu/知识库/受限知识库/2025年度总结-前端]] | [飞书](https://reliablesense.feishu.cn/wiki/MqWawqoYkiJsQekf1y2c8Hatnve) | 留归档 | 年终总结 |
| 刘远达25年年终总结.md | [[4-Archives/Notes/Feishu/知识库/受限知识库/刘远达25年年终总结]] | [飞书](https://reliablesense.feishu.cn/wiki/TfMYwzD5citiR0kXrffcRYNUn8d) | 留归档 | 年终总结 |

---

## 十、需要新建的 PARA 目录

```
3-Resources/Tech/环境配置/
3-Resources/Tech/环境配置/集群/
2-Areas/Work/业务管理/售前项目/
2-Areas/Work/业务管理/商业计划书/
2-Areas/Work/业务管理/项目评估/
2-Areas/Work/品牌宣传/品牌手册/
2-Areas/Work/品牌宣传/公司介绍/
2-Areas/Work/品牌宣传/英文资料/
2-Areas/Work/品牌宣传/PPT模版/
2-Areas/Work/品牌宣传/名片/
2-Areas/Work/品牌宣传/宣传物料/
2-Areas/Work/团队管理/招聘/
2-Areas/Work/综合管理/ISO9001/
```

---

## 十一、迁移统计预估

| 类别 | 预估文件数 | 说明 |
|------|----------|------|
| → 提取到 3-Resources/Tech/ | ~80 个 .md | 代码片段、知识卡片、设计方案、环境配置 |
| → 提取到 3-Resources/Business/ | ~50 个 .md + .pptx | 23 个行业解决方案 |
| → 提取到 2-Areas/Work/ | ~40 个 .md | 制度、模板、品牌宣传、团队管理 |
| → 提取到 1-Projects/Work/ | ~30 个 .md | 进行中项目的技术文档 |
| → 归档到 4-Archives/Projects/Work/ | ~90 个项目目录 | 已结束项目 |
| 留归档不动 | ~5000+ 个文件 | 会议纪要、附件、表格、临时文件 |

---

## 十二、执行顺序建议

1. 先创建所有需要新建的目录结构
2. 按优先级分批提取：
   - **第一批**：项目运维管理（代码片段、环境配置）
   - **第二批**：项目开发管理（设计方案）
   - **第三批**：知识库/技术分享
   - **第四批**：进行中项目资料
   - **第五批**：公司内部资料、规章制度
   - **第六批**：解决方案管理
   - **第七批**：已结束项目归档

---

## 十三、待确认事项

1. **参考/ 目录**：公司内部资料下的"参考"和莱讯科技下的"~参考资料"，需逐个查看
2. **定制版项目子目录**：14 个定制化项目子目录，需逐个确认是否已结束
3. **企业版/文档资料/ 子目录**：需查看具体内容
4. **路网维护/**：如有 .md 格式路网说明文档，需按项目归属分配
5. **售前项目/ 下 5 个客户目录**：需确认是否有正式立项
