#!/usr/bin/env python3
"""替换迁移方案中会议纪要的"见 README"为实际飞书链接"""
import os, re

URL_PREFIX = {
    'docx': 'https://reliablesense.feishu.cn/docx/',
    'doc': 'https://reliablesense.feishu.cn/docs/',
}

plan_path = '1-Projects/Personal/笔记迁移/阶段二-飞书归档提取到PARA迁移方案.md'

with open(plan_path, 'r') as f:
    lines = f.readlines()

changed = 0
for i, line in enumerate(lines):
    if '见 README' not in line:
        continue
    m = re.search(r'\[\[([^\]]+)\]\]', line)
    if not m:
        continue
    wl = m.group(1)
    fpath = wl + '.md'
    if not os.path.exists(fpath):
        continue
    try:
        with open(fpath, 'r') as f:
            content = f.read(500)
        # 先尝试 feishu_url
        m2 = re.search(r'feishu_url:\s*"([^"]+)"', content)
        if m2:
            url = m2.group(1)
        else:
            # 从 feishu_token + feishu_type 拼接
            mt = re.search(r'feishu_token:\s*"([^"]+)"', content)
            mtype = re.search(r'feishu_type:\s*(\w+)', content)
            if mt and mtype:
                token = mt.group(1)
                ftype = mtype.group(1)
                prefix = URL_PREFIX.get(ftype, f'https://reliablesense.feishu.cn/{ftype}/')
                url = f'{prefix}{token}'
            else:
                continue
        lines[i] = line.replace('见 README', f'[飞书]({url})')
        changed += 1
    except:
        pass

with open(plan_path, 'w') as f:
    f.writelines(lines)

remaining = sum(1 for l in lines if '见 README' in l)
print(f'替换了 {changed} 个，剩余 {remaining} 个')
