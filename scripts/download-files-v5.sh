#!/bin/bash
# 批量下载 file 附件 v5
# 用 bash 后台进程 + kill -9 做超时控制

FEISHU_DIR="4-Archives/Notes/Feishu"
TSV="1-Projects/Personal/笔记迁移/飞书完整文件清单.tsv"
TIMEOUT=15
SKIP_EXT="zip|rar|7z|tar|gz|tgz|mp4|mov|mkv|avi|wmv|flv|mp3|wav|iso|apk|exe|msi|dmg|dwg|bak|ai|psd"

success=0
fail=0
skip=0
total=0

download_with_timeout() {
    local token="$1"
    local outpath="$2"
    
    lark-cli drive +download --file-token "$token" --output "$outpath" --as user > /dev/null 2>&1 &
    local pid=$!
    
    local elapsed=0
    while kill -0 $pid 2>/dev/null; do
        sleep 1
        elapsed=$((elapsed + 1))
        if [ $elapsed -ge $TIMEOUT ]; then
            kill -9 $pid 2>/dev/null
            wait $pid 2>/dev/null
            [ -f "$outpath" ] && rm -f "$outpath"
            return 1
        fi
    done
    wait $pid
    [ -f "$outpath" ] && [ -s "$outpath" ] && return 0
    [ -f "$outpath" ] && rm -f "$outpath"
    return 1
}

echo "=== 开始下载 $(date +%H:%M:%S) ==="

while IFS=$'\t' read -r path ftype token name; do
    [ "$ftype" != "file" ] && continue
    total=$((total + 1))
    
    # 跳过大文件扩展名
    ext="${name##*.}"
    ext=$(echo "$ext" | tr '[:upper:]' '[:lower:]')
    if echo "$ext" | grep -qE "^($SKIP_EXT)$"; then
        skip=$((skip + 1))
        continue
    fi
    
    # 构建目标路径
    dir="$FEISHU_DIR/$(dirname "$path")"
    outpath="$dir/$name"
    
    # 跳过已存在
    if [ -f "$outpath" ]; then
        skip=$((skip + 1))
        continue
    fi
    
    mkdir -p "$dir"
    
    if download_with_timeout "$token" "$outpath"; then
        success=$((success + 1))
    else
        fail=$((fail + 1))
    fi
    
    count=$((success + fail + skip))
    if [ $((count % 100)) -eq 0 ]; then
        echo "[$count/$total] ok=$success fail=$fail skip=$skip"
    fi
done < <(tail -n +2 "$TSV")

echo ""
echo "=== 完成 $(date +%H:%M:%S) ==="
echo "成功: $success, 失败: $fail, 跳过: $skip"
