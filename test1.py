
userVal = raw_input("Please enter a positive integer:")
myInt = int(userVal)
count = 0
while myInt > 0:
    if myInt %2 == 1:
        myInt = myInt/2
    else:
        myInt = myInt - 1
    count = count + 1
print count
print myInt
