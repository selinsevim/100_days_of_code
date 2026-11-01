# randomly select the 2 celebrities from the dictionary
# compare them
# if the user select the higher one correct, than eliminate the lower one from the dictionary list
# compare the former higher one, with the new one from the dictionary
# keep going until the user answers the correct one
# for each correct answer give +1 score to the user
# for each incorrect one take -1 from the scores
# the game is over when the user gives incorrect answer = lower answer

import random
import game_data

def compare(first_random, second):
    follower_count_1 = int(first_random['follower_count'])
    follower_count_2 = int(second['follower_count'])
    # compare the numbers, find the higher one
    if follower_count_1 > follower_count_2:
        print(first_random['name'], "has higher")
        return "A"
    elif follower_count_2 > follower_count_1:
        print(second['name'], "has higher")
        return "B"

def find_the_higher_one(first_random, second):
    follower_count_1 = int(first_random['follower_count'])
    follower_count_2 = int(second['follower_count'])
    # compare the numbers, find the higher one
    highest_one = []
    if follower_count_1 > follower_count_2:
        print(first_random['name'], "has higher")
        highest_one.append(first_random)
        return highest_one[0]
    elif follower_count_2 > follower_count_1:
        print(second['name'], "has higher")
        highest_one.append(second)
        return highest_one[0]

def remove_lower_item(list_game, first_random, second):
    follower_count_1 = int(first_random['follower_count'])
    follower_count_2 = int(second['follower_count'])
    # compare the numbers, find the higher one
    if follower_count_1 > follower_count_2:
        list_game.remove(second)
        return list_game
    elif follower_count_2 > follower_count_1:
        list_game.remove(first_random)
        return list_game

def select_items(list_game):
    # set the number to select here.
    num_to_select = 2
    list_of_random_items = random.sample(list_game, num_to_select)
    first_random_item = list_of_random_items[0]
    second_random_item = list_of_random_items[1]
    print('Compare A', first_random_item)
    print('Compare B', second_random_item)
    return first_random_item, second_random_item

def reselect_items(list_game, first):
    # set the number to select here.
    num_to_select = 1
    list_of_random_items = random.sample(list_game, num_to_select)
    second_item = list_of_random_items[0]
    print('Compare A', first)
    print('Compare B', second_item)
    return second_item

score = 0
game_over = False
game_data_collection = game_data.data
# first item value, to be updated
# second item value, to be updated
value_1 = []
value_2 = []

while not game_over:

    value_1, value_2 = select_items(game_data_collection)
    user_answer = input("Who has more followers? Type 'A' or 'B'\n")
    correct_answer = compare(value_1, value_2)

    if correct_answer == user_answer:
        print("Correct answer")
        score += 1
        print(f"Score is {score}")

        while correct_answer == user_answer:
            # if it is a correct answer lower item should be eliminated from the list
            # find the index of lower item
            print("Printing the while")
            game_data_list = remove_lower_item(game_data_collection, value_1, value_2)

            higher_one = find_the_higher_one(value_1, value_2)
            print("Higher one is", higher_one)

            # find the higher item and assign it as first_random_item
            second_random = reselect_items(game_data_list, higher_one)

            user_answer = input("Who has more followers? Type 'A' or 'B'\n")
            correct_answer = compare(higher_one, second_random)

            print("Correct answer")
            score += 1
            print(f"Score is {score}")

    else:
        print("Incorrect answer")
        print("Game is over")
        score = 0
        print(f"Score is {score}")
        game_over = True

