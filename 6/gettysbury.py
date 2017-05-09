def makeWordList(gFile):
    speech = []
    for lineString in gFile:
        lineList = lineString.split()
        speech.extend(lineList)
    return speech

gFile = open("gettysbury.txt","rU")
speech = makeWordList(gFile)
print speech
print "Length:", len(speech)






