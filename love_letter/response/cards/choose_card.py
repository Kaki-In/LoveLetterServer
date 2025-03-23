import typing as _T
from love_letter.base_struct.response import *
from love_letter.enum import *
from love_letter.board import *

class LoveLetterChooseCardResponse(LoveLetterClientResponse):
    def __init__(self, card: LOVE_LETTER_PLAYER_CARD):
        LoveLetterClientResponse.__init__(self)

        self._card = card

    def get_card(self) -> LOVE_LETTER_PLAYER_CARD:
        return self._card
