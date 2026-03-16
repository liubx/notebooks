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
