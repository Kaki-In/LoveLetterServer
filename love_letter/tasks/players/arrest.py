from love_letter.base_struct.task import *
from love_letter.states import *

class LoveLetterArrestPlayerTask(LoveLetterTask):
    def __init__(self, player: LoveLetterPlayer, player_state: LoveLetterNeedingPlayerState, character_state: LoveLetterNeedingCharacterState):
        LoveLetterTask.__init__(self)

        self._player = player
        self._player_state = player_state
        self._character_state = character_state

    def get_effective_player(self) -> LoveLetterPlayer:
        return self._player
    
    def get_player_state(self) -> LoveLetterNeedingPlayerState:
        return self._player_state
    
    def get_character_state(self) -> LoveLetterNeedingCharacterState:
        return self._character_state


