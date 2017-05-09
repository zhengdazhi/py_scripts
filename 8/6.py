#coding:utf-8

#使用zip函数将序列和成元组列表，再结合字典构造函数dict可以创建字典
keys = ["red","white","blue"]
values = [100,300,500]
d = dict(zip(keys,values))
print d
#zip函数可以交换字典的键值对
d2 = dict(zip(d.values(),d.keys()))
print d2
