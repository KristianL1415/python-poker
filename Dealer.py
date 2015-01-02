# Dealer.py
# controls the actual game flow and logic

import Game
import CardDeck

class Dealer():
    def __init__(self):
        self.currentGame = self.setupNewGame()
        self.currentDeck = CardDeck.CardDeck()

    def setupNewGame(self):
        # choose num of human and ai players
        print("Welcome to the poker room!\n")
        numPlayers = raw_input("How many people (including yourself) would you like to play with? \n")
        currentGame = Game.Game(numPlayers)
        self.dealHand()
        # arrange players around the table

    def dealHand(self):
        # set blinds, dealer and deal hand
        print("Dealing hand.")
