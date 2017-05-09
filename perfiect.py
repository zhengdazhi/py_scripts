# -*- coding:utf8 -*-

#从键盘获取数字
theNum = raw_input("Please enter a number to check:")
theNum = int(theNum)


divisor = 1
sumOfDivisors = 0
while divisor < theNum:
    if theNum % divisor == 0:
        sumOfDivisors = sumOfDivisors + divisor
    divisor = divisor + 1

if theNum == sumOfDivisors:
    print theNum,"is perfect"
else:
    print theNum,"is not perfect"

