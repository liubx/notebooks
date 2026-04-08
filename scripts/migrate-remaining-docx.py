#!/usr/bin/env python3
"""批量迁移未迁移的非会议纪要 docx 文档"""
import subprocess, json, os, re, time, sys

FEISHU_DIR = "4-Archives/Notes/Feishu"
TSV = "1-Projects/Personal/笔记迁移/飞书完整文件清单.tsv"
MEETING_KEYWORDS = ["会议", "纪要", "速递", "文字记录", "Video meeting", "AI notes", "播客版"]

def run(args, timeout=30):
    try:
        r = subprocess.run(args, capture_output=True, text=True, timeout=timeout)
        return json.loads(r.stdout) if r.stdout.strip() else None
    except:
        return None

def get_migrated_tokens():
    tokens = set()
    for root, dirs, files in os.walk(FEISHU_DIR):
        for fn in files:
            if fn.endswith(".md"):
                try:
                    with open(os.path.join(root, fn)) as f:
                        c = f.read(1000)
                    m = re.search(r'feishu_token:\s*"([^"]+)"', c)
                    if m:
                        tokens.add(m.group(1))
                except:
                    pass
    return tokens

def fetch_and_save(token, title, target_dir):
    d = run(["lark-cli", "docs", "+fetch", "--doc", token, "--as", "user"])
    if not d or not d.get("ok"):
        return False
    md = d["data"]["markdown"]
    
    # 图片处理
    imgs = re.findall(r'<image token="([^"]+)"', md)
    img_map = {}
    if imgs:
        att_dir = os.path.join(target_dir, "Attachments")
        os.makedirs(att_dir, exist_ok=True)
        for it in imgs:
            for ext in ["png", "jpg", "jpeg", "gif", "webp"]:
                if os.path.exists(os.path.join(att_dir, f"{it}.{ext}")):
                    img_map[it] = f"{it}.{ext}"
                    break
            else:
                dl = run(["lark-cli", "docs", "+media-download", "--token", it,
                         "--output", os.path.join(att_dir, it), "--as", "user"])
                if dl and dl.get("ok"):
                    img_map[it] = os.path.basename(dl["data"]["saved_path"])
            time.sleep(0.1)
    
    def repl(m):
        t = re.search(r'token="([^"]+)"', m.group(0))
        if t and t.group(1) in img_map:
            return f"![](Attachments/{img_map[t.group(1)]})"
        return m.group(0)
    md = re.sub(r"<image[^>]*/>", repl, md)
    
    # 安全文件名
    safe_title = re.sub(r'[/\\:*?"<>|]', '-', title)
    
    fm = f'''---
title: "{safe_title}"
source: feishu
feishu_token: "{token}"
feishu_type: docx
feishu_url: "https://reliablesense.feishu.cn/docx/{token}"
migrated: 2026-04-05
tags:
  - feishu-migration
---

'''
    filepath = os.path.join(target_dir, f"{safe_title}.md")
    with open(filepath, "w") as f:
        f.write(fm + md)
    return True

# 读取清单
with open(TSV) as f:
    lines = f.readlines()[1:]

all_docx = []
for line in lines:
    parts = line.strip().split("\t")
    if len(parts) >= 4 and parts[1] == "docx":
        all_docx.append({"path": parts[0], "token": parts[2], "name": parts[3]})

# 已迁移的 token
migrated = get_migrated_tokens()

# 过滤：未迁移 + 非会议纪要
to_migrate = []
for d in all_docx:
    if d["token"] in migrated:
        continue
    if any(k in d["name"] for k in MEETING_KEYWORDS):
        continue
    to_migrate.append(d)

print(f"docx 总数: {len(all_docx)}")
print(f"已迁移: {len(migrated)}")
print(f"待迁移(非会议纪要): {len(to_migrate)}")
print()

# 批量迁移
success = 0
fail = 0
for i, d in enumerate(to_migrate):
    token = d["token"]
    name = d["name"]
    path = d["path"]
    
    # 构建本地目录
    target_dir = os.path.join(FEISHU_DIR, os.path.dirname(path))
    os.makedirs(target_dir, exist_ok=True)
    
    # 检查是否已存在
    safe_name = re.sub(r'[/\\:*?"<>|]', '-', name)
    if os.path.exists(os.path.join(target_dir, f"{safe_name}.md")):
        continue
    
    print(f"[{i+1}/{len(to_migrate)}] 📄 {name}")
    if fetch_and_save(token, name, target_dir):
        print(f"  ✅")
        success += 1
    else:
        print(f"  ❌")
        fail += 1
    time.sleep(0.3)

print(f"\n=== 完成 {time.strftime('%H:%M:%S')} ===")
print(f"成功: {success}, 失败: {fail}")
