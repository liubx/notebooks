---
title: Docker 安装配置
type: code-snippet
tags:
  - tech/docker
  - tech/运维
created: 2022-01-01
modified: 2022-01-01
---

# Docker 安装配置（CentOS）

```bash
yum update -y
yum remove docker docker-client docker-client-latest docker-common docker-latest docker-latest-logrotate docker-logrotate docker-engine
yum install -y yum-utils
yum-config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo
yum install docker-ce docker-ce-cli containerd.io
systemctl enable docker
systemctl start docker
```

## 配置镜像仓库

```json
// /etc/docker/daemon.json
{
  "registry-mirrors": [
    "https://nexus-registry.reliablesense.cn"
  ]
}
```

```bash
systemctl restart docker
```
