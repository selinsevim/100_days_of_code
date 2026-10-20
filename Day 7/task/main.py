import random
from unittest import skip

word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print(placeholder)

placeholder = list(placeholder)

# TODO-1: - Use a while loop to let the user guess again.
# TODO-2: Change the for loop so that you keep the previous correct letters in display.

num_blanks = placeholder.count("_")

# check each time if the user already guessed the letter in chosen word
while num_blanks > 0:
    guess = input("Guess a letter: ").lower()
    if guess in placeholder:
        print("Guess is in display", guess)
    else:
        for i, char in enumerate(chosen_word):
            # i is the index of char
            if char == guess:
                placeholder[i] = guess
    # join the list to create string
    print("".join(placeholder))
    num_blanks = placeholder.count("_")
    print(num_blanks)
