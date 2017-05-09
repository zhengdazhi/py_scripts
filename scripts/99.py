#!/usr/bin/env python

from __future__ import print_function

L1 = []
L2 = []
#for i in range(1,10):
#	#print i
#	for i in range(1,i):
#		if i == 1:
#			j = 1 * i
#		#	print "%s * %s = %s" % (i,i,j)
#			L2.append("i * i = j")
#		else:
#			k = i + 1
#			j = k * i
#		#	print "%s * %s = %s" % (i,k,j)
#			L2.append("i * i = j")
#	n = i - 1

#	print "i is %s,n is %s" % (i,n)
	#L1[n]=L2

#L1
n = 1
m = 1
for n in range(1,10):
	for m in range(1,10):
		k = n * m
		print ("%s * %s = %s" % (n,m,k))
		#print (m, end = "")

