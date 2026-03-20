---
title: OpenClash 代理配置
type: code-snippet
language: yaml
tags:
  - tech/网络
  - tech/代理
source: "[[4-Archives/Notion/莱讯科技/OpenClash b7f7dcaf807c4cc98961ef0daf778e43]]"
created: 2026-03-16
---

> 与 [[Surge代理配置]] 互补，本文为 OpenClash/Clash 格式。

```yaml
proxies:
- name: OFFICE-PROXY
  type: vmess
  server: vpn.example.net
  port: 9443
  uuid: [uuid]
  alterId: 100
  cipher: auto
  udp: true
  tls: false

- name: LA-PROXY
  type: vless
  server: la.example.com
  port: 443
  uuid: [uuid]
  udp: true
  tls: true
  network: ws
  ws-opts:
    path: "/proxyws"

- name: SFO-PROXY
  type: trojan
  server: proxy.example.com
  port: 443
  password: '[password]'
  udp: true
  network: ws
  ws-opts:
    path: "/ws"
    headers:
      Host: proxy.example.com

proxy-groups:
  - name: ABROAD-PROXY
    type: url-test
    proxies:
      - SFO-PROXY
      - LA-PROXY
    interval: 300

rule-providers:
  apple-proxy:
    type: http
    behavior: classical
    url: https://cdn.jsdelivr.net/gh/Hackl0us/SS-Rule-Snippet@master/Rulesets/Clash/Basic/Apple-proxy.yaml
    path: "./ruleset/Apple-proxy.yaml"
  cn:
    type: http
    behavior: classical
    url: https://cdn.jsdelivr.net/gh/Hackl0us/SS-Rule-Snippet@master/Rulesets/Clash/Basic/CN.yaml
    path: "./ruleset/CN.yaml"
  foreign:
    type: http
    behavior: classical
    url: https://cdn.jsdelivr.net/gh/Hackl0us/SS-Rule-Snippet@master/Rulesets/Clash/Basic/foreign.yaml
    path: "./ruleset/foreign.yaml"

rules:
- IP-CIDR,192.168.50.0/24,OFFICE-PROXY,no-resolve
- DOMAIN-SUFFIX,example.net,OFFICE-PROXY
- RULE-SET,apple-proxy,ABROAD-PROXY
- RULE-SET,cn,DIRECT
- RULE-SET,foreign,ABROAD-PROXY
- GEOIP,CN,DIRECT
- MATCH,ABROAD-PROXY
```
