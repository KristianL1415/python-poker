# Game.py
# object used to keep track of game state during the poker match

import HumanPlayer
import ComputerPlayer

class Game():
    def __init__(self, totalPlayers):
        self.totalPlayerCount = int(totalPlayers)
        self.playersRemaining = self.totalPlayerCount
        self.playerArray = []
        self.playerArray.append(HumanPlayer.HumanPlayer(500)) # eventually allow custom chip counts
        for i in range(0, (self.totalPlayerCount - 1)):
            self.playerArray.append(ComputerPlayer.ComputerPlayer(500))

        # I don't think I need these two properties..
        #self.aiPlayerCount = self.totalPlayerCount - 1 # one human for now, change later
        #self.humanPlayerCount = 1 # again, one human for now
