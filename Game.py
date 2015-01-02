# Game.py
# object used to keep track of game state during the poker match

class Game():
    def __init__(self, totalPlayers):
        self.totalPlayerCount = int(totalPlayers)
        self.aiPlayerCount = self.totalPlayerCount - 1 # one human for now, change later
        self.humanPlayerCount = 1 # again, one human for now
