# Helm Minio

```bash
helm install minio --namespace minio --set rootUser=admin --set rootPassword=secret123456 --set persistence.existingClaim=volume --set persistence.storageClass=cfs --set mode=standalone --set resources.requests.memory=2Gi minio/minio
```