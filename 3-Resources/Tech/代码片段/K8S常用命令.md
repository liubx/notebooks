---
title: K8S 常用命令
type: code-snippet
tags:
  - tech/k8s
  - tech/运维
created: 2023-01-01
modified: 2023-01-01
---

# K8S 常用命令

## 重启 Deployment

```bash
kubectl rollout restart deployment -n biz relay-stable
kubectl rollout restart deployment -n biz position-stable
kubectl rollout restart statefulset -n iaas rabbitmq
```

## 编辑 Deployment

```bash
kubectl edit deployments.apps -n mid jiguang-bluetooth-stable
```

## 编辑 ConfigMap

```bash
kubectl edit configmaps -n mid jiguang-bluetooth-env-config
```

## 查看日志

```bash
kubectl logs -n mid jiguang-bluetooth-stable-dd957b677-cd82g -f | grep "f0c8a9a2"
```

## Redis 批量删除

```bash
redis-cli KEYS "*" | xargs redis-cli DEL
redis-cli KEYS "*052110900993*" | xargs redis-cli DEL
redis-cli KEYS "*052110900993*" | xargs redis-cli unlink
```

## Docker 运行 ginrtsp

```bash
docker run -d --restart=unless-stopped \
  -p 3000:3000 --name ginrtso \
  -v //c/Users/陆东/ginrtsp/config.yaml:/opt/config/config.yaml \
  nexus-registry-releases.reliablesense.cn/online-biz-ginrtsp:v2.0.0-SH
```

## socat 端口转发

```bash
socat -d -d TCP-LISTEN:10002,fork,reuseaddr TCP:192.168.50.70:10002
socat -d -d TCP-LISTEN:7487,fork,reuseaddr TCP:172.20.160.121:7487
```


## K8S Ingress 配置示例（MinIO）

```yaml
apiVersion: networking.k8s.io/v1beta1
kind: Ingress
metadata:
  namespace: minio
  name: minio-console
  annotations:
    kubernetes.io/ingress.class: "nginx"
    kubernetes.io/tls-acme: "true"
    nginx.ingress.kubernetes.io/force-ssl-redirect: "false"
    nginx.ingress.kubernetes.io/ssl-redirect: "false"
spec:
  rules:
  - host: console.minio.reliablesense.cn
    http:
      paths:
      - path: /
        backend:
          serviceName: minio-console
          servicePort: 9001
  tls:
  - hosts:
    - console.minio.reliablesense.cn
    secretName: minio-console-tls
```

## Helm MinIO 部署

```bash
helm repo add minio https://charts.min.io/

helm install minio --namespace minio \
  --set rootUser=admin \
  --set rootPassword=secret123456 \
  --set persistence.existingClaim=volume \
  --set persistence.storageClass=cfs \
  --set mode=standalone \
  --set resources.requests.memory=2Gi \
  minio/minio

helm uninstall minio
```

## K8S Prometheus 部署

```bash
helm install kube-prometheus prometheus-community/kube-prometheus-stack \
  -n monitoring --debug

helm uninstall kube-prometheus -n monitoring

# 清理 CRD
kubectl delete crd alertmanagerconfigs.monitoring.coreos.com
kubectl delete crd alertmanagers.monitoring.coreos.com
kubectl delete crd podmonitors.monitoring.coreos.com
kubectl delete crd probes.monitoring.coreos.com
kubectl delete crd prometheuses.monitoring.coreos.com
kubectl delete crd prometheusrules.monitoring.coreos.com
kubectl delete crd servicemonitors.monitoring.coreos.com
kubectl delete crd thanosrulers.monitoring.coreos.com
```

## 坐标转换 SQL

```sql
SELECT geom, geoc_gcj02towgs84(ST_Transform(geom,3857)), ST_SRID(ST_Transform(geom,3857))
FROM reliablesense_demo.t_scenegraph;
```
