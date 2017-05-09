twoWords = raw_input("Input two space-separated worlds:")
twoWords
twoWords.split()
twoWordsList = twoWords.split()
twoWordsList

word1 = twoWordsList[0]
word2 = twoWordsList[1]
word1_sorted = sorted(word1)
word2_sorted = sorted(word2)

if word1_sorted == word2_sorted:
    print "The words are anagrams"
else:
    print "The words are not anagrams"

