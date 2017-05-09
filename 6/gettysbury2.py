
def makeWordList(gFile):
    speech = []
    for lineString in gFile:
        lineList = lineString.split()
        for word in lineList:
            word = word.lower()
            word = word.strip('.,')
            if word != "--":
                speech.append(word)
    return speech

def makeUnique(speech):
    unique = []
    for word in speech:
        if word not in unique:
            unique.append(word)
    return unique
gFile = open("gettysbury.txt","rU")
speech = makeWordList(gFile)
print "Speech Length:",len(speech)

unique = makeUnique(speech)
print unique
print "Unique Length:",len(unique)




