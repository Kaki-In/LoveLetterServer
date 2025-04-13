from love_letter.base_struct.task import *
from love_letter.context import *
from love_letter.configuration import *

class LoveLetterCharacterTask(LoveLetterTask):
    def __init__(self, player: LoveLetterPlayer):
        LoveLetterTask.__init__(self)
        
        self._player = player

    def get_effective_player(self) -> LoveLetterPlayer:
        return self._player
