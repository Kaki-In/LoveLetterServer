from love_letter.base_struct.action import *
from love_letter.enum import *
from love_letter.context import *

class LoveLetterDiscardAction(LoveLetterAction):
    def __init__(self, player: LoveLetterPlayer, card: LoveLetterCard, player_card: LOVE_LETTER_PLAYER_CARD, reason: LOVE_LETTER_DISCARD_REASON):
        LoveLetterAction.__init__(self)

        self._player = player
        self._reason = reason
        self._player_card = player_card
        self._card = card

    def get_card(self) -> LoveLetterCard:
        return self._card
    
    def get_reason(self) -> LOVE_LETTER_DISCARD_REASON:
        return self._reason
    
    def get_player(self) -> LoveLetterPlayer:
        return self._player
    
    def get_player_card(self) -> LOVE_LETTER_PLAYER_CARD:
        return self._player_card

