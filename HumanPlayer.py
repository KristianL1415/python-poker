# HumanPlayer.py
# controls the human actions for a player
# In the future this should inherit from Player class

import Card

class HumanPlayer(object):
    def __init__(self, startingChipCount):
        self.chipCount = startingChipCount
        self._firstCard = None
        self._secondCard = None

    def get_firstCard(self):
        return self._firstCard

    def set_firstCard(self, value):
        self._firstCard = value

    def get_secondCard(self):
        return self._secondCard

    def set_secondCard(self, value):
        self._secondCard = value

    firstCard = property(get_firstCard, set_firstCard)
    secondCard = property(get_secondCard, set_secondCard)

    def check():
        # player checks
        print("Checking")

    def bet(amount):
        # player bets an amount
        print(amount)

    def fold():
        # player folds
        print ("Folding")
