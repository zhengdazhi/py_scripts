
def createMileageList(epaFile):
    mileageList = []
    #逐行读取列表
    for line in epaFile:
        #使用逗号作为分隔符，将读取的行进行分割
        lineList = line.split(',')
        #将第9列，将数据转换为整型，追加到mileageList列表中
        mileageList.append(int(lineList[9]))
    return mileageList

epaFile = open("epaData.csv","rU")
mileageList = createMileageList(epaFile)
print mileageList




