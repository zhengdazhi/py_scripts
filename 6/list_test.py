
myList = [1.6,2.7,3.8,4.9]
newList = []
aList = []

for val in myList:
    temp = str(val)
    aList.append(temp.split('.'))

for val in aList:
    newList.append(int(val[0]))

myStr = ':'.join(val)

print myList
print aList
print newList
print val
print myStr

