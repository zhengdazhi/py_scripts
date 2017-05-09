#coding:utf-8

myVar = 27
def myFunction(param1=123,param2='Python'):
	for key,val in locals().items():
		print 'key %s: %s' % (key,str(val))
	myVar = myVar + 1

def betterFunction(paraml1=123,param2='Python'):
	global myVar
	for key,val in locals().items():
		print 'key %s: %s' % (key,str(val))
	myVar = myVar + 1
	print 'myVar:',myVar

#myFunction(123456,76432.0)
betterFunction()
