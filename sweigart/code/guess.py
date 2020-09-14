import random

secretNumber = random.randint(1, 10)
print('I am thinking of a number between 1 and 10.')

# Ask the player to guess 6 times
for guessesTaken in range(1, 7):
    print('Take a guess.')
    guess = int(input())

    if guess < secretNumber:
        print('Your guess is too low.')
    elif guess > secretNumber:
        print('You guess is too high.')
    else:
        break  # This condition is the correct guess

if guess == secretNumber:
    print('You win! You guessed in ' + str(guessesTaken) + ' guesses!')
else:
    print('Nope. The number I was thinking of was ' + str(secretNumber))
