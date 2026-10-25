import random
import art
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def calculate_scores(score_list):
    total = 0
    for score in score_list:
        total += score
    return total

while True:
    print(art.logo)
    answer = input("Do you want to play a game of blackjack? Type 'y' or 'n'.\n")
    if answer == 'y':
        user_cards = random.sample(cards, 2)
        computer_cards = random.sample(cards, 2)
        print(user_cards)
        print(computer_cards)
        total_user_cards = calculate_scores(user_cards)
        total_computer_cards = calculate_scores(computer_cards)
        print("User cards total", total_user_cards)
        print("Computer cards total", total_computer_cards)
        if total_user_cards == 21:
            print("Winner is user")
            break
        if total_computer_cards == 21:
            print("Winner is computer")
            break
        # You get asked to get another card or not
        get_another_card = input("Type 'y' to get another card, type 'n' to pass.\n")
        if get_another_card == 'y':
            user_card_addition = random.sample(cards, 1)
            # add this to the list
            user_cards += user_card_addition
            total_user_cards = calculate_scores(user_cards)
            print("Users cards are:", user_cards)
            if total_user_cards > 21:
                print("You went over 21, you lose")
                print("\n" * 20)
        if get_another_card == 'n':
            user_cards = user_cards
            print("user cards is", user_cards)
        if total_user_cards == 21 or total_computer_cards == 21:
            print("You win")

    if answer == 'n':
        break
