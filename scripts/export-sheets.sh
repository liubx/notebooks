#!/bin/bash
# 飞书 sheet 电子表格批量导出

export_sheet() {
  local token="$1" title="$2" target_dir="$3"
  
  if [ -f "$target_dir/${title}.xlsx" ]; then
    echo "⏭️  跳过(已存在): $title"
    return 0
  fi
  
  echo "📊 导出: $title ($token)"
  mkdir -p "$target_dir"
  
  lark-cli sheets +export \
    --spreadsheet-token "$token" \
    --file-extension xlsx \
    --output-path "$target_dir/${title}.xlsx" \
    --as user > /dev/null 2>&1
  
  if [ -f "$target_dir/${title}.xlsx" ]; then
    echo "  ✅ $title"
  else
    echo "  ❌ 导出失败: $title"
  fi
}

echo "=== 开始导出 sheet $(date) ==="

# 根目录
export_sheet "HQsEseKUKhovu0t1ewnclLSAnte" "员工花名册-在职" "4-Archives/Notes/Feishu/云空间/根目录"
export_sheet "W95RsJ1SahTaeJt0xDgcM4d6n7f" "定位对象在线时长导出表" "4-Archives/Notes/Feishu/云空间/根目录"
export_sheet "shtcnuIgoeyPvXu60pwR4XsEc1g" "红柳林筛分楼部署内容" "4-Archives/Notes/Feishu/云空间/根目录"

# 王宗光
export_sheet "shtcniz2m6u89tCpHodDRbIhDxd" "远端接口新需求问题反馈" "4-Archives/Notes/Feishu/云空间/王宗光"

# 陈子杰
export_sheet "GBc0sFzfKhEtBztmsAPcp5m5n4w" "oemusers" "4-Archives/Notes/Feishu/云空间/陈子杰"
export_sheet "ILedsU7eShMXojtZmy0cTiHln9c" "问题记录-2023-09-22" "4-Archives/Notes/Feishu/云空间/陈子杰"
export_sheet "Xl6HsOeCMhUrDwtMewMcElDGnyd" "室内定位系统工作进度" "4-Archives/Notes/Feishu/云空间/陈子杰"
export_sheet "EKkcsQr7MhV8S7teOsTcf1ISnUc" "t_poi_type" "4-Archives/Notes/Feishu/云空间/陈子杰"

# 莱讯科技 > 项目资料管理
export_sheet "shtcnUlsqXQO5eCWs8r988gphad" "项目管理" "4-Archives/Notes/Feishu/云空间/莱讯科技/项目资料管理/广州机场"

# 知识库
export_sheet "Pn2Rs9RZvhM3jYtYnJoc6cJQnQd" "项目甘特图" "4-Archives/Notes/Feishu/知识库/项目管理"
export_sheet "Obrtsq2GnhTDubtEQaucpakonZf" "费用报销单" "4-Archives/Notes/Feishu/知识库/个人知识库"
export_sheet "LnobsSBlyhcyZutJ9uDcd7RQnzg" "综合定位平台开发进度" "4-Archives/Notes/Feishu/知识库/受限知识库"

echo ""
echo "=== sheet 导出完成 $(date) ==="
