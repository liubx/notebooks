#!/usr/bin/env python3
"""
飞书 bitable 批量导出 v2
- 导出 API → xlsx
- 扫描附件字段 → 下载图片 → 生成附件映射 md
"""
import subprocess, json, os, time, sys

BITABLES = [
    ("NbIPbswwSaCfPpsWak7cbCHsnwe", "广州机场综合定位", "4-Archives/Notes/Feishu/云空间/根目录"),
    ("NepGb0sWdaPfnosidcMc7yspnFg", "周报测试", "4-Archives/Notes/Feishu/云空间/根目录"),
    ("RIHubtFOhadg4TsFWJoch9iEnuh", "工作周报", "4-Archives/Notes/Feishu/云空间/王宗光"),
    ("ZQj0bMC5eaghvxsBxzGcBWDznUc", "会议签到表", "4-Archives/Notes/Feishu/云空间/王宗光"),
    ("ZmmjbljSpa3KWBskm40cPgWGnPg", "需求及Bug管理-1", "4-Archives/Notes/Feishu/云空间/陈子杰"),
    ("BSDnb80vUaGm4hsjM06cIE0bncD", "需求及Bug管理-2", "4-Archives/Notes/Feishu/云空间/陈子杰"),
    ("RLRqbFnrPaokuRsVtTbcjkMLnZd", "移动终端目前缺失功能", "4-Archives/Notes/Feishu/云空间/陈子杰/广州机场-移动应用平台"),
    ("bascncveOYEhfjbtaaj3U6Rgete", "客户关系管理", "4-Archives/Notes/Feishu/云空间/莱讯科技/销售管理"),
    ("bascnemc8tozwPeCvL2GmUfG9Tg", "合同订单管理", "4-Archives/Notes/Feishu/云空间/莱讯科技/公司内部资料"),
    ("bascnm0yQj7bRGrIZE1vSUXMOGg", "任务管理", "4-Archives/Notes/Feishu/云空间/莱讯科技/公司内部资料"),
    ("A9NpbHhPgafD4osRWROcWPydnse", "机场任务", "4-Archives/Notes/Feishu/云空间/莱讯科技/项目资料管理/广州机场"),
]

def run_cmd(args, timeout=30):
    try:
        r = subprocess.run(args, capture_output=True, text=True, timeout=timeout)
        return json.loads(r.stdout) if r.stdout.strip() else None
    except:
        return None

def export_xlsx(token, title, target_dir):
    xlsx_path = os.path.join(target_dir, f"{title}.xlsx")
    
    # 创建导出任务
    d = run_cmd(["lark-cli", "api", "POST", "/open-apis/drive/v1/export_tasks",
                 "--data", json.dumps({"file_extension":"xlsx","token":token,"type":"bitable"}),
                 "--as", "user"])
    if not d or d.get("code") != 0:
        return False
    
    ticket = d["data"]["ticket"]
    time.sleep(4)
    
    # 查询结果
    d = run_cmd(["lark-cli", "api", "GET", f"/open-apis/drive/v1/export_tasks/{ticket}",
                 "--params", json.dumps({"token": token}), "--as", "user"])
    if not d or d.get("data",{}).get("result",{}).get("job_status") != 0:
        return False
    
    file_token = d["data"]["result"]["file_token"]
    
    # 下载
    os.makedirs(target_dir, exist_ok=True)
    run_cmd(["lark-cli", "api", "GET", f"/open-apis/drive/v1/export_tasks/file/{file_token}/download",
             "--output", xlsx_path, "--as", "user"], timeout=60)
    
    return os.path.exists(xlsx_path)

def find_attachments(token):
    """扫描所有表的附件字段，返回 [(table_name, record_desc, file_token, file_name)]"""
    attachments = []
    
    # 获取表列表
    d = run_cmd(["lark-cli", "base", "+table-list", "--base-token", token, "--as", "user"])
    if not d or not d.get("ok"):
        return attachments
    
    tables = d.get("data", {}).get("items", [])
    
    for table in tables:
        table_id = table["table_id"]
        table_name = table.get("name", "未命名")
        
        # 获取字段，找附件类型
        fd = run_cmd(["lark-cli", "base", "+field-list", "--base-token", token,
                      "--table-id", table_id, "--as", "user"])
        if not fd or not fd.get("ok"):
            continue
        
        fields = fd.get("data", {}).get("items", [])
        att_fields = [f["field_name"] for f in fields if f.get("type") == "attachment"]
        
        if not att_fields:
            continue
        
        # 读取记录
        rd = run_cmd(["lark-cli", "base", "+record-list", "--base-token", token,
                      "--table-id", table_id, "--limit", "100", "--as", "user"], timeout=60)
        if not rd or not rd.get("ok"):
            continue
        
        records = rd.get("data", {}).get("items", [])
        for rec in records:
            rec_fields = rec.get("fields", {})
            for att_field in att_fields:
                att_val = rec_fields.get(att_field)
                if isinstance(att_val, list):
                    for a in att_val:
                        if isinstance(a, dict) and "file_token" in a:
                            attachments.append((
                                table_name,
                                att_field,
                                a["file_token"],
                                a.get("name", "unknown")
                            ))
        
        time.sleep(0.3)
    
    return attachments

def download_attachment(file_token, output_dir):
    for ext in ["png", "jpg", "jpeg", "gif", "webp", "pdf"]:
        if os.path.exists(os.path.join(output_dir, f"{file_token}.{ext}")):
            return f"{file_token}.{ext}"
    
    d = run_cmd(["lark-cli", "docs", "+media-download", "--token", file_token,
                 "--output", os.path.join(output_dir, file_token), "--as", "user"])
    if d and d.get("ok"):
        return os.path.basename(d["data"]["saved_path"])
    return None

def process_bitable(token, title, target_dir):
    print(f"📋 {title}")
    
    # 1. 导出 xlsx
    xlsx_path = os.path.join(target_dir, f"{title}.xlsx")
    if os.path.exists(xlsx_path):
        print(f"  ⏭️ xlsx 已存在")
    else:
        if export_xlsx(token, title, target_dir):
            print(f"  ✅ xlsx 导出成功")
        else:
            print(f"  ❌ xlsx 导出失败")
            return
    
    # 2. 删除旧的 md 文件
    old_md = os.path.join(target_dir, f"{title}.md")
    if os.path.exists(old_md):
        os.remove(old_md)
    
    # 3. 扫描附件
    attachments = find_attachments(token)
    if not attachments:
        print(f"  📎 无附件")
        return
    
    print(f"  📎 发现 {len(attachments)} 个附件")
    
    # 4. 下载附件
    att_dir = os.path.join(target_dir, "Attachments")
    os.makedirs(att_dir, exist_ok=True)
    
    downloaded = []
    for table_name, field_name, file_token, file_name in attachments:
        local = download_attachment(file_token, att_dir)
        if local:
            downloaded.append((table_name, field_name, file_name, local))
    
    if not downloaded:
        return
    
    # 5. 生成附件映射 md
    mapping_path = os.path.join(target_dir, f"{title}-附件映射.md")
    with open(mapping_path, "w") as f:
        f.write(f"""---
title: "{title}-附件映射"
source: feishu
feishu_token: "{token}"
---

# {title} 附件映射

""")
        current_table = None
        for table_name, field_name, file_name, local in downloaded:
            if table_name != current_table:
                current_table = table_name
                f.write(f"## {table_name}\n\n")
            
            ext = local.rsplit(".", 1)[-1].lower() if "." in local else ""
            if ext in ("png", "jpg", "jpeg", "gif", "webp"):
                f.write(f"**{file_name}**\n\n![](Attachments/{local})\n\n")
            else:
                f.write(f"📎 [{file_name}](Attachments/{local})\n\n")
    
    print(f"  ✅ 附件映射已生成 ({len(downloaded)} 个)")

if __name__ == "__main__":
    print(f"=== 开始处理 bitable {time.strftime('%H:%M:%S')} ===")
    for token, title, target_dir in BITABLES:
        process_bitable(token, title, target_dir)
        time.sleep(0.5)
    print(f"\n=== 完成 {time.strftime('%H:%M:%S')} ===")
