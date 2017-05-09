#coding:utf-8
#介绍一个list利用reduce()求积

def cheng(x,y):
	return x * y

def prod(list):
	print reduce(cheng,list)

list1 = [1,2,3,4,5]
prod(list1)
