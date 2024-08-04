from .task import *

from ...objects.context.board import *
from ...enum import *

class LoveLetterDiscardTask(LoveLetterTask):
    def __init__(self, player: LoveLetterPlayer, card: LOVE_LETTER_PLAYER_CARD, reason: LOVE_LETTER_DISCARD_REASON):
        super().__init__()

        self._player = player
        self._card = card
        self._reason = reason
    
    def get_effective_player(self) -> LoveLetterPlayer:
        return self._player
    
    def get_card(self) -> LOVE_LETTER_PLAYER_CARD:
        return self._card
    
    def get_reason(self) -> LOVE_LETTER_DISCARD_REASON:
        return self._reason
