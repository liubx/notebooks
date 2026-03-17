# Nginx配置

[nginx playground (wizardzines.com)](https://nginx-playground.wizardzines.com/)

```bash
worker_processes  1;
worker_rlimit_nofile 8192;

events {
  worker_connections  4096;
}

http {
  include    /etc/nginx/mime.types;
  index    index.html index.htm index.php;

  server { # reverse proxy for a local httpbin
    listen          80;
    server_name     http.bin;
    access_log      /dev/null;

    location / {
      proxy_pass      http://localhost:7777;
    }
    
    location ~ ^/static/(public|management-service|map-service|position-service|device-service)/(.+)$ {
      alias /opt/static/$1/$2;
  	}
  }
}
```