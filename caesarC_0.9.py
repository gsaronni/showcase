from string import ascii_lowercase as al  # imports strings of alphabet


def crypt(text, key, al):
    t = len(text)
    textB = ""
    for i in range(t):
        location = al.find(text[i])
        # location = location + 1
        new_location = (location + key) % 26
        textB += al[new_location]
    return textB


def bruteforce(en, al):
    tries = []
    a = len(al)
    falseKey = 0
    for i in range(a):
        falseKey = falseKey + 1
        brute00 = crypt(en, falseKey, al)
        tries.append(brute00)
    return tries


def main():
    while True:
        text = input("Please enter the message you would like to encrypt:\n")
        if text.isalpha():
            break
        else:
            print("No symbols or spaces please")

    while True:
        try:
            key = int(input("Please enter the key you would like to use:\n"))
            if key <= 26:
                break
            else:
                print("Enter a number lower than 27")
        except ValueError:
            print("It's Caesar cypher, remember? No symbols or spaces in the message or numbers as a key")
    return text, key


text, key = main()
en = crypt(text, key, al)
brute = bruteforce(en, al)

print("Your message: " + text)
print("Encrypted: " + en)
print("Bruteforce:", brute)
print(brute.find(text))
