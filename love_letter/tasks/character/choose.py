from love_letter.base_struct.task import *
from love_letter.states import *
from love_letter.enum import *

class LoveLetterChooseCharacterTask(LoveLetterTask):
    def __init__(self, player: LoveLetterPlayer, player_state: LoveLetterNeedingCharacterState, reason: LOVE_LETTER_CHOOSE_CHARACTER_REASON):
        LoveLetterTask.__init__(self)

        self._player = player
        self._state = player_state
        self._reason = reason

    def get_effective_player(self) -> LoveLetterPlayer:
        return self._player
    
    def get_chosen_character_state(self) -> LoveLetterNeedingCharacterState:
        return self._state

    def get_reason(self) -> LOVE_LETTER_CHOOSE_CHARACTER_REASON:
        return self._reason


