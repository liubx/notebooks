#!/usr/bin/env python3
"""
从 TSV 补全 README.md 中缺失的文件条目。
对比 TSV 和 README，把 README 中没有但 TSV 中有的文件追加到 README 表格末尾。
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

TYPE_DISPLAY = {
    'docx': '文档', 'doc': '旧版文档', 'file': '文件',
    'sheet': '表格', 'bitable': '多维表格',
    'mindnote': '思维导图', 'slides': '幻灯片', 'shortcut': '快捷方式',
}

def load_tsv(tsv_path):
    """返回 {父目录 → [(文件名, 类型, token, 状态)]}"""
    mapping = defaultdict(list)
    with open(tsv_path, 'r', encoding='utf-8') as f:
        reader = csv.reader(f, delimiter='\t')
        next(reader)
        for row in reader:
            if len(row) < 4 or not row[0] or not row[2]:
                continue
            path, ftype, token, name = row[0], row[1], row[2], row[3]
            status = row[4] if len(row) > 4 else ''
            parent = path.rsplit('/', 1)[0] if '/' in path else ''
            fname = path.rsplit('/', 1)[-1]
            mapping[parent].append((fname, ftype, token, status))
    return mapping

def build_url(ftype, token):
    prefix = URL_PREFIX.get(ftype, '')
    return f'{prefix}{token}' if prefix else None

def normalize(s):
    s = os.path.splitext(s)[0]
    s = re.sub(r'[（(][^）)]*[）)]', '', s)
    s = re.sub(r'[✅🚩\s\-_：:，,。.·\*×x]', '', s)
    return s.lower().strip()

def get_existing_files(content):
    """从 README 内容中提取已有的文件名集合（标准化后）"""
    existing = set()
    for line in content.split('\n'):
        if not line.startswith('|'):
            continue
        m = re.search(r'\[\[([^\]]+)\]\]', line)
        if m:
            existing.add(normalize(m.group(1)))
            continue
        m = re.search(r'`([^`]+)`', line)
        if m:
            existing.add(normalize(m.group(1)))
    return existing

def format_entry(fname, ftype, token):
    """格式化一行 README 表格条目"""
    url = build_url(ftype, token)
    type_str = TYPE_DISPLAY.get(ftype, ftype)
    link_str = f'[打开]({url})' if url else '—'
    
    # 判断是否有本地文件（docx/doc 转成了 .md）
    if ftype in ('docx', 'doc'):
        return f'| [[{fname}]] | {type_str} | {link_str} |'
    else:
        # file/sheet/bitable 等用 ` ` 包裹
        ext_map = {'file': '', 'sheet': '.xlsx', 'bitable': '.xlsx', 'mindnote': '.mm', 'slides': '.pptx'}
        ext = ext_map.get(ftype, '')
        display_name = fname + ext if ext and '.' not in fname else fname
        return f'| `{display_name}` | {type_str} | {link_str} |'

def process_readme(readme_path, tsv_mapping):
    with open(readme_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    m = re.search(r'飞书原始路径：`([^`]+)`', content)
    if not m:
        return 0
    feishu_dir = m.group(1)
    
    # 找到对应的 TSV 目录
    search_dirs = [feishu_dir]
    if feishu_dir.endswith('/根目录'):
        search_dirs.append(feishu_dir.rsplit('/根目录', 1)[0])
    if not feishu_dir.endswith('的个人文档'):
        search_dirs.append(feishu_dir + '的个人文档')
    
    # 收集 TSV 中该目录下的所有文件
    tsv_files = []
    for sd in search_dirs:
        if sd in tsv_mapping:
            tsv_files.extend(tsv_mapping[sd])
    
    if not tsv_files:
        return 0
    
    # 获取 README 中已有的文件
    existing = get_existing_files(content)
    
    # 找出缺失的文件
    missing = []
    for fname, ftype, token, status in tsv_files:
        if normalize(fname) not in existing:
            missing.append((fname, ftype, token))
    
    if not missing:
        return 0
    
    # 在文件列表表格末尾追加
    lines = content.split('\n')
    
    # 找到最后一个表格行的位置
    last_table_line = -1
    for i, line in enumerate(lines):
        if line.startswith('|') and ('[[' in line or '`' in line):
            last_table_line = i
    
    if last_table_line == -1:
        # 没找到表格，在文件末尾追加
        lines.append('')
        lines.append('| 文件 | 类型 | 飞书链接 |')
        lines.append('|------|------|----------|')
        last_table_line = len(lines) - 1
    
    # 追加缺失的条目
    new_entries = []
    for fname, ftype, token in sorted(missing, key=lambda x: x[0]):
        new_entries.append(format_entry(fname, ftype, token))
    
    # 插入到最后一个表格行之后
    for j, entry in enumerate(new_entries):
        lines.insert(last_table_line + 1 + j, entry)
    
    with open(readme_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines))
    
    return len(missing)

def main():
    tsv_path = '1-Projects/Personal/笔记迁移/飞书文件清单与迁移状态.tsv'
    feishu_root = '4-Archives/Notes/Feishu'
    
    print(f'读取 TSV: {tsv_path}')
    tsv_mapping = load_tsv(tsv_path)
    print(f'共 {sum(len(v) for v in tsv_mapping.values())} 条记录')
    
    total_added = 0
    total_files = 0
    
    for root, dirs, files in os.walk(feishu_root):
        if 'README.md' in files:
            path = os.path.join(root, 'README.md')
            added = process_readme(path, tsv_mapping)
            if added > 0:
                total_files += 1
                total_added += added
                print(f'  ✅ {path}: 追加 {added} 个条目')
    
    print(f'\n完成！共修改 {total_files} 个 README，追加 {total_added} 个文件条目')

if __name__ == '__main__':
    main()
