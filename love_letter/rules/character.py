from ..objects import *

import typing as _T

def _abstract_async_method(f):
    async def raiseNotImplemented(*a, **b) -> _T.Any:
        raise NotImplementedError("This class is only abstract. Please use your own client")
    
    return raiseNotImplemented

def _abstract_method(f):
    def raiseNotImplemented(*a, **b) -> _T.Any:
        raise NotImplementedError("This class is only abstract. Please use your own client")
    
    return raiseNotImplemented

class LoveLetterCharacterRule():
    def __init__(self):
        pass
    
    @_abstract_async_method
    async def execute_on_player_turn(self, round: LoveLetterRound) -> _T.NoReturn:
        pass
    
    @_abstract_async_method
    async def execute_on_discarded(self, round: LoveLetterRound, player: LoveLetterPlayer) -> _T.NoReturn:
        pass
    
    @_abstract_method
    def can_be_safely_laid(self, round: LoveLetterRound) -> bool:
        return True

class LoveLetterGuardRule(LoveLetterCharacterRule):
    def __init__(self):
        super().__init__()
    
    async def execute_on_player_turn(self, round: LoveLetterRound) -> _T.NoReturn:
        target_player = await round.active_player()
        
        if target_player is None:
            return
        
        target_character = await round.activePlayer().getController().chooseCharacterForGuard()
        player_card = target_player.getCard()
        
        if player_card.getCharacter() == target_character:
            await round.kill(target_player)
    


