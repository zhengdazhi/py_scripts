#coding:utf-8
import string

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

main()
