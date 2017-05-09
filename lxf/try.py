#!/usr/bin/env python
#coding:utf-8

try:
    print 'try...'
    r = 10 / int('10')
    print 'result:', r
except ValueError, e:
    print 'ValueError', e
except ZeroDivisionError,e:
	print 'ZeroDivisionError',e
else:
	print 'no error'
finally:
    print 'finally...'
print 'END'


def foo():
	r = some_function()
	if r == (-1):
		return (-1)
	return r

def bar():
	r = foo()
	if r == (-1):
		print 'Error'
	else:
		pass

try:
	foo()
except StandardError,e:
	print 'StandardError'
except ValueError,e:
	print 'ValueError'

	
