---
title: Kubectl常用命令（Notion迁移）
type: code-snippet
language: bash
tags:
  - code-snippet
  - 技术/运维/K8S
source: "[[4-Archives/Notion/技术相关/Kubectl 相关指令 dd61c2f1d5b54afc9a1b8f9a90383153]]"
created: 2026-03-16
---

> 从 Notion 迁移，与 [[K8S常用命令]] 互补，本文侧重实际项目中的具体命令。

## 查看资源

```bash
kubectl get ingressroute -n biz
kubectl get pod -n iaas
kubectl get pod -n biz
kubectl get deployments -n biz -o wide
kubectl get events -A -o custom-columns=LastSeen:.lastTimestamp,Count:.count,From:.source.component,Type:.type,Reason:.reason,Message:.message
```

## 重启服务

```bash
# Deployment
kubectl rollout restart deployment admin-stable -n biz
kubectl rollout restart deployment map-mobile-stable -n biz
kubectl rollout restart deployment position-stable -n biz

# StatefulSet
kubectl rollout restart statefulset -n iaas rabbitmq
kubectl rollout restart statefulset -n iaas timescaledb
kubectl rollout restart statefulset -n iaas postgresql-primary
```

## 端口转发

```bash
# Release
kubectl port-forward -n iaas service/postgresql-primary --address 0.0.0.0 15432:5432
kubectl port-forward -n iaas service/timescaledb --address 0.0.0.0 25432:5432

# Master
kubectl port-forward -n iaas service/postgresql-primary --address 0.0.0.0 35432:5432
kubectl port-forward -n iaas service/timescaledb --address 0.0.0.0 45432:5432
```

## 容器操作

```bash
kubectl exec -it -n biz map-stable-66cd5cdf9f-dlrb6 -- sh
kubectl exec -it -n iaas redis-stable-694c6f495-9xk2r -- sh
kubectl exec -it -n iaas postgresql-primary-0 -- sh
redis-cli flushall
```

## 镜像更新

```bash
kubectl set image -n biz deployment/admin-stable admin=nexus-registry-releases.reliablesense.cn/online-biz-admin:v1.4.17-ltxx_czxm-OEM
kubectl set image -n biz deployment/map-mobile-stable map-mobile=nexus-registry-releases.reliablesense.cn/online-biz-map-mobile:v1.3.11-ltxx_czxm-OEM
```

## 扩缩容

```bash
kubectl scale deployment position-stable --replicas=2 -n biz
kubectl describe deployment position-stable -n biz
kubectl edit hpa position-hpa -n biz
```
