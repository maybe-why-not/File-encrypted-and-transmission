# -*- coding:UTF-8 -*-
import socket,os,hashlib
import time
from crypt import PrpCrypt


server = socket.socket()
server.bind(('0.0.0.0',9999))
server.listen()
while True:
    conn,addr = server.accept()
    print("new conn:",addr)
    
    while True:
        print("server on....")
        data = conn.recv(1024)
        
        if not data:
            print("客户端已断开")
            break
        
        cmd,file = data.decode().split()
        print(file)
        
        if os.path.isfile(file): #是否是文件
            temporary = PrpCrypt(file, '1234567891011121')#传递文件名和密钥
            filename = temporary.encrypt_output(file)#加密文件
            f = open(filename,"rb")
            m = hashlib.md5() #创建md5校验
            file_size = os.stat(filename).st_size #获取文件大小
            conn.send(str(file_size).encode()) #发送文件大小
            conn.recv(1024) #等待ACK交互防止粘包
            
            for line in f:
                m.update(line) #递增加密文件
                conn.send(line)
                
            print("file md5",m.hexdigest()) #打印16进制md5
            f.close()
            conn.send(m.hexdigest().encode())
            
        print("send done")
        
server.close()
