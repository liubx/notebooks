#!/usr/bin/env python3
"""获取 access token 用于 curl 下载"""
import subprocess, json

r = subprocess.run(
    ["lark-cli", "api", "GET", "/open-apis/drive/explorer/v2/root_folder/meta", "--dry-run", "--as", "user"],
    capture_output=True, text=True, timeout=10
)
print("DRY-RUN stdout:", r.stdout[:300])

# 尝试从 locks 目录找 token
import os, glob
locks_dir = os.path.expanduser("~/.lark-cli/locks")
if os.path.exists(locks_dir):
    for f in os.listdir(locks_dir):
        print(f"lock file: {f}")
        fp = os.path.join(locks_dir, f)
        with open(fp) as fh:
            print(f"  content: {fh.read()[:200]}")
