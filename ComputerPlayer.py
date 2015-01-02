# ComputerPlayer.py
# controls the actions of the ai player in each game
# In the future this should inherit from Player class

import Card

class ComputerPlayer():
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
