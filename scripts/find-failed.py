#!/usr/bin/env python3
import os, re

TSV = "1-Projects/Personal/笔记迁移/飞书完整文件清单.tsv"
FEISHU_DIR = "4-Archives/Notes/Feishu"
MEETING_KW = ["会议", "纪要", "速递", "文字记录", "Video meeting", "AI notes", "播客版"]

with open(TSV) as f:
    lines = f.readlines()[1:]

migrated = set()
for root, dirs, files in os.walk(FEISHU_DIR):
    for fn in files:
        if fn.endswith(".md"):
            try:
                with open(os.path.join(root, fn)) as f:
                    c = f.read(1000)
                m = re.search(r'feishu_token:\s*"([^"]+)"', c)
                if m:
                    migrated.add(m.group(1))
            except:
                pass

print(f"已迁移 token 数: {len(migrated)}")
print()
print("未迁移的非会议纪要 docx:")
for line in lines:
    parts = line.strip().split("\t")
    if len(parts) >= 4 and parts[1] == "docx":
        token, name, path = parts[2], parts[3], parts[0]
        if token in migrated:
            continue
        if any(k in name for k in MEETING_KW):
            continue
        safe = re.sub(r'[/\\:*?"<>|]', '-', name)
        target_dir = os.path.join(FEISHU_DIR, os.path.dirname(path))
        if not os.path.exists(os.path.join(target_dir, f"{safe}.md")):
            print(f"  {name}")
            print(f"    token: {token}")
            print(f"    path: {path}")
