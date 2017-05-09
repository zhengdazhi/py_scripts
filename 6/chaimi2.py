
def areAnagrams(word1,word2):
    word1_sorted = sorted(word1)
    word2_sorted = sorted(word2)

    if word1_sorted == word2_sorted:
        return True
    else:
        return False

print "Anagram Test"

twoWords = raw_input("Enter two words:")
twoWordList = twoWords.split()
word1 = twoWordList[0]
word2 = twoWordList[1]

if areAnagrams(word1,word2):
    print "The words are anagrams."
else:
    print "The words are not anagrams."

