# ComputerPlayer.py
# controls the actions of the ai player in each game
# In the future this should inherit from Player class

import Card

class ComputerPlayer(object):
    def __init__(self, startingChipCount):
        self.chipCount = startingChipCount
        self.firstCard = Card.Card(" ", " ")
        self.secondCard = Card.Card(" ", " ")

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
