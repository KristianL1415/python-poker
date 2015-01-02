# HumanPlayer.py
# controls the human actions for a player
# In the future this should inherit from Player class

import Card

class HumanPlayer():
    def __init__(self, startingChipCount):
        self.chipCount = startingChipCount
        emptyCard = Card.Card(" ", " ")
        self.hand = [emptyCard, emptyCard]

    def check():
        # player checks
        print("Checking")

    def bet(amount):
        # player bets an amount
        print(amount)

    def fold():
        # player folds
        print ("Folding")
