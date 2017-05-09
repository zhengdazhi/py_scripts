#coding:utf-8
import string

#将单词加入集合
def addWord(w,theSet):
	if len(w) > 3:
		theSet.add(w)

#处理行，剔除各种字符、分割单词，参数是行 和集合。在处理行中每个单词的时候调用函数addWord
def processLine(line,theSet):
	line = line.strip()
	wordList = line.split()
	for word in wordList:
		if word != '--':
			word = word.strip()
			word = word.strip(string.punctuation)
			word = word.lower()
			addWord(word,theSet)

#参数是两个文件集合,显示各种有关文件的信息，最后用美观的格式来显示共用的词。
def prettyPrint(gaSet,doiSet):
	print 'Count of unigue words of length 4 or graer'
	print 'Gettysbury Addr: %d,Decl of Ind: %d\n'%(len(gaSet),len(doiSet))
	print '%15s %15s' % ('Operation','Count')
	print '-'*35
	print '%15s %15d' % ('Union',len(gaSet.union(doiSet)))
	print '%15s %15d' % ('Intersection',len(gaSet.intersection(doiSet)))
	print '%15s %15d' % ('Sym Diff',len(gaSet.symmetric_difference(doiSet)))
	print '%15s %15d' % ('GA-DoI', len(gaSet.difference(doiSet)))
	print '%15s %15d' % ('DoI-GA',len(doiSet.difference(gaSet)))
	intersectionSet = gaSet.intersection(doiSet)
	wordList = list(intersectionSet)
	wordList.sort()
	print '\n Common words to both'
	print '-n'*20
	cnt = 0
	for w in wordList:
		if cnt % 5 == 0:
			print
		print '%13s' % (w),
		cnt += 1

def main():
	GASet = set()
	DoISet = set()
	GAFileObj = open('gettysburg.txt')
	DoIFileObj = open('declOfInd.txt')
	for line in GAFileObj:
		processLine(line,GASet)
	for line in DoIFileObj:
		processLine(line,DoISet)
	prettyPrint(GASet,DoISet)

main()


