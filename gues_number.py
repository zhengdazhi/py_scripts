import random

number = random.randint(0,100)
#print number
print "Hi Number Cuessing Game:between 0 and 100 inclusive"
guessString = raw_input("Guess an number:")
guess = int(guessString)

while 0 <= guess <= 100:
    if guess > number:
        print "Guessed Too Hight"
    elif guess < number:
        print "Guessed Too Low"
    else:
        print "You guessed it.The number was:",number
        break
    guessString = raw_input("Guess a number:")
    guess = int(guessString)
else:
    print "You quit early,the number was:",number
