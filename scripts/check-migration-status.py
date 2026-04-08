#!/usr/bin/env python3
"""
全面对账：飞书完整文件清单 vs 本地已迁移文件
输出详细的迁移状态报告
"""
import os, re
from collections import Counter, defaultdict

FEISHU_DIR = "4-Archives/Notes/Feishu"
TSV_FILE = "1-Projects/Personal/笔记迁移/飞书完整文件清单.tsv"

# 1. 读取飞书完整清单
with open(TSV_FILE) as f:
    lines = f.readlines()[1:]

all_files = []
for line in lines:
    parts = line.strip().split("\t")
    if len(parts) >= 4:
        all_files.append({
            "path": parts[0],
            "type": parts[1],
            "token": parts[2],
            "name": parts[3],
        })

print(f"飞书总文件数: {len(all_files)}")

# 2. 扫描本地所有文件
local_tokens = set()  # md 文件中的 feishu_token
local_files = {}  # 路径 -> 文件名列表

for root, dirs, files in os.walk(FEISHU_DIR):
    rel_root = os.path.relpath(root, FEISHU_DIR)
    for fn in files:
        fp = os.path.join(root, fn)
        
        # 提取 md 中的 feishu_token
        if fn.endswith(".md"):
            try:
                with open(fp) as f:
                    content = f.read(1000)
                m = re.search(r'feishu_token:\s*"([^"]+)"', content)
                if m:
                    local_tokens.add(m.group(1))
            except:
                pass
        
        # 记录所有本地文件
        local_files.setdefault(rel_root, []).append(fn)

# 3. 对账
status = []  # (飞书路径, 类型, token, 名称, 状态)

for f in all_files:
    token = f["token"]
    ftype = f["type"]
    name = f["name"]
    path = f["path"]
    
    if token in local_tokens:
        status.append((path, ftype, token, name, "✅ 已迁移(md)"))
    elif ftype == "shortcut":
        status.append((path, ftype, token, name, "⏭️ 跳过(快捷方式)"))
    else:
        # 检查是否有同名的 xlsx/mm/pdf 等文件
        found = False
        # 构建可能的本地目录
        feishu_path = path.replace("云空间/", "云空间/").replace("知识库/", "知识库/")
        parent = os.path.dirname(feishu_path)
        
        # 检查各种可能的文件名
        possible_names = [
            f"{name}.xlsx",
            f"{name}.mm",
            f"{name}.pdf",
            name,  # file 类型直接用原名
            f"{name}.md",
        ]
        
        for local_root, local_fns in local_files.items():
            for pn in possible_names:
                if pn in local_fns:
                    found = True
                    break
            if found:
                break
        
        if found:
            status.append((path, ftype, token, name, "✅ 已迁移(文件)"))
        else:
            # 判断是否是会议纪要
            if ftype == "docx" and any(k in name for k in ["会议", "纪要", "速递", "文字记录", "Video meeting", "AI notes"]):
                status.append((path, ftype, token, name, "⏳ 会议纪要"))
            else:
                status.append((path, ftype, token, name, "❌ 未迁移"))

# 4. 统计
status_count = Counter(s[4].split("(")[0].strip() for s in status)
type_status = defaultdict(lambda: Counter())
for path, ftype, token, name, st in status:
    type_status[ftype][st.split("(")[0].strip()] += 1

print("\n=== 总体状态 ===")
for st, count in status_count.most_common():
    print(f"  {st}: {count}")

print("\n=== 按类型统计 ===")
print(f"{'类型':10} | {'✅已迁移':>8} | {'❌未迁移':>8} | {'⏳会议纪要':>10} | {'⏭️跳过':>6} | {'总计':>6}")
print("-" * 70)
for ftype in ["file", "docx", "sheet", "bitable", "mindnote", "doc", "slides", "shortcut"]:
    ts = type_status.get(ftype, Counter())
    migrated = ts.get("✅", 0)
    unmigrated = ts.get("❌", 0)
    meeting = ts.get("⏳", 0)
    skipped = ts.get("⏭️", 0)
    total = migrated + unmigrated + meeting + skipped
    if total > 0:
        print(f"{ftype:10} | {migrated:>8} | {unmigrated:>8} | {meeting:>10} | {skipped:>6} | {total:>6}")

# 5. 未迁移文件按顶级目录分组
print("\n=== 未迁移文件按目录 ===")
unmigrated_by_dir = defaultdict(lambda: Counter())
for path, ftype, token, name, st in status:
    if "❌" in st:
        # 取前3级路径
        parts = path.split("/")
        dir_key = "/".join(parts[:3]) if len(parts) >= 3 else path
        unmigrated_by_dir[dir_key][ftype] += 1

for dir_key in sorted(unmigrated_by_dir.keys()):
    tc = unmigrated_by_dir[dir_key]
    total = sum(tc.values())
    detail = ", ".join(f"{t}:{c}" for t, c in tc.most_common())
    print(f"  {dir_key}: {total} ({detail})")

# 6. 保存详细报告
with open("/tmp/migration-status-report.tsv", "w") as f:
    f.write("飞书路径\t类型\tToken\t名称\t状态\n")
    for path, ftype, token, name, st in status:
        f.write(f"{path}\t{ftype}\t{token}\t{name}\t{st}\n")

print("\n详细报告已保存到 /tmp/migration-status-report.tsv")
