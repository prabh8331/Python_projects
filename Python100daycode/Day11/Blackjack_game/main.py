import random as r

import os 

from art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]  # this had to become a global variable because it is being directly called in other functions 

def ace_cards_check(cards_input, new_card_input):
    """This function will if new draw card is ace and total > 21, then Ace card value will become 1 else it will be 11"""
    total=sum(cards_input+[new_card_input])
    if total>21 and new_card_input == 11:
        new_card_input=1
        return cards_input+[new_card_input]
    else:
        return cards_input+[new_card_input]


def dealer_must_draw(dealer_cards_input):
    """Once player game is completed and dealer's card's value is <17 then Dealer will have to draw a new card"""
    while sum(dealer_cards_input)<17:
        dealer_new_card=r.choice(cards)
        dealer_cards_input = ace_cards_check(dealer_cards_input,dealer_new_card)
    return dealer_cards_input

#concept of local variable I had to pass dealer_cards in game function 
#because inside I am defining dealer_cards , 

def reveal(user_cards,dealer_cards):
    """Once game is over this function will reveal the final cards"""
    os.system('cls')
    print(logo)
    print(f"Your cards are: {user_cards} and cards total is: {sum(user_cards)}")
    print(f"Dealer's cards are: {dealer_cards} and cards total is: {sum(dealer_cards)}")  


def game(user_cards,dealer_cards):
    """If there is no initial blackjack happens this game will be executed"""
    os.system('cls')
    print(logo)
    print(f"Your cards are: {user_cards} and cards total is: {sum(user_cards)}")
    print(f"Dealer's first card is: {dealer_cards[0]}")
    choose=input("Do you want to Hit or Stand?: ").lower()
    if choose == "stand":
        dealer_cards=dealer_must_draw(dealer_cards)
        user_total=sum(user_cards)
        dealer_total=sum(dealer_cards)
        reveal(user_cards,dealer_cards)
        if dealer_total > 21:
            print("Dealer Bust!, You Win!")
        elif user_total>dealer_total:
            print("Win.")
        elif user_total<dealer_total:
            print("Loose.")
        elif user_total==dealer_total:
            print("Push.")
    elif choose == "hit":
        user_new_card=r.choice(cards)
        user_cards = ace_cards_check(user_cards,user_new_card)
        user_total=sum(user_cards)
        if user_total > 21:
            reveal(user_cards,dealer_cards)
            print("Bust, Loose.")
        elif user_total == 21:
            dealer_cards=dealer_must_draw(dealer_cards)
            dealer_total=sum(dealer_cards)
            if dealer_total > 21:
                reveal(user_cards,dealer_cards)
                print("You Win and Dealer Bust!")
            elif dealer_total == 21:
                reveal(user_cards,dealer_cards)
                print("Push.")
            elif dealer_total < 21:
                reveal(user_cards,dealer_cards)
                print("Win!")
        else: 
            game(user_cards,dealer_cards)
            
    else:
        print("Wrong Input!")


def blackjack_play():
    """Play Blackjack"""
    user_cards=[]
    dealer_cards=[]

    user_new_card=r.choice(cards)
    dealer_new_card=r.choice(cards)

    user_cards.append(user_new_card)
    dealer_cards.append(dealer_new_card)

    user_new_card=r.choice(cards)
    dealer_new_card=r.choice(cards)

    user_cards = ace_cards_check(user_cards,user_new_card)
    dealer_cards = ace_cards_check(dealer_cards,dealer_new_card)            

    user_total=sum(user_cards)
    dealer_total=sum(dealer_cards)

    if user_total==21 and dealer_total==21:
        reveal(user_cards,dealer_cards)
        print("Push")
    elif user_total==21 and dealer_total<21:
        reveal(user_cards,dealer_cards)
        print("Blackjack! Win.")
    elif user_total<21 and dealer_total==21:
        reveal(user_cards,dealer_cards)
        print("Dealer's Blackjack. Loose.")
    else:
        game(user_cards,dealer_cards)


continue_game=True

while continue_game==True:
    blackjack_play()
    if input("Do you want to continue playing? y/n:  ").lower() == "n":
        continue_game=False