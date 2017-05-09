inFile = open("input.txt","r")
outFile = open("output.txt","w")

oneLine = inFile.readline()
print oneLine

for line in inFile:
    outFile.write(line)
inFile.close()
outFile.close()
