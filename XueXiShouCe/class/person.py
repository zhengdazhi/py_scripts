#!/usr/bin/env python
#coding:utf-8

from classtools import AttrDisplay

class Person(AttrDisplay):
	def __init__(self,name,job=None,pay=0):
		self.name = name
		self.job = job
		self.pay = pay
	def lastName(self):
		return self.name.split()[-1]
	def giveRaise(self,percent):
		self.pay = int(self.pay * (1 + percent))
	#运算符重载，每次一个实例转换为其打印字符串的时候，__str__都会自动运行
	#打印对象就会显示对象的__str__方法所返回的内容
	#
	#def __str__(self):
	#	return '[Person: %s,%s]' % (self.name,self.pay)

if __name__ == '__main__':
	bob = Person('Bob Smith')
	sue = Person('Sue Jones',job='dev',pay=100000)
	print(bob.name,bob.pay)
	print(sue.name,sue.pay)
	print(bob.lastName(),sue.lastName())
	sue.giveRaise(.10)
	print(sue.pay)
	print(sue)

