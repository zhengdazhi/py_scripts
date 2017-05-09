
myStr = raw_input("Input a string: \n")
indexInt = 0
resultStr = ""
while indexInt < (len(myStr) - 1):
    if myStr[indexInt] > myStr[indexInt + 1]:
        resultStr = resultStr + myStr[indexInt]
    else:
        resultStr = resultStr * 2
    indexInt += 1
print resultStr
