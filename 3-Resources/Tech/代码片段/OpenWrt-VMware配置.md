---
title: OpenWrt VMware 配置
type: code-snippet
tags:
  - tech/运维
  - tech/网络
created: 2022-01-01
modified: 2022-01-01
---

# OpenWrt VMware 安装

```bash
vmkfstools -i immortalwrt-x86-64-generic-ext4-combined.vmdk OpenWrt.vmdk -d thin
vmkfstools -X 2048M OpenWrt.vmdk
```
