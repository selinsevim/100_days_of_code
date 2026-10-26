import random
import art
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def calculate_scores(score_list):
    total = 0
    for score in score_list:
        total += score
    return total

game_over = False
while True:
    game_over = True
    print(art.logo)
    answer = input("Do you want to play a game of blackjack? Type 'y' or 'n'.\n")
    if answer == 'y':
        user_cards = random.sample(cards, 2)
        computer_cards = random.sample(cards, 2)
        print("Your cards", user_cards)
        print("Computer's first card: ",computer_cards[0])
        total_user_cards = calculate_scores(user_cards)
        total_computer_cards = calculate_scores(computer_cards)
        print("User cards total", total_user_cards)
        print("Computer cards total", total_computer_cards)
        # Do the initial checks
        if total_user_cards == 21:
            print("Winner is user")
            game_over = True
        if total_computer_cards == 21:
            print("Winner is computer")
            game_over = True
        # You get asked to get another card or not
        #get_another_card = input("Type 'y' to get another card, type 'n' to pass.\n")
        users_turn = True
        while users_turn:
            get_another_card = input("Type 'y' to get another card, type 'n' to pass.\n")
            if get_another_card == 'y':
                print("It is users turn")
                user_card_addition = random.sample(cards, 1)
                # add this to the list
                user_cards += user_card_addition
                total_user_cards = calculate_scores(user_cards)
                print("Users cards are:", user_cards)
                print("User cards total", total_user_cards)
                users_turn = True
                if total_user_cards > 21:
                    print("User went over 21, computer wins")
                    users_turn = False
                    game_over = True
                    #print("\n" * 20)
                if total_user_cards == 21:
                    print("User wins")
                    users_turn = False
                    game_over = True
            if get_another_card == 'n':
                print("It is users turn")
                users_turn = False
                user_cards = user_cards
                print("You said no, user cards are", user_cards)
                while total_computer_cards <= 16:
                    users_turn = False
                    print("It is computers turn")
                    computer_card_addition = random.sample(cards, 1)
                    computer_cards += computer_card_addition
                    total_computer_cards = calculate_scores(computer_cards)
                    print("Computer cards are:", user_cards)
        if total_user_cards == 21 or total_computer_cards == 21:
            game_over = True
            print("You win")
        if 21 >= total_user_cards > total_computer_cards:
            game_over = True
            print("Users win")
        elif 21 >= total_computer_cards > total_user_cards:
            game_over = True
            print("Computer win")
        elif total_computer_cards == total_user_cards:
            game_over = True
            print("Draw")
    if answer == 'n':
        break
