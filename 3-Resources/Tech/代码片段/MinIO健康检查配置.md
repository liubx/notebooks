---
title: MinIO 健康检查配置
type: code-snippet
tags:
  - tech/k8s
  - tech/minio
created: 2025-01-01
modified: 2025-01-01
---

# MinIO K8S 健康检查配置

```yaml
imagePullPolicy: IfNotPresent
livenessProbe:
  failureThreshold: 5
  httpGet:
    path: /minio/health/live
    port: minio-api
    scheme: HTTP
  initialDelaySeconds: 5
  periodSeconds: 5
  successThreshold: 1
  timeoutSeconds: 5
readinessProbe:
  failureThreshold: 5
  initialDelaySeconds: 5
  periodSeconds: 5
  successThreshold: 1
  tcpSocket:
    port: minio-api
  timeoutSeconds: 1
```
