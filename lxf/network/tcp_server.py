#!/usr/bin/env python
#coding:utf-8

import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(('127.0.0.1',9999))
s.listen(5)
while True:
	#接受一个新请求
	sock,addr = s.accept()
	#创建新县城来处理TCP连接
	t = threading.Thread(target=tcplink,args=(sock,addr))
	t.start()

#每个连接都必须创建新线程（或进程）来处理，否则单线程在处理连接过程中，无法接受其他客户端的连接
def tcplink(sock,addr):
	print 'Accept new connection from %s:%s...' % addr
	sock.send('Welcome!')
	while True:
		data = sock.recv(1024)
		time.sleep(1)
		if data == 'exit' or not data:
			barak
		sock.send('Hello,%s!' % data)
	sock.close()
	print 'Connection from %s:%s closed' % addr

