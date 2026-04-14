#!/usr/bin/env python3
"""生成会议纪要分类的完整 markdown 表格，插入迁移方案"""
import os, re

# 手动分类 36 个待确认文件（基于标题+时间段推断）
MANUAL_CLASSIFY = {
    '五人工作安排与系统问题会议': '新太项目',
    '导航程序测试问题研讨会': '新太项目',
    '平板使用问题及解决措施研讨': '新太项目',
    '跑步速度与通知次数安排会议': '新太项目',
    '项目服务、权限及工作进展会议': '新太项目',
    '项目工作进展与规划会议纪要': '新太项目',
    '王宗光的视频会议': '新太项目',
    '陈子杰的视频会议': '新太项目',
    '接口、登录及缓存相关问题研讨': '产品研发',
    '会议研讨多项工作进展情况': '产品研发',
    '数据修改、卡顿及操作异常讨论': '产品研发',
    '数据、页面状态及功能处理会议': '产品研发',
    '多方面业务问题及解决方案探讨会': '产品研发',
    '总线接口问题沟通与反馈会议': '广州机场',
    '上海东海模型修复及接入方案研讨': '广州机场',
    '黄佳琪软件工作安排及指导会议': '广州机场',
    '平台重启及相关技术问题研讨': '技术讨论',
    '申库、测试及登录存货问题讨论': '上港项目',
    # 何宜峰 10-11月的会议 → 广州机场
    '8084接口、列表及地图问题讨论': '广州机场',
    '数据同步、订阅测试及新数据格式讨论': '广州机场',
    '管理内容、分支及注释问题讨论': '广州机场',
    '管理员数据库表及任务归属问题讨论': '广州机场',
    '项目依赖、日志及硬盘问题会议': '广州机场',
    '分子构建与插件使用安装讨论': '广州机场',
}

TARGET_MAP = {
    '新太项目': '1-Projects/Work/内蒙新太/会议纪要/',
    '广州机场': '1-Projects/Work/广州机场/会议纪要/',
    '上港项目': '1-Projects/Work/上港仓储管理/会议纪要/',
    '武汉机场': '4-Archives/Projects/Work/武汉机场/会议纪要/',
    '洛阳石化': '4-Archives/Projects/Work/洛阳石化/会议纪要/',
    '研发部周会': '2-Areas/Work/团队管理/周会纪要/研发部/',
    '项目部周会': '2-Areas/Work/团队管理/周会纪要/项目部/',
    '项目进度会': '2-Areas/Work/团队管理/周会纪要/',
    '技术讨论': '3-Resources/Tech/问题解决/',
    '产品研发': '2-Areas/Work/产品研发/会议纪要/',
}

# 读取 TSV 分类结果
results = []
with open('1-Projects/Personal/笔记迁移/会议纪要分类结果.tsv', 'r') as f:
    for line in f:
        if line.startswith('文件名\t'):
            break
    for line in f:
        parts = line.strip().split('\t')
        if len(parts) >= 4:
            fp, cat, target, reason = parts[0], parts[1], parts[2], parts[3]
            # 对待确认的应用手动分类
            if cat == '待确认':
                fname = fp.split('/')[-1]
                for topic, new_cat in MANUAL_CLASSIFY.items():
                    if topic in fname:
                        cat = new_cat
                        target = TARGET_MAP.get(new_cat, '')
                        reason = f'根据标题和时间段推断'
                        break
            results.append((fp, cat, target, reason))

# 获取飞书链接
def get_url(filepath):
    full = f'4-Archives/Notes/Feishu/云空间/{filepath}'
    if not os.path.exists(full): return ''
    try:
        with open(full, 'r') as f:
            m = re.search(r'feishu_url:\s*"([^"]+)"', f.read(500))
            return m.group(1) if m else ''
    except: return ''

# 按分类分组
from collections import defaultdict
groups = defaultdict(list)
for fp, cat, target, reason in results:
    groups[cat].append((fp, target, reason))

# 输出
order = ['新太项目', '广州机场', '上港项目', '武汉机场', '洛阳石化',
         '研发部周会', '项目部周会', '项目进度会', '技术讨论', '产品研发',
         '待确认', '留归档（AI汇总）']

output = []
for cat in order:
    if cat not in groups: continue
    items = sorted(groups[cat], key=lambda x: x[0])
    output.append(f'#### {cat}（{len(items)} 个）\n')
    if cat == '留归档（AI汇总）':
        output.append(f'> 近期会议速递、月度纪要小结等飞书 AI 生成的汇总，共 {len(items)} 个，留归档不动。\n')
        continue
    output.append(f'| 文件 | 本地路径 | 飞书链接 | 目标路径 |')
    output.append(f'|------|---------|---------|---------|')
    for fp, target, reason in items:
        fname = fp.split('/')[-1]
        wl = f'4-Archives/Notes/Feishu/云空间/{fp}'
        if wl.endswith('.md'): wl = wl[:-3]
        url = get_url(fp)
        us = f'[飞书]({url})' if url else '见 README'
        ts = f'`{target}`' if target else '待确认'
        output.append(f'| {fname} | [[{wl}]] | {us} | {ts} |')
    output.append('')

# 写入文件
with open('/tmp/meeting-md.txt', 'w') as f:
    f.write('\n'.join(output))

print(f'生成 {len(output)} 行')

# 统计
for cat in order:
    if cat in groups:
        print(f'  {len(groups[cat]):3d} | {cat}')
