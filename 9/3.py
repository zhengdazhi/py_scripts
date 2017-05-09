testFile = open("temp.txt","r")
aLine = testFile.readline()
aLine
for line in testFile:
    print line

testFile.close()
