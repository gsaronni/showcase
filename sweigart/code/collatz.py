"""
Collatz sequence

if number == even
    print(number // 2)
    return number // 2

if number == odd
    print(3 * number + 1)
    return print

"""


def collatz(number):
    if (number % 2) == 0:
        sequenza = number // 2
    else:
        sequenza = 3 * number + 1

    print(sequenza)
    return sequenza


print("Enter number: ")
utente = int(input())
collatz(utente)

while True:
    collatz(sequenza)
