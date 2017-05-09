
strLst = ['hi','mom','dad',['grandma','grandpa']]
newLst = strLst
copyLst = strLst[:]

print strLst

strLst[0] = 'bye'
newLst[1] = 'mother'
copyLst[2] = 'father'
copyLst[-1][0] = 'nanna'

print strLst
print newLst
print copyLst
