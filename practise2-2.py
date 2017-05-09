
char_inputNum = raw_input("Please input a number \n")
#int_inputNum = int(char_inputNum)
#print int_inputNum
#int_sum = 0
#while int_inputNum > 0:
#    int_sum = int_sum + int_inputNum
#    int_inputNum = int_inputNum - 1
#    print int_inputNum
#print "number ",char_inputNum,"sum is ",int_sum

##########################
int_inputNum = int(char_inputNum)
for int_num in range(int_inputNum+1):
    type(int_num)
    int_sum = 0
    while int_num > 0:
        int_sum = int_num + int_sum
        int_num = int_num - 1
        #print int_num
    if int_num > 0 and int_sum % int_num == 0:
        print int_sum




