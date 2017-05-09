
river = 'Mississippi'
target = raw_input('Input a character to find: \n')
for index,letter in enumerate(river):
    if letter == target:
        print "Letter found at index:"
        break
else:
        print 'Letter',target,'not found in',river





