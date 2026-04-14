#!/usr/bin/env python3
"""修正同事个人文档中待归类文件的分类"""
path = '1-Projects/Personal/笔记迁移/阶段二-飞书归档提取到PARA迁移方案.md'
with open(path, 'r') as f:
    lines = f.readlines()

# 分类规则
rules = {
    # 何宜峰
    '员工入职表-空白': ('留归档', '-', 'HR 模板'),
    # 陈子杰
    '2023-05-07 20-54-59.mkv': ('留归档', '-', '录屏文件'),
    'oemusers.xlsx': ('→ 提取', '1-Projects/Work/广州机场/', '广州机场 OEM 用户数据'),
    't_poi_type.xlsx': ('→ 提取', '2-Areas/Work/产品研发/', '产品 POI 类型数据'),
    '室内定位系统工作进度.xlsx': ('→ 提取', '2-Areas/Work/产品研发/', '产品开发进度'),
    '问题记录-2023-09-22.xlsx': ('留归档', '-', '历史问题记录'),
    '需求及 Bug 管理.xlsx': ('→ 提取', '2-Areas/Work/产品研发/', '需求和 Bug 管理'),
    '移动终端目前缺失功能.xlsx': ('→ 提取', '1-Projects/Work/广州机场/', '广州机场移动应用缺失功能'),
    'app_store_back-main.zip': ('→ 提取', '1-Projects/Work/广州机场/', '广州机场应用商店后端代码'),
    'app_store_flutter_module-main.zip': ('→ 提取', '1-Projects/Work/广州机场/', '广州机场应用商店 Flutter 模块'),
    'appstoreaf-main.zip': ('→ 提取', '1-Projects/Work/广州机场/', '广州机场应用商店前端代码'),
    'readme.txt': ('→ 提取', '1-Projects/Work/广州机场/', '广州机场应用商店说明'),
    # 孙永霖
    '地图管理的问题.md': ('→ 提取', '3-Resources/Tech/问题解决/', '地图管理问题记录'),
    'Help Center Template.md': ('→ 提取', '2-Areas/Work/产品研发/', '产品帮助中心模板（英文）'),
    'SaaS使用手册V4 new 英文.docx': ('→ 提取', '2-Areas/Work/产品研发/', '产品 SaaS 英文使用手册'),
    'SaaS使用手册V4 new.docx': ('→ 提取', '2-Areas/Work/产品研发/', '产品 SaaS 使用手册'),
    'saas英文版.md': ('→ 提取', '2-Areas/Work/产品研发/', '产品 SaaS 英文版文档'),
    # boxcn 图片 → 跟随 saas英文版文档
    'boxcn': ('留归档', '-', '文档内嵌图片'),
}

changed = 0
for i, line in enumerate(lines):
    if '待归类 | 待归类' not in line:
        continue
    for key, (decision, target, reason) in rules.items():
        if key in line:
            target_str = f'`{target}`' if target != '-' else '-'
            lines[i] = line.replace('| 待归类 | 待归类 |', f'| {decision} | {target_str} | {reason} |')
            changed += 1
            break

with open(path, 'w') as f:
    f.writelines(lines)
print(f'修正了 {changed} 个待归类文件')

# 检查剩余
remaining = sum(1 for l in lines if '待归类 | 待归类' in l)
print(f'剩余 {remaining} 个待归类')
