#coding:utf-8
import string
import numpy
import pylab

def barGraph(wcDict):
	#生成列表wordList，然后将从wcDict获得的所有键-值对作为元组添加到列表中。
	wordList = []
	for key,val in wcDict.items():
		if val > 2 and len(key) > 3:
			wordList.append((key,val))
	#用（键，值）的顺序对元组进行排序，将键作为元组的首元素
	wordList.sort()
	#创建两个列表分别包含键和值，键和值的索引是一致的。
	keyList = [key for key,val in wordList]
	valList = [val for key,val in wordList]
	#设置图像中条形的宽度
	barWidth = 0.5
	#创建数字列表，数字从0到keyList。使用NumPy中的函数arange（和range类似）来生成列表，用做图像中的x轴刻度数字
	xVals = numpy.arange(len(keyList))
	#xtick命令有三个参数，第一个放置刻度的位置，使用Numpy的阵列类型来表示每个刻度的位置，每个刻度由刻度位置和barWidth相加再除2得到。加法和除法是应用于xVals阵列中的每个元素。第三个参数是标签列表keyList。第三个参数为是否要求每个标签旋转45度的选项
	pylab.xticks(xVals+barWidth/2.0,keyList,rotation=45)
	#绘图
	pylab.bar(xVals,valList,width=barWidth,color='r')
	pylab.show()

#将每个单词添加到字典中，参数为单词和字典，没有返回值
def addword(w,wcDict):
	if w in wcDict:
		wcDict[w] += 1
	else:
		wcDict[w] = 1

#要处理行，还要完成剔除不同的字符，分割出单词等工作。参数是文件的行和字典。
#处理每个单词时会调用函数addWord。没有返回值。
def processLine(line,wcDict):
	#除去每行前后的空白，然后分割行，得到单词列表
	line = line.strip()
	wordList = line.split()
	#变量wordList中的每个单词，跳过文件中的特殊字符串'--'
	#将每个单词转换为小写，并将两端的空白字符去掉
	#去掉单词尾巴的标点符号
	#调用函数addWord
	for word in wordList:
		if word != '--':
			word = word.lower()
			word = word.strip()
			word = word.strip(string.punctuation)
			addword(word,wcDict)


#格式化的显示，将针对每种情况（这意味着，随后可能需要修改它），将显示功能分离出来。参数是字典，没有返回值。
def prettyPrint(wcDict):
	valKeyList=[]
	#使用items方法遍历字典，对每个字典项以(键，值)的形式返回元组，对键和值进行多重赋值
	for key,val in wcDict.items():
		#以新元组(值，键)的形式添加到列表中（项顺序调换）
		valKeyList.append((val,key))
	#使用sort方法比较列表中每个元素的第一个值
	valKeyList.sort(reverse=True)
	print '%-10s%10s' % ('word','count')
	print '_'*21
	for val,key in valKeyList:
		print '%-12s %3d' % (key,val)

#使用主函数作为主程序。像往常一样，打开文件，对文件中的每一行调用processLine。最后调用prettyPrint来输出字典。
def main():
	wcDict = {}
	fObj = open('gettysburg.txt','r')
	for line in fObj:
		processLine(line,wcDict)
	print 'Length of the dictionary:',len(wcDict)
	prettyPrint(wcDict)
	#调用绘图函数
	barGraph(wcDict)

main()

