#coding:utf-8

def f1(myDic):
	temp = 0
	for value in myDic.values():
		temp = temp + value
	return temp

def f2(myDic):
	temp=''
	for key in myDic:
		if temp < key:
			temp = key
	return temp

def f3(myDic,k,v):
	if k in myDic:
		myDic[k] = v


aDic = {'bill':1,'rich':2,'fred':10,'walter':20}
print f1(aDic)
print f2(aDic)
print None == f3(aDic,'bill',-1)
print aDic

