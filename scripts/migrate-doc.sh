#!/bin/bash
# 飞书 doc 旧版文档批量迁移
# 用法: bash scripts/migrate-doc.sh

process_doc() {
  local token="$1"
  local title="$2"
  local target_dir="$3"
  
  # 检查是否已存在
  if [ -f "$target_dir/${title}.md" ]; then
    echo "⏭️  跳过(已存在): $title"
    return 0
  fi
  
  echo "📄 处理: $title ($token)"
  
  # 1. 创建导出任务
  local export_result
  export_result=$(lark-cli api POST /open-apis/drive/v1/export_tasks \
    --data "{\"file_extension\":\"docx\",\"token\":\"$token\",\"type\":\"doc\"}" \
    --as user 2>&1)
  
  local ticket
  ticket=$(echo "$export_result" | python3 -c "import sys,json; print(json.load(sys.stdin).get('data',{}).get('ticket',''))" 2>/dev/null)
  
  if [ -z "$ticket" ]; then
    echo "  ❌ 导出任务创建失败"
    return 1
  fi
  
  # 2. 等待并查询结果
  sleep 3
  local query_result
  query_result=$(lark-cli api GET "/open-apis/drive/v1/export_tasks/$ticket" \
    --params "{\"token\":\"$token\"}" --as user 2>&1)
  
  local file_token
  file_token=$(echo "$query_result" | python3 -c "import sys,json; print(json.load(sys.stdin).get('data',{}).get('result',{}).get('file_token',''))" 2>/dev/null)
  
  if [ -z "$file_token" ]; then
    echo "  ❌ 导出未完成"
    return 1
  fi
  
  # 3. 下载
  mkdir -p "$target_dir/Attachments"
  local docx_path="$target_dir/Attachments/${title}.docx"
  lark-cli api GET "/open-apis/drive/v1/export_tasks/file/$file_token/download" \
    --output "$docx_path" --as user > /dev/null 2>&1
  
  if [ ! -f "$docx_path" ]; then
    echo "  ❌ 下载失败"
    return 1
  fi
  
  # 4. pandoc 转 Markdown
  local media_dir="$target_dir/Attachments"
  pandoc "$docx_path" -t markdown \
    --extract-media="$media_dir" \
    -o "/tmp/doc_convert_tmp.md" 2>/dev/null
  
  # 5. 修复路径并写文件
  python3 << PYEOF
import re, os
with open('/tmp/doc_convert_tmp.md') as f:
    content = f.read()
media_dir = "$media_dir"
content = content.replace(media_dir + '/', 'Attachments/')
content = re.sub(r'\{width=[^\}]+\}', '', content)
content = re.sub(r'\{height=[^\}]+\}', '', content)
frontmatter = '''---
title: "${title}"
source: feishu
feishu_token: "${token}"
feishu_type: doc
feishu_url: "https://reliablesense.feishu.cn/doc/${token}"
export_method: export-api+pandoc
migrated: 2026-04-04
tags:
  - feishu-migration
---

'''
out_path = "${target_dir}/${title}.md"
os.makedirs(os.path.dirname(out_path), exist_ok=True)
with open(out_path, 'w') as f:
    f.write(frontmatter + content)
PYEOF
  
  echo "  ✅ $title"
}

echo "=== 开始批量处理 doc 旧版文档 $(date) ==="

# === Postgis 8个 ===
process_doc "doccnI6f4RL5XRKR8R2k2oA6Ykf" "更新地图中点和边界" "4-Archives/Notes/Feishu/知识库/技术分享/数据库相关文档/Postgis"
process_doc "doccnN1mQdwwDwXCsBhuSsVzTId" "移动缩放旋转地图" "4-Archives/Notes/Feishu/知识库/技术分享/数据库相关文档/Postgis"
process_doc "doccnvu9gfk9NPRnE1FMF7fpNFe" "移动电子围栏到火星坐标" "4-Archives/Notes/Feishu/知识库/技术分享/数据库相关文档/Postgis"
process_doc "doccnZUAaAKBqN3uCPCiAHkWo30" "修改火星坐标完整语句" "4-Archives/Notes/Feishu/知识库/技术分享/数据库相关文档/Postgis"
process_doc "doccn4JOodvetnzvaKMfs3aIBSh" "偏移位置数据到火星坐标" "4-Archives/Notes/Feishu/知识库/技术分享/数据库相关文档/Postgis"
process_doc "doccnbSee08xdsJhTWt1nXJccZc" "火星坐标转换" "4-Archives/Notes/Feishu/知识库/技术分享/数据库相关文档/Postgis"
process_doc "doccnhqA2pLGKjd5fnqdDsdRbig" "获取指定范围内的点" "4-Archives/Notes/Feishu/知识库/技术分享/数据库相关文档/Postgis"
process_doc "doccnZTs4pwAZPya8zQfIgRf7Yf" "将Point转成PointZ" "4-Archives/Notes/Feishu/知识库/技术分享/数据库相关文档/Postgis"

# === TimescaleDB 4个 ===
process_doc "doccnoNAhwDhgg2FpnJ5jOODzZb" "新建hyper_table时Trigger错误" "4-Archives/Notes/Feishu/知识库/技术分享/数据库相关文档/TimescaleDB"
process_doc "doccn2mQON8tP7m08bYrNmq5BYc" "Retention-policy定期删除机制" "4-Archives/Notes/Feishu/知识库/技术分享/数据库相关文档/TimescaleDB"
process_doc "doccnSG2Jc0Fls0feLdgve23DOe" "人员物体每日在线时间统计" "4-Archives/Notes/Feishu/知识库/技术分享/数据库相关文档/TimescaleDB"
process_doc "doccnmbpSo3CRnCMyTYEVFTpbIi" "插入一条t_position数据" "4-Archives/Notes/Feishu/知识库/技术分享/数据库相关文档/TimescaleDB"

# === 技术分享根分类节点 7个 ===
process_doc "doccnhCl9hokfKaILbP59oauDQe" "地图相关文档" "4-Archives/Notes/Feishu/知识库/技术分享"
process_doc "doccnZVmB4zMyd5vRGTAsFKOgYb" "前端相关文档" "4-Archives/Notes/Feishu/知识库/技术分享"
process_doc "doccnGq8IMFmjgrgloGuXAzvOCc" "数据库相关文档" "4-Archives/Notes/Feishu/知识库/技术分享"
process_doc "doccnfb9EwlR5aYvjxzJbUwtlJh" "硬件相关文档" "4-Archives/Notes/Feishu/知识库/技术分享"
process_doc "doccnnHFcpyirHhQWM3GZh4mkQg" "后端相关文档" "4-Archives/Notes/Feishu/知识库/技术分享"
process_doc "doccnlJ8hk4ih92ZXrCFLFc9Zid" "基础平台相关文档" "4-Archives/Notes/Feishu/知识库/技术分享"
process_doc "doccnxeb0O7SDyKIHQDwBWTL3ie" "测试相关文档" "4-Archives/Notes/Feishu/知识库/技术分享"

# === 地图子节点 3个 ===
process_doc "doccnKYx4RPxYSXzTH0ssUvvBmf" "QGIS地图绘制注意事项CAD版" "4-Archives/Notes/Feishu/知识库/技术分享/地图相关文档"
process_doc "doccn6HL7llLqfP4e5qCI96CdUf" "麦钉点云图地图绘制注意事项" "4-Archives/Notes/Feishu/知识库/技术分享/地图相关文档"
process_doc "doccn3DidLn9ur0mvFbqsnXhstd" "png图片导入地图" "4-Archives/Notes/Feishu/知识库/技术分享/地图相关文档"

# === 前端 1个 ===
process_doc "doccnymhDUxjzJsBjuZ5mBGpG4c" "前端React开发规范" "4-Archives/Notes/Feishu/知识库/技术分享/前端相关文档"

# === 后端 1个 ===
process_doc "doccnVRMcLTfhON3R9OLZT7VHgf" "定位平台系统整体改造方案" "4-Archives/Notes/Feishu/知识库/技术分享/后端相关文档"

# === 基础平台 4个 ===
process_doc "doccnqi4YxvSVSY23MSLXIkwIKe" "CICD流程介绍" "4-Archives/Notes/Feishu/知识库/技术分享/基础平台相关文档"
process_doc "doccnUileviuvksypU7AAbSEGwg" "Gitlab-CICD说明" "4-Archives/Notes/Feishu/知识库/技术分享/基础平台相关文档"
process_doc "doccnlE0yWc24L79rE98oSVsY8d" "开发分支管理规范" "4-Archives/Notes/Feishu/知识库/技术分享/基础平台相关文档"
process_doc "doccncqa7DwRv2fD3Z3KA6oO4oh" "前后端CICD" "4-Archives/Notes/Feishu/知识库/技术分享/基础平台相关文档"

# === 测试 5个 ===
process_doc "doccnvKjRt0RgI04vi1UFEuAW4f" "测试流程1" "4-Archives/Notes/Feishu/知识库/技术分享/测试相关文档"
process_doc "doccnUSmCPXtSpHsITXo3gMqtqd" "测试的流程及内容" "4-Archives/Notes/Feishu/知识库/技术分享/测试相关文档"
process_doc "doccnXKbFqjR5Up9dVYrzjvUUmh" "测试计划初稿" "4-Archives/Notes/Feishu/知识库/技术分享/测试相关文档"
process_doc "doccnoMeCyK1lHtPzzIxxZTmB8U" "测试平台对比" "4-Archives/Notes/Feishu/知识库/技术分享/测试相关文档"
process_doc "doccnTqc7EnZxfZYH0T20rXWLVe" "禅道测试相关操作手册" "4-Archives/Notes/Feishu/知识库/技术分享/测试相关文档"

# === 规章制度 9个 ===
process_doc "doccnw7E90pRZqZbad9ZqMraele" "人力资源制度" "4-Archives/Notes/Feishu/知识库/规章制度"
process_doc "doccn1pktcI7i62LgQO3wTFvCDh" "财务制度" "4-Archives/Notes/Feishu/知识库/规章制度"
process_doc "doccn2IXTE0xjbI4zNUzhNjdOCc" "法务制度" "4-Archives/Notes/Feishu/知识库/规章制度"
process_doc "doccn8tPZL9k9QZy2MzWif1qWDb" "公关制度" "4-Archives/Notes/Feishu/知识库/规章制度"
process_doc "doccnNlv7YbCNSsWjdLnLTkRYWb" "采购制度" "4-Archives/Notes/Feishu/知识库/规章制度"
process_doc "doccn2AHiWmD3UQoSfsKJOWsTkc" "员工管理制度" "4-Archives/Notes/Feishu/知识库/规章制度/人力资源制度"
process_doc "doccn1Ub5gQHHvFcnKIkDy1HNmc" "薪酬福利制度" "4-Archives/Notes/Feishu/知识库/规章制度/人力资源制度"
process_doc "doccn7ZeBuL5f7dFVfYOl9ktgUg" "绩效评估制度" "4-Archives/Notes/Feishu/知识库/规章制度/人力资源制度"
process_doc "doccnwBIuqGBMP6DDr49tpEK98J" "人才政策制度" "4-Archives/Notes/Feishu/知识库/规章制度/人力资源制度"

# === 云空间 5个（组织架构图已处理） ===
process_doc "doccnYL2wLoROVlZqKWO39CnGMh" "定位平台后端汇总" "4-Archives/Notes/Feishu/云空间/莱讯科技/项目开发管理/定位平台企业版"
process_doc "doccnNYXYzLw4jvVOBOTjTmjswh" "软件架构图" "4-Archives/Notes/Feishu/云空间/莱讯科技/项目开发管理/定位平台企业版"
process_doc "doccnHv3bpc59pIIObYxQ8d1Bkf" "madinat_hll集群" "4-Archives/Notes/Feishu/云空间/莱讯科技/项目运维管理/集群资料"
process_doc "doccnRbr2ps3Rpla22Se3M7vnFc" "madinat_xmc集群" "4-Archives/Notes/Feishu/云空间/莱讯科技/项目运维管理/集群资料"
process_doc "doccn6POZJyaWmcGGsWDbuyGARb" "madinat_hjc集群" "4-Archives/Notes/Feishu/云空间/莱讯科技/项目运维管理/集群资料"

echo ""
echo "=== 全部完成 $(date) ==="
