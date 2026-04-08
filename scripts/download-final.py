#!/usr/bin/env python3
"""最后一轮下载，跳过展会/lbs分卷/共享文件，300秒超时"""
import os, re, time, signal

FEISHU_DIR = "4-Archives/Notes/Feishu"
TIMEOUT = 300
SKIP_DIRS = ["往期展会资料合集", "共享文件", "私有化部署文件"]

signal.signal(signal.SIGCHLD, signal.SIG_IGN)

def download_one(token, filename, target_dir):
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

with open("1-Projects/Personal/笔记迁移/飞书迁移状态报告.tsv") as f:
    lines = f.readlines()[1:]

pending = []
for line in lines:
    parts = line.strip().split("\t")
    if len(parts) >= 5 and "❌" in parts[4] and parts[1] == "file":
        path, token, name = parts[0], parts[2], parts[3]
        if any(s in path for s in SKIP_DIRS):
            continue
        target_dir = os.path.join(FEISHU_DIR, os.path.dirname(path))
        if not os.path.exists(os.path.join(target_dir, name)):
            pending.append((token, name, target_dir))

print(f"待下载（跳过展会/lbs/共享）: {len(pending)}")
print(f"超时: {TIMEOUT}秒")
print(flush=True)

success = 0
timeout_count = 0
fail = 0

for i, (token, name, target_dir) in enumerate(pending):
    result = download_one(token, name, target_dir)
    if result == "ok":
        success += 1
    elif result == "timeout":
        timeout_count += 1
    elif result == "fail":
        fail += 1
    if (i + 1) % 10 == 0 or result != "skip":
        print(f"[{i+1}/{len(pending)}] ok={success} timeout={timeout_count} fail={fail}", flush=True)
    time.sleep(0.05)

print(f"\n=== 完成 {time.strftime('%H:%M:%S')} ===", flush=True)
print(f"成功: {success}, 超时: {timeout_count}, 失败: {fail}", flush=True)
