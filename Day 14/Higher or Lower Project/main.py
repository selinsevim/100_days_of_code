# randomly select the 2 celebrities from the dictionary
# compare them
# if the user select the higher one correct, than eliminate the lower one from the dictionary list
# compare the former higher one, with the new one from the dictionary
# keep going until the user answers the correct one
# for each correct answer give +1 score to the user
# for each incorrect one take -1 from the scores
# the game is over when the user gives incorrect answer = lower answer

# the higher one becomes the value A after it is selected even though it starts as B

import random
import game_data

# value A and value B should be variables to be updated
value_A = []
value_B = []

# this should be a function
data_collection = game_data.data

def compare(value_1, value_2):
    follower_count_1 = int(value_1['follower_count'])
    follower_count_2 = int(value_2['follower_count'])
    # compare the numbers, find the higher one
    if follower_count_1 > follower_count_2:
        return "A"
    elif follower_count_2 > follower_count_1:
        return "B"

def find_the_higher_one(value_1, value_2):
    global value_A
    follower_count_1 = int(value_1['follower_count'])
    follower_count_2 = int(value_2['follower_count'])
    # compare the numbers, find the higher one
    if follower_count_1 > follower_count_2:
        value_A = value_1
        return value_A
    elif follower_count_2 > follower_count_1:
        value_A = value_2
        return value_A 


def remove_lower_item(list_game, value_1, value_2):
    follower_count_1 = int(value_1['follower_count'])
    follower_count_2 = int(value_2['follower_count'])
    # compare the numbers, find the higher one
    if follower_count_1 > follower_count_2:
        list_game.remove(value_2)
        return list_game
    elif follower_count_2 > follower_count_1:
        list_game.remove(value_1)
        return list_game

def select_items(list_game):
    # set the number to select here.
    num_to_select = 2
    list_of_random_items = random.sample(list_game, num_to_select)
    first_random_item = list_of_random_items[0]
    second_random_item = list_of_random_items[1]
    print('Compare A', first_random_item["name"])
    print('Compare B', second_random_item["name"])
    return first_random_item, second_random_item

def reselect_items(list_game, value_1):
    # set the number to select here.
    num_to_select = 1
    list_of_random_items = random.sample(list_game, num_to_select)
    second_item = list_of_random_items[0]
    print('Compare A', value_1["name"])
    print('Compare B', second_item["name"])
    return second_item


user_answer = ""
score = 0
game_over = False

# randomly select 2 values at the beginning
value_A, value_B = select_items(data_collection)
correct_answer = compare(value_A, value_B)


while not game_over:
    user_answer = input("Who has more followers? Type 'A' or 'B'\n")

    if correct_answer == user_answer :
        
        print("Correct answer")
        score += 1
        print(f"Score is {score}")

        # remove the value_B from the dictionary
        remove_lower_item(data_collection, value_A, value_B)

        # value_B update, value_A update
        value_A = find_the_higher_one(value_A, value_B)
        value_B = reselect_items(data_collection, value_A)
        correct_answer = compare(value_A, value_B)

    else:
        print("Game is over. Your score is: ", score)
        game_over = True
