from love_letter.base_struct.action import *
from love_letter.objects import *

class LoveLetterArrestPlayerAction(LoveLetterAction):
    def __init__(self, player: LoveLetterPlayer, arrested_player: LoveLetterPlayer, character: LoveLetterCharacter):
        LoveLetterAction.__init__(self)

        self._player = player
        self._target = arrested_player
        self._character = character

    def get_effective_player(self) -> LoveLetterPlayer:
        return self._player
    
    def get_arrested_player(self) -> LoveLetterPlayer:
        return self._player
    
    def get_arrested_character(self) -> LoveLetterCharacter:
        return self._character


