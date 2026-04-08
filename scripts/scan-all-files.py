#!/usr/bin/env python3
"""
递归扫描飞书云空间所有文件，生成完整清单。
同时扫描知识库节点。
输出到 /tmp/feishu-all-files.md
"""
import subprocess, json, time, os

def run(args, timeout=30):
    try:
        r = subprocess.run(args, capture_output=True, text=True, timeout=timeout)
        return json.loads(r.stdout) if r.stdout.strip() else None
    except:
        return None

def list_folder(token):
    d = run(["lark-cli", "api", "GET", "/open-apis/drive/v1/files",
             "--params", json.dumps({"folder_token": token, "page_size": "200"}),
             "--as", "user"])
    if d and d.get("code") == 0:
        return d.get("data", {}).get("files", [])
    return []

all_files = []  # (path, type, token, name)

def scan_folder(token, path, depth=0):
    if depth > 5:
        return
    files = list_folder(token)
    time.sleep(0.3)
    for f in files:
        ftype = f["type"]
        name = f["name"]
        ftk = f["token"]
        full_path = f"{path}/{name}"
        if ftype == "folder":
            print(f"{'  ' * depth}📁 {name}")
            scan_folder(ftk, full_path, depth + 1)
        else:
            all_files.append((full_path, ftype, ftk, name))
            icon = {"docx":"📄","doc":"📄","sheet":"📊","bitable":"📋",
                    "file":"📎","slides":"🎞️","mindnote":"🧠"}.get(ftype, "❓")
            print(f"{'  ' * depth}{icon} {name} [{ftype}]")

# 获取根目录
print("=== 扫描云空间 ===")
d = run(["lark-cli", "api", "GET", "/open-apis/drive/explorer/v2/root_folder/meta", "--as", "user"])
root_token = d["data"]["token"]
scan_folder(root_token, "云空间")

# 扫描知识库
print("\n=== 扫描知识库 ===")
# 团队知识库
spaces = [
    ("7065147197469458433", "技术分享"),
    ("7445886335376523292", "项目管理"),
    ("7066050160966516764", "规章制度"),
]
# 个人知识库
personal_spaces = [
    ("7559791731407912963", "个人知识库-1"),
    ("7527250303092015107", "个人知识库-2"),
    ("7527246326739157011", "个人知识库-3"),
    ("7527253598389125148", "受限-1"),
    ("7586861617376267458", "受限-2"),
    ("7527985368571756572", "受限-3"),
    ("7533431263699501059", "受限-4"),
    ("7530814402510241820", "受限-5"),
    ("7552826134947381251", "受限-6"),
]

def scan_wiki_space(space_id, space_name, parent_path="知识库"):
    d = run(["lark-cli", "wiki", "spaces", "list_nodes",
             "--params", json.dumps({"space_id": space_id, "page_size": "50"}),
             "--as", "user"])
    if not d or d.get("code") != 0:
        # 尝试用 spaceNode.list
        return
    nodes = d.get("data", {}).get("items", [])
    for node in nodes:
        obj_type = node.get("obj_type", "?")
        obj_token = node.get("obj_token", "")
        title = node.get("title", "未命名")
        node_token = node.get("node_token", "")
        has_child = node.get("has_child", False)
        full_path = f"{parent_path}/{space_name}/{title}"
        all_files.append((full_path, obj_type, obj_token, title))
        icon = {"docx":"📄","doc":"📄","sheet":"📊","bitable":"📋",
                "file":"📎","slides":"🎞️","mindnote":"🧠"}.get(obj_type, "❓")
        print(f"  {icon} {title} [{obj_type}]")
        
        if has_child:
            scan_wiki_children(space_id, node_token, full_path)
    time.sleep(0.3)

def scan_wiki_children(space_id, parent_node_token, parent_path):
    d = run(["lark-cli", "wiki", "spaces", "list_nodes",
             "--params", json.dumps({"space_id": space_id, "parent_node_token": parent_node_token, "page_size": "50"}),
             "--as", "user"])
    if not d or d.get("code") != 0:
        return
    nodes = d.get("data", {}).get("items", [])
    for node in nodes:
        obj_type = node.get("obj_type", "?")
        obj_token = node.get("obj_token", "")
        title = node.get("title", "未命名")
        node_token = node.get("node_token", "")
        has_child = node.get("has_child", False)
        full_path = f"{parent_path}/{title}"
        all_files.append((full_path, obj_type, obj_token, title))
        icon = {"docx":"📄","doc":"📄","sheet":"📊","bitable":"📋",
                "file":"📎","slides":"🎞️","mindnote":"🧠"}.get(obj_type, "❓")
        print(f"    {icon} {title} [{obj_type}]")
        
        if has_child:
            scan_wiki_children(space_id, node_token, full_path)
    time.sleep(0.3)

for space_id, space_name in spaces:
    print(f"\n📚 {space_name}")
    scan_wiki_space(space_id, space_name)

for space_id, space_name in personal_spaces:
    print(f"\n📚 {space_name}")
    scan_wiki_space(space_id, space_name)

# 输出完整清单
print(f"\n\n=== 总计 {len(all_files)} 个文件 ===")

# 按类型统计
from collections import Counter
type_count = Counter(f[1] for f in all_files)
for t, c in type_count.most_common():
    print(f"  {t}: {c}")

# 写入文件
with open("/tmp/feishu-all-files.tsv", "w") as f:
    f.write("路径\t类型\tToken\t标题\n")
    for path, ftype, token, name in all_files:
        f.write(f"{path}\t{ftype}\t{token}\t{name}\n")

print(f"\n完整清单已保存到 /tmp/feishu-all-files.tsv")
