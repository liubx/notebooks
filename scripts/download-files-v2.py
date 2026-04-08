#!/usr/bin/env python3
"""
批量下载 file 附件 v2
- 先下载小文件（docx/xlsx/pdf/txt/csv/md/json/yaml/doc/xls/pptx）
- 跳过大文件扩展名（zip/rar/7z/mp4/mov/mkv/iso/apk/exe/tar/gz/mp3/wav/dwg/bak）
- 用 signal 做超时控制
"""
import subprocess, json, os, re, time, signal

FEISHU_DIR = "4-Archives/Notes/Feishu"
TSV = "1-Projects/Personal/笔记迁移/飞书完整文件清单.tsv"
FAILED_LOG = "/tmp/file-download-failed.tsv"

SKIP_EXT = {
    "zip", "rar", "7z", "tar", "gz", "tgz",
    "mp4", "mov", "mkv", "avi", "wmv", "flv", "mp3", "wav",
    "iso", "apk", "exe", "msi", "dmg",
    "dwg", "bak", "ai", "psd",
}

class TimeoutError(Exception):
    pass

def timeout_handler(signum, frame):
    raise TimeoutError()

def download(token, filename, target_dir):
    path = os.path.join(target_dir, filename)
    if os.path.exists(path):
        return "skip"
    os.makedirs(target_dir, exist_ok=True)
    
    signal.signal(signal.SIGALRM, timeout_handler)
    signal.alarm(20)  # 20 秒超时
    try:
        r = subprocess.run(
            ["lark-cli", "drive", "+download", "--file-token", token,
             "--output", path, "--as", "user"],
            capture_output=True, text=True, timeout=20
        )
        signal.alarm(0)
        if os.path.exists(path):
            return "ok"
        return "fail"
    except (subprocess.TimeoutExpired, TimeoutError):
        signal.alarm(0)
        # 清理可能的部分下载文件
        if os.path.exists(path):
            try:
                os.remove(path)
            except:
                pass
        return "timeout"
    except:
        signal.alarm(0)
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

print(f"小文件(可下载): {len(small_files)}")
print(f"大文件(跳过): {len(big_files)}")
print()

# 下载小文件
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
        print(f"[{i+1}/{len(small_files)}] {success} 成功, {len(failed)} 失败, {skipped} 跳过")
    
    time.sleep(0.1)

# 保存失败 + 大文件清单
with open(FAILED_LOG, "w") as f:
    f.write("Token\t文件名\t飞书路径\t原因\n")
    for token, name, path, reason in failed:
        f.write(f"{token}\t{name}\t{path}\t{reason}\n")
    for token, name, target_dir, path in big_files:
        if not os.path.exists(os.path.join(target_dir, name)):
            f.write(f"{token}\t{name}\t{path}\tskip_big\n")

print(f"\n=== 完成 {time.strftime('%H:%M:%S')} ===")
print(f"小文件: {success} 成功, {skipped} 跳过, {len(failed)} 失败")
print(f"大文件: {len(big_files)} 个跳过")
print(f"清单已保存到 {FAILED_LOG}")
