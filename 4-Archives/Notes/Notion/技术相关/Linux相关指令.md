# Linux相关指令

`fuser -k 8080/tcp`

切换图形界面

`sudo systemctl set-default multi-user.target`

`sudo systemctl set-default graphical.target`

`tar xvf gitup-linux-amd64.tar.gz`

`tar cvf test.tar test/`

`cp -rp cnnc_qshdz-2022-12-06 platform-update`

`tar cvf platform-update.tar platform-update/`

代理

`all_proxy=socks://127.0.0.1:1080 curl -v https://www.google.com`

`ssh -N -L 5432:localhost:5432 root@82.156.16.18`

Photon 恢复密码

添加 `rw init=/bin/bash`

改密码

passwd

复制

`rsync -av --progress rsmap-demo demo --exclude node_modules --exclude rsmap/node_modules --exclude .umi --exclude .devcontainer`   

```bash
// cnnc_qshdz

cp -rp update-2022-12-13 update-2022-12-23
cp -rp update-2022-12-23 platform-update
tar cvf platform-update.tar platform-update/
coscmd upload platform-update.tar /
```

测试网络

```bash
// 监听
socat - udp-listen:30090

// 发送
echo "hello" | socat - udp4-datagram:82.157.96.77:30090

echo "hello" | socat - udp4-datagram:223.108.150.134:30002

```

测试mqtt

```bash
sudo yum install -y https://github.com/hivemq/mqtt-cli/releases/download/v4.10.0/mqtt-cli-4.10.0.rpm
mqtt test -h rtk.tulicn.com -p 12347 -u saas -pw 1SsvgiT4bP95kMuDyda1
mqtt test -h 172.16.1.244 -p 32300 -u saas -pw 1SsvgiT4bP95kMuDyda1
```

中间件网络测试

```jsx
apt update
apt install psmisc socat iputils-ping
fuser -k 10002/tcp

kubectl exec -it -n mid xbteek-gps-stable-685bdb7d7b-w66r9 -- sh

socat TCP-LISTEN:10002,fork STDOUT
echo "test" | socat - tcp:localhost:10002

socat TCP-LISTEN:10003,fork STDOUT
echo "test" | socat - tcp:localhost:10003

echo "test" | socat - tcp:xbteek-gps.mid:10003

echo "test" | socat - tcp:frp.reliablesense.cn:7080

```