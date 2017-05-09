# -*- coding: utf-8 -*- 

def weightedGrade(gradeLst,weights=(0.3,0.3,0.4)):
    '''Expects 3 elements in gradeLst.Multiples each grade by its wight.
    Returns the sum. '''
    #将传递的参数（是一个列表）进行计算
    result = (gradeLst[0] * weights[0]) + \
            (gradeLst[1] * weights[1]) + \
            (gradeLst[2] * weights[2])
    return result

def grade(fileLine):
    '''Expects a line of form last,first,exam1,exam2,final.
    return first+last and a final grade.'''
    #以逗号为分割符，将字符串进行切割,将结果保存到一个列表中
    fieldLst = fileLine.split(',')
    #print fieldLst
    #将列表的第2和第1列进行拼接保存到字符串中
    name = fieldLst[1] + ' ' + fieldLst[0]
    #定义一个列表，将列表filedLst中从3个到尾部的所有内容复制进去
    grades = []
    for element in fieldLst[2:]:
        grades.append(int(element))
    #调用函数计算
    theGrade = weightedGrade(grades)
    #print theGrade
    return name,theGrade

def main():
    '''Get a line from the file,print the final grade nicely.'''
    fileName = raw_input('Open what file:')
    fileObj = open(fileName,'r')
    print '% -15s %-15s' %('Name','Grade')
    print '-'*25
    for line in fileObj:
        #去掉字符串头尾的空格
        line = line.strip()
        print '%-15s %7.2f'%grade(line)

main()
