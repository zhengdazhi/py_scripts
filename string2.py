#-*-conding:utf-8-*-

import string
originalString = raw_input('Input a string:')
#将字符串转换成小写
modifiedStr = originalString.lower()
#创建一个ixn字符串，用来连接已修改的字符串所有不期望出现的字符，即表达和空格字符。
hadChars = string.whitespace + string.punctuation

#遍历修改后的字符串的每个字符，如果该字符是不期望出现的，则将其删除。用空格替换所有不期望出现的字符串。
for char in modifiedStr:
    if char in hadChars:
        modifiedStr = modifiedStr.replace(char,'')
#反转测试该字符串是否为回文，也就是说，修改后的字符串和反转的字符串是否相同。
if modifiedStr == modifiedStr[::-1]:
    print\
    'The original string is:    %s\n\
    the modified string is:     %s\n\
    String is palindrome'   % (originalString,modifiedStr,modifiedStr[::-1])
else:
    print\
    'The original string is:    %s\n\
    the modified string is:     %s\n\
    the reversal is:        %s\n\
    String is not a palindrome' % (originalString,modifiedStr,modifiedStr[::-1])

