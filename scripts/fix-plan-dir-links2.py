#!/usr/bin/env python3
"""
将迁移方案中目录行的"见目录 README"替换为该目录下第一个文件的实际飞书链接。
"""

import os
import re

plan_path = '1-Projects/Personal/笔记迁移/阶段二-飞书归档提取到PARA迁移方案.md'
feishu_root = '4-Archives/Notes/Feishu'

def get_first_link_from_readme(readme_path):
    """从 README 中提取第一个飞书链接"""
    if not os.path.exists(readme_path):
        return None
    with open(readme_path, 'r') as f:
        for line in f:
            m = re.search(r'\[打开\]\((https://[^)]+)\)', line)
            if m:
                return m.group(1)
    return None

with open(plan_path, 'r') as f:
    content = f.read()

# 找到所有"见目录 README"并替换
pattern = re.compile(r'\[\[([^\]]+/README)\]\] \| 见目录 README')
count = 0

def replace_fn(m):
    global count
    wikilink_path = m.group(1)
    # 转换为实际文件路径
    readme_path = wikilink_path + '.md'
    url = get_first_link_from_readme(readme_path)
    if url:
        count += 1
        return f'[[{wikilink_path}]] | [飞书（目录）]({url})'
    return m.group(0)

content = pattern.sub(replace_fn, content)

with open(plan_path, 'w') as f:
    f.write(content)

print(f'替换了 {count} 个"见目录 README"为实际飞书链接')
