# Kubectl 相关指令

```bash

kubectl get ingressroute -n biz

kubectl get pod -n iaas

kubectl get pod -n biz

kubectl get deployments -n biz -o wide

kubectl get events -A -o custom-columns=LastSeen:.lastTimestamp,Count:.count,From:.source.component,Type:.type,Reason:.reason,Message:.message

// 重启
kubectl rollout restart deployment admin-stable -n biz
kubectl rollout restart deployment map-mobile-stable -n biz
kubectl rollout restart deployment relay-stable -n biz
kubectl rollout restart deployment interceptor-stable -n biz
kubectl rollout restart deployment notification-stable -n biz
kubectl rollout restart deployment position-stable -n biz
kubectl rollout restart deployment corelocation-bluetooth-aoa-stable -n mid
kubectl rollout restart statefulset -n iaas rabbitmq
kubectl rollout restart statefulset -n iaas timescaledb
kubectl rollout restart statefulset -n iaas postgresql-primary
kubectl rollout restart statefulset -n biz eureka
kubectl rollout restart deployment -n iaas tile38

// 编辑
kubectl edit deployments.apps -n biz map-mobile-stable

kubectl edit deployments.apps -n biz map-stable

kubectl edit deployments.apps -n biz notification-stable

kubectl edit deployments.apps -n mid amwhere-rtk-stable

kubectl edit statefulsets.apps -n biz eureka

kubectl edit deployments.apps -n biz admin-stable

kubectl edit configmap jiguang-bluetooth-env-config -n mid

kubectl edit deployments.apps -n biz relay-stable

kubectl edit deployments.apps -n biz position-stable

kubectl edit statefulsets.apps -n biz rabbitmq

kubectl edit deployments.apps -n mid jiguang-bluetooth-stable

kubectl edit configmap ordistar-uwb-aoa-env-config -n mid

kubectl rollout restart deployment ordistar-uwb-aoa-stable -n mid

// 映射端口
// release
kubectl port-forward -n iaas service/postgresql-primary --address 0.0.0.0 15432:5432

kubectl port-forward -n iaas service/timescaledb --address 0.0.0.0 25432:5432

// master
kubectl port-forward -n iaas service/postgresql-primary --address 0.0.0.0 35432:5432

kubectl port-forward -n iaas service/timescaledb --address 0.0.0.0 45432:5432

// 进入容器

kubectl exec -it -n biz map-stable-66cd5cdf9f-dlrb6 -- sh

kubectl exec -it -n biz map-stable-66cd5cdf9f-dlrb6 -- sh

kubectl exec -it -n iaas redis-stable-694c6f495-9xk2r -- sh

kubectl exec -it -n iaas postgresql-primary-0 -- sh

// 清空缓存
redis-cli flushall

//日志

kubectl logs -n iaas timescaledb-0 -c timescaledb -f

kubectl logs -n iaas postgresql-primary-0 -c postgresql -f

kubectl logs -n iaas postgresql-priamary-0 -c postgresql-priamary -f

kubectl logs -n iaas rabbitmq-0 -c rabbitmq -f

kubectl logs -n biz position-stable-b97857c7c-fwv2b -f --tail 10000

kubectl logs -n mid corelocation-bluetooth-aoa-stable-75d9b8ffb4-mczsf -f --tail 10000

kubectl apply -k .

// 修改镜像

kubectl set image -n biz deployment/admin-stable admin=nexus-registry-releases.reliablesense.cn/online-biz-admin:v1.4.17-ltxx_czxm-OEM
kubectl set image -n biz deployment/map-mobile-stable map-mobile=nexus-registry-releases.reliablesense.cn/online-biz-map-mobile:v1.3.11-ltxx_czxm-OEM
kubectl set image -n biz deployment/map-stable map=nexus-registry-releases.reliablesense.cn/online-biz-map:v1.2.6-cnnc_qshdz
kubectl set image -n biz deployment/map-stable map=nexus-registry-releases.reliablesense.cn/online-biz-map:v1.2.6-SH

kubectl set image -n biz deployment/position-stable position=nexus-registry-releases.reliablesense.cn/online-biz-position:v2.1.6-SH
kubectl set image -n biz deployment/integration-stable integration=nexus-registry-releases.reliablesense.cn/online-biz-integration:v2.1.1-SH
kubectl set image -n biz deployment/map-stable map=nexus-registry-releases.reliablesense.cn/online-biz-map:v2.1.1-SH
kubectl set image -n biz deployment/map-stable map=nexus-registry-releases.reliablesense.cn/online-biz-map:v2.1.1-SH

kubectl set image -n biz deployment/business-xintai-xintai-stable business-xintai-xintai=nexus-registry-releases.reliablesense.com/online-biz-business:v1.0.6-xintai_xintai-OEM

kubectl scale deployment position-stable --replicas=2 -n biz

kubectl describe deployment position-stable -n biz

kubectl edit hpa position-hpa -n biz
```

## 常用 Kubectl 命令

### 1. 查看资源状态

```bash
# 查看 Ingress 路由
kubectl get ingressroute -n biz

# 查看 Pod
kubectl get pod -n iaas
kubectl get pod -n biz

# 查看 Deployments
kubectl get deployments -n biz -o wide

# 查看事件
kubectl get events -A -o custom-columns=LastSeen:.lastTimestamp,Count:.count,From:.source.component,Type:.type,Reason:.reason,Message:.message
```

### 2. 重启服务

```bash
# Deployment 重启
kubectl rollout restart deployment admin-stable -n biz
kubectl rollout restart deployment map-mobile-stable -n biz
kubectl rollout restart deployment relay-stable -n biz
kubectl rollout restart deployment interceptor-stable -n biz
kubectl rollout restart deployment notification-stable -n biz
kubectl rollout restart deployment position-stable -n biz
kubectl rollout restart deployment corelocation-bluetooth-aoa-stable -n mid

# StatefulSet 重启
kubectl rollout restart statefulset -n iaas rabbitmq
kubectl rollout restart statefulset -n iaas timescaledb
kubectl rollout restart statefulset -n iaas postgresql-primary
kubectl rollout restart statefulset -n biz eureka
kubectl rollout restart deployment -n iaas tile38
```

### 3. 编辑配置

```bash
# 编辑 Deployments
kubectl edit deployments.apps -n biz map-mobile-stable
kubectl edit deployments.apps -n biz map-stable
kubectl edit deployments.apps -n biz notification-stable
kubectl edit deployments.apps -n biz admin-stable
kubectl edit deployments.apps -n biz relay-stable
kubectl edit deployments.apps -n biz position-stable
kubectl edit deployments.apps -n mid amwhere-rtk-stable
kubectl edit deployments.apps -n mid jiguang-bluetooth-stable

# 编辑 StatefulSets
kubectl edit statefulsets.apps -n biz eureka
kubectl edit statefulsets.apps -n biz rabbitmq

# 编辑 ConfigMap
kubectl edit configmap jiguang-bluetooth-env-config -n mid
kubectl edit configmap ordistar-uwb-aoa-env-config -n mid
```

### 4. 端口转发

```bash
# Release 环境
kubectl port-forward -n iaas service/postgresql-primary --address 0.0.0.0 15432:5432
kubectl port-forward -n iaas service/timescaledb --address 0.0.0.0 25432:5432

# Master 环境
kubectl port-forward -n iaas service/postgresql-primary --address 0.0.0.0 35432:5432
kubectl port-forward -n iaas service/timescaledb --address 0.0.0.0 45432:5432
```

### 5. 容器操作

```bash
# 进入容器
kubectl exec -it -n biz map-stable-66cd5cdf9f-dlrb6 -- sh
kubectl exec -it -n iaas redis-stable-694c6f495-9xk2r -- sh
kubectl exec -it -n iaas postgresql-primary-0 -- sh

# 清空 Redis 缓存
redis-cli flushall
```

### 6. 查看日志

```bash
# 查看实时日志
kubectl logs -n iaas timescaledb-0 -c timescaledb -f
kubectl logs -n iaas postgresql-primary-0 -c postgresql -f
kubectl logs -n iaas rabbitmq-0 -c rabbitmq -f
kubectl logs -n biz position-stable-b97857c7c-fwv2b -f --tail 10000
kubectl logs -n mid corelocation-bluetooth-aoa-stable-75d9b8ffb4-mczsf -f --tail 10000
```

### 7. 镜像管理

```bash
# 更新镜像
kubectl set image -n biz deployment/admin-stable admin=nexus-registry-releases.reliablesense.cn/online-biz-admin:v1.4.17-ltxx_czxm-OEM
kubectl set image -n biz deployment/map-mobile-stable map-mobile=nexus-registry-releases.reliablesense.cn/online-biz-map-mobile:v1.3.11-ltxx_czxm-OEM
kubectl set image -n biz deployment/map-stable map=nexus-registry-releases.reliablesense.cn/online-biz-map:v1.2.6-cnnc_qshdz
```

### 8. 扩缩容和检查

```bash
# 扩缩容
kubectl scale deployment position-stable --replicas=2 -n biz

# 检查部署状态
kubectl describe deployment position-stable -n biz

# 编辑 HPA
kubectl edit hpa position-hpa -n biz
```