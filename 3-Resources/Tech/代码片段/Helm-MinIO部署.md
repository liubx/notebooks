---
title: Helm MinIO 部署
type: code-snippet
language: bash
tags:
  - code-snippet
  - 技术/运维/K8S
source: "[[4-Archives/Notion/技术相关/Helm Minio a4c7c9a953314c888a5123848de1cb75]]"
created: 2026-03-16
---

> 与 [[MinIO健康检查配置]] 互补。

```bash
helm install minio \
  --namespace minio \
  --set rootUser=admin \
  --set rootPassword=[password] \
  --set persistence.existingClaim=volume \
  --set persistence.storageClass=cfs \
  --set mode=standalone \
  --set resources.requests.memory=2Gi \
  minio/minio
```
