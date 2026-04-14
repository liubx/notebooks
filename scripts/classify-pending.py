#!/usr/bin/env python3
"""读取36个待确认会议纪要的内容，输出分类建议"""
import os, re, sys

ROOT = '4-Archives/Notes/Feishu/云空间'
pending_files = []

with open('1-Projects/Personal/笔记迁移/会议纪要分类结果.tsv', 'r') as f:
    for line in f:
        if '\t待确认\t' in line:
            parts = line.strip().split('\t')
            if parts[0]:
                pending_files.append(parts[0])

# 去重：只看智能纪要（内容更精炼）
unique = {}
for fp in pending_files:
    fname = fp.split('/')[-1]
    topic = fname
    for p in ['文字记录：', '智能纪要：']:
        topic = topic.replace(p, '')
    topic = re.sub(r'\d{4}年\d+月\d+日.*', '', topic).strip()
    if topic not in unique or '智能纪要' in fname:
        unique[topic] = fp

for topic, fp in sorted(unique.items()):
    full = f'{ROOT}/{fp}'
    if not os.path.exists(full):
        print(f'{topic} | 文件不存在', flush=True)
        continue
    with open(full, 'r') as f:
        c = f.read(3000)
    if '---' in c:
        ps = c.split('---', 2)
        if len(ps) >= 3: c = ps[2]
    c = c.strip()[:300]
    
    cat = '❓ 待确认'
    for kws, label in [
        (['新太','新钢联','料棚','卸料','上料','铲车','堆垛','料坑','叫号','倒运','卸货'], '新太项目'),
        (['广州机场','综合定位','A域','B域','电子围栏','手推车','AESB','TCDM','白云','三标段','机场','陪伴运行'], '广州机场'),
        (['上港','仓储','出入库','RFID'], '上港项目'),
        (['武汉机场'], '武汉机场'),
        (['洛阳石化','洛阳化工'], '洛阳石化'),
        (['Beacon','CLE','launchable','墨水屏','MQTT','定位引擎'], '技术讨论'),
        (['版本','迭代','需求评审','排期','sprint'], '产品研发'),
    ]:
        if any(k in c for k in kws):
            cat = f'→ {label}'
            break
    
    print(f'{topic} | {cat}', flush=True)
    print(f'  摘要: {c[:150]}', flush=True)
    print(flush=True)
