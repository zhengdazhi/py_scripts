def cleanWord(word):
    return word.strip().lower()

def getVowelsInWord(word):
    vowelStr = "aeiou"
    vowelsInWord = ""
    for char in word:
        if char in vowelStr:
            vowelsInWord += char
        return vowelsInWord


dataFile = open("dictionary.txt","r")


for world in dataFile:
    word = cleanWord(word)
    if len(word) <= 6:
        continue
    vowelStr = getVowelsInWord(word)
    if vowelStr == "aeiou":
        print word
