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

game_data_list = game_data.data
print(game_data_list)
# set the number to select here.
num_to_select = 2                           
list_of_random_items = random.sample(game_data_list, num_to_select)
first_random_item = list_of_random_items[0]
second_random_item = list_of_random_items[1]
print('Compare A', first_random_item)
print('Compare B', second_random_item)

# eliminate the lower item from the list
#print(first_random_item['follower_count'])
#print(second_random_item['follower_count'])

def compare():
    follower_count_1 = int(first_random_item['follower_count'])
    follower_count_2 = int(second_random_item['follower_count'])
    # compare the numbers, find the higher one
    if follower_count_1 > follower_count_2:
        print(first_random_item['name'], "has higher")
        return "A"
    elif follower_count_2 > follower_count_1:
        print(second_random_item['name'], "has higher")
        return "B"

user_answer = input("Who has more followers? Type 'A' or 'B'\n")
correct_answer = compare()

if correct_answer == user_answer:
    print("Correct answer")
else:
    print("Incorrect answer")


