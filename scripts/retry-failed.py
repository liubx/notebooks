#!/usr/bin/env python3
import subprocess, json, os, re, time

FEISHU_DIR = "4-Archives/Notes/Feishu"

def run(args, timeout=30):
    try:
        r = subprocess.run(args, capture_output=True, text=True, timeout=timeout)
        return json.loads(r.stdout) if r.stdout.strip() else None
    except:
        return None

def fetch_and_save(token, title, target_dir):
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
    safe = re.sub(r'[/\\:*?"<>|]', '-', title)
    fm = f'---\ntitle: "{safe}"\nsource: feishu\nfeishu_token: "{token}"\nfeishu_type: docx\nmigrated: 2026-04-06\ntags:\n  - feishu-migration\n---\n\n'
    with open(os.path.join(target_dir, f"{safe}.md"), "w") as f:
        f.write(fm + md)
    return True

target = os.path.join(FEISHU_DIR, "云空间/莱讯科技/公司内部资料/ISO9001质量体系认证/麦钉项目")
os.makedirs(target, exist_ok=True)

for token, name in [
    ("doxcnt148nDbZ8CKkbPwDPO60fb", "4 详细设计说明书（软件）"),
    ("doxcn60f5Ucj7TXGv7I34r4V5Tb", "10 测试分析报告"),
]:
    print(f"📄 {name}")
    if fetch_and_save(token, name, target):
        print("  ✅")
    else:
        print("  ❌")
