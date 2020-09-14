# Collatz sequence


def collatz(number):
    if (number % 2) == 0:
        return number // 2
    else:
        return 3 * number + 1


while True:
    try:
        print("Enter number: ")
        utente = int(input())
        break
    except ValueError:
        print("You must insert an integer")

risposta = 2

while risposta > 1:
    risposta = collatz(utente)
    print(risposta)
    utente = risposta
