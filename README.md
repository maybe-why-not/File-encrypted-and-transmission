# File-encrypted-and-transmission
两台电脑之间的文件AES加解密、MD5校验、tcp传输


使用说明：
  <br>    环境：python3,两台虚拟机
  <br>    步骤：1、更改socket_client.py中client.connect(('192.168.0.111',9999))处的'192.168.0.111'为另一台电脑的ip
        <br>    2、运行socket_server.py
        <br>    3、运行socket_client.py
          <br>    root@kali:~/桌面# python socket_client.py
          <br>    >>:get url.txt
          <br>    #url.txt为server上与socket_server同文件夹下的文件

注意：crypto模块安装完之后各种报错不存在，在路径Python36\Lib\site-packages下找到Crypto.Cipher把包名改成大写，安装的时候有时候大写有时候小写。

参考链接：
<br>[https://www.cnblogs.com/huangjianting/p/8666446.html](https://www.cnblogs.com/huangjianting/p/8666446.html)
<br>[https://www.cnblogs.com/xiangsikai/p/8137508.html](https://www.cnblogs.com/xiangsikai/p/8137508.html)
<br>[https://www.cnblogs.com/guqing/p/6084009.html](https://www.cnblogs.com/guqing/p/6084009.html)
<br>[https://blog.csdn.net/qq_29053519/article/details/79170519](https://blog.csdn.net/qq_29053519/article/details/79170519)
<br>[https://blog.csdn.net/yenai2008/article/details/70240658](https://blog.csdn.net/yenai2008/article/details/70240658)
