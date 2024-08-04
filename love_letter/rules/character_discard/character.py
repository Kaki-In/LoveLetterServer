from ...objects.context.board import *

class LoveLetterDiscardCharacterRule():
    def __init__(self, player: LoveLetterPlayer, contrainer: LoveLetterPlayer):
        super().__init__()

        self._player = player
        self._contrainer = contrainer
    
    def get_effective_player(self) -> LoveLetterPlayer:
        return self._player
    
    def get_contrainer(self) -> LoveLetterPlayer:
        return self._contrainer
