#!/usr/bin/env python3
import subprocess, json, os, re, time

FEISHU_DIR = "4-Archives/Notes/Feishu"

def run(args, timeout=30):
    try:
        r = subprocess.run(args, capture_output=True, text=True, timeout=timeout)
        return json.loads(r.stdout) if r.stdout.strip() else None
    except:
        return None

def safe_name(name):
    return re.sub(r'[/\\:*?"<>|]', '-', name)

def export_xlsx(token, ftype, title, target_dir):
    sn = safe_name(title)
    out = os.path.join(target_dir, f"{sn}.xlsx")
    if os.path.exists(out):
        print(f"  ⏭️ 已存在")
        return True
    d = run(["lark-cli", "api", "POST", "/open-apis/drive/v1/export_tasks",
             "--data", json.dumps({"file_extension": "xlsx", "token": token, "type": ftype}),
             "--as", "user"])
    if not d:
        print(f"  ❌ API 无响应")
        return False
    if d.get("code") != 0:
        print(f"  ❌ code={d.get('code')}, msg={d.get('msg')}")
        return False
    ticket = d["data"]["ticket"]
    time.sleep(5)
    d = run(["lark-cli", "api", "GET", f"/open-apis/drive/v1/export_tasks/{ticket}",
             "--params", json.dumps({"token": token}), "--as", "user"])
    if not d:
        print(f"  ❌ 查询无响应")
        return False
    result = d.get("data", {}).get("result", {})
    if result.get("job_status") != 0:
        print(f"  ❌ job_status={result.get('job_status')}, msg={result.get('job_error_msg')}")
        return False
    ft = result["file_token"]
    os.makedirs(target_dir, exist_ok=True)
    run(["lark-cli", "api", "GET", f"/open-apis/drive/v1/export_tasks/file/{ft}/download",
         "--output", out, "--as", "user"], timeout=60)
    if os.path.exists(out):
        print(f"  ✅")
        return True
    print(f"  ❌ 下载失败")
    return False

def export_doc(token, title, target_dir):
    sn = safe_name(title)
    out = os.path.join(target_dir, f"{sn}.md")
    if os.path.exists(out):
        print(f"  ⏭️ 已存在")
        return True
    d = run(["lark-cli", "api", "POST", "/open-apis/drive/v1/export_tasks",
             "--data", json.dumps({"file_extension": "docx", "token": token, "type": "doc"}),
             "--as", "user"])
    if not d:
        print(f"  ❌ API 无响应")
        return False
    if d.get("code") != 0:
        print(f"  ❌ code={d.get('code')}, msg={d.get('msg')}")
        return False
    ticket = d["data"]["ticket"]
    time.sleep(5)
    d = run(["lark-cli", "api", "GET", f"/open-apis/drive/v1/export_tasks/{ticket}",
             "--params", json.dumps({"token": token}), "--as", "user"])
    if not d:
        print(f"  ❌ 查询无响应")
        return False
    result = d.get("data", {}).get("result", {})
    if result.get("job_status") != 0:
        print(f"  ❌ job_status={result.get('job_status')}, msg={result.get('job_error_msg')}")
        return False
    ft = result["file_token"]
    att_dir = os.path.join(target_dir, "Attachments")
    os.makedirs(att_dir, exist_ok=True)
    docx_path = os.path.join(att_dir, f"{sn}.docx")
    run(["lark-cli", "api", "GET", f"/open-apis/drive/v1/export_tasks/file/{ft}/download",
         "--output", docx_path, "--as", "user"], timeout=60)
    if not os.path.exists(docx_path):
        print(f"  ❌ 下载失败")
        return False
    subprocess.run(["pandoc", docx_path, "-t", "markdown",
                    "--extract-media=" + att_dir, "-o", "/tmp/doc_tmp.md"],
                   capture_output=True, timeout=30)
    if not os.path.exists("/tmp/doc_tmp.md"):
        print(f"  ❌ pandoc 失败")
        return False
    with open("/tmp/doc_tmp.md") as f:
        content = f.read()
    content = content.replace(att_dir + "/", "Attachments/")
    content = re.sub(r"\{width=[^}]+\}", "", content)
    fm = f'---\ntitle: "{sn}"\nsource: feishu\nfeishu_token: "{token}"\nfeishu_type: doc\nexport_method: export-api+pandoc\nmigrated: 2026-04-06\ntags:\n  - feishu-migration\n---\n\n'
    with open(out, "w") as f:
        f.write(fm + content)
    print(f"  ✅")
    return True

failed = [
    ("doc", "doccnqFsgemZ3ESzWnfkcXfgeAh", "zhenhua_zhtl 集群", "云空间/莱讯科技/项目运维管理/集群资料/私有化部署"),
    ("sheet", "C92zswAxCheFbstoj5gclTr1n5e", "上料记录跟踪", "云空间/莱讯科技/项目开发管理/定位平台定制版/内蒙新太项目"),
    ("bitable", "bascnJYavmFDqZuOCPFO8LDSZku", "2023年项目管理", "云空间/莱讯科技/项目开发管理/定位平台企业版"),
    ("bitable", "A68tbOi2zaUPe9s4X6Ic0LZdnof", "项目管理-武汉机场", "云空间/莱讯科技/项目开发管理/定位平台定制版/武汉机场项目"),
]

for ftype, token, name, path in failed:
    target = os.path.join(FEISHU_DIR, path)
    print(f"📄 {name} [{ftype}]")
    if ftype == "doc":
        export_doc(token, name, target)
    elif ftype == "sheet":
        export_xlsx(token, "sheet", name, target)
    elif ftype == "bitable":
        export_xlsx(token, "bitable", name, target)
    time.sleep(0.5)
