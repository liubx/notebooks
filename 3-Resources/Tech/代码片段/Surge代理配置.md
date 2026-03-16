---
title: Surge 代理配置
type: code-snippet
tags:
  - tech/网络
  - tech/surge
created: 2023-01-01
modified: 2023-01-01
---

# Surge 代理配置

```yaml
proxies:
  - name: OFFICE-SNELL
    type: snell
    server: vpn.reliablesense.net
    port: 8761
    psk: 76Cs33vgnJCL3zvPgrQ4sn58YThX4H5
    version: '2'
    obfs-opts:
      mode: http
      host: bing.com
  - name: OFFICE-V2RAY
    type: vmess
    server: vpn.reliablesense.net
    port: 9443
    uuid: 48de7622-a2e1-492f-bc4c-73109e5fbbed
    alterId: 100
    cipher: auto
    udp: true
    skip-cert-verify: true
    tls: false
  - name: PROXY
    type: trojan
    server: proxy.liubx1988.com
    port: 443
    password: '1357924680'
    udp: true
    skip-cert-verify: false
    network: ws
    ws-opts:
      path: "/ws"
      headers:
        Host: proxy.liubx1988.com
```
