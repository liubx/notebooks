#!/usr/bin/env python3
"""
批量下载 file 附件 v4
用 lark-cli api GET 下载，通过 Popen + 线程超时控制
"""
import subprocess, json, os, re, time, threading

FEISHU_DIR = "4-Archives/Notes/Feishu"
TSV = "1-Projects/Personal/笔记迁移/飞书完整文件清单.tsv"
FAILED_LOG = "/tmp/file-download-failed.tsv"
TIMEOUT = 15  # 秒

SKIP_EXT = {"zip","rar","7z","tar","gz","tgz","mp4","mov","mkv","avi","wmv","flv","mp3","wav","iso","apk","exe","msi","dmg","dwg","bak","ai","psd"}

def download(token, filename, target_dir):
    path = os.path.join(target_dir, filename)
    if os.path.exists(path):
        return "skip"
    os.makedirs(target_dir, exist_ok=True)
    
    proc = subprocess.Popen(
        ["lark-cli", "drive", "+download", "--file-token", token,
         "--output", path, "--as", "user"],
        stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
        preexec_fn=os.setsid
    )
    
    start = time.time()
    while True:
        ret = proc.poll()
        if ret is not None:
            break
        if time.time() - start > TIMEOUT:
            # 尝试杀掉，但不等待（可能杀不掉）
            try: os.killpg(os.getpgid(proc.pid), 9)
            except: pass
            try: proc.kill()
            except: pass
            # 不等 proc.wait()，直接返回
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

all_files = []
big_files = []
for line in lines:
    parts = line.strip().split("\t")
    if len(parts) >= 4 and parts[1] == "file":
        path, token, name = parts[0], parts[2], parts[3]
        target_dir = os.path.join(FEISHU_DIR, os.path.dirname(path))
        ext = name.rsplit(".", 1)[-1].lower() if "." in name else ""
        if ext in SKIP_EXT:
            big_files.append((token, name, target_dir, path))
        else:
            all_files.append((token, name, target_dir, path))

already = sum(1 for t, n, d, p in all_files if os.path.exists(os.path.join(d, n)))
print(f"小文件: {len(all_files)}, 已下载: {already}, 待下载: {len(all_files) - already}")
print(f"大文件(跳过): {len(big_files)}")
print()

success = 0
skipped = 0
failed = []

for i, (token, name, target_dir, feishu_path) in enumerate(all_files):
    if os.path.exists(os.path.join(target_dir, name)):
        skipped += 1
        continue
    
    result = download(token, name, target_dir)
    
    if result == "ok":
        success += 1
    elif result == "skip":
        skipped += 1
    else:
        failed.append((token, name, feishu_path, result))
    
    if (i + 1) % 50 == 0:
        print(f"[{i+1}/{len(all_files)}] {success} ok, {len(failed)} fail, {skipped} skip")
    
    time.sleep(0.05)

with open(FAILED_LOG, "w") as f:
    f.write("Token\t文件名\t飞书路径\t原因\n")
    for token, name, path, reason in failed:
        f.write(f"{token}\t{name}\t{path}\t{reason}\n")

print(f"\n=== 完成 {time.strftime('%H:%M:%S')} ===")
print(f"成功: {success}, 跳过: {skipped}, 失败: {len(failed)}")
