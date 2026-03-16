---
title: Linux 防火墙配置
type: code-snippet
tags:
  - tech/linux
  - tech/iptables
  - tech/firewalld
created: 2024-01-01
modified: 2024-01-01
---

# Linux 防火墙配置

## firewalld 方式

### 基本操作

```bash
# 查看当前规则
sudo firewall-cmd --zone=public --list-all
firewall-cmd --get-active-zones
firewall-cmd --list-all

# 添加端口
sudo firewall-cmd --permanent --zone=public --add-port=22/tcp
sudo firewall-cmd --permanent --zone=public --add-port=80/tcp
sudo firewall-cmd --permanent --zone=public --add-port=32300/tcp
sudo firewall-cmd --permanent --zone=public --add-port=32500/udp

# 重载
sudo firewall-cmd --reload
```

### 使用 drop zone（只允许指定端口）

```bash
sudo firewall-cmd --set-default-zone=drop
sudo firewall-cmd --permanent --add-rich-rule='rule family="ipv4" source address="10.3.0.0/16" accept'
sudo firewall-cmd --permanent --add-service=ssh
sudo firewall-cmd --runtime-to-permanent
sudo firewall-cmd --reload
```

### 使用 rich-rule 拒绝特定端口

```bash
sudo firewall-cmd --permanent --zone=public --set-target=default
sudo firewall-cmd --permanent --add-rich-rule='rule family="ipv4" port port="9100" protocol="tcp" reject'
sudo firewall-cmd --permanent --add-rich-rule='rule family="ipv4" port port="9115" protocol="tcp" reject'
sudo firewall-cmd --reload
```

## iptables 方式

### 全部 DROP + 白名单

```bash
# 清理旧规则
sudo iptables -F
sudo iptables -X

# 设置默认策略为 DROP
sudo iptables -P INPUT DROP
sudo iptables -P FORWARD DROP
sudo iptables -P OUTPUT DROP

# 允许发送数据到特定 IP
sudo iptables -A OUTPUT -d <目标服务器IP> -j ACCEPT

# 允许接收来自特定 IP 的数据
sudo iptables -A INPUT -s <来源服务器IP> -j ACCEPT

# 允许已建立连接的数据双向通信
sudo iptables -A INPUT -m conntrack --ctstate ESTABLISHED,RELATED -j ACCEPT
sudo iptables -A OUTPUT -m conntrack --ctstate ESTABLISHED -j ACCEPT

# 保存规则
sudo iptables-save > /etc/iptables/rules.v4

# 重启服务
sudo systemctl restart iptables

# 验证
sudo iptables -L -v
```

## 经验总结

多次尝试 firewalld 的不同 zone（public → block → drop）配置防火墙，最终发现：
- `drop` zone 最适合严格限制场景
- 如果 firewalld 配置复杂，可以直接用 iptables 更直观
- 白名单模式：默认 DROP 所有，只放行需要的 IP/端口