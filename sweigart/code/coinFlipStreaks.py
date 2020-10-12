import random

'''
Write a program to find out how often a streak of six heads or a streak of six tails comes up 
in a randomly generated list of heads and tails.

'''
numberOfStreaks = 0
CoinFlip = []
streak = 0

for experimentNumber in range(10000):
    # Code that creates a list of 100 'heads' or 'tails' values
    for i in range(100):
        CoinFlip.append(random.randint(0, 1))
    # Code that checks if there is a streak of 6 heads or tails in a row
    for i in range(len(CoinFlip)):
        if i == 0:
            pass
        elif CoinFlip[i] == CoinFlip[i - 1]:  # checks if current list item is the same as before
            streak += 1
        else:
            streak = 0

        if streak == 6:
            numberOfStreaks += 1

print('Chance of streak: %s%%' % (numberOfStreaks / (100 * 10000)))
