#!/usr/bin/env python3
"""
批量扫描会议纪要文件，根据内容自动分类。
输出 TSV 格式：文件路径 | 分类 | 目标路径 | 判断依据

用法：python3 scripts/classify-meetings.py > /tmp/meeting-classification.tsv
"""

import os
import re

FEISHU_ROOT = '4-Archives/Notes/Feishu/云空间'

# 分类规则（按优先级排序，先匹配标题再匹配内容）
RULES = [
    (['新太', '新钢联', '料棚', '卸料', '上料', '铲车', '堆垛', '料坑', '叫号', '倒运'], '新太定位', '1-Projects/Work/内蒙新太/会议纪要/'),
    (['广州机场', '综合定位', 'A域', 'B域', '巡检app', '电子围栏', '手推车', 'AESB', 'TCDM', '白云机场', '白云信科', '三标段'], '广州机场', '1-Projects/Work/广州机场/会议纪要/'),
    (['上港', '仓储', '出入库', 'Fishbowl', 'RFID判断'], '上港项目', '1-Projects/Work/上港仓储管理/会议纪要/'),
    (['南宁机场', '无动力设备', '车载定位'], '南宁机场', '1-Projects/Work/南宁机场/会议纪要/'),
    (['武汉机场', '商铺'], '武汉机场', '4-Archives/Projects/Work/武汉机场/会议纪要/'),
    (['洛阳石化', '洛阳化工'], '洛阳石化', '4-Archives/Projects/Work/洛阳石化/会议纪要/'),
    (['赛峰', 'ADFS', 'SAML'], '赛峰项目', '4-Archives/Projects/Work/赛峰/会议纪要/'),
    (['研发部的视频会议', 'Video meeting—研发部'], '研发部周会', '2-Areas/Work/团队管理/周会纪要/研发部/'),
    (['项目部的视频会议', 'Video meeting—项目部'], '项目部周会', '2-Areas/Work/团队管理/周会纪要/项目部/'),
    (['刘秉欣'], '项目进度会', '2-Areas/Work/团队管理/周会纪要/'),
]

# 内容关键词（用于标题无法判断时读取内容）
CONTENT_RULES = [
    (['新太', '新钢联', '料棚', '卸料', '上料', '铲车', '堆垛', '料坑', '叫号', '倒运', '卸货'], '新太定位', '1-Projects/Work/内蒙新太/会议纪要/'),
    (['广州机场', '综合定位', 'A域', 'B域', '电子围栏', '手推车', 'AESB', 'TCDM', '白云', '三标段', '深化设计', '陪伴运行'], '广州机场', '1-Projects/Work/广州机场/会议纪要/'),
    (['上港', '仓储物流', '出入库', 'RFID'], '上港项目', '1-Projects/Work/上港仓储管理/会议纪要/'),
    (['南宁机场', '无动力设备', '车载定位'], '南宁机场', '1-Projects/Work/南宁机场/会议纪要/'),
    (['武汉机场'], '武汉机场', '4-Archives/Projects/Work/武汉机场/会议纪要/'),
    (['洛阳石化', '洛阳化工'], '洛阳石化', '4-Archives/Projects/Work/洛阳石化/会议纪要/'),
    (['Beacon', 'CLE', 'launchable', '墨水屏', 'MQTT', '定位引擎'], '技术讨论', '3-Resources/Tech/问题解决/'),
    (['平台版本', '前端更新', '后端更新', '版本发布'], '产品研发', '2-Areas/Work/产品研发/会议纪要/'),
]

SKIP_PATTERNS = ['近期会议速递', '月度纪要小结']

def classify_file(filepath, filename):
    # 跳过飞书 AI 汇总
    for skip in SKIP_PATTERNS:
        if skip in filename:
            return '留归档（AI汇总）', '', f'飞书 AI 汇总'

    # 标题匹配
    for keywords, category, target in RULES:
        for kw in keywords:
            if kw in filename:
                return category, target, f'标题含"{kw}"'

    # 读取内容匹配
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read(5000)
        if '---' in content:
            parts = content.split('---', 2)
            if len(parts) >= 3:
                content = parts[2]
    except:
        return '无法读取', '', '文件读取失败'

    for keywords, category, target in CONTENT_RULES:
        for kw in keywords:
            if kw in content:
                return category, target, f'内容含"{kw}"'

    return '待确认', '', '无法自动分类，需人工判断'

def main():
    results = []
    for root, dirs, files in os.walk(FEISHU_ROOT):
        for fname in sorted(files):
            if fname in ('README.md', '.DS_Store'):
                continue
            is_meeting = any(p in fname for p in [
                'Video meeting', '视频会议', '智能纪要', '文字记录',
                '近期会议速递', '月度纪要小结'
            ])
            if not is_meeting:
                continue
            filepath = os.path.join(root, fname)
            category, target, reason = classify_file(filepath, fname)
            results.append((filepath, fname, category, target, reason))

    # 统计
    from collections import Counter
    cats = Counter(r[2] for r in results)
    print('=== 分类统计 ===', flush=True)
    for cat, count in cats.most_common():
        print(f'  {count:3d} | {cat}', flush=True)
    print(f'  ---', flush=True)
    print(f'  {len(results):3d} | 总计', flush=True)
    print(flush=True)

    # 详细列表
    print('文件名\t分类\t目标路径\t判断依据', flush=True)
    for filepath, fname, category, target, reason in results:
        short_path = filepath.replace('4-Archives/Notes/Feishu/云空间/', '')
        print(f'{short_path}\t{category}\t{target}\t{reason}', flush=True)

if __name__ == '__main__':
    main()
