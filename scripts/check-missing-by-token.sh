#!/bin/bash
# 用 token 精确检查飞书迁移文件是否真正缺失
# 对于之前报告缺失的文件，在整个归档目录中搜索 token

BASE="4-Archives/Notes/Feishu"
MISSING_INPUT="/tmp/feishu-missing.txt"
REAL_MISSING="/tmp/feishu-real-missing.txt"
FALSE_POSITIVE="/tmp/feishu-false-positive.txt"
> "$REAL_MISSING"
> "$FALSE_POSITIVE"

real_missing=0
false_positive=0
total=0

# 先建立本地文件名索引（加速搜索）
echo "正在建立本地文件索引..."
find "$BASE" -type f -not -name '.DS_Store' -not -name '._*' > /tmp/feishu-local-files.txt
local_count=$(wc -l < /tmp/feishu-local-files.txt)
echo "本地文件数: $local_count"
echo ""

while IFS=$'\t' read -r type path title; do
    total=$((total + 1))
    token_from_tsv=""
    
    # 从原始 TSV 中获取 token
    token_from_tsv=$(grep -F "$path" "1-Projects/Personal/笔记迁移/飞书文件清单与迁移状态.tsv" | head -1 | cut -f3)
    
    found=false
    
    # 方法1：用 token 在本地文件中搜索
    if [[ -n "$token_from_tsv" ]]; then
        if grep -q "$token_from_tsv" /tmp/feishu-local-files.txt 2>/dev/null; then
            found=true
        fi
    fi
    
    # 方法2：如果 token 没找到，尝试在 README.md 中搜索 token
    if ! $found && [[ -n "$token_from_tsv" ]]; then
        dir_to_check="$BASE/$(dirname "$path")"
        if [[ -f "$dir_to_check/README.md" ]]; then
            if grep -q "$token_from_tsv" "$dir_to_check/README.md" 2>/dev/null; then
                # token 在 README 中记录了，说明文件是通过其他方式处理的（如同一文档的副本）
                found=true
            fi
        fi
    fi
    
    # 方法3：对于 docx 类型，文件名可能有空格差异，用去空格后的名字搜索
    if ! $found && [[ "$type" == "docx" || "$type" == "doc" ]]; then
        clean_title=$(echo "$title" | tr -d ' ')
        if [[ -n "$clean_title" ]] && grep -q "$clean_title" /tmp/feishu-local-files.txt 2>/dev/null; then
            found=true
        fi
    fi
    
    if $found; then
        false_positive=$((false_positive + 1))
        echo -e "$type\t$path\t$title" >> "$FALSE_POSITIVE"
    else
        real_missing=$((real_missing + 1))
        echo -e "$type\t$path\t$title" >> "$REAL_MISSING"
    fi
done < "$MISSING_INPUT"

echo "=== Token 精确检查完成 ==="
echo "之前报告缺失: $total"
echo "误报（实际存在）: $false_positive"
echo "真正缺失: $real_missing"
echo ""

if [[ $real_missing -gt 0 ]]; then
    echo "=== 真正缺失的文件 ==="
    echo ""
    echo "类型 | 路径 | 标题"
    echo "--- | --- | ---"
    cat "$REAL_MISSING"
fi
