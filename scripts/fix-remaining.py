#!/usr/bin/env python3
"""处理剩余未迁移的 sheet/bitable，以及跳过展会资料的 file 下载"""
import subprocess, json, os, re, time, signal

FEISHU_DIR = "4-Archives/Notes/Feishu"
SKIP_DIRS = ["往期展会资料合集"]
TIMEOUT = 120

signal.signal(signal.SIGCHLD, signal.SIG_IGN)

def run(args, timeout=30):
    try:
        r = subprocess.run(args, capture_output=True, text=True, timeout=timeout)
        return json.loads(r.stdout) if r.stdout.strip() else None
    except:
        return None

def export_xlsx(token, ftype, title, target_dir):
    safe = re.sub(r'[/\\:*?"<>|]', '-', title)
    out = os.path.join(target_dir, f"{safe}.xlsx")
    if os.path.exists(out):
        return "skip"
    d = run(["lark-cli", "api", "POST", "/open-apis/drive/v1/export_tasks",
             "--data", json.dumps({"file_extension": "xlsx", "token": token, "type": ftype}),
             "--as", "user"])
    if not d or d.get("code") != 0:
        return "fail"
    ticket = d["data"]["ticket"]
    time.sleep(5)
    d = run(["lark-cli", "api", "GET", f"/open-apis/drive/v1/export_tasks/{ticket}",
             "--params", json.dumps({"token": token}), "--as", "user"])
    if not d or d.get("data", {}).get("result", {}).get("job_status") != 0:
        return "fail"
    ft = d["data"]["result"]["file_token"]
    os.makedirs(target_dir, exist_ok=True)
    run(["lark-cli", "api", "GET", f"/open-apis/drive/v1/export_tasks/file/{ft}/download",
         "--output", out, "--as", "user"], timeout=60)
    return "ok" if os.path.exists(out) else "fail"

def download_file(token, filename, target_dir):
    path = os.path.join(target_dir, filename)
    if os.path.exists(path):
        return "skip"
    os.makedirs(target_dir, exist_ok=True)
    pid = os.fork()
    if pid == 0:
        os.setsid()
        os.execvp("lark-cli", ["lark-cli", "drive", "+download",
                                "--file-token", token, "--output", path, "--as", "user"])
        os._exit(1)
    start = time.time()
    while True:
        try:
            wpid, status = os.waitpid(pid, os.WNOHANG)
        except ChildProcessError:
            break
        if wpid != 0:
            break
        if time.time() - start > TIMEOUT:
            try: os.killpg(pid, signal.SIGKILL)
            except: pass
            try: os.kill(pid, signal.SIGKILL)
            except: pass
            time.sleep(0.5)
            if os.path.exists(path):
                try: os.remove(path)
                except: pass
            return "timeout"
        time.sleep(0.3)
    if os.path.exists(path) and os.path.getsize(path) > 0:
        return "ok"
    if os.path.exists(path):
        try: os.remove(path)
        except: pass
    return "fail"

# 读取未迁移清单
with open("1-Projects/Personal/笔记迁移/飞书迁移状态报告.tsv") as f:
    lines = f.readlines()[1:]

pending = []
for line in lines:
    parts = line.strip().split("\t")
    if len(parts) >= 5 and "❌" in parts[4]:
        path, ftype, token, name = parts[0], parts[1], parts[2], parts[3]
        # 跳过展会资料
        if any(skip in path for skip in SKIP_DIRS):
            continue
        target_dir = os.path.join(FEISHU_DIR, os.path.dirname(path))
        pending.append((ftype, token, name, target_dir))

print(f"待处理（跳过展会）: {len(pending)}")

# 按类型分组
by_type = {}
for ftype, token, name, target_dir in pending:
    by_type.setdefault(ftype, []).append((token, name, target_dir))

for t, items in by_type.items():
    print(f"  {t}: {len(items)}")
print()

# 先处理 sheet/bitable
for ftype in ["sheet", "bitable"]:
    items = by_type.get(ftype, [])
    if items:
        print(f"=== {ftype} ({len(items)}) ===")
        for token, name, target_dir in items:
            print(f"  📊 {name}")
            result = export_xlsx(token, ftype, name, target_dir)
            print(f"    {result}")
            time.sleep(0.5)

# 处理 file
files = by_type.get("file", [])
if files:
    print(f"\n=== file ({len(files)}) ===")
    success = 0
    fail = 0
    timeout_count = 0
    for i, (token, name, target_dir) in enumerate(files):
        result = download_file(token, name, target_dir)
        if result == "ok":
            success += 1
        elif result == "timeout":
            timeout_count += 1
        elif result == "fail":
            fail += 1
        if (i + 1) % 20 == 0:
            print(f"  [{i+1}/{len(files)}] ok={success} timeout={timeout_count} fail={fail}", flush=True)
        time.sleep(0.05)
    print(f"  完成: ok={success} timeout={timeout_count} fail={fail}")

# mindnote/slides 提示
for ftype in ["mindnote", "slides"]:
    items = by_type.get(ftype, [])
    if items:
        print(f"\n⚠️ {ftype}: {len(items)} 个需手动处理")

print(f"\n=== 完成 {time.strftime('%H:%M:%S')} ===")
