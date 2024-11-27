from love_letter.base_struct.response import *
from love_letter.enum import *

class LoveLetterChooseCardResponse(LoveLetterClientResponse):
    def __init__(self, card: LOVE_LETTER_PLAYER_CARD):
        super().__init__('cards.choose', {
            'card': card
        })

        self._card = card

    def get_card(self) -> LOVE_LETTER_PLAYER_CARD:
        return self._card

