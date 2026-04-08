#!/usr/bin/env python3
import os

FEISHU_DIR = "4-Archives/Notes/Feishu"
TSV = "1-Projects/Personal/笔记迁移/飞书完整文件清单.tsv"

with open(TSV) as f:
    lines = f.readlines()[1:]

count = 0
for line in lines:
    parts = line.strip().split("\t")
    if len(parts) >= 4 and parts[1] == "file":
        path, token, name = parts[0], parts[2], parts[3]
        target_dir = os.path.join(FEISHU_DIR, os.path.dirname(path))
        if not os.path.exists(os.path.join(target_dir, name)):
            count += 1
            if count <= 5:
                ext = name.rsplit(".", 1)[-1] if "." in name else "none"
                print(f"{count}. {name} [{ext}]")
                print(f"   token: {token}")
                print(f"   path: {path}")

print(f"\n总共 {count} 个未下载")
