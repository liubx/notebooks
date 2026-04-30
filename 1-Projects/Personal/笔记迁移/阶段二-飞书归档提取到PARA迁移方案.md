---
title: 阶段二-飞书归档提取到PARA迁移方案
type: design-doc
tags:
  - project/笔记迁移
created: 2026-04-11
---

# 阶段二：飞书归档提取到 PARA 迁移方案

基于 `4-Archives/Notes/Feishu/` 中已拉取的全量内容，逐文件审查后制定的迁移策略。

> ✅ 所有文件的目标路径已全部确认。

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
| API.docx（莱讯科技根目录） | - | [飞书](https://reliablesense.feishu.cn/file/EmmnbY7kboTZBMxx5pncq5cUnXe) | → 提取 | `1-Projects/Work/上港仓储管理/API.docx` | 上港项目相关 |
| 墨水屏数据协议.md | [[4-Archives/Notes/Feishu/云空间/根目录/墨水屏数据协议]] | [飞书](https://reliablesense.feishu.cn/docx/P4z0dkpVUoq3jwxUvBtcrRpundd) | → 提取 | `2-Areas/Work/设备管理/阿法迪蓝牙墨水屏/墨水屏数据协议.md` | 设备协议文档，归设备管理/阿法迪蓝牙墨水屏 |
| 系统架构图.md | [[4-Archives/Notes/Feishu/云空间/根目录/系统架构图]] | [飞书](https://reliablesense.feishu.cn/docx/IYLtdtwDQoaOetxP9Xkc66jfnPf) | → 提取 | `2-Areas/Work/产品研发/系统架构图.md` | 产品通用架构 |
| 系统整改配置表.md | [[4-Archives/Notes/Feishu/云空间/根目录/系统整改配置表]] | [飞书](https://reliablesense.feishu.cn/docx/ZpsNdChggodbeaxLg78cgtRBnGc) | → 提取 | `1-Projects/Work/广州机场/系统整改配置表.md` | 含 A域/B域、巡检app，属广州机场项目 |
| deploy.yaml | [[4-Archives/Notes/Feishu/云空间/根目录/deploy.yaml]] | [飞书](https://reliablesense.feishu.cn/file/RwsBbb50NoKUaKxeVutcaFWBnVd) | → 提取 | `1-Projects/Work/赛峰定位/deploy-sso.yaml` | 赛峰定位 SAML2/SSO 配置 |
| Doc2.docx | [[4-Archives/Notes/Feishu/云空间/根目录/Doc2.docx]] | [飞书](https://reliablesense.feishu.cn/file/VvsMbbh4OoziMkxwQGTcUXwMnYf) | → 归档 | `4-Archives/Projects/Work/中东电子厂/Doc2-波斯语翻译.docx` | 伊朗项目 UI 翻译 |
| 优化后.txt | [[4-Archives/Notes/Feishu/云空间/根目录/优化后.txt]] | [飞书](https://reliablesense.feishu.cn/file/OuyFbuM1touvroxyPjEcki2on0d) | 留归档 | - | 无上下文的临时文件 |
| map-mobile.mm | [[4-Archives/Notes/Feishu/云空间/根目录/map-mobile.mm]] | [飞书](https://reliablesense.feishu.cn/mindnotes/G7S6b8VC3mxDsPnZ1yDc4XItn2d) | → 提取 | `2-Areas/Work/产品研发/map-mobile参数设置.mm` |
| map-model.mm | [[4-Archives/Notes/Feishu/云空间/根目录/map-model.mm]] | [飞书](https://reliablesense.feishu.cn/mindnotes/ZVgJbqGpTmw5v9nD5vTcqEg8nfe) | → 提取 | `2-Areas/Work/产品研发/map-model参数设置.mm` |
| rssi数据.docx | [[4-Archives/Notes/Feishu/云空间/根目录/rssi数据.docx]] | [飞书](https://reliablesense.feishu.cn/file/WElAbEGxJoExttxZa90cDTeyn1X) | → 提取 | `2-Areas/Work/设备管理/rssi数据.docx` | 基站坐标和 RSSI 信号测试数据 |
| SaaS平台操作手册V7.docx | [[4-Archives/Notes/Feishu/云空间/根目录/SaaS平台操作手册V7.docx]] | [飞书](https://reliablesense.feishu.cn/file/Krurb4Ew6okF4jxUP8BcDru3nUf) | → 提取 | `2-Areas/Work/产品研发/SaaS平台操作手册V7.docx` |
| 快速启用，属于你的任务管理系统.md | [[4-Archives/Notes/Feishu/云空间/根目录/快速启用，属于你的任务管理系统]] | [飞书](https://reliablesense.feishu.cn/docx/X8Y8dLsjZo5wSuxGMu9cc7AAnGf) | 留归档 | - | 飞书模板文档 |
| 研发部的视频会议 2024年11月22日.md | [[4-Archives/Notes/Feishu/云空间/根目录/研发部的视频会议 2024年11月22日]] | [飞书](https://reliablesense.feishu.cn/docx/Vu8Nd0VN1ovfrOxpvDzcHcO5nSf) | → 归档 | `2-Areas/Work/团队管理/早会纪要/2024/11/` | 大部分内容属于洛阳项目 |
| 移动应用 - 监控 2025年5月13日.md | [[4-Archives/Notes/Feishu/云空间/根目录/移动应用 - 监控 2025年5月13日]] | [飞书](https://reliablesense.feishu.cn/docx/GBCkdfZNVor1Lcxgs4AcSIZonMe) | 留归档 | - | 临时监控记录 |
| 翻译.docx | [[4-Archives/Notes/Feishu/云空间/根目录/翻译.docx]] | [飞书](https://reliablesense.feishu.cn/file/FoTYbNSjwoE1trxSOvWce7rxntf) | → 归档 | `4-Archives/Projects/Work/中东电子厂/翻译.docx` | 伊朗项目翻译文件 |
| 认证文件.zip | [[4-Archives/Notes/Feishu/云空间/根目录/认证文件.zip]] | [飞书](https://reliablesense.feishu.cn/file/GCxtbICnZo5X1QxwnzfcMzErnGf) | → 提取 | `2-Areas/Work/综合管理/软著立项/认证文件.zip` | 软著和ISO质量检测认证文件 |
| 综合定位系统-深化设计方案.docx | [[4-Archives/Notes/Feishu/云空间/根目录/综合定位系统-深化设计方案.docx]] | [飞书](https://reliablesense.feishu.cn/file/OVHGbClJOoavkLx3gStcUVGAngh) | → 提取 | `1-Projects/Work/广州机场/综合定位系统-深化设计方案.docx` | 含"综合定位系统"，属广州机场 |
| 14号夜班差异分析.xlsx | [[4-Archives/Notes/Feishu/云空间/根目录/14号夜班差异分析.xlsx]] | [飞书](https://reliablesense.feishu.cn/file/JXLib9uFkoA5F3xWLfxcD2jlnKf) | → 提取 | `1-Projects/Work/新太定位/14号夜班差异分析.xlsx` | 新太定位 |
| 5.20日洛阳石化系统bug问题汇总.xlsx | [[4-Archives/Notes/Feishu/云空间/根目录/5.20日洛阳石化系统bug问题汇总.xlsx]] | [飞书](https://reliablesense.feishu.cn/file/YUCNbnhyMooytWxAZVZcntx4nff) | → 归档 | `1-Projects/Work/洛阳化工厂/5.20日洛阳石化系统bug问题汇总.xlsx` | 洛阳项目 BUG 汇总 |
| MAC-Address.xlsx | [[4-Archives/Notes/Feishu/云空间/根目录/MAC-Address.xlsx]] | [飞书](https://reliablesense.feishu.cn/file/MFjsbb7bBoHIr5xo4v7c95kqnvb) | → 提取 | `2-Areas/Work/设备管理/MAC-Address.xlsx` | 设备 MAC 地址表 |
| 员工花名册-在职.xlsx | [[4-Archives/Notes/Feishu/云空间/根目录/员工花名册-在职.xlsx]] | [飞书](https://reliablesense.feishu.cn/sheets/HQsEseKUKhovu0t1ewnclLSAnte) | → 提取 | `1-Projects/Work/广州机场/员工花名册-在职.xlsx` | 机场导入数据 |
| 周报测试.xlsx | [[4-Archives/Notes/Feishu/云空间/根目录/周报测试.xlsx]] | [飞书](https://reliablesense.feishu.cn/base/NepGb0sWdaPfnosidcMc7yspnFg) | → 提取 | `2-Areas/Work/团队管理/周报提交记录.xlsx` | 周报提交记录 |
| 定位对象在线时长导出表.xlsx | [[4-Archives/Notes/Feishu/云空间/根目录/定位对象在线时长导出表.xlsx]] | [飞书](https://reliablesense.feishu.cn/sheets/W95RsJ1SahTaeJt0xDgcM4d6n7f) | → 提取 | `2-Areas/Work/产品研发/定位对象在线时长导出表.xlsx` |
| 广州市公办小学招生报名系统入学申请表.xls | [[4-Archives/Notes/Feishu/云空间/根目录/广州市公办小学招生报名系统入学申请表.xls]] | [飞书](https://reliablesense.feishu.cn/file/T41fbSI4xoRMTJxtiWkctSUxnvp) | 留归档 | - | 个人文件 |
| 广州机场综合定位.xlsx | [[4-Archives/Notes/Feishu/云空间/根目录/广州机场综合定位.xlsx]] | [飞书](https://reliablesense.feishu.cn/base/NbIPbswwSaCfPpsWak7cbCHsnwe) | → 提取 | `1-Projects/Work/广州机场/广州机场综合定位.xlsx` | 广州机场项目数据 |
| 数字化.xlsx | [[4-Archives/Notes/Feishu/云空间/根目录/数字化.xlsx]] | [飞书](https://reliablesense.feishu.cn/file/E1b4biPmsoA4Ztx5Zj8c7CC0n6q) | → 提取 | `1-Projects/Work/新太定位/数字化措施表.xlsx` | 新太定位数字化改造措施（堆垛、铲车、料坑） |
| 红柳林筛分楼部署内容.xlsx | [[4-Archives/Notes/Feishu/云空间/根目录/红柳林筛分楼部署内容.xlsx]] | [飞书](https://reliablesense.feishu.cn/sheets/shtcnuIgoeyPvXu60pwR4XsEc1g) | → 归档 | `1-Projects/Work/麦钉定位/红柳林筛分楼部署内容.xlsx` | 红柳林项目 |
| 综合定位系统功能清单.xlsx | [[4-Archives/Notes/Feishu/云空间/根目录/综合定位系统功能清单.xlsx]] | [飞书](https://reliablesense.feishu.cn/file/JV2ibGyG9oVohcxlBwJcQdbenJe) | → 提取 | `1-Projects/Work/广州机场/综合定位系统功能清单.xlsx` | 广州机场功能清单 |
| 广州白云国际机场三期扩建项目-综合定位-接口规范-V1.0.2.docx | [[4-Archives/Notes/Feishu/云空间/根目录/广州白云国际机场三期扩建项目-综合定位-接口规范-V1.0.2.docx]] | [飞书](https://reliablesense.feishu.cn/file/UGbJbaqiUoWBJaxH4Hpc9totngd) | → 提取 | `1-Projects/Work/广州机场/接口规范-V1.0.2.docx` | 广州机场接口规范 |
| 智慧仓储物流早会汇报v1.5.pptx | [[4-Archives/Notes/Feishu/云空间/根目录/智慧仓储物流早会汇报v1.5.pptx]] | [飞书](https://reliablesense.feishu.cn/file/QeNlbb8xyoOSVPxfVMgcR8uCnKc) | → 提取 | `1-Projects/Work/新太定位/智慧仓储物流早会汇报v1.5.pptx` | 新太定位汇报 |

> **归类规则补充**：
> - 项目相关的接口/技术文档 → 跟对应项目走（`1-Projects/Work/` 或 `4-Archives/Projects/Work/`），不放通用 Tech 目录
> - 设备协议类文档 → `2-Areas/Work/设备管理/`
> - 产品架构文档（系统架构图、概要设计等描述产品整体的） → `2-Areas/Work/产品研发/`
> - 含"综合定位"、"A域/B域"、"巡检app"等广州机场特征关键词的文档 → `1-Projects/Work/广州机场/`
> - 含"新太"、"料棚"、"新钢联"等关键词的文档 → `1-Projects/Work/新太定位/`
> - 含"红柳林"、"李家壕"、"韩家村"、"高安屯"、"柠条塔"、"madinat_hll"、"madinat_xmc"、"madinat_hjc"、"madinat_gat"、"madinat_ntt" → `1-Projects/Work/麦钉定位/`

---

## 二、云空间/散落的会议纪要和飞书 AI 生成内容

256 个会议纪要文件，根据内容分类后归入对应位置。详细文件列表见 [[1-Projects/Personal/笔记迁移/会议纪要分类结果]]。

### 分类统计

| 分类 | 数量 | 目标路径 |
|------|------|---------|
| 新太定位会议 | 34 | `1-Projects/Work/新太定位/会议纪要/` |
| 广州机场会议 | 26 | `1-Projects/Work/广州机场/会议纪要/` |
| 上港项目会议 | 4 | `1-Projects/Work/上港仓储管理/会议纪要/` |
| 武汉机场会议 | 3 | `4-Archives/Projects/Work/武汉机场/会议纪要/` |
| 洛阳化工厂会议 | 1 | `1-Projects/Work/洛阳化工厂/会议纪要/` |
| 产品研发会议 | 8 | `2-Areas/Work/产品研发/会议纪要/` |
| 研发部早会 | 36 | `2-Areas/Work/团队管理/早会纪要/` |
| 项目部周会 | 18 | `2-Areas/Work/团队管理/周会纪要/项目部/` |
| 项目进度会（刘秉欣） | 35 | `2-Areas/Work/团队管理/周会纪要/` |
| 技术讨论 | 7 | `2-Areas/Work/产品研发/会议纪要/` + `1-Projects/Work/赛峰定位/会议纪要/` + `1-Projects/Work/洛阳化工厂/会议纪要/` |
| 待确认 | 36 | 需人工判断 |
| 留归档（AI 汇总） | 84 | 近期会议速递、月度纪要小结，按所属同事归入团队成员目录 |

### 分类规则

| 会议类型 | 判断依据 |
|---------|---------|
| 新太定位 | 标题/内容含"新太"、"新钢联"、"料棚"、"卸料"、"上料"、"铲车"、"堆垛" |
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

#### 新太定位（34 个）

| 文件 | 本地路径 | 飞书链接 | 目标路径 |
|------|---------|---------|---------|
| 内蒙新太定位（新钢联）的视频会议 2025年2月20日 - 智能纪要.md | [[4-Archives/Notes/Feishu/云空间/内蒙新太定位（新钢联）的视频会议 2025年2月20日 - 智能纪要]] | [飞书](https://reliablesense.feishu.cn/docx/KYotdrd3iovBS6xtsLFcrpl7nOb) | `1-Projects/Work/新太定位/会议纪要/` |
| 文字记录：上料 APP 及卸货问题研讨会  2025年4月10日.md | [[4-Archives/Notes/Feishu/云空间/文字记录：上料 APP 及卸货问题研讨会  2025年4月10日]] | [飞书](https://reliablesense.feishu.cn/docx/Q02Gd51NFov3FlxnOpgcfUe0n2d) | `1-Projects/Work/新太定位/会议纪要/` |
| 文字记录：五人工作安排与系统问题会议 2025年4月8日.md | [[4-Archives/Notes/Feishu/云空间/文字记录：五人工作安排与系统问题会议 2025年4月8日]] | [飞书](https://reliablesense.feishu.cn/docx/DDIddzu4uorHx3xVcmPc8d7Wnih) | `2-Areas/Work/团队管理/早会纪要/2025/04/` |
| 文字记录：内蒙新太定位（新钢联）的视频会议 2025年2月20日.md | [[4-Archives/Notes/Feishu/云空间/文字记录：内蒙新太定位（新钢联）的视频会议 2025年2月20日]] | [飞书](https://reliablesense.feishu.cn/docx/Qdl2dygpBoeSexx0CEzcjhsFnNf) | `1-Projects/Work/新太定位/会议纪要/` |
| 文字记录：内蒙新太定位（新钢联）的视频会议 2025年2月26日.md | [[4-Archives/Notes/Feishu/云空间/文字记录：内蒙新太定位（新钢联）的视频会议 2025年2月26日]] | [飞书](https://reliablesense.feishu.cn/docx/Pt9ydazeCozgTCxOleBcBkWnnzd) | `1-Projects/Work/新太定位/会议纪要/` |
| 文字记录：卸货条件设定及测试问题研讨 2025年4月17日.md | [[4-Archives/Notes/Feishu/云空间/文字记录：卸货条件设定及测试问题研讨 2025年4月17日]] | [飞书](https://reliablesense.feishu.cn/docx/TKuQdMeP9oG3HExLFz3cAFrknje) | `1-Projects/Work/新太定位/会议纪要/` |
| 文字记录：多项工作安排与检查会议  2025年5月8日.md | [[4-Archives/Notes/Feishu/云空间/文字记录：多项工作安排与检查会议  2025年5月8日]] | [飞书](https://reliablesense.feishu.cn/docx/ThZ5dZTgGofFRLxZibRcQm7mnBc) | `1-Projects/Work/新太定位/会议纪要/` |
| 文字记录：导航程序测试问题研讨会 2025年4月10日.md | [[4-Archives/Notes/Feishu/云空间/文字记录：导航程序测试问题研讨会 2025年4月10日]] | [飞书](https://reliablesense.feishu.cn/docx/GLSldDcEWoCwNOxaGlBcB86znwd) | `1-Projects/Work/新太定位/会议纪要/` |
| 文字记录：小程序堆垛定位路线问题会议 2025年4月22日.md | [[4-Archives/Notes/Feishu/云空间/文字记录：小程序堆垛定位路线问题会议 2025年4月22日]] | [飞书](https://reliablesense.feishu.cn/docx/BECFddgmZobgXGxpjZqcnPGRnwf) | `1-Projects/Work/新太定位/会议纪要/` |
| 文字记录：平板使用问题及解决措施研讨 2025年4月7日.md | [[4-Archives/Notes/Feishu/云空间/文字记录：平板使用问题及解决措施研讨 2025年4月7日]] | [飞书](https://reliablesense.feishu.cn/docx/KmwodbUhLokRuAxjmCWce9IHn5d) | `1-Projects/Work/新太定位/会议纪要/` |
| 文字记录：跑步速度与通知次数安排会议  2025年4月10日.md | [[4-Archives/Notes/Feishu/云空间/文字记录：跑步速度与通知次数安排会议  2025年4月10日]] | [飞书](https://reliablesense.feishu.cn/docx/ItNldtWzZolX9NxW28Tcr3tFnVf) | `1-Projects/Work/新太定位/会议纪要/` |
| 文字记录：项目工作进展与规划会议纪要  2025年5月6日.md | [[4-Archives/Notes/Feishu/云空间/文字记录：项目工作进展与规划会议纪要  2025年5月6日]] | [飞书](https://reliablesense.feishu.cn/docx/DsJ3dv1Jwo7jXHxNSyZckJz6nve) | `1-Projects/Work/新太定位/会议纪要/` |
| 智能纪要：上料 APP 及卸货问题研讨会 2025年4月10日.md | [[4-Archives/Notes/Feishu/云空间/智能纪要：上料 APP 及卸货问题研讨会 2025年4月10日]] | [飞书](https://reliablesense.feishu.cn/docx/BgwNddiWwouTVAxTA3wcb982nRh) | `1-Projects/Work/新太定位/会议纪要/` |
| 智能纪要：五人工作安排与系统问题会议 2025年4月8日.md | [[4-Archives/Notes/Feishu/云空间/智能纪要：五人工作安排与系统问题会议 2025年4月8日]] | [飞书](https://reliablesense.feishu.cn/docx/TiYHdhhLMoGcIhxLTEKcT3MKnqe) | `2-Areas/Work/团队管理/早会纪要/2025/04/` |
| 智能纪要：内蒙新太定位（新钢联）的视频会议 2025年2月26日.md | [[4-Archives/Notes/Feishu/云空间/智能纪要：内蒙新太定位（新钢联）的视频会议 2025年2月26日]] | [飞书](https://reliablesense.feishu.cn/docx/ZLRHd5XrUoztV0xtcXucyWZMnrb) | `1-Projects/Work/新太定位/会议纪要/` |
| 智能纪要：卸货条件设定及测试问题研讨 2025年4月17日.md | [[4-Archives/Notes/Feishu/云空间/智能纪要：卸货条件设定及测试问题研讨 2025年4月17日]] | [飞书](https://reliablesense.feishu.cn/docx/UHRbdu9XLoa9PUxi2szcKHAinPb) | `1-Projects/Work/新太定位/会议纪要/` |
| 智能纪要：多项工作安排与检查会议 2025年5月8日.md | [[4-Archives/Notes/Feishu/云空间/智能纪要：多项工作安排与检查会议 2025年5月8日]] | [飞书](https://reliablesense.feishu.cn/docx/AawEdXIyAo7h2XxcMoUcWvGbnBc) | `1-Projects/Work/新太定位/会议纪要/` |
| 智能纪要：导航程序测试问题研讨会 2025年4月10日.md | [[4-Archives/Notes/Feishu/云空间/智能纪要：导航程序测试问题研讨会 2025年4月10日]] | [飞书](https://reliablesense.feishu.cn/docx/SMRPdLb1soQz30xhdILcFV0Cnnc) | `1-Projects/Work/新太定位/会议纪要/` |
| 智能纪要：小程序堆垛定位路线问题会议 2025年4月22日.md | [[4-Archives/Notes/Feishu/云空间/智能纪要：小程序堆垛定位路线问题会议 2025年4月22日]] | [飞书](https://reliablesense.feishu.cn/docx/MyVSdaYrtoz7GdxuRcGce2k7nyc) | `1-Projects/Work/新太定位/会议纪要/` |
| 智能纪要：平板使用问题及解决措施研讨 2025年4月7日.md | [[4-Archives/Notes/Feishu/云空间/智能纪要：平板使用问题及解决措施研讨 2025年4月7日]] | [飞书](https://reliablesense.feishu.cn/docx/RGhodDXbEo2X70xK8WLcGZEOnXd) | `1-Projects/Work/新太定位/会议纪要/` |
| 智能纪要：跑步速度与通知次数安排会议 2025年4月10日.md | [[4-Archives/Notes/Feishu/云空间/智能纪要：跑步速度与通知次数安排会议 2025年4月10日]] | [飞书](https://reliablesense.feishu.cn/docx/PZyHddVcpoJOndxfhdscRdC5npe) | `1-Projects/Work/新太定位/会议纪要/` |
| 智能纪要：项目工作进展与规划会议纪要 2025年5月6日.md | [[4-Archives/Notes/Feishu/云空间/智能纪要：项目工作进展与规划会议纪要 2025年5月6日]] | [飞书](https://reliablesense.feishu.cn/docx/BosQdhobYolHEFxRpWdcMbMgnYd) | `1-Projects/Work/新太定位/会议纪要/` |
| 文字记录：内蒙新太定位（新钢联）的视频会议 2025年2月26日.md | [[4-Archives/Notes/Feishu/云空间/王宗光的个人文档/文字记录：内蒙新太定位（新钢联）的视频会议 2025年2月26日]] | [飞书](https://reliablesense.feishu.cn/docx/OgG5dQrQLoGY9FxEchhcSvmknXg) | `1-Projects/Work/新太定位/会议纪要/` |
| 文字记录：内蒙新太定位（新钢联）的视频会议 2025年3月5日.md | [[4-Archives/Notes/Feishu/云空间/王宗光的个人文档/文字记录：内蒙新太定位（新钢联）的视频会议 2025年3月5日]] | [飞书](https://reliablesense.feishu.cn/docx/D0aEdYFlYo9REkxhIrwcDDWCnPf) | `1-Projects/Work/新太定位/会议纪要/` |
| 文字记录：王宗光的视频会议 2025年2月20日.md | [[4-Archives/Notes/Feishu/云空间/王宗光的个人文档/文字记录：王宗光的视频会议 2025年2月20日]] | [飞书](https://reliablesense.feishu.cn/docx/DGyzdAmKkoykTYxVkoxcduRcnCc) | `2-Areas/Work/产品研发/会议纪要/` |
| 文字记录：项目服务、权限及工作进展会议 2025年4月11日.md | [[4-Archives/Notes/Feishu/云空间/王宗光的个人文档/文字记录：项目服务、权限及工作进展会议 2025年4月11日]] | [飞书](https://reliablesense.feishu.cn/docx/KoC5dKi6koHwTfx8Dkbcgrlon5g) | `1-Projects/Work/洛阳化工厂/会议纪要/` |
| 智能纪要：内蒙新太定位（新钢联）的视频会议 2025年2月26日.md | [[4-Archives/Notes/Feishu/云空间/王宗光的个人文档/智能纪要：内蒙新太定位（新钢联）的视频会议 2025年2月26日]] | [飞书](https://reliablesense.feishu.cn/docx/IQUqdVOipoy6MUx9pYicAUvrnmd) | `1-Projects/Work/新太定位/会议纪要/` |
| 智能纪要：内蒙新太定位（新钢联）的视频会议 2025年3月5日.md | [[4-Archives/Notes/Feishu/云空间/王宗光的个人文档/智能纪要：内蒙新太定位（新钢联）的视频会议 2025年3月5日]] | [飞书](https://reliablesense.feishu.cn/docx/EePFdqlyQoh4bExphrXcGX3Wnjd) | `1-Projects/Work/新太定位/会议纪要/` |
| 智能纪要：多方面业务问题及解决方案探讨会 2025年6月3日.md | [[4-Archives/Notes/Feishu/云空间/王宗光的个人文档/智能纪要：多方面业务问题及解决方案探讨会 2025年6月3日]] | [飞书](https://reliablesense.feishu.cn/docx/NPkFdqGfUo1Bf2xEQOGclc7anMh) | `1-Projects/Work/洛阳化工厂/会议纪要/` |
| 智能纪要：项目服务、权限及工作进展会议 2025年4月11日.md | [[4-Archives/Notes/Feishu/云空间/王宗光的个人文档/智能纪要：项目服务、权限及工作进展会议 2025年4月11日]] | [飞书](https://reliablesense.feishu.cn/docx/LKSodmV6loX04TxtDTNcEqmcnLe) | `1-Projects/Work/新太定位/会议纪要/` |
| 王宗光的视频会议 2025年2月20日 - 智能纪要.md | [[4-Archives/Notes/Feishu/云空间/王宗光的个人文档/王宗光的视频会议 2025年2月20日 - 智能纪要]] | [飞书](https://reliablesense.feishu.cn/docx/Rr23dKQ8vo2vyYxmepgcq5ktn1c) | `2-Areas/Work/产品研发/会议纪要/` |
| 内蒙新太定位（新钢联）的视频会议 2025年2月7日 - 智能纪要.md | [[4-Archives/Notes/Feishu/云空间/陈子杰的个人文档/内蒙新太定位（新钢联）的视频会议 2025年2月7日 - 智能纪要]] | [飞书](https://reliablesense.feishu.cn/docx/W7Jid5OiUopoqcxNqJbc8ichnnf) | `1-Projects/Work/新太定位/会议纪要/` |
| 文字记录：陈子杰的视频会议 2025年2月24日.md | [[4-Archives/Notes/Feishu/云空间/陈子杰的个人文档/文字记录：陈子杰的视频会议 2025年2月24日]] | [飞书](https://reliablesense.feishu.cn/docx/JhwjdqDfJoBMExxV9btciKO3nhf) | `1-Projects/Work/新太定位/会议纪要/` |
| 智能纪要：陈子杰的视频会议 2025年2月24日.md | [[4-Archives/Notes/Feishu/云空间/陈子杰的个人文档/智能纪要：陈子杰的视频会议 2025年2月24日]] | [飞书](https://reliablesense.feishu.cn/docx/XVxUdVtaSo0wu6xtY3Uc7GdHnrc) | `1-Projects/Work/新太定位/会议纪要/` |

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
| 文字记录：申库、测试及登录存货问题讨论 2025年9月17日.md | [[4-Archives/Notes/Feishu/云空间/王宗光的个人文档/文字记录：申库、测试及登录存货问题讨论 2025年9月17日]] | [飞书](https://reliablesense.feishu.cn/docx/NrtBdN4sQo4P0cxB0RJc21Ebnse) | `1-Projects/Work/广州机场/会议纪要/` |
| 智能纪要：刷新配置规则变更讨论会议 2025年9月25日.md | [[4-Archives/Notes/Feishu/云空间/王宗光的个人文档/智能纪要：刷新配置规则变更讨论会议 2025年9月25日]] | [飞书](https://reliablesense.feishu.cn/docx/XHG9dLsmDoBkJxx4bkJcIABInbD) | `1-Projects/Work/上港仓储管理/会议纪要/` |
| 智能纪要：申库、测试及登录存货问题讨论 2025年9月17日.md | [[4-Archives/Notes/Feishu/云空间/王宗光的个人文档/智能纪要：申库、测试及登录存货问题讨论 2025年9月17日]] | [飞书](https://reliablesense.feishu.cn/docx/HNAVdtRgzo4xLFxUjO0c3qi9nJc) | `1-Projects/Work/广州机场/会议纪要/` |

#### 武汉机场（3 个）

| 文件 | 本地路径 | 飞书链接 | 目标路径 |
|------|---------|---------|---------|
| 文字记录：数据修改、卡顿及操作异常讨论 2026年3月12日.md | [[4-Archives/Notes/Feishu/云空间/文字记录：数据修改、卡顿及操作异常讨论 2026年3月12日]] | [飞书](https://reliablesense.feishu.cn/docx/CJYtdjil1o4AVaxvtgbch27ZnAh) | `1-Projects/Work/广州机场/会议纪要/` |
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
| 文字记录：launchable查询及告警管理问题讨论 2026年3月12日.md | [[4-Archives/Notes/Feishu/云空间/文字记录：launchable查询及告警管理问题讨论 2026年3月12日]] | [飞书](https://reliablesense.feishu.cn/docx/ZUWmdKM1yogZNuxSWYocJO3ynpg) | → 提取 | `2-Areas/Work/产品研发/会议纪要/` |
| 文字记录：代码修改：Beacon与网关定位差异 2026年3月11日.md | [[4-Archives/Notes/Feishu/云空间/文字记录：代码修改：Beacon与网关定位差异 2026年3月11日]] | [飞书](https://reliablesense.feishu.cn/docx/NoSpdy20moXWLWxGp0hcjFa2n3f) | → 提取 | `2-Areas/Work/产品研发/会议纪要/` |
| 智能纪要：launchable查询及告警管理问题讨论 2026年3月12日.md | [[4-Archives/Notes/Feishu/云空间/智能纪要：launchable查询及告警管理问题讨论 2026年3月12日]] | [飞书](https://reliablesense.feishu.cn/docx/PZD8dz0C6ouiH6xY4HVc1GJjnGh) | → 提取 | `2-Areas/Work/产品研发/会议纪要/` |
| 智能纪要：代码修改：Beacon与网关定位差异 2026年3月11日.md | [[4-Archives/Notes/Feishu/云空间/智能纪要：代码修改：Beacon与网关定位差异 2026年3月11日]] | [飞书](https://reliablesense.feishu.cn/docx/EGwqdnH6voVInSxT8eicfj7znPf) | → 提取 | `2-Areas/Work/产品研发/会议纪要/` |
| 文字记录：办公室 CLE 数据配置及墨水屏问题会议 2025年8月19日.md | [[4-Archives/Notes/Feishu/云空间/王宗光的个人文档/文字记录：办公室 CLE 数据配置及墨水屏问题会议 2025年8月19日]] | [飞书](https://reliablesense.feishu.cn/docx/QG3ld8j2joWsEDxVOFocVLrAnOg) | → 提取 | `1-Projects/Work/赛峰定位/会议纪要/` |
| 文字记录：平台重启及相关技术问题研讨 2025年5月31日.md | [[4-Archives/Notes/Feishu/云空间/王宗光的个人文档/文字记录：平台重启及相关技术问题研讨 2025年5月31日]] | [飞书](https://reliablesense.feishu.cn/docx/LRjhdZLUeoMIyKxAoIyciR1qneg) | → 归档 | `1-Projects/Work/洛阳化工厂/会议纪要/` |
| 智能纪要：办公室 CLE 数据配置及墨水屏问题会议 2025年8月19日.md | [[4-Archives/Notes/Feishu/云空间/王宗光的个人文档/智能纪要：办公室 CLE 数据配置及墨水屏问题会议 2025年8月19日]] | [飞书](https://reliablesense.feishu.cn/docx/XAwMd4UStoorpRxKG3scYBLbnQe) | → 提取 | `1-Projects/Work/赛峰定位/会议纪要/` |

#### 产品研发（8 个）

| 文件 | 本地路径 | 飞书链接 | 目标路径 |
|------|---------|---------|---------|
| 文字记录：会议研讨多项工作进展情况 2026年3月11日.md | [[4-Archives/Notes/Feishu/云空间/文字记录：会议研讨多项工作进展情况 2026年3月11日]] | [飞书](https://reliablesense.feishu.cn/docx/ZEhLdBtR3oEQXnxHFezcWf3qnsb) | `2-Areas/Work/产品研发/会议纪要/` |
| 文字记录：接口、登录及缓存相关问题研讨 2025年4月14日.md | [[4-Archives/Notes/Feishu/云空间/文字记录：接口、登录及缓存相关问题研讨 2025年4月14日]] | [飞书](https://reliablesense.feishu.cn/docx/WX92d2s8aom3SixuxG8cVUyGnMc) | `2-Areas/Work/产品研发/会议纪要/` |
| 智能纪要：会议研讨多项工作进展情况 2026年3月11日.md | [[4-Archives/Notes/Feishu/云空间/智能纪要：会议研讨多项工作进展情况 2026年3月11日]] | [飞书](https://reliablesense.feishu.cn/docx/ZlJrd2jI2og5rAxI38LcMaWxnfd) | `2-Areas/Work/产品研发/会议纪要/` |
| 智能纪要：接口、登录及缓存相关问题研讨 2025年4月14日.md | [[4-Archives/Notes/Feishu/云空间/智能纪要：接口、登录及缓存相关问题研讨 2025年4月14日]] | [飞书](https://reliablesense.feishu.cn/docx/BwYtdGuyxov5I2xi2XJcsfULnef) | `2-Areas/Work/产品研发/会议纪要/` |
| 智能纪要：数据修改、卡顿及操作异常讨论 2026年3月12日.md | [[4-Archives/Notes/Feishu/云空间/智能纪要：数据修改、卡顿及操作异常讨论 2026年3月12日]] | [飞书](https://reliablesense.feishu.cn/docx/QrfYdgZQloxUTMxVcLOcaSvDnNo) | `1-Projects/Work/广州机场/会议纪要/` |
| 文字记录：多方面业务问题及解决方案探讨会 2025年6月3日.md | [[4-Archives/Notes/Feishu/云空间/王宗光的个人文档/文字记录：多方面业务问题及解决方案探讨会 2025年6月3日]] | [飞书](https://reliablesense.feishu.cn/docx/Jtm6dfrULo7SNYxWZZ9cwLULnvd) | `1-Projects/Work/洛阳化工厂/会议纪要/` |
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
| 内蒙新太定位（新钢联）的视频会议 2025年2月7日 - 智能纪要.md | [[4-Archives/Notes/Feishu/云空间/陈子杰的个人文档/内蒙新太定位（新钢联）的视频会议 2025年2月7日 - 智能纪要]] | [飞书](https://reliablesense.feishu.cn/docx/W7Jid5OiUopoqcxNqJbc8ichnnf) | 新太定位 | `1-Projects/Work/新太定位/` |
| 室内定位系统工作进度.xlsx | [[4-Archives/Notes/Feishu/云空间/陈子杰的个人文档/室内定位系统工作进度.xlsx]] | [飞书](https://reliablesense.feishu.cn/sheets/Xl6HsOeCMhUrDwtMewMcElDGnyd) | 留归档 | - | 历史进度 |
| 文字记录：上海东海模型修复及接入方案研讨 2025年5月15日.md | [[4-Archives/Notes/Feishu/云空间/陈子杰的个人文档/文字记录：上海东海模型修复及接入方案研讨 2025年5月15日]] | [飞书](https://reliablesense.feishu.cn/docx/Ky4Ldt5hFoe6mQxg8lrctpCRngh) | → 提取 | `2-Areas/Work/产品研发/会议纪要/`  |
| 文字记录：数据、页面状态及功能处理会议 2025年9月17日.md | [[4-Archives/Notes/Feishu/云空间/陈子杰的个人文档/文字记录：数据、页面状态及功能处理会议 2025年9月17日]] | [飞书](https://reliablesense.feishu.cn/docx/O7UVdlfMSoMkZbxVyWic5N0bnBf) | → 提取 | `2-Areas/Work/产品研发/会议纪要/`  |
| 文字记录：移动应用与 TCDM 会议讨论  2025年6月3日.md | [[4-Archives/Notes/Feishu/云空间/陈子杰的个人文档/文字记录：移动应用与 TCDM 会议讨论  2025年6月3日]] | [飞书](https://reliablesense.feishu.cn/docx/JmwhduJIPouIxsx7Sh6cH5ZOnph) | 广州机场 | `1-Projects/Work/广州机场/` |
| 文字记录：陈子杰的视频会议 2025年2月24日.md | [[4-Archives/Notes/Feishu/云空间/陈子杰的个人文档/文字记录：陈子杰的视频会议 2025年2月24日]] | [飞书](https://reliablesense.feishu.cn/docx/JhwjdqDfJoBMExxV9btciKO3nhf) | → 提取 | `1-Projects/Work/新太定位/会议纪要/`  |
| 文字记录：黄佳琪软件工作安排及指导会议 2025年4月11日.md | [[4-Archives/Notes/Feishu/云空间/陈子杰的个人文档/文字记录：黄佳琪软件工作安排及指导会议 2025年4月11日]] | [飞书](https://reliablesense.feishu.cn/docx/MWlJdSwz6o30ykxZGMPcLmdin0f) | → 提取 | `1-Projects/Work/广州机场/会议纪要/`  |
| 智能纪要：上海东海模型修复及接入方案研讨 2025年5月15日.md | [[4-Archives/Notes/Feishu/云空间/陈子杰的个人文档/智能纪要：上海东海模型修复及接入方案研讨 2025年5月15日]] | [飞书](https://reliablesense.feishu.cn/docx/BT99d8bucoUruTx4rvZcYbRbnff) | → 提取 | `2-Areas/Work/产品研发/会议纪要/`  |
| 智能纪要：数据、页面状态及功能处理会议 2025年9月17日.md | [[4-Archives/Notes/Feishu/云空间/陈子杰的个人文档/智能纪要：数据、页面状态及功能处理会议 2025年9月17日]] | [飞书](https://reliablesense.feishu.cn/docx/KliDdAtzionSN1xuPXic7YWynUd) | → 提取 | `2-Areas/Work/产品研发/会议纪要/`  |
| 智能纪要：移动应用与 TCDM 会议讨论 2025年6月3日.md | [[4-Archives/Notes/Feishu/云空间/陈子杰的个人文档/智能纪要：移动应用与 TCDM 会议讨论 2025年6月3日]] | [飞书](https://reliablesense.feishu.cn/docx/VARrddtC3oOlFMxENAFcoGBKnl9) | 广州机场 | `1-Projects/Work/广州机场/` |
| 智能纪要：陈子杰的视频会议 2025年2月24日.md | [[4-Archives/Notes/Feishu/云空间/陈子杰的个人文档/智能纪要：陈子杰的视频会议 2025年2月24日]] | [飞书](https://reliablesense.feishu.cn/docx/XVxUdVtaSo0wu6xtY3Uc7GdHnrc) | → 提取 | `1-Projects/Work/新太定位/会议纪要/`  |
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
| 问题记录-2023-09-22.xlsx | [[4-Archives/Notes/Feishu/云空间/陈子杰的个人文档/问题记录-2023-09-22.xlsx]] | [飞书](https://reliablesense.feishu.cn/sheets/ILedsU7eShMXojtZmy0cTiHln9c) | → 归档 | `4-Archives/Projects/Work/武汉机场/` | 武汉机场问题记录 |
| 需求及 Bug 管理.xlsx | [[4-Archives/Notes/Feishu/云空间/陈子杰的个人文档/需求及 Bug 管理.xlsx]] | [飞书](https://reliablesense.feishu.cn/base/BSDnb80vUaGm4hsjM06cIE0bncD) | → 提取 | `4-Archives/Areas/Work/团队管理/团队成员/陈子杰/` | 需求和 Bug 管理 |
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
| SaaS使用手册V4 new 英文.docx | [[4-Archives/Notes/Feishu/云空间/孙永霖的个人文档/doc/SaaS使用手册V4 new 英文.docx]] | [飞书](https://reliablesense.feishu.cn/file/boxcnrTNYMWwqMq49WzzapEj30g) | → 提取 | `2-Areas/Work/产品研发/SaaS使用手册V4-英文.docx` |
| SaaS使用手册V4 new.docx | [[4-Archives/Notes/Feishu/云空间/孙永霖的个人文档/doc/SaaS使用手册V4 new.docx]] | [飞书](https://reliablesense.feishu.cn/file/boxcnKrzYX5prPEiZIv33AL6mlc) | → 提取 | `2-Areas/Work/产品研发/SaaS使用手册V4.docx` |
| saas英文版.md | [[4-Archives/Notes/Feishu/云空间/孙永霖的个人文档/doc/saas英文版]] | [飞书](https://reliablesense.feishu.cn/docx/LZgYdpRnzouGpKxnOdZc4vDRnPg) | → 提取 | `2-Areas/Work/产品研发/saas英文版.md` |
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
| 新太运维手册.md | [[4-Archives/Notes/Feishu/云空间/莱讯科技/项目资料管理/998. 售后项目/内蒙新太元铬业/新太运维手册]] | [飞书](https://reliablesense.feishu.cn/docx/NFOVdlWSFoZJ91xTXMbcvY7mnSg) | → 提取 | `1-Projects/Work/新太定位/新太运维手册.md` | 新太定位专用运维手册 |
| 区域功能后端开发文档.md | [[4-Archives/Notes/Feishu/云空间/莱讯科技/项目运维管理/运维文档/区域功能后端开发文档]] | [飞书](https://reliablesense.feishu.cn/docx/JknBdu9hEon9gJxuC4ycEBhOnjb) | → 提取 | `2-Areas/Work/产品研发/区域功能后端开发文档.md` |
| 数据库操作说明.md | [[4-Archives/Notes/Feishu/云空间/莱讯科技/项目运维管理/运维文档/数据库操作说明]] | [飞书](https://reliablesense.feishu.cn/docx/KjS8dWiAvoxdCIxgkEEcDktinSU) | → 提取 | `2-Areas/Work/运维管理/数据库操作说明.md` |
| 数据库 pg-backup 使用方法说明.md | [[4-Archives/Notes/Feishu/云空间/莱讯科技/项目运维管理/运维文档/数据库 pg-backup 使用方法说明]] | [飞书](https://reliablesense.feishu.cn/docx/LfEodRSmnoOopsxju9kckxCtnng) | → 提取 | `2-Areas/Work/运维管理/pg-backup使用方法.md` |
| 综合定位系统运维白皮书.md | [[4-Archives/Notes/Feishu/云空间/莱讯科技/项目资料管理/004. 广州机场-综合定位/运维白皮书/综合定位系统运维白皮书]] | [飞书](https://reliablesense.feishu.cn/docx/AMuadobIrozdlZxG96gcHgtPnxe) | → 提取 | `1-Projects/Work/广州机场/综合定位系统运维白皮书.md` | 广州机场运维白皮书 |
| 综合定位系统运维白皮书编写内容框架.md | [[4-Archives/Notes/Feishu/云空间/莱讯科技/项目资料管理/004. 广州机场-综合定位/运维白皮书/综合定位系统运维白皮书编写内容框架]] | [飞书](https://reliablesense.feishu.cn/docx/GkcQdk58kocgF7x6ytNc4ikYnvg) | → 提取 | `1-Projects/Work/广州机场/综合定位系统运维白皮书编写内容框架.md` | 广州机场 |
| 移动应用平台运维白皮书编写内容框架.md | [[4-Archives/Notes/Feishu/云空间/莱讯科技/项目资料管理/005. 广州机场-移动应用平台/运维白皮书/移动应用平台运维白皮书编写内容框架]] | [飞书](https://reliablesense.feishu.cn/docx/AhnkdGgzroBd8Cx9KxDctcGjnAg) | → 提取 | `1-Projects/Work/广州机场/移动应用平台运维白皮书编写内容框架.md` | 广州机场 |
| 综合定位系统进程清单编写内容框架.md | [[4-Archives/Notes/Feishu/云空间/莱讯科技/项目资料管理/004. 广州机场-综合定位/运维白皮书/综合定位系统进程清单编写内容框架]] | [飞书](https://reliablesense.feishu.cn/docx/NibpdCR4coY77ex8qIrcRo7Dnjh) | → 提取 | `1-Projects/Work/广州机场/综合定位系统进程清单编写内容框架.md` | 广州机场 |
| 综合定位系统配置清单编写内容框架.md | [[4-Archives/Notes/Feishu/云空间/莱讯科技/项目资料管理/004. 广州机场-综合定位/运维白皮书/综合定位系统配置清单编写内容框架]] | [飞书](https://reliablesense.feishu.cn/docx/JUInd4Gmwo2B29xizZQcJtq0nKe) | → 提取 | `1-Projects/Work/广州机场/综合定位系统配置清单编写内容框架.md` | 广州机场 |
| 移动应用平台进程清单编写内容框架.md | [[4-Archives/Notes/Feishu/云空间/莱讯科技/项目资料管理/005. 广州机场-移动应用平台/运维白皮书/移动应用平台进程清单编写内容框架]] | [飞书](https://reliablesense.feishu.cn/docx/YCvydrOqHodVj8xC28EcVVMEnRf) | → 提取 | `1-Projects/Work/广州机场/移动应用平台进程清单编写内容框架.md` | 广州机场 |
| 移动应用平台配置清单编写内容框架.md | [[4-Archives/Notes/Feishu/云空间/莱讯科技/项目资料管理/005. 广州机场-移动应用平台/运维白皮书/移动应用平台配置清单编写内容框架]] | [飞书](https://reliablesense.feishu.cn/docx/Z5SFdZURjogTZ8xsMf0c5g6enos) | → 提取 | `1-Projects/Work/广州机场/移动应用平台配置清单编写内容框架.md` | 广州机场 |
| 数据库字典注释.xlsx | [[4-Archives/Notes/Feishu/云空间/莱讯科技/项目运维管理/运维文档/数据库字典注释.xlsx]] | [飞书](https://reliablesense.feishu.cn/base/WOpRbugDgamNOKsHG7scmCGSnZg) | → 提取 | `2-Areas/Work/产品研发/数据库字典注释.xlsx` | 产品数据库字典 |

### 4b. 升级文档

| 文件 | 本地路径 | 飞书链接 | 决策 | 目标路径 |
|------|---------|---------|------|---------|
| 升级文档--20260126.md | [[4-Archives/Notes/Feishu/云空间/莱讯科技/项目运维管理/升级文档/麦钉备份/升级文档--20260126]] | [飞书](https://reliablesense.feishu.cn/docx/YNlKdlNzMogEq3xSsrscEDcQnqg) | → 提取 | `1-Projects/Work/麦钉定位/升级文档-最新版.md` |
| 导航服务器更新文档.md | [[4-Archives/Notes/Feishu/云空间/莱讯科技/项目资料管理/998. 售后项目/百度-水厂定位导航平台/导航服务器更新文档]] | [飞书](https://reliablesense.feishu.cn/docx/N9DWdU324oivVsxpVVIcTh9rnyb) | → 归档 | `4-Archives/Projects/Work/百度水厂/导航服务器更新文档.md` |
| 导航服务器重启文档.md | [[4-Archives/Notes/Feishu/云空间/莱讯科技/项目资料管理/998. 售后项目/百度-水厂定位导航平台/导航服务器重启文档]] | [飞书](https://reliablesense.feishu.cn/docx/G4AWd9nxLoweeJxa0JxcNhQGn5b) | → 归档 | `4-Archives/Projects/Work/百度水厂/导航服务器重启文档.md` |
| 2.5升级文档.md | [[4-Archives/Notes/Feishu/云空间/莱讯科技/项目运维管理/升级文档/2.5升级文档]] | [飞书](https://reliablesense.feishu.cn/docx/K2X3di1MWo7vymxykJecGQoZnFb) | → 提取 | `2-Areas/Work/运维管理/平台2.5升级文档.md` |
| 2.4升级版本流程.md | [[4-Archives/Notes/Feishu/云空间/莱讯科技/项目运维管理/升级文档/2.4升级版本流程]] | [飞书](https://reliablesense.feishu.cn/docx/YtbEdiE8boGjbyxtPK3cB3tXnmg) | → 提取 | `2-Areas/Work/运维管理/平台2.4升级版本流程.md` |

### 4c. 交付文档

| 文件 | 本地路径 | 飞书链接 | 决策 | 目标路径 |
|------|---------|---------|------|---------|
| 部署手册.md | [[4-Archives/Notes/Feishu/云空间/莱讯科技/项目资料管理/998. 售后项目/百度-水厂定位导航平台/项目文档/部署手册]] | [飞书](https://reliablesense.feishu.cn/docs/JI8zdWTaSocj3pxJP2ecSyd4nok) | → 归档 | `4-Archives/Projects/Work/百度水厂/部署手册.md` |
| 部署文档离线版.md | [[4-Archives/Notes/Feishu/云空间/莱讯科技/项目运维管理/交付文档/部署文档离线版]] | [飞书](https://reliablesense.feishu.cn/docx/LsHXdLWbmogiEKxZtK5c229nnad) | → 提取 | `2-Areas/Work/运维管理/部署文档-离线版.md` |
| 私有化部署数据库生成步骤.md | [[4-Archives/Notes/Feishu/云空间/莱讯科技/项目运维管理/交付文档/私有化部署数据库生成步骤]] | [飞书](https://reliablesense.feishu.cn/docx/ArEWdDLrCoeAMpxJV7tc2YC7ntb) | → 提取 | `2-Areas/Work/运维管理/私有化部署-数据库生成步骤.md` |
| 地图交付标准.md | [[4-Archives/Notes/Feishu/云空间/莱讯科技/项目运维管理/交付文档/地图交付标准]] | [飞书](https://reliablesense.feishu.cn/docx/CHvwd4VPboHEtpxyhsWcP7PonPe) | → 提取 | `2-Areas/Work/运维管理/地图交付标准.md` |
| 交接文档.md | [[4-Archives/Notes/Feishu/云空间/王宗光的个人文档/交接文档/交接文档]] | [飞书](https://reliablesense.feishu.cn/docx/UOvmd7dz4oFkXVxuq3OczvtrnHf) | → 提取 | `4-Archives/Areas/Work/团队管理/团队成员/王宗光/交接文档.md` |
| 中间件实施标准化文档.md | [[4-Archives/Notes/Feishu/云空间/莱讯科技/项目运维管理/运维文档/中间件实施标准化文档]] | [飞书](https://reliablesense.feishu.cn/docx/CmG7d0TpIo93M8xpgWucRUSKnYb) | → 提取 | `2-Areas/Work/运维管理/中间件实施标准化文档.md` |
| 现场测试实施标准化文档.md | [[4-Archives/Notes/Feishu/云空间/莱讯科技/项目运维管理/运维文档/现场测试实施标准化文档]] | [飞书](https://reliablesense.feishu.cn/docx/Xsj8dUH5IoKCRuxYRL8ceVTOnKh) | → 提取 | `2-Areas/Work/运维管理/现场测试实施标准化文档.md` |
| 无动力设备管理系统部署指南.md | [[4-Archives/Notes/Feishu/云空间/莱讯科技/项目运维管理/交付文档/无动力设备管理系统部署指南]] | [飞书](https://reliablesense.feishu.cn/docx/NsKCdYwf3okiEPxw0yScBOeGnNh) | 留归档 | - |
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
| 系统容灾备份方案.md | [[4-Archives/Notes/Feishu/云空间/莱讯科技/项目运维管理/售后文档/系统容灾备份方案]] | [飞书](https://reliablesense.feishu.cn/docx/Na7YdwtkYosbSJxCZyPcMmSlnCe) | → 提取 | `2-Areas/Work/运维管理/系统容灾备份方案.md` |
| 定位平台配置建议.md | [[4-Archives/Notes/Feishu/云空间/莱讯科技/项目运维管理/售后文档/定位平台配置建议]] | [飞书](https://reliablesense.feishu.cn/docx/CAsBdlwMnoWeSvx5IuLciDNrnYF) | 留归档 | 旧版本，被 v2 覆盖 |
| 定位平台配置建议-待完善.md | [[4-Archives/Notes/Feishu/云空间/莱讯科技/项目运维管理/售后文档/定位平台配置建议-待完善]] | [飞书](https://reliablesense.feishu.cn/docx/INAndBfILo5yuMxTmi6cWSOynY7) | 留归档 | 草稿版 |
| 系统容灾备份的方案.md | [[4-Archives/Notes/Feishu/云空间/莱讯科技/项目运维管理/售后文档/系统容灾备份的方案]] | [飞书](https://reliablesense.feishu.cn/docx/Na7YdwtkYosbSJxCZyPcMmSlnCe) | 留归档 | 与上面重复 |
| 系统整改配置表.md | [[4-Archives/Notes/Feishu/云空间/莱讯科技/项目运维管理/售后文档/系统整改配置表]] | [飞书](https://reliablesense.feishu.cn/docx/ZpsNdChggodbeaxLg78cgtRBnGc) | 留归档 | 根目录已有同文件 |
| SOW文件.md | [[4-Archives/Notes/Feishu/云空间/莱讯科技/项目运维管理/售后文档/SOW文件]] | [飞书](https://reliablesense.feishu.cn/docx/JeSsdPfEaoy9exxBeD9cBP0pn8M) | → 提取 | `2-Areas/Work/业务管理/SOW文件模板.md` | 项目 SOW 模板 |

### 4e. 集群资料

所有 `*集群.md` 文件（约 20 个）→ 提取到 `2-Areas/Work/运维管理/环境配置/` 下按名称。

| 文件 | 本地路径 | 飞书链接 | 决策 | 目标路径 | 对应项目 |
|------|---------|---------|------|---------|---------|
| cnnc_qshdz集群.md | [[4-Archives/Notes/Feishu/云空间/莱讯科技/项目运维管理/集群资料/cnnc_qshdz集群]] | [飞书](https://reliablesense.feishu.cn/docx/MKTNd2yCQoXoGqxc7ylcO5DcnOd) | → 提取 | `2-Areas/Work/运维管理/环境配置/` | 中联核信 |
| madinat_gat集群.md | [[4-Archives/Notes/Feishu/云空间/莱讯科技/项目运维管理/集群资料/madinat_gat集群]] | [飞书](https://reliablesense.feishu.cn/docx/N7gMdz5ukoIv1Bxj38bcBobInCc) | → 提取 | `2-Areas/Work/运维管理/环境配置/` | 麦钉定位（高安屯） |
| madinat_hjc集群.md | [[4-Archives/Notes/Feishu/云空间/莱讯科技/项目运维管理/集群资料/madinat_hjc集群]] | [飞书](https://reliablesense.feishu.cn/docs/doccn6POZJyaWmcGGsWDbuyGARb) | → 提取 | `2-Areas/Work/运维管理/环境配置/` | 麦钉定位（韩家村） |
| madinat_hll集群.md | [[4-Archives/Notes/Feishu/云空间/莱讯科技/项目运维管理/集群资料/madinat_hll集群]] | [飞书](https://reliablesense.feishu.cn/docx/JdWOdanhvo8Yl8xAs9pc4xWGnI9) | → 提取 | `2-Areas/Work/运维管理/环境配置/` | 麦钉定位（红柳林） |
| madinat_xmc集群.md | [[4-Archives/Notes/Feishu/云空间/莱讯科技/项目运维管理/集群资料/madinat_xmc集群]] | [飞书](https://reliablesense.feishu.cn/docs/doccnRbr2ps3Rpla22Se3M7vnFc) | → 提取 | `2-Areas/Work/运维管理/环境配置/` | 麦钉定位（柠条塔） |
| madinat_sewd集群.md | [[4-Archives/Notes/Feishu/云空间/莱讯科技/项目运维管理/集群资料/madinat_sewd集群]] | [飞书](https://reliablesense.feishu.cn/docx/SGYudVlmgoEJ0ixNyuhcC94rncf) | → 提取 | `2-Areas/Work/运维管理/环境配置/` | 麦钉定位 |
| madinat_ntt集群.md | [[4-Archives/Notes/Feishu/云空间/莱讯科技/项目运维管理/集群资料/madinat_ntt集群]] | [飞书](https://reliablesense.feishu.cn/docx/GmiydvdkdotNEWxPntpcFGXZnmd) | → 提取 | `2-Areas/Work/运维管理/环境配置/` | 麦钉定位 |
| madinat_lyrydw集群.md | [[4-Archives/Notes/Feishu/云空间/莱讯科技/项目运维管理/集群资料/私有化部署/madinat_lyrydw集群]] | [飞书](https://reliablesense.feishu.cn/docx/O5P2dVdVMoc3pWx0GVic4cpenhc) | → 提取 | `2-Areas/Work/运维管理/环境配置/` | 洛阳化工厂 |
| madinat_lyhx集群.md | [[4-Archives/Notes/Feishu/云空间/莱讯科技/项目运维管理/集群资料/madinat_lyhx集群]] | [飞书](https://reliablesense.feishu.cn/docx/HDKcdM8myoW1RExNYvac0N4pnuJ) | → 提取 | `2-Areas/Work/运维管理/环境配置/` | 洛阳化工厂 |
| xintai_xintai集群.md | [[4-Archives/Notes/Feishu/云空间/莱讯科技/项目运维管理/集群资料/xintai_xintai集群]] | [飞书](https://reliablesense.feishu.cn/docx/MbA7diPTJosC1Gxn3XPcfdMznVg) | → 提取 | `2-Areas/Work/运维管理/环境配置/` | 新太定位 |
| gjtsg_zhdl集群.md | [[4-Archives/Notes/Feishu/云空间/莱讯科技/项目运维管理/集群资料/gjtsg_zhdl集群]] | [飞书](https://reliablesense.feishu.cn/docx/FxjUdZYiyoDWmOxHklhcjvMlnZb) | → 提取 | `2-Areas/Work/运维管理/环境配置/` | 广州机场 |
| shwl_shsg集群.md | [[4-Archives/Notes/Feishu/云空间/莱讯科技/项目运维管理/集群资料/shwl_shsg集群]] | [飞书](https://reliablesense.feishu.cn/docx/MJ2KdoekEoS4jyxuHWfcx2UMnUb) | → 提取 | `2-Areas/Work/运维管理/环境配置/` | 上港仓储管理 |
| shwl_gzhft集群.md | [[4-Archives/Notes/Feishu/云空间/莱讯科技/项目运维管理/集群资料/shwl_gzhft集群]] | [飞书](https://reliablesense.feishu.cn/docx/WY2Hd2wu5oHOI1xJb3UculFSn1d) | → 提取 | `2-Areas/Work/运维管理/环境配置/` | 广州机场 |
| jiexun_autotrader集群.md | [[4-Archives/Notes/Feishu/云空间/莱讯科技/项目运维管理/集群资料/jiexun_autotrader集群]] | [飞书](https://reliablesense.feishu.cn/docx/QNHkdVzTEooNW9xhmvScZ0cKnMd) | → 提取 | `2-Areas/Work/运维管理/环境配置/` | - |
| lance_dxgcsy集群.md | [[4-Archives/Notes/Feishu/云空间/莱讯科技/项目运维管理/集群资料/lance_dxgcsy集群]] | [飞书](https://reliablesense.feishu.cn/docx/VN9RdnZIforRPWxYXX5ckt9ynQf) | → 提取 | `2-Areas/Work/运维管理/环境配置/` | - |
| erdoswhcyy_erdoswhcyy集群.md | [[4-Archives/Notes/Feishu/云空间/莱讯科技/项目运维管理/集群资料/erdoswhcyy_erdoswhcyy集群]] | [飞书](https://reliablesense.feishu.cn/docx/GW4tda6T9opR4jxGCkUcQA57n7d) | → 提取 | `2-Areas/Work/运维管理/环境配置/` | - |
| whjc_whjc集群.md | [[4-Archives/Notes/Feishu/云空间/莱讯科技/项目运维管理/集群资料/whjc_whjc集群]] | [飞书](https://reliablesense.feishu.cn/docx/RKuQdRotpoe3zixaPrWcx9j6nBc) | → 提取 | `2-Areas/Work/运维管理/环境配置/` | 武汉机场 |
| cloud 资料.md | [[4-Archives/Notes/Feishu/云空间/莱讯科技/项目运维管理/集群资料/cloud 资料]] | [飞书](https://reliablesense.feishu.cn/docx/QXgzdOibVoySLUxFwtzctoWin0t) | → 提取 | `2-Areas/Work/运维管理/环境配置/` | - （公共环境） |
| dev-office 集群.md | [[4-Archives/Notes/Feishu/云空间/莱讯科技/项目运维管理/集群资料/dev-office 集群]] | [飞书](https://reliablesense.feishu.cn/docx/QUtcdDjFjocOxVxiEiRcPQ20nZb) | → 提取 | `2-Areas/Work/运维管理/环境配置/` | - （公共环境） |
| online-sh 集群.md | [[4-Archives/Notes/Feishu/云空间/莱讯科技/项目运维管理/集群资料/online-sh 集群]] | [飞书](https://reliablesense.feishu.cn/docs/doccn4ZbY3L0axKO5uic6o278ge) | → 提取 | `2-Areas/Work/运维管理/环境配置/` | - （公共环境） |
| middleware-bj 集群.md | [[4-Archives/Notes/Feishu/云空间/莱讯科技/项目运维管理/集群资料/middleware-bj 集群]] | [飞书](https://reliablesense.feishu.cn/docs/doccnqB78BLk2Mq9fvYb9xEEbTd) | → 提取 | `2-Areas/Work/运维管理/环境配置/` | - （公共环境） |
| 代理配置操作说明.md | [[4-Archives/Notes/Feishu/云空间/莱讯科技/项目运维管理/集群资料/代理配置操作说明]] | [飞书](https://reliablesense.feishu.cn/docx/LbLPdc4dHoROcnxVSsmcF2sgnyb) | → 提取 | `2-Areas/Work/运维管理/代理配置操作说明.md` |
| 内网穿透 frp 说明.md | [[4-Archives/Notes/Feishu/云空间/莱讯科技/项目运维管理/集群资料/内网穿透 frp 说明]] | [飞书](https://reliablesense.feishu.cn/docx/doxcnAdY9LCLIeBTvI8nVH0St8e) | → 提取 | `2-Areas/Work/运维管理/内网穿透frp说明.md` |

### 4f. 基础设施

| 文件 | 本地路径 | 飞书链接 | 决策 | 目标路径 |
|------|---------|---------|------|---------|
| 综合定位系统技术要求.md | [[4-Archives/Notes/Feishu/云空间/莱讯科技/项目运维管理/基础设施/综合定位系统技术要求]] | [飞书](https://reliablesense.feishu.cn/docx/Gi0MdNC9ToLxM0xfPDCcsKD2nzf) | → 提取 | `1-Projects/Work/广州机场/综合定位系统技术要求.md` | 广州机场技术规格 |
| 系统功能清单.md | [[4-Archives/Notes/Feishu/云空间/莱讯科技/项目运维管理/基础设施/系统功能清单]] | [飞书](https://reliablesense.feishu.cn/docx/WdNtdRhPxoN8VoxwzI5cjocCntK) | → 提取 | `1-Projects/Work/广州机场/综合定位系统功能清单.md` | 广州机场功能列表 |
| 信息安全问题回复.md | [[4-Archives/Notes/Feishu/云空间/莱讯科技/项目资料管理/998. 售后项目/Bosch 项目/验收文档整理/信息安全问题回复]] | [飞书](https://reliablesense.feishu.cn/docx/YIs2dQZh4o3v3axaC0ccR2TInGe) | → 归档 | `4-Archives/Projects/Work/博世项目/信息安全问题回复.md` | 博世项目 |
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
| 定位平台服务器.md | [[4-Archives/Notes/Feishu/云空间/莱讯科技/项目资料管理/998. 售后项目/武汉机场/定位平台服务器]] | [飞书](https://reliablesense.feishu.cn/docx/UqgAd09BRoZ306xMBW4cvIK2npg) | → 归档 | `4-Archives/Projects/Work/武汉机场/定位平台服务器.md` |
| 定位平台操作手册.md | [[4-Archives/Notes/Feishu/云空间/莱讯科技/项目开发管理/定位平台企业版/定位平台操作手册]] | [飞书](https://reliablesense.feishu.cn/docx/A2jXdJxm7o6ilNxFx8ac86MYndh) | → 提取 | `2-Areas/Work/产品研发/定位平台操作手册.md` |
| 数据中心管理平台软件功能说明.docx | - | [飞书](https://reliablesense.feishu.cn/file/boxcnWm6KjLykr4WRCMKkQnzU8c) | → 归档 | `4-Archives/Projects/Work/数讯云人员服务系统/数据中心管理平台软件功能说明.docx` |
| 人员室内定位系统说明 1.docx | - | [飞书](https://reliablesense.feishu.cn/file/boxcnwfSd5TXpiHw2CwR0eufuPg) | → 归档 | `4-Archives/Projects/Work/数讯云人员服务系统/人员室内定位系统说明 1.docx` |
| 物资管理平台软件功能说明.docx | - | [飞书](https://reliablesense.feishu.cn/file/boxcnJDVPSgGOIWbUR9NHjXBHJg) | → 归档 | `4-Archives/Projects/Work/联通定位一体化/物资管理平台软件功能说明.docx` |
| 系统软件功能.docx | - | [飞书](https://reliablesense.feishu.cn/file/boxcn0vb3E82eDSw8ElpuI2ZT0g) | → 归档 | `4-Archives/Projects/Work/联通定位一体化/系统软件功能.docx` |
| GIT项目架构.mm | - | [飞书](https://reliablesense.feishu.cn/mindnotes/bmncnuGBjIbFqBI3cE9W858YYye) | → 提取 | `2-Areas/Work/产品研发/GIT项目架构.mm` |
| 平台部署.mm | - | [飞书](https://reliablesense.feishu.cn/mindnotes/bmncnMOlj5n1meGIFIfoarmKVQf) | → 提取 | `2-Areas/Work/产品研发/平台部署.mm` |
| 需求池管理.xlsx | - | [飞书](https://reliablesense.feishu.cn/sheets/shtcn6nHN1jUZTChiTWKcdjzpig) | → 提取 | `2-Areas/Work/产品研发/需求池管理.xlsx` |
| 产品介绍.md | - | [飞书](https://reliablesense.feishu.cn/docs/doccnNq1YJTyHP2IGOIZ4C9Y0qe) | → 提取 | `2-Areas/Work/品牌宣传/产品介绍.md` |
| 旧集群数据库地址.md | - | [飞书](https://reliablesense.feishu.cn/docs/doccnAhmPjNxK3hk9LkIxXfpL2b) | → 提取 | `2-Areas/Work/运维管理/旧集群数据库地址.md` |
| 软件架构图.md（文档资料） | - | [飞书](https://reliablesense.feishu.cn/docs/doccnNYXYzLw4jvVOBOTjTmjswh) | → 提取 | `2-Areas/Work/产品研发/定位平台软件架构图.md`（同上方已有条目） |
| KeyCloakgetJWTToken.xlsx | - | [飞书](https://reliablesense.feishu.cn/sheets/shtcnvteMVovUBaN8rS8NQ1Raed) | 留归档 | - |
| SAAS平台---告警功能修改.docx | - | [飞书](https://reliablesense.feishu.cn/file/boxcndpOpTARv88CTxsmgZlYoMd) | → 提取 | `2-Areas/Work/产品研发/SAAS平台---告警功能修改.docx` |
| SAAS平台---围栏功能修改.docx | - | [飞书](https://reliablesense.feishu.cn/file/boxcn6q1GX7yiyjgaJ84WA331Fd) | → 提取 | `2-Areas/Work/产品研发/SAAS平台---围栏功能修改.docx` |
| SAAS平台---巡检功能修改.docx | - | [飞书](https://reliablesense.feishu.cn/file/boxcnUwxy1MxqCG2NIO9ko3mSCe) | → 提取 | `2-Areas/Work/产品研发/SAAS平台---巡检功能修改.docx` |
| SAAS平台---考勤功能修改.docx | - | [飞书](https://reliablesense.feishu.cn/file/boxcndqLj9IzKRMnUzjpT6RZj8I) | → 提取 | `2-Areas/Work/产品研发/SAAS平台---考勤功能修改.docx` |
| Saas 云平台功能点列表.xlsx | - | [飞书](https://reliablesense.feishu.cn/file/boxcnRxxOFcqGLRdXuYv1qmsrXf) | → 提取 | `2-Areas/Work/产品研发/Saas 云平台功能点列表.xlsx` |
| 导航手册.docx | - | [飞书](https://reliablesense.feishu.cn/file/boxcnr1wKdPID0Vb2s1k0KhNnkh) | → 归档 | `4-Archives/Projects/Work/众合人员管理/导航手册.docx` |
| 识路室内定位应用功能对比.pptx | - | [飞书](https://reliablesense.feishu.cn/file/boxcn2AdaMjt4GUGOkOUAzzLbvc) | → 提取 | `2-Areas/Work/产品研发/识路室内定位应用功能对比.pptx` |
| 2023年项目管理.xlsx | - | [飞书](https://reliablesense.feishu.cn/base/bascnJYavmFDqZuOCPFO8LDSZku) | → 提取 | `2-Areas/Work/产品研发/2023年项目管理.xlsx` |
| 2024年项目管理.xlsx | - | [飞书](https://reliablesense.feishu.cn/base/PgwrbohXQa7IZEsVrG1cjOcUnXf) | → 提取 | `2-Areas/Work/产品研发/2024年项目管理.xlsx` |
| BUG管理.xlsx | - | [飞书](https://reliablesense.feishu.cn/base/JkumbQWa2ahQ7AsVlIIcVCaenXZ) | → 提取 | `2-Areas/Work/产品研发/BUG管理.xlsx` |
| 围栏需求重构/区域产品架构.mm | - | [飞书](https://reliablesense.feishu.cn/mindnotes/M8hDbdE6bm8XWLnLOvSc222xn9c) | → 提取 | `2-Areas/Work/产品研发/区域产品架构.mm` |
| 围栏需求重构/区域和告警产品架构.mm | - | [飞书](https://reliablesense.feishu.cn/mindnotes/bmncnBYdUDda1FKYFCtZpE5r0Vb) | → 提取 | `2-Areas/Work/产品研发/区域和告警产品架构.mm` |
| 围栏需求重构/区域管理.mm | - | [飞书](https://reliablesense.feishu.cn/mindnotes/Y7Dnb6aXZmy2w7nMUL7c8zcXnoh) | → 提取 | `2-Areas/Work/产品研发/区域管理.mm` |
| 传感器服务.mm | - | [飞书](https://reliablesense.feishu.cn/mindnotes/JepTbLLBFmAltWn3MgXczHfBnEb) | → 提取 | `2-Areas/Work/产品研发/传感器服务.mm` |
| 物资管理.mm | - | [飞书](https://reliablesense.feishu.cn/mindnotes/IQNGbY8v0mb0ubncPqHcLxxqnRe) | → 提取 | `2-Areas/Work/产品研发/物资管理.mm` |
| 思维导图.md | - | [飞书](https://reliablesense.feishu.cn/docx/F71LdvKrso6RjIxYW75ckNJAn6b) | → 提取 | `2-Areas/Work/产品研发/思维导图.md` |
| 产品规划.mm | - | [飞书](https://reliablesense.feishu.cn/mindnotes/FQcVbGFGAmoPs8nkYoHc04bYnTh) | → 提取 | `2-Areas/Work/产品研发/产品规划.mm` |
| defaultMapState 排序.mm | - | [飞书](https://reliablesense.feishu.cn/mindnotes/WEo3bEcijmu6FbnNRswcMQusn4e) | → 提取 | `2-Areas/Work/产品研发/defaultMapState排序.mm` |
| 获取在线数量接口.xlsx | - | [飞书](https://reliablesense.feishu.cn/sheets/ZnJEsCd5Hh7NYetsorBco7kHnA9) | → 提取 | `2-Areas/Work/产品研发/获取在线数量接口.xlsx` |
| 统计在线时长接口.xlsx | - | [飞书](https://reliablesense.feishu.cn/sheets/Ea0ssu4RahSisJtGrvHc1LhSnKe) | → 提取 | `2-Areas/Work/产品研发/统计在线时长接口.xlsx` |
| 统计在线离线数量接口.xlsx | - | [飞书](https://reliablesense.feishu.cn/sheets/ZnDjsr5SWhoeAnta8p8cex93nje) | → 提取 | `2-Areas/Work/产品研发/统计在线离线数量接口.xlsx` |
| v2.1/标签类型和模组.mm | - | [飞书](https://reliablesense.feishu.cn/mindnotes/bmncnrNwLI3pDukiVV5qZjJpIQh) | → 提取 | `2-Areas/Work/产品研发/标签类型和模组.mm` |
| v2.1/自行添加编辑删除标签.mm | - | [飞书](https://reliablesense.feishu.cn/mindnotes/bmncn6X1Bz6kOT5GeOcN4RFqBEc) | → 提取 | `2-Areas/Work/产品研发/自行添加编辑删除标签.mm` |
| v2.1/后端扩展运行服务数量.mm | - | [飞书](https://reliablesense.feishu.cn/mindnotes/bmncnhvyA4hYJXEk0oEE4B8R5vb) | → 提取 | `2-Areas/Work/产品研发/后端扩展运行服务数量.mm` |
| 2024-03-20前端三个需求.xlsx | - | [飞书](https://reliablesense.feishu.cn/sheets/CJGzsk2rIhTcrktIx4JciYYSnSc) | → 提取 | `2-Areas/Work/产品研发/2024-03-20前端三个需求.xlsx` |
| web端功能介绍.pptx | - | [飞书](https://reliablesense.feishu.cn/file/boxcnHMdjFMQaGBSMfqAChAMucd) | → 提取 | `2-Areas/Work/品牌宣传/web端功能介绍.pptx` |
| 室内外一体化定位管理方案.pdf | - | [飞书](https://reliablesense.feishu.cn/file/boxcnFhbtKDiwkFolETLU4KkN5f) | → 提取 | `2-Areas/Work/品牌宣传/室内外一体化定位管理方案.pdf` |
| 室内外一体化定位.pptx | - | [飞书](https://reliablesense.feishu.cn/file/boxcnOW0qQo6KYlsaHkVSiLfdac) | → 提取 | `2-Areas/Work/品牌宣传/室内外一体化定位.pptx` |
| 莱讯科技项目介绍0523.docx | - | [飞书](https://reliablesense.feishu.cn/file/boxcnRhmEB4n4xjrvqPkYBijqHb) | → 提取 | `2-Areas/Work/品牌宣传/莱讯科技项目介绍0523.docx` |
| 莱讯科技-软件系统功能（APP）.pptx | - | [飞书](https://reliablesense.feishu.cn/file/boxcnqMjNBaMWLJxCCPHEFAOvff) | → 提取 | `2-Areas/Work/品牌宣传/莱讯科技-软件系统功能（APP）.pptx` |
| 室内外一体化定位管理方案.pptx | - | [飞书](https://reliablesense.feishu.cn/file/boxcnuMD4ndgOrU7DI7rY2FfMJb) | → 提取 | `2-Areas/Work/品牌宣传/室内外一体化定位管理方案.pptx` |
| 图片.pptx | - | [飞书](https://reliablesense.feishu.cn/file/boxcn8vBVpxuneZFgvXrZ68ePJf) | → 提取 | `2-Areas/Work/品牌宣传/图片.pptx` |
| 莱讯科技-软件系统功能（PC）.pdf | - | [飞书](https://reliablesense.feishu.cn/file/boxcnmGko5EMBFc6BgWSR8rnGSf) | → 提取 | `2-Areas/Work/品牌宣传/莱讯科技-软件系统功能（PC）.pdf` |
| 莱讯公司产品介绍_20220104.pptx | - | [飞书](https://reliablesense.feishu.cn/file/boxcnxtQYZ1LrsB9rA01EokY3dS) | → 提取 | `2-Areas/Work/品牌宣传/莱讯公司产品介绍_20220104.pptx` |
| 莱讯科技项目介绍0526.docx | - | [飞书](https://reliablesense.feishu.cn/file/boxcnRtMGw6YimwHjVdkjnsUzVg) | → 提取 | `2-Areas/Work/品牌宣传/莱讯科技项目介绍0526.docx` |
| 莱讯科技-软件系统功能（PC）-无巡检.pptx | - | [飞书](https://reliablesense.feishu.cn/file/boxcnxFLTnKySZwmwsBIcajpYfd) | → 提取 | `2-Areas/Work/品牌宣传/莱讯科技-软件系统功能（PC）-无巡检.pptx` |

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
| MOKO Bluetooth 中间件 | - | [飞书](https://reliablesense.feishu.cn/file/M4LZbGtg0oOIaRxbFfUcNQrZnAf) | → 提取 | `2-Areas/Work/设备管理/MOKO蓝牙/` |
| MOKO GPS 中间件 | - | [飞书](https://reliablesense.feishu.cn/docx/Mhsjd6Qz2oaCzoxduhEcYiWznwg) | → 提取 | `2-Areas/Work/设备管理/MOKO蓝牙/` |
| 盈商云服 BLUETOOTH 中间件 | - | [飞书](https://reliablesense.feishu.cn/docx/FXa7d1fR2oplTOx4S0wcfCeLnXg) | → 提取 | `2-Areas/Work/设备管理/盈商云服蓝牙/` |
| 铨顺宏 UWB 中间件 | - | [飞书](https://reliablesense.feishu.cn/file/Tn7NbJjWGoTHI5xn6kRcVFHHnWb) | → 提取 | `2-Areas/Work/设备管理/铨顺宏UWB/` |
| 软件项目资料-云端版.md | [[4-Archives/Notes/Feishu/云空间/莱讯科技/项目开发管理/定位平台云端版/软件项目资料-云端版]] | [飞书](https://reliablesense.feishu.cn/docx/doxcnYnCagX1SsmAbbSyUtL0SRb) | → 提取 | `2-Areas/Work/产品研发/软件项目资料-云端版.md` |

---

## 六、莱讯科技/项目资料管理

### 6a. 进行中项目 → `1-Projects/Work/`

| 飞书目录 | 本地路径 | 飞书链接 | 目标路径 |
|---------|---------|---------|---------|
| 002. 上海上港/ | [[4-Archives/Notes/Feishu/云空间/莱讯科技/项目资料管理/002. 上海上港/README]] | [飞书（目录）](https://reliablesense.feishu.cn/drive/folder/IwSpfxmL5lfpO8dLuoccbdnLnre) | `1-Projects/Work/上港仓储管理/` |
| 004. 广州机场-综合定位/ | [[4-Archives/Notes/Feishu/云空间/莱讯科技/项目资料管理/004. 广州机场-综合定位/README]] | [飞书（目录）](https://reliablesense.feishu.cn/drive/folder/MrIOflncTlWrkEd4hJZcUxatncd) | `1-Projects/Work/广州机场/综合定位/` |
| 005. 广州机场-移动应用平台/ | [[4-Archives/Notes/Feishu/云空间/莱讯科技/项目资料管理/005. 广州机场-移动应用平台/README]] | [飞书（目录）](https://reliablesense.feishu.cn/drive/folder/DZVbfWCNnl1IaudvPBpcpXjenQf) | `1-Projects/Work/广州机场/移动应用平台/` |
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
| 000. 售前项目/ | [[4-Archives/Notes/Feishu/云空间/莱讯科技/项目资料管理/000. 售前项目/README]] | [飞书（目录）](https://reliablesense.feishu.cn/drive/folder/JgzWfy33SlvnsSdrg5Uc3Fdrnm1) | → 提取 | `4-Archives/Areas/Work/业务管理/售前项目/` |
| 001. 项目资料模板/ | [[4-Archives/Notes/Feishu/云空间/莱讯科技/项目资料管理/001. 项目资料模板/README]] | [飞书（目录）](https://reliablesense.feishu.cn/drive/folder/XHMvfo59aln6mfd4sqpcHpI0neh) | → 提取 | `2-Areas/Work/业务管理/项目资料模板/` |
| 软著立项/ | [[4-Archives/Notes/Feishu/云空间/莱讯科技/项目资料管理/软著立项/README]] | [飞书（目录）](https://reliablesense.feishu.cn/drive/folder/SscHfr1iClEid6dcPsrc5cTJnNb) | → 提取 | `2-Areas/Work/综合管理/软著立项/` |
| 项目评估/ | [[4-Archives/Notes/Feishu/云空间/莱讯科技/项目资料管理/项目评估/README]] | [飞书（目录）](https://reliablesense.feishu.cn/drive/folder/WW7df5NEglBmvCdYGDQcFZNKnEe) | → 提取 | `2-Areas/Work/业务管理/项目评估/` |
| 展会/ | - | [飞书](https://reliablesense.feishu.cn/file/OWd6bsifDoWOGhxclnkcLzMjnxg) | → 提取 | `2-Areas/Work/品牌宣传/展会/` |
| 项目管理-bitable.xlsx | - | [飞书](https://reliablesense.feishu.cn/base/bascn8p8PpJEyLNk6UovDb1V6Of) | → 提取 | `2-Areas/Work/业务管理/` |
| 项目管理-附件映射.md | - | 无飞书链接（迁移生成） | → 提取 | `2-Areas/Work/业务管理/`（跟随 bitable） |
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
| ~参考资料/ | [[4-Archives/Notes/Feishu/云空间/莱讯科技/~参考资料/README]] | [飞书（目录）](https://reliablesense.feishu.cn/drive/folder/fldcnpp8JeCmpzMuPLsbsIczAif) | 部分提取 | 自家素材→品牌宣传/产品研发，竞品资料→待确认 |
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
| 考勤制度-原版.md | - | [飞书](https://reliablesense.feishu.cn/docx/ICeIdwPzXo2hSDxtqFqc4757nXd) | → 提取 | `2-Areas/Work/团队管理/考勤制度-原版.md` |

### 公司内部资料子目录

| 目录 | 飞书链接 | 文件数 | 决策 | 目标路径 |
|------|---------|--------|------|---------|
| 2022定位视频/ | [飞书](https://reliablesense.feishu.cn/file/boxcn1t83XNqLAuZq9F9mEKly1b) | 4 | → 提取 | `2-Areas/Work/品牌宣传/` |
| 2023宣传视频/ | [飞书](https://reliablesense.feishu.cn/file/DMccbTFYpoSz91xIuv2cyXCKnJe) | 13 | → 提取 | `2-Areas/Work/品牌宣传/` |
| 2023年研发项目立项资料/ | [飞书](https://reliablesense.feishu.cn/file/UYoXbzqTUoOZscxKuhacKzqyn8g) | 9 | → 提取 | `2-Areas/Work/综合管理/` |
| 2023年终总结/ | [飞书](https://reliablesense.feishu.cn/docx/CZj2dxw1LogAk6xxLqucPwEvngf) | 3 | → 归档 | `4-Archives/Areas/Work/团队管理/` |
| 2023年项目内容/Bosch | [飞书](https://reliablesense.feishu.cn/sheets/FG67snAd3hBsbStDZUjcHpotnhe) | 3 | → 提取 | `2-Areas/Work/综合管理/` |
| 2023年项目内容/Bossard | [飞书](https://reliablesense.feishu.cn/sheets/NORxsbRtvhK7Ggtrtb8cyWw5ndf) | 3 | → 提取 | `2-Areas/Work/综合管理/` |
| 2023年项目内容/国图 | [飞书](https://reliablesense.feishu.cn/docx/ScLMdCwAro02gjxZfnIcPEqOnTb) | 3 | → 提取 | `2-Areas/Work/综合管理/` |
| 公司网站/ | [飞书](https://reliablesense.feishu.cn/file/boxcnSTAzy0wrZa2ZqKMX1w9msM) | 8+子目录 | → 提取 | `2-Areas/Work/品牌宣传/网站素材/` |
| 名片电子版/ | [飞书](https://reliablesense.feishu.cn/file/XiyXbkRRAooP07xecJZc1399nfG) | 5+子目录 | → 提取 | `2-Areas/Work/品牌宣传/` |
| 员工管理/2022年终总结 | [飞书](https://reliablesense.feishu.cn/docx/AqesdgLmCoxGJExG8rhcJGXKnEz) | 11 | → 归档 | `4-Archives/Areas/Work/团队管理/团队成员/` |
| 商业计划书/ | [飞书](https://reliablesense.feishu.cn/file/boxcnzkIOJ3HZgyXBtGe7kK862e) | 7+子目录 | → 提取 | `2-Areas/Work/业务管理/商业计划书/` |
| 地图绘制步骤/ | [飞书](https://reliablesense.feishu.cn/file/boxcndhHyiVoqsMusxGM9xfTzIc) | 15 | → 提取 | `2-Areas/Work/产品研发/` |
| 宣传物料/ | [飞书](https://reliablesense.feishu.cn/file/E73ob0v4yof5R7xfW2HcjCWdnuf) | 6+子目录 | → 提取 | `2-Areas/Work/品牌宣传/` |
| 展会/ | [飞书](https://reliablesense.feishu.cn/file/boxcnKyHGiZPqpDgI9AkHDMnGec) | 7+子目录 | → 提取 | `2-Areas/Work/品牌宣传/展会/` |
| 沙溪办公室/ | [飞书](https://reliablesense.feishu.cn/file/boxcnntBkT4MffCt00Jan2z9czd) | 3 | → 提取 | `2-Areas/Work/综合管理/` |
| 照片/ | - | ~102 | → 提取 | `2-Areas/Work/品牌宣传/` |
| 财务/ | [飞书](https://reliablesense.feishu.cn/file/boxcn2lqM177PAuDExODeTY4Cmg) | 1 | → 提取 | `2-Areas/Work/综合管理/` |
| 项目说明综合/ | [飞书](https://reliablesense.feishu.cn/file/boxcnzJVGenDANt0bPUvqc39Hih) | 3 | → 提取 | `2-Areas/Work/品牌宣传/` |

---

## 九、知识库

### 9a. 技术分享

| 文件 | 本地路径 | 飞书链接 | 决策 | 目标路径 |
|------|---------|---------|------|---------|
| 前端React开发规范.md | [[4-Archives/Notes/Feishu/知识库/技术分享/前端相关文档/前端React开发规范]] | [飞书](https://reliablesense.feishu.cn/doc/doccnymhDUxjzJsBjuZ5mBGpG4c) | → 提取 | `3-Resources/Tech/知识卡片/前端React开发规范.md` |
| 后端开发流程规范.md | [[4-Archives/Notes/Feishu/知识库/技术分享/后端相关文档/后端开发流程规范]] | [飞书](https://reliablesense.feishu.cn/docx/CUA7dlJrRoTZ3Fx8t5kc1UiRneb) | → 提取 | `2-Areas/Work/产品研发/后端开发流程规范.md` |
| 定位平台系统整体改造方案.md | [[4-Archives/Notes/Feishu/知识库/技术分享/后端相关文档/定位平台系统整体改造方案]] | [飞书](https://reliablesense.feishu.cn/doc/doccnVRMcLTfhON3R9OLZT7VHgf) | → 提取 | `2-Areas/Work/产品研发/定位平台系统整体改造方案.md` |
| 微服务说明.md | [[4-Archives/Notes/Feishu/知识库/技术分享/后端相关文档/微服务说明]] | [飞书](https://reliablesense.feishu.cn/docx/F2PhdYeMCoHjP6xd8y0cyz6Mnac) | → 提取 | `2-Areas/Work/产品研发/微服务说明.md` |
| 后端问题QA.md | [[4-Archives/Notes/Feishu/知识库/技术分享/后端问题QA]] | [飞书](https://reliablesense.feishu.cn/docx/OpsxdI417oi5i4xLyrhc8Znyn5f) | → 提取 | `2-Areas/Work/产品研发/后端问题QA.md` |
| QGIS地图绘制准备.md | [[4-Archives/Notes/Feishu/知识库/技术分享/地图相关文档/QGIS地图绘制准备]] | [飞书](https://reliablesense.feishu.cn/docx/CXjHdQO7JogckXxR6owcL5AcnEb) | → 提取 | `3-Resources/Tech/知识卡片/QGIS地图绘制准备.md` |
| QGIS安装.md | [[4-Archives/Notes/Feishu/知识库/技术分享/地图相关文档/QGIS安装]] | [飞书](https://reliablesense.feishu.cn/docx/DKP6dIPIHoXYuMxJ5Xoc00LVngp) | → 提取 | `3-Resources/Tech/知识卡片/QGIS安装.md` |
| QGIS图片及瓦片图添加.md | [[4-Archives/Notes/Feishu/知识库/技术分享/地图相关文档/QGIS图片及瓦片图添加]] | [飞书](https://reliablesense.feishu.cn/docx/X68Zdyv98o4AgGx073LcsrscnAh) | → 提取 | `3-Resources/Tech/知识卡片/QGIS图片及瓦片图添加.md` |
| QGIS地图绘制注意事项CAD版.md | [[4-Archives/Notes/Feishu/知识库/技术分享/地图相关文档/QGIS地图绘制注意事项CAD版]] | [飞书](https://reliablesense.feishu.cn/doc/doccnKYx4RPxYSXzTH0ssUvvBmf) | → 提取 | `3-Resources/Tech/知识卡片/QGIS地图绘制注意事项CAD版.md` |
| png图片导入地图.md | [[4-Archives/Notes/Feishu/知识库/技术分享/地图相关文档/png图片导入地图]] | [飞书](https://reliablesense.feishu.cn/doc/doccn3DidLn9ur0mvFbqsnXhstd) | → 提取 | `3-Resources/Tech/知识卡片/png图片导入地图.md` |
| 瓦片图制作.md | [[4-Archives/Notes/Feishu/知识库/技术分享/地图相关文档/瓦片图制作]] | [飞书](https://reliablesense.feishu.cn/docx/OvGsdeF3UoAgULxqd9Kc08punEg) | → 提取 | `3-Resources/Tech/知识卡片/瓦片图制作.md` |
| 路网绘制.md | [[4-Archives/Notes/Feishu/知识库/技术分享/地图相关文档/路网绘制]] | [飞书](https://reliablesense.feishu.cn/docx/doxcnmMiCtaR2HkpnlPPrChqyEb) | → 提取 | `3-Resources/Tech/知识卡片/路网绘制.md` |
| 地图按钮、视角、控件控制.md | [[4-Archives/Notes/Feishu/知识库/技术分享/地图相关文档/地图按钮、视角、控件控制]] | [飞书](https://reliablesense.feishu.cn/docx/HUTId5xjFoaRIxxUkQWcEb1Xnge) | → 提取 | `3-Resources/Tech/知识卡片/地图控件控制.md` |
| 项目建立步骤.md | [[4-Archives/Notes/Feishu/知识库/技术分享/地图相关文档/项目建立步骤]] | [飞书](https://reliablesense.feishu.cn/docx/LapVd88f0oFaKUx4QwRcwrW1neI) | → 提取 | `3-Resources/Tech/知识卡片/地图项目建立步骤.md` |
| 麦钉点云图地图绘制注意事项.md | [[4-Archives/Notes/Feishu/知识库/技术分享/地图相关文档/麦钉点云图地图绘制注意事项]] | [飞书](https://reliablesense.feishu.cn/doc/doccn6HL7llLqfP4e5qCI96CdUf) | → 提取 | `1-Projects/Work/麦钉定位/麦钉点云图地图绘制注意事项.md` |
| CICD流程介绍.md | [[4-Archives/Notes/Feishu/知识库/技术分享/基础平台相关文档/CICD流程介绍]] | [飞书](https://reliablesense.feishu.cn/doc/doccnqi4YxvSVSY23MSLXIkwIKe) | → 提取 | `3-Resources/Tech/知识卡片/CICD流程介绍.md` |
| Gitlab-CICD说明.md | [[4-Archives/Notes/Feishu/知识库/技术分享/基础平台相关文档/Gitlab-CICD说明]] | [飞书](https://reliablesense.feishu.cn/doc/doccnUileviuvksypU7AAbSEGwg) | → 提取 | `3-Resources/Tech/知识卡片/Gitlab-CICD说明.md` |
| 前后端CICD.md | [[4-Archives/Notes/Feishu/知识库/技术分享/基础平台相关文档/前后端CICD]] | [飞书](https://reliablesense.feishu.cn/doc/doccncqa7DwRv2fD3Z3KA6oO4oh) | → 提取 | `3-Resources/Tech/知识卡片/前后端CICD.md` |
| 开发分支管理规范.md | [[4-Archives/Notes/Feishu/知识库/技术分享/基础平台相关文档/开发分支管理规范]] | [飞书](https://reliablesense.feishu.cn/doc/doccnlE0yWc24L79rE98oSVsY8d) | → 提取 | `3-Resources/Tech/知识卡片/开发分支管理规范.md` |
| 办公网v2ray操作手册.md | [[4-Archives/Notes/Feishu/知识库/技术分享/基础平台相关文档/办公网VPN/办公网v2ray操作手册]] | [飞书](https://reliablesense.feishu.cn/docx/G1OBdhlTSotGV6xRToRcXlzWnoe) | → 提取 | `2-Areas/Work/运维管理/办公网v2ray操作手册.md` |
| 办公网WireGuard操作手册.md | [[4-Archives/Notes/Feishu/知识库/技术分享/基础平台相关文档/办公网VPN/办公网WireGuard操作手册]] | [飞书](https://reliablesense.feishu.cn/docx/Q4OzdL6ZboG5dSxgqqlcNn4WnFf) | → 提取 | `2-Areas/Work/运维管理/办公网WireGuard操作手册.md` |
| A-Server-environment-preparation.md | [[4-Archives/Notes/Feishu/知识库/技术分享/基础平台相关文档/Deployment英文版/A-Server-environment-preparation]] | [飞书](https://reliablesense.feishu.cn/docx/CWnsdq3ryoYTSHxGAC0cpcoenbg) | → 提取 | `2-Areas/Work/运维管理/私有化部署/A-Server-environment-preparation.md` |
| B1-Cluster-setup-K3s-online.md | [[4-Archives/Notes/Feishu/知识库/技术分享/基础平台相关文档/Deployment英文版/B1-Cluster-setup-K3s-online]] | [飞书](https://reliablesense.feishu.cn/docx/Kgifd4mPJo5nuVxkmX2cF76unde) | → 提取 | `2-Areas/Work/运维管理/私有化部署/B1-Cluster-setup-K3s-online.md` |
| B2-Cluster-setup-K3s-offline.md | [[4-Archives/Notes/Feishu/知识库/技术分享/基础平台相关文档/Deployment英文版/B2-Cluster-setup-K3s-offline]] | [飞书](https://reliablesense.feishu.cn/docx/NQgadYYYJo5e4sxLhxMcLMZ9nGB) | → 提取 | `2-Areas/Work/运维管理/私有化部署/B2-Cluster-setup-K3s-offline.md` |
| C-Installation-of-basic-services.md | [[4-Archives/Notes/Feishu/知识库/技术分享/基础平台相关文档/Deployment英文版/C-Installation-of-basic-services]] | [飞书](https://reliablesense.feishu.cn/docx/MXFDdnQvAoKSMAxxdAXc2I9bnYb) | → 提取 | `2-Areas/Work/运维管理/私有化部署/C-Installation-of-basic-services.md` |
| A-服务器环境准备.md | [[4-Archives/Notes/Feishu/知识库/技术分享/基础平台相关文档/私有化部署/A-服务器环境准备]] | [飞书](https://reliablesense.feishu.cn/docx/doxcniK4NdHGlK7G8gccJ5WYnEg) | → 提取 | `2-Areas/Work/运维管理/私有化部署/A-服务器环境准备.md` |
| B1-集群搭建K3s在线版.md | [[4-Archives/Notes/Feishu/知识库/技术分享/基础平台相关文档/私有化部署/B1-集群搭建K3s在线版]] | [飞书](https://reliablesense.feishu.cn/docx/doxcn67UW5vdFM5qaPG3tc9zMdd) | → 提取 | `2-Areas/Work/运维管理/私有化部署/B1-集群搭建K3s在线版.md` |
| B2-集群搭建K3s离线版.md | [[4-Archives/Notes/Feishu/知识库/技术分享/基础平台相关文档/私有化部署/B2-集群搭建K3s离线版]] | [飞书](https://reliablesense.feishu.cn/docx/SuiNdHlegogxpcxnqqhc8AuKnZ1) | → 提取 | `2-Areas/Work/运维管理/私有化部署/B2-集群搭建K3s离线版.md` |
| C-集群内基础服务安装.md | [[4-Archives/Notes/Feishu/知识库/技术分享/基础平台相关文档/私有化部署/C-集群内基础服务安装]] | [飞书](https://reliablesense.feishu.cn/docx/doxcnSbULW58Lp1lXBy2tt8i80e) | → 提取 | `2-Areas/Work/运维管理/私有化部署/C-集群内基础服务安装.md` |
| 命令行工具oemctl.md | [[4-Archives/Notes/Feishu/知识库/技术分享/基础平台相关文档/私有化部署/命令行工具oemctl]] | [飞书](https://reliablesense.feishu.cn/docx/J1C8daWxto4clexYnaDcKtgQnzf) | → 提取 | `2-Areas/Work/运维管理/私有化部署/命令行工具oemctl.md` |
| 偏移位置数据到火星坐标.md | [[4-Archives/Notes/Feishu/知识库/技术分享/数据库相关文档/Postgis/偏移位置数据到火星坐标]] | [飞书](https://reliablesense.feishu.cn/doc/doccn4JOodvetnzvaKMfs3aIBSh) | → 提取 | `3-Resources/Tech/代码片段/` |
| 火星坐标转换.md | [[4-Archives/Notes/Feishu/知识库/技术分享/数据库相关文档/Postgis/火星坐标转换]] | [飞书](https://reliablesense.feishu.cn/doc/doccnbSee08xdsJhTWt1nXJccZc) | → 提取 | `3-Resources/Tech/代码片段/` |
| 获取指定范围内的点.md | [[4-Archives/Notes/Feishu/知识库/技术分享/数据库相关文档/Postgis/获取指定范围内的点]] | [飞书](https://reliablesense.feishu.cn/doc/doccnhqA2pLGKjd5fnqdDsdRbig) | → 提取 | `3-Resources/Tech/代码片段/` |
| 更新地图中点和边界.md | [[4-Archives/Notes/Feishu/知识库/技术分享/数据库相关文档/Postgis/更新地图中点和边界]] | [飞书](https://reliablesense.feishu.cn/doc/doccnI6f4RL5XRKR8R2k2oA6Ykf) | → 提取 | `3-Resources/Tech/代码片段/` |
| 移动缩放旋转地图.md | [[4-Archives/Notes/Feishu/知识库/技术分享/数据库相关文档/Postgis/移动缩放旋转地图]] | [飞书](https://reliablesense.feishu.cn/doc/doccnN1mQdwwDwXCsBhuSsVzTId) | → 提取 | `3-Resources/Tech/代码片段/` |
| 移动电子围栏到火星坐标.md | [[4-Archives/Notes/Feishu/知识库/技术分享/数据库相关文档/Postgis/移动电子围栏到火星坐标]] | [飞书](https://reliablesense.feishu.cn/doc/doccnvu9gfk9NPRnE1FMF7fpNFe) | → 提取 | `3-Resources/Tech/代码片段/` |
| 修改火星坐标完整语句.md | [[4-Archives/Notes/Feishu/知识库/技术分享/数据库相关文档/Postgis/修改火星坐标完整语句]] | [飞书](https://reliablesense.feishu.cn/doc/doccnZUAaAKBqN3uCPCiAHkWo30) | → 提取 | `3-Resources/Tech/代码片段/` |
| 将Point转成PointZ.md | [[4-Archives/Notes/Feishu/知识库/技术分享/数据库相关文档/Postgis/将Point转成PointZ]] | [飞书](https://reliablesense.feishu.cn/doc/doccnZTs4pwAZPya8zQfIgRf7Yf) | → 提取 | `3-Resources/Tech/代码片段/` |
| 处理连接数的问题.md | [[4-Archives/Notes/Feishu/知识库/技术分享/数据库相关文档/Postgres/处理连接数的问题]] | [飞书](https://reliablesense.feishu.cn/doc/doccnZIMQSFgw5z9FAtvRxqEF4f) | → 提取 | `3-Resources/Tech/问题解决/处理连接数的问题.md` |
| 处理t_position的id问题.md | [[4-Archives/Notes/Feishu/知识库/技术分享/数据库相关文档/Postgres/处理t_position的id问题]] | [飞书](https://reliablesense.feishu.cn/doc/doccnDPxocYNEJe0c7YYnRI6R3e) | → 提取 | `3-Resources/Tech/问题解决/处理t_position的id问题.md` |
| 生成trigger_set_timestamp.md | [[4-Archives/Notes/Feishu/知识库/技术分享/数据库相关文档/Postgres/生成trigger_set_timestamp]] | [飞书](https://reliablesense.feishu.cn/doc/doccnszyZqVAlZhQ6yFE8iVp3uf) | → 提取 | `3-Resources/Tech/代码片段/` |
| 生成UUID.md | [[4-Archives/Notes/Feishu/知识库/技术分享/数据库相关文档/Postgres/生成UUID]] | [飞书](https://reliablesense.feishu.cn/doc/doccnKzX7vdTlRNlsKlQY9oo9vd) | → 提取 | `3-Resources/Tech/代码片段/` |
| 人员物体每日在线时间统计.md | [[4-Archives/Notes/Feishu/知识库/技术分享/数据库相关文档/TimescaleDB/人员物体每日在线时间统计]] | [飞书](https://reliablesense.feishu.cn/doc/doccnSG2Jc0Fls0feLdgve23DOe) | → 提取 | `2-Areas/Work/产品研发/人员物体每日在线时间统计.md` |
| 新建hyper_table时Trigger错误.md | [[4-Archives/Notes/Feishu/知识库/技术分享/数据库相关文档/TimescaleDB/新建hyper_table时Trigger错误]] | [飞书](https://reliablesense.feishu.cn/doc/doccnoNAhwDhgg2FpnJ5jOODzZb) | → 提取 | `3-Resources/Tech/问题解决/新建hyper_table时Trigger错误.md` |
| Retention-policy定期删除机制.md | [[4-Archives/Notes/Feishu/知识库/技术分享/数据库相关文档/TimescaleDB/Retention-policy定期删除机制]] | [飞书](https://reliablesense.feishu.cn/doc/doccn2mQON8tP7m08bYrNmq5BYc) | → 提取 | `3-Resources/Tech/代码片段/` |
| 插入一条t_position数据.md | [[4-Archives/Notes/Feishu/知识库/技术分享/数据库相关文档/TimescaleDB/插入一条t_position数据]] | [飞书](https://reliablesense.feishu.cn/doc/doccnmbpSo3CRnCMyTYEVFTpbIi) | → 提取 | `3-Resources/Tech/代码片段/` |
| locust报告参数说明.md | [[4-Archives/Notes/Feishu/知识库/技术分享/测试相关文档/locust报告参数说明]] | [飞书](https://reliablesense.feishu.cn/docx/doxcnyVpKX1V11tJYH2sKdff3Ph) | → 提取 | `3-Resources/Tech/知识卡片/locust报告参数说明.md` |
| 测试平台对比.md | [[4-Archives/Notes/Feishu/知识库/技术分享/测试相关文档/测试平台对比]] | [飞书](https://reliablesense.feishu.cn/doc/doccnoMeCyK1lHtPzzIxxZTmB8U) | → 提取 | `3-Resources/Tech/知识卡片/测试平台对比.md` |
| 测试流程1.md | [[4-Archives/Notes/Feishu/知识库/技术分享/测试相关文档/测试流程1]] | [飞书](https://reliablesense.feishu.cn/doc/doccnvKjRt0RgI04vi1UFEuAW4f) | → 提取 | `1-Projects/Work/测试流程建立/测试流程1.md` |
| 测试的流程及内容.md | [[4-Archives/Notes/Feishu/知识库/技术分享/测试相关文档/测试的流程及内容]] | [飞书](https://reliablesense.feishu.cn/doc/doccnUSmCPXtSpHsITXo3gMqtqd) | → 提取 | `1-Projects/Work/测试流程建立/测试的流程及内容.md` |
| 测试计划初稿.md | [[4-Archives/Notes/Feishu/知识库/技术分享/测试相关文档/测试计划初稿]] | [飞书](https://reliablesense.feishu.cn/doc/doccnXKbFqjR5Up9dVYrzjvUUmh) | → 提取 | `1-Projects/Work/测试流程建立/测试计划初稿.md` |
| 禅道测试相关操作手册.md | [[4-Archives/Notes/Feishu/知识库/技术分享/测试相关文档/禅道测试相关操作手册]] | [飞书](https://reliablesense.feishu.cn/doc/doccnTqc7EnZxfZYH0T20rXWLVe) | → 提取 | `1-Projects/Work/测试流程建立/禅道测试操作手册.md` |
| 稳定性测试.md | [[4-Archives/Notes/Feishu/知识库/技术分享/测试相关文档/稳定性测试]] | [飞书](https://reliablesense.feishu.cn/docx/doxcnPMwcMjDrt0cdQBUlY9Jldf) | → 提取 | `3-Resources/Tech/知识卡片/稳定性测试.md` |
| MOKO-RSSI定位基站与树莓派组网.md | [[4-Archives/Notes/Feishu/知识库/技术分享/硬件相关文档/MOKO-RSSI定位基站与树莓派组网]] | [飞书](https://reliablesense.feishu.cn/docx/TDS8dDE7ToGtUWxMvu7c8bROnwf) | → 提取 | `2-Areas/Work/设备管理/MOKO蓝牙/MOKO-RSSI定位基站与树莓派组网.md` |
| RTK设备局域网WiFi使用文档.md | [[4-Archives/Notes/Feishu/知识库/技术分享/硬件相关文档/RTK设备局域网WiFi使用文档]] | [飞书](https://reliablesense.feishu.cn/docx/Yr5vdDP3YonYuWxkhZ3cfDGDnGd) | → 提取 | `2-Areas/Work/设备管理/莱讯科技设备/RTK设备局域网WiFi使用文档.md` |
| 树莓派SSD版本安装.md | [[4-Archives/Notes/Feishu/知识库/技术分享/硬件相关文档/树莓派SSD版本安装]] | [飞书](https://reliablesense.feishu.cn/docx/YUSVdEwLVooPMHx3luMcAXh6nlh) | → 提取 | `3-Resources/Tech/知识卡片/树莓派SSD版本安装.md` |
| 烧写设备.md | [[4-Archives/Notes/Feishu/知识库/技术分享/硬件相关文档/烧写设备]] | [飞书](https://reliablesense.feishu.cn/docx/NigodFqlcowXQVxYWh5cVyoDn2g) | → 提取 | `2-Areas/Work/设备管理/莱讯科技设备/烧写设备.md` |
| 日常运维相关文档.md | [[4-Archives/Notes/Feishu/知识库/技术分享/日常运维相关文档]] | [飞书](https://reliablesense.feishu.cn/doc/doccnlJ8hk4ih92ZXrCFLFc9Zid) | 留归档 | - |

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
| Iot接口对接代码.md | [[4-Archives/Notes/Feishu/知识库/个人知识库/Iot接口对接代码]] | [飞书](https://reliablesense.feishu.cn/wiki/PJMvwq7JFipjUIkquXpcVEt2nUf) | → 提取 | `1-Projects/Work/广州机场/IoT接口对接代码.md` |
| Rocket命令行测试.md | [[4-Archives/Notes/Feishu/知识库/个人知识库/Rocket命令行测试]] | [飞书](https://reliablesense.feishu.cn/wiki/NECEwJ2pUienKZkrcsRc6Pranyg) | → 提取 | `3-Resources/Tech/代码片段/RocketMQ命令行测试.md` |
| 订阅压线事件.md | [[4-Archives/Notes/Feishu/知识库/个人知识库/订阅压线事件]] | [飞书](https://reliablesense.feishu.cn/wiki/UwMHwNSUxie9kNkrqVwc0SwOnKe) | 留归档 | - |
| 车载定位连调总结.md | [[4-Archives/Notes/Feishu/知识库/个人知识库/车载定位连调总结]] | [飞书](https://reliablesense.feishu.cn/wiki/I7C8w9kEBiLR3YkaRyJcbekunVf) | → 提取 | `1-Projects/Work/南宁机场/车载定位连调总结.md` |
| 重定位.md | [[4-Archives/Notes/Feishu/知识库/个人知识库/重定位]] | [飞书](https://reliablesense.feishu.cn/wiki/EcASw46qMijgXFkNqQZcWstJnWe) | 留归档 | - |
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
| 新太元验收标准总结.md | [[4-Archives/Notes/Feishu/知识库/受限知识库/新太元验收标准总结]] | [飞书](https://reliablesense.feishu.cn/wiki/LbYbwPb1QidoL0kpKakcRhCrnPe) | → 提取 | `1-Projects/Work/新太定位/验收标准总结.md` |
| 新太定位总结.md | [[4-Archives/Notes/Feishu/知识库/受限知识库/新太定位总结]] | [飞书](https://reliablesense.feishu.cn/wiki/TK3Sw7sNkiEFD1kFx27cLTkznAV) | → 提取 | `1-Projects/Work/新太定位/项目总结.md` |
| 2025年年终总结-后端.md | [[4-Archives/Notes/Feishu/知识库/受限知识库/2025年年终总结-后端]] | [飞书](https://reliablesense.feishu.cn/wiki/ZSDawo3uLi4lxXkGZP7cHGxBnXc) | → 提取 | `4-Archives/Areas/Work/团队管理/团队成员/王宗光/` | 年终总结，按人归档 |
| 2025年度总结-前端.md | [[4-Archives/Notes/Feishu/知识库/受限知识库/2025年度总结-前端]] | [飞书](https://reliablesense.feishu.cn/wiki/MqWawqoYkiJsQekf1y2c8Hatnve) | → 提取 | `4-Archives/Areas/Work/团队管理/团队成员/陈子杰/` | 年终总结，按人归档 |
| 刘远达25年年终总结.md | [[4-Archives/Notes/Feishu/知识库/受限知识库/刘远达25年年终总结]] | [飞书](https://reliablesense.feishu.cn/wiki/TfMYwzD5citiR0kXrffcRYNUn8d) | → 提取 | `4-Archives/Areas/Work/团队管理/团队成员/刘远达/` | 年终总结，按人归档 |

---

## 十、需要新建的 PARA 目录

```
2-Areas/Work/运维管理/
3-Resources/Tech/环境配置/
3-Resources/Tech/环境配置/
4-Archives/Areas/Work/业务管理/售前项目/
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

## 十二a、单个项目迁移标准步骤

适用于所有项目/业务管理目录的迁移，目标路径根据项目状态和类型决定：

| 项目状态 | 目标路径 | 知识库位置 |
|---------|---------|-----------|
| 进行中项目 | `1-Projects/Work/{项目名}/` | 项目资料 / {项目名} |
| 已结束项目 | `4-Archives/Projects/Work/{项目名}/` | 项目资料 / 归档项目 / {项目名} |
| 进行中业务管理 | `2-Areas/Work/业务管理/{业务名}/` | 业务管理 / {业务名} |
| 已归档业务管理 | `4-Archives/Areas/Work/业务管理/{业务名}/` | 业务管理 / 归档 / {业务名} |

### 文件同步策略

| 文件类型 | 本地 | 飞书云空间 | 飞书知识库 | 0-总览中 | 说明 |
|---------|------|-----------|-----------|---------|------|
| `.md`（docx 转换） | ✅ 保留 | ✅ 原件不动 | ✅ copy 副本 | `[[wikilink]]` | Obsidian 可渲染，双端都有 |
| `Attachments/*.png/jpg` | ✅ 保留 | — | — | — | md 引用的图片，跟随 md 文件 |
| `.docx/.xlsx/.pptx`（file 类型） | ✅ 下载保留 | ✅ 原件不动 | ✅ copy 副本 | 📌 本地附件 + 飞书链接 | 上传的附件文件，本地也保留一份 |
| `sheet`（电子表格） | ❌ 不保留 | ✅ 原件不动 | ✅ copy 副本 | ☁️ 仅云端 + 飞书链接 | 在线表格 |
| `bitable`（多维表格） | ❌ 不保留 | ✅ 原件不动 | ✅ copy 副本 | ☁️ 仅云端 + 飞书链接 | 在线多维表格 |
| `slides`（幻灯片） | ❌ 不保留 | ✅ 原件不动 | ✅ copy 副本 | ☁️ 仅云端 + 飞书链接 | 在线幻灯片 |
| `mindnote`（思维导图） | ❌ 不保留 | ✅ 原件不动 | ❌ 不支持 copy | ☁️ 仅云端 + 飞书链接 | API 不支持 copy mindnote |
| `.mp4/.zip` 等大文件 | ❌ 不保留 | ✅ 原件不动 | ✅ copy 副本 | ☁️ 仅云端 + 飞书链接 | 视频/压缩包等 |
| 本地独有笔记 | ✅ 保留 | — | — | `[[wikilink]]` + 📌 仅本地 | 本地手写的笔记，飞书没有 |

**核心原则**：
- **云空间永远不动**：原始文件保留在飞书云空间原位，不移动、不删除
- **知识库放副本**：用 `drive files copy` 复制到知识库，用于结构化管理
- **本地只放 md + 图片**：Obsidian 只管理 markdown 和引用的图片
- **0-总览是索引**：所有文件（无论在哪里）都在 0-总览的文件清单中记录，☁️ 仅云端的文件附飞书链接

### 步骤 1：确认项目范围

从 TSV 和阶段二方案中确认：
- 飞书原始目录（主目录 + 关联目录）
- 目标 PARA 路径（见上表）
- 飞书知识库目标节点
- 是否有跨目录的关联文件

### 步骤 2：本地文件复制与整理

#### 2a. 逐目录确认飞书文件已下载

对照飞书云空间中的原始目录，逐个子文件夹检查：
- 该目录下的 docx 文档是否已通过 `docs +fetch` 下载为 md（保存在 `4-Archives/Notes/Feishu/` 对应路径）
- 该目录下的 doc 旧版文档是否已通过导出 API + pandoc 转为 md
- 该目录下的图片是否已通过 `docs +media-download` 下载到 `Attachments/`
- 如果有遗漏，先补充下载到 `4-Archives/Notes/Feishu/` 归档目录，再进行复制

```bash
# 列出飞书目录下的所有文件
lark-cli api GET /open-apis/drive/v1/files \
  --params '{"folder_token":"{folder_token}","page_size":"200"}' --as user

# 对比本地归档目录，确认每个 docx/doc 都有对应的 .md 文件
# 缺失的先下载：
lark-cli docs +fetch --doc {token} --as user  # docx
# 或导出 API + pandoc（doc 旧版）
```

#### 2b. 复制 md 和图片到目标目录

```bash
# 创建目标目录
mkdir -p "{目标路径}"

# 从归档目录复制 md 文件（排除 README.md）
# 从归档目录复制 Attachments（md 引用的图片）
# 从关联目录复制相关文件
# 不复制 xlsx/docx/pptx/mp4/jpeg 等非 md 文件（飞书知识库已有）
```

#### 2c. 文件整理与分类

复制完成后，对目标目录中的所有文件进行整理：

- **文件少（< 30 个）**：不建子文件夹，所有 md 平铺在根目录，在 0-总览的文件清单中按内容分类（技术文档/项目管理/演示与媒体等）
- **文件多（≥ 30 个）**：按内容分类建子文件夹（如 `项目文档/`、`运维白皮书/`、`系统对接/`），md 文件移入对应子文件夹，0-总览中的 wikilink 路径同步更新

分类参考：
| 分类 | 典型内容 |
|------|---------|
| 项目文档 | 技术要求、设计说明书、功能清单、接口规范 |
| 运维白皮书 | 运维手册、故障处理、进程清单、配置清单 |
| 系统对接 | 对接方案、堡垒机说明、GIS 注册 |
| 安全合规 | 漏洞处理、渗透测试、等保备案 |
| 工作笔记 | 进度记录、交流准备、告警规则 |
| 项目管理 | 项目汇报、施工计划、工作量评估 |
| 演示与媒体 | PPT、视频、操作手册 |
| CAD 图纸与地图 | dwg 文件、地图图片 |

### 步骤 3：飞书知识库建节点

```bash
# 项目资料知识库
SPACE_ID="7632924686837418976"
# 或业务管理知识库（2-Areas/Work/业务管理/ 下的项目用这个）
# SPACE_ID="{业务管理知识库space_id}"

# 选择父节点（根据项目状态）
PARENT="{对应父节点node_token}"

# 创建项目节点
lark-cli api POST /open-apis/wiki/v2/spaces/$SPACE_ID/nodes \
  --data '{"node_type":"origin","obj_type":"docx","title":"{项目名}","parent_node_token":"'$PARENT'"}' \
  --as user
# 记录返回的 node_token 和 obj_token
```

### 步骤 4：飞书文档复制到知识库

使用 `copy` 将云空间文档复制到知识库节点，**保持云空间原始文件不变**：

```bash
# 每个文档执行一次（docx/doc/sheet/file/bitable 都支持）
lark-cli api POST /open-apis/drive/v1/files/{文档token}/copy \
  --data '{"type":"{类型}","folder_token":"{知识库节点obj_token}","name":"{文件名}"}' \
  --as user

# 类型：docx / doc / sheet / file / bitable / slides
# 每次一个命令，避免超时
```

**原则**：
- **云空间保持不变**（原件留在原位，不移动）
- **知识库放副本**（新 token，用于结构化管理和浏览）
- 本地文档和迁移记录中记录知识库的新 token
- slides 和 bitable 也支持 copy

> ⚠️ 不要使用 `move_docs_to_wiki`！移动操作会导致云空间原始目录变空，且飞书 API 不支持从知识库移回云空间。

### 步骤 5：创建本地 0-总览.md

所有项目/业务管理目录统一使用以下模板（`1-Projects`、`4-Archives/Projects`、`2-Areas/Work/业务管理`、`4-Archives/Areas/Work/业务管理` 保持一致）：

```markdown
---
title: {项目名}
type: project
category: work
status: {维护中/已结束/进行中}
tags:
  - project/{项目名}
created: {创建日期}
modified: {最后修改日期}
---

# {项目名}

## 项目概述

**项目目标**: ...
**项目类型**: work
**状态**: {维护中/已结束/进行中}

## 飞书信息

- 任务清单：{项目名}（`{tasklist_guid}`）→ [[{路径}/1-任务|1-任务]]
- 项目群组：{项目名}（`{chat_id}`）
- 飞书知识库：[{知识库路径}](https://reliablesense.feishu.cn/wiki/{node_token})
- 飞书原始目录：[{目录名}](https://reliablesense.feishu.cn/drive/folder/{folder_token})
- 集群标识：`{cluster_id}`

## 任务总览

（仅 `1-Projects` 下的项目包含，`2-Areas` 和 `4-Archives` 下不需要）

\```tasks
filter by function \
  const t=moment(),d='day',{due:{moment:u},start:{moment:s},created:{moment:c},done:{moment:D}}=task,b=m=>m?.isSameOrBefore(t,d),q=m=>m?.isSame(t,d); \
  return !!(!task.isDone?!u||b(u)||b(s)||q(c):D?.isAfter(moment().subtract(3,d),d)||false);
path includes {当前目录路径}
tags include #task/
...
\```

## 文件清单

### {分类1}

| 文件 | 类型 | 飞书链接 | 说明 |
|------|------|---------|------|
| [[文件名]] | docx | [飞书](url) | 说明 |
| 附件名.docx | file | [飞书](url) | ☁️ 仅云端 |

### {分类2}
...

> 📌 仅本地 = 飞书知识库没有　☁️ 仅云端 = 飞书知识库有，本地不保留非 md 文件

## 项目日志

\```dataview
LIST L.text + choice(length(L.children) > 0, "<br>" + join(map(L.children, (c) => "　　- " + c.text), "<br>"), "")
FROM "0-Daily"
FLATTEN file.lists AS L
WHERE (contains(L.text, "{项目名}") OR contains(L.tags, "#project/{项目名}")) AND !L.parent
SORT file.name DESC
LIMIT 20
\```
```

**模板说明**：
- `飞书信息` 部分：非工作项目（Personal）可省略；`2-Areas` 和 `4-Archives` 下的项目按实际情况填写
- `任务总览`：仅 `1-Projects` 下的项目包含（有 `1-任务.md` 的项目）
- `文件清单`：按内容分类（技术文档/项目管理/演示与媒体等），不按文件格式
- `项目日志`：所有项目统一包含
- md 文件用 `[[wikilink]]`，非 md 文件直接写文件名
- ☁️ 仅云端 = 飞书有、本地不保留
- 📌 仅本地 = 本地有、飞书没有
- 无标记 = 双端都有
- 文件少于 30 个时平铺不建子文件夹，超过 30 个再考虑

### 步骤 6：写入飞书父节点文档

将总览内容写入飞书知识库的项目节点文档，链接使用 `<mention-doc>` 格式实现飞书内部跳转：

```bash
# 准备飞书版 markdown（去掉 frontmatter 和 wikilink，链接改为 mention-doc）
# 链接格式：<mention-doc token="{node_token}" type="wiki">文档标题</mention-doc>
# 仅本地的文件不加 mention-doc，直接写文件名

cat feishu_overview.md | lark-cli docs +update \
  --doc {obj_token} --markdown - --mode overwrite --as user
```

**飞书版与本地版的区别**：
- 去掉 YAML frontmatter
- `[[wikilink]]` → `<mention-doc token="..." type="wiki">标题</mention-doc>`
- 去掉"飞书链接"列，文件名本身就是 mention-doc 链接
- 仅本地的文件保留文字，不加链接

### 步骤 7：全面检查

提交前做三方一致性检查，确保本地、总览、飞书三端一致：

**7a. 检查原始目录文件是否都已复制**

对照飞书云空间原始目录，逐个子目录确认：
- 每个 docx/doc 文件 → 本地有对应的 .md
- 每个 file 类型 .docx/.xlsx/.pptx/.pdf → 本地有（按同步策略）
- 每个 sheet/bitable/slides → 本地不保留，但总览中有记录
- 每个子目录 → 本地有对应目录（如果需要）

**7b. 检查本地文件、总览、飞书知识库三方一致**

| 检查项 | 规则 |
|--------|------|
| 本地有的目录 | 总览中必须有对应的章节标题 |
| 本地没有的文件 | 总览中按内容分组，标记 ☁️ 仅云端 |
| 总览中的每个文件 | 飞书知识库中有对应节点（或标记为仅本地/仅云端） |
| 飞书知识库节点结构 | 与总览的章节结构一致 |
| 文件清单 | 只记录本地有的和知识库有的文件，不记录只在云空间原始目录中的文件 |

**7c. 不一致则修复**

- 本地缺文件 → 回到步骤 2 补下载
- 总览缺记录 → 补充到总览
- 知识库缺节点 → 用 copy 补充（不要用 move）
- 知识库有重复 → 在飞书网页端手动删除多余节点

### 步骤 8：提交推送

```bash
git add "{目标路径}/"
git commit -m "阶段二迁移：{项目名}（{状态}）"
git push
```

### 关键 token 速查

| 知识库 | space_id | 用途 |
|--------|----------|------|
| 项目资料 | `7632924686837418976` | `1-Projects/Work/` 和 `4-Archives/Projects/Work/` |
| 业务管理 | `7634233277791865798` | `2-Areas/Work/业务管理/` 和 `4-Archives/Areas/Work/业务管理/` |

| 节点 | node_token | 用途 |
|------|-----------|------|
| 归档项目 | `PhpuwDqUvidfKRkUXMKcLMJ0nHc` | 已结束项目的父节点 |
| 百度水厂 | `HVnAwfonxibx3Fk2O3vcDqt5nXb` | 第一个迁移完成的项目（模板参考） |

### 迁移教训（2026-04-27 广州机场还原 + 2026-04-30 百度水厂总结）

1. **不要用 `move_docs_to_wiki`**：飞书 API 不支持从知识库移回云空间，一旦移入就无法通过 API 移回。
2. **不要用 `wiki move` 调整知识库结构**：知识库节点无法通过 API 删除，反复移动会产生混乱。一旦节点位置确定就不要再动。
3. **用 `copy` 代替 `move`**：`drive files copy` 可以把文件复制到任意位置，保持原件不变。
4. **云空间保持不变**：原始文件留在云空间原位，知识库放副本用于结构化管理。
5. **先规划再执行**：先确定本地目录结构和总览分组，再一次性创建知识库节点结构并 copy 文件，不要边做边调整。
6. **知识库节点无法通过 API 删除**：只能在飞书网页端手动删除。操作前要确认结构正确，避免产生重复节点。
7. **总览结构规则**：
   - 本地有的目录 → 总览中必须有对应的章节标题
   - 本地没有的目录 → 总览中可以按内容分组
   - 飞书知识库节点结构与总览章节一致
   - 文件清单只记录本地有的和知识库有的文件，不记录只在云空间原始目录中的文件

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

#### 赛力斯 → `1-Projects/Work/赛力斯定位/`

| 文件 | 类型 | 飞书链接 | 目标路径 |
|------|------|---------|---------|
| 数字化循环载具管理平台统一接口协议V1.4 | docx | [飞书](https://reliablesense.feishu.cn/docx/Af4wdLHdhoaaeJxzscucmKyQnEf) | `1-Projects/Work/赛力斯定位/` |
| 设备相关资料 | docx | [飞书](https://reliablesense.feishu.cn/docx/Vw2ZdVXLloMFarxu7BscvzlxnKb) | `1-Projects/Work/赛力斯定位/` |

#### 博实结 → `2-Areas/Work/设备管理/博实结GPS/`

| 文件 | 类型 | 飞书链接 | 目标路径 |
|------|------|---------|---------|
| 智能硬件定位服务（2024-07-12） | docx | [飞书](https://reliablesense.feishu.cn/docx/Z2DKdMZxBoDiiKxyXtUch3d6nFc) | `2-Areas/Work/设备管理/博实结GPS/` |
| EG10E部标协议 | docx | [飞书](https://reliablesense.feishu.cn/docx/EV9gdgpxdoguXbxvhTjc8rVSn2d) | `2-Areas/Work/设备管理/博实结GPS/` |
| EG10E产品使用说明书(4) | docx | [飞书](https://reliablesense.feishu.cn/docx/GuqpdulGkoBsZUxm10pc1PwWnld) | `2-Areas/Work/设备管理/博实结GPS/` |
| 联调记录 | docx | [飞书](https://reliablesense.feishu.cn/docx/MzxSduc4soHPCZxY1aTcta0Dnfe) | `2-Areas/Work/设备管理/博实结GPS/` |

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
| NFC读卡器接口配置文档 | docx | [飞书](https://reliablesense.feishu.cn/docx/BYIudCklRoDYMixFu6Xc9HA9n1d) | `1-Projects/Work/新太定位/` | 新太定位NFC |

### 后端架构（有价值的技术文档）

| 文件 | 类型 | 飞书链接 | 目标路径 | 理由 |
|------|------|---------|---------|------|
| LBS系统梳理 | docx | [飞书](https://reliablesense.feishu.cn/docx/B6SgdFSRaoPqd7xQoTOcZGMAncd) | `2-Areas/Work/产品研发/` | 后端架构文档 |
| RS-LBS后端平台架构重构方案(v2.0.0) | docx | [飞书](https://reliablesense.feishu.cn/docx/WctjdFkvSoAIJ8x3t1scyrXVnXc) | `2-Areas/Work/产品研发/` | 后端架构 |
| RS-MID中间件平台架构方案(v1.0.0) | docx | [飞书](https://reliablesense.feishu.cn/docx/PYwpd0PL3owk84xKLsNcQCy8nmh) | `2-Areas/Work/产品研发/` | 中间件架构 |
| Zone + tile38功能实现备忘 | docx | [飞书](https://reliablesense.feishu.cn/docx/QI0SdzgAsol9SKxEh2wcWOkJnZc) | `2-Areas/Work/产品研发/` | 平台功能备忘 |
| position重构 | mindnote | [飞书](https://reliablesense.feishu.cn/mindnotes/YbkQbIQOsmcou8nM7aTcupE8n0d) | 留归档 | mindnote保留链接 |

### 测试/压测

| 文件 | 类型 | 飞书链接 | 目标路径 | 理由 |
|------|------|---------|---------|------|
| 230环境 | docx | [飞书](https://reliablesense.feishu.cn/docx/MUo8dYBWXoBwpBxdHfTcV2UJnag) | `2-Areas/Work/运维管理/` | 压测环境配置 |
| 压测备忘录 | docx | [飞书](https://reliablesense.feishu.cn/docx/TEUJd4UxnocvIIxgsy3cA58qn9g) | `2-Areas/Work/产品研发/` | 压测操作 |
| 标签数量压测数据统计_3.0 | sheet | [飞书](https://reliablesense.feishu.cn/sheets/BuXPsjDGhhwrAKtNlX8c8vttnPx) | `2-Areas/Work/产品研发/` | 最新版压测数据 |
| 标签数量压测数据统计_2.0 | sheet | [飞书](https://reliablesense.feishu.cn/sheets/P6SJsvzAOhu9RvtlnQtc3P4snkf) | `4-Archives/Areas/Work/团队管理/团队成员/王宗光/` | 旧版本压测 |
| 标签数量压测数据统计_1.0 | sheet | [飞书](https://reliablesense.feishu.cn/sheets/QGicsCeb2hEFrAtSqK6cfsBkn0d) | `4-Archives/Areas/Work/团队管理/团队成员/王宗光/` | 旧版本压测 |
| 获取规划路线接口性能测试 | sheet | [飞书](https://reliablesense.feishu.cn/sheets/QaM9sFjaihS6dotCVfgcEk48n2g) | `2-Areas/Work/产品研发/` | 路网性能测试 |

### 散落文档

| 文件 | 类型 | 飞书链接 | 决策 | 目标路径 | 理由 |
|------|------|---------|------|---------|------|
| E-Ink平台安装和使用手册 | docx | [飞书](https://reliablesense.feishu.cn/docx/BTKgdqfbXowNV5x0DSfcfafpncY) | → 提取 | `2-Areas/Work/设备管理/` | 墨水屏手册 |
| 智慧工厂电子标牌管理系统软件v1.0.0-json格式 | docx | [飞书](https://reliablesense.feishu.cn/docx/TYe7doOyNovyfLxfXOScJ2vyngf) | → 提取 | `2-Areas/Work/设备管理/阿法迪蓝牙墨水屏/` | 电子标牌系统 |
| 日志说明 | docx | [飞书](https://reliablesense.feishu.cn/docx/BdUEdhqBIofw1YxY2nGc8jEfn7d) | → 提取 | `2-Areas/Work/产品研发/` | 产品日志说明 |
| 莱讯-移动端需求 | docx | [飞书](https://reliablesense.feishu.cn/docx/U1EedFUBmoNwPQxD9oHcWweanXc) | → 提取 | `2-Areas/Work/产品研发/` | 移动端需求 |
| 无动力设备信息融合系统-源代码 | docx | [飞书](https://reliablesense.feishu.cn/docx/doxcnWD87qgPTeUnEIrenFMqHYf) | → 归档 | `4-Archives/Projects/Work/无动力设备管理/` | 无动力设备系统 |
| 交接文档 | docx | [飞书](https://reliablesense.feishu.cn/docx/UOvmd7dz4oFkXVxuq3OczvtrnHf) | → 归档 | `4-Archives/Areas/Work/团队管理/团队成员/王宗光/` | 王宗光交接文档 |
| 问题处理记录/工作记录 | docx | [飞书](https://reliablesense.feishu.cn/docx/LHvPda1imoHU2Jxj4SncmovqnRf) | → 提取 | `2-Areas/Work/产品研发/` | 产品问题处理记录 |
| 用户敏感信息处理.md | file | [飞书](https://reliablesense.feishu.cn/file/N4wvbKBhfoKdLMxIlQRckQAlnpd) | → 提取 | `2-Areas/Work/产品研发/` | 产品敏感信息处理 |
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
| 三方系统调用行李查询接口文档(座位号)20230804 | docx | [飞书](https://reliablesense.feishu.cn/docx/E3UidCx5No6qqnx2VgjcXVzdnsg) | → 归档 | `4-Archives/Projects/Work/武汉机场/` | 武汉机场行李查询接口 |
| 平台地图最新使用 | docx | [飞书](https://reliablesense.feishu.cn/docx/QbGcdI4iDok1XPxFdEUckHemnR5) | → 提取 | `2-Areas/Work/产品研发/` | 产品地图使用文档 |
| 小程序签到功能方案 | docx | [飞书](https://reliablesense.feishu.cn/docx/GxYfddex4oDcpUxG0JHcGbZEndg) | → 提取 | `2-Areas/Work/产品研发/` | 小程序签到方案 |
| 大屏页面问题 | docx | [飞书](https://reliablesense.feishu.cn/docx/OVEnde4fhoJnAPxjgr9c2WZfnIc) | → 提取 | `2-Areas/Work/产品研发/` | 产品大屏问题 |
| 流程图 | docx | [飞书](https://reliablesense.feishu.cn/docx/BWGKd2466omTdxxjRQdciMNknyh) | → 提取 | `4-Archives/Areas/Work/团队管理/团队成员/陈子杰/` | 产品流程图 |
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
| saas英文版 | docx | [飞书](https://reliablesense.feishu.cn/docx/LZgYdpRnzouGpKxnOdZc4vDRnPg) | → 提取 | `2-Areas/Work/产品研发/saas英文版.md` | SaaS英文文档 |
| SaaS使用手册V4 new 英文.docx | file | [飞书](https://reliablesense.feishu.cn/file/boxcnrTNYMWwqMq49WzzapEj30g) | → 提取 | `2-Areas/Work/产品研发/SaaS使用手册V4-英文.docx` | SaaS英文手册 |
| SaaS使用手册V4 new.docx | file | [飞书](https://reliablesense.feishu.cn/file/boxcnKrzYX5prPEiZIv33AL6mlc) | → 提取 | `2-Areas/Work/产品研发/SaaS使用手册V4.docx` | SaaS中文手册 |
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
| 李家豪轨迹室内异常.png | file | [飞书](https://reliablesense.feishu.cn/file/NYJ9b9PpRo1IgMxmAvgcjaYZnMh) | → 归档 | `1-Projects/Work/麦钉定位/` | 麦钉定位截图 |
| 韩家村统计时长缺失.png | file | [飞书](https://reliablesense.feishu.cn/file/B5bHb0v8goCfnZxMCD4cyJvjnn9) | → 归档 | `1-Projects/Work/麦钉定位/` | 麦钉定位截图 |
| 教学比赛.mov | file | [飞书](https://reliablesense.feishu.cn/file/AUT0b1zsdo1SQdxXCgHc9epunIf) | 留归档 | - | 个人文件 |
| 宏兴裁切.rar | file | [飞书](https://reliablesense.feishu.cn/file/P5MBb8Cy6oYsYfx3MZjc8BhonCd) | → 归档 | `1-Projects/Work/洛阳化工厂/` | 洛阳项目文件 |
| FRP_GithubArm64_version_1_3_6.apk | file | [飞书](https://reliablesense.feishu.cn/file/YMF3bIlvFoTvxaxPI6IcKLwMnNc) | 留归档 | - | 安装包 |
| 定位平台安装文件及文档.zip | file | [飞书](https://reliablesense.feishu.cn/file/Hr8bbKyRUoKdDtxgtLhcfDCknug) | 留归档 | - | 安装包 |
| madinat_hjc.zip | file | [飞书](https://reliablesense.feishu.cn/file/UnIjb9C7qocVGExPTZpc9wkAnog) | → 归档 | `1-Projects/Work/麦钉定位/` | 麦钉定位数据包 |
| 转化后数据.zip | file | [飞书](https://reliablesense.feishu.cn/file/NXVgbTKQioF6Kkx26yScwwRbnjg) | → 归档 | `1-Projects/Work/麦钉定位/` | 麦钉定位数据 |

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

### ~参考资料

`~参考资料/` 下内容按类型分别处理：

#### 自家产品素材（→ 提取）

| 文件 | 飞书链接 | 目标路径 |
|------|---------|---------|
| 莱讯宣传单页素材/（10 个 png） | [飞书目录](https://reliablesense.feishu.cn/drive/folder/fldcnpp8JeCmpzMuPLsbsIczAif) | `2-Areas/Work/品牌宣传/宣传单页素材/` |
| 图片资料/功能截图.docx | [飞书](https://reliablesense.feishu.cn/file/boxcn4GHkkPu2XBcBBSwcJ1kXqd) | `2-Areas/Work/产品研发/功能截图.docx` |
| 图片资料/移动端小程序图片/（14 个 png） | [飞书目录](https://reliablesense.feishu.cn/drive/folder/fldcnpp8JeCmpzMuPLsbsIczAif) | `2-Areas/Work/产品研发/移动端小程序截图/` |

#### 竞品/外部资料（已确认 2026-04-22）

| 文件 | 飞书链接 | 决策 | 目标路径 |
|------|---------|------|---------|
| 其他资料/C122高精度定位系统.docx | [飞书](https://reliablesense.feishu.cn/file/boxcn3mtxYM6vHAX78XBUOH7NNb) | → 提取 | `1-Projects/Work/广州机场/C122高精度定位系统技术方案.docx` |
| 其他资料/中弈科技智慧矿山.pptx | [飞书](https://reliablesense.feishu.cn/file/boxcnNFpbk35EFKXYin3ov4deQe) | → 提取 | `4-Archives/Areas/Work/业务管理/中弈科技智慧矿山/中弈科技智慧矿山.pptx` |
| 其他资料/叉车安全管理产品.pdf | [飞书](https://reliablesense.feishu.cn/file/boxcn7MB73uMU8yx6oYLo1bXCbe) | → 提取 | `2-Areas/Work/设备管理/合作企业/唯创安全/叉车安全管理产品.pdf` |
| 其他资料/防撞预警系统.pptx | [飞书](https://reliablesense.feishu.cn/file/boxcnlgd76R50T1K97lNvr2xOVh) | → 提取 | `2-Areas/Work/设备管理/合作企业/唯创安全/防撞预警系统.pptx` |
| 易景空间路演ppt.pdf | [飞书](https://reliablesense.feishu.cn/file/WQH1bQdUPoMOKTxB71PcLcQznCd) | → 提取 | `2-Areas/Work/设备管理/合作企业/易景空间/易景空间路演ppt.pdf` |

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
| 需人工判断 | ~55 | 边界模糊的条目，详见待确认分类文件 |
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

## 十九、项目清单

### 进行中项目（→ `1-Projects/Work/`）

| 项目名 | 飞书来源目录 | 飞书链接 | 目标路径 | 关键字 |
|--------|------------|---------|---------|--------|
| 广州机场 | 004. 广州机场-综合定位 + 005. 移动应用平台 | [飞书](https://reliablesense.feishu.cn/drive/folder/MrIOflncTlWrkEd4hJZcUxatncd) [飞书](https://reliablesense.feishu.cn/drive/folder/DZVbfWCNnl1IaudvPBpcpXjenQf) | `1-Projects/Work/广州机场/` | `综合定位`, `A域/B域`, `巡检app`, `AESB`, `TCDM`, `gjtsg`, `shwl_gzhft` |
| 新太定位 | 998. 售后项目/内蒙新太元铬业 | [飞书](https://reliablesense.feishu.cn/drive/folder/IGJBfaqbJljC6adrtbCcumrrnCf) | `1-Projects/Work/新太定位/` | `新太`, `新钢联`, `料棚`, `卸料`, `上料`, `铲车`, `堆垛`, `xintai` |
| 上港仓储管理 | 002. 上海上港 | [飞书](https://reliablesense.feishu.cn/drive/folder/IwSpfxmL5lfpO8dLuoccbdnLnre) | `1-Projects/Work/上港仓储管理/` | `上港`, `仓储`, `出入库`, `RFID`, `shwl_shsg` |
| 洛阳化工厂 | 998. 售后项目/麦钉洛阳石化 | [飞书](https://reliablesense.feishu.cn/drive/folder/S3JWftxHWl14R5dz9FncpUPUnsd) | `1-Projects/Work/洛阳化工厂/` | `洛阳`, `石化`, `化工`, `宏兴`, `lyrydw`, `lyhx` |
| 南宁机场 | 南宁机场项目 | [飞书](https://reliablesense.feishu.cn/drive/folder/JuNOf2llHlkIa9dKw73cJm5pn3w) | `1-Projects/Work/南宁机场/` | `南宁机场` |
| 麦钉定位 | 998. 售后项目/麦钉 + 红柳林/韩家村/柠条塔/李家壕等 | [飞书](https://reliablesense.feishu.cn/drive/folder/RTvgfEDMZlvXcod1aQScqUCdnXb) | `1-Projects/Work/麦钉定位/` | `红柳林`, `李家壕`, `韩家村`, `高安屯`, `柠条塔`, `孝感`, `恩菲`, `固废`, `污水处理`, `地磁`, `madinat_hll`, `madinat_xmc`, `madinat_hjc`, `madinat_gat`, `madinat_ntt` |
| 赛峰定位 | 998. 售后项目/赛峰 | | `1-Projects/Work/赛峰定位/` | `赛峰`, `SAML`, `SSO`, `CLE`, `墨水屏` |

### 已结束项目（→ `4-Archives/Projects/Work/`）

> **归档方式说明**：
> - 📁 Project = `4-Archives/Projects/Work/{项目名}/`（独立归档项目）
> - 📋 归档业务管理 = `4-Archives/Areas/Work/业务管理/{项目名}/`（文件少、无独立项目价值的售前/小项目资料）
> - 归入xxx = 合并到其他项目目录
>
> **归属判断标准**（2026-04-22 飞书 API 验证）：飞书文档最后更新日期在 2026 年之前 → `4-Archives/`，2026 年及之后 → `2-Areas/`。经查 38 个项目全部在 2026 年之前更新，全部归档。

#### 998. 售后项目

> 归入进行中项目：李家壕洗煤厂(183)、红柳林洗煤厂(51)、韩家村洗煤厂(50)、柠条塔(19) → 麦钉定位；内蒙新太元铬业(182) → 新太定位；麦钉洛阳石化(14) → 洛阳化工厂；麦钉(7) → 麦钉定位

| 项目名 | 飞书来源目录 | 飞书链接 | 文件数 | 归档方式 | 关键字 |
|--------|------------|---------|--------|---------|--------|
| 众合人员管理 | 众合Demo环境--杭州地铁定位应用 | [飞书](https://reliablesense.feishu.cn/drive/folder/fldcn9ihucqqZa3fG3Px0Gloixc) | 148 | 📁 Project | `众合`, `杭州地铁`, `Demo环境` |
| 博世定位 | Bosch 项目 | [飞书](https://reliablesense.feishu.cn/drive/folder/P4GJfXpDolZ4EodGUF9cUCBonkc) | 105 | 📁 Project | `Bosch`, `博世` |
| 国核智慧工地 | 国和一号（威海） | [飞书](https://reliablesense.feishu.cn/drive/folder/fldcnKTgV6OtJkwR2ijJyY5rVsc) | 84 | 📁 Project | `国和一号`, `威海`, `国核`, `智慧工地` |
| 海尔工厂 | 海尔工厂 | [飞书](https://reliablesense.feishu.cn/drive/folder/fldcn9yq74Lu525sk4tf7ayUr0c) | 72 | 📁 Project | `海尔` |
| 供电局库位 | 供电局库位定位 | [飞书](https://reliablesense.feishu.cn/drive/folder/fldcnhoSboKetpXvMBzbKRSmGAb) | 63 | 📁 Project | `供电局`, `库位定位` |
| 百度水厂 | 百度-水厂定位导航平台 | [飞书](https://reliablesense.feishu.cn/drive/folder/PtrXfLdAglTcVXd6tvlcIUqBnDd) | 56 | 📁 Project | `百度`, `水厂` |
| 联通定位一体化 | 联通室内外一体化 | [飞书](https://reliablesense.feishu.cn/drive/folder/fldcnlVHJxmUEdxDWjt8LvVcTjc) | 54 | 📁 Project | `联通`, `室内外一体化` |
| 兰州机场 | 兰州机场 | [飞书](https://reliablesense.feishu.cn/drive/folder/fldcn42BLWazsHzYslg6A34LLCd) | 49 | 📁 Project | `兰州机场` |
| 国家电网 | 北京技新科技有限公司（国家电网） | [飞书](https://reliablesense.feishu.cn/drive/folder/fldcnfcM9BxoadzLHM41eJujMUh) | 42 | 归入电网智能仓库 | `国家电网`, `技新` |
| 武汉机场 | 武汉机场 | [飞书](https://reliablesense.feishu.cn/drive/folder/fldcnHmHajD7TQATmdiqbTIuGRe) | 38 | 📁 Project | `武汉机场` |
| 启程科技加气站 | 加气站-北京时代启程物联科技有限公司 | [飞书](https://reliablesense.feishu.cn/drive/folder/fldcnoreuJsFnFpBJ6rVWisEtWc) | 32 | 📁 Project | `加气站`, `时代启程` |
| 山东国核 | 山东国核 | [飞书](https://reliablesense.feishu.cn/drive/folder/fldcnDKqBIiko7la9mEC6iWzlHf) | 28 | 归入国核智慧工地 | `山东国核` |
| 数讯云人员服务系统 | IDC | [飞书](https://reliablesense.feishu.cn/drive/folder/fldcnnpIG8G9K1vU3IH1XexyQpb) | 26 | 📁 Project | `数讯`, `IDC`, `数据中心` |
| 北京GE | 北京GE | [飞书](https://reliablesense.feishu.cn/drive/folder/VL31fp5utl2g59dU3CbcBV1Onkc) | 21 | 📁 Project | `GE`, `北京GE` |
| 松下LED灯 | 松下照明 | [飞书](https://reliablesense.feishu.cn/drive/folder/fldcnvFOcvpYap90lcIGxwbRTVf) | 19 | 📁 Project | `松下照明`, `松下`, `LED` |
| 孝感污水处理 | 孝感污水处理 | [飞书](https://reliablesense.feishu.cn/drive/folder/fldcnzHlG6xjy4ECXtD2za7G62e) | 19 | 归入麦钉定位 | `孝感`, `污水处理` |
| 合众思壮 | 合众思壮 | [飞书](https://reliablesense.feishu.cn/drive/folder/KS3BfWiA0lszPFdzHPHcltflnre) | 18 | 归入设备管理 | `合众思壮`, `GPS` |
| 康利达定位 | 广东康利达物联科技有限公司 | [飞书](https://reliablesense.feishu.cn/drive/folder/fldcnPZ5u2pC8jXrwCWYmW0zKsN) | 16 | 📋 归档业务管理 | `康利达` |
| 天津眼科医院 | 天津眼科医院 | [飞书](https://reliablesense.feishu.cn/drive/folder/fldcn4LNTqNz05fkkDD51VReUoh) | 16 | 📁 Project | `天津眼科` |
| 内蒙古洗煤厂 | 内蒙古洗煤厂的煤棚 | [飞书](https://reliablesense.feishu.cn/drive/folder/fldcn0XgPdqYb7z218keyA7wyhd) | 15 | 归入麦钉定位 | `内蒙古洗煤厂`, `煤棚` |
| 电子价签管理 | 电子价签管理项目（Bossard） | [飞书](https://reliablesense.feishu.cn/drive/folder/E3NmfOQ5Pl5w9wdaRkjcEAvHntf) | 14 | 📁 Project | `电子价签`, `Bossard` |
| 地磁 | 地磁 | | 13 | 归入麦钉定位 | `地磁` |
| 众合科技 | 众合科技 | [飞书](https://reliablesense.feishu.cn/drive/folder/fldcndJIt8gCWm2aGkk20nLuU3d) | 13 | 归入众合人员管理 | `众合科技` |
| 电网智能仓库 | 南方电网 - 智能仓库项目 | [飞书](https://reliablesense.feishu.cn/drive/folder/fldcnFfYXhVMbffAXURuPEYFZHg) | 12 | 📁 Project | `南方电网`, `智能仓库`, `国家电网`, `技新`, `广西电网` |
| 广西电网 | 广西电网项目 | [飞书](https://reliablesense.feishu.cn/drive/folder/fldcndXOeB44cYlW012D2C05Hcf) | 8 | 📋 归档业务管理 | `广西电网` |
| 国家图书馆 | 国家图书馆 | [飞书](https://reliablesense.feishu.cn/drive/folder/fldcn6yxWW1ngHsX0GkzZZdVkEc) | 8 | 📁 Project | `国家图书馆` |
| 厦门医院 | 厦门医院项目 | [飞书](https://reliablesense.feishu.cn/drive/folder/fldcnH7FhGrBf94gG9RsIrIa8Zg) | 5 | 📋 归档业务管理 | `厦门医院` |
| 无动力设备信息融合 | 机场-无动力设备信息融合系统 | [飞书](https://reliablesense.feishu.cn/drive/folder/fldcnByfvqKI5s5vK8WVniVvNMe) | 4 | 📋 归档业务管理 | `无动力设备`, `信息融合` |
| 核电站 | 核电站项目 | [飞书](https://reliablesense.feishu.cn/drive/folder/fldcneAiPn70Fw4xDazm6L26llg) | 3 | 归入中广核电厂 | `核电站` |
| 宏兴新能 | 宏兴新能人员定位管理系统 | [飞书](https://reliablesense.feishu.cn/drive/folder/BKYCfWVwOlXZRpdgjpscVhannlc) | 3 | 归入洛阳化工厂 | `宏兴新能` |
| 上海易同科技 | 上海易同科技 | [飞书](https://reliablesense.feishu.cn/drive/folder/fldcn8pIA6ElregB1Fggx07tGKg) | 3 | 📋 归档业务管理 | `易同` |
| 清华大学 | 清华大学 | [飞书](https://reliablesense.feishu.cn/drive/folder/fldcnpJzwab38BtPYZAFQgcicrf) | 2 | 📋 归档业务管理 | `清华大学` |
| 振华项目 | 振华项目 | [飞书](https://reliablesense.feishu.cn/drive/folder/S9lCfVWTwlUyORda8c5cb3BGnsb) | 2 | 📋 归档业务管理 | `振华` |
| 恩菲固废（孝感） | 恩菲固废(孝感)项目 | [飞书](https://reliablesense.feishu.cn/drive/folder/fldcnbKqOCYwFonGRakDFNNiXIc) | 2 | 归入麦钉定位 | `恩菲`, `固废` |
| 威海核电 | 威海核电项目 | [飞书](https://reliablesense.feishu.cn/drive/folder/CxMIfqTrnlwHNcd2Spmc5KEinnh) | 2 | 归入国核智慧工地 | `威海核电` |
| 天津医科大学总医院 | 天津医科大学总医院 | [飞书](https://reliablesense.feishu.cn/drive/folder/fldcnIVDi2da6SfdGwkyejbPZ1g) | 1 | 📋 归档业务管理 | `天津医科大学` |

#### 003. 中东电子厂

| 项目名 | 飞书来源目录 | 飞书链接 | 归档方式 | 关键字 |
|--------|------------|---------|---------|--------|
| 中东电子厂 | 003. 中东电子厂客户 | [飞书](https://reliablesense.feishu.cn/drive/folder/UF9cfyxN7lnWIwd02auc28fFnOg) | 📁 Project | `中东电子厂`, `伊朗`, `波斯语` |

#### 其他已结束项目

| 项目名 | 飞书来源目录 | 飞书链接 | 归档方式 | 关键字 |
|--------|------------|---------|---------|--------|
| 中联核信 | 中联核信 | [飞书](https://reliablesense.feishu.cn/drive/folder/LaOOfNGfBlvZqOdTmgtcRQzxnJc) | 📁 Project | `中联核信`, `核信` |
| 红点定位 | 红点定位 | [飞书](https://reliablesense.feishu.cn/docx/YBASdNrzWo8e9ExCrZYcdClTnfg) | 归入设备管理 | `红点定位`, `redpoint` |
| 嘉盛工厂 | 王宗光/项目资料/嘉盛工厂 | [飞书](https://reliablesense.feishu.cn/drive/folder/Q4jDfQS0alQqv2d0LjWcSR6rnVd) | 📁 Project | `嘉盛` |
| 博实结 | 王宗光/项目资料/博实结 | [飞书](https://reliablesense.feishu.cn/drive/folder/BudrfapCnl9fLkd8Rl3cXhwjnve) | 归入设备管理 | `博实结`, `EG10E` |
| 哒咔定位 | （画板文档） | | 归入报价记录 | `哒咖` |

#### 999. 归档项目

| 项目名 | 飞书链接 | 文件数 | 归档方式 | 关键字 |
|--------|---------|--------|---------|--------|
| 长沙酒店 | [飞书](https://reliablesense.feishu.cn/drive/folder/fldcnYRwI8knNNUXUtof87Fyajb) | 96 | 📁 Project | `长沙酒店`, `酒店样板` |
| 民生物流 | [飞书](https://reliablesense.feishu.cn/drive/folder/R07Dfa4FIlnT58dO8eWcFJ7WnXc) | 79 | 📁 Project | `民生物流` |
| 可口可乐叉车定位 | [飞书](https://reliablesense.feishu.cn/drive/folder/fldcn0qXGrnl4W8rKS5z6C6uilc) | 49 | 📁 Project | `中粮`, `可口可乐` |
| 二手车管理 | [飞书](https://reliablesense.feishu.cn/drive/folder/fldcnu9ueOQWmpUM4axmkmYh7mf) | 44 | 📁 Project | `二手车`, `车辆管理` |
| 苏州KIT | [飞书](https://reliablesense.feishu.cn/drive/folder/WWclfhyFulfuTYdxFAWcYvc4nLe) | 31 | 📁 Project | `KIT`, `苏州展会` |
| 丰田叉车 | [飞书](https://reliablesense.feishu.cn/drive/folder/fldcnoZ28nWI3HHes9jTUz2hcGe) | 31 | 📁 Project | `叉车定位`, `丰田` |
| 泰康养老院 | [飞书](https://reliablesense.feishu.cn/drive/folder/fldcn7OgGvIC4ToMxhxVQBS3Srh) | 23 | 📁 Project | `泰康`, `养老院` |
| 中远海运 | [飞书](https://reliablesense.feishu.cn/drive/folder/Bnp4fUMeol0U1xdisfTcqv2xnCd) | 16 | 📁 Project | `中远` |
| 业睿展厅 | [飞书](https://reliablesense.feishu.cn/drive/folder/fldcnO0LHPDLthNOwEOzl87p3bg) | 15 | 📁 Project | `业睿` |
| 中科海微 | [飞书](https://reliablesense.feishu.cn/drive/folder/fldcnDM4BkLZD0CfnzKBQZte1Og) | 11 | 📁 Project | `中科海微` |
| 扬州群鑫 | [飞书](https://reliablesense.feishu.cn/drive/folder/FEzCf5OfWlFFZgdDptVcgBiYnQh) | 10 | 📁 Project | `扬州群鑫`, `群鑫` |
| 运输机大屏 | [飞书](https://reliablesense.feishu.cn/drive/folder/Uh1Nfl3eml9Nq1d3jhAc1kJ8nWg) | 9 | 📋 归档业务管理 | `运输机`, `场景大屏` |
| 南通精机 | [飞书](https://reliablesense.feishu.cn/drive/folder/MOK6fhlmalZiZGdMGHbcPdHgnjf) | 8 | 📋 归档业务管理 | `南通`, `丝路咖`, `精机` |
| 中软护理院 | [飞书](https://reliablesense.feishu.cn/drive/folder/EE6nf30qtlkLzwdOkkmcLfHanGf) | 7 | 📋 归档业务管理 | `中软国际`, `护理院` |
| 胶州湾 | [飞书](https://reliablesense.feishu.cn/drive/folder/fldcn03OeBw3cqEZQLPCLDKMsUe) | 5 | 📋 归档业务管理 | `胶州湾` |
| 中奕信息 | [飞书](https://reliablesense.feishu.cn/drive/folder/fldcnGYdaFxc8EybWdmNf25npwc) | 5 | 📋 归档业务管理 | `中奕` |
| 天津展厅 | [飞书](https://reliablesense.feishu.cn/drive/folder/fldcniIKrxUSjvz71AJ07dL5Rhz) | 4 | 📋 归档业务管理 | `天津展厅` |
| 创源微致 | [飞书](https://reliablesense.feishu.cn/drive/folder/UirYfKFX2lIwo0daKshcMCOyn0b) | 4 | 📋 归档业务管理 | `创源微致` |
| 济南炼化厂 | [飞书](https://reliablesense.feishu.cn/drive/folder/fldcnW80ZP3Pl2In77nNl3YVSye) | 3 | 📋 归档业务管理 | `济南炼化` |
| 捷普工厂 | [飞书](https://reliablesense.feishu.cn/drive/folder/fldcnly6jvJUH3XExdT0Fnr0OOe) | 3 | 📋 归档业务管理 | `捷普` |
| 地铁停车场 | [飞书](https://reliablesense.feishu.cn/drive/folder/fldcnWzRLVtF16uOX9MP92WGz6e) | 3 | 📋 归档业务管理 | `地铁停车场` |
| 苏州美的 | [飞书](https://reliablesense.feishu.cn/drive/folder/GLRUfUaRKlwsaJdpq6IcNENBn6c) | 2 | 📋 归档业务管理 | `苏州美的` |
| 船只定位 | [飞书](https://reliablesense.feishu.cn/drive/folder/fldcnp91z9Kb0b3Oz9k8SxYL7Mh) | 2 | 📋 归档业务管理 | `船只定位` |
| 深圳物联AIoT | [飞书](https://reliablesense.feishu.cn/drive/folder/fldcnqBKqbikUuASzpKbKOzAgEN) | 2 | 📋 归档业务管理 | `深圳物联`, `AIoT` |
| 宝冶钢厂 | [飞书](https://reliablesense.feishu.cn/drive/folder/fldcnoKLaAoSMItdOsjC8O7A5ub) | 2 | 📋 归档业务管理 | `宝冶`, `钢厂` |
| 上海化工 | [飞书](https://reliablesense.feishu.cn/drive/folder/fldcn9H00DYxSAKglF8eSOezXTd) | 1 | 📋 归档业务管理 | `百度需求`, `上海化工` |
| 机车检修 | [飞书](https://reliablesense.feishu.cn/drive/folder/fldcnL3DdEr4YbUvw1eeUZi8W2g) | 1 | 📋 归档业务管理 | `机车检修` |
| 保定轮毂厂 | [飞书](https://reliablesense.feishu.cn/drive/folder/SPS1fUblzlJcLRdqh9UcJUJtnJK) | 1 | 📋 归档业务管理 | `保定`, `轮毂` |
| 仁爱学院地图 | [飞书](https://reliablesense.feishu.cn/drive/folder/fldcnyvb2Wvj908C5k8Yi5xlPJb) | 1 | 📋 归档业务管理 | `仁爱` |
| 世博软件 | [飞书](https://reliablesense.feishu.cn/drive/folder/fldcnIJEAyzC7kpOvwBhFkhIVvg) | 1 | 📋 归档业务管理 | `世博` |

#### ~其他项目

| 项目名 | 飞书链接 | 文件数 | 归档方式 | 关键字 |
|--------|---------|--------|---------|--------|
| 兰州机场 | [飞书](https://reliablesense.feishu.cn/drive/folder/fldcnTnuXhdZedD0zw7DZ6Hqr5f) | 50 | 归入998兰州机场 | `兰州机场`, `定位应用` |
| 电厂煤棚定位 | [飞书](https://reliablesense.feishu.cn/drive/folder/fldcn807AdSNZzZn4mJwa5qPv6b) | 34 | 📋 归档业务管理 | `电厂`, `储煤棚` |
| 松下LED灯 | [飞书](https://reliablesense.feishu.cn/drive/folder/fldcnCb3VmyuRzhftSufgN2Caah) | 26 | 归入998松下LED灯 | `松下`, `LED` |
| 可口可乐叉车定位 | [飞书](https://reliablesense.feishu.cn/drive/folder/fldcnIAC2gwnUWTyYULDObMLhGe) | 19 | 归入999可口可乐叉车定位 | `可口可乐`, `叉车安全` |
| 智能眼罩 | [飞书](https://reliablesense.feishu.cn/drive/folder/fldcn6YEXgcxuHbZEpMs51QtkEd) | 17 | 📋 归档业务管理 | `眼罩` |
| 中广核电厂 | [飞书](https://reliablesense.feishu.cn/drive/folder/fldcneO36olE18KDvp2NxfMPYZb) | 17 | 📋 归档业务管理 | `核电站`, `中广核` |
| 报价记录 | | 12 | 📋 归档业务管理 | `报价记录`, `报价` |
| 政府库房 | [飞书](https://reliablesense.feishu.cn/drive/folder/fldcni2L4SfC0jkmmESlKTeLskd) | 11 | 📋 归档业务管理 | `政府库房` |
| 科学馆展厅 | [飞书](https://reliablesense.feishu.cn/drive/folder/fldcnMImMbAFHE9aR8oVR9ehPDb) | 8 | 📋 归档业务管理 | `科学馆`, `展厅` |
| 弘冉智能 | [飞书](https://reliablesense.feishu.cn/drive/folder/fldcncDxpMwrMVeHMX6drrDqwsf) | 6 | 📋 归档业务管理 | `弘冉` |
| 天津地铁 | [飞书](https://reliablesense.feishu.cn/drive/folder/fldcnZ7jRUe6KGGbATWoCYnakjh) | 6 | 📋 归档业务管理 | `天津地铁`, `列车进站` |
| 人效考勤 | [飞书](https://reliablesense.feishu.cn/drive/folder/fldcnQPoRYuKFpdLFxVHYL0zzhf) | 6 | 📋 归档业务管理 | `人效`, `考勤` |
| 吉林工艺车 | [飞书](https://reliablesense.feishu.cn/drive/folder/fldcn0GT2pYTiFSVAWnJyLplgab) | 4 | 📋 归档业务管理 | `吉林`, `工艺车` |
| 长兴视通 | [飞书](https://reliablesense.feishu.cn/drive/folder/fldcn0597TNerxmay7zHPUgshoh) | 3 | 📋 归档业务管理 | `长兴视通` |
| 安庆项目 | [飞书](https://reliablesense.feishu.cn/drive/folder/fldcnOACxDl3JS0sASvaxzCXwSg) | 3 | 📋 归档业务管理 | `安庆` |
| 国投生物 | [飞书](https://reliablesense.feishu.cn/drive/folder/fldcnvOTu0YqJ8PADcq1QR4aUVe) | 2 | 📋 归档业务管理 | `红点`, `国投生物` |
| 百威仓库 | [飞书](https://reliablesense.feishu.cn/drive/folder/fldcn3JnJx1DXaiSnrCKFBsTc6d) | 2 | 📋 归档业务管理 | `百威`, `仓库叉车` |
| 政府小区 | [飞书](https://reliablesense.feishu.cn/drive/folder/fldcnFoCVwuLOSrlPm7BvgLWJ6e) | 2 | 📋 归档业务管理 | `政府小区` |
| 如视项目 | [飞书](https://reliablesense.feishu.cn/drive/folder/YB4ufHQhYlm0jSdEovRcOvQ1nuh) | 2 | 📋 归档业务管理 | `如视` |

### 售前项目（未正式立项）

| 项目名 | 飞书来源目录 | 飞书链接 | 文件数 | 内容 |
|--------|------------|---------|--------|------|
| 赛力斯 | 000. 售前项目/赛力斯 + 王宗光/项目资料/赛力斯 | [飞书](https://reliablesense.feishu.cn/drive/folder/CAIWftFMilP7c1dCwg9cewJ3nKc) | 30+ | ✅ 已升级为正式项目 `1-Projects/Work/赛力斯定位/` |
| 安费诺 | 000. 售前项目/安费诺 | [飞书](https://reliablesense.feishu.cn/docx/EhDyd1X29omJiHx63d7cT5X0nrf) | 1 | → `4-Archives/Areas/Work/业务管理/安费诺/` |
| 美的净饮成品仓库 | 000. 售前项目/美的净饮成品仓库 | [飞书](https://reliablesense.feishu.cn/file/TnMFb5ha5o243IxcAFYcp77onVg) | 3 | → `4-Archives/Areas/Work/业务管理/美的净饮仓储管理/` |
| 长春车城乐园 | 000. 售前项目/长春车城乐园 | [飞书](https://reliablesense.feishu.cn/drive/folder/JgzWfy33SlvnsSdrg5Uc3Fdrnm1) | 28 | → `4-Archives/Areas/Work/业务管理/长春车城乐园/` |
| 湖南金旭 | 000. 售前项目/湖南金旭仓储物流有限公司 | [飞书](https://reliablesense.feishu.cn/drive/folder/JgzWfy33SlvnsSdrg5Uc3Fdrnm1) | 20 | → `2-Areas/Work/业务管理/湖南金旭仓储管理/` |

### 统计

| 分类 | 数量 |
|------|------|
| 进行中 | 7 |
| 已结束（998. 售后） | 35 |
| 已结束（003. 中东电子厂） | 1 |
| 已结束（其他） | 5 |
| 已结束（999. 归档） | 30 |
| 已结束（~其他项目） | 18 |
| 售前 | 5 |
| **合计** | **101** |

### 项目最终目标路径汇总

按 5 个目标路径分组，列出每个项目的最终目标目录和飞书链接。

#### `1-Projects/Work/`（进行中项目）

| 项目名 | 目标路径 | 创建时间 | 最后修改 | 飞书链接 |
|--------|---------|---------|---------|---------|
| 广州机场 | `1-Projects/Work/广州机场/` | 2023-12-19 | 2026-04-17 | [综合定位](https://reliablesense.feishu.cn/drive/folder/MrIOflncTlWrkEd4hJZcUxatncd) [移动应用平台](https://reliablesense.feishu.cn/drive/folder/DZVbfWCNnl1IaudvPBpcpXjenQf) |
| 新太定位 | `1-Projects/Work/新太定位/` | 2024-12-31 | 2025-09-04 | [内蒙新太元铬业](https://reliablesense.feishu.cn/drive/folder/IGJBfaqbJljC6adrtbCcumrrnCf) |
| 上港仓储管理 | `1-Projects/Work/上港仓储管理/` | 2023-12-25 | 2026-03-01 | [上海上港](https://reliablesense.feishu.cn/drive/folder/IwSpfxmL5lfpO8dLuoccbdnLnre) |
| 洛阳化工厂 | `1-Projects/Work/洛阳化工厂/` | 2024-06-05 | 2025-02-11 | [麦钉洛阳石化](https://reliablesense.feishu.cn/drive/folder/S3JWftxHWl14R5dz9FncpUPUnsd) [宏兴新能](https://reliablesense.feishu.cn/drive/folder/BKYCfWVwOlXZRpdgjpscVhannlc) |
| 南宁机场 | `1-Projects/Work/南宁机场/` | 2025-11-04 | 2026-02-27 | [南宁机场](https://reliablesense.feishu.cn/drive/folder/JuNOf2llHlkIa9dKw73cJm5pn3w) |
| 麦钉定位 | `1-Projects/Work/麦钉定位/` | 2024-04-22 | 2025-06-24 | [麦钉+红柳林等](https://reliablesense.feishu.cn/drive/folder/RTvgfEDMZlvXcod1aQScqUCdnXb) [孝感污水处理](https://reliablesense.feishu.cn/drive/folder/fldcnzHlG6xjy4ECXtD2za7G62e) [内蒙古洗煤厂](https://reliablesense.feishu.cn/drive/folder/fldcn0XgPdqYb7z218keyA7wyhd) [恩菲固废](https://reliablesense.feishu.cn/drive/folder/fldcnbKqOCYwFonGRakDFNNiXIc) |
| 赛峰定位 | `1-Projects/Work/赛峰定位/` | - | - | （无飞书目录链接） |
| 赛力斯定位 | `1-Projects/Work/赛力斯定位/` | 2025-04-01 | 2025-04-08 | [飞书](https://reliablesense.feishu.cn/drive/folder/CAIWftFMilP7c1dCwg9cewJ3nKc) |

#### `4-Archives/Projects/Work/`（已结束独立 Project）

| 项目名 | 目标路径 | 创建时间 | 最后修改 | 飞书链接 |
|--------|---------|---------|---------|---------|
| 众合人员管理 | `4-Archives/Projects/Work/众合人员管理/` | 2022-02-24 | 2022-02-24 | [众合Demo](https://reliablesense.feishu.cn/drive/folder/fldcn9ihucqqZa3fG3Px0Gloixc) [众合科技](https://reliablesense.feishu.cn/drive/folder/fldcndJIt8gCWm2aGkk20nLuU3d) |
| 博世定位 | `4-Archives/Projects/Work/博世定位/` | 2023-10-06 | 2025-08-29 | [Bosch](https://reliablesense.feishu.cn/drive/folder/P4GJfXpDolZ4EodGUF9cUCBonkc) |
| 国核智慧工地 | `4-Archives/Projects/Work/国核智慧工地/` | 2022-08-10 | 2023-03-09 | [国和一号](https://reliablesense.feishu.cn/drive/folder/fldcnKTgV6OtJkwR2ijJyY5rVsc) [山东国核](https://reliablesense.feishu.cn/drive/folder/fldcnDKqBIiko7la9mEC6iWzlHf) [威海核电](https://reliablesense.feishu.cn/drive/folder/CxMIfqTrnlwHNcd2Spmc5KEinnh) |
| 海尔工厂 | `4-Archives/Projects/Work/海尔工厂/` | 2022-02-21 | 2022-02-21 | [飞书](https://reliablesense.feishu.cn/drive/folder/fldcn9yq74Lu525sk4tf7ayUr0c) |
| 供电局库位 | `4-Archives/Projects/Work/供电局库位/` | 2022-02-21 | 2022-02-21 | [飞书](https://reliablesense.feishu.cn/drive/folder/fldcnhoSboKetpXvMBzbKRSmGAb) |
| 百度水厂 | `4-Archives/Projects/Work/百度水厂/` | 2022-04-15 | 2023-07-14 | [百度水厂](https://reliablesense.feishu.cn/drive/folder/PtrXfLdAglTcVXd6tvlcIUqBnDd) |
| 联通定位一体化 | `4-Archives/Projects/Work/联通定位一体化/` | 2022-02-21 | 2022-02-21 | [飞书](https://reliablesense.feishu.cn/drive/folder/fldcnlVHJxmUEdxDWjt8LvVcTjc) |
| 兰州机场 | `4-Archives/Projects/Work/兰州机场/` | 2022-11-04 | 2023-08-21 | [998兰州机场](https://reliablesense.feishu.cn/drive/folder/fldcn42BLWazsHzYslg6A34LLCd) [~其他兰州机场](https://reliablesense.feishu.cn/drive/folder/fldcnTnuXhdZedD0zw7DZ6Hqr5f) |
| 武汉机场 | `4-Archives/Projects/Work/武汉机场/` | 2022-07-21 | 2024-06-04 | [飞书](https://reliablesense.feishu.cn/drive/folder/fldcnHmHajD7TQATmdiqbTIuGRe) |
| 启程科技加气站 | `4-Archives/Projects/Work/启程科技加气站/` | 2022-02-24 | 2022-02-24 | [飞书](https://reliablesense.feishu.cn/drive/folder/fldcnoreuJsFnFpBJ6rVWisEtWc) |
| 数讯云人员服务系统 | `4-Archives/Projects/Work/数讯云人员服务系统/` | 2022-02-21 | 2022-02-21 | [飞书](https://reliablesense.feishu.cn/drive/folder/fldcnnpIG8G9K1vU3IH1XexyQpb) |
| 北京GE | `4-Archives/Projects/Work/北京GE/` | 2024-05-27 | 2024-11-15 | [飞书](https://reliablesense.feishu.cn/drive/folder/VL31fp5utl2g59dU3CbcBV1Onkc) |
| 松下LED灯 | `4-Archives/Projects/Work/松下LED灯/` | 2022-02-24 | 2022-02-24 | [998松下照明](https://reliablesense.feishu.cn/drive/folder/fldcnvFOcvpYap90lcIGxwbRTVf) [~其他松下LED灯](https://reliablesense.feishu.cn/drive/folder/fldcnCb3VmyuRzhftSufgN2Caah) |
| 天津眼科医院 | `4-Archives/Projects/Work/天津眼科医院/` | 2022-02-24 | 2022-05-07 | [飞书](https://reliablesense.feishu.cn/drive/folder/fldcn4LNTqNz05fkkDD51VReUoh) |
| 电子价签管理 | `4-Archives/Projects/Work/电子价签管理/` | 2023-10-06 | 2023-11-10 | [飞书](https://reliablesense.feishu.cn/drive/folder/E3NmfOQ5Pl5w9wdaRkjcEAvHntf) |
| 电网智能仓库 | `4-Archives/Projects/Work/电网智能仓库/` | 2022-02-19 | 2022-03-24 | [南方电网](https://reliablesense.feishu.cn/drive/folder/fldcnFfYXhVMbffAXURuPEYFZHg) [国家电网](https://reliablesense.feishu.cn/drive/folder/fldcnfcM9BxoadzLHM41eJujMUh) |
| 国家图书馆 | `4-Archives/Projects/Work/国家图书馆/` | 2023-03-03 | 2025-05-26 | [飞书](https://reliablesense.feishu.cn/drive/folder/fldcn6yxWW1ngHsX0GkzZZdVkEc) |
| 中东电子厂 | `4-Archives/Projects/Work/中东电子厂/` | 2025-04-08 | 2026-02-02 | [飞书](https://reliablesense.feishu.cn/drive/folder/UF9cfyxN7lnWIwd02auc28fFnOg) |
| 中联核信 | `4-Archives/Projects/Work/中联核信/` | 2025-04-19 | 2025-04-19 | [飞书](https://reliablesense.feishu.cn/drive/folder/LaOOfNGfBlvZqOdTmgtcRQzxnJc) |
| 嘉盛工厂 | `4-Archives/Projects/Work/嘉盛工厂/` | 2025-04-01 | 2025-04-22 | [飞书](https://reliablesense.feishu.cn/drive/folder/Q4jDfQS0alQqv2d0LjWcSR6rnVd) |
| 长沙酒店 | `4-Archives/Projects/Work/长沙酒店/` | 2022-02-24 | 2022-03-19 | [飞书](https://reliablesense.feishu.cn/drive/folder/fldcnYRwI8knNNUXUtof87Fyajb) |
| 民生物流 | `4-Archives/Projects/Work/民生物流/` | 2024-08-21 | 2024-12-06 | [飞书](https://reliablesense.feishu.cn/drive/folder/R07Dfa4FIlnT58dO8eWcFJ7WnXc) |
| 可口可乐叉车定位 | `4-Archives/Projects/Work/可口可乐叉车定位/` | 2022-02-21 | 2022-02-21 | [999可口可乐](https://reliablesense.feishu.cn/drive/folder/fldcn0qXGrnl4W8rKS5z6C6uilc) [~其他可口可乐](https://reliablesense.feishu.cn/drive/folder/fldcnIAC2gwnUWTyYULDObMLhGe) |
| 二手车管理 | `4-Archives/Projects/Work/二手车管理/` | 2022-02-20 | 2023-03-14 | [飞书](https://reliablesense.feishu.cn/drive/folder/fldcnu9ueOQWmpUM4axmkmYh7mf) |
| 苏州KIT | `4-Archives/Projects/Work/苏州KIT/` | 2024-03-31 | 2024-04-02 | [飞书](https://reliablesense.feishu.cn/drive/folder/WWclfhyFulfuTYdxFAWcYvc4nLe) |
| 丰田叉车 | `4-Archives/Projects/Work/丰田叉车/` | 2022-02-21 | 2025-11-04 | [飞书](https://reliablesense.feishu.cn/drive/folder/fldcnoZ28nWI3HHes9jTUz2hcGe) |
| 泰康养老院 | `4-Archives/Projects/Work/泰康养老院/` | 2022-02-21 | 2022-02-21 | [飞书](https://reliablesense.feishu.cn/drive/folder/fldcn7OgGvIC4ToMxhxVQBS3Srh) |
| 中远海运 | `4-Archives/Projects/Work/中远海运/` | 2024-10-22 | 2024-12-10 | [飞书](https://reliablesense.feishu.cn/drive/folder/Bnp4fUMeol0U1xdisfTcqv2xnCd) |
| 业睿展厅 | `4-Archives/Projects/Work/业睿展厅/` | 2022-02-21 | 2022-02-21 | [飞书](https://reliablesense.feishu.cn/drive/folder/fldcnO0LHPDLthNOwEOzl87p3bg) |
| 中科海微 | `4-Archives/Projects/Work/中科海微/` | 2022-02-24 | 2022-03-10 | [飞书](https://reliablesense.feishu.cn/drive/folder/fldcnDM4BkLZD0CfnzKBQZte1Og) |
| 扬州群鑫 | `4-Archives/Projects/Work/扬州群鑫/` | 2024-03-31 | 2026-04-09 | [飞书](https://reliablesense.feishu.cn/drive/folder/FEzCf5OfWlFFZgdDptVcgBiYnQh) |
| 电厂煤棚定位 | `4-Archives/Projects/Work/电厂煤棚定位/` | 2022-02-24 | 2022-02-24 | [飞书](https://reliablesense.feishu.cn/drive/folder/fldcn807AdSNZzZn4mJwa5qPv6b) |
| 智能眼罩 | `4-Archives/Projects/Work/智能眼罩/` | 2022-02-21 | 2022-02-21 | [飞书](https://reliablesense.feishu.cn/drive/folder/fldcn6YEXgcxuHbZEpMs51QtkEd) |
| 中广核电厂 | `4-Archives/Projects/Work/中广核电厂/` | 2022-02-24 | 2022-02-24 | [中广核](https://reliablesense.feishu.cn/drive/folder/fldcneO36olE18KDvp2NxfMPYZb) [核电站](https://reliablesense.feishu.cn/drive/folder/fldcneAiPn70Fw4xDazm6L26llg) |
| 政府库房 | `4-Archives/Projects/Work/政府库房/` | 2022-02-24 | 2022-02-24 | [飞书](https://reliablesense.feishu.cn/drive/folder/fldcni2L4SfC0jkmmESlKTeLskd) |
| 无动力设备管理 | `4-Archives/Projects/Work/无动力设备管理/` | - | - | （定制版子目录） |

#### `4-Archives/Areas/Work/业务管理/`（已结束售前项目）

| 项目名 | 目标路径 | 创建时间 | 最后修改 | 飞书链接 |
|--------|---------|---------|---------|---------|
| 康利达定位 | `4-Archives/Areas/Work/业务管理/康利达定位/` | 2022-02-24 | 2022-04-27 | [飞书](https://reliablesense.feishu.cn/drive/folder/fldcnPZ5u2pC8jXrwCWYmW0zKsN) |
| 厦门医院 | `4-Archives/Areas/Work/业务管理/厦门医院/` | 2022-02-21 | 2022-02-21 | [飞书](https://reliablesense.feishu.cn/drive/folder/fldcnH7FhGrBf94gG9RsIrIa8Zg) |
| 无动力设备信息融合 | `4-Archives/Areas/Work/业务管理/无动力设备信息融合/` | 2022-10-10 | 2022-12-09 | [飞书](https://reliablesense.feishu.cn/drive/folder/fldcnByfvqKI5s5vK8WVniVvNMe) |
| 上海易同科技 | `4-Archives/Areas/Work/业务管理/上海易同科技/` | 2022-02-24 | 2022-02-24 | [飞书](https://reliablesense.feishu.cn/drive/folder/fldcn8pIA6ElregB1Fggx07tGKg) |
| 清华大学 | `4-Archives/Areas/Work/业务管理/清华大学/` | 2022-02-24 | 2022-02-24 | [飞书](https://reliablesense.feishu.cn/drive/folder/fldcnpJzwab38BtPYZAFQgcicrf) |
| 振华项目 | `4-Archives/Areas/Work/业务管理/振华项目/` | 2024-08-14 | 2024-08-14 | [飞书](https://reliablesense.feishu.cn/drive/folder/S9lCfVWTwlUyORda8c5cb3BGnsb) |
| 天津医科大学总医院 | `4-Archives/Areas/Work/业务管理/天津医科大学总医院/` | 2022-02-21 | 2022-02-21 | [飞书](https://reliablesense.feishu.cn/drive/folder/fldcnIVDi2da6SfdGwkyejbPZ1g) |
| 广西电网 | `4-Archives/Areas/Work/业务管理/广西电网/` | 2022-10-09 | 2024-01-16 | [飞书](https://reliablesense.feishu.cn/drive/folder/fldcndXOeB44cYlW012D2C05Hcf) |
| 运输机大屏 | `4-Archives/Areas/Work/业务管理/运输机大屏/` | 2024-01-23 | 2024-01-30 | [飞书](https://reliablesense.feishu.cn/drive/folder/Uh1Nfl3eml9Nq1d3jhAc1kJ8nWg) |
| 南通精机 | `4-Archives/Areas/Work/业务管理/南通精机/` | 2024-08-19 | 2024-11-04 | [飞书](https://reliablesense.feishu.cn/drive/folder/MOK6fhlmalZiZGdMGHbcPdHgnjf) |
| 中软护理院 | `4-Archives/Areas/Work/业务管理/中软护理院/` | 2024-08-19 | 2024-08-19 | [飞书](https://reliablesense.feishu.cn/drive/folder/EE6nf30qtlkLzwdOkkmcLfHanGf) |
| 胶州湾 | `4-Archives/Areas/Work/业务管理/胶州湾/` | 2022-10-18 | 2022-10-19 | [飞书](https://reliablesense.feishu.cn/drive/folder/fldcn03OeBw3cqEZQLPCLDKMsUe) |
| 中奕信息 | `4-Archives/Areas/Work/业务管理/中奕信息/` | 2022-02-21 | 2022-02-21 | [飞书](https://reliablesense.feishu.cn/drive/folder/fldcnGYdaFxc8EybWdmNf25npwc) |
| 天津展厅 | `4-Archives/Areas/Work/业务管理/天津展厅/` | 2022-02-21 | 2022-02-21 | [飞书](https://reliablesense.feishu.cn/drive/folder/fldcniIKrxUSjvz71AJ07dL5Rhz) |
| 创源微致 | `4-Archives/Areas/Work/业务管理/创源微致/` | 2024-08-26 | 2024-11-02 | [飞书](https://reliablesense.feishu.cn/drive/folder/UirYfKFX2lIwo0daKshcMCOyn0b) |
| 济南炼化厂 | `4-Archives/Areas/Work/业务管理/济南炼化厂/` | 2022-06-27 | 2022-06-30 | [飞书](https://reliablesense.feishu.cn/drive/folder/fldcnW80ZP3Pl2In77nNl3YVSye) |
| 捷普工厂 | `4-Archives/Areas/Work/业务管理/捷普工厂/` | 2022-02-21 | 2022-02-21 | [飞书](https://reliablesense.feishu.cn/drive/folder/fldcnly6jvJUH3XExdT0Fnr0OOe) |
| 地铁停车场 | `4-Archives/Areas/Work/业务管理/地铁停车场/` | 2022-02-21 | 2022-02-21 | [飞书](https://reliablesense.feishu.cn/drive/folder/fldcnWzRLVtF16uOX9MP92WGz6e) |
| 苏州美的 | `4-Archives/Areas/Work/业务管理/苏州美的/` | 2023-07-19 | 2023-07-19 | [飞书](https://reliablesense.feishu.cn/drive/folder/GLRUfUaRKlwsaJdpq6IcNENBn6c) |
| 船只定位 | `4-Archives/Areas/Work/业务管理/船只定位/` | 2022-08-17 | 2022-08-17 | [飞书](https://reliablesense.feishu.cn/drive/folder/fldcnp91z9Kb0b3Oz9k8SxYL7Mh) |
| 深圳物联AIoT | `4-Archives/Areas/Work/业务管理/深圳物联AIoT/` | 2023-04-18 | 2023-05-09 | [飞书](https://reliablesense.feishu.cn/drive/folder/fldcnqBKqbikUuASzpKbKOzAgEN) |
| 宝冶钢厂 | `4-Archives/Areas/Work/业务管理/宝冶钢厂/` | 2022-02-21 | 2022-02-21 | [飞书](https://reliablesense.feishu.cn/drive/folder/fldcnoKLaAoSMItdOsjC8O7A5ub) |
| 上海化工 | `4-Archives/Areas/Work/业务管理/上海化工/` | 2023-03-10 | 2023-03-10 | [飞书](https://reliablesense.feishu.cn/drive/folder/fldcn9H00DYxSAKglF8eSOezXTd) |
| 机车检修 | `4-Archives/Areas/Work/业务管理/机车检修/` | 2022-02-21 | 2022-02-21 | [飞书](https://reliablesense.feishu.cn/drive/folder/fldcnL3DdEr4YbUvw1eeUZi8W2g) |
| 保定轮毂厂 | `4-Archives/Areas/Work/业务管理/保定轮毂厂/` | 2023-11-02 | 2023-11-02 | [飞书](https://reliablesense.feishu.cn/drive/folder/SPS1fUblzlJcLRdqh9UcJUJtnJK) |
| 仁爱学院地图 | `4-Archives/Areas/Work/业务管理/仁爱学院地图/` | 2022-10-17 | 2022-10-17 | [飞书](https://reliablesense.feishu.cn/drive/folder/fldcnyvb2Wvj908C5k8Yi5xlPJb) |
| 世博软件 | `4-Archives/Areas/Work/业务管理/世博软件/` | 2022-07-21 | 2022-07-21 | [飞书](https://reliablesense.feishu.cn/drive/folder/fldcnIJEAyzC7kpOvwBhFkhIVvg) |
| 科学馆展厅 | `4-Archives/Areas/Work/业务管理/科学馆展厅/` | 2022-02-24 | 2022-02-24 | [飞书](https://reliablesense.feishu.cn/drive/folder/fldcnMImMbAFHE9aR8oVR9ehPDb) |
| 弘冉智能 | `4-Archives/Areas/Work/业务管理/弘冉智能/` | 2022-02-24 | 2022-02-24 | [飞书](https://reliablesense.feishu.cn/drive/folder/fldcncDxpMwrMVeHMX6drrDqwsf) |
| 天津地铁 | `4-Archives/Areas/Work/业务管理/天津地铁/` | 2022-02-24 | 2022-02-24 | [飞书](https://reliablesense.feishu.cn/drive/folder/fldcnZ7jRUe6KGGbATWoCYnakjh) |
| 人效考勤 | `4-Archives/Areas/Work/业务管理/人效考勤/` | 2022-02-28 | 2022-02-28 | [飞书](https://reliablesense.feishu.cn/drive/folder/fldcnQPoRYuKFpdLFxVHYL0zzhf) |
| 吉林工艺车 | `4-Archives/Areas/Work/业务管理/吉林工艺车/` | 2022-02-24 | 2022-02-24 | [飞书](https://reliablesense.feishu.cn/drive/folder/fldcn0GT2pYTiFSVAWnJyLplgab) |
| 长兴视通 | `4-Archives/Areas/Work/业务管理/长兴视通/` | 2022-02-24 | 2022-02-24 | [飞书](https://reliablesense.feishu.cn/drive/folder/fldcn0597TNerxmay7zHPUgshoh) |
| 安庆项目 | `4-Archives/Areas/Work/业务管理/安庆项目/` | 2022-02-24 | 2022-02-24 | [飞书](https://reliablesense.feishu.cn/drive/folder/fldcnOACxDl3JS0sASvaxzCXwSg) |
| 国投生物 | `4-Archives/Areas/Work/业务管理/国投生物/` | 2022-02-24 | 2022-02-24 | [飞书](https://reliablesense.feishu.cn/drive/folder/fldcnvOTu0YqJ8PADcq1QR4aUVe) |
| 百威仓库 | `4-Archives/Areas/Work/业务管理/百威仓库/` | 2022-02-24 | 2022-02-24 | [飞书](https://reliablesense.feishu.cn/drive/folder/fldcn3JnJx1DXaiSnrCKFBsTc6d) |
| 政府小区 | `4-Archives/Areas/Work/业务管理/政府小区/` | 2022-02-24 | 2022-02-24 | [飞书](https://reliablesense.feishu.cn/drive/folder/fldcnFoCVwuLOSrlPm7BvgLWJ6e) |
| 如视项目 | `4-Archives/Areas/Work/业务管理/如视项目/` | 2025-05-07 | 2025-05-07 | [飞书](https://reliablesense.feishu.cn/drive/folder/YB4ufHQhYlm0jSdEovRcOvQ1nuh) |
| 哒咔定位 | `4-Archives/Areas/Work/业务管理/报价记录/` | - | - | （画板文档，无目录链接） |
| 安费诺 | `4-Archives/Areas/Work/业务管理/安费诺/` | 2025-01-10 | 2025-01-10 | [飞书](https://reliablesense.feishu.cn/docx/EhDyd1X29omJiHx63d7cT5X0nrf) |
| 美的净饮成品仓库 | `4-Archives/Areas/Work/业务管理/美的净饮仓储管理/` | 2025-02-11 | 2025-02-11 | [飞书](https://reliablesense.feishu.cn/file/TnMFb5ha5o243IxcAFYcp77onVg) |
| 长春车城乐园 | `4-Archives/Areas/Work/业务管理/长春车城乐园/` | 2024-08-23 | 2024-12-31 | [飞书](https://reliablesense.feishu.cn/drive/folder/JgzWfy33SlvnsSdrg5Uc3Fdrnm1) |
| 报价记录 | `4-Archives/Areas/Work/业务管理/报价记录/` | - | - | （无飞书目录链接） |

#### `2-Areas/Work/业务管理/`（进行中售前项目）

| 项目名 | 目标路径 | 创建时间 | 最后修改 | 飞书链接 |
|--------|---------|---------|---------|---------|
| 湖南金旭 | `2-Areas/Work/业务管理/湖南金旭仓储管理/` | 2026-04-03 | 2026-04-07 | [飞书](https://reliablesense.feishu.cn/drive/folder/JgzWfy33SlvnsSdrg5Uc3Fdrnm1) |

#### `2-Areas/Work/设备管理/`（归入设备管理）

| 项目名 | 目标路径 | 创建时间 | 最后修改 | 飞书链接 |
|--------|---------|---------|---------|---------|
| 合众思壮 | `2-Areas/Work/设备管理/合众思壮GPS/` | 2023-09-27 | 2024-06-04 | [飞书](https://reliablesense.feishu.cn/drive/folder/KS3BfWiA0lszPFdzHPHcltflnre) |
| 博实结 | `2-Areas/Work/设备管理/博实结GPS/` | 2025-04-01 | 2025-04-02 | [飞书](https://reliablesense.feishu.cn/drive/folder/BudrfapCnl9fLkd8Rl3cXhwjnve) |
| 红点定位 | `2-Areas/Work/设备管理/红点UWB/` | 2023-12-26 | 2023-12-26 | [飞书](https://reliablesense.feishu.cn/docx/YBASdNrzWo8e9ExCrZYcdClTnfg) |

### 设备管理 — 设备厂家清单（→ `2-Areas/Work/设备管理/`）

已在方案中标记"归入设备管理"的文件，以及供应商管理目录下的厂家，统一按厂家建目录。

迁移来源说明：
- 📂 整体搬：飞书供应商管理目录整体迁移，无散落文件
- 📄 散落文件：方案中其他章节标记归入设备管理的散落文件
- 📂+📄：既有整体目录，也有散落文件

#### 设备厂家

| 厂家名 | 目标路径 | 飞书链接 | 文件数 | 迁移来源 | 关键字 |
|--------|---------|---------|--------|---------|--------|
| 核芯物联蓝牙AOA | `设备管理/核芯物联蓝牙AOA/` | [飞书](https://reliablesense.feishu.cn/drive/folder/fldcnoIBnWnazd1IHxR3YhepMYe) | 22+ | 📂+📄 定位硬件厂商/核芯互联-硬件 + 散落：CLE测算报告(6c)、核心物联资料.zip(14章) | `核芯物联`, `CLE`, `CORELOCATION`, `CL-TA10`, `CL-GA10` |
| 蓝策蓝牙AOA | `设备管理/蓝策蓝牙AOA/` | | 1 | 📄 散落：蓝牙定位平台接口文档V1.61(13章嘉盛工厂) | `蓝策` |
| 红点UWB | `设备管理/红点UWB/` | [飞书(硬件)](https://reliablesense.feishu.cn/drive/folder/fldcnioGA6B5UmWMhaZFnKLzush) [飞书(合作)](https://reliablesense.feishu.cn/drive/folder/fldcn6ICwAl87p2HaNSaZxSAOyg) | 67 | 📂 定位硬件厂商/红点-硬件(54) + 合作企业/红点(13) | `红点`, `redpoint`, `UWB` |
| MOKO蓝牙 | `设备管理/MOKO蓝牙/` | [飞书](https://reliablesense.feishu.cn/drive/folder/fldcn8QCZ8QW3d8vz2CjJFcXPUd) | 4 | 📂 定位硬件厂商/MOKO | `MOKO`, `RSSI` |
| 合众思壮GPS | `设备管理/合众思壮GPS/` | [飞书](https://reliablesense.feishu.cn/drive/folder/KS3BfWiA0lszPFdzHPHcltflnre) | 18 | 📂 998.售后项目/合众思壮（整体搬） | `合众思壮` |
| 博实结GPS | `设备管理/博实结GPS/` | [飞书](https://reliablesense.feishu.cn/drive/folder/BudrfapCnl9fLkd8Rl3cXhwjnve) | 4 | 📄 散落：王宗光/项目资料/博实结(13章) — EG10E设备资料 | `博实结`, `EG10E` |
| 阿法迪蓝牙墨水屏 | `设备管理/阿法迪蓝牙墨水屏/` | | 2 | 📄 散落：墨水屏数据协议(1章)、E-Ink平台安装和使用手册(13章) | `墨水屏`, `E-Ink`, `电子标牌` |
| 华云时空UWB | `设备管理/华云时空UWB/` | [飞书](https://reliablesense.feishu.cn/drive/folder/fldcnulnDAIMY2OG75W9xFgPcqb) | 29 | 📂 合作企业/华云时空 | `华云时空` |
| 太和电子UWB | `设备管理/太和电子UWB/` | [飞书](https://reliablesense.feishu.cn/drive/folder/fldcnOYX43nyKPQ8QgDqlmNSDBb) | 24 | 📂 合作企业/太和 | `太和` |
| 空循环UWB | `设备管理/空循环UWB/` | [飞书](https://reliablesense.feishu.cn/drive/folder/fldcn5CQzCM2a2WuDgI4Vix8MTe) | 20 | 📂 合作企业/空循环 | `空循环` |
| Omlox | `设备管理/合作企业/Omlox/` | [飞书](https://reliablesense.feishu.cn/drive/folder/fldcnQLncLx6t2CPFn41cOAh9vh) | 15 | 📂 合作企业/Omlox | `Omlox` |
| 技新科技 | `设备管理/合作企业/技新科技/` | [飞书](https://reliablesense.feishu.cn/drive/folder/fldcn51N82KOJGtQueuinfKCK5c) | 8 | 📂 合作企业/技新科技 | `技新` |
| Seeklane | `设备管理/合作企业/Seeklane/` | [飞书](https://reliablesense.feishu.cn/drive/folder/fldcnc1qIh2bDM7Vu1kAQhIirJc) | 6 | 📂 合作企业/Seeklane | `Seeklane` |
| 在那科技GPS | `设备管理/在那科技GPS/` | [飞书](https://reliablesense.feishu.cn/drive/folder/fldcn8zvDHtZ8BKmirwSypSvmRg) | 6 | 📂 合作企业/NAVIECARE | `NAVIECARE`, `固定资产定位器` |
| Keeplink交换机 | `设备管理/Keeplink交换机/` | [飞书](https://reliablesense.feishu.cn/drive/folder/fldcnbJ44nH3c2PbShIdBpBY1fe) | 6 | 📂 合作企业/Keeplink | `Keeplink` |
| 菜鸟蓝牙AOA | `设备管理/菜鸟蓝牙AOA/` | [飞书](https://reliablesense.feishu.cn/drive/folder/fldcnY6fK1Z3wPfNmlj7ZCC2Xle) | 6 | 📂 合作企业/Cainiao | `Cainiao`, `菜鸟` |
| 深圳讯通蓝牙AOA终端 | `设备管理/深圳讯通蓝牙AOA终端/` | [飞书](https://reliablesense.feishu.cn/drive/folder/fldcnCsb1aNaiazOQiih0sN7lcg) | 5 | 📂 合作企业/深圳讯通 | `深圳讯通` |
| TP-LINK交换机 | `设备管理/TP-LINK交换机/` | [飞书](https://reliablesense.feishu.cn/drive/folder/fldcnK8XL2Y2qXe93G5LWt0f8HG) | 5 | 📂 合作企业/TP-LINK | `TP-LINK` |
| 麦思物联蓝牙 | `设备管理/麦思物联蓝牙/` | [飞书](https://reliablesense.feishu.cn/drive/folder/fldcnIFzxWuwJd4glZ1JR3lDIUd) | 4 | 📂 合作企业/麦思物联 | `麦思物联` |
| 吾控健康蓝牙AOA终端 | `设备管理/吾控健康蓝牙AOA终端/` | [飞书](https://reliablesense.feishu.cn/drive/folder/fldcnM0EeDq7fNjHTMRz4pFCCNd) | 3 | 📂 合作企业/深圳吾控 | `吾控`, `健康科技` |
| 顺势为蓝牙终端 | `设备管理/顺势为蓝牙终端/` | [飞书](https://reliablesense.feishu.cn/drive/folder/fldcnRAr9w9fOsC73011wxqkMVp) | 3 | 📂 合作企业/成都顺势为 | `顺势为` |
| 威思客 | `设备管理/合作企业/威思客/` | [飞书](https://reliablesense.feishu.cn/drive/folder/fldcnl6Gfv6ZGcpElm3qs4vsWYf) | 2 | 📂 合作企业/威思客 | `威思客` |
| 马蹄铁科技 | `设备管理/合作企业/马蹄铁科技/` | [飞书](https://reliablesense.feishu.cn/drive/folder/fldcnZhyASlAoZjhKqy6xCRlLWh) | 1 | 📂 合作企业/马蹄铁 | `马蹄铁` |
| 浪潮集团 | `设备管理/合作企业/浪潮集团/` | [飞书](https://reliablesense.feishu.cn/drive/folder/fldcnQYvZc2pFzMwFoyCtCtZFJb) | 1 | 📂 合作企业/浪潮 | `浪潮` |
| 菲曼科技RTK | `设备管理/菲曼科技RTK/` | [飞书](https://reliablesense.feishu.cn/drive/folder/fldcnddM5N5RHC7GzmLb2K2EE1f) | 2 | 📂 定位硬件厂商/北斗-硬件 | `北斗`, `菲曼`, `RTK` |
| 莱讯科技GPS | `设备管理/莱讯科技GPS/` | [飞书](https://reliablesense.feishu.cn/drive/folder/fldcnEQj7iSJUFva6t1KavOcvoe) | 7 | 📂 定位硬件厂商/GPS硬件 | `GPS硬件` |
| 莱讯科技设备 | `设备管理/莱讯科技设备/` | [飞书](https://reliablesense.feishu.cn/drive/folder/fldcnyprtlz9Jw58wK5kv8y9jZd) | 19 | 📂 定位硬件厂商/公司硬件 | `公司硬件` |
| 其他厂家设备 | `设备管理/其他厂家设备/` | [飞书](https://reliablesense.feishu.cn/drive/folder/fldcniTi1Xu5xfD1hgrUKEXYpfc) | 22 | 📂 定位硬件厂商/硬件不分类 | `硬件` |

#### 供应商管理通用文件

| 文件 | 目标路径 |
|------|---------|
| 供应商合同管理.xlsx | `2-Areas/Work/设备管理/` |
| 供应商管理.xlsx | `2-Areas/Work/设备管理/` |
| 库房管理 bitable | `2-Areas/Work/设备管理/` |
| MAC-Address.xlsx | `2-Areas/Work/设备管理/` |
| rssi数据.docx | `2-Areas/Work/设备管理/` |

---

## 二十、待确认事项（更新）

### 待确认条目统计

✅ 所有待确认条目已全部确认完毕（2026-04-22）。

| 分类 | 数量 | 说明 |
|------|------|------|
| 知识库/技术分享边界 | ~60 | `3-Resources/Tech/` vs `2-Areas/Work/` |
| 会议纪要 | 36 | 脚本无法自动分类，需人工确认 |
| 操作手册/用户手册 | 6 | 产品研发 vs 运维管理 |
| 运维类放了产品研发 | 5 | 容灾备份、压测配置等 |
| 特定项目放了通用目录 | 4 | 百度水厂部署手册等 |
| 产品业务概念放了 Tech | 5 | IoT接口、压线事件等 |
| 决策冲突 | 3 | 同一文件两处目标不同 |
| 其他边界模糊 | 8+ | 文件名太泛、产品归属不明等 |
| 压测相关 | 4 | 压测环境/数据 |

### 已解决的待确认事项

1. ~~**参考/ 目录**~~ → 全部留归档（行业报告和管理参考）
2. ~~**~参考资料/**~~：自家素材→品牌宣传/产品研发，竞品资料 5 个已确认
3. ~~**路网维护/**~~ → 留归档（路网文件无法读取）
4. ~~**共享文件/**~~ → 全部留归档（临时网盘）
5. **定制版项目子目录**：5 个子目录已确认（武汉机场→归档，新太/广州/洛阳/赛峰→进行中项目，无动力设备→`4-Archives/Projects/Work/无动力设备管理/`）
6. ~~**企业版/文档资料/ 子目录**~~ → 全部已确认（散落文件14个、bitable 3个、需求管理8个、测试用例7个、莱讯总平台11个、软件功能说明4个）
7. ~~**售前项目/ 下 4 个客户目录**~~：已确认（安费诺→业务管理、美的净饮→业务管理、长春车城乐园→业务管理、湖南金旭→业务管理）
8. **公司内部资料/ 子目录**：16 个子目录已补充到迁移方案
9. **定位平台中间件/ 子目录**：4 个设备中间件已补充到迁移方案
10. **项目资料管理/展会/**：已补充到迁移方案
11. ~~**~参考资料/竞品资料 5 个**~~：已确认


---

## 二十、飞书端大文件整理（仅云端，不下载到本地）

### 背景

阶段一拉取时跳过了 328 个大文件（mp4/zip/tar/psd/rar/iso 等），这些文件不适合存放在 Obsidian vault 中，但仍然存在于飞书云空间的原始目录下。

阶段三会在飞书端建立新的 PARA 知识库结构（见 [[飞书迁移映射方案]]），这些大文件也需要跟随迁移到飞书新结构中，与已下载的文件保持一致的目录归属。本地虽然不下载，但需要在迁移总览中有完整记录。

### 处理原则

1. **飞书端移动**：阶段三执行飞书重组时，将大文件通过 Drive API 移动到新知识库对应节点下
2. **本地不下载**：这些文件不进 Obsidian vault
3. **本地有记录**：在 `飞书文件清单与迁移状态.tsv` 中记录目标归属，在对应本地目录的 README.md 中列出飞书链接

### 按飞书新知识库结构分配

#### → 业务资料/品牌宣传 — 228 个

| 飞书原始位置 | 数量 | 类型 | 飞书目标节点 | 说明 |
|------------|------|------|------------|------|
| 往期展会资料合集/4.9会展中电/素材/ | 200 | mp4 | 业务资料/品牌宣传/展会/ | 展会现场拍摄视频 |
| 宣传/ | 17 | psd/ai | 业务资料/品牌宣传/宣传/ | 宣传物料设计源文件 |
| 宣传/ | 6 | mp4/mov | 业务资料/品牌宣传/宣传/ | 宣传视频 |
| 公司内部资料/地图绘制步骤/ | 2 | mov | 业务资料/品牌宣传/ | 地图绘制教程视频 |
| 公司内部资料/2023宣传视频/ | 3 | mp4 | 业务资料/品牌宣传/ | 宣传视频 |

本地索引位置：`2-Areas/Work/品牌宣传/` 及子目录下的 README.md

#### → 进行中项目 — 8 个

| 飞书原始位置 | 数量 | 类型 | 飞书目标节点 | 说明 |
|------------|------|------|------------|------|
| 002. 上海上港/测试记录/ | 2 | mp4 | 进行中项目/上港仓储管理/ | 测试录屏 |
| 麦钉洛阳石化/洛阳地图/ | 2 | rar/zip | 进行中项目/洛阳化工厂/ | 地图源数据 |
| 李家壕洗煤厂/相关软件/ | 1 | iso | 进行中项目/麦钉定位/ | CentOS 安装镜像 |
| ~其他项目/如视/ | 2 | zip | 按项目归属判断 | 点云/模型数据 |
| 其他项目测试视频 | 1 | mp4 | 按内容归属 | 测试视频 |

本地索引位置：`1-Projects/Work/对应项目/` 下的 README.md

#### → 已归档项目 — 12 个

| 飞书原始位置 | 数量 | 类型 | 飞书目标节点 | 说明 |
|------------|------|------|------------|------|
| 百度水厂/ | 1 | zip | 已归档项目/百度水厂/ | 部署包 |
| 南方电网/虚拟机/ | 2 | zip | 已归档项目/电网智能仓库/ | 虚拟机镜像 |
| 南方电网/ | 1 | rar | 已归档项目/电网智能仓库/ | 项目数据 |
| 众合Demo/ | 1 | txt | 已归档项目/众合人员管理/ | 操作步骤 |
| 其他已结束项目 | ~7 | zip/rar/mp4 | 已归档项目/对应项目/ | 按项目分配 |

本地索引位置：`4-Archives/Projects/Work/对应项目/` 下的 README.md

#### → 技术文档/环境配置 — 11 个

| 飞书原始位置 | 数量 | 类型 | 飞书目标节点 | 说明 |
|------------|------|------|------------|------|
| 项目运维管理/集群资料/私有化部署/ | 11 | 7z分卷/zip | 技术文档/环境配置/ | lbs 私有化部署包 |

本地索引位置：`2-Areas/Work/运维管理/` 下的 README.md

#### → `_归档/`（不进新知识库）— 69 个

| 飞书原始位置 | 数量 | 类型 | 说明 |
|------------|------|------|------|
| 共享文件/ | 41 | tar/zip/iso/exe | OEM 部署包、虚拟机、系统镜像（临时网盘性质） |
| 根目录散落 | 6 | mov/rar/zip | 个人文件、临时数据 |
| 解决方案管理/ | 3 | mp4/zip | 方案演示视频 |
| 供应商管理/ | 2 | rar/zip | 硬件厂商资料包 |
| 公司内部资料/其他 | 17 | psd/ai/mp4 | 与宣传重复或无归属的设计文件 |

随旧内容一起移入飞书 `_归档/` 目录，本地不索引。

### 执行方案

1. **阶段二（本地）**：
   - 更新 `飞书文件清单与迁移状态.tsv`：将 328 个 `⏭️ 跳过(大文件)` 补充飞书目标归属
   - 在对应本地目录的 README.md 中添加「仅云端文件」索引表

2. **阶段三（飞书端）**：
   - 建立新知识库结构后，通过 Drive API 将大文件移动到对应知识库节点
   - 留归档的 69 个文件随旧内容一起移入 `_归档/`

### 本地索引格式

在对应目录的 README.md 中添加：

```markdown
## 仅云端文件（未下载到本地）

以下文件保留在飞书云空间，未下载到 Obsidian：

| 文件名 | 类型 | 飞书链接 | 说明 |
|--------|------|---------|------|
| xxx.mp4 | 视频 | [飞书](https://...) | 展会现场拍摄 |
```

### TSV 状态更新

`飞书文件清单与迁移状态.tsv` 中的状态值更新：

| 原状态 | 新状态 | 含义 |
|--------|--------|------|
| `⏭️ 跳过(大文件)` | `📌 仅云端→业务资料/品牌宣传` | 飞书端移到品牌宣传，本地不下载 |
| `⏭️ 跳过(大文件)` | `📌 仅云端→进行中项目/{项目名}` | 飞书端移到对应项目，本地不下载 |
| `⏭️ 跳过(大文件)` | `📌 仅云端→已归档项目/{项目名}` | 飞书端移到归档项目，本地不下载 |
| `⏭️ 跳过(大文件)` | `📌 仅云端→技术文档/环境配置` | 飞书端移到技术文档，本地不下载 |
| `⏭️ 跳过(大文件)` | `📌 仅云端→_归档` | 飞书端留归档，本地不下载 |
