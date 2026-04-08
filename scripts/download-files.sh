#!/bin/bash
# 飞书 file 附件批量下载

dl() {
  local token="$1" title="$2" target_dir="$3"
  
  # 检查是否已存在（按文件名模糊匹配）
  if [ -f "$target_dir/$title" ]; then
    echo "⏭️  跳过: $title"
    return 0
  fi
  
  echo "📎 下载: $title"
  mkdir -p "$target_dir"
  
  lark-cli drive +download --file-token "$token" --output "$target_dir/$title" --as user > /dev/null 2>&1
  
  if [ -f "$target_dir/$title" ]; then
    echo "  ✅ $title"
  else
    echo "  ❌ 失败: $title"
  fi
}

echo "=== 开始下载 file 附件 $(date) ==="

# 根目录散落文件
R="4-Archives/Notes/Feishu/云空间/根目录"
dl "VmgKbcDxdo0OwLxIzrAcnBqlnic" "广州白云国际机场三期扩建项目-综合定位-接口规范-V1.0.2.docx" "$R"
dl "OVHGbClJOoavkLx3gStcUVGAngh" "综合定位系统-深化设计方案.docx" "$R"
dl "RwsBbb50NoKUaKxeVutcaFWBnVd" "deploy.yaml" "$R"
dl "JV2ibGyG9oVohcxlBwJcQdbenJe" "综合定位系统功能清单.xlsx" "$R"
dl "QeNlbb8xyoOSVPxfVMgcR8uCnKc" "智慧仓储物流早会汇报v1.5.pptx" "$R"
dl "YUCNbnhyMooytWxAZVZcntx4nff" "5.20日洛阳石化系统bug问题汇总.xlsx" "$R"
dl "T41fbSI4xoRMTJxtiWkctSUxnvp" "广州市公办小学招生报名系统入学申请表.xls" "$R"
dl "JXLib9uFkoA5F3xWLfxcD2jlnKf" "14号夜班差异分析.xlsx" "$R"
dl "E1b4biPmsoA4Ztx5Zj8c7CC0n6q" "数字化.xlsx" "$R"
dl "OuyFbuM1touvroxyPjEcki2on0d" "优化后.txt" "$R"
dl "VvsMbbh4OoziMkxwQGTcUXwMnYf" "Doc2.docx" "$R"
dl "FoTYbNSjwoE1trxSOvWce7rxntf" "翻译.docx" "$R"
dl "MFjsbb7bBoHIr5xo4v7c95kqnvb" "MAC-Address.xlsx" "$R"
dl "WElAbEGxJoExttxZa90cDTeyn1X" "rssi数据.docx" "$R"
dl "Krurb4Ew6okF4jxUP8BcDru3nUf" "SaaS平台操作手册V7.docx" "$R"
dl "GCxtbICnZo5X1QxwnzfcMzErnGf" "认证文件.zip" "$R"
dl "AUT0b1zsdo1SQdxXCgHc9epunIf" "教学比赛.mov" "$R"
dl "P5MBb8Cy6oYsYfx3MZjc8BhonCd" "宏兴裁切.rar" "$R"
dl "YMF3bIlvFoTvxaxPI6IcKLwMnNc" "FRP_GithubArm64_version_1_3_6.apk" "$R"
dl "S0BSboHqco7VUOxrhiucyi9tnNb" "亿童英语分级阅读组稿教师信息汇总表.xlsx" "$R"
dl "Hr8bbKyRUoKdDtxgtLhcfDCknug" "定位平台安装文件及文档.zip" "$R"
dl "UnIjb9C7qocVGExPTZpc9wkAnog" "madinat_hjc.zip" "$R"
dl "NXVgbTKQioF6Kkx26yScwwRbnjg" "转化后数据.zip" "$R"
dl "ADaXb4skOo8TxVxNWSycGyi1nZe" "3.8.7.zip" "$R"
dl "RGtdbb0EYogQjHxMaxmcnf57n5b" "信息平台消息交换标准协议.doc" "$R"

# 何宜峰
dl "L3hKbcijfohKN2xtueVc88dcnEd" "员工入职表-空白.xls" "4-Archives/Notes/Feishu/云空间/何宜峰"

# 王宗光
dl "WRgCb0V8ToSCsqx2qSdcW81Fnlh" "王宗光24年周报.xlsx" "4-Archives/Notes/Feishu/云空间/王宗光"
dl "N4wvbKBhfoKdLMxIlQRckQAlnpd" "用户敏感信息处理.md" "4-Archives/Notes/Feishu/云空间/王宗光"

# 陈子杰
dl "MAbLblaVGoQUsEx9a4NcxF5Kn0g" "核心物联资料.zip" "4-Archives/Notes/Feishu/云空间/陈子杰"
dl "BRc2bmrbKoPzjvxIKmPcBoOFnof" "2023-05-07-20-54-59.mkv" "4-Archives/Notes/Feishu/云空间/陈子杰"

# 莱讯科技 > 项目资料管理 > 广州机场-移动应用平台
M="4-Archives/Notes/Feishu/云空间/莱讯科技/项目资料管理/广州机场-移动应用平台"
dl "UIrtb8LiKoAiUaxpRyWcRgPOnve" "移动应用平台用户手册.docx" "$M"
dl "LLVZbmV83oQqfDxp1AvcNk7cnUg" "移动应用平台资产.xlsx" "$M"
dl "PwExbhasyon68OxsTiJcXhrcnWc" "移动应用平台进程清单.xlsx" "$M"
dl "BCd4bdxfwodyh7xMbHgcltnGn8b" "移动应用平台数据字典.docx" "$M"
dl "LY7tboh44oKC38xYhiLcwqkUnmT" "移动应用平台配置清单.docx" "$M"
dl "UbD6bL2pzooRmIxaWM9ckhhunsb" "移动应用平台故障处理手册.docx" "$M"
dl "MCZ1bb5KSoRy0bxuOQGcxfwNnX9" "T3移动应用平台测评资产调研.xlsx" "$M"
dl "CPDybNkttoyBfIxdxtBcwrPUntf" "渗透测试系统域名调研-移动应用平台.xlsx" "$M"
dl "Pnnub7W0WonNIDxnBQGcsWuinma" "移动应用平台运维白皮书.docx" "$M"
dl "T3xWbWNsmoJdxxxVV0McQszSnqg" "广州机场移动应用任务清单.xlsx" "$M"
dl "Kkf6bl2V4oAr5vx5m4QccUDDniI" "移动应用平台开发与测试进展汇报.pdf" "$M"

# 莱讯科技 > 项目运维管理
dl "JPHkbo3MZoCvClxqavvcqNvynKf" "位置压测相关服务器配置.xlsx" "4-Archives/Notes/Feishu/云空间/莱讯科技/项目运维管理"

echo ""
echo "=== file 下载完成 $(date) ==="
