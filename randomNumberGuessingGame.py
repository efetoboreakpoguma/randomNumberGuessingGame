# This program is meant to generate a random number in the range of 1 through 
# 10, and ask the user to guess what the number is. It also displays the 
# number of attempts the user has made

import random

print ('Generating random number...')
print ()
print ('Random number generated !!!')
print ()

gameContinuation = 'Y'
numberOfGuesses = 1

while gameContinuation == 'Y' or gameContinuation == 'y':
    randomNumber = random.randrange (1, 10)
    guess = int(input ('Please guess the random number: '))
    while guess != randomNumber:
        numberOfGuesses += 1
        if guess < randomNumber:
            print ('Too low, try again')
            guess = int(input ('Please guess the random number: '))
        else:
            print ('Too high, try again')
            guess = int(input ('Please guess the random number: '))
    else:
        print ('Congrats, you guessed the right number:', randomNumber)
        print ('Number of tries:', numberOfGuesses)
        gameContinuation = input ("Type 'Y' to continue playing or 'N' to quit the game: ")
        if gameContinuation == 'N' or gameContinuation == 'n':
            print ()
            print ('**************** End of the game ****************')