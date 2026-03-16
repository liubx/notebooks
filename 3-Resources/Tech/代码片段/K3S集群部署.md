---
title: K3S 集群部署
type: code-snippet
tags:
  - tech/k3s
  - tech/运维
created: 2025-01-01
modified: 2025-01-01
---

# K3S 集群部署步骤

## 磁盘初始化

```bash
lsblk
parted /dev/vdb
mklabel gpt
mkpart primary 2048s 100%
mkfs -t ext4 /dev/vdb1
mkdir /data
mount /dev/vdb1 /data
ls -l /dev/disk/by-uuid/
vi /etc/fstab
# UUID=xxx /data ext4 defaults 0 2
mount -a
```

## 系统配置

```bash
systemctl disable firewalld --now
modprobe overlay
modprobe br_netfilter

tee /etc/sysctl.d/kubernetes.conf<<EOF
net.bridge.bridge-nf-call-ip6tables = 1
net.bridge.bridge-nf-call-iptables = 1
net.ipv4.ip_forward = 1
EOF

sysctl --system
reboot
```

## K3S Agent 安装

```bash
mkdir -p /etc/rancher/k3s
mkdir -p /opt/reliablesense

# 复制配置文件到新节点
scp /opt/reliablesense/k3s_install.sh root@<NODE_IP>:/opt/reliablesense/
scp /etc/rancher/k3s/config.yaml root@<NODE_IP>:/etc/rancher/k3s/
scp /etc/rancher/k3s/registries.yaml root@<NODE_IP>:/etc/rancher/k3s/
scp /usr/local/bin/k3s root@<NODE_IP>:/usr/local/bin/

chmod +x /opt/reliablesense/k3s_install.sh
chmod +x /usr/local/bin/k3s

# 安装 agent
INSTALL_K3S_SKIP_DOWNLOAD=true INSTALL_K3S_SKIP_SELINUX_RPM=true \
  INSTALL_K3S_SELINUX_WARN=true K3S_TOKEN=<TOKEN> \
  K3S_URL=https://<MASTER_IP>:6443 /opt/reliablesense/k3s_install.sh
```

## 数据目录迁移到 /data

```bash
/usr/local/bin/k3s-killall.sh
mkdir -p /data/k3s/ /data/k3s-pods/ /data/k3s-rancher/
mv /run/k3s/ /data/k3s/
mv /var/lib/kubelet/pods/ /data/k3s-pods/
mv /var/lib/rancher/ /data/k3s-rancher/
ln -s /data/k3s/ /run/k3s
ln -s /data/k3s-pods/ /var/lib/kubelet/pods
ln -s /data/k3s-rancher/ /var/lib/rancher
systemctl daemon-reload
systemctl start k3s
```

## K3S Agent 重装

```bash
# 备份
cp -rp /etc/rancher/k3s /opt/reliablesense/k3s
cp -p /usr/local/bin/k3s /opt/reliablesense/k3s/

# 卸载
/usr/local/bin/k3s-agent-uninstall.sh
rm -rf /run/k3s /var/lib/kubelet/pods /var/lib/rancher
rm -rf /data/k3s /data/k3s-pods/ /data/k3s-rancher/

# 重新安装
mkdir -p /etc/rancher/k3s
cp -p k3s/config.yaml /etc/rancher/k3s/
cp -p k3s/registries.yaml /etc/rancher/k3s/
cp -p k3s/k3s /usr/local/bin/
chmod +x /usr/local/bin/k3s
chmod +x /opt/reliablesense/k3s_install.sh

INSTALL_K3S_SKIP_DOWNLOAD=true INSTALL_K3S_SKIP_SELINUX_RPM=true \
  INSTALL_K3S_SELINUX_WARN=true K3S_TOKEN=<TOKEN> \
  K3S_URL=https://<MASTER_IP>:6443 /opt/reliablesense/k3s_install.sh
```

## 导出 K8S 资源

```bash
# Deployment
kubectl get deployment <name> -n biz -o yaml > <name>-deploy.yaml

# Service
kubectl get service <name> -n biz -o yaml > <name>-svc.yaml

# ConfigMap
kubectl get configmap <name>-configmap -n biz -o yaml > <name>-config.yaml

# IngressRoute
kubectl get ingressroute ingress-<name> -n biz -o yaml > <name>-ingress.yaml

# 导出镜像
ctr images export <name>.tar <registry>/<image>:<tag>

# 批量导入镜像
for image in $(ls | grep tar); do ctr image import "$image"; done
```


## K3S 数据目录软链接（2022 早期版本）

```bash
mkdir -p /data/run/k3s
ln -s /data/run/k3s /run/k3s

mkdir -p /var/lib/kubelet
mkdir -p /data/var/lib/kubelet/pods
ln -s /data/var/lib/kubelet/pods /var/lib/kubelet/pods

mkdir -p /data/var/lib/rancher
ln -s /data/var/lib/rancher /var/lib/rancher
```
