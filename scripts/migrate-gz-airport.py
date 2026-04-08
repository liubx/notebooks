#!/usr/bin/env python3
"""广州机场-综合定位 补充迁移"""
import subprocess, json, os, re, time, sys

TARGET = "4-Archives/Notes/Feishu/云空间/莱讯科技/项目资料管理/广州机场"

def run(args, timeout=30):
    try:
        r = subprocess.run(args, capture_output=True, text=True, timeout=timeout)
        return json.loads(r.stdout) if r.stdout.strip() else None
    except:
        return None

def fetch_docx(token, title):
    """fetch docx 并下载图片"""
    d = run(["lark-cli", "docs", "+fetch", "--doc", token, "--as", "user"])
    if not d or not d.get("ok"):
        return False
    md = d["data"]["markdown"]
    
    # 提取图片
    imgs = re.findall(r'<image token="([^"]+)"', md)
    img_map = {}
    if imgs:
        att_dir = os.path.join(TARGET, "Attachments")
        os.makedirs(att_dir, exist_ok=True)
        for img_token in imgs:
            # 检查已存在
            found = False
            for ext in ["png","jpg","jpeg","gif","webp"]:
                if os.path.exists(os.path.join(att_dir, f"{img_token}.{ext}")):
                    img_map[img_token] = f"{img_token}.{ext}"
                    found = True
                    break
            if not found:
                dl = run(["lark-cli", "docs", "+media-download", "--token", img_token,
                         "--output", os.path.join(att_dir, img_token), "--as", "user"])
                if dl and dl.get("ok"):
                    img_map[img_token] = os.path.basename(dl["data"]["saved_path"])
            time.sleep(0.1)
    
    # 替换图片标签
    def repl(match):
        t = re.search(r'token="([^"]+)"', match.group(0))
        if t and t.group(1) in img_map:
            return f"![](Attachments/{img_map[t.group(1)]})"
        return match.group(0)
    md = re.sub(r'<image[^>]*/>', repl, md)
    
    # 写文件
    content = f"""---
title: "{title}"
source: feishu
feishu_token: "{token}"
feishu_type: docx
feishu_url: "https://reliablesense.feishu.cn/docx/{token}"
migrated: 2026-04-05
tags:
  - feishu-migration
---

{md}"""
    with open(os.path.join(TARGET, f"{title}.md"), "w") as f:
        f.write(content)
    return True

def export_sheet(token, title):
    d = run(["lark-cli", "api", "POST", "/open-apis/drive/v1/export_tasks",
             "--data", json.dumps({"file_extension":"xlsx","token":token,"type":"sheet"}),
             "--as", "user"])
    if not d or d.get("code") != 0:
        return False
    ticket = d["data"]["ticket"]
    time.sleep(4)
    d = run(["lark-cli", "api", "GET", f"/open-apis/drive/v1/export_tasks/{ticket}",
             "--params", json.dumps({"token": token}), "--as", "user"])
    if not d or d.get("data",{}).get("result",{}).get("job_status") != 0:
        return False
    ft = d["data"]["result"]["file_token"]
    run(["lark-cli", "api", "GET", f"/open-apis/drive/v1/export_tasks/file/{ft}/download",
         "--output", os.path.join(TARGET, f"{title}.xlsx"), "--as", "user"], timeout=60)
    return os.path.exists(os.path.join(TARGET, f"{title}.xlsx"))

def export_bitable(token, title):
    d = run(["lark-cli", "api", "POST", "/open-apis/drive/v1/export_tasks",
             "--data", json.dumps({"file_extension":"xlsx","token":token,"type":"bitable"}),
             "--as", "user"])
    if not d or d.get("code") != 0:
        return False
    ticket = d["data"]["ticket"]
    time.sleep(4)
    d = run(["lark-cli", "api", "GET", f"/open-apis/drive/v1/export_tasks/{ticket}",
             "--params", json.dumps({"token": token}), "--as", "user"])
    if not d or d.get("data",{}).get("result",{}).get("job_status") != 0:
        return False
    ft = d["data"]["result"]["file_token"]
    run(["lark-cli", "api", "GET", f"/open-apis/drive/v1/export_tasks/file/{ft}/download",
         "--output", os.path.join(TARGET, f"{title}.xlsx"), "--as", "user"], timeout=60)
    return os.path.exists(os.path.join(TARGET, f"{title}.xlsx"))

def download_file(token, title):
    path = os.path.join(TARGET, title)
    if os.path.exists(path):
        return True
    run(["lark-cli", "drive", "+download", "--file-token", token,
         "--output", path, "--as", "user"], timeout=30)
    return os.path.exists(path)

print(f"=== 广州机场补充迁移 {time.strftime('%H:%M:%S')} ===")

# docx 5个
docx_list = [
    ("XsPQdVzUKo5wH5xfT94cVMRCngb", "系统建设清单"),
    ("WdNtdRhPxoN8VoxwzI5cjocCntK", "系统功能清单"),
    ("Uxo1dMqAfo3o1dxp3JOc7zgInhe", "表C.2.5深化设计图会审记录"),
    ("WI9UdRl6Eo0MoHxmnjxcGdmNnKh", "堡垒机登录服务器说明"),
    ("I60Ld5Ac7oSov0xDw8ZceXxDnfd", "堡垒机Linux上传下载文件说明"),
]
for token, title in docx_list:
    if os.path.exists(os.path.join(TARGET, f"{title}.md")):
        print(f"⏭️ {title}")
        continue
    print(f"📄 {title}")
    if fetch_docx(token, title):
        print(f"  ✅")
    else:
        print(f"  ❌")
    time.sleep(0.3)

# sheet 18个
sheet_list = [
    ("XgaksEdpZh2P18td6aEc1smNndc", "系统域名调研表"),
    ("S2RDswXG4hlYCmtQKVMcWUP4nCc", "综合定位系统网络需求表"),
    ("B0hUsnkcshsoWpticWFcvUEOnZf", "样板间设备"),
    ("QesCsQWpNhettFt7DAkcVtSKnch", "项目施工计划进度表"),
    ("Xp61s99BchOIectV2NkcTdfYnUd", "文档要求"),
    ("D5x5sP4whhDBWBtC3L0clKOLnib", "堡垒机权限申请"),
    ("M3i6sXhp4hpMPEtfRmOc8cF3nHx", "广州机场工作量评估"),
    ("H69Vs4AjlhHdFStq2HjcBGRUnPc", "广州机场工作量评估-v2"),
    ("NOO5sD0hahoG4Lt9vn0c6LmSn9c", "功能清单"),
    ("R8b0sOPuZh3XJLtvcLNc2i4BnNd", "访问网络表"),
    ("Q6khsOab0hyBROt2tiUcJJapnyg", "业务资源规划调研-弱电三标"),
    ("IIQwsa2FnhsyZot58h5cR41YnRg", "vpn申请表"),
    ("Oprns76RWhg3WVt5aXDcXWESnAg", "装饰观摩路线现场情况表"),
    ("QjaZs72OHh5wtCtE8ZpcpKEVnLg", "功能清单-v2"),
    ("ERh9syWSRhxpoNtwSmlceSyXndc", "广州机场三期弱电三标段清单"),
    ("I1UesR7uXhSEoItbq3EcmdIanle", "航站楼协同决策管理系统TCDM"),
    ("KLmysBGXLhroWctx0oMc7EEUnSg", "综合定位系统-sheet"),
    ("BNhgsWFdBhdWm3tGmUmc4o4lnHo", "大运控协同管理平台-sheet"),
]
for token, title in sheet_list:
    if os.path.exists(os.path.join(TARGET, f"{title}.xlsx")):
        print(f"⏭️ {title}")
        continue
    print(f"📊 {title}")
    if export_sheet(token, title):
        print(f"  ✅")
    else:
        print(f"  ❌")
    time.sleep(0.3)

# bitable 1个（机场任务已导出，机场任务管理是新的）
bitable_list = [
    ("PLw6bQFY0azlLlsKMoKclePVnxb", "机场任务管理-v2"),
]
for token, title in bitable_list:
    if os.path.exists(os.path.join(TARGET, f"{title}.xlsx")):
        print(f"⏭️ {title}")
        continue
    print(f"📋 {title}")
    if export_bitable(token, title):
        print(f"  ✅")
    else:
        print(f"  ❌")
    time.sleep(0.3)

# file 小文件（跳过 zip/mp4/apk 大文件）
file_list = [
    ("UGbJbaqiUoWBJaxH4Hpc9totngd", "广州白云国际机场-综合定位-接口规范-V1.0.2.docx"),
    ("I0hAb0OW5oROwMxT2fjc6GROn2g", "陪伴运行应急处置措施系统编辑参考模板.docx"),
    ("DdmtbLRcAoWnRmxaAY5cajBbnof", "手推车任务管理完成进度表.xlsx"),
    ("Q4KrbdRUIoD8sAxCg7jcCVUwnsh", "T3综合定位系统测评资产调研.xlsx"),
    ("WvuBbgQYgobrKIx8kLccyTxxnOw", "T3弱电网络策略申请开通登记表.xlsx"),
    ("CCqQbHeDyoBSE4xatNYcE3AWnvc", "HCS安全策略申请表.xlsx"),
    ("LtVjb7KwwoG7d6x7r8bcVthVnvh", "渗透测试系统域名调研-综合定位系统.xlsx"),
    ("S23tbldIpokF8Kxch3GcAax2nPG", "三检-综合定位系统.xlsx"),
    ("FxVybk38downmbxab1Sc4kxenDc", "业务资源规划调研-服务器发放情况.xlsx"),
    ("LmzXb8lQSoJILaxzjYXcu1AWn6c", "备案系统表.doc"),
    ("DYShbuUluo4dttxHgFdcyLm5nvf", "系统域名调研表.xlsx"),
    ("IndvbCShXogH9DxIEjbcyKaqnBb", "业务资源规划调研-服务器发放情况-v2.xlsx"),
    ("RzQibpZP2oEO2BxaJtcc7kgdnqc", "业务资源规划调研V1-综合定位系统.xlsx"),
    ("GlQ5b4tYGokEWJx5N0wce0zsnqb", "业务资源规划调研V1-业务厂家.xlsx"),
    ("VQwPbrSxxoIDpIxWHGbcG3p6nec", "机场企业服务总线使用需求调研表.xlsx"),
]
for token, title in file_list:
    if os.path.exists(os.path.join(TARGET, title)):
        print(f"⏭️ {title}")
        continue
    print(f"📎 {title}")
    if download_file(token, title):
        print(f"  ✅")
    else:
        print(f"  ❌ (可能超时)")
    time.sleep(0.3)

# 大文件跳过
print()
print("⏭️ 跳过大文件:")
print("  - patrol_v1.0.apk")
print("  - 综合定位系统深化图纸.zip")
print("  - 20241206白云信科测试工作推进会.mp4")
print()
print("⏭️ slides 无法导出(8个)，仅保留链接")

print(f"\n=== 完成 {time.strftime('%H:%M:%S')} ===")
