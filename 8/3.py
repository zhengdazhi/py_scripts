#coding:utf-8

import math
globalX = 27

def myFunction(param1=123,param2='him mom'):
	localX = 654.321
	print '\n=== local namespace ==='
	print type(locals)
	for key,val in locals().items():
		print 'key: %s,object: %s' % (key,str(val))
	print 'localX:',localX
	print 'globalX:',globalX

myFunction()

print '\n--- global namespace ---'
for key,val in globals().items():
	print 'key: %-15s object: %s' % (key,str(val))

print '\n -------------------'
print 'GlobalX:',globalX
print 'Math.pi:',math.pi
print 'Pi:',pi


