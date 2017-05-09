#!/usr/bin/env
#coding:utf-8

class Student(object):
	def __init__(self,name,score):
		self.name = name
		self.score = score

	def print_sctor(self):
		print '%s: %s' % (self.name,self.score)

	def get_grade(self):
		if self.score >= 90:
			return 'A'
		elif self.score >= 60:
			return 'B'
		else:
			return 'C'


#bart = Student('Bart Simpson',59)
#print bart.name
#print bart.score
#bart.print_sctor()
#print bart.get_grade()

