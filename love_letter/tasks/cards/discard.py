from love_letter.base_struct.task import *
from love_letter.context import *
from love_letter.enum import *

class LoveLetterDiscardTask(LoveLetterTask):
    def __init__(self, player: LoveLetterPlayer, reason: LOVE_LETTER_DISCARD_REASON, card: LOVE_LETTER_PLAYER_CARD = LOVE_LETTER_PLAYER_CARD.PLAYER_CARD):
        LoveLetterTask.__init__(self)

        self._card = card
        self._player = player
        self._reason = reason
    
    def get_effective_player(self) -> LoveLetterPlayer:
        return self._player
    
    def get_reason(self) -> LOVE_LETTER_DISCARD_REASON:
        return self._reason
    
    def get_card(self) -> LOVE_LETTER_PLAYER_CARD:
        return self._card
