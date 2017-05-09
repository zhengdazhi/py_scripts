#!/usr/bin/env python
#coding:utf8

class Fib(object):
	def __init__(self):
		#初始化两个计数器
		self.a,self.b = 0,1

	def __iter__(self):
		#实例本身是迭代对象，故返回自己
		return self

	def next(self):
		self.a,self.b = self.b,self.a + self.b
		if self.a > 10000:
			raise StopIteration();
		return self.a

for n in Fib():
	print n
