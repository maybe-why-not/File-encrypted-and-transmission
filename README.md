# File-encrypted-and-transmission
两台电脑之间的文件AES加解密、MD5校验、tcp传输


使用说明：
  环境：python3,两台虚拟机
  步骤：1、更改socket_client.py中client.connect(('192.168.0.111',9999))处的'192.168.0.111'为另一台电脑的ip
        2、运行socket_server.py
        3、运行socket_client.py
          root@kali:~/桌面# python socket_client.py
          >>:get url.txt
          #url.txt为server上与socket_server同文件夹下的文件
