import random
import art
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
user_cards = []
computer_cards = []

def calculate_scores(score_list):
    total = 0
    for score in score_list:
        total += score
    return total

def compare(users_card, computers_card, users_score, computers_score):
    if 21 == computers_score == users_score:
        print("Draw")
    elif users_score == 21 and len(users_card) > 2:
        print("User wins")
    elif computers_score == 21 and len(computers_card) > 2:
        print("Computer wins")
    elif 21 >= users_score > computers_score:
        print("User wins")
    elif 21 >= computers_score > users_score:
        print("Computer wins")
    elif computers_score == users_score:
        print("Draw")
    elif computers_score > 21 >= users_score:
        print("User wins")
    elif users_score > 21 >= computers_score:
        print("Computer wins")


while True:
    print(art.logo)
    game_over = False
    answer = input("Do you want to play a game of blackjack? Type 'y' or 'n'.\n")

    while not game_over:

        if answer == 'y':
            user_cards = random.sample(cards, 2)
            computer_cards = random.sample(cards, 2)
            print("Your cards", user_cards)
            print("Computer cards", computer_cards)
            print("Computer's first card: ",computer_cards[0])
            total_user_cards = calculate_scores(user_cards)
            total_computer_cards = calculate_scores(computer_cards)

            # Do the initial checks to see if there is any winner
            if total_computer_cards == 21 and len(computer_cards) == 2 and total_user_cards == 21 and len(user_cards) == 2:
                print("It is a draw,  already blackjack with 2 cards")
                game_over = True
            elif total_user_cards == 21 and len(user_cards) == 2:
                print("Winner is user, already blackjack with 2 cards")
                game_over = True
            elif total_computer_cards == 21 and len(computer_cards) == 2:
                print("Winner is computer,  already blackjack with 2 cards")
                game_over = True

            # Then it is users to make decisions if the game still continues
            users_turn = True
            while users_turn and not game_over:
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
                    users_turn = False
                    user_cards = user_cards
                    print("It is computers turn")
                    print("User said no, user cards are", user_cards)

            while total_computer_cards <= 16 and not game_over:
                print("It is computers turn")
                computer_card_addition = random.sample(cards, 1)
                computer_cards += computer_card_addition
                total_computer_cards = calculate_scores(computer_cards)
                print("Computer cards are:", computer_cards)
                print("Total computer score: ", total_computer_cards)

            if not game_over:
                # Compare the cards
                compare(user_cards, computer_cards, total_user_cards, total_computer_cards)
                game_over = True

        if answer == 'n':
            break