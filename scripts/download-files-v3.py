#!/usr/bin/env python3
"""
批量下载 file 附件 v3
用 lark-cli api GET 直接下载，不用 drive +download（会挂起）
"""
import subprocess, json, os, re, time

FEISHU_DIR = "4-Archives/Notes/Feishu"
TSV = "1-Projects/Personal/笔记迁移/飞书完整文件清单.tsv"
FAILED_LOG = "/tmp/file-download-failed.tsv"

SKIP_EXT = {
    "zip", "rar", "7z", "tar", "gz", "tgz",
    "mp4", "mov", "mkv", "avi", "wmv", "flv", "mp3", "wav",
    "iso", "apk", "exe", "msi", "dmg",
    "dwg", "bak", "ai", "psd",
}

def download(token, filename, target_dir):
    path = os.path.join(target_dir, filename)
    if os.path.exists(path):
        return "skip"
    os.makedirs(target_dir, exist_ok=True)
    try:
        proc = subprocess.Popen(
            ["timeout", "15", "lark-cli", "api", "GET",
             f"/open-apis/drive/v1/files/{token}/download",
             "--output", path, "--as", "user"],
            stdout=subprocess.PIPE, stderr=subprocess.PIPE
        )
        proc.communicate(timeout=20)
        if os.path.exists(path) and os.path.getsize(path) > 0:
            return "ok"
        if os.path.exists(path):
            os.remove(path)
        return "fail"
    except subprocess.TimeoutExpired:
        proc.kill()
        proc.wait()
        if os.path.exists(path):
            try: os.remove(path)
            except: pass
        return "timeout"
    except:
        return "error"

# 读取清单
with open(TSV) as f:
    lines = f.readlines()[1:]

small_files = []
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
            small_files.append((token, name, target_dir, path))

# 统计已下载
already = sum(1 for t, n, d, p in small_files if os.path.exists(os.path.join(d, n)))
print(f"小文件: {len(small_files)} (已下载 {already})")
print(f"大文件(跳过): {len(big_files)}")
print()

success = 0
skipped = 0
failed = []

for i, (token, name, target_dir, feishu_path) in enumerate(small_files):
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
    
    if (i + 1) % 100 == 0:
        print(f"[{i+1}/{len(small_files)}] {success} ok, {len(failed)} fail, {skipped} skip")
    
    time.sleep(0.05)

# 保存清单
with open(FAILED_LOG, "w") as f:
    f.write("Token\t文件名\t飞书路径\t原因\n")
    for token, name, path, reason in failed:
        f.write(f"{token}\t{name}\t{path}\t{reason}\n")
    for token, name, target_dir, path in big_files:
        if not os.path.exists(os.path.join(target_dir, name)):
            f.write(f"{token}\t{name}\t{path}\tskip_big\n")

print(f"\n=== 完成 {time.strftime('%H:%M:%S')} ===")
print(f"成功: {success}, 跳过: {skipped}, 失败: {len(failed)}")
print(f"大文件跳过: {len(big_files)}")
