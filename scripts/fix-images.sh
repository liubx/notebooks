#!/bin/bash
# 补已迁移 docx 文档的图片
# 扫描所有已迁移文档，重新 fetch 提取图片，下载并更新 Markdown

echo "=== 开始补图片 $(date) ==="

find "4-Archives/Notes/Feishu" -name "*.md" ! -name "链接索引*" ! -name "README*" | while read filepath; do
  # 提取 token 和 type
  token=$(grep 'feishu_token' "$filepath" | head -1 | sed 's/.*"\(.*\)".*/\1/')
  ftype=$(grep 'feishu_type' "$filepath" | head -1 | sed 's/.*: *//' | tr -d '"' | tr -d ' ')
  
  # 只处理 docx 类型（doc 已通过 pandoc 处理了图片）
  if [ "$ftype" != "docx" ] || [ -z "$token" ]; then
    continue
  fi
  
  # fetch 文档
  result=$(lark-cli docs +fetch --doc "$token" --as user 2>&1)
  
  # 提取图片 token
  img_tokens=$(echo "$result" | python3 -c "
import sys,json,re
try:
    d=json.load(sys.stdin)
    md=d.get('data',{}).get('markdown','')
    imgs=re.findall(r'<image token=\"([^\"]+)\"', md)
    if imgs:
        print('\n'.join(imgs))
except: pass
" 2>/dev/null)
  
  if [ -z "$img_tokens" ]; then
    continue
  fi
  
  # 有图片，处理
  dir=$(dirname "$filepath")
  img_dir="$dir/Attachments"
  mkdir -p "$img_dir"
  
  title=$(basename "$filepath" .md)
  img_count=$(echo "$img_tokens" | wc -l | tr -d ' ')
  echo "📷 $title ($img_count 张图片)"
  
  # 下载每张图片
  downloaded=0
  while IFS= read -r img_token; do
    if [ -z "$img_token" ]; then continue; fi
    
    # 检查是否已下载
    existing=$(find "$img_dir" -name "${img_token}.*" 2>/dev/null | head -1)
    if [ -n "$existing" ]; then
      continue
    fi
    
    dl_result=$(lark-cli docs +media-download --token "$img_token" --output "$img_dir/$img_token" --as user 2>&1)
    saved=$(echo "$dl_result" | python3 -c "import sys,json; print(json.load(sys.stdin).get('data',{}).get('saved_path',''))" 2>/dev/null)
    
    if [ -n "$saved" ]; then
      downloaded=$((downloaded + 1))
    fi
  done <<< "$img_tokens"
  
  if [ "$downloaded" -eq 0 ] && [ -z "$(find "$img_dir" -name "*.png" -o -name "*.jpg" -o -name "*.gif" 2>/dev/null | head -1)" ]; then
    continue
  fi
  
  # 更新 Markdown：重新获取完整内容并替换图片标签
  python3 << PYEOF
import json, re, os, sys

# 重新读取 fetch 结果
result_str = '''$(echo "$result" | python3 -c "import sys; print(sys.stdin.read())" 2>/dev/null)'''

try:
    d = json.loads(result_str)
    md = d.get('data', {}).get('markdown', '')
except:
    sys.exit(0)

if not md:
    sys.exit(0)

# 读取现有文件的 frontmatter
with open("$filepath") as f:
    old_content = f.read()

# 提取 frontmatter
fm_match = re.match(r'(---\n.*?\n---\n)', old_content, re.DOTALL)
if not fm_match:
    sys.exit(0)

frontmatter = fm_match.group(1)

# 替换图片标签
def replace_image(match):
    full = match.group(0)
    token_match = re.search(r'token="([^"]+)"', full)
    if not token_match:
        return full
    token = token_match.group(1)
    # 查找下载的文件
    img_dir = "$img_dir"
    for ext in ['png', 'jpg', 'jpeg', 'gif', 'webp']:
        path = os.path.join(img_dir, f"{token}.{ext}")
        if os.path.exists(path):
            return f"![](Attachments/{token}.{ext})"
    return full

new_md = re.sub(r'<image[^/]*/>', replace_image, md)

# 写回文件
with open("$filepath", 'w') as f:
    f.write(frontmatter + '\n' + new_md)

print(f"  ✅ 更新完成 ({downloaded} 张新下载)")
PYEOF

  sleep 0.3
done

echo ""
echo "=== 补图片完成 $(date) ==="
