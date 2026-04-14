#!/usr/bin/env python3
"""给会议纪要目标路径加上年/月子目录"""
import re

path = '1-Projects/Personal/笔记迁移/阶段二-飞书归档提取到PARA迁移方案.md'
with open(path, 'r') as f:
    lines = f.readlines()

months_en = {'Jan':'01','Feb':'02','Mar':'03','Apr':'04','May':'05','Jun':'06',
             'Jul':'07','Aug':'08','Sep':'09','Oct':'10','Nov':'11','Dec':'12'}

def get_ym(line):
    m = re.search(r'(\d{4})年(\d+)月', line)
    if m: return m.group(1), m.group(2).zfill(2)
    m = re.search(r'(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\s+\d+,\s+(\d{4})', line)
    if m: return m.group(2), months_en[m.group(1)]
    return None, None

changed = 0
for i, line in enumerate(lines):
    y, m = get_ym(line)
    if not y: continue
    for folder in ['早会纪要/', '周会纪要/研发部/', '周会纪要/项目部/', '周会纪要/`']:
        if folder in line and f'{folder}{y}/' not in line:
            lines[i] = line.replace(folder, f'{folder}{y}/{m}/')
            changed += 1
            break

# 更新规则说明
for i, line in enumerate(lines):
    if '研发部早会每天开会后移入' in line and '{年}' not in line:
        lines[i] = line.replace('早会纪要/', '早会纪要/{年}/{月}/')

with open(path, 'w') as f:
    f.writelines(lines)
print(f'修改了 {changed} 行')
