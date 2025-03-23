from .state import *

from love_letter.enum import *
import typing as _T

class LoveLetterNeedingCardState(LoveLetterState):
    def __init__(self):
        LoveLetterState.__init__(self)

        self._player_card: _T.Optional[LOVE_LETTER_PLAYER_CARD] = None

    def get_chosen_player_card(self) -> LOVE_LETTER_PLAYER_CARD:
        if self._player_card is None:
            raise TypeError("this state has not been given a player yet")

        return self._player_card
    
    def set_chosen_player_card(self, player_card: LOVE_LETTER_PLAYER_CARD):
        self._player_card = player_card

    def has_chosen_player(self) -> bool:
        return self._player_card is not None

