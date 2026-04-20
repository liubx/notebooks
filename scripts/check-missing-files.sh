#!/bin/bash
# 检查飞书迁移文件是否真正缺失
# 对比 TSV 清单和 4-Archives/Notes/Feishu/ 目录

TSV="1-Projects/Personal/笔记迁移/飞书文件清单与迁移状态.tsv"
BASE="4-Archives/Notes/Feishu"
MISSING_FILE="/tmp/feishu-missing.txt"
> "$MISSING_FILE"

missing=0
checked=0
found=0

while IFS=$'\t' read -r path type token title status rest; do
    # 跳过表头和非已迁移的
    [[ "$status" != *"✅"* ]] && continue
    # 跳过 macOS 隐藏文件
    [[ "$title" == ._* ]] && continue
    [[ "$title" == .DS_Store ]] && continue
    
    checked=$((checked + 1))
    
    # 构建本地路径
    local_dir="$BASE/$path"
    local_base=$(dirname "$local_dir")
    local_name=$(basename "$local_dir")
    
    # 根据类型确定扩展名
    case "$type" in
        docx)
            # docx 转 md
            candidates=("$local_dir.md" "$BASE/${path}.md")
            ;;
        doc)
            # doc 导出 pandoc 转 md
            candidates=("$local_dir.md" "$BASE/${path}.md")
            ;;
        file)
            # 直接下载，文件名已含扩展名
            candidates=("$BASE/$path")
            ;;
        sheet)
            # xlsx 导出
            candidates=("$local_dir.xlsx" "$BASE/${path}.xlsx")
            ;;
        bitable)
            # xlsx 导出
            candidates=("$local_dir.xlsx" "$BASE/${path}.xlsx")
            ;;
        mindnote)
            # mm 导出
            candidates=("$local_dir.mm" "$BASE/${path}.mm")
            ;;
        slides)
            # pptx 导出
            candidates=("$local_dir.pptx" "$BASE/${path}.pptx")
            ;;
        shortcut)
            continue
            ;;
        *)
            candidates=("$BASE/$path")
            ;;
    esac
    
    # 检查是否存在
    file_found=false
    for candidate in "${candidates[@]}"; do
        if [[ -e "$candidate" ]]; then
            file_found=true
            break
        fi
    done
    
    # 如果没找到，尝试模糊匹配（目录存在但文件名略有不同）
    if ! $file_found; then
        dir_to_check=$(dirname "${candidates[0]}")
        if [[ -d "$dir_to_check" ]]; then
            # 尝试用 find 在目录中搜索包含 token 的文件
            if find "$dir_to_check" -maxdepth 1 -name "*${token}*" 2>/dev/null | grep -q .; then
                file_found=true
            fi
            # 尝试搜索文件名（去掉特殊字符）
            clean_name=$(echo "$local_name" | sed 's/[()（）]//g' | head -c 10)
            if [[ -n "$clean_name" ]] && find "$dir_to_check" -maxdepth 1 -name "*${clean_name}*" 2>/dev/null | grep -q .; then
                file_found=true
            fi
        fi
    fi
    
    if $file_found; then
        found=$((found + 1))
    else
        missing=$((missing + 1))
        echo -e "${type}\t${path}\t${title}" >> "$MISSING_FILE"
    fi
done < "$TSV"

echo "=== 检查完成 ==="
echo "已检查: $checked"
echo "已找到: $found"
echo "缺失: $missing"
echo ""
echo "=== 缺失文件（按类型统计）==="
cut -f1 "$MISSING_FILE" | sort | uniq -c | sort -rn
echo ""
echo "=== 缺失文件列表（排除 file 类型中的隐藏文件）==="
grep -v '^\._' "$MISSING_FILE" | head -50
