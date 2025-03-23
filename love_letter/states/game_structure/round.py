from .turn import *

from love_letter.base_struct.states import *
from love_letter.board import *

import typing as _T

class LoveLetterRoundState(LoveLetterNeedingObjectState[LoveLetterTurnState]):
    def __init__(self, playing_player: LoveLetterPlayer):
        self._player = playing_player

    def get_playing_player(self) -> LoveLetterPlayer:
        return self._player
    
