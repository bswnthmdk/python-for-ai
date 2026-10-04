import random


def guess_game():
    ip = int(input("Guess a number between 1 to 10: "))

    secret_num = random.randint(1, 11)

    if secret_num == ip:
        return True
    else:
        return False


c = 0

while True:
    c += 1
    if guess_game():
        print("You guessed it right!")
        print(f"Guess attempts: {c}")
        break
    else:
        print("Wrong guess! Try again.")
