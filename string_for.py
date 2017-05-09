river = 'Mississippi'
target = raw_input('Input a character to find: \n')
for index in range(len(river)):
    if river[index] == target:
        print "letter found at index"
        break
else:
    print 'Letter',target,'not found in',river




