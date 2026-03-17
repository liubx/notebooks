# Omlox seminar

[http://82.156.16.18:](http://82.156.16.18:8083/)[8083/deephub/v1](http://hub.tec.deepmap.net:8081/deephub/v1)

位置上传接口

[http://82.156.16.18:](http://82.156.16.18:8083/)[8083/deephub/v1](http://hub.tec.deepmap.net:8081/deephub/v1)/providers/locations

```jsx
[
   {
       "position": {
           "type": "Point",
           "coordinates": [
               msg.payload.x,
               msg.payload.y,
               msg.payload.z
           ]
			 },
       "source": "8c72013a-e456-4d7b-b5c6-33c40260de4c",
       "floor": 4,
       "provider_type": "unknown",
       "provider_id": msg.payload.id,
       "timestamp_generated": 1698985247000,
       "crs": "local",
       "course": 0,
       "properties": { "tagName": msg.payload.mapId }
	 }
]
```

Deephub 

**Container Runtime**

docker

```jsx
kubelet --> docker shim （在 kubelet 进程中） --> dockerd --> containerd
```

containerd

```jsx
kubelet --> cri plugin（在 containerd 进程中） --> containerd
```

Call Chain of docker is longer

1. **Docker**:
    - **Role**: Docker is a comprehensive container platform that provides a container engine, a high-level API, a command-line interface (CLI), and a complete ecosystem for building, packaging, distributing, and running containers.
    - **Features**: Docker includes features for building container images, managing container lifecycles, configuring networking, and more. It has a user-friendly CLI and graphical user interface (GUI).
2. **containerd**:
    - **Role**: containerd is a core container runtime that focuses on the basic functionality of container execution, image transfer, and storage. It is designed to be lightweight and interoperable with other container orchestration systems.
    - **Features**: containerd provides essential container runtime features, such as container lifecycle management, image distribution, and storage handling. It is not as feature-rich as Docker but is designed to be embedded into higher-level container platforms.

k3s

1. lightweight of Kubernetes, which provide a cluster for automates the deployment, scaling, and management of containerized applications
2. easily expand multiple  server to support more device 

we usually install it in 

iaas - base Infrastructure

database / redis and rabbitmq

biz - bussiness

oam - Operation and maintenance infrastructure

[容器服务 如何选择 Containerd 和 Docker-常见问题-文档中心-腾讯云 (tencent.com)](https://cloud.tencent.com/document/product/457/35747)