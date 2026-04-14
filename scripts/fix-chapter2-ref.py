#!/usr/bin/env python3
"""把"已在第二章分类"替换为实际目标路径"""
import re

path = '1-Projects/Personal/笔记迁移/阶段二-飞书归档提取到PARA迁移方案.md'
with open(path, 'r') as f:
    lines = f.readlines()

# 从第二章详细列表中建立 文件名 → 目标路径 映射
file_targets = {}
for line in lines:
    if not line.startswith('|'): continue
    m = re.search(r'\[\[([^\]]+)\]\]', line)
    if not m: continue
    fname = m.group(1).rsplit('/', 1)[-1]
    # 提取目标路径
    for pattern in [r'`(1-Projects/[^`]+)`', r'`(2-Areas/[^`]+)`', r'`(3-Resources/[^`]+)`', r'`(4-Archives/Projects/[^`]+)`']:
        m2 = re.search(pattern, line)
        if m2:
            file_targets[fname] = m2.group(1)
            break

changed = 0
for i, line in enumerate(lines):
    if '已在第二章分类' not in line:
        continue
    m = re.search(r'\[\[([^\]]+)\]\]', line)
    if not m: continue
    fname = m.group(1).rsplit('/', 1)[-1]
    
    target = file_targets.get(fname, '')
    if target:
        lines[i] = line.replace('会议纪要（已在第二章分类） | 会议纪要（已在第二章分类）', f'→ 提取 | `{target}` ')
        changed += 1

with open(path, 'w') as f:
    f.writelines(lines)

remaining = sum(1 for l in lines if '已在第二章分类' in l)
print(f'替换了 {changed} 个，剩余 {remaining} 个')
