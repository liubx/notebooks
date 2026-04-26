---
title: "堡垒机Linux上传下载文件说明"
source: feishu
feishu_token: "I60Ld5Ac7oSov0xDw8ZceXxDnfd"
feishu_type: docx
feishu_url: "https://reliablesense.feishu.cn/docx/I60Ld5Ac7oSov0xDw8ZceXxDnfd"
migrated: 2026-04-05
tags:
  - feishu-migration
---

1. 右键点击需要上传文件的服务器名称>>再点击连接，如下图：
![](Attachments/KGlNbKgRYoQRfoxZEtKcacOjntg.png)

2. 点击连接后出现ssh和sftp协议，上传文件选择sftp，如下图，账户如果有root就选择root，连接方式选择web，点击连接；
![](Attachments/A96ObSDB5oJcsExa9vEclFfnnsg.png)

3. 接着进入如下界面（对应/tmp目录），进入此界面就不要去做任何修改了，或者变更目录，你们可以理解为只能上传到/tmp目录，就像直连Linux也会对上传文件的目录做限制，堡垒机工具也会对上传文件做限制，如下图；
![](Attachments/EsVEb0mtVoPEtHxdhSwct6gqnnX.png)

4. 把自己要上传的文件，从本地往此处拖拽，然后松手即可，文件自动上传，上传速率与之前通过VPN连服务器无差别，如果用的是集团办公网，则不需要连VPN也能使用堡垒机，上传文件速率会高一截，如下图；
![](Attachments/MGBnb8hAQoCyKDxEG8jcJSmPnxf.png)

5. 文件即上传到到/tmp目录，如下图；
![](Attachments/AlWDbJDYHoseiGx8hdgck6U4n0e.png)

6. 进入系统/tmp目录，可见上传的目标文件，接下来根据各业务系统的需要，移动或者拷贝文件到其它目录，如下图；
![](Attachments/Gqn5bJeVCoCdvuxm0sec7onSnHD.png)

7. 下载文件，如下图；
![](Attachments/J0m8byrs0ojQOexa0wlcUmCNnbP.png)

