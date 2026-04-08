#!/usr/bin/env python3
"""迁移项目资料管理下缺失的文件夹"""
import subprocess, json, time, os, re

BASE = "4-Archives/Notes/Feishu/云空间/莱讯科技/项目资料管理"

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
    return d.get("data", {}).get("files", []) if d else []

def export_xlsx(token, ftype, title, target_dir):
    d = run(["lark-cli", "api", "POST", "/open-apis/drive/v1/export_tasks",
             "--data", json.dumps({"file_extension": "xlsx", "token": token, "type": ftype}),
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
    run(["lark-cli", "api", "GET", f"/open-apis/drive/v1/export_tasks/file/{ft}/download",
         "--output", os.path.join(target_dir, f"{title}.xlsx"), "--as", "user"], timeout=60)
    return os.path.exists(os.path.join(target_dir, f"{title}.xlsx"))

def fetch_docx(token, title, target_dir):
    d = run(["lark-cli", "docs", "+fetch", "--doc", token, "--as", "user"])
    if not d or not d.get("ok"):
        return False
    md = d["data"]["markdown"]
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
    fm = f'---\ntitle: "{title}"\nsource: feishu\nfeishu_token: "{token}"\nfeishu_type: docx\nmigrated: 2026-04-05\ntags:\n  - feishu-migration\n---\n\n'
    with open(os.path.join(target_dir, f"{title}.md"), "w") as f:
        f.write(fm + md)
    return True

def export_doc(token, title, target_dir):
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
    docx_path = os.path.join(att_dir, f"{title}.docx")
    run(["lark-cli", "api", "GET", f"/open-apis/drive/v1/export_tasks/file/{ft}/download",
         "--output", docx_path, "--as", "user"], timeout=60)
    if not os.path.exists(docx_path):
        return False
    subprocess.run(["pandoc", docx_path, "-t", "markdown",
                    "--extract-media=" + att_dir, "-o", "/tmp/doc_tmp.md"],
                   capture_output=True, timeout=30)
    if os.path.exists("/tmp/doc_tmp.md"):
        with open("/tmp/doc_tmp.md") as f:
            content = f.read()
        content = content.replace(att_dir + "/", "Attachments/")
        content = re.sub(r"\{width=[^}]+\}", "", content)
        fm = f'---\ntitle: "{title}"\nsource: feishu\nfeishu_token: "{token}"\nfeishu_type: doc\nexport_method: export-api+pandoc\nmigrated: 2026-04-05\ntags:\n  - feishu-migration\n---\n\n'
        with open(os.path.join(target_dir, f"{title}.md"), "w") as f:
            f.write(fm + content)
        return True
    return False

def download_file(token, title, target_dir):
    path = os.path.join(target_dir, title)
    if os.path.exists(path):
        return True
    run(["lark-cli", "drive", "+download", "--file-token", token,
         "--output", path, "--as", "user"], timeout=30)
    return os.path.exists(path)

folders = [
    ("JgzWfy33SlvnsSdrg5Uc3Fdrnm1", "000. 售前项目"),
    ("JuNOf2llHlkIa9dKw73cJm5pn3w", "南宁机场项目"),
    ("UF9cfyxN7lnWIwd02auc28fFnOg", "003. 中东电子厂客户"),
    ("R0Jef62eAlU8d8dONehcJ0CdnOb", "998. 售后项目"),
    ("fldcnRPjh6QcMmwt4l61XoCDfqd", "~其他项目"),
    ("O2CofScN2lERyKdxnlych2jbnVe", "999. 归档项目"),
    ("WW7df5NEglBmvCdYGDQcFZNKnEe", "项目评估"),
    ("fldcnZ6HnXhRV12CUM57fItepSe", "展会"),
]

print(f"=== 开始迁移缺失文件夹 {time.strftime('%H:%M:%S')} ===")

for folder_token, folder_name in folders:
    target = os.path.join(BASE, folder_name)
    os.makedirs(target, exist_ok=True)
    files = list_folder(folder_token)
    non_folders = [f for f in files if f["type"] != "folder"]
    sub_folders = [f for f in files if f["type"] == "folder"]
    print(f"\n📁 {folder_name} ({len(non_folders)} 文件, {len(sub_folders)} 子文件夹)")

    for f in non_folders:
        t, name, ftype = f["token"], f["name"], f["type"]
        if ftype == "docx":
            if os.path.exists(os.path.join(target, f"{name}.md")):
                print(f"  ⏭️ {name}")
                continue
            print(f"  📄 {name}")
            print(f"    {'✅' if fetch_docx(t, name, target) else '❌'}")
        elif ftype == "doc":
            if os.path.exists(os.path.join(target, f"{name}.md")):
                print(f"  ⏭️ {name}")
                continue
            print(f"  📄 {name} (doc)")
            print(f"    {'✅' if export_doc(t, name, target) else '❌'}")
        elif ftype in ("sheet", "bitable"):
            if os.path.exists(os.path.join(target, f"{name}.xlsx")):
                print(f"  ⏭️ {name}")
                continue
            print(f"  📊 {name}")
            print(f"    {'✅' if export_xlsx(t, ftype, name, target) else '❌'}")
        elif ftype == "file":
            if os.path.exists(os.path.join(target, name)):
                print(f"  ⏭️ {name}")
                continue
            print(f"  📎 {name}")
            print(f"    {'✅' if download_file(t, name, target) else '❌ (超时)'}")
        elif ftype == "slides":
            print(f"  🎞️ {name} (slides, 需手动)")
        else:
            print(f"  ❓ {name} ({ftype})")
        time.sleep(0.3)

    if sub_folders:
        for sf in sub_folders:
            print(f"  📁 子文件夹: {sf['name']}")

print(f"\n=== 完成 {time.strftime('%H:%M:%S')} ===")
