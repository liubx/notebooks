#!/usr/bin/env python3
"""审计迁移方案中所有文件的归类是否合理"""
import re

path = '1-Projects/Personal/笔记迁移/阶段二-飞书归档提取到PARA迁移方案.md'
with open(path, 'r') as f:
    lines = f.readlines()

# 项目关键词 → 应该归到的项目
project_keywords = {
    '1-Projects/Work/内蒙新太/': ['新太', '新钢联', '料棚', '卸料', '上料', '铲车', '堆垛', '料坑', '叫号', '倒运', '卸货'],
    '1-Projects/Work/广州机场/': ['广州机场', '综合定位', 'A域', 'B域', '电子围栏', '手推车', 'AESB', 'TCDM', '白云', '三标段', '移动应用平台', '陪伴运行', '深化设计'],
    '4-Archives/Projects/Work/麦钉/': ['红柳林', '李家壕', '韩家村', '高安屯', '柠条塔', 'madinat_hll', 'madinat_xmc', 'madinat_hjc', 'madinat_gat', 'madinat_ntt', '麦钉', '高安屯'],
    '4-Archives/Projects/Work/中东电子厂/': ['伊朗', '波斯', 'madinat_sewd', '翻译'],
    '4-Archives/Projects/Work/洛阳石化/': ['洛阳石化', '洛阳化工', 'madinat_lyhx', 'madinat_lyrydw'],
    '1-Projects/Work/上港仓储管理/': ['上港', '仓储', 'SIPG'],
    '1-Projects/Work/南宁机场/': ['南宁机场', '无动力设备'],
}

issues = []
for i, line in enumerate(lines, 1):
    if not line.startswith('|') or '---' in line or '文件' in line[:10]:
        continue
    # 提取文件名和目标路径
    cols = [c.strip() for c in line.split('|')]
    if len(cols) < 4:
        continue
    fname = cols[1] if len(cols) > 1 else ''
    
    # 检查文件名中的项目关键词是否与目标路径匹配
    for target_prefix, keywords in project_keywords.items():
        for kw in keywords:
            if kw in fname:
                # 检查目标路径是否包含对应项目
                target_in_line = any(target_prefix in c for c in cols)
                if not target_in_line:
                    # 检查是否留归档（旧版本/重复等合理情况）
                    is_archive_ok = any(r in line for r in ['留归档', '旧版本', '重复', '白皮书已有', '框架文档', '被 v2 覆盖', '根目录已有', '已在第二章'])
                    if not is_archive_ok:
                        actual_target = ''
                        for c in cols:
                            if '1-Projects' in c or '2-Areas' in c or '3-Resources' in c or '4-Archives/Projects' in c:
                                actual_target = c.strip('` ')
                                break
                        issues.append(f'行{i}: 文件含"{kw}"但未归到{target_prefix}\n  文件: {fname[:60]}\n  当前: {actual_target}')
                break

if issues:
    print(f'发现 {len(issues)} 个可能归类不当的文件:\n')
    for iss in issues:
        print(iss)
        print()
else:
    print('所有文件归类合理')
