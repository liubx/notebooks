#!/usr/bin/env python3
"""生成同事个人文档的详细文件列表（带链接和分类）"""
import os, re
from collections import defaultdict

ROOT = '4-Archives/Notes/Feishu/云空间'
URL_PREFIX = {'docx':'docx','doc':'docs','file':'file','sheet':'sheets','bitable':'base','mindnote':'mindnotes'}

COLLEAGUES = [
    ('何宜峰的个人文档', '何宜峰'),
    ('陈子杰的个人文档', '陈子杰'),
    ('孙永霖的个人文档', '孙永霖'),
]

# 分类规则
def classify(fname, content=''):
    text = fname + ' ' + content
    if any(k in text for k in ['新太','新钢联','料棚','卸料','上料','铲车','堆垛']):
        return '新太项目', '1-Projects/Work/内蒙新太/'
    if any(k in text for k in ['广州机场','综合定位','A域','B域','电子围栏','AESB','TCDM','白云','移动应用平台','陪伴运行']):
        return '广州机场', '1-Projects/Work/广州机场/'
    if any(k in text for k in ['上港','仓储','出入库']):
        return '上港项目', '1-Projects/Work/上港仓储管理/'
    if any(k in text for k in ['武汉机场']):
        return '武汉机场', '4-Archives/Projects/Work/武汉机场/'
    if any(k in text for k in ['近期会议速递','月度纪要小结']):
        return '留归档（AI汇总）', ''
    if any(k in text for k in ['智能纪要','文字记录','视频会议','Video meeting']):
        return '会议纪要（已在第二章分类）', ''
    if any(k in text for k in ['年终总结','年度总结']):
        return '留归档', ''
    return '待归类', ''

def get_url(fpath):
    if not os.path.exists(fpath): return ''
    try:
        with open(fpath, 'r') as f:
            c = f.read(500)
        m = re.search(r'feishu_url:\s*"([^"]+)"', c)
        if m: return m.group(1)
        mt = re.search(r'feishu_token:\s*"([^"]+)"', c)
        mtype = re.search(r'feishu_type:\s*(\w+)', c)
        if mt and mtype:
            prefix = URL_PREFIX.get(mtype.group(1), mtype.group(1))
            return f'https://reliablesense.feishu.cn/{prefix}/{mt.group(1)}'
    except: pass
    return ''

output = []

for dirname, name in COLLEAGUES:
    dirpath = f'{ROOT}/{dirname}'
    if not os.path.exists(dirpath):
        continue
    
    # 收集所有文件（递归）
    files = []
    for root, dirs, fnames in os.walk(dirpath):
        for fn in sorted(fnames):
            if fn in ('README.md', '.DS_Store'): continue
            rel = os.path.relpath(os.path.join(root, fn), ROOT)
            files.append((fn, rel, os.path.join(root, fn)))
    
    output.append(f'### {name}的个人文档（{len(files)} 个文件）\n')
    output.append(f'| 文件 | 本地路径 | 飞书链接 | 分类 | 目标路径 |')
    output.append(f'|------|---------|---------|------|---------|')
    
    for fn, rel, full in files:
        wl = f'4-Archives/Notes/Feishu/云空间/{rel}'
        if wl.endswith('.md'): wl = wl[:-3]
        
        url = get_url(full)
        url_str = f'[飞书]({url})' if url else '见 README'
        
        cat, target = classify(fn)
        target_str = f'`{target}`' if target else cat
        
        output.append(f'| {fn} | [[{wl}]] | {url_str} | {cat} | {target_str} |')
    
    output.append('')

with open('/tmp/colleague-section.md', 'w') as f:
    f.write('\n'.join(output))

print(f'生成 {len(output)} 行')
