#!/usr/bin/env python
#coding:utf-8
#使用OrderedDict函数实现一个先进先出的字典，当容量超出限制时，先删除最早添加的key

from collections import OrderedDict

class LastUpdatedOrderedDict(OrderedDict):
	def __init__(self,capacity):
		super(LastUpdatedOrderedDict,self).__init__()
		self._capacity = capacity

	def __setitem__(self,key,value):
		containsKey = 1 if key in self else 0
		if len(self) - containsKey >= self._capacity:
			last = self.popitem(last=False)
			print 'remove:',last
		if containsKey:
			del self[key]
			print 'set:',(key,value)
		else:
			print 'add:',(key,value)
		OrderedDict.__setitem__(self,key,value)


fifo_dic = LastUpdatedOrderedDict(5)

fifo_dic['a'] = 1
fifo_dic['b'] = 2
fifo_dic['c'] = 3
fifo_dic['d'] = 4
fifo_dic['e'] = 5
print fifo_dic
fifo_dic['f'] = 6
print fifo_dic
