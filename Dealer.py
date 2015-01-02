# Dealer.py
# controls the actual game flow and logic

import Game
import CardDeck

class Dealer():
    def __init__(self):
        self.currentGame = self.setupNewGame()
        self.currentDeck = CardDeck.CardDeck()
        self.button = 0 # human starts on the button until card flip is implemented

    def setupNewGame(self):
        # choose num of human and ai players
        print("Welcome to the poker room!\n")
        numPlayers = raw_input("How many players will be in this game? \n")
        newGame = Game.Game(numPlayers)
        return newGame

    def dealHand(self):
        # set blinds, dealer and deal hand
        print("Dealing hand.\n")
        self.currentDeck.shuffle()
        self.dealCards()

    def dealCards(self):
        #players = self.currentGame.playerArray
        playerIndex = self.getNextPlayerIndex(self.button + 1)

        for i in range(0, len(self.currentGame.playerArray) * 2):
            #currentPlayer = self.currentGame.playerArray[playerIndex]
            if (i < len(self.currentGame.playerArray) - 1):
                # Deal first card
                self.currentGame.playerArray[playerIndex].hand[0] = self.currentDeck.cards[i]
                print(self.currentDeck.cards[i].suit + self.currentDeck.cards[i].value)
            else:
                # Deal second card
                self.currentGame.playerArray[playerIndex].hand[1] = self.currentDeck.cards[i]

        #print(self.currentGame.playerArray[0].hand)
        print("Your hand is " + self.currentGame.playerArray[0].hand[0].suit
                              + self.currentGame.playerArray[0].hand[0].value + " "
                              + self.currentGame.playerArray[0].hand[1].suit
                              + self.currentGame.playerArray[0].hand[1].value + ".")

    def getNextPlayerIndex(self, currentPos):
        arrayLength = len(self.currentGame.playerArray)
        nextPos = currentPos + 1
        if (nextPos > arrayLength - 1):
            return 0
        else:
            return nextPos

    def getPreviousPlayerIndex(self, currentPos):
        arrayLength = len(self.currentGame.playerArray)
        prevPos = currentPos - 1
        if (prevPos < 0):
            return arrayLength - 1
        else:
            return prevPos
