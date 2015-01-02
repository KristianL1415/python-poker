# CardDeck.py
# Manages the deck of 52 cards for the poker game

import Card

class CardDeck():
    # Standard 52 card deck initializer
    def __init__(self):
        self.cards = []
        suits = ["heart", "diamond", "spade", "club"]
        values = ["2", "3", "4", "5", "6", "7","8", "9", "10", "J", "Q", "K", "A"]

        for i in range(0, 4):
            for j in range(0, 13):
                self.cards.append(Card.Card(suits[i], values[j]))

    def shuffle(self):
        if (len(self.cards) == 52):
            print("Shuffling")
