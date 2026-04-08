#!/usr/bin/env python3
import os

FEISHU_DIR = "4-Archives/Notes/Feishu"
TSV = "1-Projects/Personal/笔记迁移/飞书完整文件清单.tsv"
SKIP_EXT = {"zip","rar","7z","tar","gz","tgz","mp4","mov","mkv","avi","wmv","flv","mp3","wav","iso","apk","exe","msi","dmg","dwg","bak","ai","psd"}

with open(TSV) as f:
    lines = f.readlines()[1:]

count = 0
for line in lines:
    parts = line.strip().split("\t")
    if len(parts) >= 4 and parts[1] == "file":
        path, token, name = parts[0], parts[2], parts[3]
        ext = name.rsplit(".", 1)[-1].lower() if "." in name else "none"
        if ext in SKIP_EXT:
            continue
        target_dir = os.path.join(FEISHU_DIR, os.path.dirname(path))
        if not os.path.exists(os.path.join(target_dir, name)):
            count += 1
            if count <= 10:
                print(f"{count}. [{ext}] {name}")
                print(f"   {path}")

print(f"\n小文件待下载: {count}")
