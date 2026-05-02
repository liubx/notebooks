#!/usr/bin/env python3
"""通用项目迁移脚本：扫描 → 创建节点 → drive copy + move_docs_to_wiki → 清理shortcut → 写入子页面列表"""
import subprocess, json, time, sys, os

# === 配置 ===
PROJECT_NAME = "武汉机场"
FOLDER_TOKEN = "fldcnHmHajD7TQATmdiqbTIuGRe"
SPACE_ID = "7632924686837418976"
PARENT_NODE = "PhpuwDqUvidfKRkUXMKcLMJ0nHc"  # 归档项目父节点
LOCAL_ARCHIVE = "4-Archives/Notes/Feishu/云空间/莱讯科技/项目资料管理/998. 售后项目/武汉机场"
TARGET_PATH = "4-Archives/Projects/Work/武汉机场"

# 本地保留的文件扩展名（小写）
LOCAL_KEEP_EXTS = {'.md', '.docx', '.xlsx', '.pptx', '.pdf', '.png', '.jpg', '.jpeg', '.svg'}

def api(method, path, params=None, data=None):
    cmd = ['lark-cli', 'api', method, path]
    if params: cmd += ['--params', json.dumps(params)]
    if data: cmd += ['--data', json.dumps(data)]
    cmd += ['--as', 'user']
    r = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
    return json.loads(r.stdout)

def list_folder(folder_token):
    d = api('GET', '/open-apis/drive/v1/files', params={'folder_token': folder_token, 'page_size': '200'})
    return d.get('data', {}).get('files', [])

def scan_recursive(folder_token, path=''):
    files = list_folder(folder_token)
    result = []
    for f in files:
        if f['type'] == 'shortcut': continue
        f['path'] = path
        if f['type'] == 'folder':
            time.sleep(1)
            result.extend(scan_recursive(f['token'], f'{path}/{f["name"]}'))
        else:
            result.append(f)
    return result

def create_node(parent, title):
    d = api('POST', f'/open-apis/wiki/v2/spaces/{SPACE_ID}/nodes',
            data={'obj_type': 'docx', 'parent_node_token': parent, 'node_type': 'origin', 'title': title})
    n = d['data']['node']
    return n['node_token'], n['obj_token']

def drive_copy_and_move(token, name, ftype, parent_wiki):
    # copy
    d = api('POST', f'/open-apis/drive/v1/files/{token}/copy',
            params={'file_token': token},
            data={'type': ftype, 'name': name, 'folder_token': FOLDER_TOKEN})
    copy_token = d['data']['file']['token']
    time.sleep(1)
    # move to wiki
    api('POST', f'/open-apis/wiki/v2/spaces/{SPACE_ID}/nodes/move_docs_to_wiki',
        data={'parent_wiki_token': parent_wiki, 'obj_type': ftype, 'obj_token': copy_token})
    return copy_token

def delete_shortcuts(folder_token):
    files = list_folder(folder_token)
    count = 0
    for f in files:
        if f['type'] == 'shortcut':
            api('DELETE', f'/open-apis/drive/v1/files/{f["token"]}', params={'type': 'shortcut'})
            count += 1; time.sleep(0.5)
        elif f['type'] == 'folder':
            time.sleep(0.5); count += delete_shortcuts(f['token'])
    return count

def get_wiki_children(parent):
    d = api('GET', f'/open-apis/wiki/v2/spaces/{SPACE_ID}/nodes', params={'parent_node_token': parent, 'page_size': '50'})
    return d.get('data', {}).get('items', [])

def write_node_content(obj_token, title, children):
    lines = [f'# {title}\n']
    for c in children:
        lines.append(f'- <mention-doc token="{c["node_token"]}" type="wiki">{c["title"]}</mention-doc>（{c["obj_type"]}）')
    md = '\n'.join(lines)
    proc = subprocess.Popen(['lark-cli','docs','+update','--doc',obj_token,'--markdown','-','--mode','overwrite','--as','user'],
        stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    stdout, _ = proc.communicate(input=md, timeout=45)
    return '"success": true' in stdout

def write_tree(node_token, title):
    children = get_wiki_children(node_token)
    if not children: return
    node = api('GET', f'/open-apis/wiki/v2/spaces/{SPACE_ID}/nodes/{node_token}')
    obj_token = node['data']['node']['obj_token']
    ok = write_node_content(obj_token, title, children)
    print(f"  {'✅' if ok else '❌'} {title} ({len(children)} 子页面)")
    time.sleep(1)
    for c in children:
        if c.get('has_child') and c['obj_type'] == 'docx':
            time.sleep(1); write_tree(c['node_token'], c['title'])

# === 主流程 ===
print(f"=== 迁移 {PROJECT_NAME} ===\n")

# 步骤 1: 扫描飞书目录
print("步骤 1: 扫描飞书目录")
all_files = scan_recursive(FOLDER_TOKEN)
print(f"  共 {len(all_files)} 个文件")
groups = {}
for f in all_files:
    p = f['path'] or '根目录'
    groups.setdefault(p, []).append(f)
for g in sorted(groups.keys()):
    print(f"  {g}: {len(groups[g])} 个")

# 步骤 2: 复制本地文件
print("\n步骤 2: 复制本地文件")
os.makedirs(TARGET_PATH, exist_ok=True)
if os.path.exists(LOCAL_ARCHIVE):
    local_copied = 0
    for root, dirs, files in os.walk(LOCAL_ARCHIVE):
        for fname in files:
            if fname in ('README.md', '.DS_Store'): continue
            ext = os.path.splitext(fname)[1].lower()
            rel = os.path.relpath(root, LOCAL_ARCHIVE)
            if rel == '.': rel = ''
            src = os.path.join(root, fname)
            if rel:
                dst_dir = os.path.join(TARGET_PATH, rel)
                os.makedirs(dst_dir, exist_ok=True)
                dst = os.path.join(dst_dir, fname)
            else:
                dst = os.path.join(TARGET_PATH, fname)
            # 只复制本地保留的类型
            if ext in LOCAL_KEEP_EXTS:
                try:
                    import shutil
                    shutil.copy2(src, dst)
                    local_copied += 1
                except: pass
    print(f"  复制了 {local_copied} 个文件")
else:
    print(f"  本地归档目录不存在: {LOCAL_ARCHIVE}")

# 步骤 3: 创建知识库节点
print("\n步骤 3: 创建知识库节点")
root_nt, root_ot = create_node(PARENT_NODE, PROJECT_NAME)
print(f"  {PROJECT_NAME}: node={root_nt} obj={root_ot}")
time.sleep(1)

# 根据文件数量决定是否分类
total_files = len(all_files)
if total_files <= 30:
    # 不分类，所有文件直接放根节点
    category_map = {p: root_nt for p in groups.keys()}
    print("  文件 <= 30，不建分类节点")
else:
    # 按子目录分类
    category_map = {'根目录': root_nt}
    created_categories = {}  # 缓存已创建的分类名 → node_token
    for p in sorted(groups.keys()):
        if p != '根目录':
            cat_name = p.strip('/').split('/')[0]  # 取一级子目录名
            if cat_name not in created_categories:
                nt, ot = create_node(root_nt, cat_name)
                created_categories[cat_name] = nt
                print(f"  分类: {cat_name} → {nt}")
                time.sleep(1)
            category_map[p] = created_categories[cat_name]

# 步骤 4: drive copy + move_docs_to_wiki
print(f"\n步骤 4: drive copy + move_docs_to_wiki ({total_files} 个文件)")
success = 0; fail = 0
for path_key, files in groups.items():
    parent_wiki = category_map.get(path_key, root_nt)
    for f in files:
        try:
            drive_copy_and_move(f['token'], f['name'], f['type'], parent_wiki)
            success += 1
            print(f"  ✅ {f['name']}")
            time.sleep(1)
        except Exception as e:
            fail += 1
            print(f"  ❌ {f['name']}: {e}")
            time.sleep(2)

# 步骤 5: 清理 shortcut
print(f"\n步骤 5: 清理 shortcut")
sc = delete_shortcuts(FOLDER_TOKEN)
print(f"  删除 {sc} 个")

# 步骤 6: 写入子页面列表
print(f"\n步骤 6: 写入子页面列表")
root_children = get_wiki_children(root_nt)
node_data = api('GET', f'/open-apis/wiki/v2/spaces/{SPACE_ID}/nodes/{root_nt}')
root_obj = node_data['data']['node']['obj_token']
ok = write_node_content(root_obj, PROJECT_NAME, root_children)
print(f"  {'✅' if ok else '❌'} {PROJECT_NAME} 根节点 ({len(root_children)} 子页面)")
time.sleep(1)
for c in root_children:
    if c.get('has_child') and c['obj_type'] == 'docx':
        time.sleep(1); write_tree(c['node_token'], c['title'])

print(f"\n=== 完成 ===")
print(f"成功: {success}, 失败: {fail}, shortcut: {sc}")
print(f"知识库根节点: {root_nt}")

# 保存结果
with open('migration_result.json', 'w') as fp:
    json.dump({'project': PROJECT_NAME, 'root_node': root_nt, 'root_obj': root_ot,
               'success': success, 'fail': fail, 'shortcuts': sc}, fp, ensure_ascii=False, indent=2)
