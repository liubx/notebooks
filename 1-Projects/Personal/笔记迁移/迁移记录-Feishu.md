---
title: 迁移记录-Feishu
type: migration-log
source: feishu
created: 2026-03-18
modified: 2026-03-20
---

# 飞书文档迁移记录

## 统计

- 云空间顶级文件夹：5（何宜峰的个人文档、莱讯科技、王宗光的个人文档、陈子杰的个人文档、孙永霖的个人文档）
- 根目录散落文件：~160+（大量智能纪要/会议记录）
- docx/doc 文档（可迁移）：~283（含根目录~137、何宜峰22、莱讯科技~5、王宗光52、陈子杰46、孙永霖2）
- 非文档类型（保留链接）：~72（bitable/sheet/mindnote/file）
- 知识库总节点数：~113（团队知识库 3 个 + 个人/受限知识库 9 个）
  - 团队知识库：技术分享 ~68 节点、项目管理 12 节点、规章制度 9 节点
  - 个人可遍历：3 个 Space 共 13 节点
  - 受限（仅 getNode）：6 个 Space 共 ~11 已知节点
  - 知识库 docx/doc（可迁移）：~95
  - 知识库非文档（保留链接）：~8（bitable/sheet/file）
- 跳过的第三方知识库：21
- ✅ 已迁移：111（docx 转 Markdown）
- 🔗 链接索引：51（doc 旧版文档，API 无法读取，创建链接索引文件）
- 🔗 保留链接：8（bitable/sheet/mindnote/file）
- ⏳ 会议纪要：97（智能纪要/会议记录，未迁移）
- 跳过的第三方知识库：21
- 迁移方式：docx → Markdown，doc → 链接索引，其他类型保留链接

---

## 一、云空间目录结构

### 📁 根目录（我的空间）

根目录下有 5 个文件夹和大量散落文件（主要是智能纪要和会议记录）。

#### 根目录散落文件

##### docx 文档

| # | 标题 | Token | 类型 | 状态 |
|---|------|-------|------|------|
| 1 | API | NoXpdv9A1oSb4gxwWDmciKajnOJ | docx | ✅ 已迁移 |
| 2 | 快速启用，属于你的任务管理系统 | X8Y8dLsjZo5wSuxGMu9cc7AAnGf | docx | ✅ 已迁移 |
| 3 | 系统整改配置表 | ZpsNdChggodbeaxLg78cgtRBnGc | docx | ✅ 已迁移 |
| 4 | 移动应用 - 监控 2025年5月13日 | GBCkdfZNVor1Lcxgs4AcSIZonMe | docx | ✅ 已迁移 |
| 5 | 墨水屏数据协议 | P4z0dkpVUoq3jwxUvBtcrRpundd | docx | ✅ 已迁移 |
| 6 | 系统架构图 | IYLtdtwDQoaOetxP9Xkc66jfnPf | docx | ✅ 已迁移 |
| 7 | 研发部的视频会议 2024年11月22日 | Vu8Nd0VN1ovfrOxpvDzcHcO5nSf | docx | ✅ 已迁移 |

##### 智能纪要/会议记录（docx，约 130+ 条）

大量自动生成的会议纪要，按时间倒序排列，包括：
- 近期会议速递（周报摘要）
- 月度纪要小结
- 智能纪要 + 文字记录（成对出现）
- Video meeting AI notes（英文版，2024年12月期间）

> 数量过多，不逐条列出。主要涉及：研发部会议、项目部会议、刘秉欣会议、内蒙新太项目会议等。
> 时间范围：2024年11月 ~ 2026年3月

##### bitable 多维表格

| # | 标题 | Token | 飞书链接 |
|---|------|-------|----------|
| 1 | 广州机场综合定位 v.2025-12-19 | NbIPbswwSaCfPpsWak7cbCHsnwe | https://reliablesense.feishu.cn/base/NbIPbswwSaCfPpsWak7cbCHsnwe |
| 2 | 周报测试 | NepGb0sWdaPfnosidcMc7yspnFg | https://reliablesense.feishu.cn/base/NepGb0sWdaPfnosidcMc7yspnFg |

##### sheet 电子表格

| # | 标题 | Token | 飞书链接 |
|---|------|-------|----------|
| 1 | 员工花名册-在职_2025-12-26 | HQsEseKUKhovu0t1ewnclLSAnte | https://reliablesense.feishu.cn/sheets/HQsEseKUKhovu0t1ewnclLSAnte |
| 2 | 定位对象在线时长导出表 | W95RsJ1SahTaeJt0xDgcM4d6n7f | https://reliablesense.feishu.cn/sheets/W95RsJ1SahTaeJt0xDgcM4d6n7f |
| 3 | 红柳林筛分楼部署内容 | shtcnuIgoeyPvXu60pwR4XsEc1g | https://reliablesense.feishu.cn/sheets/shtcnuIgoeyPvXu60pwR4XsEc1g |

##### mindnote 思维导图

| # | 标题 | Token | 飞书链接 |
|---|------|-------|----------|
| 1 | map-mobile | G7S6b8VC3mxDsPnZ1yDc4XItn2d | https://reliablesense.feishu.cn/mindnotes/G7S6b8VC3mxDsPnZ1yDc4XItn2d |
| 2 | map model | ZVgJbqGpTmw5v9nD5vTcqEg8nfe | https://reliablesense.feishu.cn/mindnotes/ZVgJbqGpTmw5v9nD5vTcqEg8nfe |
| 3 | 主题梳理 | RlIxblkhbmgyljn6ekgctdOInQy | https://reliablesense.feishu.cn/mindnotes/RlIxblkhbmgyljn6ekgctdOInQy |
| 4 | useWebsocket | Ka3QbhrfUmuBrWn4oAFcHMMEn8e | https://reliablesense.feishu.cn/mindnotes/Ka3QbhrfUmuBrWn4oAFcHMMEn8e |
| 5 | Then and now | XHFZbz7gNmUrd3nLkNScaIsUnOf | https://reliablesense.feishu.cn/mindnotes/XHFZbz7gNmUrd3nLkNScaIsUnOf |
| 6 | 认证流程 | PXQGbUjUtmaw6MnekMFcXvUtnce | https://reliablesense.feishu.cn/mindnotes/PXQGbUjUtmaw6MnekMFcXvUtnce |

##### file 附件

| # | 标题 | Token | 飞书链接 |
|---|------|-------|----------|
| 1 | 广州白云国际机场三期扩建项目-综合定位-接口规范-V1.0.2.docx | VmgKbcDxdo0OwLxIzrAcnBqlnic | https://reliablesense.feishu.cn/file/VmgKbcDxdo0OwLxIzrAcnBqlnic |
| 2 | 综合定位系统：深化设计方案.docx | OVHGbClJOoavkLx3gStcUVGAngh | https://reliablesense.feishu.cn/file/OVHGbClJOoavkLx3gStcUVGAngh |
| 3 | deploy.yaml | RwsBbb50NoKUaKxeVutcaFWBnVd | https://reliablesense.feishu.cn/file/RwsBbb50NoKUaKxeVutcaFWBnVd |
| 4 | 综合定位系统功能清单.xlsx | JV2ibGyG9oVohcxlBwJcQdbenJe | https://reliablesense.feishu.cn/file/JV2ibGyG9oVohcxlBwJcQdbenJe |
| 5 | 智慧仓储物流早会汇报v1.5.pptx | QeNlbb8xyoOSVPxfVMgcR8uCnKc | https://reliablesense.feishu.cn/file/QeNlbb8xyoOSVPxfVMgcR8uCnKc |
| 6 | 5.20日洛阳石化系统bug问题汇总.xlsx | YUCNbnhyMooytWxAZVZcntx4nff | https://reliablesense.feishu.cn/file/YUCNbnhyMooytWxAZVZcntx4nff |
| 7 | 广州市公办小学招生报名系统入学申请表.xls | T41fbSI4xoRMTJxtiWkctSUxnvp | https://reliablesense.feishu.cn/file/T41fbSI4xoRMTJxtiWkctSUxnvp |
| 8 | 14号夜班差异分析.xlsx | JXLib9uFkoA5F3xWLfxcD2jlnKf | https://reliablesense.feishu.cn/file/JXLib9uFkoA5F3xWLfxcD2jlnKf |
| 9 | 数字化.xlsx | E1b4biPmsoA4Ztx5Zj8c7CC0n6q | https://reliablesense.feishu.cn/file/E1b4biPmsoA4Ztx5Zj8c7CC0n6q |
| 10 | 优化后.txt | OuyFbuM1touvroxyPjEcki2on0d | https://reliablesense.feishu.cn/file/OuyFbuM1touvroxyPjEcki2on0d |
| 11 | Doc2.docx | VvsMbbh4OoziMkxwQGTcUXwMnYf | https://reliablesense.feishu.cn/file/VvsMbbh4OoziMkxwQGTcUXwMnYf |
| 12 | ترجمه.docx | FoTYbNSjwoE1trxSOvWce7rxntf | https://reliablesense.feishu.cn/file/FoTYbNSjwoE1trxSOvWce7rxntf |
| 13 | MAC Address.xlsx | MFjsbb7bBoHIr5xo4v7c95kqnvb | https://reliablesense.feishu.cn/file/MFjsbb7bBoHIr5xo4v7c95kqnvb |
| 14 | rssi数据.docx | WElAbEGxJoExttxZa90cDTeyn1X | https://reliablesense.feishu.cn/file/WElAbEGxJoExttxZa90cDTeyn1X |
| 15 | SaaS平台操作手册V7.docx | Krurb4Ew6okF4jxUP8BcDru3nUf | https://reliablesense.feishu.cn/file/Krurb4Ew6okF4jxUP8BcDru3nUf |
| 16 | 认证文件.zip | GCxtbICnZo5X1QxwnzfcMzErnGf | https://reliablesense.feishu.cn/file/GCxtbICnZo5X1QxwnzfcMzErnGf |
| 17 | 教学比赛.mov | AUT0b1zsdo1SQdxXCgHc9epunIf | https://reliablesense.feishu.cn/file/AUT0b1zsdo1SQdxXCgHc9epunIf |
| 18 | 宏兴裁切.rar | P5MBb8Cy6oYsYfx3MZjc8BhonCd | https://reliablesense.feishu.cn/file/P5MBb8Cy6oYsYfx3MZjc8BhonCd |
| 19 | FRP_GithubArm64_version_1_3_6.apk | YMF3bIlvFoTvxaxPI6IcKLwMnNc | https://reliablesense.feishu.cn/file/YMF3bIlvFoTvxaxPI6IcKLwMnNc |
| 20 | 20231117 亿童英语分级阅读组稿教师信息汇总表.xlsx | S0BSboHqco7VUOxrhiucyi9tnNb | https://reliablesense.feishu.cn/file/S0BSboHqco7VUOxrhiucyi9tnNb |
| 21 | 定位平台安装文件及文档.zip | Hr8bbKyRUoKdDtxgtLhcfDCknug | https://reliablesense.feishu.cn/file/Hr8bbKyRUoKdDtxgtLhcfDCknug |
| 22 | madinat_hjc.zip | UnIjb9C7qocVGExPTZpc9wkAnog | https://reliablesense.feishu.cn/file/UnIjb9C7qocVGExPTZpc9wkAnog |
| 23 | 转化后数据.zip | NXVgbTKQioF6Kkx26yScwwRbnjg | https://reliablesense.feishu.cn/file/NXVgbTKQioF6Kkx26yScwwRbnjg |
| 24 | 3.8.7.zip | ADaXb4skOo8TxVxNWSycGyi1nZe | https://reliablesense.feishu.cn/file/ADaXb4skOo8TxVxNWSycGyi1nZe |
| 25 | 信息平台消息交换标准协议_1.0.0(1).doc | RGtdbb0EYogQjHxMaxmcnf57n5b | https://reliablesense.feishu.cn/file/RGtdbb0EYogQjHxMaxmcnf57n5b |

---

### 📁 何宜峰的个人文档 (`HpWrfPlWIlsMDmdGH4DcoatKn2x`)

#### docx 文档

| # | 标题 | Token | 状态 |
|---|------|-------|------|
| 1 | IOT | J5Qndk4g1o0dWBxNCjIcxpcCneb | ✅ 已迁移 |
| 2 | 近期会议速递｜要点概览 2025年12月22日 | NJnQd8imdoNmXhxcmjccqoAwnxb | ⏳ 会议纪要 |
| 3 | 月度纪要小结｜11月24日 - 12月19日 | DkxkdBBbFoSr5Axve4GcwIvenjg | ⏳ 会议纪要 |
| 4 | 近期会议速递｜要点概览 2025年12月15日 | U7tmdjSSsoQWqTxMbYFcRLVtnxb | ⏳ 会议纪要 |
| 5 | 月度纪要小结｜10月27日 - 11月21日 | QTUOdDTqkoDqZJxzzbncYw4On2d | ⏳ 会议纪要 |
| 6 | 近期会议速递｜要点概览 2025年11月17日 | LmlMdaCD1oibasxwfDWcMTVenOh | ⏳ 会议纪要 |
| 7 | 智能纪要：管理内容、分支及注释问题讨论 2025年11月6日 | OCCsdy2coohBdmxcVdVcPIlNnof | ⏳ 会议纪要 |
| 8 | 文字记录：管理内容、分支及注释问题讨论 2025年11月6日 | Pvl3dZTnmo8xyPx3dLjcdFf8nqf | ⏳ 会议纪要 |
| 9 | 智能纪要：分子构建与插件使用安装讨论 2025年11月6日 | XmvYdGxTLoHZpJxmb0pcEgZNnbc | ⏳ 会议纪要 |
| 10 | 文字记录：分子构建与插件使用安装讨论 2025年11月6日 | HrTkdTglAohn1pxSxbfcUGPBnIc | ⏳ 会议纪要 |
| 11 | 近期会议速递｜要点概览 2025年11月3日 | CYC3dSQq8oV0jZxBvEncpFYZnKA | ⏳ 会议纪要 |
| 12 | 智能纪要：管理员数据库表及任务归属问题讨论 2025年10月30日 | QDWldDLdjoNx0Bx291QcPcBxnbS | ⏳ 会议纪要 |
| 13 | 文字记录：管理员数据库表及任务归属问题讨论 2025年10月30日 | UfuNdjJLAoTZnaxGRH0c4KAbnwg | ⏳ 会议纪要 |
| 14 | 智能纪要：数据同步、订阅测试及新数据格式讨论 2025年10月28日 | LqMIdcq9Nod1nlxOYGvcxUVwnqh | ⏳ 会议纪要 |
| 15 | 文字记录：数据同步、订阅测试及新数据格式讨论 2025年10月28日 | UHKEdQ12Mo7q1Wxrw3LchCN7ncb | ⏳ 会议纪要 |
| 16 | 智能纪要：8084接口、列表及地图问题讨论 2025年10月27日 | Vyf1d9xi7oSdZVxPUrAcWMIOnEf | ⏳ 会议纪要 |
| 17 | 文字记录：8084接口、列表及地图问题讨论 2025年10月27日 | LdfpdNSktotC7WxY1nAcoQ0gn5g | ⏳ 会议纪要 |
| 18 | 智能纪要：云江项目任务方案及后续安排会 2025年10月27日 | Satnd39gXoHjQYxUzW6cVWvinOe | ⏳ 会议纪要 |
| 19 | 文字记录：云江项目任务方案及后续安排会 2025年10月27日 | KhyYd0clVo2XuGxNWqrc9pGSnVd | ⏳ 会议纪要 |
| 20 | 近期会议速递｜要点概览 2025年10月20日 | S1nAdbGeSo5l7hxb058cIhEwnOd | ⏳ 会议纪要 |
| 21 | 智能纪要：项目依赖、日志及硬盘问题会议 2025年10月13日 | SVJodwciFoT6vGxQGiicoCpBnjg | ⏳ 会议纪要 |
| 22 | 文字记录：项目依赖、日志及硬盘问题会议 2025年10月13日 | K1rBdMgWcopeZjxXKBFc5nACndd | ⏳ 会议纪要 |

#### file 附件

| # | 标题 | Token | 飞书链接 |
|---|------|-------|----------|
| 1 | 员工入职表-空白(1).xls | L3hKbcijfohKN2xtueVc88dcnEd | https://reliablesense.feishu.cn/file/L3hKbcijfohKN2xtueVc88dcnEd |

---

### 📁 莱讯科技 (`fldcnXlYYuNIwJqa38AqI22zhMk`)

公司主文件夹，包含 17 个子文件夹和少量散落文件。

#### 子文件夹列表

| # | 文件夹名 | Token | 说明 |
|---|---------|-------|------|
| 1 | 销售管理 | fldcnuQTpZq9z3fQqoC2lpddUuf | 含 售前SOP 子文件夹、客户关系管理(bitable) |
| 2 | 共享文件 | KAzWfCcrMlNrOQdRqPhchfz2n2c | 含 madinat_xmc、madinat_hjc、综合定位、CERDB 子文件夹 + 软件安装包/ISO等 |
| 3 | 公司内部资料 | fldcnQotlfvWyG3wLT2xLKxAv9c | 含 20 个子文件夹（PPT模版、软著立项、ISO9001、地图绘制、名片、项目内容等） |
| 4 | 品牌手册与logo | fldcnxWldL28uIpPVgqGKq1iacc | |
| 5 | 项目资料管理 | fldcniMtNDIo3bJWZZrEyDVM6ec | 含 16 个子文件夹（详见下方） |
| 6 | 项目运维管理 | fldcnPox7nRmTls0wJ7mPhFhI2f | 含 运维文档、升级文档、交付文档、售后文档、集群资料、基础设施 |
| 7 | 网站维护 | UYyyf4hUllGZhWdgXMLci950nge | |
| 8 | 宣传 | ZOFWfSgpdllGNedVktUcgOupnze | |
| 9 | 路网维护 | fldcnLHpkn823HAgGZwpcki8omf | |
| 10 | ~参考资料 | fldcnpp8JeCmpzMuPLsbsIczAif | |
| 11 | 公司宣传物（公司介绍） | Ges8feJEylJjjydGKgNc6NIWnLd | |
| 12 | 往期展会资料合集 | fldcnLJHIahqTfcscC7zPIMN6cQ | |
| 13 | 公司英文资料 | ICuefj7fVl2yr7dFDNycWa4An2g | |
| 14 | 项目开发管理 | fldcnTCt4E8PT71bWj1nacGgsMf | 含 定位平台企业版/定制版/云端版/中间件 + 思维导图 |
| 15 | 解决方案管理 | fldcnSOm4zfnBox9IfQmHWN0WTh | 含 23 个行业方案子文件夹 |
| 16 | 供应商管理 | fldcnNwx1J0P7hbltFXzvM7zaZg | |
| 17 | 招聘管理 | fldcnBIre17Jup3HGpXsoiCd8se | |

#### 莱讯科技 > 散落文件

| # | 标题 | Token | 类型 |
|---|------|-------|------|
| 1 | API.docx | EmmnbY7kboTZBMxx5pncq5cUnXe | file |
| 2 | 画板文档 | RTWGd8ENYo9JSOxqoiRcEH3mnVf | docx |
| 3 | （无标题） | TrmgdsrPPosozVxRs3XcpKlfnne | docx |

#### 莱讯科技 > 项目资料管理 子文件夹

| # | 文件夹名 | Token |
|---|---------|-------|
| 1 | 002. 上海上港 | IwSpfxmL5lfpO8dLuoccbdnLnre |
| 2 | 南宁机场项目 | JuNOf2llHlkIa9dKw73cJm5pn3w |
| 3 | 003. 中东电子厂客户 | UF9cfyxN7lnWIwd02auc28fFnOg |
| 4 | 005. 广州机场-移动应用平台 | D0HIfmaPgleaANd8Cw1cDwpGnhb |
| 5 | 004. 广州机场-综合定位 | NQ2RfyZM7lO2iadqk3rcmDjPnsb |
| 6 | 998. 售后项目 | R0Jef62eAlU8d8dONehcJ0CdnOb |
| 7 | ~其他项目 | fldcnRPjh6QcMmwt4l61XoCDfqd |
| 8 | 中联核信 | LaOOfNGfBlvZqOdTmgtcRQzxnJc |
| 9 | 999. 归档项目 | O2CofScN2lERyKdxnlych2jbnVe |
| 10 | 000. 售前项目 | JgzWfy33SlvnsSdrg5Uc3Fdrnm1 |
| 11 | 001. 项目资料模板 | XHMvfo59aln6mfd4sqpcHpI0neh |
| 12 | 项目评估 | WW7df5NEglBmvCdYGDQcFZNKnEe |
| 13 | 展会 | fldcnZ6HnXhRV12CUM57fItepSe |

#### 004. 广州机场-综合定位 子文件夹内容

| # | 标题 | Token | 类型 | 迁移到 | 状态 |
|---|------|-------|------|--------|------|
| 1 | 大运控协同管理平台技术要求 | Gy3Pd3Yvho3aqUxqJJOcJqjjnBe | docx | [[4-Archives/Feishu/云空间/莱讯科技/项目资料管理/广州机场/大运控协同管理平台技术要求]] | ✅ 已迁移 |
| 2 | 广州机场热备 | Gy3Pd3Yvho3aqUxqJJOcJqjjnBe | docx | [[4-Archives/Feishu/云空间/莱讯科技/项目资料管理/广州机场/广州机场热备]] | ✅ 已迁移 |
| 3 | 航站楼协同决策管理系统（TCMD）技术要求 | Q8aPd8tcio0QHGxbuO6cmW8un3e | docx | [[4-Archives/Feishu/云空间/莱讯科技/项目资料管理/广州机场/航站楼协同决策管理系统（TCMD）技术要求]] | ✅ 已迁移 |
| 4 | 项目情况汇报 | VDJOdnJhOoGMPixqVWBcFJOznBe | docx | [[4-Archives/Feishu/云空间/莱讯科技/项目资料管理/广州机场/项目情况汇报]] | ✅ 已迁移 |
| 5 | 表C.2.5 深化评审记录(含附表)(三标段)(1205)最新 | WbRsd7TUgo7ASSx6VhicHCFynwF | docx | [[4-Archives/Feishu/云空间/莱讯科技/项目资料管理/广州机场/表C.2.5 深化评审记录]] | ✅ 已迁移 |
| 6 | AESB总线业务联调方案 | FM2hdCBaqo3humx0p1ccd8a9nKc | docx | [[4-Archives/Feishu/云空间/莱讯科技/项目资料管理/广州机场/AESB总线业务联调方案]] | ✅ 已迁移 |
| 7 | 项目情况汇报-2 | Qd1kdHm9lou4GpxZJuRckerQnFb | docx | [[4-Archives/Feishu/云空间/莱讯科技/项目资料管理/广州机场/项目情况汇报-2]] | ✅ 已迁移 |
| 8 | 综合定位系统运维白皮书 | AMuadobIrozdlZxG96gcHgtPnxe | docx | [[4-Archives/Feishu/云空间/莱讯科技/项目资料管理/广州机场/综合定位系统运维白皮书]] | ✅ 已迁移 |
| 9 | 综合定位系统技术要求 | Gi0MdNC9ToLxM0xfPDCcsKD2nzf | docx | [[4-Archives/Feishu/云空间/莱讯科技/项目资料管理/广州机场/综合定位系统技术要求]] | ✅ 已迁移 |
| 10 | 深化设计说明书（移动应用服务平台）-2025 | B2erdpLOJo5lqoxNeyucOFo2nYf | docx | [[4-Archives/Feishu/云空间/莱讯科技/项目资料管理/广州机场/深化设计说明书（移动应用服务平台）-2025]] | ✅ 已迁移 |

散落文件：
- cle测算报告 (docx, `KsIRdMFKRoRWqQx8yYkce8G0nys`)
- 项目管理 (bitable, `bascn8p8PpJEyLNk6UovDb1V6Of`)
- 项目管理 (sheet, `shtcnUlsqXQO5eCWs8r988gphad`)

#### 005. 广州机场-移动应用平台 子文件夹内容

| # | 标题 | Token | 类型 | 迁移到 | 状态 |
|---|------|-------|------|--------|------|
| 1 | 移动应用平台运维白皮书编写内容框架 | AhnkdGgzroBd8Cx9KxDctcGjnAg | docx | [[4-Archives/Feishu/云空间/莱讯科技/项目资料管理/广州机场-移动应用平台/移动应用平台运维白皮书编写内容框架]] | ✅ 已迁移 |
| 2 | 移动应用平台进程清单编写内容框架 | YCvydrOqHodVj8xC28EcVVMEnRf | docx | [[4-Archives/Feishu/云空间/莱讯科技/项目资料管理/广州机场-移动应用平台/移动应用平台进程清单编写内容框架]] | ✅ 已迁移 |
| 3 | 移动应用平台故障处理手册编写内容框架 | RPtLdFSovoD4Yex9QP6c77E2ncg | docx | [[4-Archives/Feishu/云空间/莱讯科技/项目资料管理/广州机场-移动应用平台/移动应用平台故障处理手册编写内容框架]] | ✅ 已迁移 |
| 4 | 移动应用平台配置清单编写内容框架 | Z5SFdZURjogTZ8xsMf0c5g6enos | docx | [[4-Archives/Feishu/云空间/莱讯科技/项目资料管理/广州机场-移动应用平台/移动应用平台配置清单编写内容框架]] | ✅ 已迁移 |
| 5 | 移动应用服务平台操作手册 | ZYlPd9RQYoOrXVx90tEccfHEnQg | docx | [[4-Archives/Feishu/云空间/莱讯科技/项目资料管理/广州机场-移动应用平台/移动应用服务平台操作手册]] | ✅ 已迁移 |

散落文件（file 类型，保留链接）：
- 移动应用平台用户手册.docx (file, `UIrtb8LiKoAiUaxpRyWcRgPOnve`) https://reliablesense.feishu.cn/file/UIrtb8LiKoAiUaxpRyWcRgPOnve
- 移动应用平台资产.xlsx (file, `LLVZbmV83oQqfDxp1AvcNk7cnUg`) https://reliablesense.feishu.cn/file/LLVZbmV83oQqfDxp1AvcNk7cnUg
- 移动应用平台进程清单.xlsx (file, `PwExbhasyon68OxsTiJcXhrcnWc`) https://reliablesense.feishu.cn/file/PwExbhasyon68OxsTiJcXhrcnWc
- 移动应用平台数据字典.docx (file, `BCd4bdxfwodyh7xMbHgcltnGn8b`) https://reliablesense.feishu.cn/file/BCd4bdxfwodyh7xMbHgcltnGn8b
- 移动应用平台配置清单.docx (file, `LY7tboh44oKC38xYhiLcwqkUnmT`) https://reliablesense.feishu.cn/file/LY7tboh44oKC38xYhiLcwqkUnmT
- 移动应用平台故障处理手册.docx (file, `UbD6bL2pzooRmIxaWM9ckhhunsb`) https://reliablesense.feishu.cn/file/UbD6bL2pzooRmIxaWM9ckhhunsb
- T3移动应用平台测评资产调研20250811.xlsx (file, `MCZ1bb5KSoRy0bxuOQGcxfwNnX9`) https://reliablesense.feishu.cn/file/MCZ1bb5KSoRy0bxuOQGcxfwNnX9
- 渗透测试系统域名调研 - 移动应用平台.xlsx (file, `CPDybNkttoyBfIxdxtBcwrPUntf`) https://reliablesense.feishu.cn/file/CPDybNkttoyBfIxdxtBcwrPUntf
- 移动应用平台运维白皮书.docx (file, `Pnnub7W0WonNIDxnBQGcsWuinma`) https://reliablesense.feishu.cn/file/Pnnub7W0WonNIDxnBQGcsWuinma
- 广州机场移动应用任务清单.xlsx (file, `T3xWbWNsmoJdxxxVV0McQszSnqg`) https://reliablesense.feishu.cn/file/T3xWbWNsmoJdxxxVV0McQszSnqg
- 移动应用平台开发与测试进展汇报.pdf (file, `Kkf6bl2V4oAr5vx5m4QccUDDniI`) https://reliablesense.feishu.cn/file/Kkf6bl2V4oAr5vx5m4QccUDDniI

> 注：陈子杰个人文档中的 `深化设计说明书（移动应用服务平台）-2025` 已在 004 广州机场-综合定位 section 中迁移。

#### 001. 项目资料模板 子文件夹内容

| # | 标题 | Token | 类型 | 迁移到 | 状态 |
|---|------|-------|------|--------|------|
| 1 | 0 软件项目资料-常州嘉盛半导体 | Sk1fdcud4oXDO0xLblCcpKYDn1c | docx | [[4-Archives/Feishu/云空间/莱讯科技/项目资料管理/项目资料模板/0-软件项目资料-常州嘉盛半导体]] | ✅ 已迁移 |
| 2 | 0 软件项目资料-中讯邮电 | YjyzdYSYUoXweHxGHljc7vF4nRc | docx | [[4-Archives/Feishu/云空间/莱讯科技/项目资料管理/项目资料模板/0-软件项目资料-中讯邮电]] | ✅ 已迁移 |
| 3 | 0 软件项目资料-人员定位系统 | doxcnmwgwcdPnrEHAgd4pXZMBgc | docx | [[4-Archives/Feishu/云空间/莱讯科技/项目资料管理/项目资料模板/0-软件项目资料-人员定位系统]] | ✅ 已迁移 |

> 注：另有 3 个重复 token（均为中讯邮电的副本）：`doxcnYnCagX1SsmAbbSyUtL0SRb`、`QbwZdfpAGoD01Ux19u8cuYuVnYf`、`WeIZdEfmOowHlaxp6IscEEMdnrb`，已跳过。

#### 莱讯科技 > 销售管理 子文件夹内容

| # | 标题 | Token | 类型 | 迁移到 | 状态 |
|---|------|-------|------|--------|------|
| 1 | 项目管理SOP目录 | — | docx | [[4-Archives/Feishu/云空间/莱讯科技/销售管理/项目管理SOP目录]] | ✅ 已迁移（前次session） |
| 2 | SOW文件 | JeSsdPfEaoy9exxBeD9cBP0pn8M | docx | [[4-Archives/Feishu/云空间/莱讯科技/销售管理/SOW文件]] | ✅ 已迁移 |

#### 莱讯科技 > 公司内部资料 散落 docx

| # | 标题 | Token | 类型 | 迁移到 | 状态 |
|---|------|-------|------|--------|------|
| 1 | 地图制作设计书 | — | docx | [[4-Archives/Feishu/云空间/莱讯科技/公司内部资料/地图制作设计书]] | ✅ 已迁移（前次session） |
| 2 | 工作周报管理及考核制度 | MfMRdLUQRovRsExNxjGcTZ8Jnxd | docx | [[4-Archives/Feishu/云空间/莱讯科技/公司内部资料/工作周报管理及考核制度]] | ✅ 已迁移 |
| 3 | 考勤制度 | ICeIdwPzXo2hSDxtqFqc4757nXd | docx | [[4-Archives/Feishu/云空间/莱讯科技/公司内部资料/考勤制度]] | ✅ 已迁移 |

#### 莱讯科技 > 公司内部资料 子文件夹

| # | 文件夹名 | Token |
|---|---------|-------|
| 1 | PPT模版 | fldcnU27rGaNhScFA2EumhiPNDd |
| 2 | 软著的立项资料 | SscHfr1iClEid6dcPsrc5cTJnNb |
| 3 | ISO9001质量体系认证 | fldcn3A1mrYbgL8yKwwsVrlsAtb |
| 4 | 地图绘制步骤 | fldcnYLI7hDlBu7aofuNx3Ck6Cb |
| 5 | 名片电子版 | fldcnWebyVQHsrx5NVADVNtAVof |
| 6 | 2023年项目内容 | W7WofvrPqltkcRdCffOcD6fJn2c |
| 7 | 2023年研发项目立项资料 | IvZLfBzQolsu4pdK4mCc8zhbnnf |
| 8 | 2023年终总结 | WIIBfQkG0lRBLbdSuFIcxcWlnyh |
| 9 | 照片 | fldcnsvLcjcJCnBdRwZCD7PkcYg |
| 10 | 宣传物料 | fldcn9ACHVf4Qe5rvvQUpe3yWwe |
| 11 | 展会 | fldcn9eBP3WayuYLB7wwCb9M7ub |
| 12 | 2023宣传视频 | fldcn8UgPjkTzJQLzraqLLRyWzc |
| 13 | 2022定位视频 | fldcnPvC8lXuZIrjT6n2pL6PMJc |
| 14 | 沙溪办公室 | fldcnQ9ADEkpL0UE9ryXM5TsrtM |
| 15 | 项目说明综合 | fldcnxfVszJspoPDYMK1wQv92NX |
| 16 | 员工管理 | fldcnU6GIbZ9caVTWzadIzCWukc |
| 17 | 公司网站 | fldcnbSfZdv8kFLSwZaBkyB8bPh |
| 18 | 财务 | fldcn2FV3N8eFdaZTishXl7wx0f |
| 19 | 商业计划书 | fldcnj1oIR4RBFGXn6gMASH6gZI |
| 20 | 参考 | fldcnp0dhECCllWO6ZULWdkTUCf |

散落文件：
- 合同订单管理 (bitable, `bascnemc8tozwPeCvL2GmUfG9Tg`)
- 任务管理 (bitable, `bascnm0yQj7bRGrIZE1vSUXMOGg`)
- 组织架构图 (doc, `doccnyI23DHQUFVPNJX7wFsoF0f`)
- 莱讯公司文档分类 (mindnote, `bmncnqFUTE8JqcJrJH049rDxF9b`)

#### 莱讯科技 > 解决方案管理 子文件夹

| # | 文件夹名 | Token |
|---|---------|-------|
| 1 | 医疗管理 | fldcnfW1XoDZq61aCjTTTMxn5Wb |
| 2 | 方案制作需求清单 | WEWafQtpSl0OXxdvDLxc5il1nHb |
| 3 | 工厂智能管理 | fldcnmwgAf8rXNPORyY841V9toc |
| 4 | 人员定位系统 | fldcngsLYcS76KLSqgmlf27UgFS |
| 5 | 轨道交通 | fldcnUSkIs7zEpcYhqZJdqB2mHf |
| 6 | 监狱方案 | fldcnqnbQVewfyPUywW1Kgt5p9c |
| 7 | APP | fldcnHqr92U5T4e6dsspCibhlzb |
| 8 | 仓储物流 | fldcnM1DioUybyK5yF0IpqIA4ue |
| 9 | ~其他公司方案 | fldcntIjp8709PCclFH082V5Dtw |
| 10 | 智慧工地 | fldcnB8vpGsKhbFw39wboL1KXWU |
| 11 | 展厅方案 | fldcn42c718VJ97rzaAOOj5dtYg |
| 12 | 智慧停车 | fldcnhKivCzfZBCASbfCixfBY3y |
| 13 | 三维GIS方案 | fldcnMIvLyjg0lkFSukBFjmbjgk |
| 14 | 资产管理 | fldcn6bvIwE07Vfdf22NWhTkkQg |
| 15 | 室外定位GPS | fldcnMPEUkEWzU1WooHG66ciTub |
| 16 | 工业环境解决方案 | fldcnTZK4gCDRdNYGH5TdeRIWxc |
| 17 | 枪支定位 | fldcnF3ytnSvoNWjQMVZ4MiNbef |
| 18 | 室外定位导航 | fldcnuemzAKmIchByv3yfj8FdEe |
| 19 | 智能制造 | fldcnoJlmqWb2Uz3stu8tI9nF4e |
| 20 | 执法办案中心 | fldcn0UMbtD5COUoqsR95FSiFfe |
| 21 | 交通运输方案 | fldcn4PnILhcncA0Mz0dRjnc3Gb |
| 22 | 室外手环定位 | fldcnk6tVeNUBM5yoHc0FdyB9cg |
| 23 | 煤矿智能管理 | fldcn2IcEtN0DkDCnVxp5p79IpD |

#### 莱讯科技 > 项目运维管理

| # | 文件夹名 | Token |
|---|---------|-------|
| 1 | 运维文档 | H5vtfx2x1l2p6bdrAQVcNt9Znub |
| 2 | 升级文档 | IHsJfjtq9llxoqdAZmjcHVncnUd |
| 3 | 交付文档 | GZzLfm4thlChhkdLTnLcJxiVncb |
| 4 | 售后文档 | Qjw7fos8plLYaydyOb3cPfLZngH |
| 5 | 集群资料 | fldcnKNYFNZgLPGg0DtwN4cP5se |
| 6 | 基础设施 | fldcntZLsnYqPY8zGArsdmnC9Ug |

散落文件：
- 位置压测相关服务器配置.xlsx (file, `JPHkbo3MZoCvClxqavvcqNvynKf`)
- 莱讯科技-小程序管理文档 (docx, `JgCpdERLho9N3zxiGpqcQ7GAnov`)

#### 莱讯科技 > 项目开发管理

| # | 名称 | Token | 类型 |
|---|------|-------|------|
| 1 | 定位平台企业版 | fldcnu2qBUhaE1OwRg3xs9UNnjc | folder |
| 2 | 定位平台定制版 | fldcny3eCULtDCPBvBdSDgOG2Th | folder |
| 3 | 定位平台中间件 | EFmZfeA8tlFwL4dJNbDc4emnnLc | folder |
| 4 | 定位平台云端版 | fldcnkPxyPGQvx5y0WILMcOsHJg | folder |
| 5 | 项目管理流程 | N0oObHdeam3taTnEDovcLbUFnmc | mindnote |
| 6 | 需求生命周期 | QoDWb7hy7mPUXMnjnVDc7jArnvg | mindnote |
| 7 | 项目迭代流程 | bmncnMWfRCAQqIY4UdwaMe12dVb | mindnote |

#### 莱讯科技 > 共享文件

| # | 名称 | Token | 类型 |
|---|------|-------|------|
| 1 | madinat_xmc | UBf3frRa7lJY5fdqEzMci0ganpz | folder |
| 2 | madinat_hjc | Cn1rfLplulSQpsd72jQchmFKnnb | folder |
| 3 | 综合定位 | DES9fznlPlMH82d2FfgczmFXnsg | folder |
| 4 | CERDB | XcrOfusdilCwx3dcUzIcdv7Rnic | folder |
| 5 | Clash.zip | GxZ9bCa1co8i1ux3RegcGWzenae | file |
| 6 | zh-cn_windows_11_enterprise_ltsc_2024.iso | D9GnbhzhXou3mUx5X37cOlrtnAh | file |
| 7 | tiny10 23h1 x64.iso | AJuebrJKKo2vO3xMaLAcLnBsnic | file |
| 8 | ips-server-data.zip | TLvjb8f6zoSXGUxm6aHct3ERnug | file |
| 9 | resource.zip | NvORbj9JEoO3WLxa9dfcsjrYnVc | file |
| 10 | android-studio-2023.1.1.26-windows.exe | Ddcrb2ZyeoGRP7x0zmdcQeBInEc | file |

#### 莱讯科技 > 销售管理

| # | 名称 | Token | 类型 |
|---|------|-------|------|
| 1 | 售前 SOP | QXyMfjzQElNTZmdhiSlcmb3QnLg | folder |
| 2 | 客户关系管理 | bascncveOYEhfjbtaaj3U6Rgete | bitable |

---

### 📁 王宗光的个人文档 (`HV3ufVE3UlQ9qcdRqo4c7fhnnZf`)

#### 子文件夹列表

| # | 文件夹名 | Token |
|---|---------|-------|
| 1 | 交接文档 | DQPFf8zhBlPqWYdx4gzcxEkSnLf |
| 2 | 工作总结 | I5Ytfz08kl67jkdvOhVcKpJknje |
| 3 | 项目资料 | EfkTfwPetlZv7kdv1HQcoOefn1b |
| 4 | 知识问答 | IiOLfpK0ZlX9dud4mo5cxQajn8g |
| 5 | 定制化项目 | ZtGqf8rtClqP6NdkYRWcNtf6nWh |
| 6 | 我的空间 | CwDffa7j2lXcVgdE071cyjE2ntg |
| 7 | 平台功能迭代 | LqkJfIEetlAs9udVWiKctanpnhc |
| 8 | 后端架构 | Jdsof898Blb8m6dGXeZcDNmmnzf |
| 9 | 文档 | Rfw6fLqIAlKb4cdLVg9cVZoXnJe |
| 10 | 问题处理记录 | HKpafU8pslzHdPdUhHvc5JHXnRh |
| 11 | 测试 | JuIjf8hCZlKCfOd56zgc16I1nxg |
| 12 | 会议纪要 | CaV5fgUiQlXEmbdJI7zc8DeWnqb |

#### 散落 docx 文档

| # | 标题 | Token | 状态 |
|---|------|-------|------|
| 1 | 智能纪要：刷新配置规则变更讨论会议 2025年9月25日 | XHG9dLsmDoBkJxx4bkJcIABInbD | ⏳ 会议纪要 |
| 2 | 文字记录：刷新配置规则变更讨论会议 2025年9月25日 | GUjJdm0rboypogxtgcacRhAEn7e | ⏳ 会议纪要 |
| 3 | 近期会议速递｜要点概览 2025年9月22日 | QBT7d9e5PoMLKlx5DP8c23Agne1 | ⏳ 会议纪要 |
| 4 | 月度纪要小结｜8月25日 - 9月19日 | BlTTdQJKAoia6Kxae4Jc2avHnKe | ⏳ 会议纪要 |
| 5 | 智能纪要：申库、测试及登录存货问题讨论 2025年9月17日 | HNAVdtRgzo4xLFxUjO0c3qi9nJc | ⏳ 会议纪要 |
| 6 | 文字记录：申库、测试及登录存货问题讨论 2025年9月17日 | NrtBdN4sQo4P0cxB0RJc21Ebnse | ⏳ 会议纪要 |
| 7 | 智能纪要：scommon获取及分支合并问题讨论 2025年9月16日 | LCdQdpAf7ozPMtxQUthcZqTKnLh | ⏳ 会议纪要 |
| 8 | 文字记录：scommon获取及分支合并问题讨论 2025年9月16日 | DJOWdV7t5o2Mjdxx8ZacVCh1n3d | ⏳ 会议纪要 |
| 9 | 近期会议速递｜要点概览 2025年8月25日 | JPvNdiIsbo1dmcxRiWLcdD6VnIh | ⏳ 会议纪要 |
| 10 | 智能纪要：办公室 CLE 数据配置及墨水屏问题会议 2025年8月19日 | XAwMd4UStoorpRxKG3scYBLbnQe | ⏳ 会议纪要 |
| 11 | 文字记录：办公室 CLE 数据配置及墨水屏问题会议 2025年8月19日 | QG3ld8j2joWsEDxVOFocVLrAnOg | ⏳ 会议纪要 |
| 12 | 月度纪要小结（播客版）｜5月26日 - 6月20日 | Eoy1dYW8oolqoJxhve3cn5bgncS | ⏳ 会议纪要 |
| 13 | 近期会议速递｜要点概览 2025年6月9日 | RcHbdD8uOoUWj8xecNTcAtFjnmb | ⏳ 会议纪要 |
| 14 | 智能纪要：多方面业务问题及解决方案探讨会 2025年6月3日 | NPkFdqGfUo1Bf2xEQOGclc7anMh | ⏳ 会议纪要 |
| 15 | 文字记录：多方面业务问题及解决方案探讨会 2025年6月3日 | Jtm6dfrULo7SNYxWZZ9cwLULnvd | ⏳ 会议纪要 |
| 16 | 近期会议速递｜要点概览 2025年6月2日 | TC2Od2W9Ko56Wnx5QQkcDqLlnlg | ⏳ 会议纪要 |
| 17 | 智能纪要：平台重启及相关技术问题研讨 2025年5月31日 | LDm7dDpHfoC4DBx6Vthcwqkrn4c | ⏳ 会议纪要 |
| 18 | 文字记录：平台重启及相关技术问题研讨 2025年5月31日 | LRjhdZLUeoMIyKxAoIyciR1qneg | ⏳ 会议纪要 |
| 19 | E-Ink平台安装和使用手册 | BTKgdqfbXowNV5x0DSfcfafpncY | ✅ 已迁移 |
| 20 | 智慧工厂电子标牌管理系统软件v1.0.0-json格式 | TYe7doOyNovyfLxfXOScJ2vyngf | ✅ 已迁移 |
| 21 | 近期会议速递｜要点概览 2025年5月12日 | CvpwdYui0oKufcxNcFzc4IDVnFe | ⏳ 会议纪要 |
| 22 | 近期会议速递｜要点概览 2025年4月21日 | VUzAdTmbYowa23xouqCcGhiyn8c | ⏳ 会议纪要 |
| 23 | 近期会议速递｜要点概览 2025年4月14日 | Zc4odoDyzo1REVxTrrUcl7gGnPy | ⏳ 会议纪要 |
| 24 | 智能纪要：项目服务、权限及工作进展会议 2025年4月11日 | LKSodmV6loX04TxtDTNcEqmcnLe | ⏳ 会议纪要 |
| 25 | 文字记录：项目服务、权限及工作进展会议 2025年4月11日 | KoC5dKi6koHwTfx8Dkbcgrlon5g | ⏳ 会议纪要 |
| 26 | 近期会议速递｜要点概览 2025年4月7日 | QLdTdlduEoRsZkxNEblc0rlynZf | ⏳ 会议纪要 |
| 27 | 近期会议速递｜要点概览 2025年3月17日 | UV45dVypYoiEOFx9AYXcAGFDnne | ⏳ 会议纪要 |
| 28 | 近期会议速递｜要点概览 2025年3月10日 | JHJ5d6S5QopfyHxPUnwcKyLlnSe | ⏳ 会议纪要 |
| 29 | 智能纪要：内蒙新太项目（新钢联）的视频会议 2025年3月5日 | EePFdqlyQoh4bExphrXcGX3Wnjd | ⏳ 会议纪要 |
| 30 | 文字记录：内蒙新太项目（新钢联）的视频会议 2025年3月5日 | D0aEdYFlYo9REkxhIrwcDDWCnPf | ⏳ 会议纪要 |
| 31 | 近期会议速递｜要点概览 2025年3月3日 | W5AqdUrFvoHX12xnzHFc5JZ2nqg | ⏳ 会议纪要 |
| 32 | 智能纪要：内蒙新太项目（新钢联）的视频会议 2025年2月26日 | IQUqdVOipoy6MUx9pYicAUvrnmd | ⏳ 会议纪要 |
| 33 | 文字记录：内蒙新太项目（新钢联）的视频会议 2025年2月26日 | OgG5dQrQLoGY9FxEchhcSvmknXg | ⏳ 会议纪要 |
| 34 | 智能纪要：研发部的视频会议 2025年2月24日 | C66QdPXJyolJ50xp7JBczVxunQb | ⏳ 会议纪要 |
| 35 | 文字记录：研发部的视频会议 2025年2月24日 | PhfqdTLQ3o5QyyxbK2IcRAkNn0b | ⏳ 会议纪要 |
| 36 | 近期会议速递｜要点概览 2025年2月24日 | NglNdnbykoAAZOxR5hNc8hNHn66 | ⏳ 会议纪要 |
| 37 | 王宗光的视频会议 2025年2月20日 - 智能纪要 | Rr23dKQ8vo2vyYxmepgcq5ktn1c | ⏳ 会议纪要 |
| 38 | 文字记录：王宗光的视频会议 2025年2月20日 | DGyzdAmKkoykTYxVkoxcduRcnCc | ⏳ 会议纪要 |
| 39 | 近期会议速递｜要点概览 2025年2月17日 | AAZBdw0mao7Q4ExDeMTcCEWbnXf | ⏳ 会议纪要 |
| 40 | 近期会议速递｜要点概览 2025年2月10日 | O59Ad3PUIo0fffxtZfBcq1janNc | ⏳ 会议纪要 |
| 41 | 近期会议速递｜要点概览 2025年1月27日 | IpNOd7CAmoRHjjxzosechTohn2e | ⏳ 会议纪要 |
| 42 | 近期会议速递｜要点概览 2025年1月20日 | Owhldv8t2oMiwMxyLw4cR0gpn9c | ⏳ 会议纪要 |
| 43 | 近期会议速递｜要点概览 2025年1月13日 | ODULdAXKIo54etxzWrVcAsrznqd | ⏳ 会议纪要 |
| 44 | 近期会议速递｜要点概览 2025年1月6日 | MC4vdeRzVo29YJxXa7Ncolr2nYf | ⏳ 会议纪要 |
| 45 | 近期会议速递｜要点概览 2024年12月30日 | LMBudjzZUobQUNxeyu0cPa6znUg | ⏳ 会议纪要 |
| 46 | 近期会议速递｜要点概览 2024年12月23日 | DEwIdJiEWo75WNx3acgcUrntnMb | ⏳ 会议纪要 |
| 47 | 近期会议速递｜要点概览 2024年12月16日 | Xn0Id41i2oK3rgxAaVVc5TcFnOf | ⏳ 会议纪要 |
| 48 | 日志说明 | BdUEdhqBIofw1YxY2nGc8jEfn7d | ✅ 已迁移 |
| 49 | 莱讯-移动端需求 | U1EedFUBmoNwPQxD9oHcWweanXc | ✅ 已迁移 |
| 50 | 标书3 | JBxYdx0OZoySuUx2hkicNerDnNb | ✅ 已迁移 |
| 51 | 无动力设备信息融合系统-源代码 | doxcnWD87qgPTeUnEIrenFMqHYf | ✅ 已迁移 |
| 52 | 众合Demo环境--软件 功能_20210701 | doxcnF0mpOOrz5DbDYLjwWB6VWb | ✅ 已迁移 |

#### bitable 多维表格

| # | 标题 | Token | 飞书链接 |
|---|------|-------|----------|
| 1 | 工作周报 | RIHubtFOhadg4TsFWJoch9iEnuh | https://reliablesense.feishu.cn/base/RIHubtFOhadg4TsFWJoch9iEnuh |
| 2 | 🚩会议签到表 | ZQj0bMC5eaghvxsBxzGcBWDznUc | https://reliablesense.feishu.cn/base/ZQj0bMC5eaghvxsBxzGcBWDznUc |

#### sheet 电子表格

| # | 标题 | Token | 飞书链接 |
|---|------|-------|----------|
| 1 | 远端接口新需求问题反馈-20230323 | shtcniz2m6u89tCpHodDRbIhDxd | https://reliablesense.feishu.cn/sheets/shtcniz2m6u89tCpHodDRbIhDxd |

#### file 附件

| # | 标题 | Token | 飞书链接 |
|---|------|-------|----------|
| 1 | 王宗光24年周报.xlsx | WRgCb0V8ToSCsqx2qSdcW81Fnlh | https://reliablesense.feishu.cn/file/WRgCb0V8ToSCsqx2qSdcW81Fnlh |
| 2 | 用户敏感信息处理.md | N4wvbKBhfoKdLMxIlQRckQAlnpd | https://reliablesense.feishu.cn/file/N4wvbKBhfoKdLMxIlQRckQAlnpd |

---

### 📁 陈子杰的个人文档 (`VfuVfhs6glPn7rduucrchzz1nuc`)

#### 子文件夹列表

| # | 文件夹名 | Token |
|---|---------|-------|
| 1 | 知识问答 | XK2pf4qjwlapegddDxncbEo3nCd |
| 2 | 广州机场-移动应用平台 | LgWJf48yFl4GPKdl04yc5hxrnmb |

#### 广州机场-移动应用平台 子文件夹内容

| # | 名称 | Token | 类型 |
|---|------|-------|------|
| 1 | appstore | V9sxf4h6xltx7Pd0OXccSy39ncf | folder |
| 2 | 移动终端目前缺失功能 | RLRqbFnrPaokuRsVtTbcjkMLnZd | bitable |
| 3 | 移动应用平台开发与测试进展汇报.pdf | Kkf6bl2V4oAr5vx5m4QccUDDniI | file |
| 4 | 深化设计说明书（移动应用服务平台）-2025 | B2erdpLOJo5lqoxNeyucOFo2nYf | docx |

#### 散落 docx 文档

| #   | 标题                                | Token                       | 状态  |
| --- | --------------------------------- | --------------------------- | --- |
| 1   | 近期会议速递｜要点概览 2025年9月22日            | Ij7ddnCqxoTyHsxBjRecEp4JnJc | ⏳ 会议纪要 |
| 2   | 智能纪要：数据、页面状态及功能处理会议 2025年9月17日    | KliDdAtzionSN1xuPXic7YWynUd | ⏳ 会议纪要 |
| 3   | 文字记录：数据、页面状态及功能处理会议 2025年9月17日    | O7UVdlfMSoMkZbxVyWic5N0bnBf | ⏳ 会议纪要 |
| 4   | 流程图                               | BWGKd2466omTdxxjRQdciMNknyh | ✅ 已迁移 |
| 5   | 月度纪要小结（播客版）｜5月26日 - 6月20日         | GPoCdJwSDoTzFSx3xsScQEPynCh | ⏳ 会议纪要 |
| 6   | 近期会议速递｜要点概览 2025年6月9日             | WCAQdiwTDoYuKexlMJ0cvK8MnFb | ⏳ 会议纪要 |
| 7   | 智能纪要：移动应用与 TCDM 会议讨论 2025年6月3日    | VARrddtC3oOlFMxENAFcoGBKnl9 | ⏳ 会议纪要 |
| 8   | 文字记录：移动应用与 TCDM 会议讨论 2025年6月3日    | JmwhduJIPouIxsx7Sh6cH5ZOnph | ⏳ 会议纪要 |
| 9   | 近期会议速递｜要点概览 2025年5月19日            | VNq6dqMR2opizBx1E1HcyqVinBg | ⏳ 会议纪要 |
| 10  | 智能纪要：上海东海模型修复及接入方案研讨 2025年5月15日   | BT99d8bucoUruTx4rvZcYbRbnff | ⏳ 会议纪要 |
| 11  | 文字记录：上海东海模型修复及接入方案研讨 2025年5月15日   | Ky4Ldt5hFoe6mQxg8lrctpCRngh | ⏳ 会议纪要 |
| 12  | 近期会议速递｜要点概览 2025年5月12日            | LxV2d0o1VoXVmyxwBdfcFsTanLb | ⏳ 会议纪要 |
| 13  | 近期会议速递｜要点概览 2025年4月21日            | ZIcAduwBcoXGuMxS9q8cXSccn9g | ⏳ 会议纪要 |
| 14  | 近期会议速递｜要点概览 2025年4月14日            | NmAXd423Xo5FbZxFQppcvft6nzf | ⏳ 会议纪要 |
| 15  | 智能纪要：黄佳琪软件工作安排及指导会议 2025年4月11日    | KFRAdFWTjoSKrIxLDPFcQH3Oncg | ⏳ 会议纪要 |
| 16  | 文字记录：黄佳琪软件工作安排及指导会议 2025年4月11日    | MWlJdSwz6o30ykxZGMPcLmdin0f | ⏳ 会议纪要 |
| 17  | 近期会议速递｜要点概览 2025年4月7日             | QsCbdNHr8oPl4Xx0uLicu9GUnAe | ⏳ 会议纪要 |
| 18  | 近期会议速递｜要点概览 2025年3月17日            | LICQdsN5AoOPUax19UJckYmQneb | ⏳ 会议纪要 |
| 19  | 近期会议速递｜要点概览 2025年3月3日             | UscVdJyLcoGhT9xlVCqcm6pSnPh | ⏳ 会议纪要 |
| 20  | 智能纪要：陈子杰的视频会议 2025年2月24日          | XVxUdVtaSo0wu6xtY3Uc7GdHnrc | ⏳ 会议纪要 |
| 21  | 文字记录：陈子杰的视频会议 2025年2月24日          | JhwjdqDfJoBMExxV9btciKO3nhf | ⏳ 会议纪要 |
| 22  | 近期会议速递｜要点概览 2025年2月24日            | ANZcdUqC5opTD0xfs7Cc6OuDnPh | ⏳ 会议纪要 |
| 23  | 近期会议速递｜要点概览 2025年2月17日            | Gna2dHIXQoREOUxBOXbcEYZZnqr | ⏳ 会议纪要 |
| 24  | 近期会议速递｜要点概览 2025年2月10日            | NAkkdVvn0oT5TNxjBvkcNNkmnKe | ⏳ 会议纪要 |
| 25  | 内蒙新太项目（新钢联）的视频会议 2025年2月7日 - 智能纪要 | W7Jid5OiUopoqcxNqJbc8ichnnf | ⏳ 会议纪要 |
| 26  | 近期会议速递｜要点概览 2025年1月27日            | FeykdvimxoVR6qxCjtAcpMFinxe | ⏳ 会议纪要 |
| 27  | 近期会议速递｜要点概览 2025年1月20日            | DCOHdnmZKoZE21xlQ01c7d3Unoe | ⏳ 会议纪要 |
| 28  | 近期会议速递｜要点概览 2025年1月13日            | PQffdQ2NOo3Txyx10TVcQ3UYnbg | ⏳ 会议纪要 |
| 29  | 近期会议速递｜要点概览 2025年1月6日             | L35XdsGSSoygobxzcHjctf4Mnjd | ⏳ 会议纪要 |
| 30  | 近期会议速递｜要点概览 2024年12月30日           | W7MhdWyHeoTWeZxbwVbcG6Whndh | ⏳ 会议纪要 |
| 31  | 2024年终总结                          | RNoYdOrHAoMJchxEtFJc2zHonkX | ✅ 已迁移 |
| 32  | 部门季报/半年报/年报                       | AuQldFCasoVwtLxNejocWWv8nqg | ✅ 已迁移 |
| 33  | 近期会议速递｜要点概览 2024年12月23日           | BGWhdLW32oWgRgxno7ncyfNNnSd | ⏳ 会议纪要 |
| 34  | 近期会议速递｜要点概览 2024年12月16日           | Z21kdH9RRoWSlXxKCllcwOp9nxe | ⏳ 会议纪要 |
| 35  | 平台地图最新使用                          | QbGcdI4iDok1XPxFdEUckHemnR5 | ✅ 已迁移 |
| 36  | 车间定位项目立项报告                        | Iw5cdoeumo3fVhxCZjYcw8j4nBc | ✅ 已迁移 |
| 37  | 小程序签到功能方案                         | GxYfddex4oDcpUxG0JHcGbZEndg | ✅ 已迁移 |
| 38  | 三方系统调用行李查询接口文档(座位号)20230804       | E3UidCx5No6qqnx2VgjcXVzdnsg | ✅ 已迁移 |
| 39  | 招标需求                              | NQXudjxpjo39fpxEYencmva4nke | ✅ 已迁移 |
| 40  | 招标需求                              | DYRPdzdhIo9lwQxVESDcUY4inhc | ✅ 已迁移 |
| 41  | 大屏页面问题                            | OVEnde4fhoJnAPxjgr9c2WZfnIc | ✅ 已迁移 |
| 42  | 大屏页面问题                            | HdftdeOzfobWS1xbkzecCE0unsn | ✅ 已迁移 |
| 43  | 大屏页面问题                            | HJB5dyyhmoqQAVxTE89cjIv6n1f | ✅ 已迁移 |
| 44  | 大屏页面问题                            | NxFEdepRNoHgzzx8XjxczSuhnwI | ✅ 已迁移 |
| 45  | 后端翻译                              | XULYdzrgOoC9TpxsG2GcTFBJnLf | ✅ 已迁移 |

#### bitable 多维表格

| # | 标题 | Token | 飞书链接 |
|---|------|-------|----------|
| 1 | 需求及 Bug 管理 | ZmmjbljSpa3KWBskm40cPgWGnPg | https://reliablesense.feishu.cn/base/ZmmjbljSpa3KWBskm40cPgWGnPg |
| 2 | 需求及 Bug 管理 | BSDnb80vUaGm4hsjM06cIE0bncD | https://reliablesense.feishu.cn/base/BSDnb80vUaGm4hsjM06cIE0bncD |

#### sheet 电子表格

| # | 标题 | Token | 飞书链接 |
|---|------|-------|----------|
| 1 | oemusers | GBc0sFzfKhEtBztmsAPcp5m5n4w | https://reliablesense.feishu.cn/sheets/GBc0sFzfKhEtBztmsAPcp5m5n4w |
| 2 | 问题记录-2023-09-22 | ILedsU7eShMXojtZmy0cTiHln9c | https://reliablesense.feishu.cn/sheets/ILedsU7eShMXojtZmy0cTiHln9c |
| 3 | 室内定位系统工作进度 | Xl6HsOeCMhUrDwtMewMcElDGnyd | https://reliablesense.feishu.cn/sheets/Xl6HsOeCMhUrDwtMewMcElDGnyd |
| 4 | t_poi_type | EKkcsQr7MhV8S7teOsTcf1ISnUc | https://reliablesense.feishu.cn/sheets/EKkcsQr7MhV8S7teOsTcf1ISnUc |

#### file 附件

| # | 标题 | Token | 飞书链接 |
|---|------|-------|----------|
| 1 | 核心物联资料.zip | MAbLblaVGoQUsEx9a4NcxF5Kn0g | https://reliablesense.feishu.cn/file/MAbLblaVGoQUsEx9a4NcxF5Kn0g |
| 2 | 2023-05-07 20-54-59.mkv | BRc2bmrbKoPzjvxIKmPcBoOFnof | https://reliablesense.feishu.cn/file/BRc2bmrbKoPzjvxIKmPcBoOFnof |

---

### 📁 孙永霖的个人文档 (`RnBRfKciKlzViDd4tW7cxPCsn1f`)

#### 子文件夹列表

| # | 文件夹名 | Token |
|---|---------|-------|
| 1 | doc | fldcnBIdAvAj4Yx8ahqbrsyHOMd |
| 2 | 地图管理问题 | fldcn3r4SKlOJPbnePvoZ1mv0me |

#### docx 文档

| # | 标题 | Token | 状态 |
|---|------|-------|------|
| 1 | 需翻译！！Matthias 英文稿 - 已翻译 | ZYXldX00mosg8cxjIAucj6pPnRc | ✅ 已迁移 |
| 2 | 需翻译！！Matthias 英文稿 | Ks4UdBsYPoMzuaxAqvpcVabDnFd | ✅ 已迁移 |

---

## 二、知识库（reliablesense.feishu.cn）

通过 `wiki.v2.space.list` 获取团队知识库，`wiki.v2.spaceNode.list` 遍历完整节点树，`wiki.v1.node.search` + `wiki.v2.space.getNode` 补充个人/受限知识库。

知识库总览：
- 团队知识库（space.list 可列出）：3 个（技术分享、项目管理、规章制度）
- 个人/受限知识库（通过搜索发现）：9 个
- 总节点数：~113
- 可遍历节点：~102（通过 spaceNode.list）
- 仅通过 getNode 可访问：~11（space 级别无权限，但单节点可读）

### 📚 技术分享 (Space `7065147197469458433`, team)

#### 根节点

| # | 标题 | Node Token | Token (obj) | obj_type | has_child | 飞书链接 | 状态 |
|---|------|-----------|----------|----------|-----------|----------|------|
| 1 | 地图相关文档 | wikcnsyU0eYzKrwUSEnn8IaU62c | doccnhCl9hokfKaILbP59oauDQe | doc | ✅ | https://reliablesense.feishu.cn/wiki/wikcnsyU0eYzKrwUSEnn8IaU62c | 🔗 链接索引 |
| 2 | 前端相关文档 | wikcnkUzLRliQT2oLhwPyIPf93b | doccnZVmB4zMyd5vRGTAsFKOgYb | doc | ✅ | https://reliablesense.feishu.cn/wiki/wikcnkUzLRliQT2oLhwPyIPf93b | 🔗 链接索引 |
| 3 | 数据库相关文档 | wikcnixQRqf9WAUn27GaljFP9xe | doccnGq8IMFmjgrgloGuXAzvOCc | doc | ✅ | https://reliablesense.feishu.cn/wiki/wikcnixQRqf9WAUn27GaljFP9xe | 🔗 链接索引 |
| 4 | 硬件相关文档 | wikcnKNR23l94UjDLwZeYsAyuDe | doccnfb9EwlR5aYvjxzJbUwtlJh | doc | ✅ | https://reliablesense.feishu.cn/wiki/wikcnKNR23l94UjDLwZeYsAyuDe | 🔗 链接索引 |
| 5 | 后端相关文档 | wikcnfRuSAV2GcusBVxUx1jGFUf | doccnnHFcpyirHhQWM3GZh4mkQg | doc | ✅ | https://reliablesense.feishu.cn/wiki/wikcnfRuSAV2GcusBVxUx1jGFUf | 🔗 链接索引 |
| 6 | 基础平台相关文档 | wikcnqvwxuVRYnrITuhPdah6tXc | doccnlJ8hk4ih92ZXrCFLFc9Zid | doc | ✅ | https://reliablesense.feishu.cn/wiki/wikcnqvwxuVRYnrITuhPdah6tXc | 🔗 链接索引 |
| 7 | 测试相关文档 | wikcnjrlWGjZqbYO2JYyhn7QrSh | doccnxeb0O7SDyKIHQDwBWTL3ie | doc | ✅ | https://reliablesense.feishu.cn/wiki/wikcnjrlWGjZqbYO2JYyhn7QrSh | 🔗 链接索引 |
| 8 | 日常运维相关文档 | ENSywo9uHihAmMkXZ6zcftDrnFV | UtKfd14RVooqIvxlDjucNlaSnjd | docx | — | https://reliablesense.feishu.cn/wiki/ENSywo9uHihAmMkXZ6zcftDrnFV | ✅ 已迁移 |
| 9 | 后端问题Q/A | NW6zwyxHmiD7v8kHfOBca81hnzb | OpsxdI417oi5i4xLyrhc8Znyn5f | docx | — | https://reliablesense.feishu.cn/wiki/NW6zwyxHmiD7v8kHfOBca81hnzb | ✅ 已迁移 |

#### 地图相关文档 子节点

| # | 标题 | Node Token | Token (obj) | obj_type | 飞书链接 | 状态 |
|---|------|-----------|----------|----------|----------|------|
| 1 | 项目建立步骤 | Fw8MwbW40inLaxkekY4cXmqRngg | LapVd88f0oFaKUx4QwRcwrW1neI | docx | https://reliablesense.feishu.cn/wiki/Fw8MwbW40inLaxkekY4cXmqRngg | ✅ 已迁移 |
| 2 | QGIS安装 | DW3dwVhP5i7vrwkI090cqUPcnSd | DKP6dIPIHoXYuMxJ5Xoc00LVngp | docx | https://reliablesense.feishu.cn/wiki/DW3dwVhP5i7vrwkI090cqUPcnSd | ✅ 已迁移 |
| 3 | QGIS地图绘制注意事项（CAD版） | wikcnOXgiztoNkHOs9FOhTaqQag | doccnKYx4RPxYSXzTH0ssUvvBmf | doc | https://reliablesense.feishu.cn/wiki/wikcnOXgiztoNkHOs9FOhTaqQag | 🔗 链接索引 |
| 4 | 麦钉点云图地图绘制注意事项（点云图版） | wikcnwAeT2GA0B7hl5mATlZBaEd | doccn6HL7llLqfP4e5qCI96CdUf | doc | https://reliablesense.feishu.cn/wiki/wikcnwAeT2GA0B7hl5mATlZBaEd | 🔗 链接索引 |
| 5 | QGIS画图说明（详细）.docx | wikcnmIywQmX161Ck8nmngaQpwh | boxcnfcMTBDnuvLMZbMCPWu4p4g | file | https://reliablesense.feishu.cn/wiki/wikcnmIywQmX161Ck8nmngaQpwh | 🔗 保留链接 |
| 6 | 路网绘制 | wikcne2NQ2nTe07LW7d2fNs4qpc | doxcnmMiCtaR2HkpnlPPrChqyEb | docx | https://reliablesense.feishu.cn/wiki/wikcne2NQ2nTe07LW7d2fNs4qpc | ✅ 已迁移 |
| 7 | 地图按钮、视角、控件控制 | IRYzwhW7SiquPtkXevbcRwq8nvc | HUTId5xjFoaRIxxUkQWcEb1Xnge | docx | https://reliablesense.feishu.cn/wiki/IRYzwhW7SiquPtkXevbcRwq8nvc | ✅ 已迁移 |
| 8 | QGIS图片及瓦片图添加 | FQMrwJYQQi71zOkhYezcta2BnMc | X68Zdyv98o4AgGx073LcsrscnAh | docx | https://reliablesense.feishu.cn/wiki/FQMrwJYQQi71zOkhYezcta2BnMc | ✅ 已迁移 |
| 9 | png图片导入地图（参考不是我们的系统） | wikcn6SDsrfRKEDqyDvg8UvJKHd | doccn3DidLn9ur0mvFbqsnXhstd | doc | https://reliablesense.feishu.cn/wiki/wikcn6SDsrfRKEDqyDvg8UvJKHd | 🔗 链接索引 |
| 10 | 瓦片图制作 | Ah0RwVteKibIuXkCzRYckwd2nhh | OvGsdeF3UoAgULxqd9Kc08punEg | docx | https://reliablesense.feishu.cn/wiki/Ah0RwVteKibIuXkCzRYckwd2nhh | ✅ 已迁移 |
| 11 | QGIS地图绘制准备 | VuwLwLCAaisQefkpvTHcRe1tnVe | CXjHdQO7JogckXxR6owcL5AcnEb | docx | https://reliablesense.feishu.cn/wiki/VuwLwLCAaisQefkpvTHcRe1tnVe | ✅ 已迁移 |

#### 前端相关文档 子节点

| # | 标题 | Node Token | Token (obj) | obj_type | 飞书链接 | 状态 |
|---|------|-----------|----------|----------|----------|------|
| 1 | 前端 React 开发规范 | wikcnspxL6qlUtrWgmRVWORf0Xe | doccnymhDUxjzJsBjuZ5mBGpG4c | doc | https://reliablesense.feishu.cn/wiki/wikcnspxL6qlUtrWgmRVWORf0Xe | 🔗 链接索引 |

#### 数据库相关文档 子节点

##### Postgres (`wikcnVJrx5Q8y474gHMmalqWg73`, doc)

| # | 标题 | Node Token | Token (obj) | obj_type | 飞书链接 | 状态 |
|---|------|-----------|----------|----------|----------|------|
| 1 | 生成UUID | wikcngXQDl6DfjjniOLkaXVQGnx | doccnKzX7vdTlRNlsKlQY9oo9vd | doc | https://reliablesense.feishu.cn/wiki/wikcngXQDl6DfjjniOLkaXVQGnx | 🔗 链接索引 |
| 2 | 生成 trigger_set_timestamp | wikcnqmSBcurbVVatiPSVkhvaJk | doccnszyZqVAlZhQ6yFE8iVp3uf | doc | https://reliablesense.feishu.cn/wiki/wikcnqmSBcurbVVatiPSVkhvaJk | 🔗 链接索引 |
| 3 | 处理 t_position 的 id "not null" 的问题 | wikcnIstgnXcTT02lRl6Vv1Uxkc | doccnDPxocYNEJe0c7YYnRI6R3e | doc | https://reliablesense.feishu.cn/wiki/wikcnIstgnXcTT02lRl6Vv1Uxkc | 🔗 链接索引 |
| 4 | 处理连接数的问题 | wikcn9cIwQEuooi5CWUVZs1hkXU | doccnZIMQSFgw5z9FAtvRxqEF4f | doc | https://reliablesense.feishu.cn/wiki/wikcn9cIwQEuooi5CWUVZs1hkXU | 🔗 链接索引 |

##### Postgis (`wikcnAmEcHh2yVPmpoO7wLatPBb`, doc)

| # | 标题 | Node Token | Token (obj) | obj_type | 飞书链接 | 状态 |
|---|------|-----------|----------|----------|----------|------|
| 1 | 更新地图中点和边界 | wikcnujbyBxlVvXGkrCOTRmpjmd | doccnI6f4RL5XRKR8R2k2oA6Ykf | doc | https://reliablesense.feishu.cn/wiki/wikcnujbyBxlVvXGkrCOTRmpjmd | 🔗 链接索引 |
| 2 | 移动缩放旋转地图 | wikcn4v2EUFhaJ2mMyL6TlDZ8Ue | doccnN1mQdwwDwXCsBhuSsVzTId | doc | https://reliablesense.feishu.cn/wiki/wikcn4v2EUFhaJ2mMyL6TlDZ8Ue | 🔗 链接索引 |
| 3 | 移动电子围栏到火星坐标 | wikcnRhtsNYFu5cgAIvF8HXBZzb | doccnvu9gfk9NPRnE1FMF7fpNFe | doc | https://reliablesense.feishu.cn/wiki/wikcnRhtsNYFu5cgAIvF8HXBZzb | 🔗 链接索引 |
| 4 | 修改火星坐标完整语句(旧架构) | wikcn1iBq3pcLMxYLT8Zkt0Tebe | doccnZUAaAKBqN3uCPCiAHkWo30 | doc | https://reliablesense.feishu.cn/wiki/wikcn1iBq3pcLMxYLT8Zkt0Tebe | 🔗 链接索引 |
| 5 | 偏移位置数据到火星坐标 | wikcnscV1LKfr0QuNP7s4lfXwvg | doccn4JOodvetnzvaKMfs3aIBSh | doc | https://reliablesense.feishu.cn/wiki/wikcnscV1LKfr0QuNP7s4lfXwvg | 🔗 链接索引 |
| 6 | 火星坐标转换 | wikcnOERwkqZPArkCAY4lK1xMfb | doccnbSee08xdsJhTWt1nXJccZc | doc | https://reliablesense.feishu.cn/wiki/wikcnOERwkqZPArkCAY4lK1xMfb | 🔗 链接索引 |
| 7 | 获取指定范围内的点 | wikcnU17illWrHsuZBjC8NmFpic | doccnhqA2pLGKjd5fnqdDsdRbig | doc | https://reliablesense.feishu.cn/wiki/wikcnU17illWrHsuZBjC8NmFpic | 🔗 链接索引 |
| 8 | 将Point转成PointZ | wikcnrI9pMiNAJ69RUUPAWSKGAe | doccnZTs4pwAZPya8zQfIgRf7Yf | doc | https://reliablesense.feishu.cn/wiki/wikcnrI9pMiNAJ69RUUPAWSKGAe | 🔗 链接索引 |

##### TimescaleDB (`wikcni90D268LpTPiEJKSqkM3Vb`, doc)

| # | 标题 | Node Token | Token (obj) | obj_type | 飞书链接 | 状态 |
|---|------|-----------|----------|----------|----------|------|
| 1 | 新建hyper_table时，Trigger "ts_insert_blocker"错误 | wikcnXxfOQCGo9QFhsPQerICWgh | doccnoNAhwDhgg2FpnJ5jOODzZb | doc | https://reliablesense.feishu.cn/wiki/wikcnXxfOQCGo9QFhsPQerICWgh | 🔗 链接索引 |
| 2 | Retention policy，定期删除机制 | wikcnAWFOCd4jtv1WIxxaKCQ9ui | doccn2mQON8tP7m08bYrNmq5BYc | doc | https://reliablesense.feishu.cn/wiki/wikcnAWFOCd4jtv1WIxxaKCQ9ui | 🔗 链接索引 |
| 3 | 如何实现人员、物体每日在线时间统计 | wikcnmnlgVJKu9VoUXL200yokXe | doccnSG2Jc0Fls0feLdgve23DOe | doc | https://reliablesense.feishu.cn/wiki/wikcnmnlgVJKu9VoUXL200yokXe | 🔗 链接索引 |
| 4 | 插入一条t_position数据 | wikcnNqMmyJ88VjScpsZfGe548e | doccnmbpSo3CRnCMyTYEVFTpbIi | doc | https://reliablesense.feishu.cn/wiki/wikcnNqMmyJ88VjScpsZfGe548e | 🔗 链接索引 |

#### 硬件相关文档 子节点

| # | 标题 | Node Token | Token (obj) | obj_type | 飞书链接 | 状态 |
|---|------|-----------|----------|----------|----------|------|
| 1 | RTK设备局域网WiFi使用文档V1.1 | wikcnZt2mzudfssGSngwn2SPEgc | Yr5vdDP3YonYuWxkhZ3cfDGDnGd | docx | https://reliablesense.feishu.cn/wiki/wikcnZt2mzudfssGSngwn2SPEgc | ✅ 已迁移 |
| 2 | 烧写设备 | wikcnL0WUbCN7nutgfe20tstRzV | NigodFqlcowXQVxYWh5cVyoDn2g | docx | https://reliablesense.feishu.cn/wiki/wikcnL0WUbCN7nutgfe20tstRzV | ✅ 已迁移 |
| 3 | 树莓派 SSD 版本安装 | E5bKw98fhii1ZmkpM4TcqL96nbe | YUSVdEwLVooPMHx3luMcAXh6nlh | docx | https://reliablesense.feishu.cn/wiki/E5bKw98fhii1ZmkpM4TcqL96nbe | ✅ 已迁移 |
| 4 | MOKO RSSI 定位基站与树莓派组网 | TxsmwZNpMiU8I5kAH3XcMb4hnyc | TDS8dDE7ToGtUWxMvu7c8bROnwf | docx | https://reliablesense.feishu.cn/wiki/TxsmwZNpMiU8I5kAH3XcMb4hnyc | ✅ 已迁移 |
| 5 | (无标题) | EK9EwdPiMiU1xUk8isEcTe2aneh | UNtZdtZjhoZCEIxSHEacw1e0nyf | docx | https://reliablesense.feishu.cn/wiki/EK9EwdPiMiU1xUk8isEcTe2aneh | 🔗 链接索引 |

#### 后端相关文档 子节点

| # | 标题 | Node Token | Token (obj) | obj_type | 飞书链接 | 状态 |
|---|------|-----------|----------|----------|----------|------|
| 1 | JAVA开发手册.pdf | wikcnWgIKCFhzgVEN8EJ4hO7Ucf | boxcntXN1LT755OgcYuMHHfGhUR | file | https://reliablesense.feishu.cn/wiki/wikcnWgIKCFhzgVEN8EJ4hO7Ucf | 🔗 保留链接 |
| 2 | 定位平台系统整体改造方案 | wikcnxzCMQulAARtDyfkRDgd50f | doccnVRMcLTfhON3R9OLZT7VHgf | doc | https://reliablesense.feishu.cn/wiki/wikcnxzCMQulAARtDyfkRDgd50f | 🔗 链接索引 |
| 3 | 后端开发流程规范 | wikcn6Bh2oD6cUp1yrODCPOM2qh | CUA7dlJrRoTZ3Fx8t5kc1UiRneb | docx | https://reliablesense.feishu.cn/wiki/wikcn6Bh2oD6cUp1yrODCPOM2qh | ✅ 已迁移 |
| 4 | 微服务说明 | GKGmwu9YBibrqkk6AJucGBqGngb | F2PhdYeMCoHjP6xd8y0cyz6Mnac | docx | https://reliablesense.feishu.cn/wiki/GKGmwu9YBibrqkk6AJucGBqGngb | ✅ 已迁移 |

#### 基础平台相关文档 子节点

| # | 标题 | Node Token | Token (obj) | obj_type | has_child | 飞书链接 | 状态 |
|---|------|-----------|----------|----------|-----------|----------|------|
| 1 | CI/CD流程介绍 | wikcn1AfPcjP7uzvomNTgpH4GVd | doccnqi4YxvSVSY23MSLXIkwIKe | doc | — | https://reliablesense.feishu.cn/wiki/wikcn1AfPcjP7uzvomNTgpH4GVd | 🔗 链接索引 |
| 2 | Gitlab CI/CD说明 | wikcnfTITMB8SHFIYJpy55dEJnd | doccnUileviuvksypU7AAbSEGwg | doc | ✅ | https://reliablesense.feishu.cn/wiki/wikcnfTITMB8SHFIYJpy55dEJnd | 🔗 链接索引 |
| 3 | 开发分支管理规范 | wikcnvRUrCKYizkTNNFDlMVOAfg | doccnlE0yWc24L79rE98oSVsY8d | doc | — | https://reliablesense.feishu.cn/wiki/wikcnvRUrCKYizkTNNFDlMVOAfg | 🔗 链接索引 |
| 4 | 私有化部署 | wikcnauUEEAen7cTVwneQruu0Pb | doxcn0gIaETOcyD1LPWPzUjSBTd | docx | ✅ | https://reliablesense.feishu.cn/wiki/wikcnauUEEAen7cTVwneQruu0Pb | ✅ 已迁移 |
| 5 | Deployment-English Version | LsYDwKdh9ik0qXkGz4QcKndinQb | Lm19danLpoBMNixbpIxcrSVtn1b | docx | ✅ | https://reliablesense.feishu.cn/wiki/LsYDwKdh9ik0qXkGz4QcKndinQb | ✅ 已迁移 |
| 6 | 办公网VPN手册 | wikcnxjaAkdiXVbLMrRbIutJYze | I3SHdzjW6oRYcWxAaHQcGFDansT | docx | ✅ | https://reliablesense.feishu.cn/wiki/wikcnxjaAkdiXVbLMrRbIutJYze | ✅ 已迁移 |

##### Gitlab CI/CD说明 子节点

| # | 标题 | Node Token | Token (obj) | obj_type | 飞书链接 | 状态 |
|---|------|-----------|----------|----------|----------|------|
| 1 | 前/后端 CI/CD | wikcnv7Dtt3zEVyTL8AuEj2Yy7g | doccncqa7DwRv2fD3Z3KA6oO4oh | doc | https://reliablesense.feishu.cn/wiki/wikcnv7Dtt3zEVyTL8AuEj2Yy7g | 🔗 链接索引 |

##### 私有化部署 子节点

| # | 标题 | Node Token | Token (obj) | obj_type | 飞书链接 | 状态 |
|---|------|-----------|----------|----------|----------|------|
| 1 | A. 服务器环境准备 | wikcnvUX6f3VFJZ8uMUNP5UKrXe | doxcniK4NdHGlK7G8gccJ5WYnEg | docx | https://reliablesense.feishu.cn/wiki/wikcnvUX6f3VFJZ8uMUNP5UKrXe | ✅ 已迁移 |
| 2 | B.1. 集群搭建[K3s] (在线版) | wikcnMjGUant3OpbEaUncdquAbg | doxcn67UW5vdFM5qaPG3tc9zMdd | docx | https://reliablesense.feishu.cn/wiki/wikcnMjGUant3OpbEaUncdquAbg | ✅ 已迁移 |
| 3 | B.2. 集群搭建[K3s] (离线版) | wikcnoMmmrEUo2bgOLcESnNBhQe | SuiNdHlegogxpcxnqqhc8AuKnZ1 | docx | https://reliablesense.feishu.cn/wiki/wikcnoMmmrEUo2bgOLcESnNBhQe | ✅ 已迁移 |
| 4 | C. 集群内基础服务安装 | wikcnMEraAPj2mBXidl3KhbCNlc | doxcnSbULW58Lp1lXBy2tt8i80e | docx | https://reliablesense.feishu.cn/wiki/wikcnMEraAPj2mBXidl3KhbCNlc | ✅ 已迁移 |
| 5 | 命令行工具 oemctl | TIoMwLsjAi6qr9kYRCEcql2dnTb | J1C8daWxto4clexYnaDcKtgQnzf | docx | https://reliablesense.feishu.cn/wiki/TIoMwLsjAi6qr9kYRCEcql2dnTb | ✅ 已迁移 |

##### Deployment-English Version 子节点

| # | 标题 | Node Token | Token (obj) | obj_type | 飞书链接 | 状态 |
|---|------|-----------|----------|----------|----------|------|
| 1 | A. Server environment preparation | FZdtwpJutirA7QkcpA8c9KM1nXe | CWnsdq3ryoYTSHxGAC0cpcoenbg | docx | https://reliablesense.feishu.cn/wiki/FZdtwpJutirA7QkcpA8c9KM1nXe | ✅ 已迁移 |
| 2 | B.1. Cluster setup [K3s] (online version) | YSIKw2tR8igrlDktqgmcIwwbn2b | Kgifd4mPJo5nuVxkmX2cF76unde | docx | https://reliablesense.feishu.cn/wiki/YSIKw2tR8igrlDktqgmcIwwbn2b | ✅ 已迁移 |
| 3 | B.2. Cluster setup [K3s] (offline version) | YbQcwsCptisqkdk3SWFcopjHnvg | NQgadYYYJo5e4sxLhxMcLMZ9nGB | docx | https://reliablesense.feishu.cn/wiki/YbQcwsCptisqkdk3SWFcopjHnvg | ✅ 已迁移 |
| 4 | C. Installation of basic services within the cluster | TFnuwaxRriELjQkuyUocgyhOnjf | MXFDdnQvAoKSMAxxdAXc2I9bnYb | docx | https://reliablesense.feishu.cn/wiki/TFnuwaxRriELjQkuyUocgyhOnjf | ✅ 已迁移 |

##### 办公网VPN手册 子节点

| # | 标题 | Node Token | Token (obj) | obj_type | 飞书链接 | 状态 |
|---|------|-----------|----------|----------|----------|------|
| 1 | 办公网v2ray操作手册 | wikcnYkN6s2wJU7Mg2O1ElNoT4c | G1OBdhlTSotGV6xRToRcXlzWnoe | docx | https://reliablesense.feishu.cn/wiki/wikcnYkN6s2wJU7Mg2O1ElNoT4c | ✅ 已迁移 |
| 2 | 办公网WireGuard操作手册 | wikcnEwrC67xGlAMLxCkttzewsb | Q4OzdL6ZboG5dSxgqqlcNn4WnFf | docx | https://reliablesense.feishu.cn/wiki/wikcnEwrC67xGlAMLxCkttzewsb | ✅ 已迁移 |

#### 测试相关文档 子节点

| # | 标题 | Node Token | Token (obj) | obj_type | has_child | 飞书链接 | 状态 |
|---|------|-----------|----------|----------|-----------|----------|------|
| 1 | 测试流程1 | wikcng0FqNpajFPemHO3xNQPUle | doccnvKjRt0RgI04vi1UFEuAW4f | doc | — | https://reliablesense.feishu.cn/wiki/wikcng0FqNpajFPemHO3xNQPUle | 🔗 链接索引 |
| 2 | 测试管理规范.doc | wikcnikePj6eb5QoEOYZNdxu8Md | boxcno1BITT4pkz5F6Oq4YuRjgd | file | — | https://reliablesense.feishu.cn/wiki/wikcnikePj6eb5QoEOYZNdxu8Md | 🔗 保留链接 |
| 3 | 测试的流程及内容 | wikcn3opk036dWpAkU4yOEb91fi | doccnUSmCPXtSpHsITXo3gMqtqd | doc | — | https://reliablesense.feishu.cn/wiki/wikcn3opk036dWpAkU4yOEb91fi | 🔗 链接索引 |
| 4 | 测试计划（初稿） | wikcneJwlPPT9hSaaQQLlVRVWbd | doccnXKbFqjR5Up9dVYrzjvUUmh | doc | — | https://reliablesense.feishu.cn/wiki/wikcneJwlPPT9hSaaQQLlVRVWbd | 🔗 链接索引 |
| 5 | 测试平台对比 | wikcnPCulBP9nuK1we7GZP8OMgd | doccnoMeCyK1lHtPzzIxxZTmB8U | doc | — | https://reliablesense.feishu.cn/wiki/wikcnPCulBP9nuK1we7GZP8OMgd | 🔗 链接索引 |
| 6 | 禅道测试相关操作手册 | wikcnAEHs629QoVPT40ZCpOGLog | doccnTqc7EnZxfZYH0T20rXWLVe | doc | — | https://reliablesense.feishu.cn/wiki/wikcnAEHs629QoVPT40ZCpOGLog | 🔗 链接索引 |
| 7 | 性能测试 | wikcnq3SiaY6yUonTyDWxGj8Zjg | doxcnRNCrffisaiX1R2DA9YBcTc | docx | ✅ | https://reliablesense.feishu.cn/wiki/wikcnq3SiaY6yUonTyDWxGj8Zjg | ✅ 已迁移 |

##### 性能测试 子节点

| # | 标题 | Node Token | Token (obj) | obj_type | 飞书链接 | 状态 |
|---|------|-----------|----------|----------|----------|------|
| 1 | 稳定性测试 | wikcnNPUssjUwOf9Ol3BUOGeVde | doxcnPMwcMjDrt0cdQBUlY9Jldf | docx | https://reliablesense.feishu.cn/wiki/wikcnNPUssjUwOf9Ol3BUOGeVde | ✅ 已迁移 |
| 2 | locust报告参数说明 | wikcnE7Y32JZlQ4eiMSfkfTelFe | doxcnyVpKX1V11tJYH2sKdff3Ph | docx | https://reliablesense.feishu.cn/wiki/wikcnE7Y32JZlQ4eiMSfkfTelFe | ✅ 已迁移 |

---

### 📚 项目管理 (Space `7445886335376523292`, team)

| # | 标题 | Node Token | Token (obj) | obj_type | has_child | 飞书链接 | 状态 |
|---|------|-----------|----------|----------|-----------|----------|------|
| 1 | 项目启动 | XXBIwuZzmiCxfqkwDOVcO6DqnEc | EGXddWSPeoMgiVxG4YIcm4ywnud | docx | — | https://reliablesense.feishu.cn/wiki/XXBIwuZzmiCxfqkwDOVcO6DqnEc | ✅ 已迁移 |
| 2 | 项目规划 | IkiEw4MTPieyHrkEcIhcLXGingh | JoYzdWiuUoTsEhx1c0BcK4fCnhc | docx | — | https://reliablesense.feishu.cn/wiki/IkiEw4MTPieyHrkEcIhcLXGingh | ✅ 已迁移 |
| 3 | 项目甘特图 | Nw5gwHmWTifcYxkqjPjcWFXlnyc | Pn2Rs9RZvhM3jYtYnJoc6cJQnQd | sheet | — | https://reliablesense.feishu.cn/wiki/Nw5gwHmWTifcYxkqjPjcWFXlnyc | 🔗 保留链接 |
| 4 | 团队会议 | P7brwY9LkiEslFkgolZcKnubn6c | CfePdOJvxoscSrxXLFFczDUznig | docx | ✅ | https://reliablesense.feishu.cn/wiki/P7brwY9LkiEslFkgolZcKnubn6c | ✅ 已迁移 |
| 5 | 项目复盘 | O3eLw6EjDiNBmpk4zNNcO1WnnJc | DhkPdNvBooRivhxL5kMcfjm1nCf | docx | ✅ | https://reliablesense.feishu.cn/wiki/O3eLw6EjDiNBmpk4zNNcO1WnnJc | ✅ 已迁移 |
| 6 | 文档模版 | Qb9kwDROEiR50MknBEJcI2K1nQc | Y0F7diEjXo2S0hxCo4ucoYSTnFd | docx | — | https://reliablesense.feishu.cn/wiki/Qb9kwDROEiR50MknBEJcI2K1nQc | ✅ 已迁移 |
| 7 | 售前项目 | JEWDwuaz7iT5m2kq5c0c5ScAnOh | OujDdgCTHoXRPzxGLf8cp76pnHc | docx | — | https://reliablesense.feishu.cn/wiki/JEWDwuaz7iT5m2kq5c0c5ScAnOh | 🔗 链接索引 |
| 8 | 售中项目 | Dr2qwhgN5i9y0Uks7YpcH5panHf | BREFdC7hBouQESxhGJzcFLWSn6e | docx | — | https://reliablesense.feishu.cn/wiki/Dr2qwhgN5i9y0Uks7YpcH5panHf | 🔗 链接索引 |
| 9 | 售后项目 | RDCHwOqDFiqIbBkDbeZchAo6nCf | Tu7EdgwvooFo5oxVZX2c4RWlnjA | docx | — | https://reliablesense.feishu.cn/wiki/RDCHwOqDFiqIbBkDbeZchAo6nCf | 🔗 链接索引 |

#### 团队会议 子节点

| # | 标题 | Node Token | Token (obj) | obj_type | 飞书链接 | 状态 |
|---|------|-----------|----------|----------|----------|------|
| 1 | 每日进展同步 | MzPPw96cFiZzQnkQg9ccE1i6n0f | XPxZdbSObovcRZxyoFdcqnvlnhe | docx | https://reliablesense.feishu.cn/wiki/MzPPw96cFiZzQnkQg9ccE1i6n0f | ✅ 已迁移 |
| 2 | 团队周会 | BFEMwNek2izj1wkluMYcC9WynJh | MNAVdRNXqoIQ92x3MkfcrCWfnTf | docx | https://reliablesense.feishu.cn/wiki/BFEMwNek2izj1wkluMYcC9WynJh | ✅ 已迁移 |

#### 项目复盘 子节点

| # | 标题 | Node Token | Token (obj) | obj_type | 飞书链接 | 状态 |
|---|------|-----------|----------|----------|----------|------|
| 1 | 项目实施部署问题复盘 | UMvfwLQ9FiKN43k4ls7cRQInnih | DT9Gd930poFinbxbeIQcv6wZnJ2 | docx | https://reliablesense.feishu.cn/wiki/UMvfwLQ9FiKN43k4ls7cRQInnih | 🔗 链接索引 |

---

### 📚 规章制度 (Space `7066050160966516764`, team)

| # | 标题 | Node Token | Token (obj) | obj_type | has_child | 飞书链接 | 状态 |
|---|------|-----------|----------|----------|-----------|----------|------|
| 1 | 人力资源制度 | wikcnJIcJQvqJJXJ7A25QYmCTDc | doccnw7E90pRZqZbad9ZqMraele | doc | ✅ | https://reliablesense.feishu.cn/wiki/wikcnJIcJQvqJJXJ7A25QYmCTDc | 🔗 链接索引 |
| 2 | 财务制度 | wikcnn9rN6gVZXVRdHcqu6QMOph | doccn1pktcI7i62LgQO3wTFvCDh | doc | — | https://reliablesense.feishu.cn/wiki/wikcnn9rN6gVZXVRdHcqu6QMOph | 🔗 链接索引 |
| 3 | 法务制度 | wikcnh9IhuLrBfkAeUMCQhZDHCb | doccn2IXTE0xjbI4zNUzhNjdOCc | doc | — | https://reliablesense.feishu.cn/wiki/wikcnh9IhuLrBfkAeUMCQhZDHCb | 🔗 链接索引 |
| 4 | 公关制度 | wikcnUSiOFEFp7mvFYICWsSkHxh | doccn8tPZL9k9QZy2MzWif1qWDb | doc | — | https://reliablesense.feishu.cn/wiki/wikcnUSiOFEFp7mvFYICWsSkHxh | 🔗 链接索引 |
| 5 | 采购制度 | wikcnWKYA5VzSsah041ULifZnbh | doccnNlv7YbCNSsWjdLnLTkRYWb | doc | — | https://reliablesense.feishu.cn/wiki/wikcnWKYA5VzSsah041ULifZnbh | 🔗 链接索引 |

#### 人力资源制度 子节点

| # | 标题 | Node Token | Token (obj) | obj_type | 飞书链接 | 状态 |
|---|------|-----------|----------|----------|----------|------|
| 1 | 员工管理制度 | wikcnHzVUBllcL5dcNFvWMe2cBc | doccn2AHiWmD3UQoSfsKJOWsTkc | doc | https://reliablesense.feishu.cn/wiki/wikcnHzVUBllcL5dcNFvWMe2cBc | 🔗 链接索引 |
| 2 | 薪酬福利制度 | wikcnu2YMoUfFkRiTLD6p2NYUod | doccn1Ub5gQHHvFcnKIkDy1HNmc | doc | https://reliablesense.feishu.cn/wiki/wikcnu2YMoUfFkRiTLD6p2NYUod | 🔗 链接索引 |
| 3 | 绩效评估制度 | wikcnakqZiUVkeYxXNHpCIDjmlf | doccn7ZeBuL5f7dFVfYOl9ktgUg | doc | https://reliablesense.feishu.cn/wiki/wikcnakqZiUVkeYxXNHpCIDjmlf | 🔗 链接索引 |
| 4 | 人才政策制度 | wikcnt4hNsedpUPzHhSqEH8PqJf | doccnwBIuqGBMP6DDr49tpEK98J | doc | https://reliablesense.feishu.cn/wiki/wikcnt4hNsedpUPzHhSqEH8PqJf | 🔗 链接索引 |

---

### 📚 个人知识库（可遍历）

以下知识库未在 `wiki.v2.space.list` 中列出，但通过 `spaceNode.list` 可完整遍历。

#### Space `7559791731407912963`（9 节点）

| # | 标题 | Node Token | Token (obj) | obj_type | 飞书链接 | 状态 |
|---|------|-----------|----------|----------|----------|------|
| 1 | 运行有问题的项目及其结果截图 | SAC6wR9XXiiBAKk0uvAcBPI4nmd | YJjcdrAc5o7O7kxtR9Xc9jn9nOh | docx | https://reliablesense.feishu.cn/wiki/SAC6wR9XXiiBAKk0uvAcBPI4nmd | ✅ 已迁移 |
| 2 | 订阅压线事件 | UwMHwNSUxie9kNkrqVwc0SwOnKe | YcxMdvp8no99qkx56tncdG4gnpc | docx | https://reliablesense.feishu.cn/wiki/UwMHwNSUxie9kNkrqVwc0SwOnKe | ✅ 已迁移 |
| 3 | 车载定位连调总结 | I7C8w9kEBiLR3YkaRyJcbekunVf | F0Aad5kN5oj6BsxpFbfck2K0nAh | docx | https://reliablesense.feishu.cn/wiki/I7C8w9kEBiLR3YkaRyJcbekunVf | ✅ 已迁移 |
| 4 | Iot接口对接代码 | PJMvwq7JFipjUIkquXpcVEt2nUf | N4TLdj01ZoN4DvxpLjucSWwcnSF | docx | https://reliablesense.feishu.cn/wiki/PJMvwq7JFipjUIkquXpcVEt2nUf | ✅ 已迁移 |
| 5 | Rocket命令行测试 | NECEwJ2pUienKZkrcsRc6Pranyg | VvSpdgrK0orNMuxOEkbcegTpnqh | docx | https://reliablesense.feishu.cn/wiki/NECEwJ2pUienKZkrcsRc6Pranyg | ✅ 已迁移 |
| 6 | 测试总结 | Bv23wHWcfi8SuOkDS38c8TAynZc | WnVNdw684oR504x3AykcDWQAnhg | docx | https://reliablesense.feishu.cn/wiki/Bv23wHWcfi8SuOkDS38c8TAynZc | ✅ 已迁移 |
| 7 | 重定位 | EcASw46qMijgXFkNqQZcWstJnWe | H1nPdYtz8owyl6x9JEfc2ePQnGd | docx | https://reliablesense.feishu.cn/wiki/EcASw46qMijgXFkNqQZcWstJnWe | ✅ 已迁移 |
| 8 | 南宁机场2025年12月26日 | SLcMwfrKlibIwqkwU6ccaTVZnIc | RaiLdwavCo64ICxsJUGc4f41nKc | docx | https://reliablesense.feishu.cn/wiki/SLcMwfrKlibIwqkwU6ccaTVZnIc | ✅ 已迁移 |
| 9 | 工作交接 | KumhwCH0JiPH97k7CI5cOVcznsf | OY80dGte7oB63kxe6XlcK3tXnYJ | docx | https://reliablesense.feishu.cn/wiki/KumhwCH0JiPH97k7CI5cOVcznsf | ✅ 已迁移 |

#### Space `7527250303092015107`（2 节点）

| # | 标题 | Node Token | Token (obj) | obj_type | 飞书链接 | 状态 |
|---|------|-----------|----------|----------|----------|------|
| 1 | 知识问答 | Mb5Sw96iIiXgDkkgB79ciA13nph | BuUQdbBMWoaB6LxYN3YcA3FEn3f | docx | https://reliablesense.feishu.cn/wiki/Mb5Sw96iIiXgDkkgB79ciA13nph | ✅ 已迁移 |
| 2 | 费用报销单 | YDALwrkOgipenTkarYrcvNEEnPg | Obrtsq2GnhTDubtEQaucpakonZf | sheet | https://reliablesense.feishu.cn/wiki/YDALwrkOgipenTkarYrcvNEEnPg | 🔗 保留链接 |

#### Space `7527246326739157011`（2 节点）

| # | 标题 | Node Token | Token (obj) | obj_type | 飞书链接 | 状态 |
|---|------|-----------|----------|----------|----------|------|
| 1 | 知识问答 | AR6QwWP4yiUZUrku6F8c2LUvnDc | BLpTdACDWoAfURxRzP2cPeBmnzd | docx | https://reliablesense.feishu.cn/wiki/AR6QwWP4yiUZUrku6F8c2LUvnDc | ✅ 已迁移 |
| 2 | 视频会议助手与陈子杰的会话 2025年8月8日 | AH3AwTtFVizchQky49sc1R4vnYc | NQn2dUZh3otzcCxowijcMVx3nPg | docx | https://reliablesense.feishu.cn/wiki/AH3AwTtFVizchQky49sc1R4vnYc | ✅ 已迁移 |

---

### 📚 受限知识库（仅通过 getNode 可访问单节点）

以下知识库 `spaceNode.list` 返回权限不足，但通过搜索发现的节点可用 `getNode` 单独访问。可能无法获取完整节点列表。

#### Space `7527253598389125148`（已知 1 节点）

| # | 标题 | Node Token | Token (obj) | obj_type | 飞书链接 | 状态 |
|---|------|-----------|----------|----------|----------|------|
| 1 | 综合定位平台开发进度 | RoY1wIWERis1wlk0LwIcwLtOnQc | LnobsSBlyhcyZutJ9uDcd7RQnzg | sheet | https://reliablesense.feishu.cn/wiki/RoY1wIWERis1wlk0LwIcwLtOnQc | 🔗 保留链接 |

#### Space `7586861617376267458`（已知 2 节点）

| # | 标题 | Node Token | Token (obj) | obj_type | 飞书链接 | 状态 |
|---|------|-----------|----------|----------|----------|------|
| 1 | 后端 2.7更新内容 2026.3.9 | AYprwPzeGiWaPlkUnVxcQWbMndc | RlWWdKLPio9JgQxOM94cqYBCnwg | docx | https://reliablesense.feishu.cn/wiki/AYprwPzeGiWaPlkUnVxcQWbMndc | ✅ 已迁移 |
| 2 | 2025年年终总结 | ZSDawo3uLi4lxXkGZP7cHGxBnXc | SKuRd7JuyoVxCyxAdA3cx7GTnzf | docx | https://reliablesense.feishu.cn/wiki/ZSDawo3uLi4lxXkGZP7cHGxBnXc | ✅ 已迁移 |

#### Space `7527985368571756572`（已知 3 节点）

| # | 标题 | Node Token | Token (obj) | obj_type | 飞书链接 | 状态 |
|---|------|-----------|----------|----------|----------|------|
| 1 | 2025年度总结 | MqWawqoYkiJsQekf1y2c8Hatnve | Gwf9doDuro4zsjxChktc5zRknbc | docx | https://reliablesense.feishu.cn/wiki/MqWawqoYkiJsQekf1y2c8Hatnve | ✅ 已迁移 |
| 2 | Map-mobile v2.7 版本更新报告 2026-03-11 | WiJ2wFB10iQ98skKC4lcgQgqn9b | Pje7dY48koYX1hxbnuEcq5Munmz | docx | https://reliablesense.feishu.cn/wiki/WiJ2wFB10iQ98skKC4lcgQgqn9b | ✅ 已迁移 |
| 3 | 前端Admin 2.7更新内容 2026.3.5 | OaQpwHMvhiduTDk5lBqcluCfnPf | HAmwdy6SnohV78xix73cWV0WnSg | docx | https://reliablesense.feishu.cn/wiki/OaQpwHMvhiduTDk5lBqcluCfnPf | ✅ 已迁移 |

#### Space `7533431263699501059`（已知 2 节点）

| # | 标题 | Node Token | Token (obj) | obj_type | 飞书链接 | 状态 |
|---|------|-----------|----------|----------|----------|------|
| 1 | 莱讯项目部刘远达 25年 年终总结 | TfMYwzD5citiR0kXrffcRYNUn8d | ZjEEdFBL2oEYqLxV5JDcCHpBnfd | docx | https://reliablesense.feishu.cn/wiki/TfMYwzD5citiR0kXrffcRYNUn8d | ✅ 已迁移 |
| 2 | 库房管理 | HVIfwtSHbisE0Bkbc4rcCAhHnIc | PF71bTA9Yaqo3yscmxlcsdsnnVU | bitable | https://reliablesense.feishu.cn/wiki/HVIfwtSHbisE0Bkbc4rcCAhHnIc | 🔗 保留链接 |

#### Space `7530814402510241820`（已知 2 节点）

| # | 标题 | Node Token | Token (obj) | obj_type | 飞书链接 | 状态 |
|---|------|-----------|----------|----------|----------|------|
| 1 | 新太项目总结 | TK3Sw7sNkiEFD1kFx27cLTkznAV | NmbtdK5O7oy1lnx8XamcWItRn8d | docx | https://reliablesense.feishu.cn/wiki/TK3Sw7sNkiEFD1kFx27cLTkznAV | ✅ 已迁移 |
| 2 | 新太元验收标准总结 | LbYbwPb1QidoL0kpKakcRhCrnPe | Ms75dFCNMobyS0xMoH9c4ECHn2f | docx | https://reliablesense.feishu.cn/wiki/LbYbwPb1QidoL0kpKakcRhCrnPe | ✅ 已迁移 |

#### Space `7552826134947381251`（已知 1 节点）

| # | 标题 | Node Token | Token (obj) | obj_type | 飞书链接 | 状态 |
|---|------|-----------|----------|----------|----------|------|
| 1 | ✅机场任务管理 | LmgEw2zsMihrwAkmA0FcnQbKn7e | A9NpbHhPgafD4osRWROcWPydnse | bitable | https://reliablesense.feishu.cn/wiki/LmgEw2zsMihrwAkmA0FcnQbKn7e | 🔗 保留链接 |
---

## 三、跳过的第三方知识库

以下知识库 URL 域名不是 `reliablesense.feishu.cn`，按规则跳过：

| # | 标题 | 来源域名 | 原因 |
|---|------|----------|------|
| 1 | 莱讯位置解算仿真 | m7zr8sy5wi.feishu.cn | 第三方知识库 |
| 2 | 创建地图可视化 | maptable.feishu.cn | 第三方知识库 |
| 3 | 空间分析 | maptable.feishu.cn | 第三方知识库 |
| 4 | 版本更新记录 | maptable.feishu.cn | 第三方知识库 |
| 5 | 「收支明细表」每月定时生成收支报告！自动发送负责人！ | docugenius.feishu.cn | 飞书排版打印插件文档 |
| 6 | 「授权证书」一键填入经销商信息，快速生成证书 | docugenius.feishu.cn | 飞书排版打印插件文档 |
| 7 | 小七姐：文心一言4.0、智谱清言、KimiChat 小样本测评 | waytoagi.feishu.cn | AI 学习社区知识库 |
| 8 | Manus 学习手册（全网首发&持续更新 ing...) | yunyinghui.feishu.cn | 第三方知识库 |
| 9 | Deepseek 学习手册（持续更新 ing...) | yunyinghui.feishu.cn | 第三方知识库 |
| 10 | RPS｜飞书案例合集 | bytedance.larkoffice.com | 飞书官方文档 |
| 11 | 【对外模板】车辆管理系统-多维表 | cohlzhtweb.feishu.cn | 第三方知识库 |
| 12 | 飞书大讲堂｜一站式官方学习平台 | bytedance.larkoffice.com | 飞书官方文档 |
| 13 | 短剧小说 IP 版权剧本库 | bytedance.larkoffice.com | 飞书官方文档 |
| 14 | 早点下班 AI神器-做图写方案必备 | my.feishu.cn | 飞书个人模板库 |
| 15 | Ai元语咒-提示词框架 | my.feishu.cn | 飞书个人模板库 |
| 16 | Ai视频提示词大全｜适配Sora、Pika、MJ | my.feishu.cn | 飞书个人模板库 |
| 17 | 需求撮合管理系统 | naafv2ps2p.feishu.cn | 第三方知识库 |
| 18 | Ai提高效率工具-信息处理类 | my.feishu.cn | 飞书个人模板库 |
| 19 | ChatGPT Plugin清单 | p89j9q5t4u.feishu.cn | 第三方知识库 |
| 20 | 万字专访贝索斯 | my.feishu.cn | 飞书个人模板库 |
| 21 | AI直聘｜飞书多维表格首款AI简历筛选工具 | feichuangtech.feishu.cn | 第三方插件文档 |