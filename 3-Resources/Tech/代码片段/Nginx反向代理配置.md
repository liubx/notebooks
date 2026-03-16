---
title: Nginx反向代理配置（Notion迁移）
type: code-snippet
language: nginx
tags:
  - code-snippet
  - 技术/运维/Nginx
source: "[[4-Archives/Notion/技术相关/Nginx配置 19d5e7a33a544564a81a0118f870fae0]]"
created: 2026-03-16
---

> 参考工具：[nginx playground](https://nginx-playground.wizardzines.com/)

```nginx
worker_processes  1;
worker_rlimit_nofile 8192;

events {
  worker_connections  4096;
}

http {
  include    /etc/nginx/mime.types;
  index    index.html index.htm index.php;

  server {
    listen          80;
    server_name     http.bin;
    access_log      /dev/null;

    location / {
      proxy_pass      http://localhost:7777;
    }

    # 静态文件按服务分目录
    location ~ ^/static/(public|management-service|map-service|position-service|device-service)/(.+)$ {
      alias /opt/static/$1/$2;
    }
  }
}
```
