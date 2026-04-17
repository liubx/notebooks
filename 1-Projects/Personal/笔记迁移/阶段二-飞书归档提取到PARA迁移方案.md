---
title: 阶段二-飞书归档提取到PARA迁移方案
type: design-doc
tags:
  - project/笔记迁移
created: 2026-04-11
---

# 阶段二：飞书归档提取到 PARA 迁移方案

基于 `4-Archives/Notes/Feishu/` 中已拉取的全量内容，逐文件审查后制定的迁移策略。

> ⚠️ 部分文件的目标路径尚未确定（主要是 `3-Resources/Tech/` 与 `2-Areas/Work/` 的边界），详见 [[1-Projects/Personal/笔记迁移/阶段二-待确认分类]]。确认后再移入本文档。

## 迁移原则

1. 只提取有持续参考价值的内容到 PARA，一次性/过时的按以下规则处理：
   - **有归属的** → 移到 `4-Archives/` 下对应分类目录（如 `4-Archives/Areas/Work/团队管理/团队成员/{姓名}/`、`4-Archives/Projects/Work/{项目}/` 等），不留在 Notes 里
   - **真正无用的**（无上下文临时文件、飞书模板等）→ 留 `4-Archives/Notes/Feishu/` 原位不动
   - 原则：`4-Archives/Notes/` 目录以后可能整体移走，有价值的归档内容不应留在里面
2. 会议纪要、智能纪要 → 按内容归入对应项目或团队管理目录；近期会议速递、月度纪要小结 → 按所属同事归入 `4-Archives/Areas/Work/团队管理/团队成员/{姓名}/`
3. 年终总结、工作周报 → 按所属同事归入团队成员目录
4. 同一文档有多个副本的，只提取最新/最完整版本
5. file 类型附件（上传的 .docx/.xlsx/.pptx/.pdf 等）→ 跟随所在目录规则决策，无明确归属的留原位
6. README.md 索引文件、链接索引.md → 留原位不动（仅供归档索引用）
7. bitable 导出的 .xlsx → 留原位不动（原始 bitable 数据已按目录规则处理）
8. 进行中项目的资料提取到 `1-Projects/Work/对应项目/`
9. 已结束项目整体归档到 `4-Archives/Projects/Work/`
10. 同事个人文档中不属于特定项目的内容（AI汇总、工作总结、散落文件等）→ 按人归类到团队成员目录：
    - 在职：`2-Areas/Work/团队管理/团队成员/{姓名}/`
    - 已离职：`4-Archives/Areas/Work/团队管理/团队成员/{姓名}/`
    - 属于特定项目的文件仍然跟项目走，不放团队成员目录
11. 文档内嵌图片（`Attachments/` 目录下的 .png/.jpg 等）跟随所属文档移动到目标路径的 `Attachments/` 子目录，不单独决策

---

## 一、云空间/根目录（散落文件）

| 文件 | 本地路径 | 飞书链接 | 决策 | 目标路径 | 理由 |
|------|---------|---------|------|---------|------|
| API.md | [[4-Archives/Notes/Feishu/云空间/根目录/API]] | [飞书](https://reliablesense.feishu.cn/docx/NoXpdv9A1oSb4gxwWDmciKajnOJ) | → 提取 | `1-Projects/Work/上港仓储管理/WMS-API接口文档.md` | 上港项目的 WMS 对接接口，跟项目走 |
| 墨水屏数据协议.md | [[4-Archives/Notes/Feishu/云空间/根目录/墨水屏数据协议]] | [飞书](https://reliablesense.feishu.cn/docx/P4z0dkpVUoq3jwxUvBtcrRpundd) | → 提取 | `2-Areas/Work/设备管理/墨水屏数据协议.md` | 设备协议文档，归设备管理 |
| 系统架构图.md | [[4-Archives/Notes/Feishu/云空间/根目录/系统架构图]] | [飞书](https://reliablesense.feishu.cn/docx/IYLtdtwDQoaOetxP9Xkc66jfnPf) | → 提取 | `1-Projects/Work/广州机场/综合定位系统架构图.md` | 含"综合定位系统"，归广州机场 |
| 系统整改配置表.md | [[4-Archives/Notes/Feishu/云空间/根目录/系统整改配置表]] | [飞书](https://reliablesense.feishu.cn/docx/ZpsNdChggodbeaxLg78cgtRBnGc) | → 提取 | `1-Projects/Work/广州机场/系统整改配置表.md` | 含 A域/B域、巡检app，属广州机场项目 |
| deploy.yaml | [[4-Archives/Notes/Feishu/云空间/根目录/deploy.yaml]] | [飞书](https://reliablesense.feishu.cn/file/RwsBbb50NoKUaKxeVutcaFWBnVd) | → 归档 | `4-Archives/Projects/Work/赛峰/deploy-sso.yaml` | 赛峰项目 SAML2/SSO 配置 |
| Doc2.docx | [[4-Archives/Notes/Feishu/云空间/根目录/Doc2.docx]] | [飞书](https://reliablesense.feishu.cn/file/VvsMbbh4OoziMkxwQGTcUXwMnYf) | → 归档 | `4-Archives/Projects/Work/中东电子厂/Doc2-波斯语翻译.docx` | 伊朗项目 UI 翻译 |
| 优化后.txt | [[4-Archives/Notes/Feishu/云空间/根目录/优化后.txt]] | [飞书](https://reliablesense.feishu.cn/file/OuyFbuM1touvroxyPjEcki2on0d) | 留归档 | - | 无上下文的临时文件 |
| map-mobile.mm | [[4-Archives/Notes/Feishu/云空间/根目录/map-mobile.mm]] | [飞书](https://reliablesense.feishu.cn/mindnotes/G7S6b8VC3mxDsPnZ1yDc4XItn2d) | → 提取 | `2-Areas/Work/产品研发/map-mobile参数设置.mm` | 手机端网页（小程序/APP嵌入）参数设置思维导图 |
| map-model.mm | [[4-Archives/Notes/Feishu/云空间/根目录/map-model.mm]] | [飞书](https://reliablesense.feishu.cn/mindnotes/ZVgJbqGpTmw5v9nD5vTcqEg8nfe) | → 提取 | `2-Areas/Work/产品研发/map-model参数设置.mm` | 地图模型参数设置思维导图 |
| rssi数据.docx | [[4-Archives/Notes/Feishu/云空间/根目录/rssi数据.docx]] | [飞书](https://reliablesense.feishu.cn/file/WElAbEGxJoExttxZa90cDTeyn1X) | → 提取 | `2-Areas/Work/设备管理/rssi数据.docx` | 基站坐标和 RSSI 信号测试数据 |
| SaaS平台操作手册V7.docx | [[4-Archives/Notes/Feishu/云空间/根目录/SaaS平台操作手册V7.docx]] | [飞书](https://reliablesense.feishu.cn/file/Krurb4Ew6okF4jxUP8BcDru3nUf) | → 提取 | `2-Areas/Work/产品研发/SaaS平台操作手册V7.docx` | 产品平台操作手册 |
| 快速启用，属于你的任务管理系统.md | [[4-Archives/Notes/Feishu/云空间/根目录/快速启用，属于你的任务管理系统]] | [飞书](https://reliablesense.feishu.cn/docx/X8Y8dLsjZo5wSuxGMu9cc7AAnGf) | 留归档 | - | 飞书模板文档 |
| 研发部的视频会议 2024年11月22日.md | [[4-Archives/Notes/Feishu/云空间/根目录/研发部的视频会议 2024年11月22日]] | [飞书](https://reliablesense.feishu.cn/docx/Vu8Nd0VN1ovfrOxpvDzcHcO5nSf) | → 归档 | `2-Areas/Work/团队管理/早会纪要/2024/11/` | 大部分内容属于洛阳项目 |
| 移动应用 - 监控 2025年5月13日.md | [[4-Archives/Notes/Feishu/云空间/根目录/移动应用 - 监控 2025年5月13日]] | [飞书](https://reliablesense.feishu.cn/docx/GBCkdfZNVor1Lcxgs4AcSIZonMe) | 留归档 | - | 临时监控记录 |
| 翻译.docx | [[4-Archives/Notes/Feishu/云空间/根目录/翻译.docx]] | [飞书](https://reliablesense.feishu.cn/file/FoTYbNSjwoE1trxSOvWce7rxntf) | → 归档 | `4-Archives/Projects/Work/中东电子厂/翻译.docx` | 伊朗项目翻译文件 |
| 认证文件.zip | [[4-Archives/Notes/Feishu/云空间/根目录/认证文件.zip]] | [飞书](https://reliablesense.feishu.cn/file/GCxtbICnZo5X1QxwnzfcMzErnGf) | → 提取 | `2-Areas/Work/综合管理/软著立项/认证文件.zip` | 软著和ISO质量检测认证文件 |
| 综合定位系统-深化设计方案.docx | [[4-Archives/Notes/Feishu/云空间/根目录/综合定位系统-深化设计方案.docx]] | [飞书](https://reliablesense.feishu.cn/file/OVHGbClJOoavkLx3gStcUVGAngh) | → 提取 | `1-Projects/Work/广州机场/综合定位系统-深化设计方案.docx` | 含"综合定位系统"，属广州机场 |
| 14号夜班差异分析.xlsx | [[4-Archives/Notes/Feishu/云空间/根目录/14号夜班差异分析.xlsx]] | [飞书](https://reliablesense.feishu.cn/file/JXLib9uFkoA5F3xWLfxcD2jlnKf) | → 提取 | `1-Projects/Work/新太项目/14号夜班差异分析.xlsx` | 新太项目 |
| 5.20日洛阳石化系统bug问题汇总.xlsx | [[4-Archives/Notes/Feishu/云空间/根目录/5.20日洛阳石化系统bug问题汇总.xlsx]] | [飞书](https://reliablesense.feishu.cn/file/YUCNbnhyMooytWxAZVZcntx4nff) | → 归档 | `1-Projects/Work/洛阳化工厂/5.20日洛阳石化系统bug问题汇总.xlsx` | 洛阳项目 BUG 汇总 |
| MAC-Address.xlsx | [[4-Archives/Notes/Feishu/云空间/根目录/MAC-Address.xlsx]] | [飞书](https://reliablesense.feishu.cn/file/MFjsbb7bBoHIr5xo4v7c95kqnvb) | → 提取 | `2-Areas/Work/设备管理/MAC-Address.xlsx` | 设备 MAC 地址表 |
| 员工花名册-在职.xlsx | [[4-Archives/Notes/Feishu/云空间/根目录/员工花名册-在职.xlsx]] | [飞书](https://reliablesense.feishu.cn/sheets/HQsEseKUKhovu0t1ewnclLSAnte) | → 提取 | `1-Projects/Work/广州机场/员工花名册-在职.xlsx` | 机场导入数据 |
| 周报测试.xlsx | [[4-Archives/Notes/Feishu/云空间/根目录/周报测试.xlsx]] | [飞书](https://reliablesense.feishu.cn/base/NepGb0sWdaPfnosidcMc7yspnFg) | → 提取 | `2-Areas/Work/团队管理/周报提交记录.xlsx` | 周报提交记录 |
| 定位对象在线时长导出表.xlsx | [[4-Archives/Notes/Feishu/云空间/根目录/定位对象在线时长导出表.xlsx]] | [飞书](https://reliablesense.feishu.cn/sheets/W95RsJ1SahTaeJt0xDgcM4d6n7f) | → 提取 | `2-Areas/Work/产品研发/定位对象在线时长导出表.xlsx` | 产品数据导出模板 |
| 广州市公办小学招生报名系统入学申请表.xls | [[4-Archives/Notes/Feishu/云空间/根目录/广州市公办小学招生报名系统入学申请表.xls]] | [飞书](https://reliablesense.feishu.cn/file/T41fbSI4xoRMTJxtiWkctSUxnvp) | 留归档 | - | 个人文件 |
| 广州机场综合定位.xlsx | [[4-Archives/Notes/Feishu/云空间/根目录/广州机场综合定位.xlsx]] | [飞书](https://reliablesense.feishu.cn/base/NbIPbswwSaCfPpsWak7cbCHsnwe) | → 提取 | `1-Projects/Work/广州机场/广州机场综合定位.xlsx` | 广州机场项目数据 |
| 数字化.xlsx | [[4-Archives/Notes/Feishu/云空间/根目录/数字化.xlsx]] | [飞书](https://reliablesense.feishu.cn/file/E1b4biPmsoA4Ztx5Zj8c7CC0n6q) | → 提取 | `1-Projects/Work/新太项目/数字化措施表.xlsx` | 新太项目数字化改造措施（堆垛、铲车、料坑） |
| 红柳林筛分楼部署内容.xlsx | [[4-Archives/Notes/Feishu/云空间/根目录/红柳林筛分楼部署内容.xlsx]] | [飞书](https://reliablesense.feishu.cn/sheets/shtcnuIgoeyPvXu60pwR4XsEc1g) | → 归档 | `1-Projects/Work/麦钉项目/红柳林筛分楼部署内容.xlsx` | 红柳林项目 |
| 综合定位系统功能清单.xlsx | [[4-Archives/Notes/Feishu/云空间/根目录/综合定位系统功能清单.xlsx]] | [飞书](https://reliablesense.feishu.cn/file/JV2ibGyG9oVohcxlBwJcQdbenJe) | → 提取 | `1-Projects/Work/广州机场/综合定位系统功能清单.xlsx` | 广州机场功能清单 |
| 广州白云国际机场三期扩建项目-综合定位-接口规范-V1.0.2.docx | [[4-Archives/Notes/Feishu/云空间/根目录/广州白云国际机场三期扩建项目-综合定位-接口规范-V1.0.2.docx]] | [飞书](https://reliablesense.feishu.cn/file/UGbJbaqiUoWBJaxH4Hpc9totngd) | → 提取 | `1-Projects/Work/广州机场/接口规范-V1.0.2.docx` | 广州机场接口规范 |
| 智慧仓储物流早会汇报v1.5.pptx | [[4-Archives/Notes/Feishu/云空间/根目录/智慧仓储物流早会汇报v1.5.pptx]] | [飞书](https://reliablesense.feishu.cn/file/QeNlbb8xyoOSVPxfVMgcR8uCnKc) | → 提取 | `1-Projects/Work/新太项目/智慧仓储物流早会汇报v1.5.pptx` | 新太项目汇报 |

> **归类规则补充**：
> - 项目相关的接口/技术文档 → 跟对应项目走（`1-Projects/Work/` 或 `4-Archives/Projects/Work/`），不放通用 Tech 目录
> - 设备协议类文档 → `2-Areas/Work/设备管理/`
> - 产品架构文档（系统架构图、概要设计等描述产品整体的） → `2-Areas/Work/产品研发/`
> - 含"综合定位"、"A域/B域"、"巡检app"等广州机场特征关键词的文档 → `1-Projects/Work/广州机场/`
> - 含"新太"、"料棚"、"新钢联"等关键词的文档 → `1-Projects/Work/新太项目/`
> - 含"红柳林"、"李家壕"、"韩家村"、"高安屯"、"柠条塔"、"madinat_hll"、"madinat_xmc"、"madinat_hjc"、"madinat_gat"、"madinat_ntt" → `1-Projects/Work/麦钉项目/`

---

## 二、云空间/散落的会议纪要和飞书 AI 生成内容

256 个会议纪要文件，根据内容分类后归入对应位置。详细文件列表见 [[1-Projects/Personal/笔记迁移/会议纪要分类结果]]。

### 分类统计

| 分类 | 数量 | 目标路径 |
|------|------|---------|
| 新太项目会议 | 23 | `1-Projects/Work/新太项目/会议纪要/` |
| 广州机场会议 | 12 | `1-Projects/Work/广州机场/会议纪要/` |
| 上港项目会议 | 2 | `1-Projects/Work/上港仓储管理/会议纪要/` |
| 武汉机场会议 | 3 | `4-Archives/Projects/Work/武汉机场/会议纪要/` |
| 洛阳化工厂会议 | 1 | `1-Projects/Work/洛阳化工厂/会议纪要/` |
| 研发部早会 | 36 | `2-Areas/Work/团队管理/早会纪要/` |
| 项目部周会 | 18 | `2-Areas/Work/团队管理/周会纪要/项目部/` |
| 项目进度会（刘秉欣） | 35 | `2-Areas/Work/团队管理/周会纪要/` |
| 技术讨论 | 6 | `3-Resources/Tech/问题解决/` |
| 待确认 | 36 | 需人工判断 |
| 留归档（AI 汇总） | 84 | 近期会议速递、月度纪要小结，按所属同事归入团队成员目录 |

### 分类规则

| 会议类型 | 判断依据 |
|---------|---------|
| 新太项目 | 标题/内容含"新太"、"新钢联"、"料棚"、"卸料"、"上料"、"铲车"、"堆垛" |
| 广州机场 | 标题/内容含"综合定位"、"A域/B域"、"电子围栏"、"AESB"、"TCDM" |
| 上港项目 | 标题/内容含"仓储"、"出入库"、"RFID" |
| 研发部早会 | 标题含"研发部的视频会议"或"Video meeting—研发部" |
| 项目部周会 | 标题含"项目部的视频会议"或"Video meeting—项目部" |
| 项目进度会 | 标题含"刘秉欣" |
| 研发部早会 | 会议时间在 08:45-09:30 左右 |
| 技术讨论 | 内容含"Beacon"、"CLE"、"launchable"、"墨水屏" |

> 会议纪要分类后可用于补全对应日期的日记（`0-Daily/`）。
> 同一场会议的"智能纪要"和"文字记录"归到同一位置。
> 研发部早会每天开会后移入 `2-Areas/Work/团队管理/早会纪要/{年}/{月}/`，并将内容记录到当天日记。
> 分类脚本：`scripts/classify-meetings.py`

### 详细文件列表

#### 新太项目（34 个）

| 文件 | 本地路径 | 飞书链接 | 目标路径 |
|------|---------|---------|---------|
| 内蒙新太项目（新钢联）的视频会议 2025年2月20日 - 智能纪要.md | [[4-Archives/Notes/Feishu/云空间/内蒙新太项目（新钢联）的视频会议 2025年2月20日 - 智能纪要]] | [飞书](https://reliablesense.feishu.cn/docx/KYotdrd3iovBS6xtsLFcrpl7nOb) | `1-Projects/Work/新太项目/会议纪要/` |
| 文字记录：上料 APP 及卸货问题研讨会  2025年4月10日.md | [[4-Archives/Notes/Feishu/云空间/文字记录：上料 APP 及卸货问题研讨会  2025年4月10日]] | [飞书](https://reliablesense.feishu.cn/docx/Q02Gd51NFov3FlxnOpgcfUe0n2d) | `1-Projects/Work/新太项目/会议纪要/` |
| 文字记录：五人工作安排与系统问题会议 2025年4月8日.md | [[4-Archives/Notes/Feishu/云空间/文字记录：五人工作安排与系统问题会议 2025年4月8日]] | [飞书](https://reliablesense.feishu.cn/docx/DDIddzu4uorHx3xVcmPc8d7Wnih) | `1-Projects/Work/新太项目/会议纪要/` |
| 文字记录：内蒙新太项目（新钢联）的视频会议 2025年2月20日.md | [[4-Archives/Notes/Feishu/云空间/文字记录：内蒙新太项目（新钢联）的视频会议 2025年2月20日]] | [飞书](https://reliablesense.feishu.cn/docx/Qdl2dygpBoeSexx0CEzcjhsFnNf) | `1-Projects/Work/新太项目/会议纪要/` |
| 文字记录：内蒙新太项目（新钢联）的视频会议 2025年2月26日.md | [[4-Archives/Notes/Feishu/云空间/文字记录：内蒙新太项目（新钢联）的视频会议 2025年2月26日]] | [飞书](https://reliablesense.feishu.cn/docx/Pt9ydazeCozgTCxOleBcBkWnnzd) | `1-Projects/Work/新太项目/会议纪要/` |
| 文字记录：卸货条件设定及测试问题研讨 2025年4月17日.md | [[4-Archives/Notes/Feishu/云空间/文字记录：卸货条件设定及测试问题研讨 2025年4月17日]] | [飞书](https://reliablesense.feishu.cn/docx/TKuQdMeP9oG3HExLFz3cAFrknje) | `1-Projects/Work/新太项目/会议纪要/` |
| 文字记录：多项工作安排与检查会议  2025年5月8日.md | [[4-Archives/Notes/Feishu/云空间/文字记录：多项工作安排与检查会议  2025年5月8日]] | [飞书](https://reliablesense.feishu.cn/docx/ThZ5dZTgGofFRLxZibRcQm7mnBc) | `1-Projects/Work/新太项目/会议纪要/` |
| 文字记录：导航程序测试问题研讨会 2025年4月10日.md | [[4-Archives/Notes/Feishu/云空间/文字记录：导航程序测试问题研讨会 2025年4月10日]] | [飞书](https://reliablesense.feishu.cn/docx/GLSldDcEWoCwNOxaGlBcB86znwd) | `1-Projects/Work/新太项目/会议纪要/` |
| 文字记录：小程序堆垛定位路线问题会议 2025年4月22日.md | [[4-Archives/Notes/Feishu/云空间/文字记录：小程序堆垛定位路线问题会议 2025年4月22日]] | [飞书](https://reliablesense.feishu.cn/docx/BECFddgmZobgXGxpjZqcnPGRnwf) | `1-Projects/Work/新太项目/会议纪要/` |
| 文字记录：平板使用问题及解决措施研讨 2025年4月7日.md | [[4-Archives/Notes/Feishu/云空间/文字记录：平板使用问题及解决措施研讨 2025年4月7日]] | [飞书](https://reliablesense.feishu.cn/docx/KmwodbUhLokRuAxjmCWce9IHn5d) | `1-Projects/Work/新太项目/会议纪要/` |
| 文字记录：跑步速度与通知次数安排会议  2025年4月10日.md | [[4-Archives/Notes/Feishu/云空间/文字记录：跑步速度与通知次数安排会议  2025年4月10日]] | [飞书](https://reliablesense.feishu.cn/docx/ItNldtWzZolX9NxW28Tcr3tFnVf) | `1-Projects/Work/新太项目/会议纪要/` |
| 文字记录：项目工作进展与规划会议纪要  2025年5月6日.md | [[4-Archives/Notes/Feishu/云空间/文字记录：项目工作进展与规划会议纪要  2025年5月6日]] | [飞书](https://reliablesense.feishu.cn/docx/DsJ3dv1Jwo7jXHxNSyZckJz6nve) | `1-Projects/Work/新太项目/会议纪要/` |
| 智能纪要：上料 APP 及卸货问题研讨会 2025年4月10日.md | [[4-Archives/Notes/Feishu/云空间/智能纪要：上料 APP 及卸货问题研讨会 2025年4月10日]] | [飞书](https://reliablesense.feishu.cn/docx/BgwNddiWwouTVAxTA3wcb982nRh) | `1-Projects/Work/新太项目/会议纪要/` |
| 智能纪要：五人工作安排与系统问题会议 2025年4月8日.md | [[4-Archives/Notes/Feishu/云空间/智能纪要：五人工作安排与系统问题会议 2025年4月8日]] | [飞书](https://reliablesense.feishu.cn/docx/TiYHdhhLMoGcIhxLTEKcT3MKnqe) | `1-Projects/Work/新太项目/会议纪要/` |
| 智能纪要：内蒙新太项目（新钢联）的视频会议 2025年2月26日.md | [[4-Archives/Notes/Feishu/云空间/智能纪要：内蒙新太项目（新钢联）的视频会议 2025年2月26日]] | [飞书](https://reliablesense.feishu.cn/docx/ZLRHd5XrUoztV0xtcXucyWZMnrb) | `1-Projects/Work/新太项目/会议纪要/` |
| 智能纪要：卸货条件设定及测试问题研讨 2025年4月17日.md | [[4-Archives/Notes/Feishu/云空间/智能纪要：卸货条件设定及测试问题研讨 2025年4月17日]] | [飞书](https://reliablesense.feishu.cn/docx/UHRbdu9XLoa9PUxi2szcKHAinPb) | `1-Projects/Work/新太项目/会议纪要/` |
| 智能纪要：多项工作安排与检查会议 2025年5月8日.md | [[4-Archives/Notes/Feishu/云空间/智能纪要：多项工作安排与检查会议 2025年5月8日]] | [飞书](https://reliablesense.feishu.cn/docx/AawEdXIyAo7h2XxcMoUcWvGbnBc) | `1-Projects/Work/新太项目/会议纪要/` |
| 智能纪要：导航程序测试问题研讨会 2025年4月10日.md | [[4-Archives/Notes/Feishu/云空间/智能纪要：导航程序测试问题研讨会 2025年4月10日]] | [飞书](https://reliablesense.feishu.cn/docx/SMRPdLb1soQz30xhdILcFV0Cnnc) | `1-Projects/Work/新太项目/会议纪要/` |
| 智能纪要：小程序堆垛定位路线问题会议 2025年4月22日.md | [[4-Archives/Notes/Feishu/云空间/智能纪要：小程序堆垛定位路线问题会议 2025年4月22日]] | [飞书](https://reliablesense.feishu.cn/docx/MyVSdaYrtoz7GdxuRcGce2k7nyc) | `1-Projects/Work/新太项目/会议纪要/` |
| 智能纪要：平板使用问题及解决措施研讨 2025年4月7日.md | [[4-Archives/Notes/Feishu/云空间/智能纪要：平板使用问题及解决措施研讨 2025年4月7日]] | [飞书](https://reliablesense.feishu.cn/docx/RGhodDXbEo2X70xK8WLcGZEOnXd) | `1-Projects/Work/新太项目/会议纪要/` |
| 智能纪要：跑步速度与通知次数安排会议 2025年4月10日.md | [[4-Archives/Notes/Feishu/云空间/智能纪要：跑步速度与通知次数安排会议 2025年4月10日]] | [飞书](https://reliablesense.feishu.cn/docx/PZyHddVcpoJOndxfhdscRdC5npe) | `1-Projects/Work/新太项目/会议纪要/` |
| 智能纪要：项目工作进展与规划会议纪要 2025年5月6日.md | [[4-Archives/Notes/Feishu/云空间/智能纪要：项目工作进展与规划会议纪要 2025年5月6日]] | [飞书](https://reliablesense.feishu.cn/docx/BosQdhobYolHEFxRpWdcMbMgnYd) | `1-Projects/Work/新太项目/会议纪要/` |
| 文字记录：内蒙新太项目（新钢联）的视频会议 2025年2月26日.md | [[4-Archives/Notes/Feishu/云空间/王宗光的个人文档/文字记录：内蒙新太项目（新钢联）的视频会议 2025年2月26日]] | [飞书](https://reliablesense.feishu.cn/docx/OgG5dQrQLoGY9FxEchhcSvmknXg) | `1-Projects/Work/新太项目/会议纪要/` |
| 文字记录：内蒙新太项目（新钢联）的视频会议 2025年3月5日.md | [[4-Archives/Notes/Feishu/云空间/王宗光的个人文档/文字记录：内蒙新太项目（新钢联）的视频会议 2025年3月5日]] | [飞书](https://reliablesense.feishu.cn/docx/D0aEdYFlYo9REkxhIrwcDDWCnPf) | `1-Projects/Work/新太项目/会议纪要/` |
| 文字记录：王宗光的视频会议 2025年2月20日.md | [[4-Archives/Notes/Feishu/云空间/王宗光的个人文档/文字记录：王宗光的视频会议 2025年2月20日]] | [飞书](https://reliablesense.feishu.cn/docx/DGyzdAmKkoykTYxVkoxcduRcnCc) | `1-Projects/Work/新太项目/会议纪要/` |
| 文字记录：项目服务、权限及工作进展会议 2025年4月11日.md | [[4-Archives/Notes/Feishu/云空间/王宗光的个人文档/文字记录：项目服务、权限及工作进展会议 2025年4月11日]] | [飞书](https://reliablesense.feishu.cn/docx/KoC5dKi6koHwTfx8Dkbcgrlon5g) | `1-Projects/Work/新太项目/会议纪要/` |
| 智能纪要：内蒙新太项目（新钢联）的视频会议 2025年2月26日.md | [[4-Archives/Notes/Feishu/云空间/王宗光的个人文档/智能纪要：内蒙新太项目（新钢联）的视频会议 2025年2月26日]] | [飞书](https://reliablesense.feishu.cn/docx/IQUqdVOipoy6MUx9pYicAUvrnmd) | `1-Projects/Work/新太项目/会议纪要/` |
| 智能纪要：内蒙新太项目（新钢联）的视频会议 2025年3月5日.md | [[4-Archives/Notes/Feishu/云空间/王宗光的个人文档/智能纪要：内蒙新太项目（新钢联）的视频会议 2025年3月5日]] | [飞书](https://reliablesense.feishu.cn/docx/EePFdqlyQoh4bExphrXcGX3Wnjd) | `1-Projects/Work/新太项目/会议纪要/` |
| 智能纪要：多方面业务问题及解决方案探讨会 2025年6月3日.md | [[4-Archives/Notes/Feishu/云空间/王宗光的个人文档/智能纪要：多方面业务问题及解决方案探讨会 2025年6月3日]] | [飞书](https://reliablesense.feishu.cn/docx/NPkFdqGfUo1Bf2xEQOGclc7anMh) | `1-Projects/Work/新太项目/会议纪要/` |
| 智能纪要：项目服务、权限及工作进展会议 2025年4月11日.md | [[4-Archives/Notes/Feishu/云空间/王宗光的个人文档/智能纪要：项目服务、权限及工作进展会议 2025年4月11日]] | [飞书](https://reliablesense.feishu.cn/docx/LKSodmV6loX04TxtDTNcEqmcnLe) | `1-Projects/Work/新太项目/会议纪要/` |
| 王宗光的视频会议 2025年2月20日 - 智能纪要.md | [[4-Archives/Notes/Feishu/云空间/王宗光的个人文档/王宗光的视频会议 2025年2月20日 - 智能纪要]] | [飞书](https://reliablesense.feishu.cn/docx/Rr23dKQ8vo2vyYxmepgcq5ktn1c) | `1-Projects/Work/新太项目/会议纪要/` |
| 内蒙新太项目（新钢联）的视频会议 2025年2月7日 - 智能纪要.md | [[4-Archives/Notes/Feishu/云空间/陈子杰的个人文档/内蒙新太项目（新钢联）的视频会议 2025年2月7日 - 智能纪要]] | [飞书](https://reliablesense.feishu.cn/docx/W7Jid5OiUopoqcxNqJbc8ichnnf) | `1-Projects/Work/新太项目/会议纪要/` |
| 文字记录：陈子杰的视频会议 2025年2月24日.md | [[4-Archives/Notes/Feishu/云空间/陈子杰的个人文档/文字记录：陈子杰的视频会议 2025年2月24日]] | [飞书](https://reliablesense.feishu.cn/docx/JhwjdqDfJoBMExxV9btciKO3nhf) | `1-Projects/Work/新太项目/会议纪要/` |
| 智能纪要：陈子杰的视频会议 2025年2月24日.md | [[4-Archives/Notes/Feishu/云空间/陈子杰的个人文档/智能纪要：陈子杰的视频会议 2025年2月24日]] | [飞书](https://reliablesense.feishu.cn/docx/XVxUdVtaSo0wu6xtY3Uc7GdHnrc) | `1-Projects/Work/新太项目/会议纪要/` |

#### 广州机场（26 个）

| 文件 | 本地路径 | 飞书链接 | 目标路径 |
|------|---------|---------|---------|
| 文字记录：8084接口、列表及地图问题讨论 2025年10月27日.md | [[4-Archives/Notes/Feishu/云空间/何宜峰的个人文档/文字记录：8084接口、列表及地图问题讨论 2025年10月27日]] | [飞书](https://reliablesense.feishu.cn/docx/LdfpdNSktotC7WxY1nAcoQ0gn5g) | `1-Projects/Work/广州机场/会议纪要/` |
| 文字记录：云江项目任务方案及后续安排会 2025年10月27日.md | [[4-Archives/Notes/Feishu/云空间/何宜峰的个人文档/文字记录：云江项目任务方案及后续安排会 2025年10月27日]] | [飞书](https://reliablesense.feishu.cn/docx/KhyYd0clVo2XuGxNWqrc9pGSnVd) | `1-Projects/Work/广州机场/会议纪要/` |
| 文字记录：分子构建与插件使用安装讨论 2025年11月6日.md | [[4-Archives/Notes/Feishu/云空间/何宜峰的个人文档/文字记录：分子构建与插件使用安装讨论 2025年11月6日]] | [飞书](https://reliablesense.feishu.cn/docx/HrTkdTglAohn1pxSxbfcUGPBnIc) | `1-Projects/Work/广州机场/会议纪要/` |
| 文字记录：数据同步、订阅测试及新数据格式讨论  2025年10月28日.md | [[4-Archives/Notes/Feishu/云空间/何宜峰的个人文档/文字记录：数据同步、订阅测试及新数据格式讨论  2025年10月28日]] | [飞书](https://reliablesense.feishu.cn/docx/UHKEdQ12Mo7q1Wxrw3LchCN7ncb) | `1-Projects/Work/广州机场/会议纪要/` |
| 文字记录：管理内容、分支及注释问题讨论 2025年11月6日.md | [[4-Archives/Notes/Feishu/云空间/何宜峰的个人文档/文字记录：管理内容、分支及注释问题讨论 2025年11月6日]] | [飞书](https://reliablesense.feishu.cn/docx/Pvl3dZTnmo8xyPx3dLjcdFf8nqf) | `1-Projects/Work/广州机场/会议纪要/` |
| 文字记录：管理员数据库表及任务归属问题讨论 2025年10月30日.md | [[4-Archives/Notes/Feishu/云空间/何宜峰的个人文档/文字记录：管理员数据库表及任务归属问题讨论 2025年10月30日]] | [飞书](https://reliablesense.feishu.cn/docx/UfuNdjJLAoTZnaxGRH0c4KAbnwg) | `1-Projects/Work/广州机场/会议纪要/` |
| 文字记录：项目依赖、日志及硬盘问题会议 2025年10月13日.md | [[4-Archives/Notes/Feishu/云空间/何宜峰的个人文档/文字记录：项目依赖、日志及硬盘问题会议 2025年10月13日]] | [飞书](https://reliablesense.feishu.cn/docx/K1rBdMgWcopeZjxXKBFc5nACndd) | `1-Projects/Work/广州机场/会议纪要/` |
| 智能纪要：8084接口、列表及地图问题讨论 2025年10月27日.md | [[4-Archives/Notes/Feishu/云空间/何宜峰的个人文档/智能纪要：8084接口、列表及地图问题讨论 2025年10月27日]] | [飞书](https://reliablesense.feishu.cn/docx/Vyf1d9xi7oSdZVxPUrAcWMIOnEf) | `1-Projects/Work/广州机场/会议纪要/` |
| 智能纪要：云江项目任务方案及后续安排会 2025年10月27日.md | [[4-Archives/Notes/Feishu/云空间/何宜峰的个人文档/智能纪要：云江项目任务方案及后续安排会 2025年10月27日]] | [飞书](https://reliablesense.feishu.cn/docx/Satnd39gXoHjQYxUzW6cVWvinOe) | `1-Projects/Work/广州机场/会议纪要/` |
| 智能纪要：分子构建与插件使用安装讨论 2025年11月6日.md | [[4-Archives/Notes/Feishu/云空间/何宜峰的个人文档/智能纪要：分子构建与插件使用安装讨论 2025年11月6日]] | [飞书](https://reliablesense.feishu.cn/docx/XmvYdGxTLoHZpJxmb0pcEgZNnbc) | `1-Projects/Work/广州机场/会议纪要/` |
| 智能纪要：数据同步、订阅测试及新数据格式讨论 2025年10月28日.md | [[4-Archives/Notes/Feishu/云空间/何宜峰的个人文档/智能纪要：数据同步、订阅测试及新数据格式讨论 2025年10月28日]] | [飞书](https://reliablesense.feishu.cn/docx/LqMIdcq9Nod1nlxOYGvcxUVwnqh) | `1-Projects/Work/广州机场/会议纪要/` |
| 智能纪要：管理内容、分支及注释问题讨论 2025年11月6日.md | [[4-Archives/Notes/Feishu/云空间/何宜峰的个人文档/智能纪要：管理内容、分支及注释问题讨论 2025年11月6日]] | [飞书](https://reliablesense.feishu.cn/docx/OCCsdy2coohBdmxcVdVcPIlNnof) | `1-Projects/Work/广州机场/会议纪要/` |
| 智能纪要：管理员数据库表及任务归属问题讨论 2025年10月30日.md | [[4-Archives/Notes/Feishu/云空间/何宜峰的个人文档/智能纪要：管理员数据库表及任务归属问题讨论 2025年10月30日]] | [飞书](https://reliablesense.feishu.cn/docx/QDWldDLdjoNx0Bx291QcPcBxnbS) | `1-Projects/Work/广州机场/会议纪要/` |
| 智能纪要：项目依赖、日志及硬盘问题会议 2025年10月13日.md | [[4-Archives/Notes/Feishu/云空间/何宜峰的个人文档/智能纪要：项目依赖、日志及硬盘问题会议 2025年10月13日]] | [飞书](https://reliablesense.feishu.cn/docx/SVJodwciFoT6vGxQGiicoCpBnjg) | `1-Projects/Work/广州机场/会议纪要/` |
| 文字记录：广州机场电子围栏会议安排 2026年3月12日.md | [[4-Archives/Notes/Feishu/云空间/文字记录：广州机场电子围栏会议安排 2026年3月12日]] | [飞书](https://reliablesense.feishu.cn/docx/WMlldun20ooLtQxRhSAcxJPpn9e) | `1-Projects/Work/广州机场/会议纪要/` |
| 文字记录：总线接口问题沟通与反馈会议 2025年4月16日.md | [[4-Archives/Notes/Feishu/云空间/文字记录：总线接口问题沟通与反馈会议 2025年4月16日]] | [飞书](https://reliablesense.feishu.cn/docx/FMdddrIBQo593JxEYp7c6A7VnAg) | `1-Projects/Work/广州机场/会议纪要/` |
| 智能纪要：广州机场电子围栏会议安排 2026年3月12日.md | [[4-Archives/Notes/Feishu/云空间/智能纪要：广州机场电子围栏会议安排 2026年3月12日]] | [飞书](https://reliablesense.feishu.cn/docx/XWKodUy1VoL4qyxWPAAcP1BFnOd) | `1-Projects/Work/广州机场/会议纪要/` |
| 智能纪要：总线接口问题沟通与反馈会议 2025年4月16日.md | [[4-Archives/Notes/Feishu/云空间/智能纪要：总线接口问题沟通与反馈会议 2025年4月16日]] | [飞书](https://reliablesense.feishu.cn/docx/VOCEdqdccoZHohxdLixcdebLnQe) | `1-Projects/Work/广州机场/会议纪要/` |
| 文字记录：scommon获取及分支合并问题讨论 2025年9月16日.md | [[4-Archives/Notes/Feishu/云空间/王宗光的个人文档/文字记录：scommon获取及分支合并问题讨论 2025年9月16日]] | [飞书](https://reliablesense.feishu.cn/docx/DJOWdV7t5o2Mjdxx8ZacVCh1n3d) | `1-Projects/Work/广州机场/会议纪要/` |
| 智能纪要：scommon获取及分支合并问题讨论 2025年9月16日.md | [[4-Archives/Notes/Feishu/云空间/王宗光的个人文档/智能纪要：scommon获取及分支合并问题讨论 2025年9月16日]] | [飞书](https://reliablesense.feishu.cn/docx/LCdQdpAf7ozPMtxQUthcZqTKnLh) | `1-Projects/Work/广州机场/会议纪要/` |
| 文字记录：上海东海模型修复及接入方案研讨 2025年5月15日.md | [[4-Archives/Notes/Feishu/云空间/陈子杰的个人文档/文字记录：上海东海模型修复及接入方案研讨 2025年5月15日]] | [飞书](https://reliablesense.feishu.cn/docx/Ky4Ldt5hFoe6mQxg8lrctpCRngh) | `1-Projects/Work/广州机场/会议纪要/` |
| 文字记录：移动应用与 TCDM 会议讨论  2025年6月3日.md | [[4-Archives/Notes/Feishu/云空间/陈子杰的个人文档/文字记录：移动应用与 TCDM 会议讨论  2025年6月3日]] | [飞书](https://reliablesense.feishu.cn/docx/JmwhduJIPouIxsx7Sh6cH5ZOnph) | `1-Projects/Work/广州机场/会议纪要/` |
| 文字记录：黄佳琪软件工作安排及指导会议 2025年4月11日.md | [[4-Archives/Notes/Feishu/云空间/陈子杰的个人文档/文字记录：黄佳琪软件工作安排及指导会议 2025年4月11日]] | [飞书](https://reliablesense.feishu.cn/docx/MWlJdSwz6o30ykxZGMPcLmdin0f) | `1-Projects/Work/广州机场/会议纪要/` |
| 智能纪要：上海东海模型修复及接入方案研讨 2025年5月15日.md | [[4-Archives/Notes/Feishu/云空间/陈子杰的个人文档/智能纪要：上海东海模型修复及接入方案研讨 2025年5月15日]] | [飞书](https://reliablesense.feishu.cn/docx/BT99d8bucoUruTx4rvZcYbRbnff) | `1-Projects/Work/广州机场/会议纪要/` |
| 智能纪要：移动应用与 TCDM 会议讨论 2025年6月3日.md | [[4-Archives/Notes/Feishu/云空间/陈子杰的个人文档/智能纪要：移动应用与 TCDM 会议讨论 2025年6月3日]] | [飞书](https://reliablesense.feishu.cn/docx/VARrddtC3oOlFMxENAFcoGBKnl9) | `1-Projects/Work/广州机场/会议纪要/` |
| 智能纪要：黄佳琪软件工作安排及指导会议 2025年4月11日.md | [[4-Archives/Notes/Feishu/云空间/陈子杰的个人文档/智能纪要：黄佳琪软件工作安排及指导会议 2025年4月11日]] | [飞书](https://reliablesense.feishu.cn/docx/KFRAdFWTjoSKrIxLDPFcQH3Oncg) | `1-Projects/Work/广州机场/会议纪要/` |

#### 上港项目（4 个）

| 文件 | 本地路径 | 飞书链接 | 目标路径 |
|------|---------|---------|---------|
| 文字记录：刷新配置规则变更讨论会议 2025年9月25日.md | [[4-Archives/Notes/Feishu/云空间/王宗光的个人文档/文字记录：刷新配置规则变更讨论会议 2025年9月25日]] | [飞书](https://reliablesense.feishu.cn/docx/GUjJdm0rboypogxtgcacRhAEn7e) | `1-Projects/Work/上港仓储管理/会议纪要/` |
| 文字记录：申库、测试及登录存货问题讨论 2025年9月17日.md | [[4-Archives/Notes/Feishu/云空间/王宗光的个人文档/文字记录：申库、测试及登录存货问题讨论 2025年9月17日]] | [飞书](https://reliablesense.feishu.cn/docx/NrtBdN4sQo4P0cxB0RJc21Ebnse) | `1-Projects/Work/上港仓储管理/会议纪要/` |
| 智能纪要：刷新配置规则变更讨论会议 2025年9月25日.md | [[4-Archives/Notes/Feishu/云空间/王宗光的个人文档/智能纪要：刷新配置规则变更讨论会议 2025年9月25日]] | [飞书](https://reliablesense.feishu.cn/docx/XHG9dLsmDoBkJxx4bkJcIABInbD) | `1-Projects/Work/上港仓储管理/会议纪要/` |
| 智能纪要：申库、测试及登录存货问题讨论 2025年9月17日.md | [[4-Archives/Notes/Feishu/云空间/王宗光的个人文档/智能纪要：申库、测试及登录存货问题讨论 2025年9月17日]] | [飞书](https://reliablesense.feishu.cn/docx/HNAVdtRgzo4xLFxUjO0c3qi9nJc) | `1-Projects/Work/上港仓储管理/会议纪要/` |

#### 武汉机场（3 个）

| 文件 | 本地路径 | 飞书链接 | 目标路径 |
|------|---------|---------|---------|
| 文字记录：数据修改、卡顿及操作异常讨论 2026年3月12日.md | [[4-Archives/Notes/Feishu/云空间/文字记录：数据修改、卡顿及操作异常讨论 2026年3月12日]] | [飞书](https://reliablesense.feishu.cn/docx/CJYtdjil1o4AVaxvtgbch27ZnAh) | `4-Archives/Projects/Work/武汉机场/会议纪要/` |
| 文字记录：武汉机场图标、手册及任务讨论 2026年3月12日.md | [[4-Archives/Notes/Feishu/云空间/文字记录：武汉机场图标、手册及任务讨论 2026年3月12日]] | [飞书](https://reliablesense.feishu.cn/docx/NYnMdj5MsoHJ5oxhf6ZcgZrvnOh) | `4-Archives/Projects/Work/武汉机场/会议纪要/` |
| 智能纪要：武汉机场图标、手册及任务讨论 2026年3月12日.md | [[4-Archives/Notes/Feishu/云空间/智能纪要：武汉机场图标、手册及任务讨论 2026年3月12日]] | [飞书](https://reliablesense.feishu.cn/docx/ZXTIdfp9ao2RZXxWF0scCEgCnNd) | `4-Archives/Projects/Work/武汉机场/会议纪要/` |

#### 洛阳化工厂（1 个）

| 文件 | 本地路径 | 飞书链接 | 目标路径 |
|------|---------|---------|---------|
| 智能纪要：平台重启及相关技术问题研讨 2025年5月31日.md | [[4-Archives/Notes/Feishu/云空间/王宗光的个人文档/智能纪要：平台重启及相关技术问题研讨 2025年5月31日]] | [飞书](https://reliablesense.feishu.cn/docx/LDm7dDpHfoC4DBx6Vthcwqkrn4c) | `1-Projects/Work/洛阳化工厂/会议纪要/` |

#### 研发部早会（36 个）

| 文件 | 本地路径 | 飞书链接 | 目标路径 |
|------|---------|---------|---------|
| Video meeting—研发部 on Dec 10, 2024 - AI notes.md | [[4-Archives/Notes/Feishu/云空间/Video meeting—研发部 on Dec 10, 2024 - AI notes]] | [飞书](https://reliablesense.feishu.cn/docx/TAbJdMOBpo2tuHxITNPctUUTn7e) | `2-Areas/Work/团队管理/早会纪要/2024/12/` |
| Video meeting—研发部 on Dec 11, 2024 - AI notes.md | [[4-Archives/Notes/Feishu/云空间/Video meeting—研发部 on Dec 11, 2024 - AI notes]] | [飞书](https://reliablesense.feishu.cn/docx/Dk5ndqzX0owWZHxDbAIcR4n6ntf) | `2-Areas/Work/团队管理/早会纪要/2024/12/` |
| Video meeting—研发部 on Dec 12, 2024 - AI notes.md | [[4-Archives/Notes/Feishu/云空间/Video meeting—研发部 on Dec 12, 2024 - AI notes]] | [飞书](https://reliablesense.feishu.cn/docx/LEo4dcRUgoEeb5xJSbHcK8EKn4e) | `2-Areas/Work/团队管理/早会纪要/2024/12/` |
| Video meeting—研发部 on Dec 13, 2024 - AI notes.md | [[4-Archives/Notes/Feishu/云空间/Video meeting—研发部 on Dec 13, 2024 - AI notes]] | [飞书](https://reliablesense.feishu.cn/docx/SStgdYVo6oobE5xu5A3cLem1nWC) | `2-Areas/Work/团队管理/早会纪要/2024/12/` |
| Video meeting—研发部 on Dec 2, 2024 - AI notes.md | [[4-Archives/Notes/Feishu/云空间/Video meeting—研发部 on Dec 2, 2024 - AI notes]] | [飞书](https://reliablesense.feishu.cn/docx/RamydYI3LoRFcVxx5kecugXcn3e) | `2-Areas/Work/团队管理/早会纪要/2024/12/` |
| Video meeting—研发部 on Dec 20, 2024 - AI notes.md | [[4-Archives/Notes/Feishu/云空间/Video meeting—研发部 on Dec 20, 2024 - AI notes]] | [飞书](https://reliablesense.feishu.cn/docx/WXgSdyPThocornxmijPcM9IXnLd) | `2-Areas/Work/团队管理/早会纪要/2024/12/` |
| Video meeting—研发部 on Dec 24, 2024 - AI notes.md | [[4-Archives/Notes/Feishu/云空间/Video meeting—研发部 on Dec 24, 2024 - AI notes]] | [飞书](https://reliablesense.feishu.cn/docx/IAZCdxKfDo4AMtxK1hscJjkPnGz) | `2-Areas/Work/团队管理/早会纪要/2024/12/` |
| Video meeting—研发部 on Dec 3, 2024 - AI notes.md | [[4-Archives/Notes/Feishu/云空间/Video meeting—研发部 on Dec 3, 2024 - AI notes]] | [飞书](https://reliablesense.feishu.cn/docx/CU5kdAR8tojsK1xAEZAcNeOOngp) | `2-Areas/Work/团队管理/早会纪要/2024/12/` |
| Video meeting—研发部 on Nov 26, 2024 - AI notes.md | [[4-Archives/Notes/Feishu/云空间/Video meeting—研发部 on Nov 26, 2024 - AI notes]] | [飞书](https://reliablesense.feishu.cn/docx/HOdNd211EoYIVhxoxTac0CLnnUc) | `2-Areas/Work/团队管理/早会纪要/2024/11/` |
| Video meeting—研发部 on Nov 28, 2024 - AI notes.md | [[4-Archives/Notes/Feishu/云空间/Video meeting—研发部 on Nov 28, 2024 - AI notes]] | [飞书](https://reliablesense.feishu.cn/docx/M1jpdNj13o9iDsxjpxVcX8MPnzg) | `2-Areas/Work/团队管理/早会纪要/2024/11/` |
| Video meeting—研发部 on Nov 29, 2024 - AI notes.md | [[4-Archives/Notes/Feishu/云空间/Video meeting—研发部 on Nov 29, 2024 - AI notes]] | [飞书](https://reliablesense.feishu.cn/docx/NueSdTZMGojgVFxXmmPcpN9inMN) | `2-Areas/Work/团队管理/早会纪要/2024/11/` |
| 文字记录：研发部的视频会议 2025年2月18日.md | [[4-Archives/Notes/Feishu/云空间/文字记录：研发部的视频会议 2025年2月18日]] | [飞书](https://reliablesense.feishu.cn/docx/MYasdVyF5oJh8oxRQ6mcINlXndg) | `2-Areas/Work/团队管理/早会纪要/2025/02/` |
| 文字记录：研发部的视频会议 2025年3月10日.md | [[4-Archives/Notes/Feishu/云空间/文字记录：研发部的视频会议 2025年3月10日]] | [飞书](https://reliablesense.feishu.cn/docx/LDpydakF2oBHKzxp9yJcRfufnCc) | `2-Areas/Work/团队管理/早会纪要/2025/03/` |
| 文字记录：研发部的视频会议 2025年3月7日.md | [[4-Archives/Notes/Feishu/云空间/文字记录：研发部的视频会议 2025年3月7日]] | [飞书](https://reliablesense.feishu.cn/docx/ZyQkd4vZ7o9NFkxsjhHcfhXQnud) | `2-Areas/Work/团队管理/早会纪要/2025/03/` |
| 智能纪要：研发部的视频会议 2025年3月10日.md | [[4-Archives/Notes/Feishu/云空间/智能纪要：研发部的视频会议 2025年3月10日]] | [飞书](https://reliablesense.feishu.cn/docx/JUvfdlZVgo9vcexEmGPcR1a7nO9) | `2-Areas/Work/团队管理/早会纪要/2025/03/` |
| 智能纪要：研发部的视频会议 2025年3月7日.md | [[4-Archives/Notes/Feishu/云空间/智能纪要：研发部的视频会议 2025年3月7日]] | [飞书](https://reliablesense.feishu.cn/docx/RCb1dY3WXot4czxHhO2c3WyinAe) | `2-Areas/Work/团队管理/早会纪要/2025/03/` |
| 研发部的视频会议 2024年11月22日.md | [[4-Archives/Notes/Feishu/云空间/根目录/研发部的视频会议 2024年11月22日]] | [飞书](https://reliablesense.feishu.cn/docx/Vu8Nd0VN1ovfrOxpvDzcHcO5nSf) | `2-Areas/Work/团队管理/早会纪要/2024/11/` |
| 文字记录：研发部的视频会议 2025年2月24日.md | [[4-Archives/Notes/Feishu/云空间/王宗光的个人文档/文字记录：研发部的视频会议 2025年2月24日]] | [飞书](https://reliablesense.feishu.cn/docx/PhfqdTLQ3o5QyyxbK2IcRAkNn0b) | `2-Areas/Work/团队管理/早会纪要/2025/02/` |
| 智能纪要：研发部的视频会议 2025年2月24日.md | [[4-Archives/Notes/Feishu/云空间/王宗光的个人文档/智能纪要：研发部的视频会议 2025年2月24日]] | [飞书](https://reliablesense.feishu.cn/docx/C66QdPXJyolJ50xp7JBczVxunQb) | `2-Areas/Work/团队管理/早会纪要/2025/02/` |
| 研发部的视频会议 2024年12月23日 - 智能纪要.md | [[4-Archives/Notes/Feishu/云空间/研发部的视频会议 2024年12月23日 - 智能纪要]] | [飞书](https://reliablesense.feishu.cn/docx/RWuXdy1v5oHwzhxlBm5cPlzbn9b) | `2-Areas/Work/团队管理/早会纪要/2024/12/` |
| 研发部的视频会议 2024年12月25日 - 智能纪要.md | [[4-Archives/Notes/Feishu/云空间/研发部的视频会议 2024年12月25日 - 智能纪要]] | [飞书](https://reliablesense.feishu.cn/docx/GupqdTrwYoHehjxJj3YcX3uWnrf) | `2-Areas/Work/团队管理/早会纪要/2024/12/` |
| 研发部的视频会议 2024年12月26日 - 智能纪要.md | [[4-Archives/Notes/Feishu/云空间/研发部的视频会议 2024年12月26日 - 智能纪要]] | [飞书](https://reliablesense.feishu.cn/docx/Gmrgdh86fohRq3xcXOKcFTBTnyh) | `2-Areas/Work/团队管理/早会纪要/2024/12/` |
| 研发部的视频会议 2024年12月31日 - 智能纪要.md | [[4-Archives/Notes/Feishu/云空间/研发部的视频会议 2024年12月31日 - 智能纪要]] | [飞书](https://reliablesense.feishu.cn/docx/EcAhdQ8gOoFuGpxZZjzcLvBGnoc) | `2-Areas/Work/团队管理/早会纪要/2024/12/` |
| 研发部的视频会议 2024年12月6日 - 智能纪要.md | [[4-Archives/Notes/Feishu/云空间/研发部的视频会议 2024年12月6日 - 智能纪要]] | [飞书](https://reliablesense.feishu.cn/docx/YJeHdFa9ao2nEuxzwhzcaZWHngd) | `2-Areas/Work/团队管理/早会纪要/2024/12/` |
| 研发部的视频会议 2025年1月13日 - 智能纪要.md | [[4-Archives/Notes/Feishu/云空间/研发部的视频会议 2025年1月13日 - 智能纪要]] | [飞书](https://reliablesense.feishu.cn/docx/W7jZd2iGFoohALxRv5rc1DBonbf) | `2-Areas/Work/团队管理/早会纪要/2025/01/` |
| 研发部的视频会议 2025年1月15日 - 智能纪要.md | [[4-Archives/Notes/Feishu/云空间/研发部的视频会议 2025年1月15日 - 智能纪要]] | [飞书](https://reliablesense.feishu.cn/docx/XSnldCZEGoYduVxeqUuc4aypnEb) | `2-Areas/Work/团队管理/早会纪要/2025/01/` |
| 研发部的视频会议 2025年1月17日 - 智能纪要.md | [[4-Archives/Notes/Feishu/云空间/研发部的视频会议 2025年1月17日 - 智能纪要]] | [飞书](https://reliablesense.feishu.cn/docx/EH30delY8oyRmzxlL1ncX70Jngh) | `2-Areas/Work/团队管理/早会纪要/2025/01/` |
| 研发部的视频会议 2025年1月23日 - 智能纪要.md | [[4-Archives/Notes/Feishu/云空间/研发部的视频会议 2025年1月23日 - 智能纪要]] | [飞书](https://reliablesense.feishu.cn/docx/AnTCdX6JMoJG7MxXABNczlujngb) | `2-Areas/Work/团队管理/早会纪要/2025/01/` |
| 研发部的视频会议 2025年1月24日 - 智能纪要.md | [[4-Archives/Notes/Feishu/云空间/研发部的视频会议 2025年1月24日 - 智能纪要]] | [飞书](https://reliablesense.feishu.cn/docx/TpbPdTtc9oLJe8x9gXJcVKGcnKd) | `2-Areas/Work/团队管理/早会纪要/2025/01/` |
| 研发部的视频会议 2025年1月25日 - 智能纪要.md | [[4-Archives/Notes/Feishu/云空间/研发部的视频会议 2025年1月25日 - 智能纪要]] | [飞书](https://reliablesense.feishu.cn/docx/IWPHde7Dao29UyxktRhccdUmnlg) | `2-Areas/Work/团队管理/早会纪要/2025/01/` |
| 研发部的视频会议 2025年1月2日 - 智能纪要.md | [[4-Archives/Notes/Feishu/云空间/研发部的视频会议 2025年1月2日 - 智能纪要]] | [飞书](https://reliablesense.feishu.cn/docx/Hxr2dc5CyojtH0xsglscjYugnof) | `2-Areas/Work/团队管理/早会纪要/2025/01/` |
| 研发部的视频会议 2025年1月8日 - 智能纪要.md | [[4-Archives/Notes/Feishu/云空间/研发部的视频会议 2025年1月8日 - 智能纪要]] | [飞书](https://reliablesense.feishu.cn/docx/USiGdEpMPoyyO9xLaurcdlkonVe) | `2-Areas/Work/团队管理/早会纪要/2025/01/` |
| 研发部的视频会议 2025年1月9日 - 智能纪要.md | [[4-Archives/Notes/Feishu/云空间/研发部的视频会议 2025年1月9日 - 智能纪要]] | [飞书](https://reliablesense.feishu.cn/docx/Lka3dyCM7oB8s1xSgnbcbPiRngb) | `2-Areas/Work/团队管理/早会纪要/2025/01/` |
| 研发部的视频会议 2025年2月10日 - 智能纪要.md | [[4-Archives/Notes/Feishu/云空间/研发部的视频会议 2025年2月10日 - 智能纪要]] | [飞书](https://reliablesense.feishu.cn/docx/XMVNd6JJToD12GxX8PVc8xjunSh) | `2-Areas/Work/团队管理/早会纪要/2025/02/` |
| 研发部的视频会议 2025年2月18日 - 智能纪要.md | [[4-Archives/Notes/Feishu/云空间/研发部的视频会议 2025年2月18日 - 智能纪要]] | [飞书](https://reliablesense.feishu.cn/docx/E0x1dGcBzojfwxxbtbvc1AG5nth) | `2-Areas/Work/团队管理/早会纪要/2025/02/` |
| 研发部的视频会议 2025年2月6日 - 智能纪要.md | [[4-Archives/Notes/Feishu/云空间/研发部的视频会议 2025年2月6日 - 智能纪要]] | [飞书](https://reliablesense.feishu.cn/docx/W4hjdXlxgo1W6ax14wYcWypDn5f) | `2-Areas/Work/团队管理/早会纪要/2025/02/` |

#### 项目部周会（18 个）

| 文件 | 本地路径 | 飞书链接 | 目标路径 |
|------|---------|---------|---------|
| Video meeting—项目部 on Dec 10, 2024 - AI notes.md | [[4-Archives/Notes/Feishu/云空间/Video meeting—项目部 on Dec 10, 2024 - AI notes]] | [飞书](https://reliablesense.feishu.cn/docx/QLrxdD4Feo5ja5x9QRLcTbROnOb) | `2-Areas/Work/团队管理/周会纪要/项目部/2024/12/` |
| Video meeting—项目部 on Dec 11, 2024 - AI notes.md | [[4-Archives/Notes/Feishu/云空间/Video meeting—项目部 on Dec 11, 2024 - AI notes]] | [飞书](https://reliablesense.feishu.cn/docx/RqmWdrJV7oslnbxg9REc9fIKnxV) | `2-Areas/Work/团队管理/周会纪要/项目部/2024/12/` |
| Video meeting—项目部 on Dec 13, 2024 - AI notes.md | [[4-Archives/Notes/Feishu/云空间/Video meeting—项目部 on Dec 13, 2024 - AI notes]] | [飞书](https://reliablesense.feishu.cn/docx/BW6BduOYHoeosnxrKiSch4KFndb) | `2-Areas/Work/团队管理/周会纪要/项目部/2024/12/` |
| Video meeting—项目部 on Dec 2, 2024 - AI notes.md | [[4-Archives/Notes/Feishu/云空间/Video meeting—项目部 on Dec 2, 2024 - AI notes]] | [飞书](https://reliablesense.feishu.cn/docx/PEvedYMiho57MNx6LrTcwDMInCc) | `2-Areas/Work/团队管理/周会纪要/项目部/2024/12/` |
| Video meeting—项目部 on Dec 20, 2024 - AI notes.md | [[4-Archives/Notes/Feishu/云空间/Video meeting—项目部 on Dec 20, 2024 - AI notes]] | [飞书](https://reliablesense.feishu.cn/docx/LxjxdLD1goo3tRxy8RSc2I7rnI8) | `2-Areas/Work/团队管理/周会纪要/项目部/2024/12/` |
| Video meeting—项目部 on Dec 24, 2024 - AI notes.md | [[4-Archives/Notes/Feishu/云空间/Video meeting—项目部 on Dec 24, 2024 - AI notes]] | [飞书](https://reliablesense.feishu.cn/docx/QZ5BdumZ7o4ryPxTusfcoHz2n0f) | `2-Areas/Work/团队管理/周会纪要/项目部/2024/12/` |
| Video meeting—项目部 on Dec 3, 2024 - AI notes.md | [[4-Archives/Notes/Feishu/云空间/Video meeting—项目部 on Dec 3, 2024 - AI notes]] | [飞书](https://reliablesense.feishu.cn/docx/VjGidQkvaobYSpx8Wb9cMYTxnIe) | `2-Areas/Work/团队管理/周会纪要/项目部/2024/12/` |
| Video meeting—项目部 on Nov 25, 2024 - AI notes.md | [[4-Archives/Notes/Feishu/云空间/Video meeting—项目部 on Nov 25, 2024 - AI notes]] | [飞书](https://reliablesense.feishu.cn/docx/LRE4dR8SioaHCxxf0bYc7yyrnwe) | `2-Areas/Work/团队管理/周会纪要/项目部/2024/11/` |
| Video meeting—项目部 on Nov 26, 2024 - AI notes.md | [[4-Archives/Notes/Feishu/云空间/Video meeting—项目部 on Nov 26, 2024 - AI notes]] | [飞书](https://reliablesense.feishu.cn/docx/Dm2Sd4UkBoI7rWxUqyocRjHBnoe) | `2-Areas/Work/团队管理/周会纪要/项目部/2024/11/` |
| Video meeting—项目部 on Nov 27, 2024 - AI notes.md | [[4-Archives/Notes/Feishu/云空间/Video meeting—项目部 on Nov 27, 2024 - AI notes]] | [飞书](https://reliablesense.feishu.cn/docx/KcZndgUWOoAA7YxWzLBcqOBhnjh) | `2-Areas/Work/团队管理/周会纪要/项目部/2024/11/` |
| Video meeting—项目部 on Nov 28, 2024 - AI notes.md | [[4-Archives/Notes/Feishu/云空间/Video meeting—项目部 on Nov 28, 2024 - AI notes]] | [飞书](https://reliablesense.feishu.cn/docx/KBkadj5kUo6lkvxurUHcXyg6nme) | `2-Areas/Work/团队管理/周会纪要/项目部/2024/11/` |
| 项目部的视频会议 2024年12月23日 - 智能纪要.md | [[4-Archives/Notes/Feishu/云空间/项目部的视频会议 2024年12月23日 - 智能纪要]] | [飞书](https://reliablesense.feishu.cn/docx/X3YwdVbFtoiwfXx0ix1ciECjnHg) | `2-Areas/Work/团队管理/周会纪要/项目部/2024/12/` |
| 项目部的视频会议 2025年1月13日 - 智能纪要.md | [[4-Archives/Notes/Feishu/云空间/项目部的视频会议 2025年1月13日 - 智能纪要]] | [飞书](https://reliablesense.feishu.cn/docx/Hg7tdVd6Fo94D9xlFw7c6zYTnOc) | `2-Areas/Work/团队管理/周会纪要/项目部/2025/01/` |
| 项目部的视频会议 2025年1月15日 - 智能纪要.md | [[4-Archives/Notes/Feishu/云空间/项目部的视频会议 2025年1月15日 - 智能纪要]] | [飞书](https://reliablesense.feishu.cn/docx/H9Vod5HBbotd4OxkvE5cjPMenhd) | `2-Areas/Work/团队管理/周会纪要/项目部/2025/01/` |
| 项目部的视频会议 2025年1月17日 - 智能纪要.md | [[4-Archives/Notes/Feishu/云空间/项目部的视频会议 2025年1月17日 - 智能纪要]] | [飞书](https://reliablesense.feishu.cn/docx/Af6ndwOY4oD5j0xYPCEcigi3n2c) | `2-Areas/Work/团队管理/周会纪要/项目部/2025/01/` |
| 项目部的视频会议 2025年1月22日 - 智能纪要.md | [[4-Archives/Notes/Feishu/云空间/项目部的视频会议 2025年1月22日 - 智能纪要]] | [飞书](https://reliablesense.feishu.cn/docx/NUGbdUpv7ov9nlxJ1EecS5X1n6b) | `2-Areas/Work/团队管理/周会纪要/项目部/2025/01/` |
| 项目部的视频会议 2025年1月25日 - 智能纪要.md | [[4-Archives/Notes/Feishu/云空间/项目部的视频会议 2025年1月25日 - 智能纪要]] | [飞书](https://reliablesense.feishu.cn/docx/Kp2Dd039dogQgpxvuzQcUI5tnHb) | `2-Areas/Work/团队管理/周会纪要/项目部/2025/01/` |
| 项目部的视频会议 2025年1月2日 - 智能纪要.md | [[4-Archives/Notes/Feishu/云空间/项目部的视频会议 2025年1月2日 - 智能纪要]] | [飞书](https://reliablesense.feishu.cn/docx/RIrMd8Y7Bo06GzxWoE8cBYeDnbe) | `2-Areas/Work/团队管理/周会纪要/项目部/2025/01/` |

#### 项目进度会（35 个）

| 文件 | 本地路径 | 飞书链接 | 目标路径 |
|------|---------|---------|---------|
| 刘秉欣的视频会议 2024年12月24日 - 智能纪要.md | [[4-Archives/Notes/Feishu/云空间/刘秉欣的视频会议 2024年12月24日 - 智能纪要]] | [飞书](https://reliablesense.feishu.cn/docx/XdWXdFd3yocR0Gxs4AacOg2jn7d) | `2-Areas/Work/团队管理/周会纪要/`2024/12/ |
| 刘秉欣的视频会议 2024年12月25日 - 智能纪要.md | [[4-Archives/Notes/Feishu/云空间/刘秉欣的视频会议 2024年12月25日 - 智能纪要]] | [飞书](https://reliablesense.feishu.cn/docx/TKGLdB05ioAbtOxy3QtcM6Apnhh) | `2-Areas/Work/团队管理/周会纪要/`2024/12/ |
| 刘秉欣的视频会议 2024年12月7日 - 智能纪要.md | [[4-Archives/Notes/Feishu/云空间/刘秉欣的视频会议 2024年12月7日 - 智能纪要]] | [飞书](https://reliablesense.feishu.cn/docx/MVdod7OefoPdauxmRb4cRkcqn2R) | `2-Areas/Work/团队管理/周会纪要/`2024/12/ |
| 刘秉欣的视频会议 2025年1月12日 - 智能纪要.md | [[4-Archives/Notes/Feishu/云空间/刘秉欣的视频会议 2025年1月12日 - 智能纪要]] | [飞书](https://reliablesense.feishu.cn/docx/By5CdBovVoQH7Tx855pcgAmHntv) | `2-Areas/Work/团队管理/周会纪要/`2025/01/ |
| 刘秉欣的视频会议 2025年1月13日 - 智能纪要.md | [[4-Archives/Notes/Feishu/云空间/刘秉欣的视频会议 2025年1月13日 - 智能纪要]] | [飞书](https://reliablesense.feishu.cn/docx/DnhydQrqRozQ38xMurfcWKolnyh) | `2-Areas/Work/团队管理/周会纪要/`2025/01/ |
| 刘秉欣的视频会议 2025年1月14日 - 智能纪要.md | [[4-Archives/Notes/Feishu/云空间/刘秉欣的视频会议 2025年1月14日 - 智能纪要]] | [飞书](https://reliablesense.feishu.cn/docx/VUOTdcU6Cou2evx4LzBc9Jp5nJf) | `2-Areas/Work/团队管理/周会纪要/`2025/01/ |
| 刘秉欣的视频会议 2025年1月15日 - 智能纪要.md | [[4-Archives/Notes/Feishu/云空间/刘秉欣的视频会议 2025年1月15日 - 智能纪要]] | [飞书](https://reliablesense.feishu.cn/docx/Lf2gdnvmAofZFxx9c9HctxPon8d) | `2-Areas/Work/团队管理/周会纪要/`2025/01/ |
| 刘秉欣的视频会议 2025年1月16日 - 智能纪要.md | [[4-Archives/Notes/Feishu/云空间/刘秉欣的视频会议 2025年1月16日 - 智能纪要]] | [飞书](https://reliablesense.feishu.cn/docx/SbL3daoMkoMhvVxXueRcF2VDnCc) | `2-Areas/Work/团队管理/周会纪要/`2025/01/ |
| 刘秉欣的视频会议 2025年1月18日 - 智能纪要.md | [[4-Archives/Notes/Feishu/云空间/刘秉欣的视频会议 2025年1月18日 - 智能纪要]] | [飞书](https://reliablesense.feishu.cn/docx/Xm7tdfLdxoRgTAxzdThcTpGynde) | `2-Areas/Work/团队管理/周会纪要/`2025/01/ |
| 刘秉欣的视频会议 2025年1月20日 - 智能纪要.md | [[4-Archives/Notes/Feishu/云空间/刘秉欣的视频会议 2025年1月20日 - 智能纪要]] | [飞书](https://reliablesense.feishu.cn/docx/QyRodMixpoXwzLxpb3VcCdWcnFs) | `2-Areas/Work/团队管理/周会纪要/`2025/01/ |
| 刘秉欣的视频会议 2025年1月23日 - 智能纪要.md | [[4-Archives/Notes/Feishu/云空间/刘秉欣的视频会议 2025年1月23日 - 智能纪要]] | [飞书](https://reliablesense.feishu.cn/docx/UGZCdhqSfopliHx5a7lcd5OanLE) | `2-Areas/Work/团队管理/周会纪要/`2025/01/ |
| 刘秉欣的视频会议 2025年1月24日 - 智能纪要.md | [[4-Archives/Notes/Feishu/云空间/刘秉欣的视频会议 2025年1月24日 - 智能纪要]] | [飞书](https://reliablesense.feishu.cn/docx/WoCGdjr02opws8xtJH6cBF8Knhb) | `2-Areas/Work/团队管理/周会纪要/`2025/01/ |
| 刘秉欣的视频会议 2025年1月2日 - 智能纪要.md | [[4-Archives/Notes/Feishu/云空间/刘秉欣的视频会议 2025年1月2日 - 智能纪要]] | [飞书](https://reliablesense.feishu.cn/docx/Dut7diN65okiKgxkPalchJ5wnDg) | `2-Areas/Work/团队管理/周会纪要/`2025/01/ |
| 刘秉欣的视频会议 2025年1月3日 - 智能纪要.md | [[4-Archives/Notes/Feishu/云空间/刘秉欣的视频会议 2025年1月3日 - 智能纪要]] | [飞书](https://reliablesense.feishu.cn/docx/LSGXdvOfVoUTtrxbJWmcQe04nFg) | `2-Areas/Work/团队管理/周会纪要/`2025/01/ |
| 刘秉欣的视频会议 2025年1月7日 - 智能纪要.md | [[4-Archives/Notes/Feishu/云空间/刘秉欣的视频会议 2025年1月7日 - 智能纪要]] | [飞书](https://reliablesense.feishu.cn/docx/RpYddvMajoPWHfx4QYNcrqb7n2c) | `2-Areas/Work/团队管理/周会纪要/`2025/01/ |
| 刘秉欣的视频会议 2025年2月14日 - 智能纪要.md | [[4-Archives/Notes/Feishu/云空间/刘秉欣的视频会议 2025年2月14日 - 智能纪要]] | [飞书](https://reliablesense.feishu.cn/docx/Y1redaHRyol8ClxLFducb7xAnyc) | `2-Areas/Work/团队管理/周会纪要/`2025/02/ |
| 刘秉欣的视频会议 2025年2月16日 - 智能纪要.md | [[4-Archives/Notes/Feishu/云空间/刘秉欣的视频会议 2025年2月16日 - 智能纪要]] | [飞书](https://reliablesense.feishu.cn/docx/WfjydHGojohtimxFgFhc7d6kndL) | `2-Areas/Work/团队管理/周会纪要/`2025/02/ |
| 刘秉欣的视频会议 2025年2月18日 - 智能纪要.md | [[4-Archives/Notes/Feishu/云空间/刘秉欣的视频会议 2025年2月18日 - 智能纪要]] | [飞书](https://reliablesense.feishu.cn/docx/Jr6RdJNRRoV6ajx6omacncJ3nGh) | `2-Areas/Work/团队管理/周会纪要/`2025/02/ |
| 刘秉欣的视频会议 2025年2月19日 - 智能纪要.md | [[4-Archives/Notes/Feishu/云空间/刘秉欣的视频会议 2025年2月19日 - 智能纪要]] | [飞书](https://reliablesense.feishu.cn/docx/SkOodGODEoWzk0xQPouctEEInYs) | `2-Areas/Work/团队管理/周会纪要/`2025/02/ |
| 文字记录：刘秉欣的视频会议 2025年2月14日.md | [[4-Archives/Notes/Feishu/云空间/文字记录：刘秉欣的视频会议 2025年2月14日]] | [飞书](https://reliablesense.feishu.cn/docx/Xci9dpg4GoQ2dWxdBlgcoDTtnW9) | `2-Areas/Work/团队管理/周会纪要/`2025/02/ |
| 文字记录：刘秉欣的视频会议 2025年2月16日.md | [[4-Archives/Notes/Feishu/云空间/文字记录：刘秉欣的视频会议 2025年2月16日]] | [飞书](https://reliablesense.feishu.cn/docx/LW4vdM60DouGByxZQEacE9Iwnlg) | `2-Areas/Work/团队管理/周会纪要/`2025/02/ |
| 文字记录：刘秉欣的视频会议 2025年2月18日.md | [[4-Archives/Notes/Feishu/云空间/文字记录：刘秉欣的视频会议 2025年2月18日]] | [飞书](https://reliablesense.feishu.cn/docx/VEmNd8AvQogE6vxOfNmcLrzMnVd) | `2-Areas/Work/团队管理/周会纪要/`2025/02/ |
| 文字记录：刘秉欣的视频会议 2025年2月19日.md | [[4-Archives/Notes/Feishu/云空间/文字记录：刘秉欣的视频会议 2025年2月19日]] | [飞书](https://reliablesense.feishu.cn/docx/Q6STd5e9lo8XY5xcUVMcNSQgnVH) | `2-Areas/Work/团队管理/周会纪要/`2025/02/ |
| 文字记录：刘秉欣的视频会议 2025年2月25日.md | [[4-Archives/Notes/Feishu/云空间/文字记录：刘秉欣的视频会议 2025年2月25日]] | [飞书](https://reliablesense.feishu.cn/docx/Fa8VdpdFCoFKhrxe8MlcGEhDnLP) | `2-Areas/Work/团队管理/周会纪要/`2025/02/ |
| 文字记录：刘秉欣的视频会议 2025年2月26日.md | [[4-Archives/Notes/Feishu/云空间/文字记录：刘秉欣的视频会议 2025年2月26日]] | [飞书](https://reliablesense.feishu.cn/docx/FaWHdfdqNo7LKexKngxcQyq7n7f) | `2-Areas/Work/团队管理/周会纪要/`2025/02/ |
| 文字记录：刘秉欣的视频会议 2025年2月28日.md | [[4-Archives/Notes/Feishu/云空间/文字记录：刘秉欣的视频会议 2025年2月28日]] | [飞书](https://reliablesense.feishu.cn/docx/OBsldoskLoFyhixYWbXcIJngnuc) | `2-Areas/Work/团队管理/周会纪要/`2025/02/ |
| 文字记录：刘秉欣的视频会议 2025年3月16日.md | [[4-Archives/Notes/Feishu/云空间/文字记录：刘秉欣的视频会议 2025年3月16日]] | [飞书](https://reliablesense.feishu.cn/docx/UtUndAAdGoAp2uxsUiVc5Oc0n8B) | `2-Areas/Work/团队管理/周会纪要/`2025/03/ |
| 文字记录：刘秉欣的视频会议 2025年3月2日.md | [[4-Archives/Notes/Feishu/云空间/文字记录：刘秉欣的视频会议 2025年3月2日]] | [飞书](https://reliablesense.feishu.cn/docx/P7fadiXVPoDosSxTtPYcjuezn0d) | `2-Areas/Work/团队管理/周会纪要/`2025/03/ |
| 文字记录：刘秉欣的视频会议 2025年3月6日.md | [[4-Archives/Notes/Feishu/云空间/文字记录：刘秉欣的视频会议 2025年3月6日]] | [飞书](https://reliablesense.feishu.cn/docx/PSEHdO5hKooHBxxg37DcsbJfnGd) | `2-Areas/Work/团队管理/周会纪要/`2025/03/ |
| 智能纪要：刘秉欣的视频会议 2025年2月25日.md | [[4-Archives/Notes/Feishu/云空间/智能纪要：刘秉欣的视频会议 2025年2月25日]] | [飞书](https://reliablesense.feishu.cn/docx/VwNzdZTcYoyxJLxY9NtcWm3wnad) | `2-Areas/Work/团队管理/周会纪要/`2025/02/ |
| 智能纪要：刘秉欣的视频会议 2025年2月26日.md | [[4-Archives/Notes/Feishu/云空间/智能纪要：刘秉欣的视频会议 2025年2月26日]] | [飞书](https://reliablesense.feishu.cn/docx/JdvJd0gkeoTfWsxhKinciBXdnMf) | `2-Areas/Work/团队管理/周会纪要/`2025/02/ |
| 智能纪要：刘秉欣的视频会议 2025年2月28日.md | [[4-Archives/Notes/Feishu/云空间/智能纪要：刘秉欣的视频会议 2025年2月28日]] | [飞书](https://reliablesense.feishu.cn/docx/G0CmdiAL6oiQalxVrPdcBw1jnqf) | `2-Areas/Work/团队管理/周会纪要/`2025/02/ |
| 智能纪要：刘秉欣的视频会议 2025年3月16日.md | [[4-Archives/Notes/Feishu/云空间/智能纪要：刘秉欣的视频会议 2025年3月16日]] | [飞书](https://reliablesense.feishu.cn/docx/EejLdwMcoowfW1xf5AGcbWw3nrx) | `2-Areas/Work/团队管理/周会纪要/`2025/03/ |
| 智能纪要：刘秉欣的视频会议 2025年3月2日.md | [[4-Archives/Notes/Feishu/云空间/智能纪要：刘秉欣的视频会议 2025年3月2日]] | [飞书](https://reliablesense.feishu.cn/docx/CzjodNgJQoMZlMxjKWPcvq4MnRe) | `2-Areas/Work/团队管理/周会纪要/`2025/03/ |
| 智能纪要：刘秉欣的视频会议 2025年3月6日.md | [[4-Archives/Notes/Feishu/云空间/智能纪要：刘秉欣的视频会议 2025年3月6日]] | [飞书](https://reliablesense.feishu.cn/docx/UZNfdtUa3oTDzyx12Eqcd8Rfn6g) | `2-Areas/Work/团队管理/周会纪要/`2025/03/ |

#### 技术讨论（7 个）

| 文件 | 本地路径 | 飞书链接 | 目标路径 |
|------|---------|---------|---------|
| 文字记录：launchable查询及告警管理问题讨论 2026年3月12日.md | [[4-Archives/Notes/Feishu/云空间/文字记录：launchable查询及告警管理问题讨论 2026年3月12日]] | [飞书](https://reliablesense.feishu.cn/docx/ZUWmdKM1yogZNuxSWYocJO3ynpg) | ⚠️ 待确认 | 见 [[1-Projects/Personal/笔记迁移/阶段二-待确认分类]] |
| 文字记录：代码修改：Beacon与网关定位差异 2026年3月11日.md | [[4-Archives/Notes/Feishu/云空间/文字记录：代码修改：Beacon与网关定位差异 2026年3月11日]] | [飞书](https://reliablesense.feishu.cn/docx/NoSpdy20moXWLWxGp0hcjFa2n3f) | ⚠️ 待确认 | 见 [[1-Projects/Personal/笔记迁移/阶段二-待确认分类]] |
| 智能纪要：launchable查询及告警管理问题讨论 2026年3月12日.md | [[4-Archives/Notes/Feishu/云空间/智能纪要：launchable查询及告警管理问题讨论 2026年3月12日]] | [飞书](https://reliablesense.feishu.cn/docx/PZD8dz0C6ouiH6xY4HVc1GJjnGh) | ⚠️ 待确认 | 见 [[1-Projects/Personal/笔记迁移/阶段二-待确认分类]] |
| 智能纪要：代码修改：Beacon与网关定位差异 2026年3月11日.md | [[4-Archives/Notes/Feishu/云空间/智能纪要：代码修改：Beacon与网关定位差异 2026年3月11日]] | [飞书](https://reliablesense.feishu.cn/docx/EGwqdnH6voVInSxT8eicfj7znPf) | ⚠️ 待确认 | 见 [[1-Projects/Personal/笔记迁移/阶段二-待确认分类]] |
| 文字记录：办公室 CLE 数据配置及墨水屏问题会议 2025年8月19日.md | [[4-Archives/Notes/Feishu/云空间/王宗光的个人文档/文字记录：办公室 CLE 数据配置及墨水屏问题会议 2025年8月19日]] | [飞书](https://reliablesense.feishu.cn/docx/QG3ld8j2joWsEDxVOFocVLrAnOg) | ⚠️ 待确认 | 见 [[1-Projects/Personal/笔记迁移/阶段二-待确认分类]] |
| 文字记录：平台重启及相关技术问题研讨 2025年5月31日.md | [[4-Archives/Notes/Feishu/云空间/王宗光的个人文档/文字记录：平台重启及相关技术问题研讨 2025年5月31日]] | [飞书](https://reliablesense.feishu.cn/docx/LRjhdZLUeoMIyKxAoIyciR1qneg) | ⚠️ 待确认 | 见 [[1-Projects/Personal/笔记迁移/阶段二-待确认分类]] |
| 智能纪要：办公室 CLE 数据配置及墨水屏问题会议 2025年8月19日.md | [[4-Archives/Notes/Feishu/云空间/王宗光的个人文档/智能纪要：办公室 CLE 数据配置及墨水屏问题会议 2025年8月19日]] | [飞书](https://reliablesense.feishu.cn/docx/XAwMd4UStoorpRxKG3scYBLbnQe) | ⚠️ 待确认 | 见 [[1-Projects/Personal/笔记迁移/阶段二-待确认分类]] |

#### 产品研发（8 个）

| 文件 | 本地路径 | 飞书链接 | 目标路径 |
|------|---------|---------|---------|
| 文字记录：会议研讨多项工作进展情况 2026年3月11日.md | [[4-Archives/Notes/Feishu/云空间/文字记录：会议研讨多项工作进展情况 2026年3月11日]] | [飞书](https://reliablesense.feishu.cn/docx/ZEhLdBtR3oEQXnxHFezcWf3qnsb) | `2-Areas/Work/产品研发/会议纪要/` |
| 文字记录：接口、登录及缓存相关问题研讨 2025年4月14日.md | [[4-Archives/Notes/Feishu/云空间/文字记录：接口、登录及缓存相关问题研讨 2025年4月14日]] | [飞书](https://reliablesense.feishu.cn/docx/WX92d2s8aom3SixuxG8cVUyGnMc) | `2-Areas/Work/产品研发/会议纪要/` |
| 智能纪要：会议研讨多项工作进展情况 2026年3月11日.md | [[4-Archives/Notes/Feishu/云空间/智能纪要：会议研讨多项工作进展情况 2026年3月11日]] | [飞书](https://reliablesense.feishu.cn/docx/ZlJrd2jI2og5rAxI38LcMaWxnfd) | `2-Areas/Work/产品研发/会议纪要/` |
| 智能纪要：接口、登录及缓存相关问题研讨 2025年4月14日.md | [[4-Archives/Notes/Feishu/云空间/智能纪要：接口、登录及缓存相关问题研讨 2025年4月14日]] | [飞书](https://reliablesense.feishu.cn/docx/BwYtdGuyxov5I2xi2XJcsfULnef) | `2-Areas/Work/产品研发/会议纪要/` |
| 智能纪要：数据修改、卡顿及操作异常讨论 2026年3月12日.md | [[4-Archives/Notes/Feishu/云空间/智能纪要：数据修改、卡顿及操作异常讨论 2026年3月12日]] | [飞书](https://reliablesense.feishu.cn/docx/QrfYdgZQloxUTMxVcLOcaSvDnNo) | `2-Areas/Work/产品研发/会议纪要/` |
| 文字记录：多方面业务问题及解决方案探讨会 2025年6月3日.md | [[4-Archives/Notes/Feishu/云空间/王宗光的个人文档/文字记录：多方面业务问题及解决方案探讨会 2025年6月3日]] | [飞书](https://reliablesense.feishu.cn/docx/Jtm6dfrULo7SNYxWZZ9cwLULnvd) | `2-Areas/Work/产品研发/会议纪要/` |
| 文字记录：数据、页面状态及功能处理会议 2025年9月17日.md | [[4-Archives/Notes/Feishu/云空间/陈子杰的个人文档/文字记录：数据、页面状态及功能处理会议 2025年9月17日]] | [飞书](https://reliablesense.feishu.cn/docx/O7UVdlfMSoMkZbxVyWic5N0bnBf) | `2-Areas/Work/产品研发/会议纪要/` |
| 智能纪要：数据、页面状态及功能处理会议 2025年9月17日.md | [[4-Archives/Notes/Feishu/云空间/陈子杰的个人文档/智能纪要：数据、页面状态及功能处理会议 2025年9月17日]] | [飞书](https://reliablesense.feishu.cn/docx/KliDdAtzionSN1xuPXic7YWynUd) | `2-Areas/Work/产品研发/会议纪要/` |

#### AI 汇总 → 团队成员目录（84 个）

> 近期会议速递、月度纪要小结等飞书 AI 生成的汇总，共 84 个，按所属同事归入对应的团队成员目录：
> - 何宜峰的 → `4-Archives/Areas/Work/团队管理/团队成员/何宜峰/`
> - 陈子杰的 → `4-Archives/Areas/Work/团队管理/团队成员/陈子杰/`
> - 王宗光的 → `4-Archives/Areas/Work/团队管理/团队成员/王宗光/`
> - 孙永霖的 → `4-Archives/Areas/Work/团队管理/团队成员/孙永霖/`



---

## 三、同事个人文档

### 何宜峰的个人文档（22 个文件）

| 文件 | 本地路径 | 飞书链接 | 分类 | 目标路径 |
|------|---------|---------|------|---------|
| 员工入职表-空白(1).xls | [[4-Archives/Notes/Feishu/云空间/何宜峰的个人文档/员工入职表-空白(1).xls]] | [飞书](https://reliablesense.feishu.cn/file/L3hKbcijfohKN2xtueVc88dcnEd) | → 提取 | `4-Archives/Areas/Work/团队管理/团队成员/何宜峰/` |
| 文字记录：8084接口、列表及地图问题讨论 2025年10月27日.md | [[4-Archives/Notes/Feishu/云空间/何宜峰的个人文档/文字记录：8084接口、列表及地图问题讨论 2025年10月27日]] | [飞书](https://reliablesense.feishu.cn/docx/LdfpdNSktotC7WxY1nAcoQ0gn5g) | → 提取 | `1-Projects/Work/广州机场/会议纪要/`  |
| 文字记录：云江项目任务方案及后续安排会 2025年10月27日.md | [[4-Archives/Notes/Feishu/云空间/何宜峰的个人文档/文字记录：云江项目任务方案及后续安排会 2025年10月27日]] | [飞书](https://reliablesense.feishu.cn/docx/KhyYd0clVo2XuGxNWqrc9pGSnVd) | → 提取 | `1-Projects/Work/广州机场/会议纪要/`  |
| 文字记录：分子构建与插件使用安装讨论 2025年11月6日.md | [[4-Archives/Notes/Feishu/云空间/何宜峰的个人文档/文字记录：分子构建与插件使用安装讨论 2025年11月6日]] | [飞书](https://reliablesense.feishu.cn/docx/HrTkdTglAohn1pxSxbfcUGPBnIc) | → 提取 | `1-Projects/Work/广州机场/会议纪要/`  |
| 文字记录：数据同步、订阅测试及新数据格式讨论  2025年10月28日.md | [[4-Archives/Notes/Feishu/云空间/何宜峰的个人文档/文字记录：数据同步、订阅测试及新数据格式讨论  2025年10月28日]] | [飞书](https://reliablesense.feishu.cn/docx/UHKEdQ12Mo7q1Wxrw3LchCN7ncb) | → 提取 | `1-Projects/Work/广州机场/会议纪要/`  |
| 文字记录：管理内容、分支及注释问题讨论 2025年11月6日.md | [[4-Archives/Notes/Feishu/云空间/何宜峰的个人文档/文字记录：管理内容、分支及注释问题讨论 2025年11月6日]] | [飞书](https://reliablesense.feishu.cn/docx/Pvl3dZTnmo8xyPx3dLjcdFf8nqf) | → 提取 | `1-Projects/Work/广州机场/会议纪要/`  |
| 文字记录：管理员数据库表及任务归属问题讨论 2025年10月30日.md | [[4-Archives/Notes/Feishu/云空间/何宜峰的个人文档/文字记录：管理员数据库表及任务归属问题讨论 2025年10月30日]] | [飞书](https://reliablesense.feishu.cn/docx/UfuNdjJLAoTZnaxGRH0c4KAbnwg) | → 提取 | `1-Projects/Work/广州机场/会议纪要/`  |
| 文字记录：项目依赖、日志及硬盘问题会议 2025年10月13日.md | [[4-Archives/Notes/Feishu/云空间/何宜峰的个人文档/文字记录：项目依赖、日志及硬盘问题会议 2025年10月13日]] | [飞书](https://reliablesense.feishu.cn/docx/K1rBdMgWcopeZjxXKBFc5nACndd) | → 提取 | `1-Projects/Work/广州机场/会议纪要/`  |
| 智能纪要：8084接口、列表及地图问题讨论 2025年10月27日.md | [[4-Archives/Notes/Feishu/云空间/何宜峰的个人文档/智能纪要：8084接口、列表及地图问题讨论 2025年10月27日]] | [飞书](https://reliablesense.feishu.cn/docx/Vyf1d9xi7oSdZVxPUrAcWMIOnEf) | → 提取 | `1-Projects/Work/广州机场/会议纪要/`  |
| 智能纪要：云江项目任务方案及后续安排会 2025年10月27日.md | [[4-Archives/Notes/Feishu/云空间/何宜峰的个人文档/智能纪要：云江项目任务方案及后续安排会 2025年10月27日]] | [飞书](https://reliablesense.feishu.cn/docx/Satnd39gXoHjQYxUzW6cVWvinOe) | → 提取 | `1-Projects/Work/广州机场/会议纪要/`  |
| 智能纪要：分子构建与插件使用安装讨论 2025年11月6日.md | [[4-Archives/Notes/Feishu/云空间/何宜峰的个人文档/智能纪要：分子构建与插件使用安装讨论 2025年11月6日]] | [飞书](https://reliablesense.feishu.cn/docx/XmvYdGxTLoHZpJxmb0pcEgZNnbc) | → 提取 | `1-Projects/Work/广州机场/会议纪要/`  |
| 智能纪要：数据同步、订阅测试及新数据格式讨论 2025年10月28日.md | [[4-Archives/Notes/Feishu/云空间/何宜峰的个人文档/智能纪要：数据同步、订阅测试及新数据格式讨论 2025年10月28日]] | [飞书](https://reliablesense.feishu.cn/docx/LqMIdcq9Nod1nlxOYGvcxUVwnqh) | → 提取 | `1-Projects/Work/广州机场/会议纪要/`  |
| 智能纪要：管理内容、分支及注释问题讨论 2025年11月6日.md | [[4-Archives/Notes/Feishu/云空间/何宜峰的个人文档/智能纪要：管理内容、分支及注释问题讨论 2025年11月6日]] | [飞书](https://reliablesense.feishu.cn/docx/OCCsdy2coohBdmxcVdVcPIlNnof) | → 提取 | `1-Projects/Work/广州机场/会议纪要/`  |
| 智能纪要：管理员数据库表及任务归属问题讨论 2025年10月30日.md | [[4-Archives/Notes/Feishu/云空间/何宜峰的个人文档/智能纪要：管理员数据库表及任务归属问题讨论 2025年10月30日]] | [飞书](https://reliablesense.feishu.cn/docx/QDWldDLdjoNx0Bx291QcPcBxnbS) | → 提取 | `1-Projects/Work/广州机场/会议纪要/`  |
| 智能纪要：项目依赖、日志及硬盘问题会议 2025年10月13日.md | [[4-Archives/Notes/Feishu/云空间/何宜峰的个人文档/智能纪要：项目依赖、日志及硬盘问题会议 2025年10月13日]] | [飞书](https://reliablesense.feishu.cn/docx/SVJodwciFoT6vGxQGiicoCpBnjg) | → 提取 | `1-Projects/Work/广州机场/会议纪要/`  |
| 月度纪要小结｜10月27日 - 11月21日.md | [[4-Archives/Notes/Feishu/云空间/何宜峰的个人文档/月度纪要小结｜10月27日 - 11月21日]] | [飞书](https://reliablesense.feishu.cn/docx/QTUOdDTqkoDqZJxzzbncYw4On2d) | → 提取 | `4-Archives/Areas/Work/团队管理/团队成员/何宜峰/` |
| 月度纪要小结｜11月24日 - 12月19日.md | [[4-Archives/Notes/Feishu/云空间/何宜峰的个人文档/月度纪要小结｜11月24日 - 12月19日]] | [飞书](https://reliablesense.feishu.cn/docx/DkxkdBBbFoSr5Axve4GcwIvenjg) | → 提取 | `4-Archives/Areas/Work/团队管理/团队成员/何宜峰/` |
| 近期会议速递｜要点概览 2025年10月20日.md | [[4-Archives/Notes/Feishu/云空间/何宜峰的个人文档/近期会议速递｜要点概览 2025年10月20日]] | [飞书](https://reliablesense.feishu.cn/docx/S1nAdbGeSo5l7hxb058cIhEwnOd) | → 提取 | `4-Archives/Areas/Work/团队管理/团队成员/何宜峰/` |
| 近期会议速递｜要点概览 2025年11月17日.md | [[4-Archives/Notes/Feishu/云空间/何宜峰的个人文档/近期会议速递｜要点概览 2025年11月17日]] | [飞书](https://reliablesense.feishu.cn/docx/LmlMdaCD1oibasxwfDWcMTVenOh) | → 提取 | `4-Archives/Areas/Work/团队管理/团队成员/何宜峰/` |
| 近期会议速递｜要点概览 2025年11月3日.md | [[4-Archives/Notes/Feishu/云空间/何宜峰的个人文档/近期会议速递｜要点概览 2025年11月3日]] | [飞书](https://reliablesense.feishu.cn/docx/CYC3dSQq8oV0jZxBvEncpFYZnKA) | → 提取 | `4-Archives/Areas/Work/团队管理/团队成员/何宜峰/` |
| 近期会议速递｜要点概览 2025年12月15日.md | [[4-Archives/Notes/Feishu/云空间/何宜峰的个人文档/近期会议速递｜要点概览 2025年12月15日]] | [飞书](https://reliablesense.feishu.cn/docx/U7tmdjSSsoQWqTxMbYFcRLVtnxb) | → 提取 | `4-Archives/Areas/Work/团队管理/团队成员/何宜峰/` |
| 近期会议速递｜要点概览 2025年12月22日.md | [[4-Archives/Notes/Feishu/云空间/何宜峰的个人文档/近期会议速递｜要点概览 2025年12月22日]] | [飞书](https://reliablesense.feishu.cn/docx/NJnQd8imdoNmXhxcmjccqoAwnxb) | → 提取 | `4-Archives/Areas/Work/团队管理/团队成员/何宜峰/` |

### 陈子杰的个人文档（43 个文件）

| 文件 | 本地路径 | 飞书链接 | 分类 | 目标路径 |
|------|---------|---------|------|---------|
| 2023-05-07 20-54-59.mkv | [[4-Archives/Notes/Feishu/云空间/陈子杰的个人文档/2023-05-07 20-54-59.mkv]] | [飞书](https://reliablesense.feishu.cn/file/BRc2bmrbKoPzjvxIKmPcBoOFnof) | → 提取 | - | 录屏文件 |
| oemusers.xlsx | [[4-Archives/Notes/Feishu/云空间/陈子杰的个人文档/oemusers.xlsx]] | [飞书](https://reliablesense.feishu.cn/sheets/GBc0sFzfKhEtBztmsAPcp5m5n4w) | → 提取 | `1-Projects/Work/广州机场/` | 广州机场 OEM 用户数据 |
| t_poi_type.xlsx | [[4-Archives/Notes/Feishu/云空间/陈子杰的个人文档/t_poi_type.xlsx]] | [飞书](https://reliablesense.feishu.cn/sheets/EKkcsQr7MhV8S7teOsTcf1ISnUc) | → 提取 | `2-Areas/Work/产品研发/` | 产品 POI 类型数据 |
| 内蒙新太项目（新钢联）的视频会议 2025年2月7日 - 智能纪要.md | [[4-Archives/Notes/Feishu/云空间/陈子杰的个人文档/内蒙新太项目（新钢联）的视频会议 2025年2月7日 - 智能纪要]] | [飞书](https://reliablesense.feishu.cn/docx/W7Jid5OiUopoqcxNqJbc8ichnnf) | 新太项目 | `1-Projects/Work/新太项目/` |
| 室内定位系统工作进度.xlsx | [[4-Archives/Notes/Feishu/云空间/陈子杰的个人文档/室内定位系统工作进度.xlsx]] | [飞书](https://reliablesense.feishu.cn/sheets/Xl6HsOeCMhUrDwtMewMcElDGnyd) | → 提取 | `2-Areas/Work/产品研发/` | 产品开发进度 |
| 文字记录：上海东海模型修复及接入方案研讨 2025年5月15日.md | [[4-Archives/Notes/Feishu/云空间/陈子杰的个人文档/文字记录：上海东海模型修复及接入方案研讨 2025年5月15日]] | [飞书](https://reliablesense.feishu.cn/docx/Ky4Ldt5hFoe6mQxg8lrctpCRngh) | → 提取 | `1-Projects/Work/广州机场/会议纪要/`  |
| 文字记录：数据、页面状态及功能处理会议 2025年9月17日.md | [[4-Archives/Notes/Feishu/云空间/陈子杰的个人文档/文字记录：数据、页面状态及功能处理会议 2025年9月17日]] | [飞书](https://reliablesense.feishu.cn/docx/O7UVdlfMSoMkZbxVyWic5N0bnBf) | → 提取 | `2-Areas/Work/产品研发/会议纪要/`  |
| 文字记录：移动应用与 TCDM 会议讨论  2025年6月3日.md | [[4-Archives/Notes/Feishu/云空间/陈子杰的个人文档/文字记录：移动应用与 TCDM 会议讨论  2025年6月3日]] | [飞书](https://reliablesense.feishu.cn/docx/JmwhduJIPouIxsx7Sh6cH5ZOnph) | 广州机场 | `1-Projects/Work/广州机场/` |
| 文字记录：陈子杰的视频会议 2025年2月24日.md | [[4-Archives/Notes/Feishu/云空间/陈子杰的个人文档/文字记录：陈子杰的视频会议 2025年2月24日]] | [飞书](https://reliablesense.feishu.cn/docx/JhwjdqDfJoBMExxV9btciKO3nhf) | → 提取 | `1-Projects/Work/新太项目/会议纪要/`  |
| 文字记录：黄佳琪软件工作安排及指导会议 2025年4月11日.md | [[4-Archives/Notes/Feishu/云空间/陈子杰的个人文档/文字记录：黄佳琪软件工作安排及指导会议 2025年4月11日]] | [飞书](https://reliablesense.feishu.cn/docx/MWlJdSwz6o30ykxZGMPcLmdin0f) | → 提取 | `1-Projects/Work/广州机场/会议纪要/`  |
| 智能纪要：上海东海模型修复及接入方案研讨 2025年5月15日.md | [[4-Archives/Notes/Feishu/云空间/陈子杰的个人文档/智能纪要：上海东海模型修复及接入方案研讨 2025年5月15日]] | [飞书](https://reliablesense.feishu.cn/docx/BT99d8bucoUruTx4rvZcYbRbnff) | → 提取 | `1-Projects/Work/广州机场/会议纪要/`  |
| 智能纪要：数据、页面状态及功能处理会议 2025年9月17日.md | [[4-Archives/Notes/Feishu/云空间/陈子杰的个人文档/智能纪要：数据、页面状态及功能处理会议 2025年9月17日]] | [飞书](https://reliablesense.feishu.cn/docx/KliDdAtzionSN1xuPXic7YWynUd) | → 提取 | `2-Areas/Work/产品研发/会议纪要/`  |
| 智能纪要：移动应用与 TCDM 会议讨论 2025年6月3日.md | [[4-Archives/Notes/Feishu/云空间/陈子杰的个人文档/智能纪要：移动应用与 TCDM 会议讨论 2025年6月3日]] | [飞书](https://reliablesense.feishu.cn/docx/VARrddtC3oOlFMxENAFcoGBKnl9) | 广州机场 | `1-Projects/Work/广州机场/` |
| 智能纪要：陈子杰的视频会议 2025年2月24日.md | [[4-Archives/Notes/Feishu/云空间/陈子杰的个人文档/智能纪要：陈子杰的视频会议 2025年2月24日]] | [飞书](https://reliablesense.feishu.cn/docx/XVxUdVtaSo0wu6xtY3Uc7GdHnrc) | → 提取 | `1-Projects/Work/新太项目/会议纪要/`  |
| 智能纪要：黄佳琪软件工作安排及指导会议 2025年4月11日.md | [[4-Archives/Notes/Feishu/云空间/陈子杰的个人文档/智能纪要：黄佳琪软件工作安排及指导会议 2025年4月11日]] | [飞书](https://reliablesense.feishu.cn/docx/KFRAdFWTjoSKrIxLDPFcQH3Oncg) | → 提取 | `1-Projects/Work/广州机场/会议纪要/`  |
| 月度纪要小结（播客版）｜5月26日 - 6月20日.md | [[4-Archives/Notes/Feishu/云空间/陈子杰的个人文档/月度纪要小结（播客版）｜5月26日 - 6月20日]] | [飞书](https://reliablesense.feishu.cn/docx/GPoCdJwSDoTzFSx3xsScQEPynCh) | → 提取 | `4-Archives/Areas/Work/团队管理/团队成员/陈子杰/` |
| 近期会议速递｜要点概览  2024年12月16日.md | [[4-Archives/Notes/Feishu/云空间/陈子杰的个人文档/近期会议速递｜要点概览  2024年12月16日]] | [飞书](https://reliablesense.feishu.cn/docx/Z21kdH9RRoWSlXxKCllcwOp9nxe) | → 提取 | `4-Archives/Areas/Work/团队管理/团队成员/陈子杰/` |
| 近期会议速递｜要点概览  2024年12月23日.md | [[4-Archives/Notes/Feishu/云空间/陈子杰的个人文档/近期会议速递｜要点概览  2024年12月23日]] | [飞书](https://reliablesense.feishu.cn/docx/BGWhdLW32oWgRgxno7ncyfNNnSd) | → 提取 | `4-Archives/Areas/Work/团队管理/团队成员/陈子杰/` |
| 近期会议速递｜要点概览  2024年12月30日.md | [[4-Archives/Notes/Feishu/云空间/陈子杰的个人文档/近期会议速递｜要点概览  2024年12月30日]] | [飞书](https://reliablesense.feishu.cn/docx/W7MhdWyHeoTWeZxbwVbcG6Whndh) | → 提取 | `4-Archives/Areas/Work/团队管理/团队成员/陈子杰/` |
| 近期会议速递｜要点概览  2025年1月13日.md | [[4-Archives/Notes/Feishu/云空间/陈子杰的个人文档/近期会议速递｜要点概览  2025年1月13日]] | [飞书](https://reliablesense.feishu.cn/docx/PQffdQ2NOo3Txyx10TVcQ3UYnbg) | → 提取 | `4-Archives/Areas/Work/团队管理/团队成员/陈子杰/` |
| 近期会议速递｜要点概览  2025年1月20日.md | [[4-Archives/Notes/Feishu/云空间/陈子杰的个人文档/近期会议速递｜要点概览  2025年1月20日]] | [飞书](https://reliablesense.feishu.cn/docx/DCOHdnmZKoZE21xlQ01c7d3Unoe) | → 提取 | `4-Archives/Areas/Work/团队管理/团队成员/陈子杰/` |
| 近期会议速递｜要点概览  2025年1月27日.md | [[4-Archives/Notes/Feishu/云空间/陈子杰的个人文档/近期会议速递｜要点概览  2025年1月27日]] | [飞书](https://reliablesense.feishu.cn/docx/FeykdvimxoVR6qxCjtAcpMFinxe) | → 提取 | `4-Archives/Areas/Work/团队管理/团队成员/陈子杰/` |
| 近期会议速递｜要点概览  2025年1月6日.md | [[4-Archives/Notes/Feishu/云空间/陈子杰的个人文档/近期会议速递｜要点概览  2025年1月6日]] | [飞书](https://reliablesense.feishu.cn/docx/L35XdsGSSoygobxzcHjctf4Mnjd) | → 提取 | `4-Archives/Areas/Work/团队管理/团队成员/陈子杰/` |
| 近期会议速递｜要点概览  2025年2月10日.md | [[4-Archives/Notes/Feishu/云空间/陈子杰的个人文档/近期会议速递｜要点概览  2025年2月10日]] | [飞书](https://reliablesense.feishu.cn/docx/NAkkdVvn0oT5TNxjBvkcNNkmnKe) | → 提取 | `4-Archives/Areas/Work/团队管理/团队成员/陈子杰/` |
| 近期会议速递｜要点概览  2025年2月17日.md | [[4-Archives/Notes/Feishu/云空间/陈子杰的个人文档/近期会议速递｜要点概览  2025年2月17日]] | [飞书](https://reliablesense.feishu.cn/docx/Gna2dHIXQoREOUxBOXbcEYZZnqr) | → 提取 | `4-Archives/Areas/Work/团队管理/团队成员/陈子杰/` |
| 近期会议速递｜要点概览  2025年2月24日.md | [[4-Archives/Notes/Feishu/云空间/陈子杰的个人文档/近期会议速递｜要点概览  2025年2月24日]] | [飞书](https://reliablesense.feishu.cn/docx/ANZcdUqC5opTD0xfs7Cc6OuDnPh) | → 提取 | `4-Archives/Areas/Work/团队管理/团队成员/陈子杰/` |
| 近期会议速递｜要点概览  2025年3月17日.md | [[4-Archives/Notes/Feishu/云空间/陈子杰的个人文档/近期会议速递｜要点概览  2025年3月17日]] | [飞书](https://reliablesense.feishu.cn/docx/LICQdsN5AoOPUax19UJckYmQneb) | → 提取 | `4-Archives/Areas/Work/团队管理/团队成员/陈子杰/` |
| 近期会议速递｜要点概览  2025年3月3日.md | [[4-Archives/Notes/Feishu/云空间/陈子杰的个人文档/近期会议速递｜要点概览  2025年3月3日]] | [飞书](https://reliablesense.feishu.cn/docx/UscVdJyLcoGhT9xlVCqcm6pSnPh) | → 提取 | `4-Archives/Areas/Work/团队管理/团队成员/陈子杰/` |
| 近期会议速递｜要点概览  2025年4月14日.md | [[4-Archives/Notes/Feishu/云空间/陈子杰的个人文档/近期会议速递｜要点概览  2025年4月14日]] | [飞书](https://reliablesense.feishu.cn/docx/NmAXd423Xo5FbZxFQppcvft6nzf) | → 提取 | `4-Archives/Areas/Work/团队管理/团队成员/陈子杰/` |
| 近期会议速递｜要点概览  2025年4月21日.md | [[4-Archives/Notes/Feishu/云空间/陈子杰的个人文档/近期会议速递｜要点概览  2025年4月21日]] | [飞书](https://reliablesense.feishu.cn/docx/ZIcAduwBcoXGuMxS9q8cXSccn9g) | → 提取 | `4-Archives/Areas/Work/团队管理/团队成员/陈子杰/` |
| 近期会议速递｜要点概览  2025年4月7日.md | [[4-Archives/Notes/Feishu/云空间/陈子杰的个人文档/近期会议速递｜要点概览  2025年4月7日]] | [飞书](https://reliablesense.feishu.cn/docx/QsCbdNHr8oPl4Xx0uLicu9GUnAe) | → 提取 | `4-Archives/Areas/Work/团队管理/团队成员/陈子杰/` |
| 近期会议速递｜要点概览  2025年5月12日.md | [[4-Archives/Notes/Feishu/云空间/陈子杰的个人文档/近期会议速递｜要点概览  2025年5月12日]] | [飞书](https://reliablesense.feishu.cn/docx/LxV2d0o1VoXVmyxwBdfcFsTanLb) | → 提取 | `4-Archives/Areas/Work/团队管理/团队成员/陈子杰/` |
| 近期会议速递｜要点概览  2025年5月19日.md | [[4-Archives/Notes/Feishu/云空间/陈子杰的个人文档/近期会议速递｜要点概览  2025年5月19日]] | [飞书](https://reliablesense.feishu.cn/docx/VNq6dqMR2opizBx1E1HcyqVinBg) | → 提取 | `4-Archives/Areas/Work/团队管理/团队成员/陈子杰/` |
| 近期会议速递｜要点概览  2025年6月9日.md | [[4-Archives/Notes/Feishu/云空间/陈子杰的个人文档/近期会议速递｜要点概览  2025年6月9日]] | [飞书](https://reliablesense.feishu.cn/docx/WCAQdiwTDoYuKexlMJ0cvK8MnFb) | → 提取 | `4-Archives/Areas/Work/团队管理/团队成员/陈子杰/` |
| 近期会议速递｜要点概览 2025年9月22日.md | [[4-Archives/Notes/Feishu/云空间/陈子杰的个人文档/近期会议速递｜要点概览 2025年9月22日]] | [飞书](https://reliablesense.feishu.cn/docx/Ij7ddnCqxoTyHsxBjRecEp4JnJc) | → 提取 | `4-Archives/Areas/Work/团队管理/团队成员/陈子杰/` |
| 问题记录-2023-09-22.xlsx | [[4-Archives/Notes/Feishu/云空间/陈子杰的个人文档/问题记录-2023-09-22.xlsx]] | [飞书](https://reliablesense.feishu.cn/sheets/ILedsU7eShMXojtZmy0cTiHln9c) | → 提取 | - | 历史问题记录 |
| 需求及 Bug 管理.xlsx | [[4-Archives/Notes/Feishu/云空间/陈子杰的个人文档/需求及 Bug 管理.xlsx]] | [飞书](https://reliablesense.feishu.cn/base/BSDnb80vUaGm4hsjM06cIE0bncD) | → 提取 | `2-Areas/Work/产品研发/` | 需求和 Bug 管理 |
| 移动应用平台开发与测试进展汇报.pdf | [[4-Archives/Notes/Feishu/云空间/陈子杰的个人文档/广州机场-移动应用平台/移动应用平台开发与测试进展汇报.pdf]] | [飞书](https://reliablesense.feishu.cn/file/Kkf6bl2V4oAr5vx5m4QccUDDniI) | 广州机场 | `1-Projects/Work/广州机场/` |
| 移动终端目前缺失功能.xlsx | [[4-Archives/Notes/Feishu/云空间/陈子杰的个人文档/广州机场-移动应用平台/移动终端目前缺失功能.xlsx]] | [飞书](https://reliablesense.feishu.cn/base/RLRqbFnrPaokuRsVtTbcjkMLnZd) | → 提取 | `1-Projects/Work/广州机场/` | 广州机场移动应用缺失功能 |
| app_store_back-main.zip | [[4-Archives/Notes/Feishu/云空间/陈子杰的个人文档/广州机场-移动应用平台/appstore/app_store_back-main.zip]] | [飞书](https://reliablesense.feishu.cn/file/Ugv8bHqsAosoRmxmBQxcUBcOnDb) | → 提取 | `1-Projects/Work/广州机场/` | 广州机场应用商店后端代码 |
| app_store_flutter_module-main.zip | [[4-Archives/Notes/Feishu/云空间/陈子杰的个人文档/广州机场-移动应用平台/appstore/app_store_flutter_module-main.zip]] | [飞书](https://reliablesense.feishu.cn/file/RFX9bi65aoymAAxNFgUcHtlRn5f) | → 提取 | `1-Projects/Work/广州机场/` | 广州机场应用商店 Flutter 模块 |
| appstoreaf-main.zip | [[4-Archives/Notes/Feishu/云空间/陈子杰的个人文档/广州机场-移动应用平台/appstore/appstoreaf-main.zip]] | [飞书](https://reliablesense.feishu.cn/file/Wv5yb07DVon7EvxNBOPc6yFDn0c) | → 提取 | `1-Projects/Work/广州机场/` | 广州机场应用商店前端代码 |
| readme.txt | [[4-Archives/Notes/Feishu/云空间/陈子杰的个人文档/广州机场-移动应用平台/appstore/readme.txt]] | [飞书](https://reliablesense.feishu.cn/file/KsdVbaNAvo4hXrx7rEhc1x3pnch) | → 提取 | `1-Projects/Work/广州机场/` | 广州机场应用商店说明 |

### 孙永霖的个人文档（24 个文件）

| 文件 | 本地路径 | 飞书链接 | 分类 | 目标路径 |
|------|---------|---------|------|---------|
| 地图管理的问题.md | [[4-Archives/Notes/Feishu/云空间/孙永霖的个人文档/地图管理问题/地图管理的问题]] | [飞书](https://reliablesense.feishu.cn/docx/doxcnesMSLP6dXGeKzB6EibeSCx) | 留归档 | - |
| Help Center Template.md | [[4-Archives/Notes/Feishu/云空间/孙永霖的个人文档/doc/Help Center Template]] | [飞书](https://reliablesense.feishu.cn/docx/DaQhd5gMxowrj6xCReccmQKanIg) | → 提取 | `2-Areas/Work/产品研发/` | 产品帮助中心模板（英文） |
| SaaS使用手册V4 new 英文.docx | [[4-Archives/Notes/Feishu/云空间/孙永霖的个人文档/doc/SaaS使用手册V4 new 英文.docx]] | [飞书](https://reliablesense.feishu.cn/file/boxcnrTNYMWwqMq49WzzapEj30g) | → 提取 | `2-Areas/Work/产品研发/` | 产品 SaaS 英文使用手册 |
| SaaS使用手册V4 new.docx | [[4-Archives/Notes/Feishu/云空间/孙永霖的个人文档/doc/SaaS使用手册V4 new.docx]] | [飞书](https://reliablesense.feishu.cn/file/boxcnKrzYX5prPEiZIv33AL6mlc) | → 提取 | `2-Areas/Work/产品研发/` | 产品 SaaS 使用手册 |
| saas英文版.md | [[4-Archives/Notes/Feishu/云空间/孙永霖的个人文档/doc/saas英文版]] | [飞书](https://reliablesense.feishu.cn/docx/LZgYdpRnzouGpKxnOdZc4vDRnPg) | → 提取 | `2-Areas/Work/产品研发/` | 产品 SaaS 英文版文档 |
| boxcn5whZmWzb6xt0T2Bfwbo8Qg.png | [[4-Archives/Notes/Feishu/云空间/孙永霖的个人文档/doc/Attachments/boxcn5whZmWzb6xt0T2Bfwbo8Qg.png]] | 跟随文档 | - | 文档内嵌图片 |
| boxcnAXiWzdFee83pTIlUz4I2sb.png | [[4-Archives/Notes/Feishu/云空间/孙永霖的个人文档/doc/Attachments/boxcnAXiWzdFee83pTIlUz4I2sb.png]] | 跟随文档 | - | 文档内嵌图片 |
| boxcnCvKWqI9Vu1CBRZ1hjkLvEd.png | [[4-Archives/Notes/Feishu/云空间/孙永霖的个人文档/doc/Attachments/boxcnCvKWqI9Vu1CBRZ1hjkLvEd.png]] | 跟随文档 | - | 文档内嵌图片 |
| boxcnDkc7WQyBowbMfqCy6c0X0d.png | [[4-Archives/Notes/Feishu/云空间/孙永霖的个人文档/doc/Attachments/boxcnDkc7WQyBowbMfqCy6c0X0d.png]] | 跟随文档 | - | 文档内嵌图片 |
| boxcnLYHovN34VDGy5EkCL1Nawh.png | [[4-Archives/Notes/Feishu/云空间/孙永霖的个人文档/doc/Attachments/boxcnLYHovN34VDGy5EkCL1Nawh.png]] | 跟随文档 | - | 文档内嵌图片 |
| boxcnMENxDxKZyWmFxcpzm7KRRf.png | [[4-Archives/Notes/Feishu/云空间/孙永霖的个人文档/doc/Attachments/boxcnMENxDxKZyWmFxcpzm7KRRf.png]] | 跟随文档 | - | 文档内嵌图片 |
| boxcnODrGjqz5ocEqaTAbKfZvVe.png | [[4-Archives/Notes/Feishu/云空间/孙永霖的个人文档/doc/Attachments/boxcnODrGjqz5ocEqaTAbKfZvVe.png]] | 跟随文档 | - | 文档内嵌图片 |
| boxcnQlrEgwhWvStw47Xr06QpAh.png | [[4-Archives/Notes/Feishu/云空间/孙永霖的个人文档/doc/Attachments/boxcnQlrEgwhWvStw47Xr06QpAh.png]] | 跟随文档 | - | 文档内嵌图片 |
| boxcnQy1uAaY57GtvYo7wT2oAwd.png | [[4-Archives/Notes/Feishu/云空间/孙永霖的个人文档/doc/Attachments/boxcnQy1uAaY57GtvYo7wT2oAwd.png]] | 跟随文档 | - | 文档内嵌图片 |
| boxcnRN9pcf6QWygTj7OPyeGaxe.png | [[4-Archives/Notes/Feishu/云空间/孙永霖的个人文档/doc/Attachments/boxcnRN9pcf6QWygTj7OPyeGaxe.png]] | 跟随文档 | - | 文档内嵌图片 |
| boxcnT6Muz2GbtaT31e2Gl0ADPe.png | [[4-Archives/Notes/Feishu/云空间/孙永霖的个人文档/doc/Attachments/boxcnT6Muz2GbtaT31e2Gl0ADPe.png]] | 跟随文档 | - | 文档内嵌图片 |
| boxcncQ5fIRU875xINJTZu1lNTf.png | [[4-Archives/Notes/Feishu/云空间/孙永霖的个人文档/doc/Attachments/boxcncQ5fIRU875xINJTZu1lNTf.png]] | 跟随文档 | - | 文档内嵌图片 |
| boxcnh6Uax5jwOgMsXzcoG7thuh.png | [[4-Archives/Notes/Feishu/云空间/孙永霖的个人文档/doc/Attachments/boxcnh6Uax5jwOgMsXzcoG7thuh.png]] | 跟随文档 | - | 文档内嵌图片 |
| boxcnkOcZLQt9nXWC1e1YWNM3fc.png | [[4-Archives/Notes/Feishu/云空间/孙永霖的个人文档/doc/Attachments/boxcnkOcZLQt9nXWC1e1YWNM3fc.png]] | 跟随文档 | - | 文档内嵌图片 |
| boxcnlehyCUpSJKoD0omuclUGue.png | [[4-Archives/Notes/Feishu/云空间/孙永霖的个人文档/doc/Attachments/boxcnlehyCUpSJKoD0omuclUGue.png]] | 跟随文档 | - | 文档内嵌图片 |
| boxcnqphPdO91JLopkr035K9jUc.png | [[4-Archives/Notes/Feishu/云空间/孙永霖的个人文档/doc/Attachments/boxcnqphPdO91JLopkr035K9jUc.png]] | 跟随文档 | - | 文档内嵌图片 |
| boxcnyLy0jFnbi6yeVcHodc6bsf.png | [[4-Archives/Notes/Feishu/云空间/孙永霖的个人文档/doc/Attachments/boxcnyLy0jFnbi6yeVcHodc6bsf.png]] | 跟随文档 | - | 文档内嵌图片 |
| boxcnyULVjHIEbES042oawOsZag.png | [[4-Archives/Notes/Feishu/云空间/孙永霖的个人文档/doc/Attachments/boxcnyULVjHIEbES042oawOsZag.png]] | 跟随文档 | - | 文档内嵌图片 |
| boxcnzeFMj9LWq9NabhlExDF2H3.png | [[4-Archives/Notes/Feishu/云空间/孙永霖的个人文档/doc/Attachments/boxcnzeFMj9LWq9NabhlExDF2H3.png]] | 跟随文档 | - | 文档内嵌图片 |



---

## 四、莱讯科技/项目运维管理

### 4a. 运维文档

| 文件 | 本地路径 | 飞书链接 | 决策 | 目标路径 |
|------|---------|---------|------|---------|
| 前端运维手册.md | [[4-Archives/Notes/Feishu/云空间/莱讯科技/项目运维管理/运维文档/前端运维手册]] | [飞书](https://reliablesense.feishu.cn/docx/CT42dawUcoGhYLx2UIjcjVuTnYf) | → 提取 | `2-Areas/Work/运维管理/前端运维手册.md` |
| 后端运维手册.md | [[4-Archives/Notes/Feishu/云空间/莱讯科技/项目运维管理/运维文档/后端运维手册]] | [飞书](https://reliablesense.feishu.cn/docx/OGLIdpLsJoaVecxBWuZcD41xnEf) | → 提取 | `2-Areas/Work/运维管理/后端运维手册.md` |
| 新太运维手册.md | [[4-Archives/Notes/Feishu/云空间/莱讯科技/项目运维管理/运维文档/新太运维手册]] | [飞书](https://reliablesense.feishu.cn/docx/NFOVdlWSFoZJ91xTXMbcvY7mnSg) | → 提取 | `1-Projects/Work/新太项目/新太运维手册.md` | 新太项目专用运维手册 |
| 区域功能后端开发文档.md | [[4-Archives/Notes/Feishu/云空间/莱讯科技/项目运维管理/运维文档/区域功能后端开发文档]] | [飞书](https://reliablesense.feishu.cn/docx/JknBdu9hEon9gJxuC4ycEBhOnjb) | ⚠️ 待确认 | 见 [[1-Projects/Personal/笔记迁移/阶段二-待确认分类]] |
| 数据库操作说明.md | [[4-Archives/Notes/Feishu/云空间/莱讯科技/项目运维管理/运维文档/数据库操作说明]] | [飞书](https://reliablesense.feishu.cn/docx/KjS8dWiAvoxdCIxgkEEcDktinSU) | → 提取 | `2-Areas/Work/运维管理/数据库操作说明.md` |
| 数据库 pg-backup 使用方法说明.md | [[4-Archives/Notes/Feishu/云空间/莱讯科技/项目运维管理/运维文档/数据库 pg-backup 使用方法说明]] | [飞书](https://reliablesense.feishu.cn/docx/LfEodRSmnoOopsxju9kckxCtnng) | → 提取 | `2-Areas/Work/运维管理/pg-backup使用方法.md` |
| 综合定位系统运维白皮书.md | [[4-Archives/Notes/Feishu/云空间/莱讯科技/项目运维管理/运维文档/综合定位系统运维白皮书]] | [飞书](https://reliablesense.feishu.cn/docx/AMuadobIrozdlZxG96gcHgtPnxe) | → 提取 | `1-Projects/Work/广州机场/综合定位系统运维白皮书.md` | 广州机场运维白皮书 |
| 综合定位系统运维白皮书编写内容框架.md | [[4-Archives/Notes/Feishu/云空间/莱讯科技/项目运维管理/运维文档/综合定位系统运维白皮书编写内容框架]] | [飞书](https://reliablesense.feishu.cn/docx/GkcQdk58kocgF7x6ytNc4ikYnvg) | → 提取 | `1-Projects/Work/广州机场/综合定位系统运维白皮书编写内容框架.md` | 广州机场 |
| 移动应用平台运维白皮书编写内容框架.md | [[4-Archives/Notes/Feishu/云空间/莱讯科技/项目运维管理/运维文档/移动应用平台运维白皮书编写内容框架]] | [飞书](https://reliablesense.feishu.cn/docx/AhnkdGgzroBd8Cx9KxDctcGjnAg) | → 提取 | `1-Projects/Work/广州机场/移动应用平台运维白皮书编写内容框架.md` | 广州机场 |
| 综合定位系统进程清单编写内容框架.md | [[4-Archives/Notes/Feishu/云空间/莱讯科技/项目运维管理/运维文档/综合定位系统进程清单编写内容框架]] | [飞书](https://reliablesense.feishu.cn/docx/NibpdCR4coY77ex8qIrcRo7Dnjh) | → 提取 | `1-Projects/Work/广州机场/综合定位系统进程清单编写内容框架.md` | 广州机场 |
| 综合定位系统配置清单编写内容框架.md | [[4-Archives/Notes/Feishu/云空间/莱讯科技/项目运维管理/运维文档/综合定位系统配置清单编写内容框架]] | [飞书](https://reliablesense.feishu.cn/docx/JUInd4Gmwo2B29xizZQcJtq0nKe) | → 提取 | `1-Projects/Work/广州机场/综合定位系统配置清单编写内容框架.md` | 广州机场 |
| 移动应用平台进程清单编写内容框架.md | [[4-Archives/Notes/Feishu/云空间/莱讯科技/项目运维管理/运维文档/移动应用平台进程清单编写内容框架]] | [飞书](https://reliablesense.feishu.cn/docx/YCvydrOqHodVj8xC28EcVVMEnRf) | → 提取 | `1-Projects/Work/广州机场/移动应用平台进程清单编写内容框架.md` | 广州机场 |
| 移动应用平台配置清单编写内容框架.md | [[4-Archives/Notes/Feishu/云空间/莱讯科技/项目运维管理/运维文档/移动应用平台配置清单编写内容框架]] | [飞书](https://reliablesense.feishu.cn/docx/Z5SFdZURjogTZ8xsMf0c5g6enos) | → 提取 | `1-Projects/Work/广州机场/移动应用平台配置清单编写内容框架.md` | 广州机场 |
| 数据库字典注释.xlsx | [[4-Archives/Notes/Feishu/云空间/莱讯科技/项目运维管理/运维文档/数据库字典注释.xlsx]] | [飞书](https://reliablesense.feishu.cn/base/WOpRbugDgamNOKsHG7scmCGSnZg) | → 提取 | `2-Areas/Work/产品研发/数据库字典注释.xlsx` | 产品数据库字典 |

### 4b. 升级文档

| 文件 | 本地路径 | 飞书链接 | 决策 | 目标路径 |
|------|---------|---------|------|---------|
| 升级文档--20260126.md | [[4-Archives/Notes/Feishu/云空间/莱讯科技/项目运维管理/升级文档/升级文档--20260126]] | [飞书](https://reliablesense.feishu.cn/docx/YNlKdlNzMogEq3xSsrscEDcQnqg) | → 提取 | `2-Areas/Work/运维管理/平台升级文档-最新版.md` |
| 导航服务器更新文档.md | [[4-Archives/Notes/Feishu/云空间/莱讯科技/项目运维管理/升级文档/导航服务器更新文档]] | [飞书](https://reliablesense.feishu.cn/docx/Ffvddci64oATfcx9BVbckMwgnnh) | → 提取 | `2-Areas/Work/运维管理/导航服务器更新文档.md` |
| 导航服务器重启文档.md | [[4-Archives/Notes/Feishu/云空间/莱讯科技/项目运维管理/升级文档/导航服务器重启文档]] | [飞书](https://reliablesense.feishu.cn/docx/JusGdT3I3oe2guxmy6SclellnYe) | → 提取 | `2-Areas/Work/运维管理/导航服务器重启文档.md` |
| 2.5升级文档.md | [[4-Archives/Notes/Feishu/云空间/莱讯科技/项目运维管理/升级文档/2.5升级文档]] | [飞书](https://reliablesense.feishu.cn/docx/K2X3di1MWo7vymxykJecGQoZnFb) | 留归档 | 旧版本 |
| 2.4升级版本流程.md | [[4-Archives/Notes/Feishu/云空间/莱讯科技/项目运维管理/升级文档/2.4升级版本流程]] | [飞书](https://reliablesense.feishu.cn/docx/YtbEdiE8boGjbyxtPK3cB3tXnmg) | 留归档 | 旧版本 |

### 4c. 交付文档

| 文件 | 本地路径 | 飞书链接 | 决策 | 目标路径 |
|------|---------|---------|------|---------|
| 部署手册.md | [[4-Archives/Notes/Feishu/云空间/莱讯科技/项目运维管理/交付文档/部署手册]] | [飞书](https://reliablesense.feishu.cn/docs/doxcn3NLUHLJwrpSxVsnCtVfTfd) | → 提取 | `2-Areas/Work/运维管理/部署手册.md` |
| 部署文档离线版.md | [[4-Archives/Notes/Feishu/云空间/莱讯科技/项目运维管理/交付文档/部署文档离线版]] | [飞书](https://reliablesense.feishu.cn/docx/LsHXdLWbmogiEKxZtK5c229nnad) | → 提取 | `2-Areas/Work/运维管理/部署文档-离线版.md` |
| 私有化部署数据库生成步骤.md | [[4-Archives/Notes/Feishu/云空间/莱讯科技/项目运维管理/交付文档/私有化部署数据库生成步骤]] | [飞书](https://reliablesense.feishu.cn/docx/ArEWdDLrCoeAMpxJV7tc2YC7ntb) | → 提取 | `2-Areas/Work/运维管理/私有化部署-数据库生成步骤.md` |
| 地图交付标准.md | [[4-Archives/Notes/Feishu/云空间/莱讯科技/项目运维管理/交付文档/地图交付标准]] | [飞书](https://reliablesense.feishu.cn/docx/CHvwd4VPboHEtpxyhsWcP7PonPe) | → 提取 | `2-Areas/Work/运维管理/地图交付标准.md` |
| 交接文档.md | [[4-Archives/Notes/Feishu/云空间/莱讯科技/项目运维管理/交付文档/交接文档]] | [飞书](https://reliablesense.feishu.cn/docx/UOvmd7dz4oFkXVxuq3OczvtrnHf) | → 提取 | `2-Areas/Work/运维管理/项目交接文档.md` |
| 中间件实施标准化文档.md | [[4-Archives/Notes/Feishu/云空间/莱讯科技/项目运维管理/交付文档/中间件实施标准化文档]] | [飞书](https://reliablesense.feishu.cn/docx/CmG7d0TpIo93M8xpgWucRUSKnYb) | → 提取 | `2-Areas/Work/运维管理/中间件实施标准化文档.md` |
| 现场测试实施标准化文档.md | [[4-Archives/Notes/Feishu/云空间/莱讯科技/项目运维管理/交付文档/现场测试实施标准化文档]] | [飞书](https://reliablesense.feishu.cn/docx/Xsj8dUH5IoKCRuxYRL8ceVTOnKh) | → 提取 | `2-Areas/Work/运维管理/现场测试实施标准化文档.md` |
| 无动力设备管理系统部署指南.md | [[4-Archives/Notes/Feishu/云空间/莱讯科技/项目运维管理/交付文档/无动力设备管理系统部署指南]] | [飞书](https://reliablesense.feishu.cn/docx/NsKCdYwf3okiEPxw0yScBOeGnNh) | → 提取 | `1-Projects/Work/广州机场/无动力设备管理系统部署指南.md` |
| 验收会议流程.md | [[4-Archives/Notes/Feishu/云空间/莱讯科技/项目运维管理/交付文档/验收会议流程]] | [飞书](https://reliablesense.feishu.cn/docx/F9ufd0xoxoa5n0xXlWdcvRrEnJf) | → 提取 | `2-Areas/Work/业务管理/验收会议流程.md` |
| 验收确认报告.md | [[4-Archives/Notes/Feishu/云空间/莱讯科技/项目运维管理/交付文档/验收确认报告]] | [飞书](https://reliablesense.feishu.cn/docx/CwTrdyjpIoh9CcxFymscde3Jnq6) | → 提取 | `2-Areas/Work/业务管理/验收确认报告-模板.md` |
| 确认报告（软件）.md | [[4-Archives/Notes/Feishu/云空间/莱讯科技/项目运维管理/交付文档/确认报告（软件）]] | [飞书](https://reliablesense.feishu.cn/docx/doxcnljrKooELVNhrut5pZswMzc) | → 提取 | `2-Areas/Work/业务管理/软件确认报告-模板.md` |
| 设计验证报告.md | [[4-Archives/Notes/Feishu/云空间/莱讯科技/项目运维管理/交付文档/设计验证报告]] | [飞书](https://reliablesense.feishu.cn/docx/YbkHdX5zoopuh6xyFHOcNPHFndb) | → 提取 | `2-Areas/Work/业务管理/设计验证报告-模板.md` |
| 管理系统项目验收报告.md | [[4-Archives/Notes/Feishu/云空间/莱讯科技/项目运维管理/交付文档/管理系统项目验收报告]] | [飞书](https://reliablesense.feishu.cn/docx/IF1qd37NdoCGVUxMAi4cw1wynZb) | → 提取 | `2-Areas/Work/业务管理/项目验收报告-模板.md` |
| 用户手册（软件）.md | [[4-Archives/Notes/Feishu/云空间/莱讯科技/项目运维管理/交付文档/用户手册（软件）]] | [飞书](https://reliablesense.feishu.cn/docx/Z3H7dsbrSob9Kfxbw7ZcwloHnJc) | → 提取 | `2-Areas/Work/产品研发/定位平台用户手册.md` |

### 4d. 售后文档

| 文件 | 本地路径 | 飞书链接 | 决策 | 目标路径 |
|------|---------|---------|------|---------|
| 定位平台配置建议-v2.md | [[4-Archives/Notes/Feishu/云空间/莱讯科技/项目运维管理/售后文档/定位平台配置建议-v2]] | [飞书](https://reliablesense.feishu.cn/docx/BQ3fdtAgtoeyEuxvvxScqWCznne) | → 提取 | `2-Areas/Work/运维管理/定位平台配置建议.md` |
| 系统容灾备份方案.md | [[4-Archives/Notes/Feishu/云空间/莱讯科技/项目运维管理/售后文档/系统容灾备份方案]] | [飞书](https://reliablesense.feishu.cn/docx/Na7YdwtkYosbSJxCZyPcMmSlnCe) | → 提取 | `2-Areas/Work/产品研发/系统容灾备份方案.md` |
| 定位平台配置建议.md | [[4-Archives/Notes/Feishu/云空间/莱讯科技/项目运维管理/售后文档/定位平台配置建议]] | [飞书](https://reliablesense.feishu.cn/docx/CAsBdlwMnoWeSvx5IuLciDNrnYF) | 留归档 | 旧版本，被 v2 覆盖 |
| 定位平台配置建议-待完善.md | [[4-Archives/Notes/Feishu/云空间/莱讯科技/项目运维管理/售后文档/定位平台配置建议-待完善]] | [飞书](https://reliablesense.feishu.cn/docx/INAndBfILo5yuMxTmi6cWSOynY7) | 留归档 | 草稿版 |
| 系统容灾备份的方案.md | [[4-Archives/Notes/Feishu/云空间/莱讯科技/项目运维管理/售后文档/系统容灾备份的方案]] | [飞书](https://reliablesense.feishu.cn/docx/Na7YdwtkYosbSJxCZyPcMmSlnCe) | 留归档 | 与上面重复 |
| 系统整改配置表.md | [[4-Archives/Notes/Feishu/云空间/莱讯科技/项目运维管理/售后文档/系统整改配置表]] | [飞书](https://reliablesense.feishu.cn/docx/ZpsNdChggodbeaxLg78cgtRBnGc) | 留归档 | 根目录已有同文件 |
| SOW文件.md | [[4-Archives/Notes/Feishu/云空间/莱讯科技/项目运维管理/售后文档/SOW文件]] | [飞书](https://reliablesense.feishu.cn/docx/JeSsdPfEaoy9exxBeD9cBP0pn8M) | → 提取 | `2-Areas/Work/业务管理/SOW文件模板.md` | 项目 SOW 模板 |

### 4e. 集群资料

所有 `*集群.md` 文件（约 20 个）→ ⚠️ 待确认，见 [[1-Projects/Personal/笔记迁移/阶段二-待确认分类]]。

| 文件 | 本地路径 | 飞书链接 | 决策 | 目标路径 |
|------|---------|---------|------|---------|
| cnnc_qshdz集群.md | [[4-Archives/Notes/Feishu/云空间/莱讯科技/项目运维管理/集群资料/cnnc_qshdz集群]] | [飞书](https://reliablesense.feishu.cn/docx/MKTNd2yCQoXoGqxc7ylcO5DcnOd) | ⚠️ 待确认 | 见 [[1-Projects/Personal/笔记迁移/阶段二-待确认分类]] |
| madinat_gat集群.md | [[4-Archives/Notes/Feishu/云空间/莱讯科技/项目运维管理/集群资料/madinat_gat集群]] | [飞书](https://reliablesense.feishu.cn/docx/N7gMdz5ukoIv1Bxj38bcBobInCc) | ⚠️ 待确认 | 同上 |
| madinat_hjc集群.md | [[4-Archives/Notes/Feishu/云空间/莱讯科技/项目运维管理/集群资料/madinat_hjc集群]] | [飞书](https://reliablesense.feishu.cn/docs/doccn6POZJyaWmcGGsWDbuyGARb) | ⚠️ 待确认 | 同上 |
| madinat_hll集群.md | [[4-Archives/Notes/Feishu/云空间/莱讯科技/项目运维管理/集群资料/madinat_hll集群]] | [飞书](https://reliablesense.feishu.cn/docx/JdWOdanhvo8Yl8xAs9pc4xWGnI9) | ⚠️ 待确认 | 同上 |
| madinat_xmc集群.md | [[4-Archives/Notes/Feishu/云空间/莱讯科技/项目运维管理/集群资料/madinat_xmc集群]] | [飞书](https://reliablesense.feishu.cn/docs/doccnRbr2ps3Rpla22Se3M7vnFc) | ⚠️ 待确认 | 同上 |
| madinat_sewd集群.md | [[4-Archives/Notes/Feishu/云空间/莱讯科技/项目运维管理/集群资料/madinat_sewd集群]] | [飞书](https://reliablesense.feishu.cn/docx/SGYudVlmgoEJ0ixNyuhcC94rncf) | ⚠️ 待确认 | 同上 |
| madinat_ntt集群.md | [[4-Archives/Notes/Feishu/云空间/莱讯科技/项目运维管理/集群资料/madinat_ntt集群]] | [飞书](https://reliablesense.feishu.cn/docx/GmiydvdkdotNEWxPntpcFGXZnmd) | ⚠️ 待确认 | 同上 |
| madinat_lyrydw集群.md | [[4-Archives/Notes/Feishu/云空间/莱讯科技/项目运维管理/集群资料/madinat_lyrydw集群]] | [飞书](https://reliablesense.feishu.cn/docx/O5P2dVdVMoc3pWx0GVic4cpenhc) | ⚠️ 待确认 | 同上 |
| madinat_lyhx集群.md | [[4-Archives/Notes/Feishu/云空间/莱讯科技/项目运维管理/集群资料/madinat_lyhx集群]] | [飞书](https://reliablesense.feishu.cn/docx/HDKcdM8myoW1RExNYvac0N4pnuJ) | ⚠️ 待确认 | 同上 |
| xintai_xintai集群.md | [[4-Archives/Notes/Feishu/云空间/莱讯科技/项目运维管理/集群资料/xintai_xintai集群]] | [飞书](https://reliablesense.feishu.cn/docx/MbA7diPTJosC1Gxn3XPcfdMznVg) | ⚠️ 待确认 | 同上 |
| gjtsg_zhdl集群.md | [[4-Archives/Notes/Feishu/云空间/莱讯科技/项目运维管理/集群资料/gjtsg_zhdl集群]] | [飞书](https://reliablesense.feishu.cn/docx/FxjUdZYiyoDWmOxHklhcjvMlnZb) | ⚠️ 待确认 | 同上 |
| shwl_shsg集群.md | [[4-Archives/Notes/Feishu/云空间/莱讯科技/项目运维管理/集群资料/shwl_shsg集群]] | [飞书](https://reliablesense.feishu.cn/docx/MJ2KdoekEoS4jyxuHWfcx2UMnUb) | ⚠️ 待确认 | 同上 |
| shwl_gzhft集群.md | [[4-Archives/Notes/Feishu/云空间/莱讯科技/项目运维管理/集群资料/shwl_gzhft集群]] | [飞书](https://reliablesense.feishu.cn/docx/WY2Hd2wu5oHOI1xJb3UculFSn1d) | ⚠️ 待确认 | 同上 |
| jiexun_autotrader集群.md | [[4-Archives/Notes/Feishu/云空间/莱讯科技/项目运维管理/集群资料/jiexun_autotrader集群]] | [飞书](https://reliablesense.feishu.cn/docx/QNHkdVzTEooNW9xhmvScZ0cKnMd) | ⚠️ 待确认 | 同上 |
| lance_dxgcsy集群.md | [[4-Archives/Notes/Feishu/云空间/莱讯科技/项目运维管理/集群资料/lance_dxgcsy集群]] | [飞书](https://reliablesense.feishu.cn/docx/VN9RdnZIforRPWxYXX5ckt9ynQf) | ⚠️ 待确认 | 同上 |
| erdoswhcyy_erdoswhcyy集群.md | [[4-Archives/Notes/Feishu/云空间/莱讯科技/项目运维管理/集群资料/erdoswhcyy_erdoswhcyy集群]] | [飞书](https://reliablesense.feishu.cn/docx/GW4tda6T9opR4jxGCkUcQA57n7d) | ⚠️ 待确认 | 同上 |
| whjc_whjc集群.md | [[4-Archives/Notes/Feishu/云空间/莱讯科技/项目运维管理/集群资料/whjc_whjc集群]] | [飞书](https://reliablesense.feishu.cn/docx/RKuQdRotpoe3zixaPrWcx9j6nBc) | ⚠️ 待确认 | 同上 |
| cloud 资料.md | [[4-Archives/Notes/Feishu/云空间/莱讯科技/项目运维管理/集群资料/cloud 资料]] | [飞书](https://reliablesense.feishu.cn/docx/QXgzdOibVoySLUxFwtzctoWin0t) | ⚠️ 待确认 | 同上 |
| dev-office 集群.md | [[4-Archives/Notes/Feishu/云空间/莱讯科技/项目运维管理/集群资料/dev-office 集群]] | [飞书](https://reliablesense.feishu.cn/docx/QUtcdDjFjocOxVxiEiRcPQ20nZb) | ⚠️ 待确认 | 同上 |
| online-sh 集群.md | [[4-Archives/Notes/Feishu/云空间/莱讯科技/项目运维管理/集群资料/online-sh 集群]] | [飞书](https://reliablesense.feishu.cn/docs/doccn4ZbY3L0axKO5uic6o278ge) | ⚠️ 待确认 | 同上 |
| middleware-bj 集群.md | [[4-Archives/Notes/Feishu/云空间/莱讯科技/项目运维管理/集群资料/middleware-bj 集群]] | [飞书](https://reliablesense.feishu.cn/docs/doccnqB78BLk2Mq9fvYb9xEEbTd) | ⚠️ 待确认 | 同上 |
| 代理配置操作说明.md | [[4-Archives/Notes/Feishu/云空间/莱讯科技/项目运维管理/集群资料/代理配置操作说明]] | [飞书](https://reliablesense.feishu.cn/docx/LbLPdc4dHoROcnxVSsmcF2sgnyb) | → 提取 | `2-Areas/Work/运维管理/代理配置操作说明.md` |
| 内网穿透 frp 说明.md | [[4-Archives/Notes/Feishu/云空间/莱讯科技/项目运维管理/集群资料/内网穿透 frp 说明]] | [飞书](https://reliablesense.feishu.cn/docx/doxcnAdY9LCLIeBTvI8nVH0St8e) | → 提取 | `2-Areas/Work/运维管理/内网穿透frp说明.md` |

### 4f. 基础设施

| 文件 | 本地路径 | 飞书链接 | 决策 | 目标路径 |
|------|---------|---------|------|---------|
| 综合定位系统技术要求.md | [[4-Archives/Notes/Feishu/云空间/莱讯科技/项目运维管理/基础设施/综合定位系统技术要求]] | [飞书](https://reliablesense.feishu.cn/docx/Gi0MdNC9ToLxM0xfPDCcsKD2nzf) | → 提取 | `1-Projects/Work/广州机场/综合定位系统技术要求.md` | 广州机场技术规格 |
| 系统功能清单.md | [[4-Archives/Notes/Feishu/云空间/莱讯科技/项目运维管理/基础设施/系统功能清单]] | [飞书](https://reliablesense.feishu.cn/docx/WdNtdRhPxoN8VoxwzI5cjocCntK) | → 提取 | `1-Projects/Work/广州机场/综合定位系统功能清单.md` | 广州机场功能列表 |
| 信息安全问题回复.md | [[4-Archives/Notes/Feishu/云空间/莱讯科技/项目运维管理/基础设施/信息安全问题回复]] | [飞书](https://reliablesense.feishu.cn/docx/YIs2dQZh4o3v3axaC0ccR2TInGe) | → 提取 | `1-Projects/Work/广州机场/信息安全问题回复.md` | 含综合定位系统特征，归广州机场 |
| Nexus相关地址.md | [[4-Archives/Notes/Feishu/云空间/莱讯科技/项目运维管理/基础设施/Nexus相关地址]] | [飞书](https://reliablesense.feishu.cn/docs/doccnMTqpCuBzz3UTWyYm6iiF2e) | → 提取 | `2-Areas/Work/运维管理/Nexus相关地址.md` |
| 系统架构图.md | [[4-Archives/Notes/Feishu/云空间/莱讯科技/项目运维管理/基础设施/系统架构图]] | [飞书](https://reliablesense.feishu.cn/docx/IYLtdtwDQoaOetxP9Xkc66jfnPf) | 留归档 | 根目录已提取到产品研发 |
| 系统架构图-v2.md | [[4-Archives/Notes/Feishu/云空间/莱讯科技/项目运维管理/基础设施/系统架构图-v2]] | [飞书](https://reliablesense.feishu.cn/docx/JdRpdI6QKoDIICx8qducxh97nWh) | 留归档 | 根目录已提取到产品研发 |

### 4g. 散落文件

| 文件 | 本地路径 | 飞书链接 | 决策 | 目标路径 |
|------|---------|---------|------|---------|
| 莱讯科技-小程序管理文档.md | [[4-Archives/Notes/Feishu/云空间/莱讯科技/项目运维管理/莱讯科技-小程序管理文档]] | [飞书](https://reliablesense.feishu.cn/docx/JgCpdERLho9N3zxiGpqcQ7GAnov) | → 提取 | `2-Areas/Work/产品研发/小程序管理文档.md` |

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

| 文件 | 本地路径 | 飞书链接 | 决策 | 目标路径 |
|------|---------|---------|------|---------|
| 软件项目资料-定制版.md | [[4-Archives/Notes/Feishu/云空间/莱讯科技/项目开发管理/定位平台定制版/软件项目资料-定制版]] | [飞书](https://reliablesense.feishu.cn/docx/doxcnmwgwcdPnrEHAgd4pXZMBgc) | → 提取 | `2-Areas/Work/产品研发/软件项目资料-定制版.md` |
| 概要设计说明书-定制版.md | [[4-Archives/Notes/Feishu/云空间/莱讯科技/项目开发管理/定位平台定制版/概要设计说明书-定制版]] | [飞书](https://reliablesense.feishu.cn/docx/doxcnE47mE0e0UrshePl4lw033d) | → 提取 | `2-Areas/Work/产品研发/概要设计说明书-定制版.md` |
| 各项目子目录 | 见下方项目资料管理部分 | → 归档 | 按项目分配 |

### 5c. 定位平台中间件 / 5d. 云端版

| 文件 | 本地路径 | 飞书链接 | 决策 | 目标路径 |
|------|---------|---------|------|---------|
| 软件项目资料-中间件.md | [[4-Archives/Notes/Feishu/云空间/莱讯科技/项目开发管理/定位平台中间件/软件项目资料-中间件]] | [飞书](https://reliablesense.feishu.cn/docx/QbwZdfpAGoD01Ux19u8cuYuVnYf) | → 提取 | `2-Areas/Work/产品研发/软件项目资料-中间件.md` |
| 软件项目资料-云端版.md | [[4-Archives/Notes/Feishu/云空间/莱讯科技/项目开发管理/定位平台云端版/软件项目资料-云端版]] | [飞书](https://reliablesense.feishu.cn/docx/doxcnYnCagX1SsmAbbSyUtL0SRb) | → 提取 | `2-Areas/Work/产品研发/软件项目资料-云端版.md` |

---

## 六、莱讯科技/项目资料管理

### 6a. 进行中项目 → `1-Projects/Work/`

| 飞书目录 | 本地路径 | 飞书链接 | 目标路径 |
|---------|---------|---------|---------|
| 002. 上海上港/ | [[4-Archives/Notes/Feishu/云空间/莱讯科技/项目资料管理/002. 上海上港/README]] | [飞书（目录）](https://reliablesense.feishu.cn/drive/folder/IwSpfxmL5lfpO8dLuoccbdnLnre) | `1-Projects/Work/上港仓储管理/` |
| 004. 广州机场-综合定位/ | [[4-Archives/Notes/Feishu/云空间/莱讯科技/项目资料管理/004. 广州机场-综合定位/README]] | [飞书（目录）](https://reliablesense.feishu.cn/drive/folder/NQ2RfyZM7lO2iadqk3rcmDjPnsb) | `1-Projects/Work/广州机场/综合定位/` |
| 005. 广州机场-移动应用平台/ | [[4-Archives/Notes/Feishu/云空间/莱讯科技/项目资料管理/005. 广州机场-移动应用平台/README]] | [飞书（目录）](https://reliablesense.feishu.cn/drive/folder/D0HIfmaPgleaANd8Cw1cDwpGnhb) | `1-Projects/Work/广州机场/移动应用平台/` |
| 南宁机场项目/ | [[4-Archives/Notes/Feishu/云空间/莱讯科技/项目资料管理/南宁机场项目/README]] | [飞书（目录）](https://reliablesense.feishu.cn/drive/folder/JuNOf2llHlkIa9dKw73cJm5pn3w) | `1-Projects/Work/南宁机场/` |

> 只提取 .md 技术文档，.xlsx/.pptx/.docx/.mp4/.zip 等附件留归档。

### 6b. 已结束项目 → `4-Archives/Projects/Work/`

| 飞书目录 | 本地路径 | 飞书链接 | 目标路径 |
|---------|---------|---------|---------|
| 003. 中东电子厂客户/ | [[4-Archives/Notes/Feishu/云空间/莱讯科技/项目资料管理/003. 中东电子厂客户/README]] | [飞书（目录）](https://reliablesense.feishu.cn/drive/folder/UF9cfyxN7lnWIwd02auc28fFnOg) | `4-Archives/Projects/Work/中东电子厂/` |
| 中联核信/ | [[4-Archives/Notes/Feishu/云空间/莱讯科技/项目资料管理/中联核信/README]] | [飞书（目录）](https://reliablesense.feishu.cn/drive/folder/LaOOfNGfBlvZqOdTmgtcRQzxnJc) | `4-Archives/Projects/Work/中联核信/` |
| 红点定位/ | [[4-Archives/Notes/Feishu/云空间/莱讯科技/项目资料管理/红点定位/README]] | [飞书（目录）](https://reliablesense.feishu.cn/docx/YBASdNrzWo8e9ExCrZYcdClTnfg) | `4-Archives/Projects/Work/红点定位/` |
| 998. 售后项目/ | [[4-Archives/Notes/Feishu/云空间/莱讯科技/项目资料管理/998. 售后项目/README]] | [飞书（目录）](https://reliablesense.feishu.cn/drive/folder/R0Jef62eAlU8d8dONehcJ0CdnOb) | `4-Archives/Projects/Work/对应项目名/` |
| 999. 归档项目/ | [[4-Archives/Notes/Feishu/云空间/莱讯科技/项目资料管理/999. 归档项目/README]] | [飞书（目录）](https://reliablesense.feishu.cn/drive/folder/O2CofScN2lERyKdxnlych2jbnVe) | `4-Archives/Projects/Work/对应项目名/` |
| ~其他项目/ | [[4-Archives/Notes/Feishu/云空间/莱讯科技/项目资料管理/~其他项目/README]] | [飞书（目录）](https://reliablesense.feishu.cn/drive/folder/fldcnRPjh6QcMmwt4l61XoCDfqd) | `4-Archives/Projects/Work/对应项目名/` |

### 6c. 通用资料

| 飞书目录 | 本地路径 | 飞书链接 | 决策 | 目标路径 |
|---------|---------|---------|------|---------|
| 000. 售前项目/ | [[4-Archives/Notes/Feishu/云空间/莱讯科技/项目资料管理/000. 售前项目/README]] | [飞书（目录）](https://reliablesense.feishu.cn/drive/folder/JgzWfy33SlvnsSdrg5Uc3Fdrnm1) | → 提取 | `2-Areas/Work/业务管理/售前项目/` |
| 001. 项目资料模板/ | [[4-Archives/Notes/Feishu/云空间/莱讯科技/项目资料管理/001. 项目资料模板/README]] | [飞书（目录）](https://reliablesense.feishu.cn/drive/folder/XHMvfo59aln6mfd4sqpcHpI0neh) | → 提取 | `2-Areas/Work/业务管理/项目资料模板/` |
| 软著立项/ | [[4-Archives/Notes/Feishu/云空间/莱讯科技/项目资料管理/软著立项/README]] | [飞书（目录）](https://reliablesense.feishu.cn/drive/folder/SscHfr1iClEid6dcPsrc5cTJnNb) | → 提取 | `2-Areas/Work/综合管理/软著立项/` |
| 项目评估/ | [[4-Archives/Notes/Feishu/云空间/莱讯科技/项目资料管理/项目评估/README]] | [飞书（目录）](https://reliablesense.feishu.cn/drive/folder/WW7df5NEglBmvCdYGDQcFZNKnEe) | → 提取 | `2-Areas/Work/业务管理/项目评估/` |
| cle测算报告.md | [[4-Archives/Notes/Feishu/云空间/莱讯科技/项目资料管理/cle测算报告]] | [飞书](https://reliablesense.feishu.cn/docx/KsIRdMFKRoRWqQx8yYkce8G0nys) | → 提取 | `2-Areas/Work/设备管理/核芯物联蓝牙AOA/CLE定位引擎测算报告.md` |

---

## 七、莱讯科技/解决方案管理

23 个行业方案目录 → `3-Resources/Business/解决方案/` 下按行业分子文件夹。

| 飞书目录 | 本地路径 | 飞书链接 | 目标路径 |
|---------|---------|---------|---------|
| 医疗管理/ | [[4-Archives/Notes/Feishu/云空间/莱讯科技/解决方案管理/医疗管理/README]] | [飞书（目录）](https://reliablesense.feishu.cn/drive/folder/fldcnfW1XoDZq61aCjTTTMxn5Wb) | `3-Resources/Business/解决方案/医疗管理/` |
| 工厂智能管理/ | [[4-Archives/Notes/Feishu/云空间/莱讯科技/解决方案管理/工厂智能管理/README]] | [飞书（目录）](https://reliablesense.feishu.cn/drive/folder/fldcnmwgAf8rXNPORyY841V9toc) | `3-Resources/Business/解决方案/工厂智能管理/` |
| 人员定位系统/ | [[4-Archives/Notes/Feishu/云空间/莱讯科技/解决方案管理/人员定位系统/README]] | [飞书（目录）](https://reliablesense.feishu.cn/drive/folder/fldcngsLYcS76KLSqgmlf27UgFS) | `3-Resources/Business/解决方案/人员定位系统/` |
| 轨道交通/ | [[4-Archives/Notes/Feishu/云空间/莱讯科技/解决方案管理/轨道交通/README]] | [飞书（目录）](https://reliablesense.feishu.cn/drive/folder/fldcnUSkIs7zEpcYhqZJdqB2mHf) | `3-Resources/Business/解决方案/轨道交通/` |
| 监狱方案/ | [[4-Archives/Notes/Feishu/云空间/莱讯科技/解决方案管理/监狱方案/README]] | [飞书（目录）](https://reliablesense.feishu.cn/drive/folder/fldcnqnbQVewfyPUywW1Kgt5p9c) | `3-Resources/Business/解决方案/监狱方案/` |
| APP/ | [[4-Archives/Notes/Feishu/云空间/莱讯科技/解决方案管理/APP/README]] | [飞书（目录）](https://reliablesense.feishu.cn/drive/folder/fldcnHqr92U5T4e6dsspCibhlzb) | `3-Resources/Business/解决方案/APP/` |
| 仓储物流/ | [[4-Archives/Notes/Feishu/云空间/莱讯科技/解决方案管理/仓储物流/README]] | [飞书（目录）](https://reliablesense.feishu.cn/drive/folder/fldcnM1DioUybyK5yF0IpqIA4ue) | `3-Resources/Business/解决方案/仓储物流/` |
| 智慧工地/ | [[4-Archives/Notes/Feishu/云空间/莱讯科技/解决方案管理/智慧工地/README]] | [飞书（目录）](https://reliablesense.feishu.cn/drive/folder/fldcnB8vpGsKhbFw39wboL1KXWU) | `3-Resources/Business/解决方案/智慧工地/` |
| 展厅方案/ | [[4-Archives/Notes/Feishu/云空间/莱讯科技/解决方案管理/展厅方案/README]] | [飞书（目录）](https://reliablesense.feishu.cn/drive/folder/fldcn42c718VJ97rzaAOOj5dtYg) | `3-Resources/Business/解决方案/展厅方案/` |
| 智慧停车/ | [[4-Archives/Notes/Feishu/云空间/莱讯科技/解决方案管理/智慧停车/README]] | [飞书（目录）](https://reliablesense.feishu.cn/drive/folder/fldcnhKivCzfZBCASbfCixfBY3y) | `3-Resources/Business/解决方案/智慧停车/` |
| 三维GIS方案/ | [[4-Archives/Notes/Feishu/云空间/莱讯科技/解决方案管理/三维GIS方案/README]] | [飞书（目录）](https://reliablesense.feishu.cn/drive/folder/fldcnMIvLyjg0lkFSukBFjmbjgk) | `3-Resources/Business/解决方案/三维GIS方案/` |
| 资产管理/ | [[4-Archives/Notes/Feishu/云空间/莱讯科技/解决方案管理/资产管理/README]] | [飞书（目录）](https://reliablesense.feishu.cn/drive/folder/fldcn6bvIwE07Vfdf22NWhTkkQg) | `3-Resources/Business/解决方案/资产管理/` |
| 室外定位GPS/ | [[4-Archives/Notes/Feishu/云空间/莱讯科技/解决方案管理/室外定位GPS/README]] | [飞书（目录）](https://reliablesense.feishu.cn/drive/folder/fldcnMPEUkEWzU1WooHG66ciTub) | `3-Resources/Business/解决方案/室外定位GPS/` |
| 工业环境解决方案/ | [[4-Archives/Notes/Feishu/云空间/莱讯科技/解决方案管理/工业环境解决方案/README]] | [飞书（目录）](https://reliablesense.feishu.cn/drive/folder/fldcnTZK4gCDRdNYGH5TdeRIWxc) | `3-Resources/Business/解决方案/工业环境/` |
| 枪支定位/ | [[4-Archives/Notes/Feishu/云空间/莱讯科技/解决方案管理/枪支定位/README]] | [飞书（目录）](https://reliablesense.feishu.cn/drive/folder/fldcnF3ytnSvoNWjQMVZ4MiNbef) | `3-Resources/Business/解决方案/枪支定位/` |
| 室外定位导航/ | [[4-Archives/Notes/Feishu/云空间/莱讯科技/解决方案管理/室外定位导航/README]] | [飞书（目录）](https://reliablesense.feishu.cn/drive/folder/fldcnuemzAKmIchByv3yfj8FdEe) | `3-Resources/Business/解决方案/室外定位导航/` |
| 智能制造/ | [[4-Archives/Notes/Feishu/云空间/莱讯科技/解决方案管理/智能制造/README]] | [飞书（目录）](https://reliablesense.feishu.cn/drive/folder/fldcnoJlmqWb2Uz3stu8tI9nF4e) | `3-Resources/Business/解决方案/智能制造/` |
| 执法办案中心/ | [[4-Archives/Notes/Feishu/云空间/莱讯科技/解决方案管理/执法办案中心/README]] | [飞书（目录）](https://reliablesense.feishu.cn/drive/folder/fldcn0UMbtD5COUoqsR95FSiFfe) | `3-Resources/Business/解决方案/执法办案中心/` |
| 交通运输方案/ | [[4-Archives/Notes/Feishu/云空间/莱讯科技/解决方案管理/交通运输方案/README]] | [飞书（目录）](https://reliablesense.feishu.cn/drive/folder/fldcn4PnILhcncA0Mz0dRjnc3Gb) | `3-Resources/Business/解决方案/交通运输/` |
| 室外手环定位/ | [[4-Archives/Notes/Feishu/云空间/莱讯科技/解决方案管理/室外手环定位/README]] | [飞书（目录）](https://reliablesense.feishu.cn/drive/folder/fldcnk6tVeNUBM5yoHc0FdyB9cg) | `3-Resources/Business/解决方案/室外手环定位/` |
| 煤矿智能管理/ | [[4-Archives/Notes/Feishu/云空间/莱讯科技/解决方案管理/煤矿智能管理/README]] | [飞书（目录）](https://reliablesense.feishu.cn/drive/folder/fldcn2IcEtN0DkDCnVxp5p79IpD) | `3-Resources/Business/解决方案/煤矿智能管理/` |
| 方案制作需求清单/ | [[4-Archives/Notes/Feishu/云空间/莱讯科技/解决方案管理/方案制作需求清单/README]] | [飞书（目录）](https://reliablesense.feishu.cn/drive/folder/WEWafQtpSl0OXxdvDLxc5il1nHb) | `3-Resources/Business/解决方案/` |
| ~其他公司方案/ | [[4-Archives/Notes/Feishu/云空间/莱讯科技/解决方案管理/~其他公司方案/README]] | [飞书（目录）](https://reliablesense.feishu.cn/drive/folder/fldcntIjp8709PCclFH082V5Dtw) | 留归档 |

---

## 八、莱讯科技/其他子目录

| 飞书目录 | 本地路径 | 飞书链接 | 决策 | 目标路径 |
|---------|---------|---------|------|---------|
| 销售管理/ | [[4-Archives/Notes/Feishu/云空间/莱讯科技/销售管理/README]] | [飞书（目录）](https://reliablesense.feishu.cn/drive/folder/fldcnuQTpZq9z3fQqoC2lpddUuf) | → 提取 | `2-Areas/Work/业务管理/销售管理/` |
| 供应商管理/ | [[4-Archives/Notes/Feishu/云空间/莱讯科技/供应商管理/README]] | [飞书（目录）](https://reliablesense.feishu.cn/drive/folder/fldcnNwx1J0P7hbltFXzvM7zaZg) | → 提取 | `2-Areas/Work/设备管理/供应商管理/` |
| 品牌手册与logo/ | [[4-Archives/Notes/Feishu/云空间/莱讯科技/品牌手册与logo/README]] | [飞书（目录）](https://reliablesense.feishu.cn/drive/folder/fldcnxWldL28uIpPVgqGKq1iacc) | → 提取 | `2-Areas/Work/品牌宣传/品牌手册/` |
| 招聘管理/ | [[4-Archives/Notes/Feishu/云空间/莱讯科技/招聘管理/README]] | [飞书（目录）](https://reliablesense.feishu.cn/drive/folder/fldcnBIre17Jup3HGpXsoiCd8se) | → 提取 | `2-Areas/Work/团队管理/招聘/` |
| 网站维护/ | [[4-Archives/Notes/Feishu/云空间/莱讯科技/网站维护/README]] | [飞书（目录）](https://reliablesense.feishu.cn/drive/folder/UYyyf4hUllGZhWdgXMLci950nge) | → 提取 | `2-Areas/Work/品牌宣传/网站维护/` |
| 宣传/ | [[4-Archives/Notes/Feishu/云空间/莱讯科技/宣传/README]] | [飞书（目录）](https://reliablesense.feishu.cn/drive/folder/ZOFWfSgpdllGNedVktUcgOupnze) | → 提取 | `2-Areas/Work/品牌宣传/宣传/` |
| 公司宣传物（公司介绍）/ | [[4-Archives/Notes/Feishu/云空间/莱讯科技/公司宣传物（公司介绍）/README]] | [飞书（目录）](https://reliablesense.feishu.cn/drive/folder/Ges8feJEylJjjydGKgNc6NIWnLd) | → 提取 | `2-Areas/Work/品牌宣传/公司介绍/` |
| 往期展会资料合集/ | [[4-Archives/Notes/Feishu/云空间/莱讯科技/往期展会资料合集/README]] | [飞书（目录）](https://reliablesense.feishu.cn/drive/folder/fldcnLJHIahqTfcscC7zPIMN6cQ) | → 提取 | `2-Areas/Work/品牌宣传/展会/` |
| 公司英文资料/ | [[4-Archives/Notes/Feishu/云空间/莱讯科技/公司英文资料/README]] | [飞书（目录）](https://reliablesense.feishu.cn/drive/folder/ICuefj7fVl2yr7dFDNycWa4An2g) | → 提取 | `2-Areas/Work/品牌宣传/英文资料/` |
| 路网维护/ | [[4-Archives/Notes/Feishu/云空间/莱讯科技/路网维护/README]] | [飞书（目录）](https://reliablesense.feishu.cn/drive/folder/fldcnLHpkn823HAgGZwpcki8omf) | 留归档 | - | .osm 路网文件，Obsidian 无法打开 |
| ~参考资料/ | [[4-Archives/Notes/Feishu/云空间/莱讯科技/~参考资料/README]] | [飞书（目录）](https://reliablesense.feishu.cn/drive/folder/fldcnpp8JeCmpzMuPLsbsIczAif) | 留归档 | - | 竞品方案、宣传素材截图，全是附件 |
| 共享文件/ | [[4-Archives/Notes/Feishu/云空间/莱讯科技/共享文件/README]] | [飞书（目录）](https://reliablesense.feishu.cn/drive/folder/KAzWfCcrMlNrOQdRqPhchfz2n2c) | 留归档 | - | 临时网盘 |

### 公司内部资料重点文件

| 文件 | 本地路径 | 飞书链接 | 决策 | 目标路径 |
|------|---------|---------|------|---------|
| 员工管理制度.md | [[4-Archives/Notes/Feishu/云空间/莱讯科技/公司内部资料/员工管理制度]] | [飞书](https://reliablesense.feishu.cn/docx/doxcng2WuNQoFwYt9IDn3iqXqUb) | → 提取 | `2-Areas/Work/团队管理/员工管理制度.md` |
| 工作周报管理及考核制度.md | [[4-Archives/Notes/Feishu/云空间/莱讯科技/公司内部资料/工作周报管理及考核制度]] | [飞书](https://reliablesense.feishu.cn/docx/MfMRdLUQRovRsExNxjGcTZ8Jnxd) | → 提取 | `2-Areas/Work/团队管理/工作周报管理及考核制度.md` |
| 考勤制度.md | [[4-Archives/Notes/Feishu/云空间/莱讯科技/公司内部资料/考勤制度]] | [飞书](https://reliablesense.feishu.cn/docx/ICeIdwPzXo2hSDxtqFqc4757nXd) | → 提取 | `2-Areas/Work/团队管理/考勤制度.md` |
| 组织架构图.md | [[4-Archives/Notes/Feishu/云空间/莱讯科技/公司内部资料/组织架构图]] | [飞书](https://reliablesense.feishu.cn/docs/doccnyI23DHQUFVPNJX7wFsoF0f) | → 提取 | `2-Areas/Work/团队管理/组织架构图.md` |
| 地图制作设计书.md | [[4-Archives/Notes/Feishu/云空间/莱讯科技/公司内部资料/地图制作设计书]] | [飞书](https://reliablesense.feishu.cn/docx/doxcn7nMEKVIzB4JtbnSLhsJUXc) | → 提取 | `2-Areas/Work/产品研发/地图制作设计书.md` |
| PPT模版/ | [[4-Archives/Notes/Feishu/云空间/莱讯科技/公司内部资料/PPT模版/README]] | [飞书（目录）](https://reliablesense.feishu.cn/drive/folder/fldcnU27rGaNhScFA2EumhiPNDd) | → 提取 | `2-Areas/Work/品牌宣传/PPT模版/` |
| ISO9001质量体系认证/ | [[4-Archives/Notes/Feishu/云空间/莱讯科技/公司内部资料/ISO9001质量体系认证/README]] | [飞书（目录）](https://reliablesense.feishu.cn/drive/folder/fldcn3A1mrYbgL8yKwwsVrlsAtb) | → 提取 | `2-Areas/Work/综合管理/ISO9001/` |
| 软著的立项资料/ | [[4-Archives/Notes/Feishu/云空间/莱讯科技/公司内部资料/软著的立项资料/README]] | [飞书（目录）](https://reliablesense.feishu.cn/drive/folder/SscHfr1iClEid6dcPsrc5cTJnNb) | → 提取 | `2-Areas/Work/综合管理/软著立项/` |
| 小程序管理文档.md | [[4-Archives/Notes/Feishu/云空间/莱讯科技/小程序管理文档]] | [飞书](https://reliablesense.feishu.cn/docx/JgCpdERLho9N3zxiGpqcQ7GAnov) | → 提取 | `2-Areas/Work/产品研发/小程序账号管理.md` |
| 参考/ | [[4-Archives/Notes/Feishu/云空间/莱讯科技/公司内部资料/参考/README]] | - | 留归档 | - | 行业白皮书（5G定位、AIoT）、敏捷管理文章、竞品方案，全是 .pdf/.docx 附件 |

---

## 九、知识库

### 9a. 技术分享

| 文件 | 本地路径 | 飞书链接 | 决策 | 目标路径 |
|------|---------|---------|------|---------|
| 前端React开发规范.md | [[4-Archives/Notes/Feishu/知识库/技术分享/前端相关文档/前端React开发规范]] | [飞书](https://reliablesense.feishu.cn/doc/doccnymhDUxjzJsBjuZ5mBGpG4c) | ⚠️ 待确认 | 见 [[1-Projects/Personal/笔记迁移/阶段二-待确认分类]] |
| 后端开发流程规范.md | [[4-Archives/Notes/Feishu/知识库/技术分享/后端相关文档/后端开发流程规范]] | [飞书](https://reliablesense.feishu.cn/docx/CUA7dlJrRoTZ3Fx8t5kc1UiRneb) | → 提取 | `2-Areas/Work/产品研发/后端开发流程规范.md` |
| 定位平台系统整体改造方案.md | [[4-Archives/Notes/Feishu/知识库/技术分享/后端相关文档/定位平台系统整体改造方案]] | [飞书](https://reliablesense.feishu.cn/doc/doccnVRMcLTfhON3R9OLZT7VHgf) | → 提取 | `2-Areas/Work/产品研发/定位平台系统整体改造方案.md` |
| 微服务说明.md | [[4-Archives/Notes/Feishu/知识库/技术分享/后端相关文档/微服务说明]] | [飞书](https://reliablesense.feishu.cn/docx/F2PhdYeMCoHjP6xd8y0cyz6Mnac) | ⚠️ 待确认 | 见 [[1-Projects/Personal/笔记迁移/阶段二-待确认分类]] |
| 后端问题QA.md | [[4-Archives/Notes/Feishu/知识库/技术分享/后端问题QA]] | [飞书](https://reliablesense.feishu.cn/docx/OpsxdI417oi5i4xLyrhc8Znyn5f) | ⚠️ 待确认 | 见 [[1-Projects/Personal/笔记迁移/阶段二-待确认分类]] |
| QGIS地图绘制准备.md | [[4-Archives/Notes/Feishu/知识库/技术分享/地图相关文档/QGIS地图绘制准备]] | [飞书](https://reliablesense.feishu.cn/docx/CXjHdQO7JogckXxR6owcL5AcnEb) | → 提取 | `3-Resources/Tech/知识卡片/QGIS地图绘制准备.md` |
| QGIS安装.md | [[4-Archives/Notes/Feishu/知识库/技术分享/地图相关文档/QGIS安装]] | [飞书](https://reliablesense.feishu.cn/docx/DKP6dIPIHoXYuMxJ5Xoc00LVngp) | → 提取 | `3-Resources/Tech/知识卡片/QGIS安装.md` |
| QGIS图片及瓦片图添加.md | [[4-Archives/Notes/Feishu/知识库/技术分享/地图相关文档/QGIS图片及瓦片图添加]] | [飞书](https://reliablesense.feishu.cn/docx/X68Zdyv98o4AgGx073LcsrscnAh) | → 提取 | `3-Resources/Tech/知识卡片/QGIS图片及瓦片图添加.md` |
| QGIS地图绘制注意事项CAD版.md | [[4-Archives/Notes/Feishu/知识库/技术分享/地图相关文档/QGIS地图绘制注意事项CAD版]] | [飞书](https://reliablesense.feishu.cn/doc/doccnKYx4RPxYSXzTH0ssUvvBmf) | → 提取 | `3-Resources/Tech/知识卡片/QGIS地图绘制注意事项CAD版.md` |
| png图片导入地图.md | [[4-Archives/Notes/Feishu/知识库/技术分享/地图相关文档/png图片导入地图]] | [飞书](https://reliablesense.feishu.cn/doc/doccn3DidLn9ur0mvFbqsnXhstd) | → 提取 | `3-Resources/Tech/知识卡片/png图片导入地图.md` |
| 瓦片图制作.md | [[4-Archives/Notes/Feishu/知识库/技术分享/地图相关文档/瓦片图制作]] | [飞书](https://reliablesense.feishu.cn/docx/OvGsdeF3UoAgULxqd9Kc08punEg) | ⚠️ 待确认 | 见 [[1-Projects/Personal/笔记迁移/阶段二-待确认分类]] |
| 路网绘制.md | [[4-Archives/Notes/Feishu/知识库/技术分享/地图相关文档/路网绘制]] | [飞书](https://reliablesense.feishu.cn/docx/doxcnmMiCtaR2HkpnlPPrChqyEb) | ⚠️ 待确认 | 见 [[1-Projects/Personal/笔记迁移/阶段二-待确认分类]] |
| 地图按钮、视角、控件控制.md | [[4-Archives/Notes/Feishu/知识库/技术分享/地图相关文档/地图按钮、视角、控件控制]] | [飞书](https://reliablesense.feishu.cn/docx/HUTId5xjFoaRIxxUkQWcEb1Xnge) | ⚠️ 待确认 | 见 [[1-Projects/Personal/笔记迁移/阶段二-待确认分类]] |
| 项目建立步骤.md | [[4-Archives/Notes/Feishu/知识库/技术分享/地图相关文档/项目建立步骤]] | [飞书](https://reliablesense.feishu.cn/docx/LapVd88f0oFaKUx4QwRcwrW1neI) | ⚠️ 待确认 | 见 [[1-Projects/Personal/笔记迁移/阶段二-待确认分类]] |
| 麦钉点云图地图绘制注意事项.md | [[4-Archives/Notes/Feishu/知识库/技术分享/地图相关文档/麦钉点云图地图绘制注意事项]] | [飞书](https://reliablesense.feishu.cn/doc/doccn6HL7llLqfP4e5qCI96CdUf) | → 提取 | `1-Projects/Work/麦钉项目/麦钉点云图地图绘制注意事项.md` | 麦钉项目专用 |
| CICD流程介绍.md | [[4-Archives/Notes/Feishu/知识库/技术分享/基础平台相关文档/CICD流程介绍]] | [飞书](https://reliablesense.feishu.cn/doc/doccnqi4YxvSVSY23MSLXIkwIKe) | ⚠️ 待确认 | 见 [[1-Projects/Personal/笔记迁移/阶段二-待确认分类]] |
| Gitlab-CICD说明.md | [[4-Archives/Notes/Feishu/知识库/技术分享/基础平台相关文档/Gitlab-CICD说明]] | [飞书](https://reliablesense.feishu.cn/doc/doccnUileviuvksypU7AAbSEGwg) | ⚠️ 待确认 | 见 [[1-Projects/Personal/笔记迁移/阶段二-待确认分类]] |
| 前后端CICD.md | [[4-Archives/Notes/Feishu/知识库/技术分享/基础平台相关文档/前后端CICD]] | [飞书](https://reliablesense.feishu.cn/doc/doccncqa7DwRv2fD3Z3KA6oO4oh) | ⚠️ 待确认 | 见 [[1-Projects/Personal/笔记迁移/阶段二-待确认分类]] |
| 开发分支管理规范.md | [[4-Archives/Notes/Feishu/知识库/技术分享/基础平台相关文档/开发分支管理规范]] | [飞书](https://reliablesense.feishu.cn/doc/doccnlE0yWc24L79rE98oSVsY8d) | ⚠️ 待确认 | 见 [[1-Projects/Personal/笔记迁移/阶段二-待确认分类]] |
| 办公网v2ray操作手册.md | [[4-Archives/Notes/Feishu/知识库/技术分享/基础平台相关文档/办公网VPN/办公网v2ray操作手册]] | [飞书](https://reliablesense.feishu.cn/docx/G1OBdhlTSotGV6xRToRcXlzWnoe) | ⚠️ 待确认 | 见 [[1-Projects/Personal/笔记迁移/阶段二-待确认分类]] |
| 办公网WireGuard操作手册.md | [[4-Archives/Notes/Feishu/知识库/技术分享/基础平台相关文档/办公网VPN/办公网WireGuard操作手册]] | [飞书](https://reliablesense.feishu.cn/docx/Q4OzdL6ZboG5dSxgqqlcNn4WnFf) | ⚠️ 待确认 | 见 [[1-Projects/Personal/笔记迁移/阶段二-待确认分类]] |
| A-Server-environment-preparation.md | [[4-Archives/Notes/Feishu/知识库/技术分享/基础平台相关文档/Deployment英文版/A-Server-environment-preparation]] | [飞书](https://reliablesense.feishu.cn/docx/CWnsdq3ryoYTSHxGAC0cpcoenbg) | ⚠️ 待确认 | 见 [[1-Projects/Personal/笔记迁移/阶段二-待确认分类]] |
| B1-Cluster-setup-K3s-online.md | [[4-Archives/Notes/Feishu/知识库/技术分享/基础平台相关文档/Deployment英文版/B1-Cluster-setup-K3s-online]] | [飞书](https://reliablesense.feishu.cn/docx/Kgifd4mPJo5nuVxkmX2cF76unde) | ⚠️ 待确认 | 见 [[1-Projects/Personal/笔记迁移/阶段二-待确认分类]] |
| B2-Cluster-setup-K3s-offline.md | [[4-Archives/Notes/Feishu/知识库/技术分享/基础平台相关文档/Deployment英文版/B2-Cluster-setup-K3s-offline]] | [飞书](https://reliablesense.feishu.cn/docx/NQgadYYYJo5e4sxLhxMcLMZ9nGB) | ⚠️ 待确认 | 见 [[1-Projects/Personal/笔记迁移/阶段二-待确认分类]] |
| C-Installation-of-basic-services.md | [[4-Archives/Notes/Feishu/知识库/技术分享/基础平台相关文档/Deployment英文版/C-Installation-of-basic-services]] | [飞书](https://reliablesense.feishu.cn/docx/MXFDdnQvAoKSMAxxdAXc2I9bnYb) | ⚠️ 待确认 | 见 [[1-Projects/Personal/笔记迁移/阶段二-待确认分类]] |
| A-服务器环境准备.md | [[4-Archives/Notes/Feishu/知识库/技术分享/基础平台相关文档/私有化部署/A-服务器环境准备]] | [飞书](https://reliablesense.feishu.cn/docx/doxcniK4NdHGlK7G8gccJ5WYnEg) | ⚠️ 待确认 | 见 [[1-Projects/Personal/笔记迁移/阶段二-待确认分类]] |
| B1-集群搭建K3s在线版.md | [[4-Archives/Notes/Feishu/知识库/技术分享/基础平台相关文档/私有化部署/B1-集群搭建K3s在线版]] | [飞书](https://reliablesense.feishu.cn/docx/doxcn67UW5vdFM5qaPG3tc9zMdd) | ⚠️ 待确认 | 见 [[1-Projects/Personal/笔记迁移/阶段二-待确认分类]] |
| B2-集群搭建K3s离线版.md | [[4-Archives/Notes/Feishu/知识库/技术分享/基础平台相关文档/私有化部署/B2-集群搭建K3s离线版]] | [飞书](https://reliablesense.feishu.cn/docx/SuiNdHlegogxpcxnqqhc8AuKnZ1) | ⚠️ 待确认 | 见 [[1-Projects/Personal/笔记迁移/阶段二-待确认分类]] |
| C-集群内基础服务安装.md | [[4-Archives/Notes/Feishu/知识库/技术分享/基础平台相关文档/私有化部署/C-集群内基础服务安装]] | [飞书](https://reliablesense.feishu.cn/docx/doxcnSbULW58Lp1lXBy2tt8i80e) | ⚠️ 待确认 | 见 [[1-Projects/Personal/笔记迁移/阶段二-待确认分类]] |
| 命令行工具oemctl.md | [[4-Archives/Notes/Feishu/知识库/技术分享/基础平台相关文档/私有化部署/命令行工具oemctl]] | [飞书](https://reliablesense.feishu.cn/docx/J1C8daWxto4clexYnaDcKtgQnzf) | ⚠️ 待确认 | 见 [[1-Projects/Personal/笔记迁移/阶段二-待确认分类]] |
| 偏移位置数据到火星坐标.md | [[4-Archives/Notes/Feishu/知识库/技术分享/数据库相关文档/Postgis/偏移位置数据到火星坐标]] | [飞书](https://reliablesense.feishu.cn/doc/doccn4JOodvetnzvaKMfs3aIBSh) | → 提取 | `3-Resources/Tech/代码片段/` |
| 火星坐标转换.md | [[4-Archives/Notes/Feishu/知识库/技术分享/数据库相关文档/Postgis/火星坐标转换]] | [飞书](https://reliablesense.feishu.cn/doc/doccnbSee08xdsJhTWt1nXJccZc) | → 提取 | `3-Resources/Tech/代码片段/` |
| 获取指定范围内的点.md | [[4-Archives/Notes/Feishu/知识库/技术分享/数据库相关文档/Postgis/获取指定范围内的点]] | [飞书](https://reliablesense.feishu.cn/doc/doccnhqA2pLGKjd5fnqdDsdRbig) | → 提取 | `3-Resources/Tech/代码片段/` |
| 更新地图中点和边界.md | [[4-Archives/Notes/Feishu/知识库/技术分享/数据库相关文档/Postgis/更新地图中点和边界]] | [飞书](https://reliablesense.feishu.cn/doc/doccnI6f4RL5XRKR8R2k2oA6Ykf) | → 提取 | `3-Resources/Tech/代码片段/` |
| 移动缩放旋转地图.md | [[4-Archives/Notes/Feishu/知识库/技术分享/数据库相关文档/Postgis/移动缩放旋转地图]] | [飞书](https://reliablesense.feishu.cn/doc/doccnN1mQdwwDwXCsBhuSsVzTId) | → 提取 | `3-Resources/Tech/代码片段/` |
| 移动电子围栏到火星坐标.md | [[4-Archives/Notes/Feishu/知识库/技术分享/数据库相关文档/Postgis/移动电子围栏到火星坐标]] | [飞书](https://reliablesense.feishu.cn/doc/doccnvu9gfk9NPRnE1FMF7fpNFe) | → 提取 | `3-Resources/Tech/代码片段/` |
| 修改火星坐标完整语句.md | [[4-Archives/Notes/Feishu/知识库/技术分享/数据库相关文档/Postgis/修改火星坐标完整语句]] | [飞书](https://reliablesense.feishu.cn/doc/doccnZUAaAKBqN3uCPCiAHkWo30) | → 提取 | `3-Resources/Tech/代码片段/` |
| 将Point转成PointZ.md | [[4-Archives/Notes/Feishu/知识库/技术分享/数据库相关文档/Postgis/将Point转成PointZ]] | [飞书](https://reliablesense.feishu.cn/doc/doccnZTs4pwAZPya8zQfIgRf7Yf) | → 提取 | `3-Resources/Tech/代码片段/` |
| 处理连接数的问题.md | [[4-Archives/Notes/Feishu/知识库/技术分享/数据库相关文档/Postgres/处理连接数的问题]] | [飞书](https://reliablesense.feishu.cn/doc/doccnZIMQSFgw5z9FAtvRxqEF4f) | → 提取 | `3-Resources/Tech/代码片段/` |
| 处理t_position的id问题.md | [[4-Archives/Notes/Feishu/知识库/技术分享/数据库相关文档/Postgres/处理t_position的id问题]] | [飞书](https://reliablesense.feishu.cn/doc/doccnDPxocYNEJe0c7YYnRI6R3e) | → 提取 | `3-Resources/Tech/代码片段/` |
| 生成trigger_set_timestamp.md | [[4-Archives/Notes/Feishu/知识库/技术分享/数据库相关文档/Postgres/生成trigger_set_timestamp]] | [飞书](https://reliablesense.feishu.cn/doc/doccnszyZqVAlZhQ6yFE8iVp3uf) | → 提取 | `3-Resources/Tech/代码片段/` |
| 生成UUID.md | [[4-Archives/Notes/Feishu/知识库/技术分享/数据库相关文档/Postgres/生成UUID]] | [飞书](https://reliablesense.feishu.cn/doc/doccnKzX7vdTlRNlsKlQY9oo9vd) | → 提取 | `3-Resources/Tech/代码片段/` |
| 人员物体每日在线时间统计.md | [[4-Archives/Notes/Feishu/知识库/技术分享/数据库相关文档/TimescaleDB/人员物体每日在线时间统计]] | [飞书](https://reliablesense.feishu.cn/doc/doccnSG2Jc0Fls0feLdgve23DOe) | → 提取 | `3-Resources/Tech/代码片段/` |
| 新建hyper_table时Trigger错误.md | [[4-Archives/Notes/Feishu/知识库/技术分享/数据库相关文档/TimescaleDB/新建hyper_table时Trigger错误]] | [飞书](https://reliablesense.feishu.cn/doc/doccnoNAhwDhgg2FpnJ5jOODzZb) | → 提取 | `3-Resources/Tech/代码片段/` |
| Retention-policy定期删除机制.md | [[4-Archives/Notes/Feishu/知识库/技术分享/数据库相关文档/TimescaleDB/Retention-policy定期删除机制]] | [飞书](https://reliablesense.feishu.cn/doc/doccn2mQON8tP7m08bYrNmq5BYc) | → 提取 | `3-Resources/Tech/代码片段/` |
| 插入一条t_position数据.md | [[4-Archives/Notes/Feishu/知识库/技术分享/数据库相关文档/TimescaleDB/插入一条t_position数据]] | [飞书](https://reliablesense.feishu.cn/doc/doccnmbpSo3CRnCMyTYEVFTpbIi) | → 提取 | `3-Resources/Tech/代码片段/` |
| locust报告参数说明.md | [[4-Archives/Notes/Feishu/知识库/技术分享/测试相关文档/locust报告参数说明]] | [飞书](https://reliablesense.feishu.cn/docx/doxcnyVpKX1V11tJYH2sKdff3Ph) | → 提取 | `3-Resources/Tech/知识卡片/locust报告参数说明.md` |
| 测试平台对比.md | [[4-Archives/Notes/Feishu/知识库/技术分享/测试相关文档/测试平台对比]] | [飞书](https://reliablesense.feishu.cn/doc/doccnoMeCyK1lHtPzzIxxZTmB8U) | → 提取 | `3-Resources/Tech/知识卡片/测试平台对比.md` |
| 测试流程1.md | [[4-Archives/Notes/Feishu/知识库/技术分享/测试相关文档/测试流程1]] | [飞书](https://reliablesense.feishu.cn/doc/doccnvKjRt0RgI04vi1UFEuAW4f) | ⚠️ 待确认 | 见 [[1-Projects/Personal/笔记迁移/阶段二-待确认分类]] |
| 测试的流程及内容.md | [[4-Archives/Notes/Feishu/知识库/技术分享/测试相关文档/测试的流程及内容]] | [飞书](https://reliablesense.feishu.cn/doc/doccnUSmCPXtSpHsITXo3gMqtqd) | ⚠️ 待确认 | 见 [[1-Projects/Personal/笔记迁移/阶段二-待确认分类]] |
| 测试计划初稿.md | [[4-Archives/Notes/Feishu/知识库/技术分享/测试相关文档/测试计划初稿]] | [飞书](https://reliablesense.feishu.cn/doc/doccnXKbFqjR5Up9dVYrzjvUUmh) | ⚠️ 待确认 | 见 [[1-Projects/Personal/笔记迁移/阶段二-待确认分类]] |
| 禅道测试相关操作手册.md | [[4-Archives/Notes/Feishu/知识库/技术分享/测试相关文档/禅道测试相关操作手册]] | [飞书](https://reliablesense.feishu.cn/doc/doccnTqc7EnZxfZYH0T20rXWLVe) | ⚠️ 待确认 | 见 [[1-Projects/Personal/笔记迁移/阶段二-待确认分类]] |
| 稳定性测试.md | [[4-Archives/Notes/Feishu/知识库/技术分享/测试相关文档/稳定性测试]] | [飞书](https://reliablesense.feishu.cn/docx/doxcnPMwcMjDrt0cdQBUlY9Jldf) | ⚠️ 待确认 | 见 [[1-Projects/Personal/笔记迁移/阶段二-待确认分类]] |
| MOKO-RSSI定位基站与树莓派组网.md | [[4-Archives/Notes/Feishu/知识库/技术分享/硬件相关文档/MOKO-RSSI定位基站与树莓派组网]] | [飞书](https://reliablesense.feishu.cn/docx/TDS8dDE7ToGtUWxMvu7c8bROnwf) | ⚠️ 待确认 | 见 [[1-Projects/Personal/笔记迁移/阶段二-待确认分类]] |
| RTK设备局域网WiFi使用文档.md | [[4-Archives/Notes/Feishu/知识库/技术分享/硬件相关文档/RTK设备局域网WiFi使用文档]] | [飞书](https://reliablesense.feishu.cn/docx/Yr5vdDP3YonYuWxkhZ3cfDGDnGd) | ⚠️ 待确认 | 见 [[1-Projects/Personal/笔记迁移/阶段二-待确认分类]] |
| 树莓派SSD版本安装.md | [[4-Archives/Notes/Feishu/知识库/技术分享/硬件相关文档/树莓派SSD版本安装]] | [飞书](https://reliablesense.feishu.cn/docx/YUSVdEwLVooPMHx3luMcAXh6nlh) | → 提取 | `3-Resources/Tech/知识卡片/树莓派SSD版本安装.md` |
| 烧写设备.md | [[4-Archives/Notes/Feishu/知识库/技术分享/硬件相关文档/烧写设备]] | [飞书](https://reliablesense.feishu.cn/docx/NigodFqlcowXQVxYWh5cVyoDn2g) | ⚠️ 待确认 | 见 [[1-Projects/Personal/笔记迁移/阶段二-待确认分类]] |
| 日常运维相关文档.md | [[4-Archives/Notes/Feishu/知识库/技术分享/日常运维相关文档]] | [飞书](https://reliablesense.feishu.cn/doc/doccnlJ8hk4ih92ZXrCFLFc9Zid) | → 提取 | `2-Areas/Work/运维管理/日常运维相关文档.md` |

### 9b. 项目管理

| 文件 | 本地路径 | 飞书链接 | 决策 | 目标路径 |
|------|---------|---------|------|---------|
| 团队会议.md | [[4-Archives/Notes/Feishu/知识库/项目管理/团队会议]] | [飞书](https://reliablesense.feishu.cn/wiki/P7brwY9LkiEslFkgolZcKnubn6c) | → 提取 | `2-Areas/Work/团队管理/团队会议模板.md` |
| 团队周会.md | [[4-Archives/Notes/Feishu/知识库/项目管理/团队周会]] | [飞书](https://reliablesense.feishu.cn/wiki/BFEMwNek2izj1wkluMYcC9WynJh) | → 提取 | `2-Areas/Work/团队管理/团队周会模板.md` |
| 文档模版.md | [[4-Archives/Notes/Feishu/知识库/项目管理/文档模版]] | [飞书](https://reliablesense.feishu.cn/wiki/Qb9kwDROEiR50MknBEJcI2K1nQc) | → 提取 | `2-Areas/Work/业务管理/文档模版.md` |
| 每日进展同步.md | [[4-Archives/Notes/Feishu/知识库/项目管理/每日进展同步]] | [飞书](https://reliablesense.feishu.cn/wiki/MzPPw96cFiZzQnkQg9ccE1i6n0f) | → 提取 | `2-Areas/Work/团队管理/每日进展同步模板.md` |
| 项目启动.md | [[4-Archives/Notes/Feishu/知识库/项目管理/项目启动]] | [飞书](https://reliablesense.feishu.cn/wiki/XXBIwuZzmiCxfqkwDOVcO6DqnEc) | → 提取 | `2-Areas/Work/业务管理/项目启动模板.md` |
| 项目复盘.md | [[4-Archives/Notes/Feishu/知识库/项目管理/项目复盘]] | [飞书](https://reliablesense.feishu.cn/wiki/O3eLw6EjDiNBmpk4zNNcO1WnnJc) | → 提取 | `2-Areas/Work/业务管理/项目复盘模板.md` |
| 项目规划.md | [[4-Archives/Notes/Feishu/知识库/项目管理/项目规划]] | [飞书](https://reliablesense.feishu.cn/wiki/IkiEw4MTPieyHrkEcIhcLXGingh) | → 提取 | `2-Areas/Work/业务管理/项目规划模板.md` |

### 9c. 规章制度

| 文件 | 本地路径 | 飞书链接 | 决策 | 目标路径 |
|------|---------|---------|------|---------|
| 人力资源制度.md | [[4-Archives/Notes/Feishu/知识库/规章制度/人力资源制度]] | [飞书](https://reliablesense.feishu.cn/doc/doccnw7E90pRZqZbad9ZqMraele) | → 提取 | `2-Areas/Work/团队管理/人力资源制度.md` |
| 人力资源制度/ 子目录 | [[4-Archives/Notes/Feishu/知识库/规章制度/人力资源制度/]] | [飞书（目录）](https://reliablesense.feishu.cn/doc/doccnw7E90pRZqZbad9ZqMraele) | → 提取 | `2-Areas/Work/团队管理/人力资源制度/` |
| 公关制度.md | [[4-Archives/Notes/Feishu/知识库/规章制度/公关制度]] | [飞书](https://reliablesense.feishu.cn/doc/doccn8tPZL9k9QZy2MzWif1qWDb) | → 提取 | `2-Areas/Work/综合管理/公关制度.md` |
| 法务制度.md | [[4-Archives/Notes/Feishu/知识库/规章制度/法务制度]] | [飞书](https://reliablesense.feishu.cn/doc/doccn2IXTE0xjbI4zNUzhNjdOCc) | → 提取 | `2-Areas/Work/综合管理/法务制度.md` |
| 财务制度.md | [[4-Archives/Notes/Feishu/知识库/规章制度/财务制度]] | [飞书](https://reliablesense.feishu.cn/doc/doccn1pktcI7i62LgQO3wTFvCDh) | → 提取 | `2-Areas/Work/综合管理/财务制度.md` |
| 采购制度.md | [[4-Archives/Notes/Feishu/知识库/规章制度/采购制度]] | [飞书](https://reliablesense.feishu.cn/doc/doccnNlv7YbCNSsWjdLnLTkRYWb) | → 提取 | `2-Areas/Work/综合管理/采购制度.md` |

### 9d. 个人知识库

| 文件 | 本地路径 | 飞书链接 | 决策 | 目标路径 |
|------|---------|---------|------|---------|
| Iot接口对接代码.md | [[4-Archives/Notes/Feishu/知识库/个人知识库/Iot接口对接代码]] | [飞书](https://reliablesense.feishu.cn/wiki/PJMvwq7JFipjUIkquXpcVEt2nUf) | → 提取 | `3-Resources/Tech/代码片段/IoT接口对接代码.md` |
| Rocket命令行测试.md | [[4-Archives/Notes/Feishu/知识库/个人知识库/Rocket命令行测试]] | [飞书](https://reliablesense.feishu.cn/wiki/NECEwJ2pUienKZkrcsRc6Pranyg) | → 提取 | `3-Resources/Tech/代码片段/RocketMQ命令行测试.md` |
| 订阅压线事件.md | [[4-Archives/Notes/Feishu/知识库/个人知识库/订阅压线事件]] | [飞书](https://reliablesense.feishu.cn/wiki/UwMHwNSUxie9kNkrqVwc0SwOnKe) | → 提取 | `3-Resources/Tech/知识卡片/订阅压线事件.md` |
| 车载定位连调总结.md | [[4-Archives/Notes/Feishu/知识库/个人知识库/车载定位连调总结]] | [飞书](https://reliablesense.feishu.cn/wiki/I7C8w9kEBiLR3YkaRyJcbekunVf) | → 提取 | `3-Resources/Tech/知识卡片/车载定位连调总结.md` |
| 重定位.md | [[4-Archives/Notes/Feishu/知识库/个人知识库/重定位]] | [飞书](https://reliablesense.feishu.cn/wiki/EcASw46qMijgXFkNqQZcWstJnWe) | → 提取 | `3-Resources/Tech/知识卡片/重定位.md` |
| 南宁机场2025年12月26日.md | [[4-Archives/Notes/Feishu/知识库/个人知识库/南宁机场2025年12月26日]] | [飞书](https://reliablesense.feishu.cn/wiki/SLcMwfrKlibIwqkwU6ccaTVZnIc) | → 提取 | `1-Projects/Work/南宁机场/南宁机场记录.md` |
| 工作交接.md | [[4-Archives/Notes/Feishu/知识库/个人知识库/工作交接]] | [飞书](https://reliablesense.feishu.cn/wiki/KumhwCH0JiPH97k7CI5cOVcznsf) | → 提取 | `4-Archives/Areas/Work/团队管理/团队成员/陈子杰/` | 同事工作交接文档，按人归档 |
| 测试总结.md | [[4-Archives/Notes/Feishu/知识库/个人知识库/测试总结]] | [飞书](https://reliablesense.feishu.cn/wiki/Bv23wHWcfi8SuOkDS38c8TAynZc) | → 提取 | `4-Archives/Areas/Work/团队管理/团队成员/陈子杰/` | 同事测试总结，按人归档 |
| 运行有问题的项目及其结果截图.md | [[4-Archives/Notes/Feishu/知识库/个人知识库/运行有问题的项目及其结果截图]] | [飞书](https://reliablesense.feishu.cn/wiki/SAC6wR9XXiiBAKk0uvAcBPI4nmd) | 留归档 | 临时记录 |
| 知识问答-Space7527246326739157011.md | [[4-Archives/Notes/Feishu/知识库/个人知识库/知识问答-Space7527246326739157011]] | [飞书](https://reliablesense.feishu.cn/wiki/AR6QwWP4yiUZUrku6F8c2LUvnDc) | 留归档 | 飞书 AI 问答 |
| 知识问答-Space7527250303092015107.md | [[4-Archives/Notes/Feishu/知识库/个人知识库/知识问答-Space7527250303092015107]] | [飞书](https://reliablesense.feishu.cn/wiki/Mb5Sw96iIiXgDkkgB79ciA13nph) | 留归档 | 飞书 AI 问答 |
| 视频会议助手与陈子杰的会话.md | [[4-Archives/Notes/Feishu/知识库/个人知识库/视频会议助手与陈子杰的会话]] | [飞书](https://reliablesense.feishu.cn/wiki/AH3AwTtFVizchQky49sc1R4vnYc) | → 提取 | `4-Archives/Areas/Work/团队管理/团队成员/陈子杰/` |
| 费用报销单.xlsx | [[4-Archives/Notes/Feishu/知识库/个人知识库/费用报销单.xlsx]] | [飞书](https://reliablesense.feishu.cn/wiki/YDALwrkOgipenTkarYrcvNEEnPg?table=tbl8OSrYcXrhnivM) | 留归档 | 个人财务 |

### 9e. 受限知识库

| 文件 | 本地路径 | 飞书链接 | 决策 | 目标路径 |
|------|---------|---------|------|---------|
| Map-mobile-v2.7版本更新报告.md | [[4-Archives/Notes/Feishu/知识库/受限知识库/Map-mobile-v2.7版本更新报告]] | [飞书](https://reliablesense.feishu.cn/wiki/WiJ2wFB10iQ98skKC4lcgQgqn9b) | → 提取 | `2-Areas/Work/产品研发/Map-mobile-v2.7更新报告.md` |
| 前端Admin-2.7更新内容.md | [[4-Archives/Notes/Feishu/知识库/受限知识库/前端Admin-2.7更新内容]] | [飞书](https://reliablesense.feishu.cn/wiki/OaQpwHMvhiduTDk5lBqcluCfnPf) | → 提取 | `2-Areas/Work/产品研发/前端Admin-2.7更新内容.md` |
| 后端2.7更新内容.md | [[4-Archives/Notes/Feishu/知识库/受限知识库/后端2.7更新内容]] | [飞书](https://reliablesense.feishu.cn/wiki/AYprwPzeGiWaPlkUnVxcQWbMndc) | → 提取 | `2-Areas/Work/产品研发/后端2.7更新内容.md` |
| 新太元验收标准总结.md | [[4-Archives/Notes/Feishu/知识库/受限知识库/新太元验收标准总结]] | [飞书](https://reliablesense.feishu.cn/wiki/LbYbwPb1QidoL0kpKakcRhCrnPe) | → 提取 | `1-Projects/Work/新太项目/验收标准总结.md` |
| 新太项目总结.md | [[4-Archives/Notes/Feishu/知识库/受限知识库/新太项目总结]] | [飞书](https://reliablesense.feishu.cn/wiki/TK3Sw7sNkiEFD1kFx27cLTkznAV) | → 提取 | `1-Projects/Work/新太项目/项目总结.md` |
| 2025年年终总结-后端.md | [[4-Archives/Notes/Feishu/知识库/受限知识库/2025年年终总结-后端]] | [飞书](https://reliablesense.feishu.cn/wiki/ZSDawo3uLi4lxXkGZP7cHGxBnXc) | → 提取 | `4-Archives/Areas/Work/团队管理/团队成员/王宗光/` | 年终总结，按人归档 |
| 2025年度总结-前端.md | [[4-Archives/Notes/Feishu/知识库/受限知识库/2025年度总结-前端]] | [飞书](https://reliablesense.feishu.cn/wiki/MqWawqoYkiJsQekf1y2c8Hatnve) | → 提取 | `4-Archives/Areas/Work/团队管理/团队成员/陈子杰/` | 年终总结，按人归档 |
| 刘远达25年年终总结.md | [[4-Archives/Notes/Feishu/知识库/受限知识库/刘远达25年年终总结]] | [飞书](https://reliablesense.feishu.cn/wiki/TfMYwzD5citiR0kXrffcRYNUn8d) | → 提取 | `4-Archives/Areas/Work/团队管理/团队成员/刘远达/` | 年终总结，按人归档 |

---

## 十、需要新建的 PARA 目录

```
2-Areas/Work/运维管理/
3-Resources/Tech/环境配置/
3-Resources/Tech/环境配置/
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
| → 提取到 3-Resources/Tech/ | ~65 个 .md | 代码片段、知识卡片、环境配置 |
| → 提取到 3-Resources/Business/ | ~50 个 .md + .pptx | 23 个行业解决方案 |
| → 提取到 2-Areas/Work/ | ~55 个 .md | 运维管理、制度、模板、品牌宣传、团队管理 |
| → 提取到 1-Projects/Work/ | ~30 个 .md | 进行中项目的技术文档 |
| → 归档到 4-Archives/Projects/Work/ | ~90 个项目目录 | 已结束项目 |
| 留归档不动 | ~5000+ 个文件 | 无上下文临时文件、旧版本重复文件、媒体附件、安装包等真正无用的文件 |

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

## 十三、王宗光个人文档（补充）

### 工作总结 → `4-Archives/Areas/Work/团队管理/团队成员/王宗光/`

| 文件 | 本地路径 | 飞书链接 | 决策 | 理由 |
|------|---------|---------|------|------|
| 2024年度工作总结 | 云空间/王宗光的个人文档/工作总结/ | - | → 提取 | `4-Archives/Areas/Work/团队管理/团队成员/王宗光/` |
| 2024年中工作总结 | 云空间/王宗光的个人文档/工作总结/ | - | → 提取 | `4-Archives/Areas/Work/团队管理/团队成员/王宗光/` |
| 2023年度工作总结 | 云空间/王宗光的个人文档/工作总结/ | - | → 提取 | `4-Archives/Areas/Work/团队管理/团队成员/王宗光/` |
| 2023年度工作总结.mm | 云空间/王宗光的个人文档/工作总结/ | - | → 提取 | `4-Archives/Areas/Work/团队管理/团队成员/王宗光/` |

### 项目资料

#### 嘉盛工厂 → `4-Archives/Projects/Work/嘉盛工厂/`

| 文件 | 类型 | 飞书链接 | 目标路径 |
|------|------|---------|---------|
| 1-2502211H23Q59（W200PG-CAT1设备TCP协议） | docx | [飞书](https://reliablesense.feishu.cn/docx/KdFmdGbaBodNKHxstx6cbhzWn3g) | `4-Archives/Projects/Work/嘉盛工厂/` |
| 工作记录 | docx | [飞书](https://reliablesense.feishu.cn/docx/LkFQdJGmBoBeM8xqlPZcK0EWnbe) | `4-Archives/Projects/Work/嘉盛工厂/` |
| 嘉盛工厂项目进度计划表 副本 | sheet | [飞书](https://reliablesense.feishu.cn/sheets/EswasJvZrhia4ftJQVrc9bX8nBc) | `4-Archives/Projects/Work/嘉盛工厂/` |
| 蓝牙定位平台接口文档V1.61_250409.pdf | file | [飞书](https://reliablesense.feishu.cn/file/TwdAbVtybo6bYyxamOhcemubnTf) | `2-Areas/Work/设备管理/蓝策蓝牙AOA/` |
| 需求说明书.docx | file | [飞书](https://reliablesense.feishu.cn/file/N4HubB8QNoU07nxIX7Fc16XWnde) | `4-Archives/Projects/Work/嘉盛工厂/` |
| JT808_部标精简协议(2021-11-24更改).pdf | file | [飞书](https://reliablesense.feishu.cn/file/N6v1bgyQcon6ahx1jPyc9U3NnSc) | `4-Archives/Projects/Work/嘉盛工厂/` |
| 808协议集成 & 指令下发.txt | file | [飞书](https://reliablesense.feishu.cn/file/BkaIbNoeSo2Nb7xZ1wQckNYRn1b) | `4-Archives/Projects/Work/嘉盛工厂/` |

#### 赛力斯 → `2-Areas/Work/业务管理/售前项目/赛力斯/`

| 文件 | 类型 | 飞书链接 | 目标路径 |
|------|------|---------|---------|
| 数字化循环载具管理平台统一接口协议V1.4 | docx | [飞书](https://reliablesense.feishu.cn/docx/Af4wdLHdhoaaeJxzscucmKyQnEf) | `2-Areas/Work/业务管理/售前项目/赛力斯/` |
| 设备相关资料 | docx | [飞书](https://reliablesense.feishu.cn/docx/Vw2ZdVXLloMFarxu7BscvzlxnKb) | `2-Areas/Work/业务管理/售前项目/赛力斯/` |

#### 博实结 → `4-Archives/Projects/Work/博实结/`

| 文件 | 类型 | 飞书链接 | 目标路径 |
|------|------|---------|---------|
| 智能硬件定位服务（2024-07-12） | docx | [飞书](https://reliablesense.feishu.cn/docx/Z2DKdMZxBoDiiKxyXtUch3d6nFc) | `4-Archives/Projects/Work/博实结/` |
| EG10E部标协议 | docx | [飞书](https://reliablesense.feishu.cn/docx/EV9gdgpxdoguXbxvhTjc8rVSn2d) | `4-Archives/Projects/Work/博实结/` |
| EG10E产品使用说明书(4) | docx | [飞书](https://reliablesense.feishu.cn/docx/GuqpdulGkoBsZUxm10pc1PwWnld) | `4-Archives/Projects/Work/博实结/` |
| 联调记录 | docx | [飞书](https://reliablesense.feishu.cn/docx/MzxSduc4soHPCZxY1aTcta0Dnfe) | `4-Archives/Projects/Work/博实结/` |

#### 洛阳化工 → `1-Projects/Work/洛阳化工厂/`

| 文件 | 类型 | 飞书链接 | 目标路径 |
|------|------|---------|---------|
| 洛阳化工（定制功能）系统设计 | docx | [飞书](https://reliablesense.feishu.cn/docx/QbSTdG086oR3a6xOlgAcQNqNnEj) | `1-Projects/Work/洛阳化工厂/` |
| 应用系统联调测试报告-模板v5.docx | file | [飞书](https://reliablesense.feishu.cn/file/SlFHbIfCxoRaXaxZqxHcoQwtnhf) | `1-Projects/Work/洛阳化工厂/` |
| 中国石化统一身份OAuth2.0认证集成指南v2.8.pdf | file | [飞书](https://reliablesense.feishu.cn/file/QfpBb88rNoiezKxgieQcMXctncf) | `1-Projects/Work/洛阳化工厂/` |
| 中国石化统一身份管理系统操作手册v1.1.pdf | file | [飞书](https://reliablesense.feishu.cn/file/TFpVb6pj1oVL7Mxno5OcyNjFnOg) | `1-Projects/Work/洛阳化工厂/` |
| 中国石化统一身份消息订阅.NET版v4.3.pdf | file | [飞书](https://reliablesense.feishu.cn/file/M8eDbzCOjof23DxiroQccvWZnjI) | `1-Projects/Work/洛阳化工厂/` |
| 中国石化统一身份JWT认证集成指南v3.1.pdf | file | [飞书](https://reliablesense.feishu.cn/file/DClEbe3Z2ownR7xZ1T7cGAeknbc) | `1-Projects/Work/洛阳化工厂/` |

#### 广州机场 → `1-Projects/Work/广州机场/`

| 文件 | 类型 | 飞书链接 | 目标路径 |
|------|------|---------|---------|
| 广州机场App登录验证码 | docx | [飞书](https://reliablesense.feishu.cn/docx/ZxChdrcWCofAbxxzQEIcRopQnPg) | `1-Projects/Work/广州机场/` |

### 定制化项目

| 文件 | 类型 | 飞书链接 | 目标路径 | 理由 |
|------|------|---------|---------|------|
| NFC读卡器接口配置文档 | docx | [飞书](https://reliablesense.feishu.cn/docx/BYIudCklRoDYMixFu6Xc9HA9n1d) | `1-Projects/Work/新太项目/` | 新太项目NFC |

### 后端架构（有价值的技术文档）

| 文件 | 类型 | 飞书链接 | 目标路径 | 理由 |
|------|------|---------|---------|------|
| LBS系统梳理 | docx | [飞书](https://reliablesense.feishu.cn/docx/B6SgdFSRaoPqd7xQoTOcZGMAncd) | `2-Areas/Work/产品研发/` | 后端架构文档 |
| RS-LBS后端平台架构重构方案(v2.0.0) | docx | [飞书](https://reliablesense.feishu.cn/docx/WctjdFkvSoAIJ8x3t1scyrXVnXc) | `2-Areas/Work/产品研发/` | 后端架构 |
| RS-MID中间件平台架构方案(v1.0.0) | docx | [飞书](https://reliablesense.feishu.cn/docx/PYwpd0PL3owk84xKLsNcQCy8nmh) | `2-Areas/Work/产品研发/` | 中间件架构 |
| Zone + tile38功能实现备忘 | docx | [飞书](https://reliablesense.feishu.cn/docx/QI0SdzgAsol9SKxEh2wcWOkJnZc) | `3-Resources/Tech/知识卡片/` | 平台功能备忘 |
| position重构 | mindnote | [飞书](https://reliablesense.feishu.cn/mindnotes/YbkQbIQOsmcou8nM7aTcupE8n0d) | 留归档 | mindnote保留链接 |

### 测试/压测

| 文件 | 类型 | 飞书链接 | 目标路径 | 理由 |
|------|------|---------|---------|------|
| 230环境 | docx | [飞书](https://reliablesense.feishu.cn/docx/MUo8dYBWXoBwpBxdHfTcV2UJnag) | `3-Resources/Tech/代码片段/` | 压测环境配置 |
| 压测备忘录 | docx | [飞书](https://reliablesense.feishu.cn/docx/TEUJd4UxnocvIIxgsy3cA58qn9g) | `3-Resources/Tech/代码片段/` | 压测操作 |
| 标签数量压测数据统计_3.0 | sheet | [飞书](https://reliablesense.feishu.cn/sheets/BuXPsjDGhhwrAKtNlX8c8vttnPx) | `3-Resources/Tech/代码片段/` | 最新版压测数据 |
| 标签数量压测数据统计_2.0 | sheet | [飞书](https://reliablesense.feishu.cn/sheets/P6SJsvzAOhu9RvtlnQtc3P4snkf) | `4-Archives/Areas/Work/团队管理/团队成员/王宗光/` | 旧版本压测 |
| 标签数量压测数据统计_1.0 | sheet | [飞书](https://reliablesense.feishu.cn/sheets/QGicsCeb2hEFrAtSqK6cfsBkn0d) | `4-Archives/Areas/Work/团队管理/团队成员/王宗光/` | 旧版本压测 |
| 获取规划路线接口性能测试 | sheet | [飞书](https://reliablesense.feishu.cn/sheets/QaM9sFjaihS6dotCVfgcEk48n2g) | `3-Resources/Tech/代码片段/` | 路网性能测试 |

### 散落文档

| 文件 | 类型 | 飞书链接 | 决策 | 目标路径 | 理由 |
|------|------|---------|------|---------|------|
| E-Ink平台安装和使用手册 | docx | [飞书](https://reliablesense.feishu.cn/docx/BTKgdqfbXowNV5x0DSfcfafpncY) | → 提取 | `2-Areas/Work/设备管理/` | 墨水屏手册 |
| 智慧工厂电子标牌管理系统软件v1.0.0-json格式 | docx | [飞书](https://reliablesense.feishu.cn/docx/TYe7doOyNovyfLxfXOScJ2vyngf) | → 提取 | `2-Areas/Work/产品研发/` | 电子标牌系统 |
| 日志说明 | docx | [飞书](https://reliablesense.feishu.cn/docx/BdUEdhqBIofw1YxY2nGc8jEfn7d) | → 提取 | `3-Resources/Tech/知识卡片/` | 日志说明 |
| 莱讯-移动端需求 | docx | [飞书](https://reliablesense.feishu.cn/docx/U1EedFUBmoNwPQxD9oHcWweanXc) | → 提取 | `2-Areas/Work/产品研发/` | 移动端需求 |
| 无动力设备信息融合系统-源代码 | docx | [飞书](https://reliablesense.feishu.cn/docx/doxcnWD87qgPTeUnEIrenFMqHYf) | → 提取 | `1-Projects/Work/广州机场/` | 无动力设备系统 |
| 交接文档 | docx | [飞书](https://reliablesense.feishu.cn/docx/UOvmd7dz4oFkXVxuq3OczvtrnHf) | → 提取 | `2-Areas/Work/运维管理/` | 项目交接文档 |
| 问题处理记录/工作记录 | docx | [飞书](https://reliablesense.feishu.cn/docx/LHvPda1imoHU2Jxj4SncmovqnRf) | → 提取 | `3-Resources/Tech/问题解决/` | 问题处理记录 |
| 用户敏感信息处理.md | file | [飞书](https://reliablesense.feishu.cn/file/N4wvbKBhfoKdLMxIlQRckQAlnpd) | → 提取 | `3-Resources/Tech/知识卡片/` | 敏感信息处理 |
| 🚩会议签到表 | bitable | [飞书](https://reliablesense.feishu.cn/base/ZQj0bMC5eaghvxsBxzGcBWDznUc) | → 提取 | `4-Archives/Areas/Work/团队管理/团队成员/王宗光/` | bitable |
| 远端接口新需求问题反馈-20230323 | sheet | [飞书](https://reliablesense.feishu.cn/sheets/shtcniz2m6u89tCpHodDRbIhDxd) | → 提取 | `4-Archives/Areas/Work/团队管理/团队成员/王宗光/` | 历史需求反馈 |
| 标书3 | docx | [飞书](https://reliablesense.feishu.cn/docx/JBxYdx0OZoySuUx2hkicNerDnNb) | → 提取 | `4-Archives/Areas/Work/团队管理/团队成员/王宗光/` | 历史标书 |
| 众合Demo环境--软件 功能_20210701 | docx | [飞书](https://reliablesense.feishu.cn/docx/doxcnF0mpOOrz5DbDYLjwWB6VWb) | → 提取 | `4-Archives/Areas/Work/团队管理/团队成员/王宗光/` | 历史Demo |
| 王宗光24年周报.xlsx | file | [飞书](https://reliablesense.feishu.cn/file/WRgCb0V8ToSCsqx2qSdcW81Fnlh) | → 提取 | `4-Archives/Areas/Work/团队管理/团队成员/王宗光/` | 周报 |
| 莱讯科技（苏州）与博世（中国）家电展厅会议纪要 | docx | [飞书](https://reliablesense.feishu.cn/docx/FXjzdUWweozVIAxCLpUcspXXnpb) | → 提取 | `4-Archives/Areas/Work/团队管理/团队成员/王宗光/` | 博世会议 |
| 莱讯智能定位安全管理系统报价-20220422 | bitable | [飞书](https://reliablesense.feishu.cn/base/P1X5bHcrtaw23vsIHhMcb3YGnue) | → 提取 | `4-Archives/Areas/Work/团队管理/团队成员/王宗光/` | 历史报价 |
| 2023-7-10 来邦沟通会 | mindnote | [飞书](https://reliablesense.feishu.cn/mindnotes/HjIQbXkkTmr5zfnfgsCcck71n4c) | → 提取 | `4-Archives/Areas/Work/团队管理/团队成员/王宗光/` | mindnote |

---

## 十四、陈子杰个人文档（补充）

### 广州机场-移动应用平台

| 文件 | 类型 | 飞书链接 | 目标路径 | 理由 |
|------|------|---------|---------|------|
| 移动终端目前缺失功能 | bitable | [飞书](https://reliablesense.feishu.cn/base/RLRqbFnrPaokuRsVtTbcjkMLnZd) | `1-Projects/Work/广州机场/` | 移动应用缺失功能 |
| 深化设计说明书（移动应用服务平台）-2025 | docx | [飞书](https://reliablesense.feishu.cn/docx/B2erdpLOJo5lqoxNeyucOFo2nYf) | `1-Projects/Work/广州机场/` | 移动应用深化设计 |
| 移动应用平台开发与测试进展汇报.pdf | file | [飞书](https://reliablesense.feishu.cn/file/Kkf6bl2V4oAr5vx5m4QccUDDniI) | `1-Projects/Work/广州机场/` | 移动应用进展 |
| app_store_back-main.zip | file | [飞书](https://reliablesense.feishu.cn/file/Ugv8bHqsAosoRmxmBQxcUBcOnDb) | `1-Projects/Work/广州机场/` | 应用商店后端代码 |
| app_store_flutter_module-main.zip | file | [飞书](https://reliablesense.feishu.cn/file/RFX9bi65aoymAAxNFgUcHtlRn5f) | `1-Projects/Work/广州机场/` | Flutter模块 |
| appstoreaf-main.zip | file | [飞书](https://reliablesense.feishu.cn/file/Wv5yb07DVon7EvxNBOPc6yFDn0c) | `1-Projects/Work/广州机场/` | 应用商店前端 |
| readme.txt | file | [飞书](https://reliablesense.feishu.cn/file/KsdVbaNAvo4hXrx7rEhc1x3pnch) | `1-Projects/Work/广州机场/` | 应用商店说明 |

### 散落文档

| 文件 | 类型 | 飞书链接 | 决策 | 目标路径 | 理由 |
|------|------|---------|------|---------|------|
| oemusers | sheet | [飞书](https://reliablesense.feishu.cn/sheets/GBc0sFzfKhEtBztmsAPcp5m5n4w) | → 提取 | `1-Projects/Work/广州机场/` | OEM用户数据 |
| t_poi_type | sheet | [飞书](https://reliablesense.feishu.cn/sheets/EKkcsQr7MhV8S7teOsTcf1ISnUc) | → 提取 | `2-Areas/Work/产品研发/` | POI类型数据 |
| 三方系统调用行李查询接口文档(座位号)20230804 | docx | [飞书](https://reliablesense.feishu.cn/docx/E3UidCx5No6qqnx2VgjcXVzdnsg) | → 提取 | `1-Projects/Work/广州机场/` | 行李查询接口 |
| 平台地图最新使用 | docx | [飞书](https://reliablesense.feishu.cn/docx/QbGcdI4iDok1XPxFdEUckHemnR5) | → 提取 | `3-Resources/Tech/知识卡片/` | 地图使用文档 |
| 小程序签到功能方案 | docx | [飞书](https://reliablesense.feishu.cn/docx/GxYfddex4oDcpUxG0JHcGbZEndg) | → 提取 | `2-Areas/Work/产品研发/` | 小程序签到方案 |
| 大屏页面问题 | docx | [飞书](https://reliablesense.feishu.cn/docx/OVEnde4fhoJnAPxjgr9c2WZfnIc) | → 提取 | `3-Resources/Tech/问题解决/` | 大屏页面问题 |
| 流程图 | docx | [飞书](https://reliablesense.feishu.cn/docx/BWGKd2466omTdxxjRQdciMNknyh) | → 提取 | `2-Areas/Work/产品研发/` | 产品流程图 |
| 部门季报/半年报/年报 | docx | [飞书](https://reliablesense.feishu.cn/docx/AuQldFCasoVwtLxNejocWWv8nqg) | → 提取 | `4-Archives/Areas/Work/团队管理/团队成员/陈子杰/` | 部门报告 |
| 车间定位项目立项报告 | docx | [飞书](https://reliablesense.feishu.cn/docx/Iw5cdoeumo3fVhxCZjYcw8j4nBc) | → 提取 | `4-Archives/Areas/Work/团队管理/团队成员/陈子杰/` | 历史立项 |
| 需求及 Bug 管理 | bitable | [飞书](https://reliablesense.feishu.cn/base/ZmmjbljSpa3KWBskm40cPgWGnPg) | → 提取 | `4-Archives/Areas/Work/团队管理/团队成员/陈子杰/` | bitable |
| 问题记录-2023-09-22 | sheet | [飞书](https://reliablesense.feishu.cn/sheets/ILedsU7eShMXojtZmy0cTiHln9c) | 留归档 | - | 历史问题记录 |
| 室内定位系统工作进度 | sheet | [飞书](https://reliablesense.feishu.cn/sheets/Xl6HsOeCMhUrDwtMewMcElDGnyd) | 留归档 | - | 历史进度 |
| 招标需求 | docx | [飞书](https://reliablesense.feishu.cn/docx/NQXudjxpjo39fpxEYencmva4nke) | → 归档 | `4-Archives/Projects/Work/武汉机场/` | 武汉机场招标需求 |
| 后端翻译 | docx | [飞书](https://reliablesense.feishu.cn/docx/XULYdzrgOoC9TpxsG2GcTFBJnLf) | → 提取 | `4-Archives/Areas/Work/团队管理/团队成员/陈子杰/` | 翻译文件 |
| 核心物联资料.zip | file | [飞书](https://reliablesense.feishu.cn/file/MAbLblaVGoQUsEx9a4NcxF5Kn0g) | → 提取 | `2-Areas/Work/设备管理/核芯物联蓝牙AOA/` | 核芯物联资料 |
| 2023-05-07 20-54-59.mkv | file | [飞书](https://reliablesense.feishu.cn/file/BRc2bmrbKoPzjvxIKmPcBoOFnof) | → 提取 | `4-Archives/Areas/Work/团队管理/团队成员/陈子杰/` | 录屏文件 |

---

## 十五、孙永霖个人文档（补充）

| 文件 | 类型 | 飞书链接 | 决策 | 目标路径 | 理由 |
|------|------|---------|------|---------|------|
| saas英文版 | docx | [飞书](https://reliablesense.feishu.cn/docx/LZgYdpRnzouGpKxnOdZc4vDRnPg) | → 提取 | `2-Areas/Work/产品研发/` | SaaS英文文档 |
| SaaS使用手册V4 new 英文.docx | file | [飞书](https://reliablesense.feishu.cn/file/boxcnrTNYMWwqMq49WzzapEj30g) | → 提取 | `2-Areas/Work/产品研发/` | SaaS英文手册 |
| SaaS使用手册V4 new.docx | file | [飞书](https://reliablesense.feishu.cn/file/boxcnKrzYX5prPEiZIv33AL6mlc) | → 提取 | `2-Areas/Work/产品研发/` | SaaS中文手册 |
| 地图管理的问题 | docx | [飞书](https://reliablesense.feishu.cn/docx/doxcnesMSLP6dXGeKzB6EibeSCx) | 留归档 | - | 地图管理问题 |
| Help Center Template | docx | [飞书](https://reliablesense.feishu.cn/docx/DaQhd5gMxowrj6xCReccmQKanIg) | → 提取 | `4-Archives/Areas/Work/团队管理/团队成员/孙永霖/` | 模板文档 |
| 需翻译！！Matthias 英文稿 - 已翻译 | docx | [飞书](https://reliablesense.feishu.cn/docx/ZYXldX00mosg8cxjIAucj6pPnRc) | → 提取 | `4-Archives/Areas/Work/团队管理/团队成员/孙永霖/` | 翻译稿 |
| 需翻译！！Matthias 英文稿 | docx | [飞书](https://reliablesense.feishu.cn/docx/Ks4UdBsYPoMzuaxAqvpcVabDnFd) | → 提取 | `4-Archives/Areas/Work/团队管理/团队成员/孙永霖/` | 翻译稿 |
| doc/Attachments/*.png（17个） | file | | 跟随文档 | saas英文版 → `2-Areas/Work/产品研发/Attachments/`，Help Center Template → `4-Archives/Areas/Work/团队管理/团队成员/孙永霖/Attachments/` | 文档内嵌图片，跟随所属文档移动 |

---

## 十六、云空间根目录散落文件（补充）

之前第一章已覆盖大部分，以下是补充的散落文件：

| 文件 | 类型 | 飞书链接 | 决策 | 目标路径 | 理由 |
|------|------|---------|------|---------|------|
| 广州机场综合定位 v.2025-12-19 | bitable | [飞书](https://reliablesense.feishu.cn/base/NbIPbswwSaCfPpsWak7cbCHsnwe) | → 提取 | `1-Projects/Work/广州机场/` | 广州机场综合定位数据 |
| 信息平台消息交换标准协议_1.0.0(1).doc | file | [飞书](https://reliablesense.feishu.cn/file/RGtdbb0EYogQjHxMaxmcnf57n5b) | → 归档 | `4-Archives/Projects/Work/武汉机场/` | 武汉机场接口协议 |
| 李家豪轨迹室内异常.png | file | [飞书](https://reliablesense.feishu.cn/file/NYJ9b9PpRo1IgMxmAvgcjaYZnMh) | → 归档 | `1-Projects/Work/麦钉项目/` | 麦钉项目截图 |
| 韩家村统计时长缺失.png | file | [飞书](https://reliablesense.feishu.cn/file/B5bHb0v8goCfnZxMCD4cyJvjnn9) | → 归档 | `1-Projects/Work/麦钉项目/` | 麦钉项目截图 |
| 教学比赛.mov | file | [飞书](https://reliablesense.feishu.cn/file/AUT0b1zsdo1SQdxXCgHc9epunIf) | 留归档 | - | 个人文件 |
| 宏兴裁切.rar | file | [飞书](https://reliablesense.feishu.cn/file/P5MBb8Cy6oYsYfx3MZjc8BhonCd) | → 归档 | `1-Projects/Work/洛阳化工厂/` | 洛阳项目文件 |
| FRP_GithubArm64_version_1_3_6.apk | file | [飞书](https://reliablesense.feishu.cn/file/YMF3bIlvFoTvxaxPI6IcKLwMnNc) | 留归档 | - | 安装包 |
| 定位平台安装文件及文档.zip | file | [飞书](https://reliablesense.feishu.cn/file/Hr8bbKyRUoKdDtxgtLhcfDCknug) | 留归档 | - | 安装包 |
| madinat_hjc.zip | file | [飞书](https://reliablesense.feishu.cn/file/UnIjb9C7qocVGExPTZpc9wkAnog) | → 归档 | `1-Projects/Work/麦钉项目/` | 麦钉项目数据包 |
| 转化后数据.zip | file | [飞书](https://reliablesense.feishu.cn/file/NXVgbTKQioF6Kkx26yScwwRbnjg) | → 归档 | `1-Projects/Work/麦钉项目/` | 麦钉项目数据 |

---

## 十七、莱讯科技其他子目录（补充）

### 公司内部资料散落文件

| 文件 | 类型 | 飞书链接 | 决策 | 目标路径 | 理由 |
|------|------|---------|------|---------|------|
| 库房管理 | bitable | [飞书](https://reliablesense.feishu.cn/base/PF71bTA9Yaqo3yscmxlcsdsnnVU) | → 提取 | `2-Areas/Work/设备管理/` | 库房管理 |
| 合同订单管理 | bitable | [飞书](https://reliablesense.feishu.cn/base/bascnemc8tozwPeCvL2GmUfG9Tg) | → 提取 | `2-Areas/Work/综合管理/` | 合同订单管理 |
| 任务管理 | bitable | [飞书](https://reliablesense.feishu.cn/base/bascnm0yQj7bRGrIZE1vSUXMOGg) | 留归档 | - | bitable保留链接 |
| 组织架构图 | doc | [飞书](https://reliablesense.feishu.cn/docs/doccnyI23DHQUFVPNJX7wFsoF0f) | → 提取 | `2-Areas/Work/团队管理/` | 公司组织架构 |
| 莱讯公司文档分类 | mindnote | [飞书](https://reliablesense.feishu.cn/mindnotes/bmncnqFUTE8JqcJrJH049rDxF9b) | 留归档 | - | mindnote保留链接 |

### ~参考资料（留归档）

`~参考资料/` 下 6 个文档类附件全部为竞品参考资料，留归档不进 PARA：

- v1.0版-5-必须反馈文件-技术响应及技术方案-C122高精度定位系统.docx
- 叉车安全管理产品(2).pdf
- 防撞预警系统.pptx
- 中弈科技智慧矿山部分需确认资料(修改).pptx
- 功能截图.docx
- 易景空间-2024十二届电子信息博览会-路演ppt20240410.pdf

### 公司内部资料/参考（留归档）

`参考/` 下 18 个文档类附件为行业报告和管理参考，留归档不进 PARA：

- 2019智能硬件终端行业研究报告.pdf
- 2020年中国智能物联网（AIoT）白皮书.pdf
- 5G 室内融合定位白皮书 - ZTE.pdf
- 合作方案-20200910.docx
- 智能蓝牙照明app二期详细设计书Ver1.0.pptx
- 4敏捷组织设计原则.docx / 3五个关键推动敏捷绩效.docx / 5识别真正的敏捷组织.docx（管理参考）
- 其余为历史行业报告和参考文档

### 共享文件（全部留归档）

共享文件夹是临时网盘，全部留归档不进 PARA。包含 4 个 .txt 文件（登陆方式、MD5校验）和各种项目数据包。

### 画板文档

| 文件 | 类型 | 飞书链接 | 决策 | 理由 |
|------|------|---------|------|------|
| 画板文档 | docx | [飞书](https://reliablesense.feishu.cn/docx/RTWGd8ENYo9JSOxqoiRcEH3mnVf) | → 归档 | `4-Archives/Projects/Work/哒咖项目/` | 哒咖项目画板文档 |

### 项目开发管理散落文件

| 文件 | 类型 | 飞书链接 | 决策 | 理由 |
|------|------|---------|------|------|
| 项目管理流程 | mindnote | [飞书](https://reliablesense.feishu.cn/mindnotes/N0oObHdeam3taTnEDovcLbUFnmc) | → 提取 | `2-Areas/Work/业务管理/` | 项目管理流程思维导图 |
| 需求生命周期 | mindnote | [飞书](https://reliablesense.feishu.cn/mindnotes/QoDWb7hy7mPUXMnjnVDc7jArnvg) | → 提取 | `2-Areas/Work/产品研发/` | 需求生命周期思维导图 |
| 项目迭代流程 | mindnote | [飞书](https://reliablesense.feishu.cn/mindnotes/bmncnMWfRCAQqIY4UdwaMe12dVb) | → 提取 | `2-Areas/Work/产品研发/` | 项目迭代流程思维导图 |

### 项目运维管理散落文件

| 文件 | 类型 | 飞书链接 | 决策 | 目标路径 | 理由 |
|------|------|---------|------|---------|------|
| 莱讯科技-小程序管理文档 | docx | [飞书](https://reliablesense.feishu.cn/docx/JgCpdERLho9N3zxiGpqcQ7GAnov) | → 提取 | `2-Areas/Work/产品研发/` | 小程序管理 |
| 位置压测相关服务器配置.xlsx | file | [飞书](https://reliablesense.feishu.cn/file/JPHkbo3MZoCvClxqavvcqNvynKf) | → 提取 | `2-Areas/Work/产品研发/` | 压测服务器配置 |

---

## 十八、全量文件统计（2026-04-16 更新）

基于 `飞书文件清单与迁移状态.tsv` 的 5,800 个文件全量分析：

### 文件类型分布

| 类型 | 数量 | 说明 |
|------|------|------|
| file | 4,871 | 上传附件（.docx/.xlsx/.pptx/.pdf/.jpg/.mp4 等） |
| docx | 687 | 飞书新版文档（已转 Markdown） |
| sheet | 109 | 电子表格 |
| bitable | 43 | 多维表格 |
| mindnote | 43 | 思维导图 |
| doc | 28 | 旧版文档 |
| slides | 17 | 幻灯片 |
| shortcut | 2 | 快捷方式 |

### file 类型扩展名分布（Top 20）

| 扩展名 | 数量 | 处理方式 |
|--------|------|---------|
| jpg | 871 | 跟随目录规则 |
| png | 605 | 跟随目录规则 |
| docx | 562 | 按目录规则决策，重要的用 markitdown 查看 |
| pdf | 489 | 按目录规则决策 |
| mp4 | 365 | 跟随目录规则（视频） |
| xlsx | 247 | 按目录规则决策 |
| pptx | 238 | 按目录规则决策 |
| heic | 179 | 跟随目录规则（照片） |
| zip | 130 | 留归档 |
| dwg | 119 | 跟随目录规则（CAD图纸） |
| ds_store | 93 | 忽略 |
| ai | 92 | 跟随目录规则（设计文件） |
| doc | 88 | 按目录规则决策 |
| mov | 86 | 跟随目录规则（视频） |
| skp | 77 | 跟随目录规则（SketchUp） |
| psd | 72 | 跟随目录规则（Photoshop） |
| jpeg | 58 | 跟随目录规则 |
| cpa | 46 | 跟随目录规则 |
| txt | 33 | 按目录规则决策 |
| rar | 31 | 留归档 |

### 决策覆盖统计

| 分类 | 数量 | 说明 |
|------|------|------|
| 已按目录规则决策 | 2,451 | docx/doc/sheet/bitable/slides 等按映射规则分配 |
| 媒体/设计文件跟随目录 | 3,182 | 图片/视频/CAD/设计等跟随所在目录的规则 |
| 手动补充决策 | 160 | 本文档中逐个列出的散落文件 |
| 需人工判断 | 0 | 全部已决策 |
| **合计** | **5,794** | 覆盖率 99.9% |

### 目标路径分布

| 目标路径 | 文件数 | 说明 |
|---------|-------|------|
| `4-Archives/Projects/Work/` | ~912 | 已结束项目归档 |
| `1-Projects/Work/广州机场/` | ~180 | 进行中项目 |
| `2-Areas/Work/设备管理/供应商管理/` | ~228 | 供应商资料 |
| `2-Areas/Work/综合管理/公司制度/` | ~182 | ISO/规章制度 |
| `3-Resources/Business/解决方案/` | ~175 | 行业方案 |
| `2-Areas/Work/产品研发/` | ~160 | 产品文档 |
| `会议纪要（按分类规则）` | ~270 | 会议纪要 |
| `2-Areas/Work/综合管理/软著立项/` | ~76 | 软著资料 |
| `3-Resources/Tech/环境配置/` | ~55 | 集群/环境配置 |
| `2-Areas/Work/品牌宣传/` | ~100 | 品牌/展会/宣传 |
| `2-Areas/Work/业务管理/` | ~70 | 售前/模板/评估 |
| `3-Resources/Tech/代码片段/` | ~30 | 运维/部署/升级手册 |
| `3-Resources/Tech/知识卡片/` | ~15 | 技术知识文档 |
| `3-Resources/Tech/问题解决/` | ~10 | 问题解决记录 |
| `留归档` | ~3,200+ | 媒体文件+历史文件+临时文件 |

---

## 十九、待确认事项（更新）

### ✅ 全部已决策（0 个待确认）

### 已解决的待确认事项

1. ~~**参考/ 目录**~~ → 全部留归档（行业报告和管理参考）
2. ~~**~参考资料/**~~ → 全部留归档（竞品参考）
3. ~~**路网维护/**~~ → 留归档（路网文件无法读取）
4. ~~**共享文件/**~~ → 全部留归档（临时网盘）
5. **定制版项目子目录**：14 个定制化项目子目录，需逐个确认是否已结束（待执行时逐个处理）
6. **企业版/文档资料/ 子目录**：需查看具体内容（待执行时处理）
7. **售前项目/ 下 5 个客户目录**：需确认是否有正式立项（待执行时处理）
