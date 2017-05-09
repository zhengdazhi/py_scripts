#coding:utf-8
#使用filter()删除1-100的素数(质数)

#判断数字是否是素数的函数
def is_PrimeNum(x):
	n = 2
	m = x - 1
	while n < x:
		if(x % n == 0):
			print "%d is not prime number" % x
			print "N is %d" % n
			#break	
			return 0
		else:
			n = n + 1
		if n == m: 
			print "%d is prime number" % x
			print "N is %d" % n
			return 1
#测试函数
#result=is_PrimeNum(8)
#print result

filter(is_PrimeNum,range(100))

