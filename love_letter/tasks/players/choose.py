from love_letter.enum import *
from love_letter.base_struct.task import *
from love_letter.board import *
from love_letter.states import *

class LoveLetterChoosePlayerTask(LoveLetterTask):
    def __init__(self, player: LoveLetterPlayer, player_state: LoveLetterNeedingPlayerState, reason: LOVE_LETTER_CHOOSE_PLAYER_REASON):
        super().__init__()

        self._player = player
        self._player_state = player_state
        self._reason = reason
    
    def get_effective_player(self) -> LoveLetterPlayer:
        return self._player
    
    def get_chosen_player_state(self) -> LoveLetterNeedingPlayerState:
        return self._player_state
    
    def get_reason(self) -> LOVE_LETTER_CHOOSE_PLAYER_REASON:
        return self._reason

