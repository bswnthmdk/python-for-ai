import json
import random

with open("questions.json", "r") as file:
    questions = json.load(file)

print("Welcome to the Quiz Game!")

no_of_questions = int(input("How many questions would you like to answer? "))
selected_questions = random.sample(questions, no_of_questions)

score = 0

for question in selected_questions:
    print(question["question"])
    answer = input("Your answer: ")

    if question["answer"].lower() == answer.lower():
        score += 1
        print("Correct!")
    else:
        print("Wrong!")

print(f"Your final score is: {score}")
