#!/usr/bin/env python
#coding=utf-8

#冒泡排序

array = [1,2,5,3,6,8,4]

#获取列表长度-1的数，根据长度，生成一个倒序的列表，
#range(n,0,-1) 表示生成一个从n到0的列表，步长是1
#range(0,n,1)表示生成一个从0到n的列表，步长是1
for i in range(len(array)-1,0,-1):
	for j in range(0,i):
		if array[j] > array[j+1]:
			array[j],array[j+1] = array[j+1],array[j]

print array
