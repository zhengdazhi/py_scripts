#coding:utf-8

#首字母大写函数
#capitalize()
#str1 = 'admin'
#str1.capitalize()

#定义一个函数转换手字母大写
def up_HeadWord(string):
	return string.capitalize()

#map函数调用up_HeadWord函数
#print map(up_HeadWord,['admin','oracle','linux','python'])

def up_ListHead(list):
	up_list = map(up_HeadWord,list)
	return up_list

list1 = ['admin','linux','python']
print up_ListHead(list1)
