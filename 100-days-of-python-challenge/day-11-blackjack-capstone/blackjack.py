import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

user_cards = []
computer_cards = []

def deal_card():
    """Returns a random card from the deck."""
    return random.choice(cards)

def stop_game(user_cards, computer_cards):
    computer_cards.append(deal_card())
    print(f"\n Computer's final hand: {computer_cards}, final score: {sum(computer_cards)} \n")
    if sum(user_cards) > 21:
        print(" You went over. You lose \n")
    elif sum(computer_cards) > 21:
        print(" Computer went over. You win \n")
    elif sum(user_cards) > sum(computer_cards):
        print(" You win \n")
    elif sum(user_cards) < sum(computer_cards):
        print(" You lose \n")
    else:
        print(" It's a draw \n")

play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")

user_cards.append(deal_card())
user_cards.append(deal_card())
computer_cards.append(deal_card())

if play == 'n':
    print("Game over")

elif play == 'y':    
    while play == 'y':

        print(f"\n Your cards: {user_cards}, current score: {sum(user_cards)}")
        print(f" Computer's first card: {computer_cards[0]}\n")

        if sum(user_cards) == 21:
            stop_game(user_cards, computer_cards)
            break

        else: continue_game = input("Type 'y' to get another card, type 'n' to pass: ")
    
        while continue_game == 'y':
            user_cards.append(deal_card())
            print(f"\n Your cards: {user_cards}, current score: {sum(user_cards)}")
            if sum(user_cards) >= 21:
                break
            else:
                continue_game = input("Type 'y' to get another card, type 'n' to pass: ")
    
        if continue_game == 'n':
            stop_game(user_cards, computer_cards)
            break
        elif sum(user_cards) >= 21:
            stop_game(user_cards, computer_cards)
            break
        else:
            print("Invalid input select 'y' or 'n'")
else:
    print("Invalid input select 'y' or 'n'")