---
title: DNS 配置
type: code-snippet
tags:
  - tech/网络
  - tech/运维
created: 2022-01-01
modified: 2022-01-01
---

# DNSPod Token

| 项目 | 值 |
|------|-----|
| 名称 | DNSPod |
| ID | 291648 |
| Token | b5e60f304dbf85e72369fce5af65af36 |
| 创建时间 | 2022-02-12 22:51:04 |

# 公共 DNS

```
223.5.5.5, 114.114.114.114
https://doh.pub/dns-query, https://dns.alidns.com/dns-query
```

# SSH 公钥

```
ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDV15hg7BB+huct1xgC+SmMiN7JuD8pEPjExRuZyl/VVuBI2jX2d1w4mwGiEpPc4LPOZf8KSZy5I8AeuZATt0sffW9k/dKZobOi5XD5WWUMhHgts06KFB8h20H5DUz0dTZxE2lgQBk6YGPpn06pmAnp+PudiDHAUZa4UTGqDiXf/osuVGEjGsYG0EoW9GxogvfOxWAdkXr2A2N0KMsSyWw5dI4k2SfSdLe/+W2dw948yg46wfuXH/H2QK8+JeZ3vOo0KHQsKx6KMZmBeBeWDNq24SLr2sN8hmCD+5duXs2RIhen6AeOi9RzuTgI7eMBjSJuL0uheKBlO7nMa3OMqaRJ
```

# NAS 挂载

```bash
nas.liubx1988.com:/mnt/Storage/Familys-Storage/Bingxins-Storage    /home/liubx/Storage    nfs auto,nofail,noatime,nolock,intr,tcp,actimeo=1800 0 0
nas.liubx1988.com:/mnt/Workspace/Familys-Workspace/Bingxins-Workspace    /home/liubx/Workspace    nfs auto,nofail,noatime,nolock,intr,tcp,actimeo=1800 0 0
```
