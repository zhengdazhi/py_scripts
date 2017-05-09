testFile = open("temp.txt","r")
wholeFile = testFile.read()
for line in wholeFile:
    print line
testFile.close()
