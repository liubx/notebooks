#!/usr/bin/env python3
"""替换迁移方案中剩余的"见 README"为实际飞书链接（从 README 和 TSV 查找）"""
import os, re, csv

# 加载 README 中的链接
readme_links = {}
for root, dirs, files in os.walk('4-Archives/Notes/Feishu'):
    if 'README.md' not in files: continue
    with open(os.path.join(root, 'README.md'), 'r') as f:
        for line in f:
            m = re.search(r'(?:\[\[([^\]]+)\]\]|`([^`]+)`)', line)
            m2 = re.search(r'\[打开\]\((https://[^)]+)\)', line)
            if m and m2:
                name = m.group(1) or m.group(2)
                readme_links[name] = m2.group(1)
                # 也存不带扩展名的
                base = os.path.splitext(name)[0]
                if base != name:
                    readme_links[base] = m2.group(1)

# 加载 TSV 链接
tsv_links = {}
prefix_map = {'docx':'docx','doc':'docs','file':'file','sheet':'sheets','bitable':'base','mindnote':'mindnotes','slides':'slides'}
with open('1-Projects/Personal/笔记迁移/飞书文件清单与迁移状态.tsv', 'r') as f:
    reader = csv.reader(f, delimiter='\t')
    next(reader)
    for row in reader:
        if len(row) < 4 or not row[2]: continue
        fname = row[0].rsplit('/', 1)[-1]
        p = prefix_map.get(row[1], row[1])
        url = f'https://reliablesense.feishu.cn/{p}/{row[2]}'
        tsv_links[fname] = url
        base = os.path.splitext(fname)[0]
        if base != fname:
            tsv_links[base] = url

def normalize(s):
    s = os.path.splitext(s)[0]
    return re.sub(r'[（(][^）)]*[）)]', '', s).replace('-', '').replace('_', '').replace(' ', '').lower()

plan_path = '1-Projects/Personal/笔记迁移/阶段二-飞书归档提取到PARA迁移方案.md'
with open(plan_path, 'r') as f:
    lines = f.readlines()

changed = 0
for i, line in enumerate(lines):
    if '见 README' not in line: continue
    
    # 提取文件名
    m = re.search(r'\[\[([^\]]+)\]\]', line)
    if not m: continue
    wl = m.group(1)
    fname = wl.rsplit('/', 1)[-1]
    
    # 查找链接
    url = None
    # 精确匹配
    if fname in readme_links: url = readme_links[fname]
    elif fname in tsv_links: url = tsv_links[fname]
    else:
        # 标准化匹配
        fn = normalize(fname)
        for k, v in readme_links.items():
            if normalize(k) == fn:
                url = v; break
        if not url:
            for k, v in tsv_links.items():
                if normalize(k) == fn:
                    url = v; break
    
    if url:
        lines[i] = line.replace('见 README', f'[飞书]({url})')
        changed += 1

with open(plan_path, 'w') as f:
    f.writelines(lines)

remaining = sum(1 for l in lines if '见 README' in l)
print(f'替换了 {changed} 个，剩余 {remaining} 个')
