#!/usr/bin/env python3
"""
批量下载 file 附件 v6
用 os.fork() 隔离下载，父进程用 WNOHANG 非阻塞等待
超时后直接 os.kill(SIGKILL) 并继续，不等待僵尸进程
"""
import os, time, signal, sys

FEISHU_DIR = "4-Archives/Notes/Feishu"
TSV = "1-Projects/Personal/笔记迁移/飞书完整文件清单.tsv"
TIMEOUT = 120
SKIP_EXT = set()  # 不跳过任何扩展名，全部尝试

# 忽略子进程退出信号，避免僵尸进程
signal.signal(signal.SIGCHLD, signal.SIG_IGN)

def download_one(token, filename, target_dir):
    path = os.path.join(target_dir, filename)
    if os.path.exists(path):
        return "skip"
    os.makedirs(target_dir, exist_ok=True)
    
    pid = os.fork()
    if pid == 0:
        # 子进程：执行下载然后退出
        os.setsid()
        os.execvp("lark-cli", ["lark-cli", "drive", "+download",
                                "--file-token", token, "--output", path, "--as", "user"])
        os._exit(1)
    
    # 父进程：非阻塞等待
    start = time.time()
    while True:
        try:
            wpid, status = os.waitpid(pid, os.WNOHANG)
        except ChildProcessError:
            wpid = pid  # 已被 SIG_IGN 回收
            break
        
        if wpid != 0:
            break
        
        if time.time() - start > TIMEOUT:
            # 超时，杀掉整个进程组
            try: os.killpg(pid, signal.SIGKILL)
            except: pass
            try: os.kill(pid, signal.SIGKILL)
            except: pass
            # 清理文件
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

# 读取清单
with open(TSV) as f:
    lines = f.readlines()[1:]

small_files = []
big_count = 0
for line in lines:
    parts = line.strip().split("\t")
    if len(parts) >= 4 and parts[1] == "file":
        path, token, name = parts[0], parts[2], parts[3]
        ext = name.rsplit(".", 1)[-1].lower() if "." in name else ""
        target_dir = os.path.join(FEISHU_DIR, os.path.dirname(path))
        if ext in SKIP_EXT:
            big_count += 1
        else:
            small_files.append((token, name, target_dir))

already = sum(1 for t, n, d in small_files if os.path.exists(os.path.join(d, n)))
print(f"小文件: {len(small_files)}, 已下载: {already}, 待下载: {len(small_files) - already}")
print(f"大文件(跳过): {big_count}")
print(flush=True)

success = 0
skipped = 0
failed = 0
timeout_count = 0

for i, (token, name, target_dir) in enumerate(small_files):
    result = download_one(token, name, target_dir)
    
    if result == "ok":
        success += 1
    elif result == "skip":
        skipped += 1
    elif result == "timeout":
        timeout_count += 1
    else:
        failed += 1
    
    if (i + 1) % 50 == 0:
        print(f"[{i+1}/{len(small_files)}] ok={success} timeout={timeout_count} fail={failed} skip={skipped}", flush=True)
    
    time.sleep(0.05)

print(f"\n=== 完成 {time.strftime('%H:%M:%S')} ===", flush=True)
print(f"成功: {success}, 超时: {timeout_count}, 失败: {failed}, 跳过: {skipped}", flush=True)
