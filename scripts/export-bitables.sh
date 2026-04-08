#!/bin/bash
# 飞书 bitable 多维表格批量导出

export_bitable() {
  local token="$1" title="$2" target_dir="$3"
  
  if [ -f "$target_dir/${title}.md" ]; then
    echo "⏭️  跳过(已存在): $title"
    return 0
  fi
  
  echo "📋 导出: $title ($token)"
  mkdir -p "$target_dir"
  
  # 1. 获取表列表
  local tables_result
  tables_result=$(lark-cli base +table-list --base-token "$token" --as user 2>&1)
  local tables_ok=$(echo "$tables_result" | python3 -c "import sys,json; d=json.load(sys.stdin); print(d.get('ok',''))" 2>/dev/null)
  
  if [ "$tables_ok" != "True" ]; then
    echo "  ❌ 获取表列表失败"
    return 1
  fi
  
  # 2. 用 python 处理导出
  python3 -u << PYEOF
import json, subprocess, sys, time

token = "$token"
title = "$title"
target_dir = "$target_dir"

# 获取表列表
result = subprocess.run(
    ["lark-cli", "base", "+table-list", "--base-token", token, "--as", "user"],
    capture_output=True, text=True, timeout=30
)
data = json.loads(result.stdout)
if not data.get("ok"):
    print("  ❌ 获取表列表失败")
    sys.exit(1)

tables = data.get("data", {}).get("items", [])
if not tables:
    print("  ⚠️ 没有数据表")
    sys.exit(0)

md_content = f"""---
title: "{title}"
source: feishu
feishu_token: "{token}"
feishu_type: bitable
feishu_url: "https://reliablesense.feishu.cn/base/{token}"
export_method: base-record-list
migrated: 2026-04-05
tags:
  - feishu-migration
---

# {title}

"""

for table in tables:
    table_id = table.get("table_id", "")
    table_name = table.get("name", "未命名")
    
    md_content += f"## {table_name}\n\n"
    
    # 获取字段
    try:
        field_result = subprocess.run(
            ["lark-cli", "base", "+field-list", "--base-token", token, "--table-id", table_id, "--as", "user"],
            capture_output=True, text=True, timeout=30
        )
        field_data = json.loads(field_result.stdout)
        fields = field_data.get("data", {}).get("items", [])
    except:
        fields = []
    
    if not fields:
        md_content += "（无字段信息）\n\n"
        continue
    
    field_names = [f.get("field_name", "?") for f in fields]
    
    # 获取记录（最多 100 条）
    try:
        record_result = subprocess.run(
            ["lark-cli", "base", "+record-list", "--base-token", token, "--table-id", table_id, "--limit", "100", "--as", "user"],
            capture_output=True, text=True, timeout=60
        )
        record_data = json.loads(record_result.stdout)
        records = record_data.get("data", {}).get("items", [])
        total = record_data.get("data", {}).get("total", 0)
    except:
        records = []
        total = 0
    
    # 生成 Markdown 表格
    header = "| " + " | ".join(field_names) + " |"
    separator = "| " + " | ".join(["---"] * len(field_names)) + " |"
    md_content += header + "\n" + separator + "\n"
    
    for record in records:
        fields_data = record.get("fields", {})
        row = []
        for fname in field_names:
            val = fields_data.get(fname, "")
            if isinstance(val, list):
                # 处理数组类型（人员、多选等）
                parts = []
                for item in val:
                    if isinstance(item, dict):
                        parts.append(item.get("text", item.get("name", str(item))))
                    else:
                        parts.append(str(item))
                val = ", ".join(parts)
            elif isinstance(val, dict):
                val = val.get("text", val.get("name", str(val)))
            val = str(val).replace("|", "\\|").replace("\n", " ")
            if len(val) > 100:
                val = val[:97] + "..."
            row.append(val)
        md_content += "| " + " | ".join(row) + " |\n"
    
    if total > 100:
        md_content += f"\n> 共 {total} 条记录，仅显示前 100 条\n"
    
    md_content += "\n"
    time.sleep(0.5)

with open(f"{target_dir}/{title}.md", "w") as f:
    f.write(md_content)

print(f"  ✅ {title} ({len(tables)} 个表)")
PYEOF
}

echo "=== 开始导出 bitable $(date) ==="

# 根目录
export_bitable "NbIPbswwSaCfPpsWak7cbCHsnwe" "广州机场综合定位" "4-Archives/Notes/Feishu/云空间/根目录"
export_bitable "NepGb0sWdaPfnosidcMc7yspnFg" "周报测试" "4-Archives/Notes/Feishu/云空间/根目录"

# 王宗光
export_bitable "RIHubtFOhadg4TsFWJoch9iEnuh" "工作周报" "4-Archives/Notes/Feishu/云空间/王宗光"
export_bitable "ZQj0bMC5eaghvxsBxzGcBWDznUc" "会议签到表" "4-Archives/Notes/Feishu/云空间/王宗光"

# 陈子杰
export_bitable "ZmmjbljSpa3KWBskm40cPgWGnPg" "需求及Bug管理-1" "4-Archives/Notes/Feishu/云空间/陈子杰"
export_bitable "BSDnb80vUaGm4hsjM06cIE0bncD" "需求及Bug管理-2" "4-Archives/Notes/Feishu/云空间/陈子杰"
export_bitable "RLRqbFnrPaokuRsVtTbcjkMLnZd" "移动终端目前缺失功能" "4-Archives/Notes/Feishu/云空间/陈子杰/广州机场-移动应用平台"

# 莱讯科技
export_bitable "bascncveOYEhfjbtaaj3U6Rgete" "客户关系管理" "4-Archives/Notes/Feishu/云空间/莱讯科技/销售管理"
export_bitable "bascnemc8tozwPeCvL2GmUfG9Tg" "合同订单管理" "4-Archives/Notes/Feishu/云空间/莱讯科技/公司内部资料"
export_bitable "bascnm0yQj7bRGrIZE1vSUXMOGg" "任务管理" "4-Archives/Notes/Feishu/云空间/莱讯科技/公司内部资料"
export_bitable "bascn8p8PpJEyLNk6UovDb1V6Of" "项目管理-bitable" "4-Archives/Notes/Feishu/云空间/莱讯科技/项目资料管理/广州机场"

# 知识库
export_bitable "PF71bTA9Yaqo3yscmxlcsdsnnVU" "库房管理" "4-Archives/Notes/Feishu/知识库/受限知识库"
export_bitable "A9NpbHhPgafD4osRWROcWPydnse" "机场任务管理" "4-Archives/Notes/Feishu/知识库/受限知识库"

echo ""
echo "=== bitable 导出完成 $(date) ==="
