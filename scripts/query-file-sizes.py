#!/usr/bin/env python3
"""批量查询 file 类型的文件大小"""
import subprocess, json, time, os

TSV = "1-Projects/Personal/笔记迁移/飞书完整文件清单.tsv"

with open(TSV) as f:
    lines = f.readlines()[1:]

# 提取所有 file 类型的 token
file_tokens = []
for line in lines:
    parts = line.strip().split("\t")
    if len(parts) >= 4 and parts[1] == "file":
        file_tokens.append((parts[2], parts[3], parts[0]))

print(f"file 类型总数: {len(file_tokens)}")

# batch_query 每次最多 15 个
total_size = 0
count = 0
sizes = []

for i in range(0, len(file_tokens), 15):
    batch = file_tokens[i:i+15]
    request_docs = [{"doc_token": t, "doc_type": "file"} for t, _, _ in batch]
    
    try:
        r = subprocess.run(
            ["lark-cli", "drive", "metas", "batch_query",
             "--data", json.dumps({"request_docs": request_docs}),
             "--as", "user"],
            capture_output=True, text=True, timeout=30
        )
        data = json.loads(r.stdout)
        if data.get("code") == 0:
            for meta in data.get("data", {}).get("metas", []):
                # metas 不返回 size，但 export 结果有
                pass
    except:
        pass
    
    if (i // 15) % 20 == 0:
        print(f"  进度: {i}/{len(file_tokens)}")
    time.sleep(0.2)

# batch_query 不返回文件大小...换个方式
# 用 sheets +export 的 dry-run 也不行
# 实际上飞书 API 没有批量获取文件大小的接口
# 只能通过 drive/v1/files 列出文件夹时拿到的信息

print("\n注意: drive metas batch_query 不返回文件大小")
print("需要通过 list_folder API 获取（扫描时已经调用过了）")
print("重新扫描并记录大小...")
