---
title: Docker 安装配置
type: code-snippet
tags:
  - tech/docker
  - tech/运维
created: 2022-01-01
modified: 2022-01-01
---

# Docker 安装配置

## Docker 安装配置（CentOS）

```bash
yum update -y
yum remove docker docker-client docker-client-latest docker-common docker-latest docker-latest-logrotate docker-logrotate docker-engine
yum install -y yum-utils
yum-config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo
yum install docker-ce docker-ce-cli containerd.io
systemctl enable docker
systemctl start docker
```

### 配置镜像仓库

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


## Yuque 补充 — 快速安装方式

```bash
sudo yum check-update
curl -fsSL https://get.docker.com/ | sh
sudo systemctl start docker
sudo systemctl status docker
sudo systemctl enable docker
sudo usermod -aG docker development
sudo chmod 666 /var/run/docker.sock
```

### 国内镜像加速

```json
// /etc/docker/daemon.json
{
  "registry-mirrors": [
    "https://hub-mirror.c.163.com",
    "https://mirror.baidubce.com"
  ]
}
```

```bash
sudo systemctl restart docker
```

### Docker Compose 安装

```bash
# 官方地址
sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose

# 国内地址
curl -L https://get.daocloud.io/docker/compose/releases/download/1.29.2/docker-compose-`uname -s`-`uname -m` > /usr/local/bin/docker-compose

sudo chmod +x /usr/local/bin/docker-compose
```

## CentOS 服务器初始设置（Yuque 补充）

### 新建用户

```bash
adduser [username]
passwd [username]
gpasswd -a [username] wheel
```

### 加入 SSH 密钥

```bash
cat ~/.ssh/id_rsa.pub  # 复制密钥

su - [username]
mkdir .ssh
chmod 700 .ssh
vi .ssh/authorized_keys  # 粘贴密钥
chmod 600 .ssh/authorized_keys
```

### 禁用 root 登录

```bash
vi /etc/ssh/sshd_config

# 修改以下配置
PermitRootLogin no
ClientAliveInterval 120
ClientAliveCountMax 15

systemctl reload sshd
```

### 修改 Hostname

```bash
hostnamectl set-hostname [hostname]
```

## 定位服务部署脚本（Yuque 补充）

微服务架构包含：auth（授权）、map（地图）、device（设备）、pos（位置）、sewd（业务）

```bash
# 登录私有镜像仓库
docker login registry.example.com --username [user] --password [password]

# 分别进入各服务文件夹，执行：
./script.sh start     # 启动服务
./script.sh down      # 停止服务
./script.sh restart   # 重启服务
./script.sh backup    # 备份数据
./script.sh restore   # 还原数据
```

---
*来源：语雀 - 莱讯科技技术分享/服务器相关文档*
