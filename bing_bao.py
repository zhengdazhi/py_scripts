#-*- coding:utf-8 -*-

char_numString = raw_input("Enter a positive intger:")
int_num = int(char_numString)
count = 0

print "Starting with number:",int_num
print "Sequence is:",

while int_num > 1:
    if int_num%2:
        int_num = int_num * 3 + 1
    else:
        int_num = int_num / 2
    print int_num,","
    count += 1
else:
    print
    print "Sequence is",count,"numbers long"
