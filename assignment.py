# Programmer: Kristina Mueller
# Course: CS701/GB-731, Dr. Yalew
# Date: 08/23/2024
# Programming Assignment: 6
# Function that generates a shuffled deck of 52 cards.
# Function that returns the name of a card given its string representation.
# Function that displays the names of the cards in a hand.
# Function that calculates and returns the total value of a hand.

import random

# Function that generates a shuffled deck of 52 cards.
def main():

    suits = ["Diamonds", "Hearts", "Spades", "Clubs"]
    ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]

    def generate_deck():
        deck = []

        for suit in suits:
            for rank in ranks:
                card = rank + " "+ "of" + " " + suit
                deck.append(card)
        random.shuffle(deck)
        return deck
    
    deck = generate_deck()
    for card in deck:
        print(card)

# Function that returns the name of a card given its string representation.

    def card_name(card_str):
        split_name = card_str.split(" of ")
        rank, suit = split_name
        return "This card is " + rank + " of " + suit
        
#try it out
    card_str = "9 of Diamonds"
    print(card_name(card_str))

# Function that displays the names of the cards in a hand.
    def display_hand(hand):
        for card in hand:
            card = card.split(" of ")
            rank, suit = card
            print("This card is " + rank + " of " + suit)
        
#try it out
    my_hand=["7 of Hearts", "Ace of Spades"]
    display_hand(my_hand)

# Function that calculates and returns the total value of a hand.
    def hand_value(hand):
        card_values = {"2": 2, "3" : 3, "4" : 4, "5": 5, "6" : 6, "7" : 7, "8": 8, "9" : 9, "10": 10, "Jack": 10, 
                       "Queen": 10, "King": 10, "Ace": 11}
        total = 0

        for card in hand:
            card = card.split(" of ")
            rank, suit = card
            rank = rank.strip()
            if rank in card_values:
                total += card_values[rank]
            else: 
                print("Rank not found, check capitalization")
        
        return total
#try it out
    my_hand=["9 of Clubs", "Ace of Spades"]
    print(hand_value(my_hand))

if __name__ == "__main__":
    main()