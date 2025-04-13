from love_letter.base_struct.response import *
from love_letter.enum import *
from love_letter.context import *
import typing as _T

class LoveLetterChoosePlayerResponse(LoveLetterClientResponse):
    def __init__(self, player: LoveLetterPlayer):
        LoveLetterClientResponse.__init__(self)

        self._player = player

    def get_player(self) -> LoveLetterPlayer:
        return self._player
