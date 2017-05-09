
import string
def func1 (str1):
    resultStr = ''
    for char in str1:
        if char in string.digits:
            resultStr = resultStr + char
    if resultStr:
        return resultStr
    else:
        return -1

def func2 (str1):
    if len(str1) > 0:
        str1 = str1.strip()
        resultInt = func1(str1)
    else:
        resultInt = 0
    return resultInt

responseStr = raw_input("Input a string:")
print func2(responseStr)
