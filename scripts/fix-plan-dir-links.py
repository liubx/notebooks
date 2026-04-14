#!/usr/bin/env python3
"""
修复迁移方案中目录级别表格缺少飞书链接列的问题。
将 3 列格式（飞书目录 | 本地路径 | 目标路径）转为 4 列（飞书目录 | 本地路径 | 飞书链接 | 目标路径）。
对于目录，飞书链接指向对应的 README。
"""

import re

plan_path = '1-Projects/Personal/笔记迁移/阶段二-飞书归档提取到PARA迁移方案.md'

with open(plan_path, 'r') as f:
    lines = f.readlines()

changed = 0
i = 0
while i < len(lines):
    line = lines[i]
    
    # 找到 3 列表头（飞书目录 | 本地路径 | 目标路径）
    if '| 飞书目录 | 本地路径 | 目标路径 |' in line:
        # 替换表头
        lines[i] = '| 飞书目录 | 本地路径 | 飞书链接 | 目标路径 |\n'
        # 替换分隔行
        if i + 1 < len(lines) and '|---' in lines[i+1]:
            lines[i+1] = '|---------|---------|---------|---------|' + '\n'
        
        # 处理后续数据行
        j = i + 2
        while j < len(lines) and lines[j].startswith('|'):
            row = lines[j]
            cols = row.split('|')
            # cols: ['', ' 飞书目录 ', ' 本地路径 ', ' 目标路径 ', '\n']
            if len(cols) == 5:  # 3 列数据 + 前后空
                # 提取 wikilink 路径，改为指向 README
                wikilink = cols[2].strip()
                if '[[' in wikilink:
                    # 把 [[path/]] 改为 [[path/README]]
                    readme_link = wikilink.rstrip('/]]') + '/README]]' if wikilink.endswith('/]]') else wikilink
                    cols[2] = f' {readme_link} '
                
                # 插入飞书链接列
                cols.insert(3, ' 见目录 README ')
                lines[j] = '|'.join(cols)
                changed += 1
            j += 1
        
        i = j
        continue
    
    i += 1

with open(plan_path, 'w') as f:
    f.writelines(lines)

print(f'修复了 {changed} 行')
