import asyncio as _asyncio

UNSAFE_NO_SUCH_TARGET    = 0
UNSAFE_SELF_IS_TARGET    = 1
UNSAFE_COUNTESS_PRESENCE = 2
UNSAFE_IS_SUICIDE        = 3
SAFE                     = 4

class LoveLetterCharacter():
    async def makeAction(round):
        pass
    
    def isSafe(round):
        return SAFE
    
    async def onDiscard(player):
        pass
    
    def getName():
        return ""
    
    def getValue():
        return 0
    
    def __lt__(self, second_character):
        return self.getValue() < second_character.getValue()
    
    def __gt__(self, second_character):
        return self.getValue() > second_character.getValue()
    
    def __eq__(self, second_character):
        return self.getValue() == second_character.getValue()

class LoveLetterGuard(LoveLetterCharacter):
    async def makeAction(round):
        target_player = await round.getPlayer()
        
        if target_player is None:
            return
        
        target_character = await round.activePlayer().getController().chooseCharacterForGuard()
        player_card = target_player.getCard()
        
        if player_card.getCharacter() == target_character:
            await round.kill(target_player)
    
    def isSafe(round):
        if round.availablePlayers() == [ round.activePlayer() ]:
            return UNSAFE_NO_SUCH_TARGET
        
        return SAFE

    def getName():
        return "Garde"

    def getValue():
        return 1

class LoveLetterPriest(LoveLetterCharacter):
    async def makeAction(round):
        active_player = round.activePlayer()
        target_player = await round.getPlayer()
        
        if target_player:
            await target_player.getController().displayCard(target_player)
        
    def isSafe(round):
        if round.availablePlayers() == [round.activePlayer()]:
            return UNSAFE_NO_SUCH_TARGET
        
        return SAFE

    def getName():
        return "Prêtre"
    
    def getValue():
        return 2

class LoveLetterBaron(LoveLetterCharacter):
    async def makeAction(round):
        player = round.activePlayer()
        target = await round.getPlayer()
        
        if target is None:
            return
        
        player_card = player.getController().chooseCard()
        target_card = target.getController().chooseCard()
        
        await _asyncio.gather(player.displayCard(target), target.displayCard(player))
        
        if player_card > target_card:
            await round.kill(target)
        
        elif player_card < target_card:
            await round.kill(player)
    
    def isSafe(round):
        if round.availablePlayers() == [round.activePlayer()]:
            return UNSAFE_NO_SUCH_TARGET
        
        return True

    def getName():
        return "Baron"
    
    def getValue():
        return 3

class LoveLetterServant(LoveLetterCharacter):
    async def makeAction(round):
        await round.protect(round.activePlayer())
    
    def getName():
        return "Servante"
    
    def getValue():
        return 4

class LoveLetterPrince(LoveLetterCharacter):
    async def makeAction(round):
        target = await round.getPlayer(False)
        answer = await target.discard()
        
        if not target.hasBeenKilled():
            await target.drawCard(round.getDraw().takeCard())
        
        return answer
    
    def isSafe(round):
        player = round.activePlayer()
        
        if LoveLetterCountess in ( player.getCard().getCharacter(), player.getDrawnCard().getCharacter()):
            return UNSAFE_COUNTESS_PRESENCE
        
        if round.availablePlayers() == [player]:
            return UNSAFE_SELF_IS_TARGET

        return SAFE

    def getName():
        return "Prince"
    
    def getValue():
        return 5

class LoveLetterKing(LoveLetterCharacter):
    async def makeAction(round):
        player = round.activePlayer()
        target = round.getPlayer()
        
        if target is None:
            return
        
        player_card = player.getCard()
        target_card = target.getCard()
        
        await player.replaceCard(target_card)
        await target.replaceCard(player_card)
        
    def isSafe(round):
        player = round.activePlayer()
        
        if LoveLetterCountess in ( player.getCard().getCharacter(), player.getDrawnCard().getCharacter()):
            return UNSAFE_COUNTESS_PRESENCE
        
        if round.availablePlayers() == [player]:
            return UNSAFE_SELF_IS_TARGET

        return SAFE
    
    def getName():
        return "Roi"
    
    def getValue():
        return 6

class LoveLetterCountess(LoveLetterCharacter):
    def getName():
        return "Comtesse"
    
    def getValue():
        return 7

class LoveLetterPrincess(LoveLetterCharacter):
    async def makeAction(round):
        pass
    
    def isSafe(round):
        return UNSAFE_IS_SUICIDE
    
    async def onDiscard(self, player):
        await round.kill( player )
    
    def getName():
        return "Princesse"
    
    def getValue():
        return 8

