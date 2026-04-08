#!/usr/bin/env python3
"""
批量扫描已迁移文档，重新 fetch 获取完整内容（含图片标签），
下载缺失的图片，更新 Markdown 中的图片引用。
"""
import subprocess
import json
import re
import os
import sys
import time

FEISHU_DIR = "4-Archives/Notes/Feishu"

def fetch_doc(token):
    """fetch 文档内容"""
    try:
        result = subprocess.run(
            ["lark-cli", "docs", "+fetch", "--doc", token, "--as", "user"],
            capture_output=True, text=True, timeout=30
        )
        data = json.loads(result.stdout)
        if data.get("ok"):
            return data.get("data", {})
    except:
        pass
    return None

def download_image(img_token, output_dir):
    """下载图片，返回保存的文件名"""
    # 检查是否已存在
    for ext in ["png", "jpg", "jpeg", "gif", "webp"]:
        if os.path.exists(os.path.join(output_dir, f"{img_token}.{ext}")):
            return f"{img_token}.{ext}"
    
    try:
        result = subprocess.run(
            ["lark-cli", "docs", "+media-download", "--token", img_token,
             "--output", os.path.join(output_dir, img_token), "--as", "user"],
            capture_output=True, text=True, timeout=30
        )
        data = json.loads(result.stdout)
        if data.get("ok"):
            saved = data["data"]["saved_path"]
            return os.path.basename(saved)
    except:
        pass
    return None

def process_file(filepath):
    """处理单个文件"""
    with open(filepath, "r") as f:
        content = f.read()
    
    # 提取 frontmatter
    fm_match = re.match(r"(---\n.*?\n---\n)", content, re.DOTALL)
    if not fm_match:
        return False
    
    # 提取 token 和 type
    token_match = re.search(r'feishu_token:\s*"([^"]+)"', content)
    type_match = re.search(r'feishu_type:\s*(\S+)', content)
    if not token_match or not type_match:
        return False
    
    token = token_match.group(1)
    ftype = type_match.group(1).strip('"')
    
    if ftype != "docx":
        return False
    
    # fetch 文档
    doc_data = fetch_doc(token)
    if not doc_data:
        return False
    
    markdown = doc_data.get("markdown", "")
    img_tokens = re.findall(r'<image token="([^"]+)"', markdown)
    
    if not img_tokens:
        return False
    
    # 下载图片
    file_dir = os.path.dirname(filepath)
    att_dir = os.path.join(file_dir, "Attachments")
    os.makedirs(att_dir, exist_ok=True)
    
    title = os.path.basename(filepath).replace(".md", "")
    downloaded = 0
    img_map = {}  # token -> filename
    
    for img_token in img_tokens:
        filename = download_image(img_token, att_dir)
        if filename:
            img_map[img_token] = filename
            downloaded += 1
    
    if not img_map:
        return False
    
    # 替换图片标签
    def replace_image(match):
        full = match.group(0)
        t = re.search(r'token="([^"]+)"', full)
        if t and t.group(1) in img_map:
            return f"![](Attachments/{img_map[t.group(1)]})"
        return full
    
    new_markdown = re.sub(r'<image[^>]*/>', replace_image, markdown)
    
    # 保留原 frontmatter，替换正文
    frontmatter = fm_match.group(1)
    with open(filepath, "w") as f:
        f.write(frontmatter + "\n" + new_markdown)
    
    print(f"  ✅ {title} ({len(img_tokens)} 张图片, {downloaded} 张下载)")
    return True

def main():
    print(f"=== 开始更新图片引用 {time.strftime('%H:%M:%S')} ===")
    
    processed = 0
    total_images = 0
    
    for root, dirs, files in os.walk(FEISHU_DIR):
        for fname in files:
            if not fname.endswith(".md"):
                continue
            if fname.startswith("链接索引") or fname == "README.md":
                continue
            
            filepath = os.path.join(root, fname)
            
            with open(filepath) as f:
                content = f.read()
            
            if 'feishu_type: docx' not in content and 'feishu_type: "docx"' not in content:
                continue
            
            token_match = re.search(r'feishu_token:\s*"([^"]+)"', content)
            if not token_match:
                continue
            
            token = token_match.group(1)
            title = fname.replace(".md", "")
            
            # fetch 检查是否有图片
            doc_data = fetch_doc(token)
            if not doc_data:
                continue
            
            markdown = doc_data.get("markdown", "")
            img_tokens = re.findall(r'<image token="([^"]+)"', markdown)
            
            if not img_tokens:
                continue
            
            print(f"📷 {title} ({len(img_tokens)} 张图片)")
            
            # 下载图片
            file_dir = os.path.dirname(filepath)
            att_dir = os.path.join(file_dir, "Attachments")
            os.makedirs(att_dir, exist_ok=True)
            
            img_map = {}
            for img_token in img_tokens:
                filename = download_image(img_token, att_dir)
                if filename:
                    img_map[img_token] = filename
                time.sleep(0.1)
            
            if not img_map:
                print(f"  ⚠️ 图片下载失败")
                continue
            
            # 替换图片标签
            def replace_image(match):
                full = match.group(0)
                t = re.search(r'token="([^"]+)"', full)
                if t and t.group(1) in img_map:
                    return f"![](Attachments/{img_map[t.group(1)]})"
                return full
            
            new_markdown = re.sub(r'<image[^>]*/>', replace_image, markdown)
            
            # 保留原 frontmatter，替换正文
            fm_match = re.match(r"(---\n.*?\n---\n)", content, re.DOTALL)
            if fm_match:
                with open(filepath, "w") as f:
                    f.write(fm_match.group(1) + "\n" + new_markdown)
            
            processed += 1
            total_images += len(img_tokens)
            print(f"  ✅ 更新完成 ({len(img_map)}/{len(img_tokens)} 张)")
            
            time.sleep(0.2)
    
    print(f"\n=== 完成 {time.strftime('%H:%M:%S')} ===")
    print(f"处理了 {processed} 个文档，共 {total_images} 张图片")

if __name__ == "__main__":
    main()
