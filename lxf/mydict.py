#/usr/bin/env python
#coding:utf-8

class Dict(dict):
	def __init__(self,**kw):
		super(Dict,self).__init__(**kw)

	def __getattr__(self,key):
		try:
			return self[key]
		except KeyError:
			raise AttributeError(r"'Dict' object has no attribute '%s'" % key)
	def __setatter__(self,key,value):
		self[key] = value


d = Dict(a=1,b='test')
print d

print d[0]
print d[1]
