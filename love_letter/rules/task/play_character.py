from .task import *

from ...objects.context.board import *

class LoveLetterPlayCharacterTask(LoveLetterTask):
    def __init__(self, player: LoveLetterPlayer, character: LoveLetterCharacter):
        super().__init__()

        self._player = player
        self._character = character
    
    def get_effective_player(self) -> LoveLetterPlayer:
        return self._player
    
    def get_character(self) -> LoveLetterCharacter:
        return self._character


