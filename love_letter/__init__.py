from .round import *

class LoveLetterGame():
    def __init__(self, players):
        self._round = None
        self._actualRound = None
        self._players = players
        
    async def initRound(self):
        self._actualRound = LoveLetterRound( self._players )

    async def play(self):
        player = self.activePlayer()
        await player.stopProtection()
        
        await player.takeCard(self.drawCard())
        
        card = await player.controller.chooseCard(player.getCard(), player.getDrawnCard())
        await card.getCharacter().makeAction(self)
#        self.disp.displayHistory(card.play(self))
#        self.kbd.wait()
