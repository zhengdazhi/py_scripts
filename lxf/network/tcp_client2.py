#!/usr/bin/env python
#coding:utf-8

import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(('127.0.0.1',9999))
print s.recv(1024)
for data in ['Micheal','Tracy','Sarah']:
	s.data(data)
	print s.recv(1024)
s.send('exit')
s.close()
