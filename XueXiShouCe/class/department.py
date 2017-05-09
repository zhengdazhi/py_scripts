#!/usr/bin/env python
#coding:utf-8

from person import Person
from manager import Manager

class Department:
	#函数的参数是可变参数，类的初始化参数是一个元组
	def __init__(self,*args):
		self.members = list(args)
	def addMember(self,person):
		self.members.append(person)
	def giveRaises(self,percent):
		for person in self.members:
			person.giveRaise(percent)
	def showAll(self):
		for person in self.members:
			print(person)
			
if __name__ == '__main__':
	bob = Person('Bob Smith')
	sue = Person('Sue Jone')
	tom = Manager('Tom Green',5000)
	development = Department(bob,sue)
	development.addMember(tom)
	development.giveRaises(.10)
	development.showAll()


