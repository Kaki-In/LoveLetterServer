from love_letter.base_struct.interaction import *
from love_letter.board import *
from love_letter.enum import *

class LoveLetterChoosePlayerInteraction(LoveLetterClientInteraction):
    def __init__(self, player: LoveLetterPlayer, reason: LOVE_LETTER_CHOOSE_PLAYER_REASON):
        super().__init__('players.choose', {
            'reason': reason,
            'player': player
        })

        self._player = player
        self._reason = reason
    
    def get_reason(self) -> LOVE_LETTER_CHOOSE_PLAYER_REASON:
        return self._reason
    
    def get_effective_player(self) -> LoveLetterPlayer:
        return self._player

