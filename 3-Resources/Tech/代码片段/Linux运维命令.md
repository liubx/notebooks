---
title: Linux运维命令（Notion迁移）
type: code-snippet
language: bash
tags:
  - tech/linux
  - tech/运维
source: "[[4-Archives/Notion/技术相关/Linux相关指令 4e807713bb61406db430d4f17e348f7c]]"
created: 2026-03-16
---

> 从 Notion 迁移，与 [[Linux防火墙配置]] 互补。

## 常用操作

```bash
# 杀端口进程
fuser -k 8080/tcp

# 切换图形界面
sudo systemctl set-default multi-user.target
sudo systemctl set-default graphical.target

# 压缩/解压
tar xvf gitup-linux-amd64.tar.gz
tar cvf test.tar test/

# 复制保留权限
cp -rp source destination

# rsync 排除目录
rsync -av --progress rsmap-demo demo --exclude node_modules --exclude .umi
```

## 代理

```bash
all_proxy=socks://127.0.0.1:1080 curl -v https://www.google.com
ssh -N -L 5432:localhost:5432 root@82.156.16.18
```

## 网络测试

```bash
# UDP 监听/发送
socat - udp-listen:30090
echo "hello" | socat - udp4-datagram:82.157.96.77:30090

# TCP 监听/发送
socat TCP-LISTEN:80 STDOUT
echo "test" | socat - tcp:localhost:10002

# 抓包
tcpdump port 9000 -v -XX -n
tcpdump -i ens192 udp port 32500 -v
```

## 端口转发

```bash
nc -l -p 8888 -c "nc 192.168.1.100 22"
socat -d -d TCP-LISTEN:7487,fork,reuseaddr TCP:172.20.160.121:7487
```

## MQTT 测试

```bash
sudo yum install -y https://github.com/hivemq/mqtt-cli/releases/download/v4.10.0/mqtt-cli-4.10.0.rpm
mqtt test -h rtk.tulicn.com -p 12347 -u saas -pw [password]
```

## NFS 自动挂载

```bash
# /etc/fstab
nas.example.com:/mnt/Storage /home/user/Storage nfs auto,nofail,noatime,nolock,intr,tcp,actimeo=1800 0 0
```

## Photon 恢复密码

启动时添加 `rw init=/bin/bash`，然后 `passwd` 改密码。
