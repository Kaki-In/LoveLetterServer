from .cards import *
from .player import *

import asyncio as _asyncio

class LoveLetterRound():
    def __init__(self, players, active_player):
        self._draw = LoveLetterDraw()
        self._hidden = self.drawCard()
        self._removed = []
        
        if len(players) == 2:
            for _ in range(3):
                self._removed.append( self.drawCard() )
        
        self._players = players
        self._active_player = active_player
    
    def players(self):
        return self._players
    
    def removedCards(self):
        return self._removed
    
    def hiddenCard(self):
        return self._hidden
    
    def drawCard(self):
        if len(self._draw):
            return self._draw.takeCard()
        else:
            hidden = self._hidden
            self._hidden = None
            return hidden
    
    def activePlayer(self):
        return self._players[ self._active_player ]
    
    def availablePlayers(self):
        players = []
        for player in self._players:
            if not (player.hasBeenKilled() or player.isProtected()):
                players.append(player)
        
        return players

    def selectNextPlayer(self):
        while True:
            self._activePlayer = (self._active_player + 1) % len( self._players )
            if not self._players[ self._active_player ].hasBeenKilled():
                break

    def alivePlayers(self):
        players = []
        
        for player in players:
            if not player.hasBeenKilled():
                players.append(player)
        
        return players
    
    async def getPlayer(self, remove_self = True):
        player = self.activePlayer()
        players = self.availablePlayers()
        
        if remove_self:
            players.remove(player)
        
        if not players:
            return

        return await player.getController().choosePlayerBetween(players)
    
    def getDraw(self):
        return self._draw
    
