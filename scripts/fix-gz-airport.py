#!/usr/bin/env python3
"""把含"综合定位系统"和"移动应用平台"的文件从产品研发改到广州机场"""
with open('1-Projects/Personal/笔记迁移/阶段二-飞书归档提取到PARA迁移方案.md', 'r') as f:
    c = f.read()

pairs = [
    ('2-Areas/Work/产品研发/综合定位系统架构图.md', '1-Projects/Work/广州机场/综合定位系统架构图.md'),
    ('2-Areas/Work/产品研发/综合定位系统功能清单.xlsx', '1-Projects/Work/广州机场/综合定位系统功能清单.xlsx'),
    ('2-Areas/Work/产品研发/综合定位系统运维白皮书.md', '1-Projects/Work/广州机场/综合定位系统运维白皮书.md'),
    ('2-Areas/Work/产品研发/综合定位系统技术要求.md', '1-Projects/Work/广州机场/综合定位系统技术要求.md'),
    ('2-Areas/Work/产品研发/综合定位系统功能清单.md', '1-Projects/Work/广州机场/综合定位系统功能清单.md'),
]

n = 0
for old, new in pairs:
    if old in c:
        c = c.replace(old, new)
        n += 1

c = c.replace('产品架构文档，归产品研发', '含"综合定位系统"，归广州机场')
c = c.replace('| 产品功能清单 |', '| 广州机场功能清单 |')
c = c.replace('| 产品技术规格 |', '| 广州机场技术规格 |')
c = c.replace('| 产品功能列表 |', '| 广州机场功能列表 |')

with open('1-Projects/Personal/笔记迁移/阶段二-飞书归档提取到PARA迁移方案.md', 'w') as f:
    f.write(c)
print(f'修正了 {n} 个')
