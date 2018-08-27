# -*- coding:UTF-8 -*-
import socket
from crypt import PrpCrypt
import hashlib
import time


client = socket.socket()
client.connect(('192.168.0.111',9999))

while True:

	cmd = input(">>:").strip()

	if len(cmd) == 0:continue

	if cmd.startswith("get"): #是否以get开头
                
		client.send(cmd.encode())
		server_response = client.recv(1024)
		print("server respoense:",server_response)
		client.send(b"ready to recv file") #发送ACK确认，交互防止send粘包
		file_total_size = int(server_response.decode())
		received_size = 0
		filename = cmd.split()[1]
		f = open(filename + ".new","wb")
		m = hashlib.md5() #使用md5加密
		
		while received_size < file_total_size:  #判断总数据比递增接收数据大就成立

			if file_total_size - received_size > 1024: #数据比recv大就成立
				size = 1024
				
			else: #最后一次，还剩多少
				size = file_total_size - received_size  #求出剩余recv数值
				print("last receive:",size) #最后一次收了多少
				
			data = client.recv(size)
			received_size += len(data) #递增接收数据
			m.update(data) #递增接收数据并加密md5
			f.write(data)
			#print(file_total_size,received_size) #每次发送大小
		else:
			new_file_md5 = m.hexdigest()#返回十六进制
			print("file recv done",received_size,file_total_size)
			f.close()
			temporary = PrpCrypt(f.name, '1234567891011121')#传递文件名和密钥
			file = temporary.decrypt_output(f.name)#解密文件
			
		server_file_md5 = client.recv(1024)
		print("server file md5:",server_file_md5)
		print("client file md5:",new_file_md5)
client.close()

