#!/usr/bin/env python3
"""
从飞书文件清单 TSV 中提取 token，补全所有 README.md 中缺失的飞书链接。
v3: 递归子目录查找 + 更宽松的模糊匹配
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

LOCAL_ONLY_FILES = {'链接索引', '项目管理-附件映射', 'README'}

def load_tsv(tsv_path):
    """读取 TSV，返回全量列表 [(飞书路径, 类型, token, 名称)]"""
    entries = []
    with open(tsv_path, 'r', encoding='utf-8') as f:
        reader = csv.reader(f, delimiter='\t')
        next(reader)
        for row in reader:
            if len(row) < 4 or not row[0] or not row[2]:
                continue
            entries.append((row[0], row[1], row[2], row[3]))
    return entries

def build_url(file_type, token):
    prefix = URL_PREFIX.get(file_type, '')
    return f'{prefix}{token}' if prefix else None

def normalize(s):
    """去掉扩展名、特殊字符、括号内容"""
    s = os.path.splitext(s)[0]
    # 去掉括号及内容 (1) （三标段）
    s = re.sub(r'[（(][^）)]*[）)]', '', s)
    # 去掉特殊字符
    s = re.sub(r'[✅🚩\s\-_：:，,。.·\*×x]', '', s)
    return s.lower().strip()

def extract_filename(line):
    m = re.search(r'`([^`]+)`', line)
    if m:
        return m.group(1)
    m = re.search(r'\[\[([^\]]+)\]\]', line)
    if m:
        return m.group(1)
    return None

def find_match(tsv_entries, feishu_dir, filename):
    """在 TSV 中查找匹配的文件"""
    fname_base = os.path.splitext(filename)[0]
    fname_norm = normalize(filename)
    
    # 构建搜索目录前缀列表
    prefixes = [feishu_dir + '/']
    # 根目录映射
    if feishu_dir.endswith('/根目录'):
        prefixes.append(feishu_dir.rsplit('/根目录', 1)[0] + '/')
    # 同事个人文档映射：本地 README 路径可能是 "云空间/王宗光"，TSV 是 "云空间/王宗光的个人文档"
    if not feishu_dir.endswith('的个人文档'):
        prefixes.append(feishu_dir + '的个人文档/')
    
    best_match = None
    best_score = 0
    
    for tsv_path, file_type, token, tsv_name in tsv_entries:
        # 检查是否在目标目录下（包括子目录）
        in_dir = False
        for prefix in prefixes:
            if tsv_path.startswith(prefix):
                in_dir = True
                break
        if not in_dir:
            # 也检查根目录直接文件（无子目录）
            for prefix in prefixes:
                parent = prefix.rstrip('/')
                if tsv_path.rsplit('/', 1)[0] == parent.rsplit('/', 1)[0] and not '/' in tsv_path[len(parent.rsplit('/', 1)[0])+1:]:
                    in_dir = True
                    break
        if not in_dir:
            continue
        
        # 提取 TSV 中的文件名（路径最后一段）
        tsv_fname = tsv_path.rsplit('/', 1)[-1]
        tsv_fname_norm = normalize(tsv_fname)
        
        # 精确匹配
        if tsv_fname == filename or tsv_fname == fname_base:
            return file_type, token
        
        # 标准化匹配
        if tsv_fname_norm and fname_norm and tsv_fname_norm == fname_norm:
            return file_type, token
        
        # 包含匹配（较长的包含较短的）
        if tsv_fname_norm and fname_norm:
            shorter = min(tsv_fname_norm, fname_norm, key=len)
            longer = max(tsv_fname_norm, fname_norm, key=len)
            if len(shorter) >= 4 and shorter in longer:
                score = len(shorter) / len(longer)
                if score > best_score:
                    best_score = score
                    best_match = (file_type, token)
    
    if best_match and best_score >= 0.5:
        return best_match
    return None

def process_readme(readme_path, tsv_entries):
    with open(readme_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    m = re.search(r'飞书原始路径：`([^`]+)`', content)
    if not m:
        return 0, 0
    feishu_dir = m.group(1)
    
    lines = content.split('\n')
    changed = 0
    remaining = 0
    
    for i, line in enumerate(lines):
        if '| — |' not in line and '| —|' not in line:
            continue
        
        filename = extract_filename(line)
        if not filename:
            remaining += 1
            continue
        
        fname_base = os.path.splitext(filename)[0]
        if fname_base in LOCAL_ONLY_FILES:
            lines[i] = re.sub(r'\| —\s*\|', '| 本地文件 |', line)
            changed += 1
            continue
        
        result = find_match(tsv_entries, feishu_dir, filename)
        if result:
            file_type, token = result
            url = build_url(file_type, token)
            if url:
                lines[i] = re.sub(r'\| —\s*\|', f'| [打开]({url}) |', line)
                changed += 1
                continue
        
        remaining += 1
    
    if changed > 0:
        with open(readme_path, 'w', encoding='utf-8') as f:
            f.write('\n'.join(lines))
    
    return changed, remaining

def main():
    tsv_path = '1-Projects/Personal/笔记迁移/飞书文件清单与迁移状态.tsv'
    feishu_root = '4-Archives/Notes/Feishu'
    
    print(f'读取 TSV: {tsv_path}')
    tsv_entries = load_tsv(tsv_path)
    print(f'共 {len(tsv_entries)} 条记录')
    
    total_changed = 0
    total_files = 0
    total_remaining = 0
    unfixed = []
    
    for root, dirs, files in os.walk(feishu_root):
        for fname in files:
            if fname == 'README.md':
                readme_path = os.path.join(root, fname)
                changed, remaining = process_readme(readme_path, tsv_entries)
                if changed > 0:
                    total_files += 1
                    total_changed += changed
                    print(f'  ✅ {readme_path}: 补全 {changed} 个链接')
                if remaining > 0:
                    total_remaining += remaining
                    unfixed.append((readme_path, remaining))
    
    print(f'\n完成！共修改 {total_files} 个 README，补全 {total_changed} 个飞书链接')
    if total_remaining > 0:
        print(f'⚠️ 仍有 {total_remaining} 个链接未补全：')
        for path, count in unfixed:
            print(f'  {count} 个 | {path}')

if __name__ == '__main__':
    main()
