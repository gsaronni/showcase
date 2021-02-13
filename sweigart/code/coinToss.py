import random
while True:
    print('Guess the coin toss! Enter 1 for heads or 0 for tails:')
    guess = int(input())
    toss = random.randint(0, 1)  # 0 is tails, 1 is heads
    if toss == guess:
        print('You got it!')
        break
    else:
        print('Nope! Guess again!')
        guess = input()
        if toss == guess:
            print('You got it!')
        else:
            print('Nope. You are really bad at this game.')
