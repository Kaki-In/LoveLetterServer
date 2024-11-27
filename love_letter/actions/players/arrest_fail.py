from love_letter.base_struct.action import *
from love_letter.board import *

class LoveLetterArrestPlayerFailedAction(LoveLetterAction):
    def __init__(self, player: LoveLetterPlayer, arrested_player: LoveLetterPlayer, failing_character: LoveLetterCharacter):
        super().__init__()

        self._player = player
        self._target = arrested_player
        self._character = failing_character

    def get_effective_player(self) -> LoveLetterPlayer:
        return self._player
    
    def get_arrested_player(self) -> LoveLetterPlayer:
        return self._player
    
    def get_failing_character(self) -> LoveLetterCharacter:
        return self._character


