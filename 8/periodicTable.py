#coding:utf-8
#算法
#1、读元素周期表CSV文件中的内容
#2、创建元素周期表的字典，使用每个元素符号作为建，使用CSV文件中的信息
#3、提示输入一中化合物，将他转换成元素列表
#4、解析化合物，生成符号-数量对，比如化合物“H2”变为（"H",2）
#5、显示化合物中每种元素的名称。
#6、使用字典中的信息将将化合物中的每个原子质量相加，得到总质量。

import csv

#输入文件对象并返回字典，其中的建为原子符号，值为csv文件中每个元素的信息
def readTable(dataFile):
	#读取文件，存入字典
	dataFile = csv.reader(fileObj)
	periodicTable = {}
	for row in dataFile:
		#只取是数字开头的行
		if row[0].isdigit():
			symbol = row[1]
			#取出每行的前7个字段作为字典的值
			periodicTable[symbol] = row[:8]
	return periodicTable

#接受'SymbolCount'形式的字符串，如'H2'。返回(symbol,count)形式的数对，例如('H',2)
def parseElement(elementStr):
	symbol = ""
	quantity = ""
	for ch in elementStr:
		if ch.isalpha():
			symbol = symbol + ch
		else:
			quantity = quantity + ch
	if quantity == "":
		quantity = 1
	return symbol,int(quantity)

#读取文件
fileHandle = open("Periodic-Table.csv","rUb")
#将读入的文件创建成字典
periodicTable = readTable(fileHandle)
#输入化合物的化学公式
compoundString = raw_input("Input a chemical compound,hyphenated,e.g.C-02: ")
#以'-'为分割符,分割字符串H2SO4   H-2-S-O-4，分割成列表
compoundList = compoundString.split("-")
mass = 0
print "The compound is composed of:"
for c in compoundList:
	symbol,quantity = parseElement(c)
	print periodicTable[symbol][5],
	mass = mass + quantity*float(periodicTable[symbol][6])
	print "\n\nThe atomic mass of the compound is",mass
	fileHandle.close()




