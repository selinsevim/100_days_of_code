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

EASY_ATTEMPT_COUNTER = 10
HARD_ATTEMPT_COUNTER = 5
game_over = False

def choose_level():
    answer = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if answer == "easy":
        return EASY_ATTEMPT_COUNTER
    if answer == "hard":
        return HARD_ATTEMPT_COUNTER

while True:
    print("Welcome to the Number Guessing Game! I'm thinking of a number between 1 and 100.")

    chosen_number = random.randint(1, 100)
    print("Number is:", chosen_number)

    counter = choose_level()

    while counter > 0 and not game_over:
        user_guess = int(input("Make a guess: "))
        if user_guess > chosen_number:
            print("Too high")
            print("Guess again")
            counter -= 1
            print(f"You have {counter} attempts remaining to guess the number.")
        if user_guess < chosen_number:
            print("Too low")
            print("Guess again")
            counter -= 1
            print(f"You have {counter} attempts remaining to guess the number.")
        if user_guess == chosen_number:
            print(f"You got it! The answer was {chosen_number}.")
            game_over = True
        if counter == 0 and not game_over:
            print(f"You lost it!.")
            game_over = True



