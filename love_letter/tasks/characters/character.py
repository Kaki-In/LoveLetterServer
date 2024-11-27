from love_letter.base_struct.task import *
from love_letter.objects import *

class LoveLetterCharacterTask(LoveLetterTask):
    def __init__(self, player: LoveLetterPlayer):
        self._player = player

    def get_effective_player(self) -> LoveLetterPlayer:
        return self._player
