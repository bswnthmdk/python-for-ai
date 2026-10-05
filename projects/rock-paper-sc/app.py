import random

print("Welcome to the Rock-Paper-Scissors Game!")

target = int(input("Set the target score to win the game: "))

user_score = 0
computer_score = 0


def game():
    global user_score, computer_score

    user_choice = input("Select any one (R-P-S): ").lower()
    if user_choice not in ["r", "p", "s"]:
        print("Invalid choice. Please select R, P, or S.")
        return
    computer_choice = random.choice(["r", "p", "s"])
    print(f"Computer selected: {computer_choice.upper()}")

    if (
        (user_choice == "r" and computer_choice == "s")
        or (user_choice == "p" and computer_choice == "r")
        or (user_choice == "s" and computer_choice == "p")
    ):
        user_score += 1
        print(f"You: {user_score}, Computer: {computer_score}")
    elif (
        (computer_choice == "r" and user_choice == "s")
        or (computer_choice == "p" and user_choice == "r")
        or (computer_choice == "s" and user_choice == "p")
    ):
        computer_score += 1
        print(f"You: {user_score}, Computer: {computer_score}")
    else:
        print(f"DRAW! You: {user_score}, Computer: {computer_score}")


while user_score < target and computer_score < target:
    game()


if user_score > computer_score:
    print(f"Congratulation! You: {user_score} & Computer: {computer_score}")
else:
    print(f"You Lost! You: {user_score} & Computer: {computer_score}")
