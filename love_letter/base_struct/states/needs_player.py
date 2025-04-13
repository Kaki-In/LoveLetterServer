from love_letter.context import *
from .state import *

import typing as _T

class LoveLetterNeedingPlayerState(LoveLetterState):
    def __init__(self, possibilities: list[LoveLetterPlayer]):
        LoveLetterState.__init__(self)

        self._player: _T.Optional[LoveLetterPlayer] = None
        self._player_possibilities = possibilities

    def get_chosen_player(self) -> LoveLetterPlayer:
        if self._player is None:
            raise TypeError("this state has not been given a player yet")

        return self._player
    
    def set_chosen_player(self, player: LoveLetterPlayer):
        self._player = player

    def has_chosen_player(self) -> bool:
        return self._player is not None
    
    def get_chosable_players(self) -> list[LoveLetterPlayer]:
        return self._player_possibilities.copy()

