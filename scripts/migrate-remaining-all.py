#!/usr/bin/env python3
"""批量迁移剩余的 doc、sheet、bitable"""
import subprocess, json, os, re, time

FEISHU_DIR = "4-Archives/Notes/Feishu"
TSV = "1-Projects/Personal/笔记迁移/飞书完整文件清单.tsv"

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

def safe_name(name):
    return re.sub(r'[/\\:*?"<>|]', '-', name)

def export_via_api(token, ftype, title, target_dir, ext="xlsx"):
    """通过导出 API 导出 sheet/bitable 为 xlsx"""
    out = os.path.join(target_dir, f"{safe_name(title)}.{ext}")
    if os.path.exists(out):
        return True
    d = run(["lark-cli", "api", "POST", "/open-apis/drive/v1/export_tasks",
             "--data", json.dumps({"file_extension": ext, "token": token, "type": ftype}),
             "--as", "user"])
    if not d or d.get("code") != 0:
        return False
    ticket = d["data"]["ticket"]
    time.sleep(4)
    d = run(["lark-cli", "api", "GET", f"/open-apis/drive/v1/export_tasks/{ticket}",
             "--params", json.dumps({"token": token}), "--as", "user"])
    if not d or d.get("data", {}).get("result", {}).get("job_status") != 0:
        return False
    ft = d["data"]["result"]["file_token"]
    os.makedirs(target_dir, exist_ok=True)
    run(["lark-cli", "api", "GET", f"/open-apis/drive/v1/export_tasks/file/{ft}/download",
         "--output", out, "--as", "user"], timeout=60)
    return os.path.exists(out)

def export_doc(token, title, target_dir):
    """导出 doc 旧版文档为 Markdown"""
    sn = safe_name(title)
    out = os.path.join(target_dir, f"{sn}.md")
    if os.path.exists(out):
        return True
    # 导出为 docx
    d = run(["lark-cli", "api", "POST", "/open-apis/drive/v1/export_tasks",
             "--data", json.dumps({"file_extension": "docx", "token": token, "type": "doc"}),
             "--as", "user"])
    if not d or d.get("code") != 0:
        return False
    ticket = d["data"]["ticket"]
    time.sleep(4)
    d = run(["lark-cli", "api", "GET", f"/open-apis/drive/v1/export_tasks/{ticket}",
             "--params", json.dumps({"token": token}), "--as", "user"])
    if not d or d.get("data", {}).get("result", {}).get("job_status") != 0:
        return False
    ft = d["data"]["result"]["file_token"]
    att_dir = os.path.join(target_dir, "Attachments")
    os.makedirs(att_dir, exist_ok=True)
    docx_path = os.path.join(att_dir, f"{sn}.docx")
    run(["lark-cli", "api", "GET", f"/open-apis/drive/v1/export_tasks/file/{ft}/download",
         "--output", docx_path, "--as", "user"], timeout=60)
    if not os.path.exists(docx_path):
        return False
    # pandoc 转换
    subprocess.run(["pandoc", docx_path, "-t", "markdown",
                    "--extract-media=" + att_dir, "-o", "/tmp/doc_tmp.md"],
                   capture_output=True, timeout=30)
    if not os.path.exists("/tmp/doc_tmp.md"):
        return False
    with open("/tmp/doc_tmp.md") as f:
        content = f.read()
    content = content.replace(att_dir + "/", "Attachments/")
    content = re.sub(r"\{width=[^}]+\}", "", content)
    fm = f'---\ntitle: "{sn}"\nsource: feishu\nfeishu_token: "{token}"\nfeishu_type: doc\nexport_method: export-api+pandoc\nmigrated: 2026-04-06\ntags:\n  - feishu-migration\n---\n\n'
    with open(out, "w") as f:
        f.write(fm + content)
    return True

# 读取清单
with open(TSV) as f:
    lines = f.readlines()[1:]

migrated = get_migrated_tokens()

# 也检查已存在的 xlsx
existing_xlsx = set()
for root, dirs, files in os.walk(FEISHU_DIR):
    for fn in files:
        if fn.endswith(".xlsx"):
            existing_xlsx.add(fn)

# 分类
docs_to_migrate = []
sheets_to_migrate = []
bitables_to_migrate = []

for line in lines:
    parts = line.strip().split("\t")
    if len(parts) < 4:
        continue
    path, ftype, token, name = parts[0], parts[1], parts[2], parts[3]
    sn = safe_name(name)
    target_dir = os.path.join(FEISHU_DIR, os.path.dirname(path))
    
    if ftype == "doc" and token not in migrated:
        if not os.path.exists(os.path.join(target_dir, f"{sn}.md")):
            docs_to_migrate.append((token, name, target_dir))
    elif ftype == "sheet":
        if f"{sn}.xlsx" not in existing_xlsx and not os.path.exists(os.path.join(target_dir, f"{sn}.xlsx")):
            sheets_to_migrate.append((token, name, target_dir))
    elif ftype == "bitable":
        if f"{sn}.xlsx" not in existing_xlsx and not os.path.exists(os.path.join(target_dir, f"{sn}.xlsx")):
            bitables_to_migrate.append((token, name, target_dir))

print(f"待处理: doc={len(docs_to_migrate)}, sheet={len(sheets_to_migrate)}, bitable={len(bitables_to_migrate)}")
print()

# 处理 doc
if docs_to_migrate:
    print(f"=== doc 旧版文档 ({len(docs_to_migrate)}) ===")
    for i, (token, name, target_dir) in enumerate(docs_to_migrate):
        print(f"[{i+1}/{len(docs_to_migrate)}] 📄 {name}")
        if export_doc(token, name, target_dir):
            print("  ✅")
        else:
            print("  ❌")
        time.sleep(0.3)

# 处理 sheet
if sheets_to_migrate:
    print(f"\n=== sheet ({len(sheets_to_migrate)}) ===")
    for i, (token, name, target_dir) in enumerate(sheets_to_migrate):
        print(f"[{i+1}/{len(sheets_to_migrate)}] 📊 {name}")
        if export_via_api(token, "sheet", name, target_dir):
            print("  ✅")
        else:
            print("  ❌")
        time.sleep(0.3)

# 处理 bitable
if bitables_to_migrate:
    print(f"\n=== bitable ({len(bitables_to_migrate)}) ===")
    for i, (token, name, target_dir) in enumerate(bitables_to_migrate):
        print(f"[{i+1}/{len(bitables_to_migrate)}] 📋 {name}")
        if export_via_api(token, "bitable", name, target_dir):
            print("  ✅")
        else:
            print("  ❌")
        time.sleep(0.3)

print(f"\n=== 完成 {time.strftime('%H:%M:%S')} ===")
