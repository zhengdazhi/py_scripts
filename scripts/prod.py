#!/usr/bin/evn python
#coding:utf-8

#接受一个list并求积

def produce(x,y):
	return x * y

def prod(L):
	print L
	print reduce(produce,L)

prod([1,2,3,4])


