#!/usr/bin/env python3
"""批量下载所有 file 类型附件，超时自动跳过并记录"""
import subprocess, json, os, re, time

FEISHU_DIR = "4-Archives/Notes/Feishu"
TSV = "1-Projects/Personal/笔记迁移/飞书完整文件清单.tsv"
FAILED_LOG = "/tmp/file-download-failed.tsv"

def safe_name(name):
    return re.sub(r'[/\\:*?"<>|]', '-', name)

def download(token, filename, target_dir, timeout=30):
    path = os.path.join(target_dir, filename)
    if os.path.exists(path):
        return "skip"
    os.makedirs(target_dir, exist_ok=True)
    try:
        r = subprocess.run(
            ["lark-cli", "drive", "+download", "--file-token", token,
             "--output", path, "--as", "user"],
            capture_output=True, text=True, timeout=timeout
        )
        if os.path.exists(path):
            return "ok"
        return "fail"
    except subprocess.TimeoutExpired:
        return "timeout"
    except:
        return "error"

# 读取清单
with open(TSV) as f:
    lines = f.readlines()[1:]

files_to_download = []
for line in lines:
    parts = line.strip().split("\t")
    if len(parts) >= 4 and parts[1] == "file":
        path, token, name = parts[0], parts[2], parts[3]
        target_dir = os.path.join(FEISHU_DIR, os.path.dirname(path))
        files_to_download.append((token, name, target_dir, path))

print(f"file 附件总数: {len(files_to_download)}")

# 先统计已下载的
already = 0
for token, name, target_dir, path in files_to_download:
    if os.path.exists(os.path.join(target_dir, name)):
        already += 1

print(f"已下载: {already}")
print(f"待下载: {len(files_to_download) - already}")
print()

# 批量下载
success = 0
skipped = 0
failed = []
total = len(files_to_download)

for i, (token, name, target_dir, feishu_path) in enumerate(files_to_download):
    if os.path.exists(os.path.join(target_dir, name)):
        skipped += 1
        continue
    
    # 根据扩展名决定超时时间
    ext = name.rsplit(".", 1)[-1].lower() if "." in name else ""
    if ext in ("zip", "rar", "7z", "mp4", "mov", "mkv", "avi", "iso", "apk", "exe", "tar", "gz"):
        timeout = 60  # 大文件给 60 秒
    else:
        timeout = 30
    
    if (i + 1) % 50 == 0 or i == 0:
        print(f"[{i+1}/{total}] 进度: {success} 成功, {len(failed)} 失败, {skipped} 跳过")
    
    result = download(token, name, target_dir, timeout)
    
    if result == "ok":
        success += 1
    elif result == "skip":
        skipped += 1
    else:
        failed.append((token, name, feishu_path, result))
        if len(failed) <= 20:  # 只打印前 20 个失败
            print(f"  ❌ {name} ({result})")
    
    time.sleep(0.1)

# 保存失败清单
with open(FAILED_LOG, "w") as f:
    f.write("Token\t文件名\t飞书路径\t原因\n")
    for token, name, path, reason in failed:
        f.write(f"{token}\t{name}\t{path}\t{reason}\n")

print(f"\n=== 完成 {time.strftime('%H:%M:%S')} ===")
print(f"成功: {success}")
print(f"跳过(已存在): {skipped}")
print(f"失败: {len(failed)}")
if failed:
    print(f"失败清单已保存到 {FAILED_LOG}")
