#!/usr/bin/env python
#coding:utf-8

from person import Person

class Manager(Person):
	#定制构造函数，增加mgr属性
	def __init__(self,name,pay):
		Person.__init__(self,name,'mgr',pay)
	#扩展父类方法，使用扩展的参数来直接调用其初始的版本
	#可以避免未来维护的工作量，例如父类方法中加薪方式修改了，子类不需要修改，
	def giveRaise(self,percent,bonus=.10):
		Person.giveRaise(self,percent + bonus)
		

if __name__ == '__main__':
	bob = Person('Bob Smith')
	sue = Person('Sue Jones',job='dev',pay=100000)
	print(bob)
	print(sue)
	print(bob.lastName(),sue.lastName())
	sue.giveRaise(.10)
	print(sue)
	tom = Manager('Tom Jones',500000)
	tom.giveRaise(.10)
	print(tom.lastName())
	print(tom)
	print('-- All three --')
	for object in (bob,sue,tom):
		object.giveRaise(.10)
		print(object)



