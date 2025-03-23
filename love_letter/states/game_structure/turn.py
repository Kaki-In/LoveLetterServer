from love_letter.enum import *
from love_letter.base_struct.states import *

from love_letter.board import *

import typing as _T

class LoveLetterTurnState(LoveLetterNeedingCardState):
    def __init__(self, player: LoveLetterPlayer):
        LoveLetterNeedingCardState.__init__(self)

        self._player = player
    
    def get_player(self) -> LoveLetterPlayer:
        return self._player

