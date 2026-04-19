#!/usr/bin/env python3
"""修正麦钉定位相关文件的归类"""
path = '1-Projects/Personal/笔记迁移/阶段二-飞书归档提取到PARA迁移方案.md'
with open(path, 'r') as f:
    lines = f.readlines()

changed = 0
for i, line in enumerate(lines):
    # 周报测试 → 团队管理（提交记录，不是模板）
    if '周报测试.xlsx' in line and '周报模板' in line:
        lines[i] = line.replace('周报模板', '周报提交记录')
        changed += 1
    
    # 红柳林 → 麦钉定位
    if '红柳林' in line and '4-Archives/Projects/Work/红柳林' in line:
        lines[i] = line.replace('4-Archives/Projects/Work/红柳林/', '4-Archives/Projects/Work/麦钉/')
        changed += 1
    
    # 集群配置：麦钉定位的集群
    for kw in ['madinat_hll', 'madinat_xmc', 'madinat_hjc', 'madinat_gat', 'madinat_ntt']:
        if kw in line and '环境配置' in line:
            # 不改路径（环境配置是通用的），但可以加备注
            pass

with open(path, 'w') as f:
    f.writelines(lines)
print(f'修改了 {changed} 行')
