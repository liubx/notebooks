#!/usr/bin/env python3
"""
从 README.md 和 TSV 中提取飞书链接，补全迁移方案中所有缺失的飞书链接。
处理迁移方案中飞书链接列为 `- ` 的行。
"""

import os
import re
import csv
from collections import defaultdict

URL_PREFIX = {
    'docx': 'https://reliablesense.feishu.cn/docx/',
    'doc': 'https://reliablesense.feishu.cn/docs/',
    'file': 'https://reliablesense.feishu.cn/file/',
    'sheet': 'https://reliablesense.feishu.cn/sheets/',
    'bitable': 'https://reliablesense.feishu.cn/base/',
    'mindnote': 'https://reliablesense.feishu.cn/mindnotes/',
    'slides': 'https://reliablesense.feishu.cn/slides/',
}

def load_readme_links(feishu_root):
    """从所有 README.md 中提取 {文件名 → 飞书链接} 映射"""
    links = {}
    for root, dirs, files in os.walk(feishu_root):
        if 'README.md' not in files:
            continue
        with open(os.path.join(root, 'README.md'), 'r') as f:
            for line in f:
                if not line.startswith('|'):
                    continue
                # 提取文件名
                m = re.search(r'\[\[([^\]]+)\]\]', line)
                if not m:
                    m = re.search(r'`([^`]+)`', line)
                if not m:
                    continue
                fname = m.group(1)
                # 提取链接
                m2 = re.search(r'\[打开\]\((https://[^)]+)\)', line)
                if m2:
                    links[fname] = m2.group(1)
                    # 也存不带扩展名的版本
                    base = os.path.splitext(fname)[0]
                    if base != fname:
                        links[base] = m2.group(1)
    return links

def load_tsv_links(tsv_path):
    """从 TSV 中提取 {文件名 → 飞书链接} 映射"""
    links = {}
    with open(tsv_path, 'r') as f:
        reader = csv.reader(f, delimiter='\t')
        next(reader)
        for row in reader:
            if len(row) < 4 or not row[2]:
                continue
            fname = row[0].rsplit('/', 1)[-1]
            ftype = row[1]
            token = row[2]
            prefix = URL_PREFIX.get(ftype, '')
            if prefix:
                url = f'{prefix}{token}'
                links[fname] = url
                base = os.path.splitext(fname)[0]
                if base != fname:
                    links[base] = url
    return links

def normalize(s):
    s = os.path.splitext(s)[0]
    s = re.sub(r'[（(][^）)]*[）)]', '', s)
    s = re.sub(r'[✅🚩\s\-_：:，,。.·]', '', s)
    return s.lower().strip()

def find_link(fname, readme_links, tsv_links):
    """查找文件的飞书链接"""
    # 精确匹配
    if fname in readme_links:
        return readme_links[fname]
    if fname in tsv_links:
        return tsv_links[fname]
    
    base = os.path.splitext(fname)[0]
    if base in readme_links:
        return readme_links[base]
    if base in tsv_links:
        return tsv_links[base]
    
    # 标准化匹配
    fname_norm = normalize(fname)
    for k, v in readme_links.items():
        if normalize(k) == fname_norm:
            return v
    for k, v in tsv_links.items():
        if normalize(k) == fname_norm:
            return v
    
    return None

def process_plan(plan_path, readme_links, tsv_links):
    with open(plan_path, 'r') as f:
        lines = f.readlines()
    
    changed = 0
    for i, line in enumerate(lines):
        # 找到表格行中飞书链接列为 - 的
        if '|' not in line:
            continue
        
        cols = line.split('|')
        if len(cols) < 5:
            continue
        
        # 检查是否有飞书链接列为 -
        # 表格格式: | 文件 | 本地路径 | 飞书链接 | 决策 | ...
        # 或: | 文件 | 本地路径 | 飞书链接 | 决策 | 目标路径 | 理由 |
        feishu_col_idx = None
        for j, col in enumerate(cols):
            c = col.strip()
            if c == '-' and j >= 2:
                # 检查前面的列是否有 [[ 或 ` （本地路径列）
                prev_has_path = any('[[' in cols[k] or '`' in cols[k] for k in range(1, j))
                # 检查后面是否有"留归档"或"提取"（决策列）
                next_has_decision = any('留归档' in cols[k] or '提取' in cols[k] for k in range(j+1, len(cols)))
                if prev_has_path and next_has_decision:
                    feishu_col_idx = j
                    break
        
        if feishu_col_idx is None:
            continue
        
        # 提取文件名
        m = re.search(r'\[\[([^\]]+)\]\]', line)
        if not m:
            m = re.search(r'`([^`]+)`', line)
        if not m:
            continue
        
        fname_full = m.group(1)
        # 从 wikilink 路径中提取文件名
        fname = fname_full.rsplit('/', 1)[-1] if '/' in fname_full else fname_full
        
        url = find_link(fname, readme_links, tsv_links)
        if url:
            cols[feishu_col_idx] = f' [飞书]({url}) '
            lines[i] = '|'.join(cols)
            changed += 1
    
    if changed > 0:
        with open(plan_path, 'w') as f:
            f.writelines(lines)
    
    return changed

def main():
    plan_path = '1-Projects/Personal/笔记迁移/阶段二-飞书归档提取到PARA迁移方案.md'
    tsv_path = '1-Projects/Personal/笔记迁移/飞书文件清单与迁移状态.tsv'
    feishu_root = '4-Archives/Notes/Feishu'
    
    print('加载 README 链接...')
    readme_links = load_readme_links(feishu_root)
    print(f'  {len(readme_links)} 个链接')
    
    print('加载 TSV 链接...')
    tsv_links = load_tsv_links(tsv_path)
    print(f'  {len(tsv_links)} 个链接')
    
    print(f'处理迁移方案: {plan_path}')
    changed = process_plan(plan_path, readme_links, tsv_links)
    print(f'  补全 {changed} 个飞书链接')

if __name__ == '__main__':
    main()
