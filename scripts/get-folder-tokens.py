#!/usr/bin/env python3
"""
递归获取飞书云空间文件夹的 folder_token，输出 {路径 → token} 映射。
"""

import json
import subprocess
import sys

LARK_CLI = '/Users/liubx/.local/share/mise/installs/node/20.19.5/bin/lark-cli'

def list_folders(folder_token):
    """列出指定文件夹下的所有子文件夹"""
    result = subprocess.run(
        [LARK_CLI, 'api', 'GET', '/open-apis/drive/v1/files',
         '--params', json.dumps({"folder_token": folder_token, "page_size": 200}),
         '--as', 'user'],
        capture_output=True, text=True, timeout=30
    )
    raw = result.stdout
    start = raw.find('{')
    if start < 0:
        return []
    data = json.loads(raw[start:])
    folders = []
    for f in data.get('data', {}).get('files', []):
        if f.get('type') == 'folder':
            folders.append((f['name'], f['token']))
    return folders

def crawl(folder_token, path, depth=0, max_depth=3):
    """递归爬取文件夹"""
    if depth > max_depth:
        return
    folders = list_folders(folder_token)
    for name, token in sorted(folders):
        full_path = f'{path}/{name}' if path else name
        url = f'https://reliablesense.feishu.cn/drive/folder/{token}'
        print(f'{full_path}\t{token}\t{url}')
        crawl(token, full_path, depth + 1, max_depth)

# 需要爬取的根目录
roots = {
    '莱讯科技': 'fldcnXlYYuNIwJqa38AqI22zhMk',
}

for name, token in roots.items():
    url = f'https://reliablesense.feishu.cn/drive/folder/{token}'
    print(f'{name}\t{token}\t{url}')
    crawl(token, name, 0, 3)
