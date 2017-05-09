#!/usr/bin/env python
#coding:utf-8
#使用filter高阶函数实现输出1～100内的素数

import math

#判断是否是素数
def IsPrime(n):
	if n <= 1:
		return False
	for i in range(2,int(math.sqrt(n)) + 1):
		if n % i == 0:
			return False
	return True

#传如一个列表，输出素数
def FilterPrime(L):
	print filter(IsPrime,L)


if __name__ == '__main__':
	FilterPrime(range(1,100))

