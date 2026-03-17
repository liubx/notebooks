# OpenClash

```bash
proxies:
- name: OFFICE-PROXY
  type: vmess
  server: vpn.reliablesense.net
  port: 9443
  uuid: 48de7622-a2e1-492f-bc4c-73109e5fbbed
  alterId: 100
  cipher: auto
  udp: true
  skip-cert-verify: true
  tls: false
- name: LA-PROXY
  type: vless
  server: la.liubx1988.com
  port: 443
  uuid: 77b69f18-85f0-4222-9e6e-92ea02637285
  udp: true
  skip-cert-verify: true
  tls: true
  network: ws
  ws-opts:
    path: "/proxyws"
- name: SFO-PROXY
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
    interval: 3600
  apple-direct:
    type: http
    behavior: classical
    url: https://cdn.jsdelivr.net/gh/Hackl0us/SS-Rule-Snippet@master/Rulesets/Clash/Basic/Apple-direct.yaml
    path: "./ruleset/Apple-direct.yaml"
    interval: 3600
  cn:
    type: http
    behavior: classical
    url: https://cdn.jsdelivr.net/gh/Hackl0us/SS-Rule-Snippet@master/Rulesets/Clash/Basic/CN.yaml
    path: "./ruleset/CN.yaml"
    interval: 3600
  ad-keyword:
    type: http
    behavior: classical
    url: https://cdn.jsdelivr.net/gh/Hackl0us/SS-Rule-Snippet@master/Rulesets/Clash/Basic/common-ad-keyword.yaml
    path: "./ruleset/common-ad-keyword.yaml"
    interval: 3600
  foreign:
    type: http
    behavior: classical
    url: https://cdn.jsdelivr.net/gh/Hackl0us/SS-Rule-Snippet@master/Rulesets/Clash/Basic/foreign.yaml
    path: "./ruleset/foreign.yaml"
    interval: 3600
  telegram:
    type: http
    behavior: classical
    url: https://cdn.jsdelivr.net/gh/Hackl0us/SS-Rule-Snippet@master/Rulesets/Clash/App/social/Telegram.yaml
    path: "./ruleset/Telegram.yaml"
    interval: 3600
  lan:
    type: http
    behavior: classical
    url: https://cdn.jsdelivr.net/gh/Hackl0us/SS-Rule-Snippet@master/Rulesets/Clash/Basic/LAN.yaml
    path: "./ruleset/LAN.yaml"
    interval: 3600
rules:
- IP-CIDR,192.168.50.0/24,OFFICE-PROXY,no-resolve
- DOMAIN-SUFFIX,reliablesense.net,OFFICE-PROXY
- DOMAIN-SUFFIX,reliablesense.cn,OFFICE-PROXY
- RULE-SET,apple-proxy,ABROAD-PROXY
- RULE-SET,apple-direct,DIRECT
- RULE-SET,cn,DIRECT
- RULE-SET,ad-keyword,REJECT
- RULE-SET,foreign,ABROAD-PROXY
- RULE-SET,telegram,ABROAD-PROXY
- RULE-SET,lan,DIRECT
- GEOIP,CN,DIRECT
- MATCH,ABROAD-PROXY
```