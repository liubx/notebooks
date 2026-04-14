#!/usr/bin/env python3
"""
用正确的 folder URL 替换迁移方案中所有 [飞书（目录）] 链接。
从 /tmp/folder-tokens.tsv 读取 {飞书路径 → folder URL} 映射。
"""

import re

# 加载 folder token 映射
folder_urls = {}
with open('/tmp/folder-tokens.tsv', 'r') as f:
    for line in f:
        parts = line.strip().split('\t')
        if len(parts) >= 3:
            path, token, url = parts[0], parts[1], parts[2]
            folder_urls[path] = url

plan_path = '1-Projects/Personal/笔记迁移/阶段二-飞书归档提取到PARA迁移方案.md'
with open(plan_path, 'r') as f:
    lines = f.readlines()

changed = 0
for i, line in enumerate(lines):
    if '飞书（目录）' not in line:
        continue
    
    # 从 wikilink 中提取飞书路径
    # [[4-Archives/Notes/Feishu/云空间/莱讯科技/xxx/README]]
    m = re.search(r'\[\[4-Archives/Notes/Feishu/云空间/([^\]]+?)/?README\]\]', line)
    if not m:
        continue
    
    local_path = m.group(1)  # 如 莱讯科技/项目资料管理/004. 广州机场-综合定位
    
    # 在 folder_urls 中查找
    url = folder_urls.get(local_path)
    if not url:
        # 尝试去掉末尾的 /
        url = folder_urls.get(local_path.rstrip('/'))
    if not url:
        print(f'  ❌ 未找到: {local_path}')
        continue
    
    # 替换旧的错误链接
    old_pattern = r'\[飞书（目录）\]\(https://[^)]+\)'
    new_link = f'[飞书（目录）]({url})'
    new_line = re.sub(old_pattern, new_link, line)
    if new_line != line:
        lines[i] = new_line
        changed += 1

with open(plan_path, 'w') as f:
    f.writelines(lines)

print(f'替换了 {changed} 个目录链接')
