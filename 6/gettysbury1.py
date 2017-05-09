def makeWordList(gFile):
    speech = []
    for lineString in gFile:
        lineList = lineString.split()
        for word in lineList:
            if word != "--":
                speech.append(word)
    return speech

gFile = open("gettysbury.txt","rU")
speech = makeWordList(gFile)

print speech
print "Speech Length:",len(speech)


