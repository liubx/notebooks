#!/usr/bin/env python3
"""替换迁移方案中剩余的"见目录 README"为实际飞书链接"""

replacements = {
    '998. 售后项目/README': 'https://reliablesense.feishu.cn/docx/NFOVdlWSFoZJ91xTXMbcvY7mnSg',
    '999. 归档项目/README': 'https://reliablesense.feishu.cn/file/boxcnGCzZKdUb61mgStHtJ2c6Uh',
    '~其他项目/README': 'https://reliablesense.feishu.cn/file/PjlbbXG5QoodTExMXrecEceHnAh',
    '000. 售前项目/README': 'https://reliablesense.feishu.cn/file/Cb6Pb6qJooFni9xK6M0ce7A6nUF',
    '~其他公司方案/README': 'https://reliablesense.feishu.cn/file/boxcnXkEa3B2CHo7RdsBUWYtW8g',
    '品牌手册与logo/README': 'https://reliablesense.feishu.cn/file/KMxvbtPcHodockxg232cNVj6nqh',
    '宣传/README': 'https://reliablesense.feishu.cn/file/XAOPbnGcNoWIlMxfYRfcOk4ange',
    '公司宣传物（公司介绍）/README': 'https://reliablesense.feishu.cn/file/YxtcbEUUqoZRPtxXAD6ch0EEnmc',
    '往期展会资料合集/README': 'https://reliablesense.feishu.cn/file/QdzebrwgjoCuU5xdXyRcMUEjnmh',
    '软著的立项资料/README': 'https://reliablesense.feishu.cn/file/UCrZbeH6Jo4i3oxRYMFcpLwgnjg',
    '人力资源制度/': 'https://reliablesense.feishu.cn/doc/doccnw7E90pRZqZbad9ZqMraele',
}

path = '1-Projects/Personal/笔记迁移/阶段二-飞书归档提取到PARA迁移方案.md'
with open(path, 'r') as f:
    content = f.read()

count = 0
for key, url in replacements.items():
    old = f'| 见目录 README |'
    if key in content:
        # 找到包含这个 key 的行并替换
        lines = content.split('\n')
        for i, line in enumerate(lines):
            if key in line and '见目录 README' in line:
                lines[i] = line.replace('见目录 README', f'[飞书（目录）]({url})')
                count += 1
        content = '\n'.join(lines)

with open(path, 'w') as f:
    f.write(content)

print(f'替换了 {count} 个')
