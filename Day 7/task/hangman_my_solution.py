import random

stages = [r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

word_list = ["aardvark", "baboon", "camel"]

# TODO-3: - print the ASCII art from 'stages'
#  that corresponds to the current number of 'lives' the user has remaining.

chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print(placeholder)

placeholder = list(placeholder)
num_blanks = placeholder.count("_")

# TODO-1: - Create a variable called 'lives' to keep track of the number of lives left.
#  Set 'lives' to equal 6.

lives = 6

# check each time if the user already guessed the letter in chosen word
# have a logic for the wrong letters, if guess wrong take the lives
while lives > 0:
    guess = input("Guess a letter: ").lower()
    if guess in placeholder:
        print("Guess is in display", guess)
    if guess not in chosen_word:
# TODO-2: - If guess is not a letter in the chosen_word, Then reduce 'lives' by 1.
        lives -= 1
        print("Number of lives left: ", lives)
    else:
        for i, char in enumerate(chosen_word):
            # i is the index of char
            if char == guess:
                placeholder[i] = guess
    # join the list to create string
    print("".join(placeholder))
    #num_blanks = placeholder.count("_")
    if lives == 6:
        print(stages[0])
    if lives == 5:
        print(stages[1])
    if lives == 4:
        print(stages[2])
    if lives == 3:
        print(stages[3])
    if lives == 2:
        print(stages[4])
    if lives == 1:
        print(stages[5])
#  If lives goes down to 0 then the game should stop and it should print "You lose."
    if lives == 0:
        print(stages[6])
        print("Game is over. You lose.")

