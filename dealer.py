# dealer.py
# controls the actual game flow and logic

import Game

def setupNewGame():
    # choose num of human and ai players
    print("Welcome to the poker room!\n")
    numPlayers = raw_input("How many people (including yourself) would you like to play with? \n")
    currentGame = new Game(numPlayers)
    # arrange players around the table

def dealHand():
    # set blinds and
