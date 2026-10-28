import random

import art
print(art.logo)

# go into the game with while loop
# ask the user if they want easy or hard
# if it is easy you have 10 attempts -> have counter with while loop
# if it is hard you have 5 attempts -> have counter with while loop
# randomly choose a number between 0-100 -> save it to a variable
# ask the user choose a number -> save it to a temporary variable
# if the temp var smaller than the chosen var -> say it is way too low
# else say it is too high
# when the user predicts restart the game

def compare(chosen, user, level):
    global game_over, counter_easy, counter_hard
    if level == "easy":
        if user > chosen:
            print("Too high")
            print("Guess again")
            counter_easy -= 1
            print(f"You have {counter_easy} attempts remaining to guess the number.")
        if user < chosen:
            print("Too low")
            print("Guess again")
            counter_easy -= 1
            print(f"You have {counter_easy} attempts remaining to guess the number.")
        if user == chosen:
            print(f"You got it! The answer was {chosen}.")
            game_over = True
        if counter_easy == 0 and not game_over:
            print(f"You lost it!.")
            game_over = True
    if level == "hard":
        if user > chosen:
            print("Too high")
            print("Guess again")
            counter_hard -= 1
            print(f"You have {counter_hard} attempts remaining to guess the number.")
        if user < chosen:
            print("Too low")
            print("Guess again")
            counter_hard -= 1
            print(f"You have {counter_hard} attempts remaining to guess the number.")
        if user == chosen:
            print(f"You got it! The answer was {chosen}.")
            game_over = True
        if counter_hard == 0 and not game_over:
            print(f"You lost it!.")
            game_over = True


new_game = True

while True:
    print("Welcome to the Number Guessing Game! I'm thinking of a number between 1 and 100.")

    while new_game:
        counter_easy = 10
        counter_hard = 5
        game_over = False  # global variable

        chosen_number = random.randint(0, 100)
        print("Number is:", chosen_number)

        answer = input("Choose a difficulty. Type 'easy' or 'hard': ")

        if answer == "easy":

            while counter_easy > 0 and not game_over:
                user_variable_easy = int(input("Make a guess: "))
                compare(chosen_number, user_variable_easy, "easy")

        if answer == "hard":

            while counter_hard > 0 and not game_over:
                user_variable_hard = int(input("Make a guess: "))
                compare(chosen_number, user_variable_hard, "hard")



