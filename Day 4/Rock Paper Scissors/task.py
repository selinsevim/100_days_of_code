import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
my_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors"))
# ask my choice
# map the choices to the signs
# make a list, from the list make a randomization
# from that print the results

computer = [rock, paper, scissors]
computer_choice = random.choice(computer)
print("Computer choose: ", computer_choice)

if my_choice == 0:
    print("My choice is rock!")
    print(rock)
    if computer_choice == rock:
        print("Equal")
    if computer_choice == paper:
        print("You lose")
    if computer_choice == scissors:
        print("You win")
if my_choice == 1:
    print("My choice is paper!")
    print(paper)
    if computer_choice == paper:
        print("Equal")
    if computer_choice == scissors:
        print("You lose")
    if computer_choice == rock:
        print("You win")
if my_choice == 2:
    print("My choice is scissors!")
    print(scissors)
    if computer_choice == scissors:
        print("Equal")
    if computer_choice == rock:
        print("You lose")
    if computer_choice == paper:
        print("You win")

