---
title: K8S集群部署配置（Notion迁移）
type: code-snippet
language: yaml
tags:
  - code-snippet
  - 技术/运维/K8S
source: "[[4-Archives/Notion/莱讯科技/集群部署相关 c41a2518af6f405cb0c5b960fa27220f]]"
created: 2026-03-16
---

> 与 [[K3S集群部署]] 互补，本文为实际项目中的 K8S 部署配置模板。

## NodePort Service

```yaml
apiVersion: v1
kind: Service
metadata:
  name: demo-node-port
  namespace: mid-dev
spec:
  ports:
  - name: 6666-6666-tcp
    nodePort: 30600
    port: 6666
    protocol: TCP
    targetPort: 6666
  type: NodePort
```

## Deployment 模板（中间件对接服务）

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: demo-middleware
  namespace: mid-dev
spec:
  replicas: 1
  template:
    spec:
      containers:
      - env:
        - name: ACTIVE_PROFILES
          value: dev
        - name: RABBITMQ_SERVER
          value: rabbitmq
        - name: RABBITMQ_PORT
          value: "5672"
        - name: API_ENDPOINT
          value: http://gateway.saas-dev:8080
        - name: WEBSOCKET_ENDPOINT
          value: ws://gateway.saas-dev:8080
        - name: CLIENT_ID
          value: demo_client
        - name: CLIENT_SECRET
          value: "[secret]"
        resources:
          limits:
            cpu: 500m
            memory: 1Gi
          requests:
            cpu: 250m
            memory: 256Mi
      imagePullSecrets:
      - name: registrykey
```


# Yuque 补充内容

## Helm 安装

### Helm v3

```bash
curl -O https://get.helm.sh/helm-v3.2.4-linux-amd64.tar.gz
tar xzvf helm-v3.2.4-linux-amd64.tar.gz

# 或使用国内镜像
curl -O https://resource-1300645485.cos.ap-chengdu.myqcloud.com/download/helm-v3.7.2-linux-amd64.tar.gz
tar xzvf helm-v3.7.2-linux-amd64.tar.gz

sudo cp linux-amd64/helm /usr/bin/helm
```

### Helm v2

```bash
curl -O https://get.helm.sh/helm-v2.11.0-linux-amd64.tar.gz
tar xzvf helm-v2.11.0-linux-amd64.tar.gz
sudo cp linux-amd64/helm /usr/bin/helm

# Tiller + Client
helm init --upgrade --service-account tiller -i hub.tencentyun.com/helm/tiller:v2.11.0

kubectl create serviceaccount --namespace kube-system tiller
kubectl create clusterrolebinding tiller-cluster-rule --clusterrole=cluster-admin --serviceaccount=kube-system:tiller

# Client only
helm init --client-only --upgrade --service-account tiller -i hub.tencentyun.com/helm/tiller:v2.11.0
```

## Harbor 安装

```bash
helm repo add harbor https://helm.goharbor.io

helm install harbor harbor/harbor --namespace harbor \
  --set expose.ingress.hosts.core=registry.example.com \
  --set expose.ingress.hosts.notary=notary.example.com \
  --set expose.tls.certSource=secret \
  --set expose.tls.secret.secretName=harbor-tls \
  --set expose.tls.secret.notarySecretName=notary-tls \
  --set persistence.enabled=true \
  --set externalURL=https://registry.example.com \
  --set harborAdminPassword=[password] \
  --set expose.ingress.annotations."kubernetes\.io/ingress\.class"=nginx \
  --set expose.ingress.annotations."kubernetes\.io/tls-acme"=\"true\" \
  --set persistence.persistentVolumeClaim.registry.storageClass=cfs \
  --set persistence.persistentVolumeClaim.chartmuseum.storageClass=cfs \
  --set persistence.persistentVolumeClaim.jobservice.storageClass=cfs \
  --set persistence.persistentVolumeClaim.database.storageClass=cfs \
  --set persistence.persistentVolumeClaim.redis.storageClass=cfs \
  --set persistence.persistentVolumeClaim.trivy.storageClass=cfs
```

## Rancher 安装

```bash
helm repo add rancher-stable https://releases.rancher.com/server-charts/stable
kubectl create namespace cattle-system

# 使用 Let's Encrypt（需要安装 cert-manager）
helm install rancher rancher-stable/rancher \
  --namespace cattle-system \
  --set hostname=rancher.example.com \
  --set ingress.tls.source=letsEncrypt \
  --set letsEncrypt.email=admin@example.com

# 使用自签名证书
helm install rancher rancher-stable/rancher \
  --namespace cattle-system \
  --set hostname=rancher.example.com

# 使用已有 Secret
helm install rancher rancher-stable/rancher \
  --namespace cattle-system \
  --set hostname=rancher.example.com \
  --set ingress.tls.source=secret
```

## cert-manager 安装

```bash
kubectl create namespace cert-manager
helm repo add jetstack https://charts.jetstack.io
helm repo update

# Helm v3+ 自动配置
helm install cert-manager jetstack/cert-manager \
  --namespace cert-manager \
  --create-namespace \
  --version v1.6.1 \
  --set installCRDs=true \
  --set ingressShim.defaultIssuerName=letsencrypt-prod \
  --set ingressShim.defaultIssuerKind=ClusterIssuer \
  --set ingressShim.defaultIssuerGroup=cert-manager.io

# 验证
kubectl get pods --namespace cert-manager
```

### ClusterIssuer 配置

```yaml
# letsencrypt-prod.yaml
apiVersion: cert-manager.io/v1
kind: ClusterIssuer
metadata:
  name: letsencrypt-prod
spec:
  acme:
    email: admin@example.com
    server: https://acme-v02.api.letsencrypt.org/directory
    privateKeySecretRef:
      name: letsencrypt-prod
    solvers:
    - http01:
        ingress:
          class: nginx
```

### Ingress TLS 配置

```yaml
annotations:
  kubernetes.io/ingress.class: nginx
  kubernetes.io/tls-acme: "true"
  nginx.ingress.kubernetes.io/force-ssl-redirect: "false"
  nginx.ingress.kubernetes.io/ssl-redirect: "false"

tls:
- hosts:
  - example.com
  secretName: example-tls
```

## nginx-ingress 安装

```bash
helm repo add ingress-nginx https://kubernetes.github.io/ingress-nginx
helm install ingress-nginx ingress-nginx/ingress-nginx
```

## MinIO 安装

```bash
kubectl create namespace minio
helm repo add minio https://charts.min.io/
helm repo update

helm install minio --namespace minio \
  --set rootUser=admin \
  --set rootPassword=[password] \
  --set persistence.existingClaim=volume \
  --set persistence.storageClass=cfs \
  --set mode=standalone \
  --set resources.requests.memory=2Gi \
  --set environment.MINIO_SERVER_URL=https://minio.example.com \
  --set environment.MINIO_BROWSER_REDIRECT_URL=https://console.minio.example.com \
  minio/minio
```

### MinIO Ingress

```yaml
apiVersion: networking.k8s.io/v1beta1
kind: Ingress
metadata:
  namespace: minio
  name: minio
  annotations:
    kubernetes.io/ingress.class: "nginx"
    kubernetes.io/tls-acme: "true"
    nginx.ingress.kubernetes.io/proxy-body-size: "0"
spec:
  rules:
  - host: minio.example.com
    http:
      paths:
      - path: /
        backend:
          serviceName: minio
          servicePort: 9000
  tls:
  - hosts:
    - minio.example.com
    secretName: minio-tls
```

## Longhorn 安装

```bash
# 需要在每个主机安装
yum install -y iscsi-initiator-utils
```

## 连接 Kubernetes

```bash
mkdir ~/.kube
vi ~/.kube/config
chmod o-r ~/.kube/config
chmod g-r ~/.kube/config

kubectl config get-contexts
kubectl config use-context [context-name]
kubectl get node
```

---
*来源：语雀 - 莱讯科技技术分享/服务器相关文档/Kubernetes文档*
