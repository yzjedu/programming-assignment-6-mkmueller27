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
        split_name = card_str.split("of")
        rank, suit = split_name
        print("This card is", rank, "of", suit)
#try it out
    card_str = "9 of diamonds"
    print(card_name(card_str))